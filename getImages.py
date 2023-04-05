import serial
import sys
import ctypes
import mil as MIL
import PIL.Image as Image
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp
import os
import datetime

"""
This part of the code that contains GetSpeed(), GetPath(), SetFrequency() and SerialCommand(),
is responsible for getting the required inputs and from them give the related input to the camera
through serial connection
"""


def GetSpeed():
    speed = float(input("Enter the speed [m/s], must be a value between [6.35e-4, 6.91] : \n"))
    if speed < 6.35e-4 or speed > 6.91:
        print(f"{speed} is out of the desired range!")
        return GetSpeed()
    else:
        return speed*1000 # return the speed in mm/s, as referenced in the manual

def GetPath():
    path = input("Enter the saving path (if it does not exist, it will be created): \n")
    return path

def SetFrequency(speed):
    # f [Hz] = speed [mm/s] / pixel size [mm]
    frequency = speed/0.0635
    frequencyCommand = "F"+str(int(frequency/10.0))
    return frequencyCommand
    


def SerialCommand(speed):
    global PATH
    PATH = GetPath()
    frequency = SetFrequency(speed)
    frequencyCommand = frequency + "\r"
    print(frequencyCommand)
    # set the parameters for the serial connection
    port = 'COM4'
    baudrate = 9600
    timeout = 1
    bytesize = serial.EIGHTBITS 
    parity = serial.PARITY_NONE 
    stopbits = serial.STOPBITS_ONE 

    # create the serial connection
    ser = serial.Serial(port=port, baudrate=baudrate, 
                        bytesize=bytesize, parity=parity, 
                        stopbits=stopbits, timeout=timeout)


    try:
        # the parenthesis around the wanted command is important, otherwise it wont work
        # ser.write(("M0\r").encode())
        ser.write((frequencyCommand).encode())
        response = ser.readline()
        print(response)

    except serial.SerialException as e:
        print('Error communicating with camera:', e)

    finally:
        # close the serial connection
        ser.close()





""" 
This part of the code containing GrabImages(), HookDataStruct and ProcessingFunction()
is related to grabing, processing and saving the images from the camera
"""

BUFFERING_SIZE_MAX = 5

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
    print("Press <Enter> to start processing.")
    print(input())


    # interrupt continuous grabbing
    MIL.MdigHalt(MilDigitizer)


    MilGrabBufferList = (MIL.MIL_ID * BUFFERING_SIZE_MAX)()
    MilGrabBufferListSize = 0
    dimensionA = MIL.MdigInquire(MilDigitizer, MIL.M_SIZE_X, MIL.M_NULL)
    dimensionB = MIL.MdigInquire(MilDigitizer, MIL.M_SIZE_Y, MIL.M_NULL)

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
       


    if StopProcess():
        return -1

    MIL.MdigProcess(MilDigitizer, 
                    MilGrabBufferList, 
                    MilGrabBufferListSize,
                    MIL.M_STOP, 
                    MIL.M_DEFAULT,  
                    ProcessingFunctionPtr, 
                    ctypes.byref(UserHookData))    


    for id in range(MilGrabBufferListSize):
        MIL.MbufFree(MilGrabBufferList[id])





    # Release defaults.
    MIL.MbufFree(MilBuff)
    MIL.MdispFree(MilDisplay)
    MIL.MdigFree(MilDigitizer)
    MIL.MsysFree(MilSystem)
    MIL.MappFree(MilApplication)
    print("Acquisition has ended!")
    return 


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
        # process_display_image(img, UserData.ProcessedImageCount)
        
        # Save the complete image
        basename = f"image{UserData.ProcessedImageCount}_"
        SaveImage(img, basename)
        
        # In case you just want to check if the images are being correctly grabbed and stop the acquisition
        # if UserData.ProcessedImageCount == 1: 
        #     sys.exit()

    else:
        print('ModifiedBufferId is M_NULL')

    return 0


""""
save images with an "id"(basename) and a timestamp:
imageID_year-month-day_hour-minute-second.png
"""
def SaveImage(img, basename):
    extension = "png"
    output_dir = PATH
    timestamp = basename + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    img.save(os.path.join(output_dir, f"{timestamp}.{extension}"))



"""both of the display_image functions are just to check if the 
   image is being correctly grabbed"""

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


def StopProcess():
    return input("Press <Enter> to stop the process. \n")



if __name__ == "__main__":
    SerialCommand(GetSpeed())
    GrabImages()
