from __future__ import print_function
import serial.tools.list_ports as port_list
import sys
import ctypes
import mil as MIL
import PIL.Image as Image
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp

BUFFERING_SIZE_MAX = 5
SPEED = input("Enter the speed: \n")
PATH = input("Enter the saving path: \n")


def GrabImages():
    # allocate all the necessary stuff: application, system, display, digitizer and buffer
    MilApplication = MIL.MappAlloc(MIL.MIL_TEXT("M_DEFAULT"), MIL.M_DEFAULT, None)
    MilSystem = MIL.MsysAlloc(MIL.M_DEFAULT , MIL.M_SYSTEM_DEFAULT , MIL.M_DEFAULT, MIL.M_DEFAULT , None)
    MilDisplay = MIL.MdispAlloc(MilSystem, MIL.M_DEFAULT, MIL.MIL_TEXT("M_DEFAULT"), MIL.M_DEFAULT, None)
    MilDigitizer = MIL.MdigAlloc(MilSystem, MIL.M_DEFAULT , MIL.MIL_TEXT(r"C:\Users\lsk-fm\Downloads\FFBZeichelkamera.dcf"), MIL.M_DEFAULT, None)
    MilBuff = MIL.MbufAllocDefault(MilSystem, MilDigitizer, MIL.M_GRAB,MIL.M_DEFAULT, MIL.M_DEFAULT, None)
   

    # grab continuously and wait for key press
    MIL.MdigGrabContinuous(MilDigitizer, MilBuff)
    print("Live acquisition in progress...")
    print("Press <Enter> to start processing.\n")
    print(input())


    # interrupt continuous grabbing
    MIL.MdigHalt(MilDigitizer)


    MilGrabBufferList = (MIL.MIL_ID * BUFFERING_SIZE_MAX)()
    MilGrabBufferListSize = 0
    dimensionA = MIL.MdigInquire(MilDigitizer, MIL.M_SIZE_X, MIL.M_NULL)
    dimensionB = MIL.MdigInquire(MilDigitizer, MIL.M_SIZE_Y, MIL.M_NULL)
    print(dimensionA,'dimA')
    print(dimensionB,'dimB')

    for n in range(BUFFERING_SIZE_MAX):
        MilGrabBufferList[n] =  MIL.MbufAlloc2d(MilSystem, 
                                                dimensionA,
                                                dimensionB,
                                                16 + MIL.M_UNSIGNED,
                                                MIL.M_IMAGE + MIL.M_GRAB + MIL.M_PROC,
                                                None)

        if MilGrabBufferList[n]:
            MIL.MbufClear(MilGrabBufferList[n], 0xFF)
            MilGrabBufferListSize += 1
        else:
            break


    UserHookData = HookDataStruct(MilDigitizer, MilBuff, 0)
    ProcessingFunctionPtr = MIL.MIL_DIG_HOOK_FUNCTION_PTR(ProcessingFunction)


    MIL.MdigProcess(MilDigitizer, 
                    MilGrabBufferList, 
                    MilGrabBufferListSize,
                    MIL.M_START, 
                    MIL.M_DEFAULT,  
                    ProcessingFunctionPtr, 
                    ctypes.byref(UserHookData))
       



    print("Press <Enter> to stop.                    \n\n")
    print(input())

    MIL.MdigProcess(MilDigitizer, 
                    MilGrabBufferList, 
                    MilGrabBufferListSize,
                    MIL.M_STOP, 
                    MIL.M_DEFAULT,  
                    ProcessingFunctionPtr, 
                    ctypes.byref(UserHookData))    


    for id in range(MilGrabBufferListSize):
        print('ola')
        MIL.MbufFree(MilGrabBufferList[id])

    print('end')



    # Release defaults.
    MIL.MbufFree(MilBuff)
    MIL.MdispFree(MilDisplay)
    MIL.MdigFree(MilDigitizer)
    MIL.MsysFree(MilSystem)
    MIL.MappFree(MilApplication)
   
    return 





"""both of the display_image functions are just for checking if the 
   image is being correctly grabbed,"""

def display_image(img):
    plt.imshow(img, cmap='gray')
    plt.show()

def process_display_image(img, img_count):
    if img_count == 1:
        p = mp.Process(target=display_image, args=(img,))
        p.start()
        p.join()
    else:
        pass



class HookDataStruct(ctypes.Structure):
    _fields_ = [("MilDigitizer", MIL.MIL_ID),
                ("MilContainerDisp", MIL.MIL_ID),
                ("ProcessedImageCount", MIL.MIL_INT)]

def ProcessingFunction(HookType, HookId, HookDataPtr):
    
    # Define the local buffer
    localBuffer = ((8192 * 1024) * ctypes.c_ushort)()
    
    # Retrieve the MIL_ID of the grabbed buffer.
    ModifiedBufferId = MIL.MIL_ID(0)
    MIL.MdigGetHookInfo(HookId, MIL.M_MODIFIED_BUFFER + MIL.M_BUFFER_ID, ctypes.byref(ModifiedBufferId))

    if ModifiedBufferId != MIL.M_NULL:
        # Extract the userdata structure
        UserData = ctypes.cast(ctypes.c_void_p(HookDataPtr), ctypes.POINTER(HookDataStruct)).contents

        # Increment the frame counter.
        UserData.ProcessedImageCount += 1

        # Print and draw the frame count (remove to reduce CPU usage).
        print("Processing frame #{:d}.\r".format(UserData.ProcessedImageCount), end='')

        MIL.MbufGet(ModifiedBufferId, localBuffer)

        # Convert the buffer to an image
        img_buf = np.ctypeslib.as_array(localBuffer, shape=(8192, 1024))
        img = Image.fromarray(img_buf.reshape((1024, 8192)).astype(np.uint8))
        process_display_image(img, UserData.ProcessedImageCount)
        
        # Save the complete image
        output_dir = "output"
        basename = f"image{UserData.ProcessedImageCount}"
        extension = "png"
        # img.save(f"{output_dir}/{basename}.{extension}")
        
        # In case you just want to check if the images are being correctly grabbed and stop the acquisition
        # if UserData.ProcessedImageCount == 1: 
        #     sys.exit()

    else:
        print('ModifiedBufferId is M_NULL')

    return 0



if __name__ == "__main__":
    GrabImages()
