#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################
#
#
# Filename     :  MIL.PY
# Revision     :  10.40.0881
# Content      :  This file contains the defines necessary to use the
#              :  Matrox Imaging Library "Python" user interface.
#
# Comments     :  Some defines may be here but not yet
#                 implemented in the library.
#
# This file has been tested with Python 3.4 and Python 2.7
#
# This file is to be used with a 64-bit MIL installation
#
# Copyright © Matrox Electronic Systems Ltd., 1992-2021.
# All Rights Reserved
##########################################################################


import os.path
import ctypes

try:
   MIL = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'mil.dll'))
except:
   MIL = None
try:
   MILSTR = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'milstr.dll'))
except:
   MILSTR = None
try:
   MILREG = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'milreg.dll'))
except:
   MILREG = None
try:
   MILPAT = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'milpat.dll'))
except:
   MILPAT = None
try:
   MILOCR = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'milocr.dll'))
except:
   MILOCR = None
try:
   MILMOD = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'milmod.dll'))
except:
   MILMOD = None
try:
   MILMETROL = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'milmetrol.dll'))
except:
   MILMETROL = None
try:
   MILMEAS = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'milmeas.dll'))
except:
   MILMEAS = None
try:
   MILIM = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'milim.dll'))
except:
   MILIM = None
try:
   MILFPGA = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'milfpga.dll'))
except:
   MILFPGA = None
try:
   MILEDGE = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'miledge.dll'))
except:
   MILEDGE = None
try:
   MILDMR = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'mildmr.dll'))
except:
   MILDMR = None
try:
   MILCOM = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'milcom.dll'))
except:
   MILCOM = None
try:
   MILCOLOR = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'milcolor.dll'))
except:
   MILCOLOR = None
try:
   MILCODE = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'milcode.dll'))
except:
   MILCODE = None
try:
   MILCLASS = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'milclass.dll'))
except:
   MILCLASS = None
try:
   MILCAL = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'milcal.dll'))
except:
   MILCAL = None
try:
   MIL3D = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'mil3d.dll'))
except:
   MIL3D = None
try:
   MILBLOB = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'milblob.dll'))
except:
   MILBLOB = None
try:
   MILBEAD = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'milbead.dll'))
except:
   MILBEAD = None
try:
   MIL3DREG = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'mil3dreg.dll'))
except:
   MIL3DREG = None
try:
   MIL3DMET = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'mil3dmet.dll'))
except:
   MIL3DMET = None
try:
   MIL3DMAP = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'mil3dmap.dll'))
except:
   MIL3DMAP = None
try:
   MIL3DIM = ctypes.windll.LoadLibrary(os.path.join(os.environ['MIL_PATH64'], 'mil3dim.dll'))
except:
   MIL3DIM = None

MIL_APP_HOOK_FUNCTION_PTR = ctypes.WINFUNCTYPE(ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p)
MIL_BUF_HOOK_FUNCTION_PTR = ctypes.WINFUNCTYPE(ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p)
MIL_CLASS_HOOK_FUNCTION_PTR = ctypes.WINFUNCTYPE(ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p)
MIL_FOCUS_HOOK_FUNCTION_PTR = ctypes.WINFUNCTYPE(ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p)
MIL_DIG_HOOK_FUNCTION_PTR = ctypes.WINFUNCTYPE(ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p)
MIL_DISP_HOOK_FUNCTION_PTR = ctypes.WINFUNCTYPE(ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p)
MIL_FPGA_HOOK_FUNCTION_PTR = ctypes.WINFUNCTYPE(ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p)
MIL_FUNC_FUNCTION_PTR = ctypes.WINFUNCTYPE(None, ctypes.c_longlong)
MIL_GRA_HOOK_FUNCTION_PTR = ctypes.WINFUNCTYPE(ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p)
MIL_OBJ_HOOK_FUNCTION_PTR = ctypes.WINFUNCTYPE(ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p)
MIL_OCR_HOOK_FUNCTION_PTR = ctypes.WINFUNCTYPE(ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_void_p)
MIL_SEQ_HOOK_FUNCTION_PTR = ctypes.WINFUNCTYPE(ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p)
MIL_SYS_HOOK_FUNCTION_PTR = ctypes.WINFUNCTYPE(ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p)
MIL_THREAD_FUNCTION_PTR = ctypes.WINFUNCTYPE(ctypes.c_ulong, ctypes.c_void_p)
MFPGAHOOKFCTPTR = ctypes.WINFUNCTYPE(ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p)
MFUNCFCTPTR = ctypes.WINFUNCTYPE(None, ctypes.c_longlong)
MTHREADFCTPTR = ctypes.WINFUNCTYPE(ctypes.c_ulong, ctypes.c_void_p)

MIL_ID = ctypes.c_longlong
MIL_INT = ctypes.c_longlong

class MIL_UUID(ctypes.Structure):
   _fields_ = [("bytes", ctypes.c_ubyte*16)]

if MIL3D is not None:
   try:
      MIL3D.M3ddispAllocW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_void_p]
      MIL3D.M3ddispAllocW.restype = ctypes.c_longlong
      M3ddispAllocW = MIL3D.M3ddispAllocW
   except:
      M3ddispAllocW = None
if MIL3D is not None:
   try:
      MIL3D.M3ddispControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL3D.M3ddispControlDouble.restype = None
      M3ddispControlDouble = MIL3D.M3ddispControlDouble
   except:
      M3ddispControlDouble = None
if MIL3D is not None:
   try:
      MIL3D.M3ddispControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3ddispControlInt64.restype = None
      M3ddispControlInt64 = MIL3D.M3ddispControlInt64
   except:
      M3ddispControlInt64 = None
if MIL3D is not None:
   try:
      MIL3D.M3ddispCopy.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3ddispCopy.restype = None
      M3ddispCopy = MIL3D.M3ddispCopy
   except:
      M3ddispCopy = None
if MIL3D is not None:
   try:
      MIL3D.M3ddispFree.argtypes = [ctypes.c_longlong]
      MIL3D.M3ddispFree.restype = None
      M3ddispFree = MIL3D.M3ddispFree
   except:
      M3ddispFree = None
if MIL3D is not None:
   try:
      MIL3D.M3ddispGetView.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MIL3D.M3ddispGetView.restype = None
      M3ddispGetView = MIL3D.M3ddispGetView
   except:
      M3ddispGetView = None
if MIL3D is not None:
   try:
      MIL3D.M3ddispInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3D.M3ddispInquire.restype = ctypes.c_longlong
      M3ddispInquire = MIL3D.M3ddispInquire
   except:
      M3ddispInquire = None
if MIL3D is not None:
   try:
      MIL3D.M3ddispSelect.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3ddispSelect.restype = ctypes.c_longlong
      M3ddispSelect = MIL3D.M3ddispSelect
   except:
      M3ddispSelect = None
if MIL3D is not None:
   try:
      MIL3D.M3ddispSelectWindow.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3ddispSelectWindow.restype = ctypes.c_longlong
      M3ddispSelectWindow = MIL3D.M3ddispSelectWindow
   except:
      M3ddispSelectWindow = None
if MIL3D is not None:
   try:
      MIL3D.M3ddispSetViewDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3D.M3ddispSetViewDouble.restype = None
      M3ddispSetViewDouble = MIL3D.M3ddispSetViewDouble
   except:
      M3ddispSetViewDouble = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3D.M3dgeoAlloc.restype = ctypes.c_longlong
      M3dgeoAlloc = MIL3D.M3dgeoAlloc
   except:
      M3dgeoAlloc = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoBox.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3D.M3dgeoBox.restype = None
      M3dgeoBox = MIL3D.M3dgeoBox
   except:
      M3dgeoBox = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoCopy.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3dgeoCopy.restype = None
      M3dgeoCopy = MIL3D.M3dgeoCopy
   except:
      M3dgeoCopy = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoCylinder.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3D.M3dgeoCylinder.restype = None
      M3dgeoCylinder = MIL3D.M3dgeoCylinder
   except:
      M3dgeoCylinder = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoDraw3d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3dgeoDraw3d.restype = ctypes.c_longlong
      M3dgeoDraw3d = MIL3D.M3dgeoDraw3d
   except:
      M3dgeoDraw3d = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoFree.argtypes = [ctypes.c_longlong]
      MIL3D.M3dgeoFree.restype = None
      M3dgeoFree = MIL3D.M3dgeoFree
   except:
      M3dgeoFree = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3D.M3dgeoInquire.restype = ctypes.c_double
      M3dgeoInquire = MIL3D.M3dgeoInquire
   except:
      M3dgeoInquire = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoLine.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3D.M3dgeoLine.restype = None
      M3dgeoLine = MIL3D.M3dgeoLine
   except:
      M3dgeoLine = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoMatrixGetDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double)]
      MIL3D.M3dgeoMatrixGetDouble.restype = None
      M3dgeoMatrixGetDouble = MIL3D.M3dgeoMatrixGetDouble
   except:
      M3dgeoMatrixGetDouble = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoMatrixGetFloat.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_float)]
      MIL3D.M3dgeoMatrixGetFloat.restype = None
      M3dgeoMatrixGetFloat = MIL3D.M3dgeoMatrixGetFloat
   except:
      M3dgeoMatrixGetFloat = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoMatrixGetTransform.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_longlong]
      MIL3D.M3dgeoMatrixGetTransform.restype = None
      M3dgeoMatrixGetTransform = MIL3D.M3dgeoMatrixGetTransform
   except:
      M3dgeoMatrixGetTransform = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoMatrixPutDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double)]
      MIL3D.M3dgeoMatrixPutDouble.restype = None
      M3dgeoMatrixPutDouble = MIL3D.M3dgeoMatrixPutDouble
   except:
      M3dgeoMatrixPutDouble = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoMatrixPutFloat.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_float)]
      MIL3D.M3dgeoMatrixPutFloat.restype = None
      M3dgeoMatrixPutFloat = MIL3D.M3dgeoMatrixPutFloat
   except:
      M3dgeoMatrixPutFloat = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoMatrixSetTransformDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3D.M3dgeoMatrixSetTransformDouble.restype = None
      M3dgeoMatrixSetTransformDouble = MIL3D.M3dgeoMatrixSetTransformDouble
   except:
      M3dgeoMatrixSetTransformDouble = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoMatrixSetWithAxes.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3D.M3dgeoMatrixSetWithAxes.restype = None
      M3dgeoMatrixSetWithAxes = MIL3D.M3dgeoMatrixSetWithAxes
   except:
      M3dgeoMatrixSetWithAxes = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoPlane.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3D.M3dgeoPlane.restype = None
      M3dgeoPlane = MIL3D.M3dgeoPlane
   except:
      M3dgeoPlane = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoRestoreW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL3D.M3dgeoRestoreW.restype = ctypes.c_longlong
      M3dgeoRestoreW = MIL3D.M3dgeoRestoreW
   except:
      M3dgeoRestoreW = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3dgeoSaveW.restype = None
      M3dgeoSaveW = MIL3D.M3dgeoSaveW
   except:
      M3dgeoSaveW = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoSphere.argtypes = [ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3D.M3dgeoSphere.restype = None
      M3dgeoSphere = MIL3D.M3dgeoSphere
   except:
      M3dgeoSphere = None
if MIL3D is not None:
   try:
      MIL3D.M3dgeoStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MIL3D.M3dgeoStreamW.restype = None
      M3dgeoStreamW = MIL3D.M3dgeoStreamW
   except:
      M3dgeoStreamW = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraAdd.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3dgraAdd.restype = ctypes.c_longlong
      M3dgraAdd = MIL3D.M3dgraAdd
   except:
      M3dgraAdd = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3D.M3dgraAlloc.restype = ctypes.c_longlong
      M3dgraAlloc = MIL3D.M3dgraAlloc
   except:
      M3dgraAlloc = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraArc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3D.M3dgraArc.restype = ctypes.c_longlong
      M3dgraArc = MIL3D.M3dgraArc
   except:
      M3dgraArc = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraAxisW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3dgraAxisW.restype = ctypes.c_longlong
      M3dgraAxisW = MIL3D.M3dgraAxisW
   except:
      M3dgraAxisW = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraBox.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3dgraBox.restype = ctypes.c_longlong
      M3dgraBox = MIL3D.M3dgraBox
   except:
      M3dgraBox = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL3D.M3dgraControlDouble.restype = None
      M3dgraControlDouble = MIL3D.M3dgraControlDouble
   except:
      M3dgraControlDouble = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3dgraControlInt64.restype = None
      M3dgraControlInt64 = MIL3D.M3dgraControlInt64
   except:
      M3dgraControlInt64 = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraCopy.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3dgraCopy.restype = ctypes.c_longlong
      M3dgraCopy = MIL3D.M3dgraCopy
   except:
      M3dgraCopy = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraCylinder.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3D.M3dgraCylinder.restype = ctypes.c_longlong
      M3dgraCylinder = MIL3D.M3dgraCylinder
   except:
      M3dgraCylinder = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraDotsDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MIL3D.M3dgraDotsDouble.restype = ctypes.c_longlong
      M3dgraDotsDouble = MIL3D.M3dgraDotsDouble
   except:
      M3dgraDotsDouble = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraDotsFloat.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MIL3D.M3dgraDotsFloat.restype = ctypes.c_longlong
      M3dgraDotsFloat = MIL3D.M3dgraDotsFloat
   except:
      M3dgraDotsFloat = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraFree.argtypes = [ctypes.c_longlong]
      MIL3D.M3dgraFree.restype = None
      M3dgraFree = MIL3D.M3dgraFree
   except:
      M3dgraFree = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraGrid.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3D.M3dgraGrid.restype = ctypes.c_longlong
      M3dgraGrid = MIL3D.M3dgraGrid
   except:
      M3dgraGrid = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3D.M3dgraInquire.restype = ctypes.c_longlong
      M3dgraInquire = MIL3D.M3dgraInquire
   except:
      M3dgraInquire = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraLine.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3D.M3dgraLine.restype = ctypes.c_longlong
      M3dgraLine = MIL3D.M3dgraLine
   except:
      M3dgraLine = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraNode.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3dgraNode.restype = ctypes.c_longlong
      M3dgraNode = MIL3D.M3dgraNode
   except:
      M3dgraNode = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraPlane.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3D.M3dgraPlane.restype = ctypes.c_longlong
      M3dgraPlane = MIL3D.M3dgraPlane
   except:
      M3dgraPlane = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraPolygonDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3dgraPolygonDouble.restype = ctypes.c_longlong
      M3dgraPolygonDouble = MIL3D.M3dgraPolygonDouble
   except:
      M3dgraPolygonDouble = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraPolygonFloat.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3dgraPolygonFloat.restype = ctypes.c_longlong
      M3dgraPolygonFloat = MIL3D.M3dgraPolygonFloat
   except:
      M3dgraPolygonFloat = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraRemove.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3dgraRemove.restype = None
      M3dgraRemove = MIL3D.M3dgraRemove
   except:
      M3dgraRemove = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraSphere.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3D.M3dgraSphere.restype = ctypes.c_longlong
      M3dgraSphere = MIL3D.M3dgraSphere
   except:
      M3dgraSphere = None
if MIL3D is not None:
   try:
      MIL3D.M3dgraTextW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.M3dgraTextW.restype = ctypes.c_longlong
      M3dgraTextW = MIL3D.M3dgraTextW
   except:
      M3dgraTextW = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3DIM.M3dimAlloc.restype = ctypes.c_longlong
      M3dimAlloc = MIL3DIM.M3dimAlloc
   except:
      M3dimAlloc = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3DIM.M3dimAllocResult.restype = ctypes.c_longlong
      M3dimAllocResult = MIL3DIM.M3dimAllocResult
   except:
      M3dimAllocResult = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimArith.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DIM.M3dimArith.restype = None
      M3dimArith = MIL3DIM.M3dimArith
   except:
      M3dimArith = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimCalculateMapSize.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.POINTER(ctypes.c_longlong)]
      MIL3DIM.M3dimCalculateMapSize.restype = None
      M3dimCalculateMapSize = MIL3DIM.M3dimCalculateMapSize
   except:
      M3dimCalculateMapSize = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimCalibrateDepthMap.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DIM.M3dimCalibrateDepthMap.restype = None
      M3dimCalibrateDepthMap = MIL3DIM.M3dimCalibrateDepthMap
   except:
      M3dimCalibrateDepthMap = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL3DIM.M3dimControlDouble.restype = None
      M3dimControlDouble = MIL3DIM.M3dimControlDouble
   except:
      M3dimControlDouble = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DIM.M3dimControlInt64.restype = None
      M3dimControlInt64 = MIL3DIM.M3dimControlInt64
   except:
      M3dimControlInt64 = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimCopy.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DIM.M3dimCopy.restype = None
      M3dimCopy = MIL3DIM.M3dimCopy
   except:
      M3dimCopy = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimCopyResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DIM.M3dimCopyResult.restype = None
      M3dimCopyResult = MIL3DIM.M3dimCopyResult
   except:
      M3dimCopyResult = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimCrop.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DIM.M3dimCrop.restype = None
      M3dimCrop = MIL3DIM.M3dimCrop
   except:
      M3dimCrop = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimFillGaps.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DIM.M3dimFillGaps.restype = None
      M3dimFillGaps = MIL3DIM.M3dimFillGaps
   except:
      M3dimFillGaps = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimFree.argtypes = [ctypes.c_longlong]
      MIL3DIM.M3dimFree.restype = None
      M3dimFree = MIL3DIM.M3dimFree
   except:
      M3dimFree = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimGetResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3DIM.M3dimGetResult.restype = ctypes.c_double
      M3dimGetResult = MIL3DIM.M3dimGetResult
   except:
      M3dimGetResult = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3DIM.M3dimInquire.restype = ctypes.c_longlong
      M3dimInquire = MIL3DIM.M3dimInquire
   except:
      M3dimInquire = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimMatrixTransform.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DIM.M3dimMatrixTransform.restype = None
      M3dimMatrixTransform = MIL3DIM.M3dimMatrixTransform
   except:
      M3dimMatrixTransform = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimMatrixTransformListDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_longlong]
      MIL3DIM.M3dimMatrixTransformListDouble.restype = None
      M3dimMatrixTransformListDouble = MIL3DIM.M3dimMatrixTransformListDouble
   except:
      M3dimMatrixTransformListDouble = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimMatrixTransformListFloat.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.c_longlong]
      MIL3DIM.M3dimMatrixTransformListFloat.restype = None
      M3dimMatrixTransformListFloat = MIL3DIM.M3dimMatrixTransformListFloat
   except:
      M3dimMatrixTransformListFloat = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimMerge.argtypes = [ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DIM.M3dimMerge.restype = None
      M3dimMerge = MIL3DIM.M3dimMerge
   except:
      M3dimMerge = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimMesh.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DIM.M3dimMesh.restype = None
      M3dimMesh = MIL3DIM.M3dimMesh
   except:
      M3dimMesh = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimNormals.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DIM.M3dimNormals.restype = None
      M3dimNormals = MIL3DIM.M3dimNormals
   except:
      M3dimNormals = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimProfile.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3DIM.M3dimProfile.restype = None
      M3dimProfile = MIL3DIM.M3dimProfile
   except:
      M3dimProfile = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimProject.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DIM.M3dimProject.restype = None
      M3dimProject = MIL3DIM.M3dimProject
   except:
      M3dimProject = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimRemovePoints.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DIM.M3dimRemovePoints.restype = None
      M3dimRemovePoints = MIL3DIM.M3dimRemovePoints
   except:
      M3dimRemovePoints = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimRestoreW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL3DIM.M3dimRestoreW.restype = ctypes.c_longlong
      M3dimRestoreW = MIL3DIM.M3dimRestoreW
   except:
      M3dimRestoreW = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimRotate.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3DIM.M3dimRotate.restype = None
      M3dimRotate = MIL3DIM.M3dimRotate
   except:
      M3dimRotate = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimSample.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DIM.M3dimSample.restype = None
      M3dimSample = MIL3DIM.M3dimSample
   except:
      M3dimSample = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DIM.M3dimSaveW.restype = None
      M3dimSaveW = MIL3DIM.M3dimSaveW
   except:
      M3dimSaveW = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimScale.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3DIM.M3dimScale.restype = None
      M3dimScale = MIL3DIM.M3dimScale
   except:
      M3dimScale = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimStat.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DIM.M3dimStat.restype = None
      M3dimStat = MIL3DIM.M3dimStat
   except:
      M3dimStat = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MIL3DIM.M3dimStreamW.restype = None
      M3dimStreamW = MIL3DIM.M3dimStreamW
   except:
      M3dimStreamW = None
if MIL3DIM is not None:
   try:
      MIL3DIM.M3dimTranslate.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3DIM.M3dimTranslate.restype = None
      M3dimTranslate = MIL3DIM.M3dimTranslate
   except:
      M3dimTranslate = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapAddScan.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DMAP.M3dmapAddScan.restype = None
      M3dmapAddScan = MIL3DMAP.M3dmapAddScan
   except:
      M3dmapAddScan = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3DMAP.M3dmapAlloc.restype = ctypes.c_longlong
      M3dmapAlloc = MIL3DMAP.M3dmapAlloc
   except:
      M3dmapAlloc = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3DMAP.M3dmapAllocResult.restype = ctypes.c_longlong
      M3dmapAllocResult = MIL3DMAP.M3dmapAllocResult
   except:
      M3dmapAllocResult = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapCalibrate.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DMAP.M3dmapCalibrate.restype = None
      M3dmapCalibrate = MIL3DMAP.M3dmapCalibrate
   except:
      M3dmapCalibrate = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapCalibrateMultiple.argtypes = [ctypes.POINTER(ctypes.c_longlong), ctypes.POINTER(ctypes.c_longlong), ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_longlong]
      MIL3DMAP.M3dmapCalibrateMultiple.restype = None
      M3dmapCalibrateMultiple = MIL3DMAP.M3dmapCalibrateMultiple
   except:
      M3dmapCalibrateMultiple = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapClear.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DMAP.M3dmapClear.restype = None
      M3dmapClear = MIL3DMAP.M3dmapClear
   except:
      M3dmapClear = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL3DMAP.M3dmapControlDouble.restype = None
      M3dmapControlDouble = MIL3DMAP.M3dmapControlDouble
   except:
      M3dmapControlDouble = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DMAP.M3dmapControlInt64.restype = None
      M3dmapControlInt64 = MIL3DMAP.M3dmapControlInt64
   except:
      M3dmapControlInt64 = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapCopy.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DMAP.M3dmapCopy.restype = None
      M3dmapCopy = MIL3DMAP.M3dmapCopy
   except:
      M3dmapCopy = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapCopyResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DMAP.M3dmapCopyResult.restype = None
      M3dmapCopyResult = MIL3DMAP.M3dmapCopyResult
   except:
      M3dmapCopyResult = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapDraw.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DMAP.M3dmapDraw.restype = None
      M3dmapDraw = MIL3DMAP.M3dmapDraw
   except:
      M3dmapDraw = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapDraw3d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DMAP.M3dmapDraw3d.restype = ctypes.c_longlong
      M3dmapDraw3d = MIL3DMAP.M3dmapDraw3d
   except:
      M3dmapDraw3d = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapFree.argtypes = [ctypes.c_longlong]
      MIL3DMAP.M3dmapFree.restype = None
      M3dmapFree = MIL3DMAP.M3dmapFree
   except:
      M3dmapFree = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapGetResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3DMAP.M3dmapGetResult.restype = None
      M3dmapGetResult = MIL3DMAP.M3dmapGetResult
   except:
      M3dmapGetResult = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3DMAP.M3dmapInquire.restype = ctypes.c_longlong
      M3dmapInquire = MIL3DMAP.M3dmapInquire
   except:
      M3dmapInquire = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapRestoreW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL3DMAP.M3dmapRestoreW.restype = ctypes.c_longlong
      M3dmapRestoreW = MIL3DMAP.M3dmapRestoreW
   except:
      M3dmapRestoreW = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DMAP.M3dmapSaveW.restype = None
      M3dmapSaveW = MIL3DMAP.M3dmapSaveW
   except:
      M3dmapSaveW = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MIL3DMAP.M3dmapStreamW.restype = None
      M3dmapStreamW = MIL3DMAP.M3dmapStreamW
   except:
      M3dmapStreamW = None
if MIL3DMAP is not None:
   try:
      MIL3DMAP.M3dmapTriangulate.argtypes = [ctypes.POINTER(ctypes.c_longlong), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DMAP.M3dmapTriangulate.restype = None
      M3dmapTriangulate = MIL3DMAP.M3dmapTriangulate
   except:
      M3dmapTriangulate = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3DMET.M3dmetAlloc.restype = ctypes.c_longlong
      M3dmetAlloc = MIL3DMET.M3dmetAlloc
   except:
      M3dmetAlloc = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3DMET.M3dmetAllocResult.restype = ctypes.c_longlong
      M3dmetAllocResult = MIL3DMET.M3dmetAllocResult
   except:
      M3dmetAllocResult = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL3DMET.M3dmetControlDouble.restype = None
      M3dmetControlDouble = MIL3DMET.M3dmetControlDouble
   except:
      M3dmetControlDouble = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DMET.M3dmetControlInt64.restype = None
      M3dmetControlInt64 = MIL3DMET.M3dmetControlInt64
   except:
      M3dmetControlInt64 = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetCopy.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DMET.M3dmetCopy.restype = None
      M3dmetCopy = MIL3DMET.M3dmetCopy
   except:
      M3dmetCopy = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetCopyResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DMET.M3dmetCopyResult.restype = None
      M3dmetCopyResult = MIL3DMET.M3dmetCopyResult
   except:
      M3dmetCopyResult = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetDistance.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong]
      MIL3DMET.M3dmetDistance.restype = None
      M3dmetDistance = MIL3DMET.M3dmetDistance
   except:
      M3dmetDistance = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetDraw3d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DMET.M3dmetDraw3d.restype = ctypes.c_longlong
      M3dmetDraw3d = MIL3DMET.M3dmetDraw3d
   except:
      M3dmetDraw3d = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetFit.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong]
      MIL3DMET.M3dmetFit.restype = None
      M3dmetFit = MIL3DMET.M3dmetFit
   except:
      M3dmetFit = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetFree.argtypes = [ctypes.c_longlong]
      MIL3DMET.M3dmetFree.restype = None
      M3dmetFree = MIL3DMET.M3dmetFree
   except:
      M3dmetFree = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetGetResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3DMET.M3dmetGetResult.restype = ctypes.c_double
      M3dmetGetResult = MIL3DMET.M3dmetGetResult
   except:
      M3dmetGetResult = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3DMET.M3dmetInquire.restype = ctypes.c_longlong
      M3dmetInquire = MIL3DMET.M3dmetInquire
   except:
      M3dmetInquire = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetRestoreW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL3DMET.M3dmetRestoreW.restype = ctypes.c_longlong
      M3dmetRestoreW = MIL3DMET.M3dmetRestoreW
   except:
      M3dmetRestoreW = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DMET.M3dmetSaveW.restype = None
      M3dmetSaveW = MIL3DMET.M3dmetSaveW
   except:
      M3dmetSaveW = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetStat.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL3DMET.M3dmetStat.restype = None
      M3dmetStat = MIL3DMET.M3dmetStat
   except:
      M3dmetStat = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MIL3DMET.M3dmetStreamW.restype = None
      M3dmetStreamW = MIL3DMET.M3dmetStreamW
   except:
      M3dmetStreamW = None
if MIL3DMET is not None:
   try:
      MIL3DMET.M3dmetVolume.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p]
      MIL3DMET.M3dmetVolume.restype = ctypes.c_double
      M3dmetVolume = MIL3DMET.M3dmetVolume
   except:
      M3dmetVolume = None
if MIL3DREG is not None:
   try:
      MIL3DREG.M3dregAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3DREG.M3dregAlloc.restype = ctypes.c_longlong
      M3dregAlloc = MIL3DREG.M3dregAlloc
   except:
      M3dregAlloc = None
if MIL3DREG is not None:
   try:
      MIL3DREG.M3dregAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3DREG.M3dregAllocResult.restype = ctypes.c_longlong
      M3dregAllocResult = MIL3DREG.M3dregAllocResult
   except:
      M3dregAllocResult = None
if MIL3DREG is not None:
   try:
      MIL3DREG.M3dregCalculate.argtypes = [ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DREG.M3dregCalculate.restype = None
      M3dregCalculate = MIL3DREG.M3dregCalculate
   except:
      M3dregCalculate = None
if MIL3DREG is not None:
   try:
      MIL3DREG.M3dregControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL3DREG.M3dregControlDouble.restype = None
      M3dregControlDouble = MIL3DREG.M3dregControlDouble
   except:
      M3dregControlDouble = None
if MIL3DREG is not None:
   try:
      MIL3DREG.M3dregControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DREG.M3dregControlInt64.restype = None
      M3dregControlInt64 = MIL3DREG.M3dregControlInt64
   except:
      M3dregControlInt64 = None
if MIL3DREG is not None:
   try:
      MIL3DREG.M3dregCopy.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DREG.M3dregCopy.restype = None
      M3dregCopy = MIL3DREG.M3dregCopy
   except:
      M3dregCopy = None
if MIL3DREG is not None:
   try:
      MIL3DREG.M3dregCopyResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DREG.M3dregCopyResult.restype = None
      M3dregCopyResult = MIL3DREG.M3dregCopyResult
   except:
      M3dregCopyResult = None
if MIL3DREG is not None:
   try:
      MIL3DREG.M3dregFree.argtypes = [ctypes.c_longlong]
      MIL3DREG.M3dregFree.restype = None
      M3dregFree = MIL3DREG.M3dregFree
   except:
      M3dregFree = None
if MIL3DREG is not None:
   try:
      MIL3DREG.M3dregGetResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3DREG.M3dregGetResult.restype = ctypes.c_double
      M3dregGetResult = MIL3DREG.M3dregGetResult
   except:
      M3dregGetResult = None
if MIL3DREG is not None:
   try:
      MIL3DREG.M3dregInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL3DREG.M3dregInquire.restype = ctypes.c_longlong
      M3dregInquire = MIL3DREG.M3dregInquire
   except:
      M3dregInquire = None
if MIL3DREG is not None:
   try:
      MIL3DREG.M3dregMerge.argtypes = [ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DREG.M3dregMerge.restype = None
      M3dregMerge = MIL3DREG.M3dregMerge
   except:
      M3dregMerge = None
if MIL3DREG is not None:
   try:
      MIL3DREG.M3dregRestoreW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL3DREG.M3dregRestoreW.restype = ctypes.c_longlong
      M3dregRestoreW = MIL3DREG.M3dregRestoreW
   except:
      M3dregRestoreW = None
if MIL3DREG is not None:
   try:
      MIL3DREG.M3dregSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DREG.M3dregSaveW.restype = None
      M3dregSaveW = MIL3DREG.M3dregSaveW
   except:
      M3dregSaveW = None
if MIL3DREG is not None:
   try:
      MIL3DREG.M3dregSetLocation.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3DREG.M3dregSetLocation.restype = None
      M3dregSetLocation = MIL3DREG.M3dregSetLocation
   except:
      M3dregSetLocation = None
if MIL3DREG is not None:
   try:
      MIL3DREG.M3dregStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MIL3DREG.M3dregStreamW.restype = None
      M3dregStreamW = MIL3DREG.M3dregStreamW
   except:
      M3dregStreamW = None
if MIL is not None:
   try:
      MIL.MappAllocW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MappAllocW.restype = ctypes.c_longlong
      MappAllocW = MIL.MappAllocW
   except:
      MappAllocW = None
if MIL is not None:
   try:
      MIL.MappCloseConnection.argtypes = [ctypes.c_longlong]
      MIL.MappCloseConnection.restype = None
      MappCloseConnection = MIL.MappCloseConnection
   except:
      MappCloseConnection = None
if MIL is not None:
   try:
      MIL.MappControl.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MappControl.restype = None
      MappControl = MIL.MappControl
   except:
      MappControl = None
if MIL is not None:
   try:
      MIL.MappControlMp.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MappControlMp.restype = None
      MappControlMp = MIL.MappControlMp
   except:
      MappControlMp = None
if MIL is not None:
   try:
      MIL.MappFileOperationW.argtypes = [ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MappFileOperationW.restype = None
      MappFileOperationW = MIL.MappFileOperationW
   except:
      MappFileOperationW = None
if MIL is not None:
   try:
      MIL.MappFree.argtypes = [ctypes.c_longlong]
      MIL.MappFree.restype = None
      MappFree = MIL.MappFree
   except:
      MappFree = None
if MIL is not None:
   try:
      MIL.MappGetError.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MappGetError.restype = ctypes.c_longlong
      MappGetError = MIL.MappGetError
   except:
      MappGetError = None
if MIL is not None:
   try:
      MIL.MappGetHookInfo.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MappGetHookInfo.restype = ctypes.c_longlong
      MappGetHookInfo = MIL.MappGetHookInfo
   except:
      MappGetHookInfo = None
if MIL is not None:
   try:
      MIL.MappHookFunction.argtypes = [ctypes.c_longlong, ctypes.c_longlong, MIL_APP_HOOK_FUNCTION_PTR, ctypes.c_void_p]
      MIL.MappHookFunction.restype = None
      MappHookFunction = MIL.MappHookFunction
   except:
      MappHookFunction = None
if MIL is not None:
   try:
      MIL.MappInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MappInquire.restype = ctypes.c_longlong
      MappInquire = MIL.MappInquire
   except:
      MappInquire = None
if MIL is not None:
   try:
      MIL.MappInquireConnection.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL.MappInquireConnection.restype = ctypes.c_longlong
      MappInquireConnection = MIL.MappInquireConnection
   except:
      MappInquireConnection = None
if MIL is not None:
   try:
      MIL.MappInquireMp.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MappInquireMp.restype = ctypes.c_longlong
      MappInquireMp = MIL.MappInquireMp
   except:
      MappInquireMp = None
if MIL is not None:
   try:
      MIL.MappOpenConnectionW.argtypes = [ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL.MappOpenConnectionW.restype = None
      MappOpenConnectionW = MIL.MappOpenConnectionW
   except:
      MappOpenConnectionW = None
if MIL is not None:
   try:
      MIL.MappTimer.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MappTimer.restype = ctypes.c_double
      MappTimer = MIL.MappTimer
   except:
      MappTimer = None
if MIL is not None:
   try:
      MIL.MappTraceW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MappTraceW.restype = None
      MappTraceW = MIL.MappTraceW
   except:
      MappTraceW = None
if MILBEAD is not None:
   try:
      MILBEAD.MbeadAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILBEAD.MbeadAlloc.restype = ctypes.c_longlong
      MbeadAlloc = MILBEAD.MbeadAlloc
   except:
      MbeadAlloc = None
if MILBEAD is not None:
   try:
      MILBEAD.MbeadAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILBEAD.MbeadAllocResult.restype = ctypes.c_longlong
      MbeadAllocResult = MILBEAD.MbeadAllocResult
   except:
      MbeadAllocResult = None
if MILBEAD is not None:
   try:
      MILBEAD.MbeadControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILBEAD.MbeadControlDouble.restype = None
      MbeadControlDouble = MILBEAD.MbeadControlDouble
   except:
      MbeadControlDouble = None
if MILBEAD is not None:
   try:
      MILBEAD.MbeadControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILBEAD.MbeadControlInt64.restype = None
      MbeadControlInt64 = MILBEAD.MbeadControlInt64
   except:
      MbeadControlInt64 = None
if MILBEAD is not None:
   try:
      MILBEAD.MbeadDraw.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILBEAD.MbeadDraw.restype = None
      MbeadDraw = MILBEAD.MbeadDraw
   except:
      MbeadDraw = None
if MILBEAD is not None:
   try:
      MILBEAD.MbeadFree.argtypes = [ctypes.c_longlong]
      MILBEAD.MbeadFree.restype = None
      MbeadFree = MILBEAD.MbeadFree
   except:
      MbeadFree = None
if MILBEAD is not None:
   try:
      MILBEAD.MbeadGetNeighbors.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MILBEAD.MbeadGetNeighbors.restype = None
      MbeadGetNeighbors = MILBEAD.MbeadGetNeighbors
   except:
      MbeadGetNeighbors = None
if MILBEAD is not None:
   try:
      MILBEAD.MbeadGetResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILBEAD.MbeadGetResult.restype = None
      MbeadGetResult = MILBEAD.MbeadGetResult
   except:
      MbeadGetResult = None
if MILBEAD is not None:
   try:
      MILBEAD.MbeadInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILBEAD.MbeadInquire.restype = ctypes.c_longlong
      MbeadInquire = MILBEAD.MbeadInquire
   except:
      MbeadInquire = None
if MILBEAD is not None:
   try:
      MILBEAD.MbeadRestoreW.argtypes = [ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILBEAD.MbeadRestoreW.restype = ctypes.c_longlong
      MbeadRestoreW = MILBEAD.MbeadRestoreW
   except:
      MbeadRestoreW = None
if MILBEAD is not None:
   try:
      MILBEAD.MbeadSaveW.argtypes = [ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong]
      MILBEAD.MbeadSaveW.restype = None
      MbeadSaveW = MILBEAD.MbeadSaveW
   except:
      MbeadSaveW = None
if MILBEAD is not None:
   try:
      MILBEAD.MbeadStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MILBEAD.MbeadStreamW.restype = None
      MbeadStreamW = MILBEAD.MbeadStreamW
   except:
      MbeadStreamW = None
if MILBEAD is not None:
   try:
      MILBEAD.MbeadTemplate.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MILBEAD.MbeadTemplate.restype = None
      MbeadTemplate = MILBEAD.MbeadTemplate
   except:
      MbeadTemplate = None
if MILBEAD is not None:
   try:
      MILBEAD.MbeadTrain.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILBEAD.MbeadTrain.restype = None
      MbeadTrain = MILBEAD.MbeadTrain
   except:
      MbeadTrain = None
if MILBEAD is not None:
   try:
      MILBEAD.MbeadVerify.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILBEAD.MbeadVerify.restype = None
      MbeadVerify = MILBEAD.MbeadVerify
   except:
      MbeadVerify = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILBLOB.MblobAlloc.restype = ctypes.c_longlong
      MblobAlloc = MILBLOB.MblobAlloc
   except:
      MblobAlloc = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobAllocResultNew.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILBLOB.MblobAllocResultNew.restype = ctypes.c_longlong
      MblobAllocResultNew = MILBLOB.MblobAllocResultNew
   except:
      MblobAllocResultNew = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobCalculate.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILBLOB.MblobCalculate.restype = None
      MblobCalculate = MILBLOB.MblobCalculate
   except:
      MblobCalculate = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILBLOB.MblobControlDouble.restype = None
      MblobControlDouble = MILBLOB.MblobControlDouble
   except:
      MblobControlDouble = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILBLOB.MblobControlInt64.restype = None
      MblobControlInt64 = MILBLOB.MblobControlInt64
   except:
      MblobControlInt64 = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobDraw.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILBLOB.MblobDraw.restype = None
      MblobDraw = MILBLOB.MblobDraw
   except:
      MblobDraw = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobFree.argtypes = [ctypes.c_longlong]
      MILBLOB.MblobFree.restype = None
      MblobFree = MILBLOB.MblobFree
   except:
      MblobFree = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobGetLabel.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILBLOB.MblobGetLabel.restype = ctypes.c_longlong
      MblobGetLabel = MILBLOB.MblobGetLabel
   except:
      MblobGetLabel = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobGetResultNew.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILBLOB.MblobGetResultNew.restype = None
      MblobGetResultNew = MILBLOB.MblobGetResultNew
   except:
      MblobGetResultNew = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILBLOB.MblobInquire.restype = ctypes.c_longlong
      MblobInquire = MILBLOB.MblobInquire
   except:
      MblobInquire = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobLabel.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILBLOB.MblobLabel.restype = None
      MblobLabel = MILBLOB.MblobLabel
   except:
      MblobLabel = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobMerge.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILBLOB.MblobMerge.restype = None
      MblobMerge = MILBLOB.MblobMerge
   except:
      MblobMerge = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobReconstruct.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILBLOB.MblobReconstruct.restype = None
      MblobReconstruct = MILBLOB.MblobReconstruct
   except:
      MblobReconstruct = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobRestoreW.argtypes = [ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILBLOB.MblobRestoreW.restype = ctypes.c_longlong
      MblobRestoreW = MILBLOB.MblobRestoreW
   except:
      MblobRestoreW = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILBLOB.MblobSaveW.restype = None
      MblobSaveW = MILBLOB.MblobSaveW
   except:
      MblobSaveW = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobSelect.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double]
      MILBLOB.MblobSelect.restype = None
      MblobSelect = MILBLOB.MblobSelect
   except:
      MblobSelect = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MILBLOB.MblobStreamW.restype = None
      MblobStreamW = MILBLOB.MblobStreamW
   except:
      MblobStreamW = None
if MILBLOB is not None:
   try:
      MILBLOB.MblobTransform.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MILBLOB.MblobTransform.restype = None
      MblobTransform = MILBLOB.MblobTransform
   except:
      MblobTransform = None
if MIL is not None:
   try:
      MIL.MbufAlloc1d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufAlloc1d.restype = ctypes.c_longlong
      MbufAlloc1d = MIL.MbufAlloc1d
   except:
      MbufAlloc1d = None
if MIL is not None:
   try:
      MIL.MbufAlloc2d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufAlloc2d.restype = ctypes.c_longlong
      MbufAlloc2d = MIL.MbufAlloc2d
   except:
      MbufAlloc2d = None
if MIL is not None:
   try:
      MIL.MbufAllocColor.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufAllocColor.restype = ctypes.c_longlong
      MbufAllocColor = MIL.MbufAllocColor
   except:
      MbufAllocColor = None
if MIL is not None:
   try:
      MIL.MbufAllocComponent.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufAllocComponent.restype = ctypes.c_longlong
      MbufAllocComponent = MIL.MbufAllocComponent
   except:
      MbufAllocComponent = None
if MIL is not None:
   try:
      MIL.MbufAllocContainer.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufAllocContainer.restype = ctypes.c_longlong
      MbufAllocContainer = MIL.MbufAllocContainer
   except:
      MbufAllocContainer = None
if MIL is not None:
   try:
      MIL.MbufAllocDefault.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL.MbufAllocDefault.restype = ctypes.c_longlong
      MbufAllocDefault = MIL.MbufAllocDefault
   except:
      MbufAllocDefault = None
if MIL is not None:
   try:
      MIL.MbufBayer.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MbufBayer.restype = None
      MbufBayer = MIL.MbufBayer
   except:
      MbufBayer = None
if MIL is not None:
   try:
      MIL.MbufChild1d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufChild1d.restype = ctypes.c_longlong
      MbufChild1d = MIL.MbufChild1d
   except:
      MbufChild1d = None
if MIL is not None:
   try:
      MIL.MbufChild2d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufChild2d.restype = ctypes.c_longlong
      MbufChild2d = MIL.MbufChild2d
   except:
      MbufChild2d = None
if MIL is not None:
   try:
      MIL.MbufChildColor.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufChildColor.restype = ctypes.c_longlong
      MbufChildColor = MIL.MbufChildColor
   except:
      MbufChildColor = None
if MIL is not None:
   try:
      MIL.MbufChildColor2d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufChildColor2d.restype = ctypes.c_longlong
      MbufChildColor2d = MIL.MbufChildColor2d
   except:
      MbufChildColor2d = None
if MIL is not None:
   try:
      MIL.MbufChildColor2dClip.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p]
      MIL.MbufChildColor2dClip.restype = ctypes.c_longlong
      MbufChildColor2dClip = MIL.MbufChildColor2dClip
   except:
      MbufChildColor2dClip = None
if MIL is not None:
   try:
      MIL.MbufChildContainer.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL.MbufChildContainer.restype = ctypes.c_longlong
      MbufChildContainer = MIL.MbufChildContainer
   except:
      MbufChildContainer = None
if MIL is not None:
   try:
      MIL.MbufChildMove.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MbufChildMove.restype = None
      MbufChildMove = MIL.MbufChildMove
   except:
      MbufChildMove = None
if MIL is not None:
   try:
      MIL.MbufClearCondDouble.argtypes = [ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MbufClearCondDouble.restype = None
      MbufClearCondDouble = MIL.MbufClearCondDouble
   except:
      MbufClearCondDouble = None
if MIL is not None:
   try:
      MIL.MbufClearDouble.argtypes = [ctypes.c_longlong, ctypes.c_double]
      MIL.MbufClearDouble.restype = None
      MbufClearDouble = MIL.MbufClearDouble
   except:
      MbufClearDouble = None
if MIL is not None:
   try:
      MIL.MbufClone.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufClone.restype = ctypes.c_longlong
      MbufClone = MIL.MbufClone
   except:
      MbufClone = None
if MIL is not None:
   try:
      MIL.MbufControlAreaDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MbufControlAreaDouble.restype = None
      MbufControlAreaDouble = MIL.MbufControlAreaDouble
   except:
      MbufControlAreaDouble = None
if MIL is not None:
   try:
      MIL.MbufControlContainerDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MbufControlContainerDouble.restype = None
      MbufControlContainerDouble = MIL.MbufControlContainerDouble
   except:
      MbufControlContainerDouble = None
if MIL is not None:
   try:
      MIL.MbufControlContainerInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MbufControlContainerInt64.restype = None
      MbufControlContainerInt64 = MIL.MbufControlContainerInt64
   except:
      MbufControlContainerInt64 = None
if MIL is not None:
   try:
      MIL.MbufControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MbufControlDouble.restype = None
      MbufControlDouble = MIL.MbufControlDouble
   except:
      MbufControlDouble = None
if MIL is not None:
   try:
      MIL.MbufControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MbufControlInt64.restype = None
      MbufControlInt64 = MIL.MbufControlInt64
   except:
      MbufControlInt64 = None
if MIL3D is not None:
   try:
      MIL3D.MbufConvert3d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL3D.MbufConvert3d.restype = None
      MbufConvert3d = MIL3D.MbufConvert3d
   except:
      MbufConvert3d = None
if MIL is not None:
   try:
      MIL.MbufCopy.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
      MIL.MbufCopy.restype = None
      MbufCopy = MIL.MbufCopy
   except:
      MbufCopy = None
if MIL is not None:
   try:
      MIL.MbufCopyClip.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MbufCopyClip.restype = None
      MbufCopyClip = MIL.MbufCopyClip
   except:
      MbufCopyClip = None
if MIL is not None:
   try:
      MIL.MbufCopyColor.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MbufCopyColor.restype = None
      MbufCopyColor = MIL.MbufCopyColor
   except:
      MbufCopyColor = None
if MIL is not None:
   try:
      MIL.MbufCopyColor2d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MbufCopyColor2d.restype = None
      MbufCopyColor2d = MIL.MbufCopyColor2d
   except:
      MbufCopyColor2d = None
if MIL is not None:
   try:
      MIL.MbufCopyComponent.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MbufCopyComponent.restype = None
      MbufCopyComponent = MIL.MbufCopyComponent
   except:
      MbufCopyComponent = None
if MIL is not None:
   try:
      MIL.MbufCopyCondDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MbufCopyCondDouble.restype = None
      MbufCopyCondDouble = MIL.MbufCopyCondDouble
   except:
      MbufCopyCondDouble = None
if MIL is not None:
   try:
      MIL.MbufCopyMask.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MbufCopyMask.restype = None
      MbufCopyMask = MIL.MbufCopyMask
   except:
      MbufCopyMask = None
if MIL is not None:
   try:
      MIL.MbufCreate2dFunc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_ulonglong, ctypes.c_void_p]
      MIL.MbufCreate2dFunc.restype = ctypes.c_longlong
      MbufCreate2dFunc = MIL.MbufCreate2dFunc
   except:
      MbufCreate2dFunc = None
if MIL is not None:
   try:
      MIL.MbufCreateColor.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p]
      MIL.MbufCreateColor.restype = ctypes.c_longlong
      MbufCreateColor = MIL.MbufCreateColor
   except:
      MbufCreateColor = None
if MIL is not None:
   try:
      MIL.MbufCreateComponent.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL.MbufCreateComponent.restype = ctypes.c_longlong
      MbufCreateComponent = MIL.MbufCreateComponent
   except:
      MbufCreateComponent = None
if MIL is not None:
   try:
      MIL.MbufDiskInquireW.argtypes = [ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufDiskInquireW.restype = ctypes.c_longlong
      MbufDiskInquireW = MIL.MbufDiskInquireW
   except:
      MbufDiskInquireW = None
if MIL is not None:
   try:
      MIL.MbufExportSequenceW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong]
      MIL.MbufExportSequenceW.restype = None
      MbufExportSequenceW = MIL.MbufExportSequenceW
   except:
      MbufExportSequenceW = None
if MIL is not None:
   try:
      MIL.MbufExportW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MbufExportW.restype = None
      MbufExportW = MIL.MbufExportW
   except:
      MbufExportW = None
if MIL is not None:
   try:
      MIL.MbufFree.argtypes = [ctypes.c_longlong]
      MIL.MbufFree.restype = None
      MbufFree = MIL.MbufFree
   except:
      MbufFree = None
if MIL is not None:
   try:
      MIL.MbufFreeComponent.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MbufFreeComponent.restype = None
      MbufFreeComponent = MIL.MbufFreeComponent
   except:
      MbufFreeComponent = None
if MIL is not None:
   try:
      MIL.MbufGet.argtypes = [ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufGet.restype = None
      MbufGet = MIL.MbufGet
   except:
      MbufGet = None
if MIL is not None:
   try:
      MIL.MbufGet1d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufGet1d.restype = None
      MbufGet1d = MIL.MbufGet1d
   except:
      MbufGet1d = None
if MIL is not None:
   try:
      MIL.MbufGet2d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufGet2d.restype = None
      MbufGet2d = MIL.MbufGet2d
   except:
      MbufGet2d = None
if MIL is not None:
   try:
      MIL.MbufGetArc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_void_p, ctypes.c_void_p]
      MIL.MbufGetArc.restype = ctypes.c_longlong
      MbufGetArc = MIL.MbufGetArc
   except:
      MbufGetArc = None
if MIL is not None:
   try:
      MIL.MbufGetArc2.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
      MIL.MbufGetArc2.restype = ctypes.c_longlong
      MbufGetArc2 = MIL.MbufGetArc2
   except:
      MbufGetArc2 = None
if MIL is not None:
   try:
      MIL.MbufGetColor.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufGetColor.restype = None
      MbufGetColor = MIL.MbufGetColor
   except:
      MbufGetColor = None
if MIL is not None:
   try:
      MIL.MbufGetColor2d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufGetColor2d.restype = None
      MbufGetColor2d = MIL.MbufGetColor2d
   except:
      MbufGetColor2d = None
if MIL is not None:
   try:
      MIL.MbufGetHookInfo.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufGetHookInfo.restype = ctypes.c_longlong
      MbufGetHookInfo = MIL.MbufGetHookInfo
   except:
      MbufGetHookInfo = None
if MIL is not None:
   try:
      MIL.MbufGetLine.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p]
      MIL.MbufGetLine.restype = None
      MbufGetLine = MIL.MbufGetLine
   except:
      MbufGetLine = None
if MIL is not None:
   try:
      MIL.MbufGetListDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufGetListDouble.restype = None
      MbufGetListDouble = MIL.MbufGetListDouble
   except:
      MbufGetListDouble = None
if MIL is not None:
   try:
      MIL.MbufGetListInt32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufGetListInt32.restype = None
      MbufGetListInt32 = MIL.MbufGetListInt32
   except:
      MbufGetListInt32 = None
if MIL is not None:
   try:
      MIL.MbufGetListInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufGetListInt64.restype = None
      MbufGetListInt64 = MIL.MbufGetListInt64
   except:
      MbufGetListInt64 = None
if MIL is not None:
   try:
      MIL.MbufHookFunction.argtypes = [ctypes.c_longlong, ctypes.c_longlong, MIL_BUF_HOOK_FUNCTION_PTR, ctypes.c_void_p]
      MIL.MbufHookFunction.restype = None
      MbufHookFunction = MIL.MbufHookFunction
   except:
      MbufHookFunction = None
if MIL is not None:
   try:
      MIL.MbufImportSequenceW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MbufImportSequenceW.restype = None
      MbufImportSequenceW = MIL.MbufImportSequenceW
   except:
      MbufImportSequenceW = None
if MIL is not None:
   try:
      MIL.MbufImportW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufImportW.restype = ctypes.c_longlong
      MbufImportW = MIL.MbufImportW
   except:
      MbufImportW = None
if MIL is not None:
   try:
      MIL.MbufInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufInquire.restype = ctypes.c_longlong
      MbufInquire = MIL.MbufInquire
   except:
      MbufInquire = None
if MIL is not None:
   try:
      MIL.MbufInquireContainer.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufInquireContainer.restype = ctypes.c_longlong
      MbufInquireContainer = MIL.MbufInquireContainer
   except:
      MbufInquireContainer = None
if MIL is not None:
   try:
      MIL.MbufLink.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MbufLink.restype = None
      MbufLink = MIL.MbufLink
   except:
      MbufLink = None
if MIL is not None:
   try:
      MIL.MbufLoadW.argtypes = [ctypes.c_void_p, ctypes.c_longlong]
      MIL.MbufLoadW.restype = None
      MbufLoadW = MIL.MbufLoadW
   except:
      MbufLoadW = None
if MIL is not None:
   try:
      MIL.MbufPut.argtypes = [ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufPut.restype = None
      MbufPut = MIL.MbufPut
   except:
      MbufPut = None
if MIL is not None:
   try:
      MIL.MbufPut1d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufPut1d.restype = None
      MbufPut1d = MIL.MbufPut1d
   except:
      MbufPut1d = None
if MIL is not None:
   try:
      MIL.MbufPut2d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufPut2d.restype = None
      MbufPut2d = MIL.MbufPut2d
   except:
      MbufPut2d = None
if MIL is not None:
   try:
      MIL.MbufPutColor.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufPutColor.restype = None
      MbufPutColor = MIL.MbufPutColor
   except:
      MbufPutColor = None
if MIL is not None:
   try:
      MIL.MbufPutColor2d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufPutColor2d.restype = None
      MbufPutColor2d = MIL.MbufPutColor2d
   except:
      MbufPutColor2d = None
if MIL is not None:
   try:
      MIL.MbufPutLine.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p]
      MIL.MbufPutLine.restype = None
      MbufPutLine = MIL.MbufPutLine
   except:
      MbufPutLine = None
if MIL is not None:
   try:
      MIL.MbufPutListDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufPutListDouble.restype = None
      MbufPutListDouble = MIL.MbufPutListDouble
   except:
      MbufPutListDouble = None
if MIL is not None:
   try:
      MIL.MbufPutListInt32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufPutListInt32.restype = None
      MbufPutListInt32 = MIL.MbufPutListInt32
   except:
      MbufPutListInt32 = None
if MIL is not None:
   try:
      MIL.MbufPutListInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufPutListInt64.restype = None
      MbufPutListInt64 = MIL.MbufPutListInt64
   except:
      MbufPutListInt64 = None
if MIL is not None:
   try:
      MIL.MbufRestoreW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL.MbufRestoreW.restype = ctypes.c_longlong
      MbufRestoreW = MIL.MbufRestoreW
   except:
      MbufRestoreW = None
if MIL is not None:
   try:
      MIL.MbufSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong]
      MIL.MbufSaveW.restype = None
      MbufSaveW = MIL.MbufSaveW
   except:
      MbufSaveW = None
if MIL is not None:
   try:
      MIL.MbufSetRegionDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MbufSetRegionDouble.restype = None
      MbufSetRegionDouble = MIL.MbufSetRegionDouble
   except:
      MbufSetRegionDouble = None
if MIL is not None:
   try:
      MIL.MbufStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MIL.MbufStreamW.restype = None
      MbufStreamW = MIL.MbufStreamW
   except:
      MbufStreamW = None
if MIL is not None:
   try:
      MIL.MbufTransfer.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MbufTransfer.restype = None
      MbufTransfer = MIL.MbufTransfer
   except:
      MbufTransfer = None
if MILCAL is not None:
   try:
      MILCAL.McalAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCAL.McalAlloc.restype = ctypes.c_longlong
      McalAlloc = MILCAL.McalAlloc
   except:
      McalAlloc = None
if MILCAL is not None:
   try:
      MILCAL.McalAssociate.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCAL.McalAssociate.restype = None
      McalAssociate = MILCAL.McalAssociate
   except:
      McalAssociate = None
if MILCAL is not None:
   try:
      MILCAL.McalControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILCAL.McalControlDouble.restype = None
      McalControlDouble = MILCAL.McalControlDouble
   except:
      McalControlDouble = None
if MILCAL is not None:
   try:
      MILCAL.McalControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCAL.McalControlInt64.restype = None
      McalControlInt64 = MILCAL.McalControlInt64
   except:
      McalControlInt64 = None
if MILCAL is not None:
   try:
      MILCAL.McalDraw.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCAL.McalDraw.restype = None
      McalDraw = MILCAL.McalDraw
   except:
      McalDraw = None
if MILCAL is not None:
   try:
      MILCAL.McalDraw3d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCAL.McalDraw3d.restype = ctypes.c_longlong
      McalDraw3d = MILCAL.McalDraw3d
   except:
      McalDraw3d = None
if MILCAL is not None:
   try:
      MILCAL.McalFixtureDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
      MILCAL.McalFixtureDouble.restype = None
      McalFixtureDouble = MILCAL.McalFixtureDouble
   except:
      McalFixtureDouble = None
if MILCAL is not None:
   try:
      MILCAL.McalFree.argtypes = [ctypes.c_longlong]
      MILCAL.McalFree.restype = None
      McalFree = MILCAL.McalFree
   except:
      McalFree = None
if MILCAL is not None:
   try:
      MILCAL.McalGetCoordinateSystem.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
      MILCAL.McalGetCoordinateSystem.restype = None
      McalGetCoordinateSystem = MILCAL.McalGetCoordinateSystem
   except:
      McalGetCoordinateSystem = None
if MILCAL is not None:
   try:
      MILCAL.McalGrid.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_longlong, ctypes.c_longlong]
      MILCAL.McalGrid.restype = None
      McalGrid = MILCAL.McalGrid
   except:
      McalGrid = None
if MILCAL is not None:
   try:
      MILCAL.McalInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCAL.McalInquire.restype = ctypes.c_longlong
      McalInquire = MILCAL.McalInquire
   except:
      McalInquire = None
if MILCAL is not None:
   try:
      MILCAL.McalInquireSingle.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCAL.McalInquireSingle.restype = ctypes.c_longlong
      McalInquireSingle = MILCAL.McalInquireSingle
   except:
      McalInquireSingle = None
if MILCAL is not None:
   try:
      MILCAL.McalList.argtypes = [ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCAL.McalList.restype = None
      McalList = MILCAL.McalList
   except:
      McalList = None
if MILCAL is not None:
   try:
      MILCAL.McalRelativeOrigin.argtypes = [ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MILCAL.McalRelativeOrigin.restype = None
      McalRelativeOrigin = MILCAL.McalRelativeOrigin
   except:
      McalRelativeOrigin = None
if MILCAL is not None:
   try:
      MILCAL.McalRestoreW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILCAL.McalRestoreW.restype = ctypes.c_longlong
      McalRestoreW = MILCAL.McalRestoreW
   except:
      McalRestoreW = None
if MILCAL is not None:
   try:
      MILCAL.McalSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILCAL.McalSaveW.restype = None
      McalSaveW = MILCAL.McalSaveW
   except:
      McalSaveW = None
if MILCAL is not None:
   try:
      MILCAL.McalSetCoordinateSystem.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
      MILCAL.McalSetCoordinateSystem.restype = None
      McalSetCoordinateSystem = MILCAL.McalSetCoordinateSystem
   except:
      McalSetCoordinateSystem = None
if MILCAL is not None:
   try:
      MILCAL.McalStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MILCAL.McalStreamW.restype = None
      McalStreamW = MILCAL.McalStreamW
   except:
      McalStreamW = None
if MILCAL is not None:
   try:
      MILCAL.McalTransformCoordinate.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
      MILCAL.McalTransformCoordinate.restype = None
      McalTransformCoordinate = MILCAL.McalTransformCoordinate
   except:
      McalTransformCoordinate = None
if MILCAL is not None:
   try:
      MILCAL.McalTransformCoordinate3dList.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_void_p, ctypes.c_longlong]
      MILCAL.McalTransformCoordinate3dList.restype = None
      McalTransformCoordinate3dList = MILCAL.McalTransformCoordinate3dList
   except:
      McalTransformCoordinate3dList = None
if MILCAL is not None:
   try:
      MILCAL.McalTransformCoordinateList.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.c_void_p]
      MILCAL.McalTransformCoordinateList.restype = None
      McalTransformCoordinateList = MILCAL.McalTransformCoordinateList
   except:
      McalTransformCoordinateList = None
if MILCAL is not None:
   try:
      MILCAL.McalTransformImage.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCAL.McalTransformImage.restype = None
      McalTransformImage = MILCAL.McalTransformImage
   except:
      McalTransformImage = None
if MILCAL is not None:
   try:
      MILCAL.McalTransformResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
      MILCAL.McalTransformResult.restype = None
      McalTransformResult = MILCAL.McalTransformResult
   except:
      McalTransformResult = None
if MILCAL is not None:
   try:
      MILCAL.McalTransformResultAtPosition.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
      MILCAL.McalTransformResultAtPosition.restype = None
      McalTransformResultAtPosition = MILCAL.McalTransformResultAtPosition
   except:
      McalTransformResultAtPosition = None
if MILCAL is not None:
   try:
      MILCAL.McalUniform.argtypes = [ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MILCAL.McalUniform.restype = None
      McalUniform = MILCAL.McalUniform
   except:
      McalUniform = None
if MILCAL is not None:
   try:
      MILCAL.McalWarp.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCAL.McalWarp.restype = None
      McalWarp = MILCAL.McalWarp
   except:
      McalWarp = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCLASS.MclassAlloc.restype = ctypes.c_longlong
      MclassAlloc = MILCLASS.MclassAlloc
   except:
      MclassAlloc = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCLASS.MclassAllocResult.restype = ctypes.c_longlong
      MclassAllocResult = MILCLASS.MclassAllocResult
   except:
      MclassAllocResult = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILCLASS.MclassControlDouble.restype = None
      MclassControlDouble = MILCLASS.MclassControlDouble
   except:
      MclassControlDouble = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassControlEntryDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, MIL_UUID, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_void_p, ctypes.c_longlong]
      MILCLASS.MclassControlEntryDouble.restype = None
      MclassControlEntryDouble = MILCLASS.MclassControlEntryDouble
   except:
      MclassControlEntryDouble = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassControlEntryInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, MIL_UUID, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong]
      MILCLASS.MclassControlEntryInt64.restype = None
      MclassControlEntryInt64 = MILCLASS.MclassControlEntryInt64
   except:
      MclassControlEntryInt64 = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCLASS.MclassControlInt64.restype = None
      MclassControlInt64 = MILCLASS.MclassControlInt64
   except:
      MclassControlInt64 = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassControlMilUuid.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, MIL_UUID]
      MILCLASS.MclassControlMilUuid.restype = None
      MclassControlMilUuid = MILCLASS.MclassControlMilUuid
   except:
      MclassControlMilUuid = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassCopy.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCLASS.MclassCopy.restype = None
      MclassCopy = MILCLASS.MclassCopy
   except:
      MclassCopy = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassCopyResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCLASS.MclassCopyResult.restype = None
      MclassCopyResult = MILCLASS.MclassCopyResult
   except:
      MclassCopyResult = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassDraw.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCLASS.MclassDraw.restype = None
      MclassDraw = MILCLASS.MclassDraw
   except:
      MclassDraw = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassExportW.argtypes = [ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCLASS.MclassExportW.restype = None
      MclassExportW = MILCLASS.MclassExportW
   except:
      MclassExportW = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassFree.argtypes = [ctypes.c_longlong]
      MILCLASS.MclassFree.restype = None
      MclassFree = MILCLASS.MclassFree
   except:
      MclassFree = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassGetHookInfo.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCLASS.MclassGetHookInfo.restype = ctypes.c_longlong
      MclassGetHookInfo = MILCLASS.MclassGetHookInfo
   except:
      MclassGetHookInfo = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassGetResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCLASS.MclassGetResult.restype = None
      MclassGetResult = MILCLASS.MclassGetResult
   except:
      MclassGetResult = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassHookFunction.argtypes = [ctypes.c_longlong, ctypes.c_longlong, MIL_CLASS_HOOK_FUNCTION_PTR, ctypes.c_void_p]
      MILCLASS.MclassHookFunction.restype = None
      MclassHookFunction = MILCLASS.MclassHookFunction
   except:
      MclassHookFunction = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassImportW.argtypes = [ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCLASS.MclassImportW.restype = None
      MclassImportW = MILCLASS.MclassImportW
   except:
      MclassImportW = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCLASS.MclassInquire.restype = ctypes.c_longlong
      MclassInquire = MILCLASS.MclassInquire
   except:
      MclassInquire = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassInquireEntry.argtypes = [ctypes.c_longlong, ctypes.c_longlong, MIL_UUID, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCLASS.MclassInquireEntry.restype = ctypes.c_longlong
      MclassInquireEntry = MILCLASS.MclassInquireEntry
   except:
      MclassInquireEntry = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassPredict.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCLASS.MclassPredict.restype = None
      MclassPredict = MILCLASS.MclassPredict
   except:
      MclassPredict = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassPreprocess.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
      MILCLASS.MclassPreprocess.restype = None
      MclassPreprocess = MILCLASS.MclassPreprocess
   except:
      MclassPreprocess = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassRestoreW.argtypes = [ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILCLASS.MclassRestoreW.restype = ctypes.c_longlong
      MclassRestoreW = MILCLASS.MclassRestoreW
   except:
      MclassRestoreW = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILCLASS.MclassSaveW.restype = None
      MclassSaveW = MILCLASS.MclassSaveW
   except:
      MclassSaveW = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassSplitDataset.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.c_longlong]
      MILCLASS.MclassSplitDataset.restype = None
      MclassSplitDataset = MILCLASS.MclassSplitDataset
   except:
      MclassSplitDataset = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MILCLASS.MclassStreamW.restype = None
      MclassStreamW = MILCLASS.MclassStreamW
   except:
      MclassStreamW = None
if MILCLASS is not None:
   try:
      MILCLASS.MclassTrain.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCLASS.MclassTrain.restype = None
      MclassTrain = MILCLASS.MclassTrain
   except:
      MclassTrain = None
if MILCODE is not None:
   try:
      MILCODE.McodeAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCODE.McodeAlloc.restype = ctypes.c_longlong
      McodeAlloc = MILCODE.McodeAlloc
   except:
      McodeAlloc = None
if MILCODE is not None:
   try:
      MILCODE.McodeAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCODE.McodeAllocResult.restype = ctypes.c_longlong
      McodeAllocResult = MILCODE.McodeAllocResult
   except:
      McodeAllocResult = None
if MILCODE is not None:
   try:
      MILCODE.McodeControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILCODE.McodeControlDouble.restype = None
      McodeControlDouble = MILCODE.McodeControlDouble
   except:
      McodeControlDouble = None
if MILCODE is not None:
   try:
      MILCODE.McodeControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCODE.McodeControlInt64.restype = None
      McodeControlInt64 = MILCODE.McodeControlInt64
   except:
      McodeControlInt64 = None
if MILCODE is not None:
   try:
      MILCODE.McodeDetect.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCODE.McodeDetect.restype = None
      McodeDetect = MILCODE.McodeDetect
   except:
      McodeDetect = None
if MILCODE is not None:
   try:
      MILCODE.McodeDrawNew.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCODE.McodeDrawNew.restype = None
      McodeDrawNew = MILCODE.McodeDrawNew
   except:
      McodeDrawNew = None
if MILCODE is not None:
   try:
      MILCODE.McodeFree.argtypes = [ctypes.c_longlong]
      MILCODE.McodeFree.restype = None
      McodeFree = MILCODE.McodeFree
   except:
      McodeFree = None
if MILCODE is not None:
   try:
      MILCODE.McodeGetResultNew.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCODE.McodeGetResultNew.restype = None
      McodeGetResultNew = MILCODE.McodeGetResultNew
   except:
      McodeGetResultNew = None
if MILCODE is not None:
   try:
      MILCODE.McodeGrade.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCODE.McodeGrade.restype = None
      McodeGrade = MILCODE.McodeGrade
   except:
      McodeGrade = None
if MILCODE is not None:
   try:
      MILCODE.McodeInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCODE.McodeInquire.restype = ctypes.c_longlong
      McodeInquire = MILCODE.McodeInquire
   except:
      McodeInquire = None
if MILCODE is not None:
   try:
      MILCODE.McodeModel.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCODE.McodeModel.restype = ctypes.c_longlong
      McodeModel = MILCODE.McodeModel
   except:
      McodeModel = None
if MILCODE is not None:
   try:
      MILCODE.McodeRead.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCODE.McodeRead.restype = None
      McodeRead = MILCODE.McodeRead
   except:
      McodeRead = None
if MILCODE is not None:
   try:
      MILCODE.McodeRestoreW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILCODE.McodeRestoreW.restype = ctypes.c_longlong
      McodeRestoreW = MILCODE.McodeRestoreW
   except:
      McodeRestoreW = None
if MILCODE is not None:
   try:
      MILCODE.McodeSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILCODE.McodeSaveW.restype = None
      McodeSaveW = MILCODE.McodeSaveW
   except:
      McodeSaveW = None
if MILCODE is not None:
   try:
      MILCODE.McodeStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MILCODE.McodeStreamW.restype = None
      McodeStreamW = MILCODE.McodeStreamW
   except:
      McodeStreamW = None
if MILCODE is not None:
   try:
      MILCODE.McodeTrain.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_longlong]
      MILCODE.McodeTrain.restype = None
      McodeTrain = MILCODE.McodeTrain
   except:
      McodeTrain = None
if MILCODE is not None:
   try:
      MILCODE.McodeWriteNewW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong]
      MILCODE.McodeWriteNewW.restype = None
      McodeWriteNewW = MILCODE.McodeWriteNewW
   except:
      McodeWriteNewW = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCOLOR.McolAlloc.restype = ctypes.c_longlong
      McolAlloc = MILCOLOR.McolAlloc
   except:
      McolAlloc = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCOLOR.McolAllocResult.restype = ctypes.c_longlong
      McolAllocResult = MILCOLOR.McolAllocResult
   except:
      McolAllocResult = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILCOLOR.McolControlDouble.restype = None
      McolControlDouble = MILCOLOR.McolControlDouble
   except:
      McolControlDouble = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCOLOR.McolControlInt64.restype = None
      McolControlInt64 = MILCOLOR.McolControlInt64
   except:
      McolControlInt64 = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolDefine.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
      MILCOLOR.McolDefine.restype = None
      McolDefine = MILCOLOR.McolDefine
   except:
      McolDefine = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolDistance.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong]
      MILCOLOR.McolDistance.restype = None
      McolDistance = MILCOLOR.McolDistance
   except:
      McolDistance = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolDraw.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCOLOR.McolDraw.restype = None
      McolDraw = MILCOLOR.McolDraw
   except:
      McolDraw = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolFree.argtypes = [ctypes.c_longlong]
      MILCOLOR.McolFree.restype = None
      McolFree = MILCOLOR.McolFree
   except:
      McolFree = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolGetResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCOLOR.McolGetResult.restype = None
      McolGetResult = MILCOLOR.McolGetResult
   except:
      McolGetResult = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCOLOR.McolInquire.restype = ctypes.c_longlong
      McolInquire = MILCOLOR.McolInquire
   except:
      McolInquire = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolMask.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCOLOR.McolMask.restype = None
      McolMask = MILCOLOR.McolMask
   except:
      McolMask = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolMatch.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCOLOR.McolMatch.restype = None
      McolMatch = MILCOLOR.McolMatch
   except:
      McolMatch = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolPreprocess.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
      MILCOLOR.McolPreprocess.restype = None
      McolPreprocess = MILCOLOR.McolPreprocess
   except:
      McolPreprocess = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolProject.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCOLOR.McolProject.restype = None
      McolProject = MILCOLOR.McolProject
   except:
      McolProject = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolRestoreW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILCOLOR.McolRestoreW.restype = ctypes.c_longlong
      McolRestoreW = MILCOLOR.McolRestoreW
   except:
      McolRestoreW = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILCOLOR.McolSaveW.restype = None
      McolSaveW = MILCOLOR.McolSaveW
   except:
      McolSaveW = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolSetMethod.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCOLOR.McolSetMethod.restype = None
      McolSetMethod = MILCOLOR.McolSetMethod
   except:
      McolSetMethod = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MILCOLOR.McolStreamW.restype = None
      McolStreamW = MILCOLOR.McolStreamW
   except:
      McolStreamW = None
if MILCOLOR is not None:
   try:
      MILCOLOR.McolTransform.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCOLOR.McolTransform.restype = None
      McolTransform = MILCOLOR.McolTransform
   except:
      McolTransform = None
if MILCOM is not None:
   try:
      MILCOM.McomAllocW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCOM.McomAllocW.restype = ctypes.c_longlong
      McomAllocW = MILCOM.McomAllocW
   except:
      McomAllocW = None
if MILCOM is not None:
   try:
      MILCOM.McomControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILCOM.McomControlDouble.restype = None
      McomControlDouble = MILCOM.McomControlDouble
   except:
      McomControlDouble = None
if MILCOM is not None:
   try:
      MILCOM.McomControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILCOM.McomControlInt64.restype = None
      McomControlInt64 = MILCOM.McomControlInt64
   except:
      McomControlInt64 = None
if MILCOM is not None:
   try:
      MILCOM.McomControlText.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p]
      MILCOM.McomControlText.restype = None
      McomControlText = MILCOM.McomControlText
   except:
      McomControlText = None
if MILCOM is not None:
   try:
      MILCOM.McomFree.argtypes = [ctypes.c_longlong]
      MILCOM.McomFree.restype = None
      McomFree = MILCOM.McomFree
   except:
      McomFree = None
if MILCOM is not None:
   try:
      MILCOM.McomInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCOM.McomInquire.restype = ctypes.c_longlong
      McomInquire = MILCOM.McomInquire
   except:
      McomInquire = None
if MILCOM is not None:
   try:
      MILCOM.McomReadW.argtypes = [ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCOM.McomReadW.restype = None
      McomReadW = MILCOM.McomReadW
   except:
      McomReadW = None
if MILCOM is not None:
   try:
      MILCOM.McomSendPosition.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong, ctypes.c_double]
      MILCOM.McomSendPosition.restype = None
      McomSendPosition = MILCOM.McomSendPosition
   except:
      McomSendPosition = None
if MILCOM is not None:
   try:
      MILCOM.McomWaitPositionRequest.argtypes = [ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.POINTER(ctypes.c_longlong), ctypes.POINTER(ctypes.c_longlong), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_longlong, ctypes.c_double]
      MILCOM.McomWaitPositionRequest.restype = None
      McomWaitPositionRequest = MILCOM.McomWaitPositionRequest
   except:
      McomWaitPositionRequest = None
if MILCOM is not None:
   try:
      MILCOM.McomWriteW.argtypes = [ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILCOM.McomWriteW.restype = None
      McomWriteW = MILCOM.McomWriteW
   except:
      McomWriteW = None
if MIL is not None:
   try:
      MIL.MdigAllocW.argtypes = [ctypes.c_longlong, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MdigAllocW.restype = ctypes.c_longlong
      MdigAllocW = MIL.MdigAllocW
   except:
      MdigAllocW = None
if MIL is not None:
   try:
      MIL.MdigControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MdigControlDouble.restype = None
      MdigControlDouble = MIL.MdigControlDouble
   except:
      MdigControlDouble = None
if MIL is not None:
   try:
      MIL.MdigControlFeatureW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MdigControlFeatureW.restype = None
      MdigControlFeatureW = MIL.MdigControlFeatureW
   except:
      MdigControlFeatureW = None
if MIL is not None:
   try:
      MIL.MdigControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MdigControlInt64.restype = None
      MdigControlInt64 = MIL.MdigControlInt64
   except:
      MdigControlInt64 = None
if MILIM is not None:
   try:
      MILIM.MdigFocus.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, MIL_FOCUS_HOOK_FUNCTION_PTR, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILIM.MdigFocus.restype = None
      MdigFocus = MILIM.MdigFocus
   except:
      MdigFocus = None
if MIL is not None:
   try:
      MIL.MdigFree.argtypes = [ctypes.c_longlong]
      MIL.MdigFree.restype = None
      MdigFree = MIL.MdigFree
   except:
      MdigFree = None
if MIL is not None:
   try:
      MIL.MdigGetHookInfo.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MdigGetHookInfo.restype = ctypes.c_longlong
      MdigGetHookInfo = MIL.MdigGetHookInfo
   except:
      MdigGetHookInfo = None
if MIL is not None:
   try:
      MIL.MdigGrab.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
      MIL.MdigGrab.restype = None
      MdigGrab = MIL.MdigGrab
   except:
      MdigGrab = None
if MIL is not None:
   try:
      MIL.MdigGrabContinuous.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
      MIL.MdigGrabContinuous.restype = None
      MdigGrabContinuous = MIL.MdigGrabContinuous
   except:
      MdigGrabContinuous = None
if MIL is not None:
   try:
      MIL.MdigGrabWait.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
      MIL.MdigGrabWait.restype = None
      MdigGrabWait = MIL.MdigGrabWait
   except:
      MdigGrabWait = None
if MIL is not None:
   try:
      MIL.MdigHalt.argtypes = [ctypes.c_longlong]
      MIL.MdigHalt.restype = None
      MdigHalt = MIL.MdigHalt
   except:
      MdigHalt = None
if MIL is not None:
   try:
      MIL.MdigHookFunction.argtypes = [ctypes.c_longlong, ctypes.c_longlong, MIL_DIG_HOOK_FUNCTION_PTR, ctypes.c_void_p]
      MIL.MdigHookFunction.restype = None
      MdigHookFunction = MIL.MdigHookFunction
   except:
      MdigHookFunction = None
if MIL is not None:
   try:
      MIL.MdigInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MdigInquire.restype = ctypes.c_longlong
      MdigInquire = MIL.MdigInquire
   except:
      MdigInquire = None
if MIL is not None:
   try:
      MIL.MdigInquireFeatureW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MdigInquireFeatureW.restype = None
      MdigInquireFeatureW = MIL.MdigInquireFeatureW
   except:
      MdigInquireFeatureW = None
if MIL is not None:
   try:
      MIL.MdigProcess.argtypes = [ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, MIL_DIG_HOOK_FUNCTION_PTR, ctypes.c_void_p]
      MIL.MdigProcess.restype = None
      MdigProcess = MIL.MdigProcess
   except:
      MdigProcess = None
if MIL is not None:
   try:
      MIL.MdispAllocW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MdispAllocW.restype = ctypes.c_longlong
      MdispAllocW = MIL.MdispAllocW
   except:
      MdispAllocW = None
if MIL is not None:
   try:
      MIL.MdispControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MdispControlDouble.restype = None
      MdispControlDouble = MIL.MdispControlDouble
   except:
      MdispControlDouble = None
if MIL is not None:
   try:
      MIL.MdispControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MdispControlInt64.restype = None
      MdispControlInt64 = MIL.MdispControlInt64
   except:
      MdispControlInt64 = None
if MIL is not None:
   try:
      MIL.MdispFree.argtypes = [ctypes.c_longlong]
      MIL.MdispFree.restype = None
      MdispFree = MIL.MdispFree
   except:
      MdispFree = None
if MIL is not None:
   try:
      MIL.MdispGetHookInfo.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MdispGetHookInfo.restype = ctypes.c_longlong
      MdispGetHookInfo = MIL.MdispGetHookInfo
   except:
      MdispGetHookInfo = None
if MIL is not None:
   try:
      MIL.MdispHookFunction.argtypes = [ctypes.c_longlong, ctypes.c_longlong, MIL_DISP_HOOK_FUNCTION_PTR, ctypes.c_void_p]
      MIL.MdispHookFunction.restype = None
      MdispHookFunction = MIL.MdispHookFunction
   except:
      MdispHookFunction = None
if MIL is not None:
   try:
      MIL.MdispInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MdispInquire.restype = ctypes.c_longlong
      MdispInquire = MIL.MdispInquire
   except:
      MdispInquire = None
if MIL is not None:
   try:
      MIL.MdispLut.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
      MIL.MdispLut.restype = None
      MdispLut = MIL.MdispLut
   except:
      MdispLut = None
if MIL is not None:
   try:
      MIL.MdispPan.argtypes = [ctypes.c_longlong, ctypes.c_double, ctypes.c_double]
      MIL.MdispPan.restype = None
      MdispPan = MIL.MdispPan
   except:
      MdispPan = None
if MIL is not None:
   try:
      MIL.MdispSelect.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
      MIL.MdispSelect.restype = None
      MdispSelect = MIL.MdispSelect
   except:
      MdispSelect = None
if MIL is not None:
   try:
      MIL.MdispSelectWindow.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MdispSelectWindow.restype = None
      MdispSelectWindow = MIL.MdispSelectWindow
   except:
      MdispSelectWindow = None
if MIL is not None:
   try:
      MIL.MdispZoom.argtypes = [ctypes.c_longlong, ctypes.c_double, ctypes.c_double]
      MIL.MdispZoom.restype = None
      MdispZoom = MIL.MdispZoom
   except:
      MdispZoom = None
if MILDMR is not None:
   try:
      MILDMR.MdmrAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILDMR.MdmrAlloc.restype = ctypes.c_longlong
      MdmrAlloc = MILDMR.MdmrAlloc
   except:
      MdmrAlloc = None
if MILDMR is not None:
   try:
      MILDMR.MdmrAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILDMR.MdmrAllocResult.restype = ctypes.c_longlong
      MdmrAllocResult = MILDMR.MdmrAllocResult
   except:
      MdmrAllocResult = None
if MILDMR is not None:
   try:
      MILDMR.MdmrControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILDMR.MdmrControlDouble.restype = None
      MdmrControlDouble = MILDMR.MdmrControlDouble
   except:
      MdmrControlDouble = None
if MILDMR is not None:
   try:
      MILDMR.MdmrControlFontDoubleW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_double, ctypes.c_void_p]
      MILDMR.MdmrControlFontDoubleW.restype = None
      MdmrControlFontDoubleW = MILDMR.MdmrControlFontDoubleW
   except:
      MdmrControlFontDoubleW = None
if MILDMR is not None:
   try:
      MILDMR.MdmrControlFontInt64W.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILDMR.MdmrControlFontInt64W.restype = None
      MdmrControlFontInt64W = MILDMR.MdmrControlFontInt64W
   except:
      MdmrControlFontInt64W = None
if MILDMR is not None:
   try:
      MILDMR.MdmrControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILDMR.MdmrControlInt64.restype = None
      MdmrControlInt64 = MILDMR.MdmrControlInt64
   except:
      MdmrControlInt64 = None
if MILDMR is not None:
   try:
      MILDMR.MdmrControlStringModelDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_void_p]
      MILDMR.MdmrControlStringModelDouble.restype = None
      MdmrControlStringModelDouble = MILDMR.MdmrControlStringModelDouble
   except:
      MdmrControlStringModelDouble = None
if MILDMR is not None:
   try:
      MILDMR.MdmrControlStringModelInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILDMR.MdmrControlStringModelInt64.restype = None
      MdmrControlStringModelInt64 = MILDMR.MdmrControlStringModelInt64
   except:
      MdmrControlStringModelInt64 = None
if MILDMR is not None:
   try:
      MILDMR.MdmrDraw.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILDMR.MdmrDraw.restype = None
      MdmrDraw = MILDMR.MdmrDraw
   except:
      MdmrDraw = None
if MILDMR is not None:
   try:
      MILDMR.MdmrExportFontW.argtypes = [ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILDMR.MdmrExportFontW.restype = None
      MdmrExportFontW = MILDMR.MdmrExportFontW
   except:
      MdmrExportFontW = None
if MILDMR is not None:
   try:
      MILDMR.MdmrFree.argtypes = [ctypes.c_longlong]
      MILDMR.MdmrFree.restype = None
      MdmrFree = MILDMR.MdmrFree
   except:
      MdmrFree = None
if MILDMR is not None:
   try:
      MILDMR.MdmrGetResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILDMR.MdmrGetResult.restype = None
      MdmrGetResult = MILDMR.MdmrGetResult
   except:
      MdmrGetResult = None
if MILDMR is not None:
   try:
      MILDMR.MdmrImportFontW.argtypes = [ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong]
      MILDMR.MdmrImportFontW.restype = None
      MdmrImportFontW = MILDMR.MdmrImportFontW
   except:
      MdmrImportFontW = None
if MILDMR is not None:
   try:
      MILDMR.MdmrInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILDMR.MdmrInquire.restype = ctypes.c_longlong
      MdmrInquire = MILDMR.MdmrInquire
   except:
      MdmrInquire = None
if MILDMR is not None:
   try:
      MILDMR.MdmrInquireFontW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_void_p]
      MILDMR.MdmrInquireFontW.restype = ctypes.c_longlong
      MdmrInquireFontW = MILDMR.MdmrInquireFontW
   except:
      MdmrInquireFontW = None
if MILDMR is not None:
   try:
      MILDMR.MdmrInquireStringModel.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILDMR.MdmrInquireStringModel.restype = ctypes.c_longlong
      MdmrInquireStringModel = MILDMR.MdmrInquireStringModel
   except:
      MdmrInquireStringModel = None
if MILDMR is not None:
   try:
      MILDMR.MdmrNameW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MILDMR.MdmrNameW.restype = None
      MdmrNameW = MILDMR.MdmrNameW
   except:
      MdmrNameW = None
if MILDMR is not None:
   try:
      MILDMR.MdmrPreprocess.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
      MILDMR.MdmrPreprocess.restype = None
      MdmrPreprocess = MILDMR.MdmrPreprocess
   except:
      MdmrPreprocess = None
if MILDMR is not None:
   try:
      MILDMR.MdmrRead.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILDMR.MdmrRead.restype = None
      MdmrRead = MILDMR.MdmrRead
   except:
      MdmrRead = None
if MILDMR is not None:
   try:
      MILDMR.MdmrRestoreW.argtypes = [ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILDMR.MdmrRestoreW.restype = ctypes.c_longlong
      MdmrRestoreW = MILDMR.MdmrRestoreW
   except:
      MdmrRestoreW = None
if MILDMR is not None:
   try:
      MILDMR.MdmrSaveW.argtypes = [ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong]
      MILDMR.MdmrSaveW.restype = None
      MdmrSaveW = MILDMR.MdmrSaveW
   except:
      MdmrSaveW = None
if MILDMR is not None:
   try:
      MILDMR.MdmrStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MILDMR.MdmrStreamW.restype = None
      MdmrStreamW = MILDMR.MdmrStreamW
   except:
      MdmrStreamW = None
if MILEDGE is not None:
   try:
      MILEDGE.MedgeAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILEDGE.MedgeAlloc.restype = ctypes.c_longlong
      MedgeAlloc = MILEDGE.MedgeAlloc
   except:
      MedgeAlloc = None
if MILEDGE is not None:
   try:
      MILEDGE.MedgeAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILEDGE.MedgeAllocResult.restype = ctypes.c_longlong
      MedgeAllocResult = MILEDGE.MedgeAllocResult
   except:
      MedgeAllocResult = None
if MILEDGE is not None:
   try:
      MILEDGE.MedgeCalculate.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILEDGE.MedgeCalculate.restype = None
      MedgeCalculate = MILEDGE.MedgeCalculate
   except:
      MedgeCalculate = None
if MILEDGE is not None:
   try:
      MILEDGE.MedgeControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILEDGE.MedgeControlDouble.restype = None
      MedgeControlDouble = MILEDGE.MedgeControlDouble
   except:
      MedgeControlDouble = None
if MILEDGE is not None:
   try:
      MILEDGE.MedgeControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILEDGE.MedgeControlInt64.restype = None
      MedgeControlInt64 = MILEDGE.MedgeControlInt64
   except:
      MedgeControlInt64 = None
if MILEDGE is not None:
   try:
      MILEDGE.MedgeDraw.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILEDGE.MedgeDraw.restype = None
      MedgeDraw = MILEDGE.MedgeDraw
   except:
      MedgeDraw = None
if MILEDGE is not None:
   try:
      MILEDGE.MedgeFree.argtypes = [ctypes.c_longlong]
      MILEDGE.MedgeFree.restype = None
      MedgeFree = MILEDGE.MedgeFree
   except:
      MedgeFree = None
if MILEDGE is not None:
   try:
      MILEDGE.MedgeGetNeighbors.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MILEDGE.MedgeGetNeighbors.restype = None
      MedgeGetNeighbors = MILEDGE.MedgeGetNeighbors
   except:
      MedgeGetNeighbors = None
if MILEDGE is not None:
   try:
      MILEDGE.MedgeGetResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p]
      MILEDGE.MedgeGetResult.restype = None
      MedgeGetResult = MILEDGE.MedgeGetResult
   except:
      MedgeGetResult = None
if MILEDGE is not None:
   try:
      MILEDGE.MedgeInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILEDGE.MedgeInquire.restype = ctypes.c_longlong
      MedgeInquire = MILEDGE.MedgeInquire
   except:
      MedgeInquire = None
if MILEDGE is not None:
   try:
      MILEDGE.MedgeMask.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILEDGE.MedgeMask.restype = None
      MedgeMask = MILEDGE.MedgeMask
   except:
      MedgeMask = None
if MILEDGE is not None:
   try:
      MILEDGE.MedgePut.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MILEDGE.MedgePut.restype = None
      MedgePut = MILEDGE.MedgePut
   except:
      MedgePut = None
if MILEDGE is not None:
   try:
      MILEDGE.MedgeRestoreW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILEDGE.MedgeRestoreW.restype = ctypes.c_longlong
      MedgeRestoreW = MILEDGE.MedgeRestoreW
   except:
      MedgeRestoreW = None
if MILEDGE is not None:
   try:
      MILEDGE.MedgeSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILEDGE.MedgeSaveW.restype = None
      MedgeSaveW = MILEDGE.MedgeSaveW
   except:
      MedgeSaveW = None
if MILEDGE is not None:
   try:
      MILEDGE.MedgeSelect.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double]
      MILEDGE.MedgeSelect.restype = None
      MedgeSelect = MILEDGE.MedgeSelect
   except:
      MedgeSelect = None
if MILEDGE is not None:
   try:
      MILEDGE.MedgeStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MILEDGE.MedgeStreamW.restype = None
      MedgeStreamW = MILEDGE.MedgeStreamW
   except:
      MedgeStreamW = None
if MILFPGA is not None:
   try:
      MILFPGA.MfpgaCommandAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILFPGA.MfpgaCommandAlloc.restype = ctypes.c_longlong
      MfpgaCommandAlloc = MILFPGA.MfpgaCommandAlloc
   except:
      MfpgaCommandAlloc = None
if MILFPGA is not None:
   try:
      MILFPGA.MfpgaCommandControl.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILFPGA.MfpgaCommandControl.restype = None
      MfpgaCommandControl = MILFPGA.MfpgaCommandControl
   except:
      MfpgaCommandControl = None
if MILFPGA is not None:
   try:
      MILFPGA.MfpgaCommandFree.argtypes = [ctypes.c_void_p, ctypes.c_longlong]
      MILFPGA.MfpgaCommandFree.restype = ctypes.c_longlong
      MfpgaCommandFree = MILFPGA.MfpgaCommandFree
   except:
      MfpgaCommandFree = None
if MILFPGA is not None:
   try:
      MILFPGA.MfpgaCommandInquire.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILFPGA.MfpgaCommandInquire.restype = None
      MfpgaCommandInquire = MILFPGA.MfpgaCommandInquire
   except:
      MfpgaCommandInquire = None
if MILFPGA is not None:
   try:
      MILFPGA.MfpgaCommandQueue.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILFPGA.MfpgaCommandQueue.restype = None
      MfpgaCommandQueue = MILFPGA.MfpgaCommandQueue
   except:
      MfpgaCommandQueue = None
if MILFPGA is not None:
   try:
      MILFPGA.MfpgaControl.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILFPGA.MfpgaControl.restype = ctypes.c_longlong
      MfpgaControl = MILFPGA.MfpgaControl
   except:
      MfpgaControl = None
if MILFPGA is not None:
   try:
      MILFPGA.MfpgaGetHookInfo.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILFPGA.MfpgaGetHookInfo.restype = ctypes.c_longlong
      MfpgaGetHookInfo = MILFPGA.MfpgaGetHookInfo
   except:
      MfpgaGetHookInfo = None
if MILFPGA is not None:
   try:
      MILFPGA.MfpgaGetRegister.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong]
      MILFPGA.MfpgaGetRegister.restype = None
      MfpgaGetRegister = MILFPGA.MfpgaGetRegister
   except:
      MfpgaGetRegister = None
if MILFPGA is not None:
   try:
      MILFPGA.MfpgaHookFunction.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, MIL_FPGA_HOOK_FUNCTION_PTR, ctypes.c_void_p]
      MILFPGA.MfpgaHookFunction.restype = None
      MfpgaHookFunction = MILFPGA.MfpgaHookFunction
   except:
      MfpgaHookFunction = None
if MILFPGA is not None:
   try:
      MILFPGA.MfpgaInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILFPGA.MfpgaInquire.restype = ctypes.c_longlong
      MfpgaInquire = MILFPGA.MfpgaInquire
   except:
      MfpgaInquire = None
if MILFPGA is not None:
   try:
      MILFPGA.MfpgaLoadW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong]
      MILFPGA.MfpgaLoadW.restype = ctypes.c_longlong
      MfpgaLoadW = MILFPGA.MfpgaLoadW
   except:
      MfpgaLoadW = None
if MILFPGA is not None:
   try:
      MILFPGA.MfpgaSetDestination.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILFPGA.MfpgaSetDestination.restype = None
      MfpgaSetDestination = MILFPGA.MfpgaSetDestination
   except:
      MfpgaSetDestination = None
if MILFPGA is not None:
   try:
      MILFPGA.MfpgaSetLink.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILFPGA.MfpgaSetLink.restype = None
      MfpgaSetLink = MILFPGA.MfpgaSetLink
   except:
      MfpgaSetLink = None
if MILFPGA is not None:
   try:
      MILFPGA.MfpgaSetRegister.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong]
      MILFPGA.MfpgaSetRegister.restype = None
      MfpgaSetRegister = MILFPGA.MfpgaSetRegister
   except:
      MfpgaSetRegister = None
if MILFPGA is not None:
   try:
      MILFPGA.MfpgaSetSource.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILFPGA.MfpgaSetSource.restype = None
      MfpgaSetSource = MILFPGA.MfpgaSetSource
   except:
      MfpgaSetSource = None
if MIL is not None:
   try:
      MIL.MfuncAllocId.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MfuncAllocId.restype = ctypes.c_longlong
      MfuncAllocId = MIL.MfuncAllocId
   except:
      MfuncAllocId = None
if MIL is not None:
   try:
      MIL.MfuncAllocScriptW.argtypes = [ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL.MfuncAllocScriptW.restype = ctypes.c_longlong
      MfuncAllocScriptW = MIL.MfuncAllocScriptW
   except:
      MfuncAllocScriptW = None
if MIL is not None:
   try:
      MIL.MfuncAllocW.argtypes = [ctypes.c_wchar_p, ctypes.c_longlong, MIL_FUNC_FUNCTION_PTR, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MfuncAllocW.restype = ctypes.c_longlong
      MfuncAllocW = MIL.MfuncAllocW
   except:
      MfuncAllocW = None
if MIL is not None:
   try:
      MIL.MfuncBufAncestorId.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufAncestorId.restype = ctypes.c_longlong
      MfuncBufAncestorId = MIL.MfuncBufAncestorId
   except:
      MfuncBufAncestorId = None
if MIL is not None:
   try:
      MIL.MfuncBufAncestorOffsetBand.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufAncestorOffsetBand.restype = ctypes.c_longlong
      MfuncBufAncestorOffsetBand = MIL.MfuncBufAncestorOffsetBand
   except:
      MfuncBufAncestorOffsetBand = None
if MIL is not None:
   try:
      MIL.MfuncBufAncestorOffsetBit.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufAncestorOffsetBit.restype = ctypes.c_longlong
      MfuncBufAncestorOffsetBit = MIL.MfuncBufAncestorOffsetBit
   except:
      MfuncBufAncestorOffsetBit = None
if MIL is not None:
   try:
      MIL.MfuncBufAncestorOffsetX.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufAncestorOffsetX.restype = ctypes.c_longlong
      MfuncBufAncestorOffsetX = MIL.MfuncBufAncestorOffsetX
   except:
      MfuncBufAncestorOffsetX = None
if MIL is not None:
   try:
      MIL.MfuncBufAncestorOffsetY.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufAncestorOffsetY.restype = ctypes.c_longlong
      MfuncBufAncestorOffsetY = MIL.MfuncBufAncestorOffsetY
   except:
      MfuncBufAncestorOffsetY = None
if MIL is not None:
   try:
      MIL.MfuncBufAttribute.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufAttribute.restype = ctypes.c_longlong
      MfuncBufAttribute = MIL.MfuncBufAttribute
   except:
      MfuncBufAttribute = None
if MIL is not None:
   try:
      MIL.MfuncBufFormat.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufFormat.restype = ctypes.c_longlong
      MfuncBufFormat = MIL.MfuncBufFormat
   except:
      MfuncBufFormat = None
if MIL is not None:
   try:
      MIL.MfuncBufHostAddress.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufHostAddress.restype = None
      MfuncBufHostAddress = MIL.MfuncBufHostAddress
   except:
      MfuncBufHostAddress = None
if MIL is not None:
   try:
      MIL.MfuncBufHostAddressBand.argtypes = [ctypes.c_void_p, ctypes.c_longlong]
      MIL.MfuncBufHostAddressBand.restype = None
      MfuncBufHostAddressBand = MIL.MfuncBufHostAddressBand
   except:
      MfuncBufHostAddressBand = None
if MIL is not None:
   try:
      MIL.MfuncBufId.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufId.restype = ctypes.c_longlong
      MfuncBufId = MIL.MfuncBufId
   except:
      MfuncBufId = None
if MIL is not None:
   try:
      MIL.MfuncBufMaxValue.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufMaxValue.restype = ctypes.c_double
      MfuncBufMaxValue = MIL.MfuncBufMaxValue
   except:
      MfuncBufMaxValue = None
if MIL is not None:
   try:
      MIL.MfuncBufMinValue.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufMinValue.restype = ctypes.c_double
      MfuncBufMinValue = MIL.MfuncBufMinValue
   except:
      MfuncBufMinValue = None
if MIL is not None:
   try:
      MIL.MfuncBufOwnerSystemId.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufOwnerSystemId.restype = ctypes.c_longlong
      MfuncBufOwnerSystemId = MIL.MfuncBufOwnerSystemId
   except:
      MfuncBufOwnerSystemId = None
if MIL is not None:
   try:
      MIL.MfuncBufOwnerSystemType.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufOwnerSystemType.restype = ctypes.c_longlong
      MfuncBufOwnerSystemType = MIL.MfuncBufOwnerSystemType
   except:
      MfuncBufOwnerSystemType = None
if MIL is not None:
   try:
      MIL.MfuncBufParentId.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufParentId.restype = ctypes.c_longlong
      MfuncBufParentId = MIL.MfuncBufParentId
   except:
      MfuncBufParentId = None
if MIL is not None:
   try:
      MIL.MfuncBufParentOffsetBand.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufParentOffsetBand.restype = ctypes.c_longlong
      MfuncBufParentOffsetBand = MIL.MfuncBufParentOffsetBand
   except:
      MfuncBufParentOffsetBand = None
if MIL is not None:
   try:
      MIL.MfuncBufParentOffsetX.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufParentOffsetX.restype = ctypes.c_longlong
      MfuncBufParentOffsetX = MIL.MfuncBufParentOffsetX
   except:
      MfuncBufParentOffsetX = None
if MIL is not None:
   try:
      MIL.MfuncBufParentOffsetY.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufParentOffsetY.restype = ctypes.c_longlong
      MfuncBufParentOffsetY = MIL.MfuncBufParentOffsetY
   except:
      MfuncBufParentOffsetY = None
if MIL is not None:
   try:
      MIL.MfuncBufPhysicalAddress.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufPhysicalAddress.restype = ctypes.c_ulonglong
      MfuncBufPhysicalAddress = MIL.MfuncBufPhysicalAddress
   except:
      MfuncBufPhysicalAddress = None
if MIL is not None:
   try:
      MIL.MfuncBufPhysicalAddressBand.argtypes = [ctypes.c_void_p, ctypes.c_longlong]
      MIL.MfuncBufPhysicalAddressBand.restype = ctypes.c_ulonglong
      MfuncBufPhysicalAddressBand = MIL.MfuncBufPhysicalAddressBand
   except:
      MfuncBufPhysicalAddressBand = None
if MIL is not None:
   try:
      MIL.MfuncBufPitch.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufPitch.restype = ctypes.c_longlong
      MfuncBufPitch = MIL.MfuncBufPitch
   except:
      MfuncBufPitch = None
if MIL is not None:
   try:
      MIL.MfuncBufPitchByte.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufPitchByte.restype = ctypes.c_longlong
      MfuncBufPitchByte = MIL.MfuncBufPitchByte
   except:
      MfuncBufPitchByte = None
if MIL is not None:
   try:
      MIL.MfuncBufSizeBand.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufSizeBand.restype = ctypes.c_longlong
      MfuncBufSizeBand = MIL.MfuncBufSizeBand
   except:
      MfuncBufSizeBand = None
if MIL is not None:
   try:
      MIL.MfuncBufSizeBit.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufSizeBit.restype = ctypes.c_longlong
      MfuncBufSizeBit = MIL.MfuncBufSizeBit
   except:
      MfuncBufSizeBit = None
if MIL is not None:
   try:
      MIL.MfuncBufSizeX.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufSizeX.restype = ctypes.c_longlong
      MfuncBufSizeX = MIL.MfuncBufSizeX
   except:
      MfuncBufSizeX = None
if MIL is not None:
   try:
      MIL.MfuncBufSizeY.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufSizeY.restype = ctypes.c_longlong
      MfuncBufSizeY = MIL.MfuncBufSizeY
   except:
      MfuncBufSizeY = None
if MIL is not None:
   try:
      MIL.MfuncBufType.argtypes = [ctypes.c_void_p]
      MIL.MfuncBufType.restype = ctypes.c_longlong
      MfuncBufType = MIL.MfuncBufType
   except:
      MfuncBufType = None
if MIL is not None:
   try:
      MIL.MfuncCall.argtypes = [ctypes.c_longlong]
      MIL.MfuncCall.restype = ctypes.c_longlong
      MfuncCall = MIL.MfuncCall
   except:
      MfuncCall = None
if MIL is not None:
   try:
      MIL.MfuncControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MfuncControlDouble.restype = None
      MfuncControlDouble = MIL.MfuncControlDouble
   except:
      MfuncControlDouble = None
if MIL is not None:
   try:
      MIL.MfuncControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncControlInt64.restype = None
      MfuncControlInt64 = MIL.MfuncControlInt64
   except:
      MfuncControlInt64 = None
if MIL is not None:
   try:
      MIL.MfuncErrorReportW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p]
      MIL.MfuncErrorReportW.restype = ctypes.c_longlong
      MfuncErrorReportW = MIL.MfuncErrorReportW
   except:
      MfuncErrorReportW = None
if MIL is not None:
   try:
      MIL.MfuncFree.argtypes = [ctypes.c_longlong]
      MIL.MfuncFree.restype = None
      MfuncFree = MIL.MfuncFree
   except:
      MfuncFree = None
if MIL is not None:
   try:
      MIL.MfuncFreeId.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncFreeId.restype = None
      MfuncFreeId = MIL.MfuncFreeId
   except:
      MfuncFreeId = None
if MIL is not None:
   try:
      MIL.MfuncInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MfuncInquire.restype = ctypes.c_longlong
      MfuncInquire = MIL.MfuncInquire
   except:
      MfuncInquire = None
if MIL is not None:
   try:
      MIL.MfuncParamArrayMilDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamArrayMilDouble.restype = None
      MfuncParamArrayMilDouble = MIL.MfuncParamArrayMilDouble
   except:
      MfuncParamArrayMilDouble = None
if MIL is not None:
   try:
      MIL.MfuncParamArrayMilId.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamArrayMilId.restype = None
      MfuncParamArrayMilId = MIL.MfuncParamArrayMilId
   except:
      MfuncParamArrayMilId = None
if MIL is not None:
   try:
      MIL.MfuncParamArrayMilInt.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamArrayMilInt.restype = None
      MfuncParamArrayMilInt = MIL.MfuncParamArrayMilInt
   except:
      MfuncParamArrayMilInt = None
if MIL is not None:
   try:
      MIL.MfuncParamArrayMilInt32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_long), ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamArrayMilInt32.restype = None
      MfuncParamArrayMilInt32 = MIL.MfuncParamArrayMilInt32
   except:
      MfuncParamArrayMilInt32 = None
if MIL is not None:
   try:
      MIL.MfuncParamArrayMilInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamArrayMilInt64.restype = None
      MfuncParamArrayMilInt64 = MIL.MfuncParamArrayMilInt64
   except:
      MfuncParamArrayMilInt64 = None
if MIL is not None:
   try:
      MIL.MfuncParamArrayMilUint.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_ulonglong), ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamArrayMilUint.restype = None
      MfuncParamArrayMilUint = MIL.MfuncParamArrayMilUint
   except:
      MfuncParamArrayMilUint = None
if MIL is not None:
   try:
      MIL.MfuncParamArrayMilUint32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_ulong), ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamArrayMilUint32.restype = None
      MfuncParamArrayMilUint32 = MIL.MfuncParamArrayMilUint32
   except:
      MfuncParamArrayMilUint32 = None
if MIL is not None:
   try:
      MIL.MfuncParamArrayMilUint64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_ulonglong), ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamArrayMilUint64.restype = None
      MfuncParamArrayMilUint64 = MIL.MfuncParamArrayMilUint64
   except:
      MfuncParamArrayMilUint64 = None
if MIL is not None:
   try:
      MIL.MfuncParamCheck.argtypes = [ctypes.c_longlong]
      MIL.MfuncParamCheck.restype = ctypes.c_longlong
      MfuncParamCheck = MIL.MfuncParamCheck
   except:
      MfuncParamCheck = None
if MIL is not None:
   try:
      MIL.MfuncParamConstArrayMilDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamConstArrayMilDouble.restype = None
      MfuncParamConstArrayMilDouble = MIL.MfuncParamConstArrayMilDouble
   except:
      MfuncParamConstArrayMilDouble = None
if MIL is not None:
   try:
      MIL.MfuncParamConstArrayMilId.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamConstArrayMilId.restype = None
      MfuncParamConstArrayMilId = MIL.MfuncParamConstArrayMilId
   except:
      MfuncParamConstArrayMilId = None
if MIL is not None:
   try:
      MIL.MfuncParamConstArrayMilInt.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamConstArrayMilInt.restype = None
      MfuncParamConstArrayMilInt = MIL.MfuncParamConstArrayMilInt
   except:
      MfuncParamConstArrayMilInt = None
if MIL is not None:
   try:
      MIL.MfuncParamConstArrayMilInt32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_long), ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamConstArrayMilInt32.restype = None
      MfuncParamConstArrayMilInt32 = MIL.MfuncParamConstArrayMilInt32
   except:
      MfuncParamConstArrayMilInt32 = None
if MIL is not None:
   try:
      MIL.MfuncParamConstArrayMilInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamConstArrayMilInt64.restype = None
      MfuncParamConstArrayMilInt64 = MIL.MfuncParamConstArrayMilInt64
   except:
      MfuncParamConstArrayMilInt64 = None
if MIL is not None:
   try:
      MIL.MfuncParamConstArrayMilUint.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_ulonglong), ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamConstArrayMilUint.restype = None
      MfuncParamConstArrayMilUint = MIL.MfuncParamConstArrayMilUint
   except:
      MfuncParamConstArrayMilUint = None
if MIL is not None:
   try:
      MIL.MfuncParamConstArrayMilUint32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_ulong), ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamConstArrayMilUint32.restype = None
      MfuncParamConstArrayMilUint32 = MIL.MfuncParamConstArrayMilUint32
   except:
      MfuncParamConstArrayMilUint32 = None
if MIL is not None:
   try:
      MIL.MfuncParamConstArrayMilUint64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_ulonglong), ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamConstArrayMilUint64.restype = None
      MfuncParamConstArrayMilUint64 = MIL.MfuncParamConstArrayMilUint64
   except:
      MfuncParamConstArrayMilUint64 = None
if MIL is not None:
   try:
      MIL.MfuncParamConstDataPointer.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamConstDataPointer.restype = None
      MfuncParamConstDataPointer = MIL.MfuncParamConstDataPointer
   except:
      MfuncParamConstDataPointer = None
if MIL is not None:
   try:
      MIL.MfuncParamConstMilTextW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamConstMilTextW.restype = None
      MfuncParamConstMilTextW = MIL.MfuncParamConstMilTextW
   except:
      MfuncParamConstMilTextW = None
if MIL is not None:
   try:
      MIL.MfuncParamDataPointer.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamDataPointer.restype = None
      MfuncParamDataPointer = MIL.MfuncParamDataPointer
   except:
      MfuncParamDataPointer = None
if MIL is not None:
   try:
      MIL.MfuncParamFilenameW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamFilenameW.restype = None
      MfuncParamFilenameW = MIL.MfuncParamFilenameW
   except:
      MfuncParamFilenameW = None
if MIL is not None:
   try:
      MIL.MfuncParamMilDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MfuncParamMilDouble.restype = None
      MfuncParamMilDouble = MIL.MfuncParamMilDouble
   except:
      MfuncParamMilDouble = None
if MIL is not None:
   try:
      MIL.MfuncParamMilId.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamMilId.restype = None
      MfuncParamMilId = MIL.MfuncParamMilId
   except:
      MfuncParamMilId = None
if MIL is not None:
   try:
      MIL.MfuncParamMilInt.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamMilInt.restype = None
      MfuncParamMilInt = MIL.MfuncParamMilInt
   except:
      MfuncParamMilInt = None
if MIL is not None:
   try:
      MIL.MfuncParamMilInt32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_long]
      MIL.MfuncParamMilInt32.restype = None
      MfuncParamMilInt32 = MIL.MfuncParamMilInt32
   except:
      MfuncParamMilInt32 = None
if MIL is not None:
   try:
      MIL.MfuncParamMilInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamMilInt64.restype = None
      MfuncParamMilInt64 = MIL.MfuncParamMilInt64
   except:
      MfuncParamMilInt64 = None
if MIL is not None:
   try:
      MIL.MfuncParamMilTextW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamMilTextW.restype = None
      MfuncParamMilTextW = MIL.MfuncParamMilTextW
   except:
      MfuncParamMilTextW = None
if MIL is not None:
   try:
      MIL.MfuncParamMilUint.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_ulonglong]
      MIL.MfuncParamMilUint.restype = None
      MfuncParamMilUint = MIL.MfuncParamMilUint
   except:
      MfuncParamMilUint = None
if MIL is not None:
   try:
      MIL.MfuncParamMilUint32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_ulong]
      MIL.MfuncParamMilUint32.restype = None
      MfuncParamMilUint32 = MIL.MfuncParamMilUint32
   except:
      MfuncParamMilUint32 = None
if MIL is not None:
   try:
      MIL.MfuncParamMilUint64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_ulonglong]
      MIL.MfuncParamMilUint64.restype = None
      MfuncParamMilUint64 = MIL.MfuncParamMilUint64
   except:
      MfuncParamMilUint64 = None
if MIL is not None:
   try:
      MIL.MfuncParamValue.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MfuncParamValue.restype = None
      MfuncParamValue = MIL.MfuncParamValue
   except:
      MfuncParamValue = None
if MIL is not None:
   try:
      MIL.MfuncParamValueArrayMilDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_void_p)]
      MIL.MfuncParamValueArrayMilDouble.restype = None
      MfuncParamValueArrayMilDouble = MIL.MfuncParamValueArrayMilDouble
   except:
      MfuncParamValueArrayMilDouble = None
if MIL is not None:
   try:
      MIL.MfuncParamValueArrayMilId.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_void_p)]
      MIL.MfuncParamValueArrayMilId.restype = None
      MfuncParamValueArrayMilId = MIL.MfuncParamValueArrayMilId
   except:
      MfuncParamValueArrayMilId = None
if MIL is not None:
   try:
      MIL.MfuncParamValueArrayMilInt.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_void_p)]
      MIL.MfuncParamValueArrayMilInt.restype = None
      MfuncParamValueArrayMilInt = MIL.MfuncParamValueArrayMilInt
   except:
      MfuncParamValueArrayMilInt = None
if MIL is not None:
   try:
      MIL.MfuncParamValueArrayMilInt32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_void_p)]
      MIL.MfuncParamValueArrayMilInt32.restype = None
      MfuncParamValueArrayMilInt32 = MIL.MfuncParamValueArrayMilInt32
   except:
      MfuncParamValueArrayMilInt32 = None
if MIL is not None:
   try:
      MIL.MfuncParamValueArrayMilInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_void_p)]
      MIL.MfuncParamValueArrayMilInt64.restype = None
      MfuncParamValueArrayMilInt64 = MIL.MfuncParamValueArrayMilInt64
   except:
      MfuncParamValueArrayMilInt64 = None
if MIL is not None:
   try:
      MIL.MfuncParamValueArrayMilUint.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_void_p)]
      MIL.MfuncParamValueArrayMilUint.restype = None
      MfuncParamValueArrayMilUint = MIL.MfuncParamValueArrayMilUint
   except:
      MfuncParamValueArrayMilUint = None
if MIL is not None:
   try:
      MIL.MfuncParamValueArrayMilUint32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_void_p)]
      MIL.MfuncParamValueArrayMilUint32.restype = None
      MfuncParamValueArrayMilUint32 = MIL.MfuncParamValueArrayMilUint32
   except:
      MfuncParamValueArrayMilUint32 = None
if MIL is not None:
   try:
      MIL.MfuncParamValueArrayMilUint64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_void_p)]
      MIL.MfuncParamValueArrayMilUint64.restype = None
      MfuncParamValueArrayMilUint64 = MIL.MfuncParamValueArrayMilUint64
   except:
      MfuncParamValueArrayMilUint64 = None
if MIL is not None:
   try:
      MIL.MfuncParamValueConstArrayMilDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_void_p)]
      MIL.MfuncParamValueConstArrayMilDouble.restype = None
      MfuncParamValueConstArrayMilDouble = MIL.MfuncParamValueConstArrayMilDouble
   except:
      MfuncParamValueConstArrayMilDouble = None
if MIL is not None:
   try:
      MIL.MfuncParamValueConstArrayMilId.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_void_p)]
      MIL.MfuncParamValueConstArrayMilId.restype = None
      MfuncParamValueConstArrayMilId = MIL.MfuncParamValueConstArrayMilId
   except:
      MfuncParamValueConstArrayMilId = None
if MIL is not None:
   try:
      MIL.MfuncParamValueConstArrayMilInt.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_void_p)]
      MIL.MfuncParamValueConstArrayMilInt.restype = None
      MfuncParamValueConstArrayMilInt = MIL.MfuncParamValueConstArrayMilInt
   except:
      MfuncParamValueConstArrayMilInt = None
if MIL is not None:
   try:
      MIL.MfuncParamValueConstArrayMilInt32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_void_p)]
      MIL.MfuncParamValueConstArrayMilInt32.restype = None
      MfuncParamValueConstArrayMilInt32 = MIL.MfuncParamValueConstArrayMilInt32
   except:
      MfuncParamValueConstArrayMilInt32 = None
if MIL is not None:
   try:
      MIL.MfuncParamValueConstArrayMilInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_void_p)]
      MIL.MfuncParamValueConstArrayMilInt64.restype = None
      MfuncParamValueConstArrayMilInt64 = MIL.MfuncParamValueConstArrayMilInt64
   except:
      MfuncParamValueConstArrayMilInt64 = None
if MIL is not None:
   try:
      MIL.MfuncParamValueConstArrayMilUint.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_void_p)]
      MIL.MfuncParamValueConstArrayMilUint.restype = None
      MfuncParamValueConstArrayMilUint = MIL.MfuncParamValueConstArrayMilUint
   except:
      MfuncParamValueConstArrayMilUint = None
if MIL is not None:
   try:
      MIL.MfuncParamValueConstArrayMilUint32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_void_p)]
      MIL.MfuncParamValueConstArrayMilUint32.restype = None
      MfuncParamValueConstArrayMilUint32 = MIL.MfuncParamValueConstArrayMilUint32
   except:
      MfuncParamValueConstArrayMilUint32 = None
if MIL is not None:
   try:
      MIL.MfuncParamValueConstArrayMilUint64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_void_p)]
      MIL.MfuncParamValueConstArrayMilUint64.restype = None
      MfuncParamValueConstArrayMilUint64 = MIL.MfuncParamValueConstArrayMilUint64
   except:
      MfuncParamValueConstArrayMilUint64 = None
if MIL is not None:
   try:
      MIL.MfuncParamValueConstMilTextW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p]
      MIL.MfuncParamValueConstMilTextW.restype = None
      MfuncParamValueConstMilTextW = MIL.MfuncParamValueConstMilTextW
   except:
      MfuncParamValueConstMilTextW = None
if MIL is not None:
   try:
      MIL.MfuncParamValueFilenameW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p]
      MIL.MfuncParamValueFilenameW.restype = None
      MfuncParamValueFilenameW = MIL.MfuncParamValueFilenameW
   except:
      MfuncParamValueFilenameW = None
if MIL is not None:
   try:
      MIL.MfuncParamValueMilDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double)]
      MIL.MfuncParamValueMilDouble.restype = None
      MfuncParamValueMilDouble = MIL.MfuncParamValueMilDouble
   except:
      MfuncParamValueMilDouble = None
if MIL is not None:
   try:
      MIL.MfuncParamValueMilId.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL.MfuncParamValueMilId.restype = None
      MfuncParamValueMilId = MIL.MfuncParamValueMilId
   except:
      MfuncParamValueMilId = None
if MIL is not None:
   try:
      MIL.MfuncParamValueMilInt.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL.MfuncParamValueMilInt.restype = None
      MfuncParamValueMilInt = MIL.MfuncParamValueMilInt
   except:
      MfuncParamValueMilInt = None
if MIL is not None:
   try:
      MIL.MfuncParamValueMilInt32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_long)]
      MIL.MfuncParamValueMilInt32.restype = None
      MfuncParamValueMilInt32 = MIL.MfuncParamValueMilInt32
   except:
      MfuncParamValueMilInt32 = None
if MIL is not None:
   try:
      MIL.MfuncParamValueMilInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL.MfuncParamValueMilInt64.restype = None
      MfuncParamValueMilInt64 = MIL.MfuncParamValueMilInt64
   except:
      MfuncParamValueMilInt64 = None
if MIL is not None:
   try:
      MIL.MfuncParamValueMilTextW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p]
      MIL.MfuncParamValueMilTextW.restype = None
      MfuncParamValueMilTextW = MIL.MfuncParamValueMilTextW
   except:
      MfuncParamValueMilTextW = None
if MIL is not None:
   try:
      MIL.MfuncParamValueMilUint.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_ulonglong)]
      MIL.MfuncParamValueMilUint.restype = None
      MfuncParamValueMilUint = MIL.MfuncParamValueMilUint
   except:
      MfuncParamValueMilUint = None
if MIL is not None:
   try:
      MIL.MfuncParamValueMilUint32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_ulong)]
      MIL.MfuncParamValueMilUint32.restype = None
      MfuncParamValueMilUint32 = MIL.MfuncParamValueMilUint32
   except:
      MfuncParamValueMilUint32 = None
if MIL is not None:
   try:
      MIL.MfuncParamValueMilUint64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_ulonglong)]
      MIL.MfuncParamValueMilUint64.restype = None
      MfuncParamValueMilUint64 = MIL.MfuncParamValueMilUint64
   except:
      MfuncParamValueMilUint64 = None
if MIL is not None:
   try:
      MIL.MfuncParamW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_ulonglong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MfuncParamW.restype = None
      MfuncParamW = MIL.MfuncParamW
   except:
      MfuncParamW = None
if MIL is not None:
   try:
      MIL.MgenLutFunction.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong]
      MIL.MgenLutFunction.restype = None
      MgenLutFunction = MIL.MgenLutFunction
   except:
      MgenLutFunction = None
if MIL is not None:
   try:
      MIL.MgenLutRamp.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.c_double]
      MIL.MgenLutRamp.restype = None
      MgenLutRamp = MIL.MgenLutRamp
   except:
      MgenLutRamp = None
if MIL is not None:
   try:
      MIL.MgenRamp.argtypes = [ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL.MgenRamp.restype = None
      MgenRamp = MIL.MgenRamp
   except:
      MgenRamp = None
if MIL is not None:
   try:
      MIL.MgenWarpParameter.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double]
      MIL.MgenWarpParameter.restype = None
      MgenWarpParameter = MIL.MgenWarpParameter
   except:
      MgenWarpParameter = None
if MIL is not None:
   try:
      MIL.MgraAlloc.argtypes = [ctypes.c_longlong, ctypes.c_void_p]
      MIL.MgraAlloc.restype = ctypes.c_longlong
      MgraAlloc = MIL.MgraAlloc
   except:
      MgraAlloc = None
if MIL is not None:
   try:
      MIL.MgraAllocList.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MgraAllocList.restype = ctypes.c_longlong
      MgraAllocList = MIL.MgraAllocList
   except:
      MgraAllocList = None
if MIL is not None:
   try:
      MIL.MgraArcAngleDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL.MgraArcAngleDouble.restype = None
      MgraArcAngleDouble = MIL.MgraArcAngleDouble
   except:
      MgraArcAngleDouble = None
if MIL is not None:
   try:
      MIL.MgraArcAngleInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL.MgraArcAngleInt64.restype = None
      MgraArcAngleInt64 = MIL.MgraArcAngleInt64
   except:
      MgraArcAngleInt64 = None
if MIL is not None:
   try:
      MIL.MgraArcDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
      MIL.MgraArcDouble.restype = None
      MgraArcDouble = MIL.MgraArcDouble
   except:
      MgraArcDouble = None
if MIL is not None:
   try:
      MIL.MgraArcFillDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
      MIL.MgraArcFillDouble.restype = None
      MgraArcFillDouble = MIL.MgraArcFillDouble
   except:
      MgraArcFillDouble = None
if MIL is not None:
   try:
      MIL.MgraArcFillInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double]
      MIL.MgraArcFillInt64.restype = None
      MgraArcFillInt64 = MIL.MgraArcFillInt64
   except:
      MgraArcFillInt64 = None
if MIL is not None:
   try:
      MIL.MgraArcInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double]
      MIL.MgraArcInt64.restype = None
      MgraArcInt64 = MIL.MgraArcInt64
   except:
      MgraArcInt64 = None
if MIL is not None:
   try:
      MIL.MgraBackColorDouble.argtypes = [ctypes.c_longlong, ctypes.c_double]
      MIL.MgraBackColorDouble.restype = None
      MgraBackColorDouble = MIL.MgraBackColorDouble
   except:
      MgraBackColorDouble = None
if MIL is not None:
   try:
      MIL.MgraClear.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
      MIL.MgraClear.restype = None
      MgraClear = MIL.MgraClear
   except:
      MgraClear = None
if MIL is not None:
   try:
      MIL.MgraColorDouble.argtypes = [ctypes.c_longlong, ctypes.c_double]
      MIL.MgraColorDouble.restype = None
      MgraColorDouble = MIL.MgraColorDouble
   except:
      MgraColorDouble = None
if MIL is not None:
   try:
      MIL.MgraControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MgraControlDouble.restype = None
      MgraControlDouble = MIL.MgraControlDouble
   except:
      MgraControlDouble = None
if MIL is not None:
   try:
      MIL.MgraControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MgraControlInt64.restype = None
      MgraControlInt64 = MIL.MgraControlInt64
   except:
      MgraControlInt64 = None
if MIL is not None:
   try:
      MIL.MgraControlListDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MgraControlListDouble.restype = None
      MgraControlListDouble = MIL.MgraControlListDouble
   except:
      MgraControlListDouble = None
if MIL is not None:
   try:
      MIL.MgraControlListInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MgraControlListInt64.restype = None
      MgraControlListInt64 = MIL.MgraControlListInt64
   except:
      MgraControlListInt64 = None
if MIL is not None:
   try:
      MIL.MgraCopy.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MIL.MgraCopy.restype = None
      MgraCopy = MIL.MgraCopy
   except:
      MgraCopy = None
if MIL is not None:
   try:
      MIL.MgraDotDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double]
      MIL.MgraDotDouble.restype = None
      MgraDotDouble = MIL.MgraDotDouble
   except:
      MgraDotDouble = None
if MIL is not None:
   try:
      MIL.MgraDotInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MgraDotInt64.restype = None
      MgraDotInt64 = MIL.MgraDotInt64
   except:
      MgraDotInt64 = None
if MIL is not None:
   try:
      MIL.MgraDotsDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_longlong]
      MIL.MgraDotsDouble.restype = None
      MgraDotsDouble = MIL.MgraDotsDouble
   except:
      MgraDotsDouble = None
if MIL is not None:
   try:
      MIL.MgraDotsInt32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_longlong]
      MIL.MgraDotsInt32.restype = None
      MgraDotsInt32 = MIL.MgraDotsInt32
   except:
      MgraDotsInt32 = None
if MIL is not None:
   try:
      MIL.MgraDotsInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong]
      MIL.MgraDotsInt64.restype = None
      MgraDotsInt64 = MIL.MgraDotsInt64
   except:
      MgraDotsInt64 = None
if MIL is not None:
   try:
      MIL.MgraDraw.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MgraDraw.restype = None
      MgraDraw = MIL.MgraDraw
   except:
      MgraDraw = None
if MIL is not None:
   try:
      MIL.MgraFillDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double]
      MIL.MgraFillDouble.restype = None
      MgraFillDouble = MIL.MgraFillDouble
   except:
      MgraFillDouble = None
if MIL is not None:
   try:
      MIL.MgraFillInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MgraFillInt64.restype = None
      MgraFillInt64 = MIL.MgraFillInt64
   except:
      MgraFillInt64 = None
if MIL is not None:
   try:
      MIL.MgraFontScale.argtypes = [ctypes.c_longlong, ctypes.c_double, ctypes.c_double]
      MIL.MgraFontScale.restype = None
      MgraFontScale = MIL.MgraFontScale
   except:
      MgraFontScale = None
if MIL is not None:
   try:
      MIL.MgraFontW.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
      MIL.MgraFontW.restype = None
      MgraFontW = MIL.MgraFontW
   except:
      MgraFontW = None
if MIL is not None:
   try:
      MIL.MgraFree.argtypes = [ctypes.c_longlong]
      MIL.MgraFree.restype = None
      MgraFree = MIL.MgraFree
   except:
      MgraFree = None
if MIL is not None:
   try:
      MIL.MgraGetHookInfo.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MgraGetHookInfo.restype = ctypes.c_longlong
      MgraGetHookInfo = MIL.MgraGetHookInfo
   except:
      MgraGetHookInfo = None
if MIL is not None:
   try:
      MIL.MgraHookFunction.argtypes = [ctypes.c_longlong, ctypes.c_longlong, MIL_GRA_HOOK_FUNCTION_PTR, ctypes.c_void_p]
      MIL.MgraHookFunction.restype = None
      MgraHookFunction = MIL.MgraHookFunction
   except:
      MgraHookFunction = None
if MIL is not None:
   try:
      MIL.MgraInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MgraInquire.restype = ctypes.c_longlong
      MgraInquire = MIL.MgraInquire
   except:
      MgraInquire = None
if MIL is not None:
   try:
      MIL.MgraInquireList.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MgraInquireList.restype = ctypes.c_longlong
      MgraInquireList = MIL.MgraInquireList
   except:
      MgraInquireList = None
if MIL is not None:
   try:
      MIL.MgraInteractive.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MgraInteractive.restype = None
      MgraInteractive = MIL.MgraInteractive
   except:
      MgraInteractive = None
if MIL is not None:
   try:
      MIL.MgraLineDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
      MIL.MgraLineDouble.restype = None
      MgraLineDouble = MIL.MgraLineDouble
   except:
      MgraLineDouble = None
if MIL is not None:
   try:
      MIL.MgraLineInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MgraLineInt64.restype = None
      MgraLineInt64 = MIL.MgraLineInt64
   except:
      MgraLineInt64 = None
if MIL is not None:
   try:
      MIL.MgraLinesDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MIL.MgraLinesDouble.restype = None
      MgraLinesDouble = MIL.MgraLinesDouble
   except:
      MgraLinesDouble = None
if MIL is not None:
   try:
      MIL.MgraLinesInt32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MIL.MgraLinesInt32.restype = None
      MgraLinesInt32 = MIL.MgraLinesInt32
   except:
      MgraLinesInt32 = None
if MIL is not None:
   try:
      MIL.MgraLinesInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MIL.MgraLinesInt64.restype = None
      MgraLinesInt64 = MIL.MgraLinesInt64
   except:
      MgraLinesInt64 = None
if MIL is not None:
   try:
      MIL.MgraRectAngleDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MIL.MgraRectAngleDouble.restype = None
      MgraRectAngleDouble = MIL.MgraRectAngleDouble
   except:
      MgraRectAngleDouble = None
if MIL is not None:
   try:
      MIL.MgraRectAngleInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong]
      MIL.MgraRectAngleInt64.restype = None
      MgraRectAngleInt64 = MIL.MgraRectAngleInt64
   except:
      MgraRectAngleInt64 = None
if MIL is not None:
   try:
      MIL.MgraRectDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
      MIL.MgraRectDouble.restype = None
      MgraRectDouble = MIL.MgraRectDouble
   except:
      MgraRectDouble = None
if MIL is not None:
   try:
      MIL.MgraRectFillDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
      MIL.MgraRectFillDouble.restype = None
      MgraRectFillDouble = MIL.MgraRectFillDouble
   except:
      MgraRectFillDouble = None
if MIL is not None:
   try:
      MIL.MgraRectFillInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MgraRectFillInt64.restype = None
      MgraRectFillInt64 = MIL.MgraRectFillInt64
   except:
      MgraRectFillInt64 = None
if MIL is not None:
   try:
      MIL.MgraRectInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MgraRectInt64.restype = None
      MgraRectInt64 = MIL.MgraRectInt64
   except:
      MgraRectInt64 = None
if MIL is not None:
   try:
      MIL.MgraTextWDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_wchar_p]
      MIL.MgraTextWDouble.restype = None
      MgraTextWDouble = MIL.MgraTextWDouble
   except:
      MgraTextWDouble = None
if MIL is not None:
   try:
      MIL.MgraTextWInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p]
      MIL.MgraTextWInt64.restype = None
      MgraTextWInt64 = MIL.MgraTextWInt64
   except:
      MgraTextWInt64 = None
if MIL is not None:
   try:
      MIL.MgraVectorsDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong]
      MIL.MgraVectorsDouble.restype = None
      MgraVectorsDouble = MIL.MgraVectorsDouble
   except:
      MgraVectorsDouble = None
if MIL is not None:
   try:
      MIL.MgraVectorsFloat.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong]
      MIL.MgraVectorsFloat.restype = None
      MgraVectorsFloat = MIL.MgraVectorsFloat
   except:
      MgraVectorsFloat = None
if MIL is not None:
   try:
      MIL.MgraVectorsGrid.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong]
      MIL.MgraVectorsGrid.restype = None
      MgraVectorsGrid = MIL.MgraVectorsGrid
   except:
      MgraVectorsGrid = None
if MIL is not None:
   try:
      MIL.MgraVectorsInt32.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.POINTER(ctypes.c_long), ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong]
      MIL.MgraVectorsInt32.restype = None
      MgraVectorsInt32 = MIL.MgraVectorsInt32
   except:
      MgraVectorsInt32 = None
if MIL is not None:
   try:
      MIL.MgraVectorsInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.POINTER(ctypes.c_longlong), ctypes.POINTER(ctypes.c_longlong), ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong]
      MIL.MgraVectorsInt64.restype = None
      MgraVectorsInt64 = MIL.MgraVectorsInt64
   except:
      MgraVectorsInt64 = None
if MILIM is not None:
   try:
      MILIM.MimAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILIM.MimAlloc.restype = ctypes.c_longlong
      MimAlloc = MILIM.MimAlloc
   except:
      MimAlloc = None
if MILIM is not None:
   try:
      MILIM.MimAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILIM.MimAllocResult.restype = ctypes.c_longlong
      MimAllocResult = MILIM.MimAllocResult
   except:
      MimAllocResult = None
if MILIM is not None:
   try:
      MILIM.MimArithDouble.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimArithDouble.restype = None
      MimArithDouble = MILIM.MimArithDouble
   except:
      MimArithDouble = None
if MILIM is not None:
   try:
      MILIM.MimArithMultipleDouble.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimArithMultipleDouble.restype = None
      MimArithMultipleDouble = MILIM.MimArithMultipleDouble
   except:
      MimArithMultipleDouble = None
if MILIM is not None:
   try:
      MILIM.MimAugment.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimAugment.restype = None
      MimAugment = MILIM.MimAugment
   except:
      MimAugment = None
if MILIM is not None:
   try:
      MILIM.MimBinarizeAdaptive.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimBinarizeAdaptive.restype = None
      MimBinarizeAdaptive = MILIM.MimBinarizeAdaptive
   except:
      MimBinarizeAdaptive = None
if MILIM is not None:
   try:
      MILIM.MimBinarizeDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double]
      MILIM.MimBinarizeDouble.restype = ctypes.c_longlong
      MimBinarizeDouble = MILIM.MimBinarizeDouble
   except:
      MimBinarizeDouble = None
if MILIM is not None:
   try:
      MILIM.MimClipDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
      MILIM.MimClipDouble.restype = None
      MimClipDouble = MILIM.MimClipDouble
   except:
      MimClipDouble = None
if MILIM is not None:
   try:
      MILIM.MimClose.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimClose.restype = None
      MimClose = MILIM.MimClose
   except:
      MimClose = None
if MILIM is not None:
   try:
      MILIM.MimConnectMap.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimConnectMap.restype = None
      MimConnectMap = MILIM.MimConnectMap
   except:
      MimConnectMap = None
if MILIM is not None:
   try:
      MILIM.MimControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILIM.MimControlDouble.restype = None
      MimControlDouble = MILIM.MimControlDouble
   except:
      MimControlDouble = None
if MILIM is not None:
   try:
      MILIM.MimControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimControlInt64.restype = None
      MimControlInt64 = MILIM.MimControlInt64
   except:
      MimControlInt64 = None
if MILIM is not None:
   try:
      MILIM.MimConvert.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimConvert.restype = None
      MimConvert = MILIM.MimConvert
   except:
      MimConvert = None
if MILIM is not None:
   try:
      MILIM.MimConvolve.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimConvolve.restype = None
      MimConvolve = MILIM.MimConvolve
   except:
      MimConvolve = None
if MILIM is not None:
   try:
      MILIM.MimCountDifference.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimCountDifference.restype = ctypes.c_longlong
      MimCountDifference = MILIM.MimCountDifference
   except:
      MimCountDifference = None
if MILIM is not None:
   try:
      MILIM.MimDeadPixelCorrection.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimDeadPixelCorrection.restype = None
      MimDeadPixelCorrection = MILIM.MimDeadPixelCorrection
   except:
      MimDeadPixelCorrection = None
if MILIM is not None:
   try:
      MILIM.MimDeinterlace.argtypes = [ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimDeinterlace.restype = None
      MimDeinterlace = MILIM.MimDeinterlace
   except:
      MimDeinterlace = None
if MILIM is not None:
   try:
      MILIM.MimDifferential.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimDifferential.restype = None
      MimDifferential = MILIM.MimDifferential
   except:
      MimDifferential = None
if MILIM is not None:
   try:
      MILIM.MimDilate.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimDilate.restype = None
      MimDilate = MILIM.MimDilate
   except:
      MimDilate = None
if MILIM is not None:
   try:
      MILIM.MimDistance.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimDistance.restype = None
      MimDistance = MILIM.MimDistance
   except:
      MimDistance = None
if MILIM is not None:
   try:
      MILIM.MimDrawDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MILIM.MimDrawDouble.restype = None
      MimDrawDouble = MILIM.MimDrawDouble
   except:
      MimDrawDouble = None
if MILIM is not None:
   try:
      MILIM.MimEdgeDetectMIL_INT.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimEdgeDetectMIL_INT.restype = None
      MimEdgeDetectMIL_INT = MILIM.MimEdgeDetectMIL_INT
   except:
      MimEdgeDetectMIL_INT = None
if MILIM is not None:
   try:
      MILIM.MimErode.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimErode.restype = None
      MimErode = MILIM.MimErode
   except:
      MimErode = None
if MILIM is not None:
   try:
      MILIM.MimFilterAdaptive.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MILIM.MimFilterAdaptive.restype = None
      MimFilterAdaptive = MILIM.MimFilterAdaptive
   except:
      MimFilterAdaptive = None
if MILIM is not None:
   try:
      MILIM.MimFindExtreme.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimFindExtreme.restype = None
      MimFindExtreme = MILIM.MimFindExtreme
   except:
      MimFindExtreme = None
if MILIM is not None:
   try:
      MILIM.MimFindOrientation.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimFindOrientation.restype = None
      MimFindOrientation = MILIM.MimFindOrientation
   except:
      MimFindOrientation = None
if MILIM is not None:
   try:
      MILIM.MimFlatField.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimFlatField.restype = None
      MimFlatField = MILIM.MimFlatField
   except:
      MimFlatField = None
if MILIM is not None:
   try:
      MILIM.MimFlip.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimFlip.restype = None
      MimFlip = MILIM.MimFlip
   except:
      MimFlip = None
if MILIM is not None:
   try:
      MILIM.MimFree.argtypes = [ctypes.c_longlong]
      MILIM.MimFree.restype = None
      MimFree = MILIM.MimFree
   except:
      MimFree = None
if MILIM is not None:
   try:
      MILIM.MimGet.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MILIM.MimGet.restype = ctypes.c_longlong
      MimGet = MILIM.MimGet
   except:
      MimGet = None
if MILIM is not None:
   try:
      MILIM.MimGetResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILIM.MimGetResult.restype = None
      MimGetResult = MILIM.MimGetResult
   except:
      MimGetResult = None
if MILIM is not None:
   try:
      MILIM.MimGetResult1d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILIM.MimGetResult1d.restype = None
      MimGetResult1d = MILIM.MimGetResult1d
   except:
      MimGetResult1d = None
if MILIM is not None:
   try:
      MILIM.MimGetResult2d.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILIM.MimGetResult2d.restype = None
      MimGetResult2d = MILIM.MimGetResult2d
   except:
      MimGetResult2d = None
if MILIM is not None:
   try:
      MILIM.MimGetResultSingleInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILIM.MimGetResultSingleInt64.restype = None
      MimGetResultSingleInt64 = MILIM.MimGetResultSingleInt64
   except:
      MimGetResultSingleInt64 = None
if MILIM is not None:
   try:
      MILIM.MimHistogram.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimHistogram.restype = None
      MimHistogram = MILIM.MimHistogram
   except:
      MimHistogram = None
if MILIM is not None:
   try:
      MILIM.MimHistogramEqualizeAdaptive.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimHistogramEqualizeAdaptive.restype = None
      MimHistogramEqualizeAdaptive = MILIM.MimHistogramEqualizeAdaptive
   except:
      MimHistogramEqualizeAdaptive = None
if MILIM is not None:
   try:
      MILIM.MimHistogramEqualizeDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double]
      MILIM.MimHistogramEqualizeDouble.restype = None
      MimHistogramEqualizeDouble = MILIM.MimHistogramEqualizeDouble
   except:
      MimHistogramEqualizeDouble = None
if MILIM is not None:
   try:
      MILIM.MimInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILIM.MimInquire.restype = ctypes.c_longlong
      MimInquire = MILIM.MimInquire
   except:
      MimInquire = None
if MILIM is not None:
   try:
      MILIM.MimLabel.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimLabel.restype = None
      MimLabel = MILIM.MimLabel
   except:
      MimLabel = None
if MILIM is not None:
   try:
      MILIM.MimLocateEventDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double]
      MILIM.MimLocateEventDouble.restype = ctypes.c_longlong
      MimLocateEventDouble = MILIM.MimLocateEventDouble
   except:
      MimLocateEventDouble = None
if MILIM is not None:
   try:
      MILIM.MimLocatePeak1dDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.c_double]
      MILIM.MimLocatePeak1dDouble.restype = None
      MimLocatePeak1dDouble = MILIM.MimLocatePeak1dDouble
   except:
      MimLocatePeak1dDouble = None
if MILIM is not None:
   try:
      MILIM.MimLutMap.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimLutMap.restype = None
      MimLutMap = MILIM.MimLutMap
   except:
      MimLutMap = None
if MILIM is not None:
   try:
      MILIM.MimMatch.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimMatch.restype = None
      MimMatch = MILIM.MimMatch
   except:
      MimMatch = None
if MILIM is not None:
   try:
      MILIM.MimMorphic.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimMorphic.restype = None
      MimMorphic = MILIM.MimMorphic
   except:
      MimMorphic = None
if MILIM is not None:
   try:
      MILIM.MimOpen.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimOpen.restype = None
      MimOpen = MILIM.MimOpen
   except:
      MimOpen = None
if MILIM is not None:
   try:
      MILIM.MimPolarTransform.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p]
      MILIM.MimPolarTransform.restype = None
      MimPolarTransform = MILIM.MimPolarTransform
   except:
      MimPolarTransform = None
if MILIM is not None:
   try:
      MILIM.MimProjection.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.c_double]
      MILIM.MimProjection.restype = None
      MimProjection = MILIM.MimProjection
   except:
      MimProjection = None
if MILIM is not None:
   try:
      MILIM.MimPut.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MILIM.MimPut.restype = None
      MimPut = MILIM.MimPut
   except:
      MimPut = None
if MILIM is not None:
   try:
      MILIM.MimRank.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimRank.restype = None
      MimRank = MILIM.MimRank
   except:
      MimRank = None
if MILIM is not None:
   try:
      MILIM.MimRearrange.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimRearrange.restype = None
      MimRearrange = MILIM.MimRearrange
   except:
      MimRearrange = None
if MILIM is not None:
   try:
      MILIM.MimRemap.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimRemap.restype = None
      MimRemap = MILIM.MimRemap
   except:
      MimRemap = None
if MILIM is not None:
   try:
      MILIM.MimResize.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MILIM.MimResize.restype = None
      MimResize = MILIM.MimResize
   except:
      MimResize = None
if MILIM is not None:
   try:
      MILIM.MimRestoreW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILIM.MimRestoreW.restype = ctypes.c_longlong
      MimRestoreW = MILIM.MimRestoreW
   except:
      MimRestoreW = None
if MILIM is not None:
   try:
      MILIM.MimRotate.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MILIM.MimRotate.restype = None
      MimRotate = MILIM.MimRotate
   except:
      MimRotate = None
if MILIM is not None:
   try:
      MILIM.MimSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimSaveW.restype = None
      MimSaveW = MILIM.MimSaveW
   except:
      MimSaveW = None
if MILIM is not None:
   try:
      MILIM.MimShift.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimShift.restype = None
      MimShift = MILIM.MimShift
   except:
      MimShift = None
if MILIM is not None:
   try:
      MILIM.MimStatCalculate.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimStatCalculate.restype = None
      MimStatCalculate = MILIM.MimStatCalculate
   except:
      MimStatCalculate = None
if MILIM is not None:
   try:
      MILIM.MimStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MILIM.MimStreamW.restype = None
      MimStreamW = MILIM.MimStreamW
   except:
      MimStreamW = None
if MILIM is not None:
   try:
      MILIM.MimThick.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimThick.restype = None
      MimThick = MILIM.MimThick
   except:
      MimThick = None
if MILIM is not None:
   try:
      MILIM.MimThin.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimThin.restype = None
      MimThin = MILIM.MimThin
   except:
      MimThin = None
if MILIM is not None:
   try:
      MILIM.MimTransform.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimTransform.restype = None
      MimTransform = MILIM.MimTransform
   except:
      MimTransform = None
if MILIM is not None:
   try:
      MILIM.MimTranslate.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MILIM.MimTranslate.restype = None
      MimTranslate = MILIM.MimTranslate
   except:
      MimTranslate = None
if MILIM is not None:
   try:
      MILIM.MimWarp.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimWarp.restype = None
      MimWarp = MILIM.MimWarp
   except:
      MimWarp = None
if MILIM is not None:
   try:
      MILIM.MimWarpList.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_longlong]
      MILIM.MimWarpList.restype = None
      MimWarpList = MILIM.MimWarpList
   except:
      MimWarpList = None
if MILIM is not None:
   try:
      MILIM.MimWatershed.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimWatershed.restype = None
      MimWatershed = MILIM.MimWatershed
   except:
      MimWatershed = None
if MILIM is not None:
   try:
      MILIM.MimWaveletDenoise.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimWaveletDenoise.restype = None
      MimWaveletDenoise = MILIM.MimWaveletDenoise
   except:
      MimWaveletDenoise = None
if MILIM is not None:
   try:
      MILIM.MimWaveletSetFilter.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimWaveletSetFilter.restype = None
      MimWaveletSetFilter = MILIM.MimWaveletSetFilter
   except:
      MimWaveletSetFilter = None
if MILIM is not None:
   try:
      MILIM.MimWaveletTransform.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimWaveletTransform.restype = None
      MimWaveletTransform = MILIM.MimWaveletTransform
   except:
      MimWaveletTransform = None
if MILIM is not None:
   try:
      MILIM.MimZoneOfInfluence.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILIM.MimZoneOfInfluence.restype = None
      MimZoneOfInfluence = MILIM.MimZoneOfInfluence
   except:
      MimZoneOfInfluence = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasAllocContext.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILMEAS.MmeasAllocContext.restype = ctypes.c_longlong
      MmeasAllocContext = MILMEAS.MmeasAllocContext
   except:
      MmeasAllocContext = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasAllocMarker.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILMEAS.MmeasAllocMarker.restype = ctypes.c_longlong
      MmeasAllocMarker = MILMEAS.MmeasAllocMarker
   except:
      MmeasAllocMarker = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILMEAS.MmeasAllocResult.restype = ctypes.c_longlong
      MmeasAllocResult = MILMEAS.MmeasAllocResult
   except:
      MmeasAllocResult = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasCalculate.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILMEAS.MmeasCalculate.restype = None
      MmeasCalculate = MILMEAS.MmeasCalculate
   except:
      MmeasCalculate = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILMEAS.MmeasControlDouble.restype = None
      MmeasControlDouble = MILMEAS.MmeasControlDouble
   except:
      MmeasControlDouble = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILMEAS.MmeasControlInt64.restype = None
      MmeasControlInt64 = MILMEAS.MmeasControlInt64
   except:
      MmeasControlInt64 = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasDraw.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILMEAS.MmeasDraw.restype = None
      MmeasDraw = MILMEAS.MmeasDraw
   except:
      MmeasDraw = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasFindMarker.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILMEAS.MmeasFindMarker.restype = None
      MmeasFindMarker = MILMEAS.MmeasFindMarker
   except:
      MmeasFindMarker = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasFree.argtypes = [ctypes.c_longlong]
      MILMEAS.MmeasFree.restype = None
      MmeasFree = MILMEAS.MmeasFree
   except:
      MmeasFree = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasGetResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p]
      MILMEAS.MmeasGetResult.restype = None
      MmeasGetResult = MILMEAS.MmeasGetResult
   except:
      MmeasGetResult = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasGetResultSingle.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MILMEAS.MmeasGetResultSingle.restype = None
      MmeasGetResultSingle = MILMEAS.MmeasGetResultSingle
   except:
      MmeasGetResultSingle = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasGetScore.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MILMEAS.MmeasGetScore.restype = None
      MmeasGetScore = MILMEAS.MmeasGetScore
   except:
      MmeasGetScore = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p]
      MILMEAS.MmeasInquire.restype = ctypes.c_longlong
      MmeasInquire = MILMEAS.MmeasInquire
   except:
      MmeasInquire = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasRestoreMarkerW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILMEAS.MmeasRestoreMarkerW.restype = ctypes.c_longlong
      MmeasRestoreMarkerW = MILMEAS.MmeasRestoreMarkerW
   except:
      MmeasRestoreMarkerW = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasSaveMarkerW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILMEAS.MmeasSaveMarkerW.restype = None
      MmeasSaveMarkerW = MILMEAS.MmeasSaveMarkerW
   except:
      MmeasSaveMarkerW = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasSetMarkerDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double]
      MILMEAS.MmeasSetMarkerDouble.restype = None
      MmeasSetMarkerDouble = MILMEAS.MmeasSetMarkerDouble
   except:
      MmeasSetMarkerDouble = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasSetMarkerInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILMEAS.MmeasSetMarkerInt64.restype = None
      MmeasSetMarkerInt64 = MILMEAS.MmeasSetMarkerInt64
   except:
      MmeasSetMarkerInt64 = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasSetScore.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong, ctypes.c_longlong]
      MILMEAS.MmeasSetScore.restype = None
      MmeasSetScore = MILMEAS.MmeasSetScore
   except:
      MmeasSetScore = None
if MILMEAS is not None:
   try:
      MILMEAS.MmeasStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MILMEAS.MmeasStreamW.restype = None
      MmeasStreamW = MILMEAS.MmeasStreamW
   except:
      MmeasStreamW = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetAddFeature.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILMETROL.MmetAddFeature.restype = None
      MmetAddFeature = MILMETROL.MmetAddFeature
   except:
      MmetAddFeature = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetAddTolerance.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILMETROL.MmetAddTolerance.restype = None
      MmetAddTolerance = MILMETROL.MmetAddTolerance
   except:
      MmetAddTolerance = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILMETROL.MmetAlloc.restype = ctypes.c_longlong
      MmetAlloc = MILMETROL.MmetAlloc
   except:
      MmetAlloc = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILMETROL.MmetAllocResult.restype = ctypes.c_longlong
      MmetAllocResult = MILMETROL.MmetAllocResult
   except:
      MmetAllocResult = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetCalculate.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILMETROL.MmetCalculate.restype = None
      MmetCalculate = MILMETROL.MmetCalculate
   except:
      MmetCalculate = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILMETROL.MmetControlDouble.restype = None
      MmetControlDouble = MILMETROL.MmetControlDouble
   except:
      MmetControlDouble = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILMETROL.MmetControlInt64.restype = None
      MmetControlInt64 = MILMETROL.MmetControlInt64
   except:
      MmetControlInt64 = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetDraw.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILMETROL.MmetDraw.restype = None
      MmetDraw = MILMETROL.MmetDraw
   except:
      MmetDraw = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetFree.argtypes = [ctypes.c_longlong]
      MILMETROL.MmetFree.restype = None
      MmetFree = MILMETROL.MmetFree
   except:
      MmetFree = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetGetResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILMETROL.MmetGetResult.restype = None
      MmetGetResult = MILMETROL.MmetGetResult
   except:
      MmetGetResult = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILMETROL.MmetInquire.restype = ctypes.c_longlong
      MmetInquire = MILMETROL.MmetInquire
   except:
      MmetInquire = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetNameW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MILMETROL.MmetNameW.restype = None
      MmetNameW = MILMETROL.MmetNameW
   except:
      MmetNameW = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetPutDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MILMETROL.MmetPutDouble.restype = None
      MmetPutDouble = MILMETROL.MmetPutDouble
   except:
      MmetPutDouble = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetPutFloat.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.c_void_p, ctypes.c_void_p, ctypes.c_longlong]
      MILMETROL.MmetPutFloat.restype = None
      MmetPutFloat = MILMETROL.MmetPutFloat
   except:
      MmetPutFloat = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetRestoreW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILMETROL.MmetRestoreW.restype = ctypes.c_longlong
      MmetRestoreW = MILMETROL.MmetRestoreW
   except:
      MmetRestoreW = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILMETROL.MmetSaveW.restype = None
      MmetSaveW = MILMETROL.MmetSaveW
   except:
      MmetSaveW = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetSetPositionDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MILMETROL.MmetSetPositionDouble.restype = None
      MmetSetPositionDouble = MILMETROL.MmetSetPositionDouble
   except:
      MmetSetPositionDouble = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetSetPositionInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MILMETROL.MmetSetPositionInt64.restype = None
      MmetSetPositionInt64 = MILMETROL.MmetSetPositionInt64
   except:
      MmetSetPositionInt64 = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetSetRegionDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
      MILMETROL.MmetSetRegionDouble.restype = None
      MmetSetRegionDouble = MILMETROL.MmetSetRegionDouble
   except:
      MmetSetRegionDouble = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetSetRegionInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
      MILMETROL.MmetSetRegionInt64.restype = None
      MmetSetRegionInt64 = MILMETROL.MmetSetRegionInt64
   except:
      MmetSetRegionInt64 = None
if MILMETROL is not None:
   try:
      MILMETROL.MmetStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MILMETROL.MmetStreamW.restype = None
      MmetStreamW = MILMETROL.MmetStreamW
   except:
      MmetStreamW = None
if MILMOD is not None:
   try:
      MILMOD.MmodAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILMOD.MmodAlloc.restype = ctypes.c_longlong
      MmodAlloc = MILMOD.MmodAlloc
   except:
      MmodAlloc = None
if MILMOD is not None:
   try:
      MILMOD.MmodAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILMOD.MmodAllocResult.restype = ctypes.c_longlong
      MmodAllocResult = MILMOD.MmodAllocResult
   except:
      MmodAllocResult = None
if MILMOD is not None:
   try:
      MILMOD.MmodControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILMOD.MmodControlDouble.restype = None
      MmodControlDouble = MILMOD.MmodControlDouble
   except:
      MmodControlDouble = None
if MILMOD is not None:
   try:
      MILMOD.MmodControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILMOD.MmodControlInt64.restype = None
      MmodControlInt64 = MILMOD.MmodControlInt64
   except:
      MmodControlInt64 = None
if MILMOD is not None:
   try:
      MILMOD.MmodDefineDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
      MILMOD.MmodDefineDouble.restype = None
      MmodDefineDouble = MILMOD.MmodDefineDouble
   except:
      MmodDefineDouble = None
if MILMOD is not None:
   try:
      MILMOD.MmodDefineFromFileW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong]
      MILMOD.MmodDefineFromFileW.restype = None
      MmodDefineFromFileW = MILMOD.MmodDefineFromFileW
   except:
      MmodDefineFromFileW = None
if MILMOD is not None:
   try:
      MILMOD.MmodDefineInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
      MILMOD.MmodDefineInt64.restype = None
      MmodDefineInt64 = MILMOD.MmodDefineInt64
   except:
      MmodDefineInt64 = None
if MILMOD is not None:
   try:
      MILMOD.MmodDraw.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILMOD.MmodDraw.restype = None
      MmodDraw = MILMOD.MmodDraw
   except:
      MmodDraw = None
if MILMOD is not None:
   try:
      MILMOD.MmodFind.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILMOD.MmodFind.restype = None
      MmodFind = MILMOD.MmodFind
   except:
      MmodFind = None
if MILMOD is not None:
   try:
      MILMOD.MmodFree.argtypes = [ctypes.c_longlong]
      MILMOD.MmodFree.restype = None
      MmodFree = MILMOD.MmodFree
   except:
      MmodFree = None
if MILMOD is not None:
   try:
      MILMOD.MmodGetResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILMOD.MmodGetResult.restype = None
      MmodGetResult = MILMOD.MmodGetResult
   except:
      MmodGetResult = None
if MILMOD is not None:
   try:
      MILMOD.MmodInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILMOD.MmodInquire.restype = ctypes.c_longlong
      MmodInquire = MILMOD.MmodInquire
   except:
      MmodInquire = None
if MILMOD is not None:
   try:
      MILMOD.MmodMask.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILMOD.MmodMask.restype = None
      MmodMask = MILMOD.MmodMask
   except:
      MmodMask = None
if MILMOD is not None:
   try:
      MILMOD.MmodPreprocess.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
      MILMOD.MmodPreprocess.restype = None
      MmodPreprocess = MILMOD.MmodPreprocess
   except:
      MmodPreprocess = None
if MILMOD is not None:
   try:
      MILMOD.MmodRestoreW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILMOD.MmodRestoreW.restype = ctypes.c_longlong
      MmodRestoreW = MILMOD.MmodRestoreW
   except:
      MmodRestoreW = None
if MILMOD is not None:
   try:
      MILMOD.MmodSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILMOD.MmodSaveW.restype = None
      MmodSaveW = MILMOD.MmodSaveW
   except:
      MmodSaveW = None
if MILMOD is not None:
   try:
      MILMOD.MmodStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MILMOD.MmodStreamW.restype = None
      MmodStreamW = MILMOD.MmodStreamW
   except:
      MmodStreamW = None
if MIL is not None:
   try:
      MIL.MobjAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MobjAlloc.restype = ctypes.c_longlong
      MobjAlloc = MIL.MobjAlloc
   except:
      MobjAlloc = None
if MIL is not None:
   try:
      MIL.MobjControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MobjControlDouble.restype = None
      MobjControlDouble = MIL.MobjControlDouble
   except:
      MobjControlDouble = None
if MIL is not None:
   try:
      MIL.MobjControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MobjControlInt64.restype = None
      MobjControlInt64 = MIL.MobjControlInt64
   except:
      MobjControlInt64 = None
if MIL is not None:
   try:
      MIL.MobjFree.argtypes = [ctypes.c_longlong]
      MIL.MobjFree.restype = None
      MobjFree = MIL.MobjFree
   except:
      MobjFree = None
if MIL is not None:
   try:
      MIL.MobjGetHookInfo.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL.MobjGetHookInfo.restype = ctypes.c_longlong
      MobjGetHookInfo = MIL.MobjGetHookInfo
   except:
      MobjGetHookInfo = None
if MIL is not None:
   try:
      MIL.MobjHookFunction.argtypes = [ctypes.c_longlong, ctypes.c_longlong, MIL_OBJ_HOOK_FUNCTION_PTR, ctypes.c_void_p]
      MIL.MobjHookFunction.restype = None
      MobjHookFunction = MIL.MobjHookFunction
   except:
      MobjHookFunction = None
if MIL is not None:
   try:
      MIL.MobjInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MobjInquire.restype = ctypes.c_longlong
      MobjInquire = MIL.MobjInquire
   except:
      MobjInquire = None
if MIL is not None:
   try:
      MIL.MobjMessageRead.argtypes = [ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong]
      MIL.MobjMessageRead.restype = ctypes.c_longlong
      MobjMessageRead = MIL.MobjMessageRead
   except:
      MobjMessageRead = None
if MIL is not None:
   try:
      MIL.MobjMessageWrite.argtypes = [ctypes.c_longlong, ctypes.POINTER(ctypes.c_ubyte), ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MobjMessageWrite.restype = None
      MobjMessageWrite = MIL.MobjMessageWrite
   except:
      MobjMessageWrite = None
if MILOCR is not None:
   try:
      MILOCR.MocrAllocFont.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILOCR.MocrAllocFont.restype = ctypes.c_longlong
      MocrAllocFont = MILOCR.MocrAllocFont
   except:
      MocrAllocFont = None
if MILOCR is not None:
   try:
      MILOCR.MocrAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILOCR.MocrAllocResult.restype = ctypes.c_longlong
      MocrAllocResult = MILOCR.MocrAllocResult
   except:
      MocrAllocResult = None
if MILOCR is not None:
   try:
      MILOCR.MocrCalibrateFontW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MILOCR.MocrCalibrateFontW.restype = None
      MocrCalibrateFontW = MILOCR.MocrCalibrateFontW
   except:
      MocrCalibrateFontW = None
if MILOCR is not None:
   try:
      MILOCR.MocrControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILOCR.MocrControlDouble.restype = None
      MocrControlDouble = MILOCR.MocrControlDouble
   except:
      MocrControlDouble = None
if MILOCR is not None:
   try:
      MILOCR.MocrControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILOCR.MocrControlInt64.restype = None
      MocrControlInt64 = MILOCR.MocrControlInt64
   except:
      MocrControlInt64 = None
if MILOCR is not None:
   try:
      MILOCR.MocrCopyFontW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILOCR.MocrCopyFontW.restype = None
      MocrCopyFontW = MILOCR.MocrCopyFontW
   except:
      MocrCopyFontW = None
if MILOCR is not None:
   try:
      MILOCR.MocrDrawW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong]
      MILOCR.MocrDrawW.restype = None
      MocrDrawW = MILOCR.MocrDrawW
   except:
      MocrDrawW = None
if MILOCR is not None:
   try:
      MILOCR.MocrFree.argtypes = [ctypes.c_longlong]
      MILOCR.MocrFree.restype = None
      MocrFree = MILOCR.MocrFree
   except:
      MocrFree = None
if MILOCR is not None:
   try:
      MILOCR.MocrGetResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILOCR.MocrGetResult.restype = None
      MocrGetResult = MILOCR.MocrGetResult
   except:
      MocrGetResult = None
if MILOCR is not None:
   try:
      MILOCR.MocrHookFunction.argtypes = [ctypes.c_longlong, ctypes.c_longlong, MIL_OCR_HOOK_FUNCTION_PTR, ctypes.c_void_p]
      MILOCR.MocrHookFunction.restype = MIL_OCR_HOOK_FUNCTION_PTR
      MocrHookFunction = MILOCR.MocrHookFunction
   except:
      MocrHookFunction = None
if MILOCR is not None:
   try:
      MILOCR.MocrImportFontW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong]
      MILOCR.MocrImportFontW.restype = None
      MocrImportFontW = MILOCR.MocrImportFontW
   except:
      MocrImportFontW = None
if MILOCR is not None:
   try:
      MILOCR.MocrInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILOCR.MocrInquire.restype = ctypes.c_longlong
      MocrInquire = MILOCR.MocrInquire
   except:
      MocrInquire = None
if MILOCR is not None:
   try:
      MILOCR.MocrModifyFont.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILOCR.MocrModifyFont.restype = None
      MocrModifyFont = MILOCR.MocrModifyFont
   except:
      MocrModifyFont = None
if MILOCR is not None:
   try:
      MILOCR.MocrPreprocess.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
      MILOCR.MocrPreprocess.restype = None
      MocrPreprocess = MILOCR.MocrPreprocess
   except:
      MocrPreprocess = None
if MILOCR is not None:
   try:
      MILOCR.MocrReadString.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILOCR.MocrReadString.restype = None
      MocrReadString = MILOCR.MocrReadString
   except:
      MocrReadString = None
if MILOCR is not None:
   try:
      MILOCR.MocrRestoreFontW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILOCR.MocrRestoreFontW.restype = ctypes.c_longlong
      MocrRestoreFontW = MILOCR.MocrRestoreFontW
   except:
      MocrRestoreFontW = None
if MILOCR is not None:
   try:
      MILOCR.MocrSaveFontW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILOCR.MocrSaveFontW.restype = None
      MocrSaveFontW = MILOCR.MocrSaveFontW
   except:
      MocrSaveFontW = None
if MILOCR is not None:
   try:
      MILOCR.MocrSetConstraintW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILOCR.MocrSetConstraintW.restype = None
      MocrSetConstraintW = MILOCR.MocrSetConstraintW
   except:
      MocrSetConstraintW = None
if MILOCR is not None:
   try:
      MILOCR.MocrStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MILOCR.MocrStreamW.restype = None
      MocrStreamW = MILOCR.MocrStreamW
   except:
      MocrStreamW = None
if MILOCR is not None:
   try:
      MILOCR.MocrVerifyStringW.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong]
      MILOCR.MocrVerifyStringW.restype = None
      MocrVerifyStringW = MILOCR.MocrVerifyStringW
   except:
      MocrVerifyStringW = None
if MILPAT is not None:
   try:
      MILPAT.MpatAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILPAT.MpatAlloc.restype = ctypes.c_longlong
      MpatAlloc = MILPAT.MpatAlloc
   except:
      MpatAlloc = None
if MILPAT is not None:
   try:
      MILPAT.MpatAllocResultNew.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILPAT.MpatAllocResultNew.restype = ctypes.c_longlong
      MpatAllocResultNew = MILPAT.MpatAllocResultNew
   except:
      MpatAllocResultNew = None
if MILPAT is not None:
   try:
      MILPAT.MpatControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILPAT.MpatControlDouble.restype = None
      MpatControlDouble = MILPAT.MpatControlDouble
   except:
      MpatControlDouble = None
if MILPAT is not None:
   try:
      MILPAT.MpatControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILPAT.MpatControlInt64.restype = None
      MpatControlInt64 = MILPAT.MpatControlInt64
   except:
      MpatControlInt64 = None
if MILPAT is not None:
   try:
      MILPAT.MpatDefine.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MILPAT.MpatDefine.restype = None
      MpatDefine = MILPAT.MpatDefine
   except:
      MpatDefine = None
if MILPAT is not None:
   try:
      MILPAT.MpatDraw.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILPAT.MpatDraw.restype = None
      MpatDraw = MILPAT.MpatDraw
   except:
      MpatDraw = None
if MILPAT is not None:
   try:
      MILPAT.MpatFind.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILPAT.MpatFind.restype = None
      MpatFind = MILPAT.MpatFind
   except:
      MpatFind = None
if MILPAT is not None:
   try:
      MILPAT.MpatFree.argtypes = [ctypes.c_longlong]
      MILPAT.MpatFree.restype = None
      MpatFree = MILPAT.MpatFree
   except:
      MpatFree = None
if MILPAT is not None:
   try:
      MILPAT.MpatGetResultNew.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILPAT.MpatGetResultNew.restype = None
      MpatGetResultNew = MILPAT.MpatGetResultNew
   except:
      MpatGetResultNew = None
if MILPAT is not None:
   try:
      MILPAT.MpatInquireNew.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILPAT.MpatInquireNew.restype = ctypes.c_longlong
      MpatInquireNew = MILPAT.MpatInquireNew
   except:
      MpatInquireNew = None
if MILPAT is not None:
   try:
      MILPAT.MpatMask.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILPAT.MpatMask.restype = None
      MpatMask = MILPAT.MpatMask
   except:
      MpatMask = None
if MILPAT is not None:
   try:
      MILPAT.MpatPreprocess.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILPAT.MpatPreprocess.restype = None
      MpatPreprocess = MILPAT.MpatPreprocess
   except:
      MpatPreprocess = None
if MILPAT is not None:
   try:
      MILPAT.MpatRestoreNewW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILPAT.MpatRestoreNewW.restype = ctypes.c_longlong
      MpatRestoreNewW = MILPAT.MpatRestoreNewW
   except:
      MpatRestoreNewW = None
if MILPAT is not None:
   try:
      MILPAT.MpatSaveNewW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILPAT.MpatSaveNewW.restype = None
      MpatSaveNewW = MILPAT.MpatSaveNewW
   except:
      MpatSaveNewW = None
if MILPAT is not None:
   try:
      MILPAT.MpatStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MILPAT.MpatStreamW.restype = None
      MpatStreamW = MILPAT.MpatStreamW
   except:
      MpatStreamW = None
if MILREG is not None:
   try:
      MILREG.MregAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILREG.MregAlloc.restype = ctypes.c_longlong
      MregAlloc = MILREG.MregAlloc
   except:
      MregAlloc = None
if MILREG is not None:
   try:
      MILREG.MregAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILREG.MregAllocResult.restype = ctypes.c_longlong
      MregAllocResult = MILREG.MregAllocResult
   except:
      MregAllocResult = None
if MILREG is not None:
   try:
      MILREG.MregCalculate.argtypes = [ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILREG.MregCalculate.restype = None
      MregCalculate = MILREG.MregCalculate
   except:
      MregCalculate = None
if MILREG is not None:
   try:
      MILREG.MregControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILREG.MregControlDouble.restype = None
      MregControlDouble = MILREG.MregControlDouble
   except:
      MregControlDouble = None
if MILREG is not None:
   try:
      MILREG.MregControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILREG.MregControlInt64.restype = None
      MregControlInt64 = MILREG.MregControlInt64
   except:
      MregControlInt64 = None
if MILREG is not None:
   try:
      MILREG.MregDraw.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILREG.MregDraw.restype = None
      MregDraw = MILREG.MregDraw
   except:
      MregDraw = None
if MILREG is not None:
   try:
      MILREG.MregFree.argtypes = [ctypes.c_longlong]
      MILREG.MregFree.restype = None
      MregFree = MILREG.MregFree
   except:
      MregFree = None
if MILREG is not None:
   try:
      MILREG.MregGetResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILREG.MregGetResult.restype = None
      MregGetResult = MILREG.MregGetResult
   except:
      MregGetResult = None
if MILREG is not None:
   try:
      MILREG.MregInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILREG.MregInquire.restype = ctypes.c_longlong
      MregInquire = MILREG.MregInquire
   except:
      MregInquire = None
if MILREG is not None:
   try:
      MILREG.MregRestoreW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILREG.MregRestoreW.restype = ctypes.c_longlong
      MregRestoreW = MILREG.MregRestoreW
   except:
      MregRestoreW = None
if MILREG is not None:
   try:
      MILREG.MregSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILREG.MregSaveW.restype = None
      MregSaveW = MILREG.MregSaveW
   except:
      MregSaveW = None
if MILREG is not None:
   try:
      MILREG.MregSetLocationDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MILREG.MregSetLocationDouble.restype = None
      MregSetLocationDouble = MILREG.MregSetLocationDouble
   except:
      MregSetLocationDouble = None
if MILREG is not None:
   try:
      MILREG.MregSetLocationInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_longlong]
      MILREG.MregSetLocationInt64.restype = None
      MregSetLocationInt64 = MILREG.MregSetLocationInt64
   except:
      MregSetLocationInt64 = None
if MILREG is not None:
   try:
      MILREG.MregStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MILREG.MregStreamW.restype = None
      MregStreamW = MILREG.MregStreamW
   except:
      MregStreamW = None
if MILREG is not None:
   try:
      MILREG.MregTransformCoordinate.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_longlong]
      MILREG.MregTransformCoordinate.restype = None
      MregTransformCoordinate = MILREG.MregTransformCoordinate
   except:
      MregTransformCoordinate = None
if MILREG is not None:
   try:
      MILREG.MregTransformCoordinateList.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_longlong]
      MILREG.MregTransformCoordinateList.restype = None
      MregTransformCoordinateList = MILREG.MregTransformCoordinateList
   except:
      MregTransformCoordinateList = None
if MILREG is not None:
   try:
      MILREG.MregTransformImage.argtypes = [ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILREG.MregTransformImage.restype = None
      MregTransformImage = MILREG.MregTransformImage
   except:
      MregTransformImage = None
if MIL is not None:
   try:
      MIL.MseqAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_ulong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MseqAlloc.restype = ctypes.c_longlong
      MseqAlloc = MIL.MseqAlloc
   except:
      MseqAlloc = None
if MIL is not None:
   try:
      MIL.MseqControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MseqControlDouble.restype = None
      MseqControlDouble = MIL.MseqControlDouble
   except:
      MseqControlDouble = None
if MIL is not None:
   try:
      MIL.MseqControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MseqControlInt64.restype = None
      MseqControlInt64 = MIL.MseqControlInt64
   except:
      MseqControlInt64 = None
if MIL is not None:
   try:
      MIL.MseqDefine.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_double]
      MIL.MseqDefine.restype = None
      MseqDefine = MIL.MseqDefine
   except:
      MseqDefine = None
if MIL is not None:
   try:
      MIL.MseqFeed.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MseqFeed.restype = None
      MseqFeed = MIL.MseqFeed
   except:
      MseqFeed = None
if MIL is not None:
   try:
      MIL.MseqFree.argtypes = [ctypes.c_longlong]
      MIL.MseqFree.restype = None
      MseqFree = MIL.MseqFree
   except:
      MseqFree = None
if MIL is not None:
   try:
      MIL.MseqGetHookInfo.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MIL.MseqGetHookInfo.restype = ctypes.c_longlong
      MseqGetHookInfo = MIL.MseqGetHookInfo
   except:
      MseqGetHookInfo = None
if MIL is not None:
   try:
      MIL.MseqHookFunction.argtypes = [ctypes.c_longlong, ctypes.c_longlong, MIL_SEQ_HOOK_FUNCTION_PTR, ctypes.c_void_p]
      MIL.MseqHookFunction.restype = None
      MseqHookFunction = MIL.MseqHookFunction
   except:
      MseqHookFunction = None
if MIL is not None:
   try:
      MIL.MseqInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MseqInquire.restype = ctypes.c_longlong
      MseqInquire = MIL.MseqInquire
   except:
      MseqInquire = None
if MIL is not None:
   try:
      MIL.MseqProcess.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MseqProcess.restype = None
      MseqProcess = MIL.MseqProcess
   except:
      MseqProcess = None
if MILSTR is not None:
   try:
      MILSTR.MstrAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILSTR.MstrAlloc.restype = ctypes.c_longlong
      MstrAlloc = MILSTR.MstrAlloc
   except:
      MstrAlloc = None
if MILSTR is not None:
   try:
      MILSTR.MstrAllocResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILSTR.MstrAllocResult.restype = ctypes.c_longlong
      MstrAllocResult = MILSTR.MstrAllocResult
   except:
      MstrAllocResult = None
if MILSTR is not None:
   try:
      MILSTR.MstrControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MILSTR.MstrControlDouble.restype = None
      MstrControlDouble = MILSTR.MstrControlDouble
   except:
      MstrControlDouble = None
if MILSTR is not None:
   try:
      MILSTR.MstrControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILSTR.MstrControlInt64.restype = None
      MstrControlInt64 = MILSTR.MstrControlInt64
   except:
      MstrControlInt64 = None
if MILSTR is not None:
   try:
      MILSTR.MstrDraw.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_longlong]
      MILSTR.MstrDraw.restype = None
      MstrDraw = MILSTR.MstrDraw
   except:
      MstrDraw = None
if MILSTR is not None:
   try:
      MILSTR.MstrEditFont.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p, ctypes.c_void_p]
      MILSTR.MstrEditFont.restype = None
      MstrEditFont = MILSTR.MstrEditFont
   except:
      MstrEditFont = None
if MILSTR is not None:
   try:
      MILSTR.MstrExpert.argtypes = [ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILSTR.MstrExpert.restype = None
      MstrExpert = MILSTR.MstrExpert
   except:
      MstrExpert = None
if MILSTR is not None:
   try:
      MILSTR.MstrFree.argtypes = [ctypes.c_longlong]
      MILSTR.MstrFree.restype = None
      MstrFree = MILSTR.MstrFree
   except:
      MstrFree = None
if MILSTR is not None:
   try:
      MILSTR.MstrGetResult.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILSTR.MstrGetResult.restype = None
      MstrGetResult = MILSTR.MstrGetResult
   except:
      MstrGetResult = None
if MILSTR is not None:
   try:
      MILSTR.MstrInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILSTR.MstrInquire.restype = ctypes.c_longlong
      MstrInquire = MILSTR.MstrInquire
   except:
      MstrInquire = None
if MILSTR is not None:
   try:
      MILSTR.MstrPreprocess.argtypes = [ctypes.c_longlong, ctypes.c_longlong]
      MILSTR.MstrPreprocess.restype = None
      MstrPreprocess = MILSTR.MstrPreprocess
   except:
      MstrPreprocess = None
if MILSTR is not None:
   try:
      MILSTR.MstrRead.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MILSTR.MstrRead.restype = None
      MstrRead = MILSTR.MstrRead
   except:
      MstrRead = None
if MILSTR is not None:
   try:
      MILSTR.MstrRestoreW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong)]
      MILSTR.MstrRestoreW.restype = ctypes.c_longlong
      MstrRestoreW = MILSTR.MstrRestoreW
   except:
      MstrRestoreW = None
if MILSTR is not None:
   try:
      MILSTR.MstrSaveW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong]
      MILSTR.MstrSaveW.restype = None
      MstrSaveW = MILSTR.MstrSaveW
   except:
      MstrSaveW = None
if MILSTR is not None:
   try:
      MILSTR.MstrSetConstraint.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MILSTR.MstrSetConstraint.restype = None
      MstrSetConstraint = MILSTR.MstrSetConstraint
   except:
      MstrSetConstraint = None
if MILSTR is not None:
   try:
      MILSTR.MstrStreamW.argtypes = [ctypes.c_void_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_longlong, ctypes.POINTER(ctypes.c_longlong), ctypes.c_void_p]
      MILSTR.MstrStreamW.restype = None
      MstrStreamW = MILSTR.MstrStreamW
   except:
      MstrStreamW = None
if MIL is not None:
   try:
      MIL.MsysAllocW.argtypes = [ctypes.c_longlong, ctypes.c_wchar_p, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MsysAllocW.restype = ctypes.c_longlong
      MsysAllocW = MIL.MsysAllocW
   except:
      MsysAllocW = None
if MIL is not None:
   try:
      MIL.MsysControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MsysControlDouble.restype = None
      MsysControlDouble = MIL.MsysControlDouble
   except:
      MsysControlDouble = None
if MIL is not None:
   try:
      MIL.MsysControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MsysControlInt64.restype = None
      MsysControlInt64 = MIL.MsysControlInt64
   except:
      MsysControlInt64 = None
if MIL is not None:
   try:
      MIL.MsysFree.argtypes = [ctypes.c_longlong]
      MIL.MsysFree.restype = None
      MsysFree = MIL.MsysFree
   except:
      MsysFree = None
if MIL is not None:
   try:
      MIL.MsysGetHookInfo.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MsysGetHookInfo.restype = ctypes.c_longlong
      MsysGetHookInfo = MIL.MsysGetHookInfo
   except:
      MsysGetHookInfo = None
if MIL is not None:
   try:
      MIL.MsysHookFunction.argtypes = [ctypes.c_longlong, ctypes.c_longlong, MIL_SYS_HOOK_FUNCTION_PTR, ctypes.c_void_p]
      MIL.MsysHookFunction.restype = None
      MsysHookFunction = MIL.MsysHookFunction
   except:
      MsysHookFunction = None
if MIL is not None:
   try:
      MIL.MsysInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MsysInquire.restype = ctypes.c_longlong
      MsysInquire = MIL.MsysInquire
   except:
      MsysInquire = None
if MIL is not None:
   try:
      MIL.MsysIoAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MsysIoAlloc.restype = ctypes.c_longlong
      MsysIoAlloc = MIL.MsysIoAlloc
   except:
      MsysIoAlloc = None
if MIL is not None:
   try:
      MIL.MsysIoCommandRegister.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double, ctypes.c_double, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MsysIoCommandRegister.restype = ctypes.c_longlong
      MsysIoCommandRegister = MIL.MsysIoCommandRegister
   except:
      MsysIoCommandRegister = None
if MIL is not None:
   try:
      MIL.MsysIoControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MsysIoControlDouble.restype = None
      MsysIoControlDouble = MIL.MsysIoControlDouble
   except:
      MsysIoControlDouble = None
if MIL is not None:
   try:
      MIL.MsysIoControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MsysIoControlInt64.restype = None
      MsysIoControlInt64 = MIL.MsysIoControlInt64
   except:
      MsysIoControlInt64 = None
if MIL is not None:
   try:
      MIL.MsysIoFree.argtypes = [ctypes.c_longlong]
      MIL.MsysIoFree.restype = None
      MsysIoFree = MIL.MsysIoFree
   except:
      MsysIoFree = None
if MIL is not None:
   try:
      MIL.MsysIoInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MsysIoInquire.restype = ctypes.c_longlong
      MsysIoInquire = MIL.MsysIoInquire
   except:
      MsysIoInquire = None
if MIL is not None:
   try:
      MIL.MthrAlloc.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, MIL_THREAD_FUNCTION_PTR, ctypes.c_void_p, ctypes.c_void_p]
      MIL.MthrAlloc.restype = ctypes.c_longlong
      MthrAlloc = MIL.MthrAlloc
   except:
      MthrAlloc = None
if MIL is not None:
   try:
      MIL.MthrControlDouble.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_double]
      MIL.MthrControlDouble.restype = None
      MthrControlDouble = MIL.MthrControlDouble
   except:
      MthrControlDouble = None
if MIL is not None:
   try:
      MIL.MthrControlInt64.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong]
      MIL.MthrControlInt64.restype = None
      MthrControlInt64 = MIL.MthrControlInt64
   except:
      MthrControlInt64 = None
if MIL is not None:
   try:
      MIL.MthrControlMp.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MthrControlMp.restype = None
      MthrControlMp = MIL.MthrControlMp
   except:
      MthrControlMp = None
if MIL is not None:
   try:
      MIL.MthrFree.argtypes = [ctypes.c_longlong]
      MIL.MthrFree.restype = None
      MthrFree = MIL.MthrFree
   except:
      MthrFree = None
if MIL is not None:
   try:
      MIL.MthrInquire.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MthrInquire.restype = ctypes.c_longlong
      MthrInquire = MIL.MthrInquire
   except:
      MthrInquire = None
if MIL is not None:
   try:
      MIL.MthrInquireMp.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MthrInquireMp.restype = ctypes.c_longlong
      MthrInquireMp = MIL.MthrInquireMp
   except:
      MthrInquireMp = None
if MIL is not None:
   try:
      MIL.MthrWait.argtypes = [ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MthrWait.restype = ctypes.c_longlong
      MthrWait = MIL.MthrWait
   except:
      MthrWait = None
if MIL is not None:
   try:
      MIL.MthrWaitMultiple.argtypes = [ctypes.POINTER(ctypes.c_longlong), ctypes.c_longlong, ctypes.c_longlong, ctypes.c_void_p]
      MIL.MthrWaitMultiple.restype = ctypes.c_longlong
      MthrWaitMultiple = MIL.MthrWaitMultiple
   except:
      MthrWaitMultiple = None

M3ddispAlloc = M3ddispAllocW if MIL3D is not None else None
M3ddispControl = M3ddispControlDouble if MIL3D is not None else None
M3ddispSetView = M3ddispSetViewDouble if MIL3D is not None else None
M3dgeoMatrixGet = M3dgeoMatrixGetDouble if MIL3D is not None else None
M3dgeoMatrixPut = M3dgeoMatrixPutDouble if MIL3D is not None else None
M3dgeoMatrixSetTransform = M3dgeoMatrixSetTransformDouble if MIL3D is not None else None
M3dgeoRestore = M3dgeoRestoreW if MIL3D is not None else None
M3dgeoSave = M3dgeoSaveW if MIL3D is not None else None
M3dgeoStream = M3dgeoStreamW if MIL3D is not None else None
M3dgraAxis = M3dgraAxisW if MIL3D is not None else None
M3dgraControl = M3dgraControlDouble if MIL3D is not None else None
M3dgraDots = M3dgraDotsDouble if MIL3D is not None else None
M3dgraPolygon = M3dgraPolygonDouble if MIL3D is not None else None
M3dgraText = M3dgraTextW if MIL3D is not None else None
M3dimControl = M3dimControlDouble if MIL3DIM is not None else None
M3dimMatrixTransformList = M3dimMatrixTransformListDouble if MIL3DIM is not None else None
M3dimRestore = M3dimRestoreW if MIL3DIM is not None else None
M3dimSave = M3dimSaveW if MIL3DIM is not None else None
M3dimStream = M3dimStreamW if MIL3DIM is not None else None
M3dmapControl = M3dmapControlDouble if MIL3DMAP is not None else None
M3dmapRestore = M3dmapRestoreW if MIL3DMAP is not None else None
M3dmapSave = M3dmapSaveW if MIL3DMAP is not None else None
M3dmapStream = M3dmapStreamW if MIL3DMAP is not None else None
M3dmetControl = M3dmetControlDouble if MIL3DMET is not None else None
M3dmetRestore = M3dmetRestoreW if MIL3DMET is not None else None
M3dmetSave = M3dmetSaveW if MIL3DMET is not None else None
M3dmetStream = M3dmetStreamW if MIL3DMET is not None else None
M3dregControl = M3dregControlDouble if MIL3DREG is not None else None
M3dregRestore = M3dregRestoreW if MIL3DREG is not None else None
M3dregSave = M3dregSaveW if MIL3DREG is not None else None
M3dregStream = M3dregStreamW if MIL3DREG is not None else None
MappAlloc = MappAllocW if MIL is not None else None
MappFileOperation = MappFileOperationW if MIL is not None else None
MappOpenConnection = MappOpenConnectionW if MIL is not None else None
MappTrace = MappTraceW if MIL is not None else None
MbeadControl = MbeadControlDouble if MILBEAD is not None else None
MbeadRestore = MbeadRestoreW if MILBEAD is not None else None
MbeadSave = MbeadSaveW if MILBEAD is not None else None
MbeadStream = MbeadStreamW if MILBEAD is not None else None
MblobAllocResult = MblobAllocResultNew if MILBLOB is not None else None
MblobControl = MblobControlDouble if MILBLOB is not None else None
MblobGetResult = MblobGetResultNew if MILBLOB is not None else None
MblobRestore = MblobRestoreW if MILBLOB is not None else None
MblobSave = MblobSaveW if MILBLOB is not None else None
MblobStream = MblobStreamW if MILBLOB is not None else None
MbufClear = MbufClearDouble if MIL is not None else None
MbufClearCond = MbufClearCondDouble if MIL is not None else None
MbufControl = MbufControlDouble if MIL is not None else None
MbufControlArea = MbufControlAreaDouble if MIL is not None else None
MbufControlContainer = MbufControlContainerDouble if MIL is not None else None
MbufCopyCond = MbufCopyCondDouble if MIL is not None else None
MbufCreate2d = MbufCreate2dFunc if MIL is not None else None
MbufDiskInquire = MbufDiskInquireW if MIL is not None else None
MbufExport = MbufExportW if MIL is not None else None
MbufExportSequence = MbufExportSequenceW if MIL is not None else None
MbufGetArc = MbufGetArc2 if MIL is not None else None
MbufGetList = MbufGetListDouble if MIL is not None else None
MbufImport = MbufImportW if MIL is not None else None
MbufImportSequence = MbufImportSequenceW if MIL is not None else None
MbufLoad = MbufLoadW if MIL is not None else None
MbufPutList = MbufPutListDouble if MIL is not None else None
MbufRestore = MbufRestoreW if MIL is not None else None
MbufSave = MbufSaveW if MIL is not None else None
MbufSetRegion = MbufSetRegionDouble if MIL is not None else None
MbufStream = MbufStreamW if MIL is not None else None
McalControl = McalControlDouble if MILCAL is not None else None
McalFixture = McalFixtureDouble if MILCAL is not None else None
McalRestore = McalRestoreW if MILCAL is not None else None
McalSave = McalSaveW if MILCAL is not None else None
McalStream = McalStreamW if MILCAL is not None else None
MclassControl = MclassControlDouble if MILCLASS is not None else None
MclassControlEntry = MclassControlEntryDouble if MILCLASS is not None else None
MclassExport = MclassExportW if MILCLASS is not None else None
MclassImport = MclassImportW if MILCLASS is not None else None
MclassRestore = MclassRestoreW if MILCLASS is not None else None
MclassSave = MclassSaveW if MILCLASS is not None else None
MclassStream = MclassStreamW if MILCLASS is not None else None
McodeControl = McodeControlDouble if MILCODE is not None else None
McodeDraw = McodeDrawNew if MILCODE is not None else None
McodeGetResult = McodeGetResultNew if MILCODE is not None else None
McodeRestore = McodeRestoreW if MILCODE is not None else None
McodeSave = McodeSaveW if MILCODE is not None else None
McodeStream = McodeStreamW if MILCODE is not None else None
McodeWrite = McodeWriteNewW if MILCODE is not None else None
McolControl = McolControlDouble if MILCOLOR is not None else None
McolRestore = McolRestoreW if MILCOLOR is not None else None
McolSave = McolSaveW if MILCOLOR is not None else None
McolStream = McolStreamW if MILCOLOR is not None else None
McomAlloc = McomAllocW if MILCOM is not None else None
McomControl = McomControlDouble if MILCOM is not None else None
McomRead = McomReadW if MILCOM is not None else None
McomWrite = McomWriteW if MILCOM is not None else None
MdigAlloc = MdigAllocW if MIL is not None else None
MdigControl = MdigControlDouble if MIL is not None else None
MdigControlFeature = MdigControlFeatureW if MIL is not None else None
MdigInquireFeature = MdigInquireFeatureW if MIL is not None else None
MdispAlloc = MdispAllocW if MIL is not None else None
MdispControl = MdispControlDouble if MIL is not None else None
MdmrControl = MdmrControlDouble if MILDMR is not None else None
MdmrControlFont = MdmrControlFontDoubleW if MILDMR is not None else None
MdmrControlStringModel = MdmrControlStringModelDouble if MILDMR is not None else None
MdmrExportFont = MdmrExportFontW if MILDMR is not None else None
MdmrImportFont = MdmrImportFontW if MILDMR is not None else None
MdmrInquireFont = MdmrInquireFontW if MILDMR is not None else None
MdmrName = MdmrNameW if MILDMR is not None else None
MdmrRestore = MdmrRestoreW if MILDMR is not None else None
MdmrSave = MdmrSaveW if MILDMR is not None else None
MdmrStream = MdmrStreamW if MILDMR is not None else None
MedgeControl = MedgeControlDouble if MILEDGE is not None else None
MedgeRestore = MedgeRestoreW if MILEDGE is not None else None
MedgeSave = MedgeSaveW if MILEDGE is not None else None
MedgeStream = MedgeStreamW if MILEDGE is not None else None
MfpgaLoad = MfpgaLoadW if MILFPGA is not None else None
MfuncAlloc = MfuncAllocW if MIL is not None else None
MfuncAllocScript = MfuncAllocScriptW if MIL is not None else None
MfuncControl = MfuncControlDouble if MIL is not None else None
MfuncErrorReport = MfuncErrorReportW if MIL is not None else None
MfuncParam = MfuncParamW if MIL is not None else None
MfuncParamConstMilText = MfuncParamConstMilTextW if MIL is not None else None
MfuncParamFilename = MfuncParamFilenameW if MIL is not None else None
MfuncParamMilText = MfuncParamMilTextW if MIL is not None else None
MfuncParamValueConstMilText = MfuncParamValueConstMilTextW if MIL is not None else None
MfuncParamValueFilename = MfuncParamValueFilenameW if MIL is not None else None
MfuncParamValueMilText = MfuncParamValueMilTextW if MIL is not None else None
MgraArc = MgraArcDouble if MIL is not None else None
MgraArcAngle = MgraArcAngleDouble if MIL is not None else None
MgraArcFill = MgraArcFillDouble if MIL is not None else None
MgraBackColor = MgraBackColorDouble if MIL is not None else None
MgraColor = MgraColorDouble if MIL is not None else None
MgraControl = MgraControlDouble if MIL is not None else None
MgraControlList = MgraControlListDouble if MIL is not None else None
MgraDot = MgraDotDouble if MIL is not None else None
MgraDots = MgraDotsDouble if MIL is not None else None
MgraFill = MgraFillDouble if MIL is not None else None
MgraFont = MgraFontW if MIL is not None else None
MgraLine = MgraLineDouble if MIL is not None else None
MgraLines = MgraLinesDouble if MIL is not None else None
MgraRect = MgraRectDouble if MIL is not None else None
MgraRectAngle = MgraRectAngleDouble if MIL is not None else None
MgraRectFill = MgraRectFillDouble if MIL is not None else None
MgraText = MgraTextWDouble if MIL is not None else None
MgraVectors = MgraVectorsDouble if MIL is not None else None
MimArith = MimArithDouble if MILIM is not None else None
MimArithMultiple = MimArithMultipleDouble if MILIM is not None else None
MimBinarize = MimBinarizeDouble if MILIM is not None else None
MimClip = MimClipDouble if MILIM is not None else None
MimControl = MimControlDouble if MILIM is not None else None
MimDraw = MimDrawDouble if MILIM is not None else None
MimEdgeDetect = MimEdgeDetectMIL_INT if MILIM is not None else None
MimGetResultSingle = MimGetResultSingleInt64 if MILIM is not None else None
MimHistogramEqualize = MimHistogramEqualizeDouble if MILIM is not None else None
MimLocateEvent = MimLocateEventDouble if MILIM is not None else None
MimLocatePeak1d = MimLocatePeak1dDouble if MILIM is not None else None
MimRestore = MimRestoreW if MILIM is not None else None
MimSave = MimSaveW if MILIM is not None else None
MimStream = MimStreamW if MILIM is not None else None
MmeasControl = MmeasControlDouble if MILMEAS is not None else None
MmeasRestoreMarker = MmeasRestoreMarkerW if MILMEAS is not None else None
MmeasSaveMarker = MmeasSaveMarkerW if MILMEAS is not None else None
MmeasSetMarker = MmeasSetMarkerDouble if MILMEAS is not None else None
MmeasStream = MmeasStreamW if MILMEAS is not None else None
MmetControl = MmetControlDouble if MILMETROL is not None else None
MmetName = MmetNameW if MILMETROL is not None else None
MmetPut = MmetPutDouble if MILMETROL is not None else None
MmetRestore = MmetRestoreW if MILMETROL is not None else None
MmetSave = MmetSaveW if MILMETROL is not None else None
MmetSetPosition = MmetSetPositionDouble if MILMETROL is not None else None
MmetSetRegion = MmetSetRegionDouble if MILMETROL is not None else None
MmetStream = MmetStreamW if MILMETROL is not None else None
MmodControl = MmodControlDouble if MILMOD is not None else None
MmodDefine = MmodDefineDouble if MILMOD is not None else None
MmodDefineFromFile = MmodDefineFromFileW if MILMOD is not None else None
MmodRestore = MmodRestoreW if MILMOD is not None else None
MmodSave = MmodSaveW if MILMOD is not None else None
MmodStream = MmodStreamW if MILMOD is not None else None
MobjControl = MobjControlDouble if MIL is not None else None
MocrCalibrateFont = MocrCalibrateFontW if MILOCR is not None else None
MocrControl = MocrControlDouble if MILOCR is not None else None
MocrCopyFont = MocrCopyFontW if MILOCR is not None else None
MocrDraw = MocrDrawW if MILOCR is not None else None
MocrImportFont = MocrImportFontW if MILOCR is not None else None
MocrRestoreFont = MocrRestoreFontW if MILOCR is not None else None
MocrSaveFont = MocrSaveFontW if MILOCR is not None else None
MocrSetConstraint = MocrSetConstraintW if MILOCR is not None else None
MocrStream = MocrStreamW if MILOCR is not None else None
MocrVerifyString = MocrVerifyStringW if MILOCR is not None else None
MpatAllocResult = MpatAllocResultNew if MILPAT is not None else None
MpatControl = MpatControlDouble if MILPAT is not None else None
MpatGetResult = MpatGetResultNew if MILPAT is not None else None
MpatInquire = MpatInquireNew if MILPAT is not None else None
MpatRestore = MpatRestoreNewW if MILPAT is not None else None
MpatSave = MpatSaveNewW if MILPAT is not None else None
MpatStream = MpatStreamW if MILPAT is not None else None
MregControl = MregControlDouble if MILREG is not None else None
MregRestore = MregRestoreW if MILREG is not None else None
MregSave = MregSaveW if MILREG is not None else None
MregSetLocation = MregSetLocationDouble if MILREG is not None else None
MregStream = MregStreamW if MILREG is not None else None
MseqControl = MseqControlDouble if MIL is not None else None
MstrControl = MstrControlDouble if MILSTR is not None else None
MstrRestore = MstrRestoreW if MILSTR is not None else None
MstrSave = MstrSaveW if MILSTR is not None else None
MstrStream = MstrStreamW if MILSTR is not None else None
MsysAlloc = MsysAllocW if MIL is not None else None
MsysControl = MsysControlDouble if MIL is not None else None
MsysIoControl = MsysIoControlDouble if MIL is not None else None
MthrControl = MthrControlDouble if MIL is not None else None

def MIL_TEXT(s):
   return s.encode('utf-16','replace').decode('utf-16','replace')
def create_c_string_buffer(*params):
   return ctypes.create_unicode_buffer(*params)
def M_PTR_TO_DOUBLE(s):
   try:
      str_type = basestring
   except NameError:
      str_type = str
   if isinstance(s, str_type):
      st = create_c_string_buffer(s)
      return ctypes.cast(st, ctypes.c_void_p).value
   else:
      return ctypes.cast(s, ctypes.c_void_p).value
def M_PTR_TO_MIL_INT(s):
   try:
      str_type = basestring
   except NameError:
      str_type = str
   if isinstance(s, str_type):
      st = create_c_string_buffer(s)
      return ctypes.cast(st, ctypes.c_void_p).value
   else:
      return ctypes.cast(s, ctypes.c_void_p).value
def MIL_FONT_NAME(s):
   return M_PTR_TO_DOUBLE(s)
def M_FEATURE_OP(n):
   return M_FEATURE_OP_MASK & n
def M_FEATURE_ENUM(n):
   return M_FEATURE_ENUM_MASK & n
def M_SUBFEATURE_INDEX(n):
   return M_SUBFEATURE_INDEX_MASK & n
def M_FEATURE_IS_IMPLEMENTED(accessMode):
   return accessMode != M_FEATURE_NOT_IMPLEMENTED
def M_FEATURE_IS_AVAILABLE(accessMode):
   return not ((accessMode == M_FEATURE_NOT_AVAILABLE) or (accessMode == M_FEATURE_NOT_IMPLEMENTED))
def M_FEATURE_IS_READABLE(accessMode):
   return (accessMode == M_FEATURE_READ_ONLY) or (accessMode == M_FEATURE_READ_WRITE)
def M_FEATURE_IS_WRITABLE(accessMode):
   return (accessMode == M_FEATURE_WRITE_ONLY) or (accessMode == M_FEATURE_READ_WRITE)
def M_FEATURE_IS_CACHABLE(n):
   return n != M_FEATURE_CACHING_MODE_NONE
def M_FEATURE_ENUM_ENTRY_INDEX(n):
   return n & M_FEATURE_ENUM_ENTRY_INDEX_MASK
def M_HORIZONTAL_LEVEL(a):
   return (M_HORIZONTAL_LEVEL_TAG + (a))
def M_VERTICAL_LEVEL(a):
   return (M_VERTICAL_LEVEL_TAG + (a))
def M_DIAGONAL_LEVEL(a):
   return (M_DIAGONAL_LEVEL_TAG + (a))
def M_POINT_CLOUD_LABEL(a):
   return ((a) | M_POINT_CLOUD_LABEL_FLAG)
def M_POINT_CLOUD_INDEX(a):
   return ((a) | M_POINT_CLOUD_INDEX_FLAG)
def M_INTERPRETER_CUSTOM(a):
   return dllPath
def M_SCAN_RESULT_INDEX(i):
   return 0 if (i == M_ALL or i == M_DEFAULT) else ((i + 1) << M_GRADE_RESULT_OFFSET)
def M_ROW_RESULT_INDEX(i):
   return M_SCAN_RESULT_INDEX(i)
def M_FEATURE_USER_ARRAY_SIZE(N):
   return (M_FEATURE_USER_ARRAY_SIZE_BITS | (((N) & M_FEATURE_USER_ARRAY_SIZE_MASK) <<  (ctypes.c_ulong(M_FEATURE_USER_ARRAY_SIZE_SHIFT).value)))
def M_VALUE_INDEX(Instance):
   return (Instance << M_DATA_LATCH_INSTANCE_BITSHIFT)
def M_LIST_SIZE(n):
   if ( n < 0):
      return 0
   elif (n > 1000):
      return 1000
   else:
      return n
def M_DIST_NN_SIGNED(n):
   return ((((n) >> 1) & M_DIST_NN_SIZE_MASK) | M_DIST_NN_SIGNED_TAG)
def M_DIST_NN(n):
   return ((((n) >> 1) & M_DIST_NN_SIZE_MASK) | M_DIST_NN_TAG)
def M_FONT_LABEL(i):
   return M_FONT_LABEL_FLAG | i
def M_STRING_LABEL(i):
   return M_STRING_LABEL_FLAG | i
def M_POSITION_CONSTRAINED_ORDER(i):
   return M_POSITION_CONSTRAINED_ORDER_FLAG | i
def M_POSITION_IN_STRING(i):
   return M_POSITION_IN_STRING_FLAG | i
def M_BLOB_INDEX(blobIndex):
   return ((blobIndex) | M_BLOB_INDEX_FLAG)
def M_BLOB_LABEL(label):
   return label
def M_INDEX_IN_STRING(IndexValue):
   return (M_INDEX_IN_STRING_FLAG | (IndexValue))
def M_INDEX_IN_FORMATTED_STRING(IndexValue):
   return (M_INDEX_IN_FORMATTED_STRING_FLAG | (IndexValue))
def M_IO_COMMAND_BIT_MASK(IndexValue):
   return (M_IO_COMMAND_BIT_MASK_FLAG | (IndexValue))
def M_GENTL_PRODUCER(IndexValue):
   return (M_GENTL_PRODUCER_BIT | ((IndexValue  << M_GENTL_PRODUCER_SHIFT) & M_GENTL_PRODUCER_MASK))
def M_GENTL_INTERFACE_NUMBER(IndexValue):
   return (M_GENTL_INTERFACE | (((IndexValue) << M_GENTL_XML_INDEX_SHIFT_LOWER) & M_GENTL_XML_INDEX_MASK_LOWER) | (((IndexValue) << M_GENTL_XML_INDEX_SHIFT_UPPER) & M_GENTL_XML_INDEX_MASK_UPPER))
def M_GENTL_STREAM_NUMBER(IndexValue):
   return (M_GENTL_STREAM | (((IndexValue) << M_GENTL_XML_INDEX_SHIFT_LOWER) & M_GENTL_XML_INDEX_MASK_LOWER) | (((IndexValue) << M_GENTL_XML_INDEX_SHIFT_UPPER) & M_GENTL_XML_INDEX_MASK_UPPER))
def M_SELECT_PEAK(a, b):
   return (a << 32 | b)
def M_REGION_INDEX(IndexValue):
   return (M_REGION_INDEX_FLAG    | (IndexValue))
def M_CLASS_INDEX(IndexValue):
   return (M_CLASS_DEF_INDEX_FLAG | (IndexValue))
def M_COMPONENT_BY_ID(IndexValue):
   return (M_COMPONENT_BY_ID_FLAG    | (IndexValue))
def M_COMPONENT_BY_INDEX(IndexValue):
   return (M_COMPONENT_BY_INDEX_FLAG    | (IndexValue))
def M_COMPONENT_BY_GROUP_ID(IndexValue):
   return (M_COMPONENT_BY_GROUP_ID_FLAG    | (IndexValue))
def M_COMPONENT_BY_GROUP(IndexValue):
   return 0
def M_COMPONENT_BY_REGION_ID(IndexValue):
   return (M_COMPONENT_BY_REGION_ID_FLAG    | (IndexValue))
def M_COMPONENT_BY_SOURCE_ID(IndexValue):
   return (M_COMPONENT_BY_SOURCE_ID_FLAG    | (IndexValue))
def M_AUTHOR_INDEX(IndexValue):
   return (M_AUTHOR_INDEX_FLAG    | (IndexValue))
def M_PFNC_TO_TYPE(IndexValue):
   return (M_PFNC_COMPACT    | ((IndexValue) & 0xFFFF))
def M_CORNER_X(IndexValue):
   return (1221 + (IndexValue) + (2595 if (IndexValue) > 3 else 0))
def M_CORNER_Y(IndexValue):
   return (1225 + (IndexValue) + (2595 if (IndexValue) > 3 else 0))
def M_CORNER_Z(IndexValue):
   return (3828 + (IndexValue))
def M_CAMERA_LABEL(CameraLabel):
   return ( ((CameraLabel) << M_CAMERA_OFFSET) | M_CAMERA_LABEL_FLAG)
def M_LASER_LABEL(LaserLabel):
   return ( ((LaserLabel) << M_LASER_OFFSET) | M_LASER_LABEL_FLAG )
def M_DX_VERSION(X):
   return  (M_DIRECTX_VERSION_FLAG + (1 << M_DIRECTX_VERSION_OFFSET)) if (X == M_DEFAULT) else (M_DIRECTX_VERSION_FLAG + (X << M_DIRECTX_VERSION_OFFSET))
def M_CLUSTER_NODE(x):
   return ((x << M_SET_CLUSTER_NODE_OFFSET) & M_SET_CLUSTER_NODE_MASK)
def M_TEMPLATE_INDEX(i):
   return (M_TEMPLATE_INDEX_TAG | (i))
def M_TEMPLATE_LABEL(i):
   return (M_TEMPLATE_LABEL_TAG | (i))
def M_BAYER_BIT_SHIFT(i):
   return (i << 20)
def M_RGB888(Red, Green, Blue):
   newRed = ctypes.c_long(ctypes.c_ubyte(Red).value).value
   newBlue = ctypes.c_long(ctypes.c_ubyte(Blue).value).value
   newGreen = ctypes.c_long(ctypes.c_ubyte(Green).value).value
   return (M_RGB_COLOR | newBlue << 16 | newGreen << 8 | newRed )
def M_IS_RGB888(color):
   return ((color & 0xFF000000) == M_RGB_COLOR)
def M_RGB888_R(color):
   return (color & 0x000000FF)
def M_RGB888_G(color):
   return ((color & 0x0000FF00) >> 8)
def M_RGB888_B(color):
   return ((color & 0x00FF0000) >> 16)
def M_BGR888(b, g, r):
   newRed = ctypes.c_long(ctypes.c_ubyte(r).value).value
   newBlue = ctypes.c_long(ctypes.c_ubyte(b).value).value
   newGreen = ctypes.c_long(ctypes.c_ubyte(g).value).value
   return (M_RGB_COLOR | newRed << 16 | newGreen << 8 | newBlue  )
def M_BGR888_B(color):
   return (color & 0x000000FF)
def M_BGR888_G(color):
   return ((color & 0x0000FF00) >> 8)
def M_BGR888_R(color):
   return ((color & 0x00FF0000) >> 16)
def M_SAMPLE_LABEL(sampleIndex):
   return M_SAMPLE_LABEL_TAG | sampleIndex
def M_SAMPLE_INDEX(sampleIndex):
   return M_SAMPLE_INDEX_TAG | sampleIndex
def M_SAMPLE_LABEL_ITEM(lbl, subidx):
   return ((lbl  | (subidx << 12)) | M_COLOR_ITEM_TAG | M_SAMPLE_LABEL_TAG)
def M_SAMPLE_INDEX_ITEM(idx, subidx):
   return ((idx  | (subidx << 12)) | M_COLOR_ITEM_TAG | M_SAMPLE_INDEX_TAG)
def M_CAMERA_SAMPLE_LABEL(sampleIndex):
   return M_SAMPLE_LABEL(sampleIndex)
def M_REFERENCE_SAMPLE_ITEM(subidx):
   return ((M_REFERENCE_SAMPLE_LABEL | (subidx << 12)) | M_COLOR_ITEM_TAG | M_SAMPLE_LABEL_TAG)
def M_COLOR888(r,g,b):
   return M_RGB888(r,g,b)
def M_GC_CAMERA_ID(x):
   return x
def M_GC_MANIFEST_ENTRY(N):
   return (((N & M_GC_MANIFEST_ENTRY_MASK) << M_GC_MANIFEST_ENTRY_SHIFT) | M_GC_MANIFEST_ENTRY_BIT)
def M_COUNT(n):
   return  ctypes.c_uint(n << M_DIG_PRCSS_COUNT_SHIFT).value
def M_FRAMES_PER_TRIGGER(n):
   return M_COUNT(n)
def M_GRAPHIC_INDEX(i):
   return M_GRAPHIC_INDEX_TAG + i
def M_GRAPHIC_LABEL(i):
   return M_GRAPHIC_LABEL_TAG + i
def M_DERICHE_FILTER(FilterOperation, FilterSmoothness):
   if ((((FilterOperation) & M_ID_OFFSET_OF_DEFAULT_KERNEL) != M_ID_OFFSET_OF_DEFAULT_KERNEL) and (FilterOperation != M_DEFAULT)):
      return M_DERICHE_PREDEFINED_KERNEL_INVALID_TYPE
   elif ((((FilterOperation) & (~(M_ID_OFFSET_OF_DEFAULT_KERNEL | 0xFF))) != 0) and (FilterOperation != M_DEFAULT)):
      return M_DERICHE_PREDEFINED_KERNEL_INVALID_TYPE
   elif (((((FilterSmoothness) < 0) or ((FilterSmoothness) > 100))) and (FilterSmoothness != M_DEFAULT)):
      return M_DERICHE_PREDEFINED_KERNEL_INVALID_FACTOR
   else:
      filter = M_DERICHE_PREDEFINED_KERNEL
      filter = filter | ( FilterOperation if FilterOperation != M_DEFAULT else 0x80)
      filter = filter | ( (FilterSmoothness << 8) if FilterSmoothness != M_DEFAULT else 0xFF00)
      return filter
def M_SHEN_FILTER(FilterOperation, FilterSmoothness):
   if ((((FilterOperation) & M_ID_OFFSET_OF_DEFAULT_KERNEL) != M_ID_OFFSET_OF_DEFAULT_KERNEL) and (FilterOperation != M_DEFAULT)):
      return M_SHEN_PREDEFINED_KERNEL_INVALID_TYPE
   elif ((((FilterOperation) & (~(M_ID_OFFSET_OF_DEFAULT_KERNEL | 0xFF))) != 0) and (FilterOperation != M_DEFAULT)):
      return M_SHEN_PREDEFINED_KERNEL_INVALID_TYPE
   elif (((((FilterSmoothness) < 0) or ((FilterSmoothness) > 100))) and (FilterSmoothness != M_DEFAULT)):
      return M_SHEN_PREDEFINED_KERNEL_INVALID_FACTOR
   else:
      filter = M_SHEN_PREDEFINED_KERNEL
      filter = filter | ( FilterOperation if FilterOperation != M_DEFAULT else 0x80)
      filter = filter | ( (FilterSmoothness << 8) if FilterSmoothness != M_DEFAULT else 0xFF00)
      return filter
def M_RESULT_PER_SUBREGION(subregion, occurence):
   return (M_SUB_REGION_TAG | subregion << M_MEAS_DRAW_INDEX_BIT_SHIFT | occurence)
def M_FEATURE_INDEX(index):
   return M_FEATURE_INDEX_TAG | index
def M_FEATURE_LABEL(label):
   return M_FEATURE_LABEL_TAG | label
def M_TOLERANCE_INDEX(index):
   return M_TOLERANCE_INDEX_TAG | index
def M_TOLERANCE_LABEL(label):
   return M_TOLERANCE_LABEL_TAG | label
def M_SEQ_INPUT(x):
   return (M_SEQ_CONTAINER_SOURCE | x)
def M_SEQ_OUTPUT(x):
   return (M_SEQ_CONTAINER_OUTPUT | (x << 18))
def M_SEQ_DEST(x):
   return (M_SEQ_CONTAINER_DESTINATION | x)
def M_FONT_INDEX(index):
   return M_FONT_MASK | (index)
def M_STRING_INDEX(index):
   return M_STRING_MASK | (index)
def M_UART_NB(value):
   return (value & M_MAX_UART_NB) << M_UART_NB_MASK_SHIFT
def M_THREAD_TIMEOUT(timeout):
   return M_EVENT_TIMEOUT(timeout)
def M_EVENT_TIMEOUT(timeout):
   ut = ctypes.c_ulong(timeout).value
   return ut if ut < M_MAX_TIMEOUT else 0
def M_BASE_FEATURE_LABEL(label):
   return M_CONSTRUCTION_FEATURE_LABEL_TAG | label
def M_BASE_SUBFEATURE_INDEX(index):
   return M_CONSTRUCTION_FEATURE_INDEX_TAG | index
M_DEFAULT_UUID = MIL_UUID((ctypes.c_ubyte * 16)(0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x00, 0x00, 0x00))
M_DEFAULT_KEY = M_DEFAULT_UUID
M_NULL_UUID = MIL_UUID((ctypes.c_ubyte * 16)(0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))
M_NULL_KEY = M_NULL_UUID
M_UNKNOWN_UUID = M_DEFAULT_UUID
M_UNKNOWN_KEY = M_UNKNOWN_UUID

M_NULL = 0
M_INVALID_POINT = 1.79769313486232E+308
M_INVALID_POINT_FLOAT = 3.40282346638529E+38
M_0_DEGREE = 0
M_10BIT = 70
M_12BIT = 72
M_1300 = 1355808768
M_1300C = 1372585984
M_1300NIR = 1389363200
M_1394_BANDWIDTH_FLAG = 2048
M_1394_FINGERPRINT = 20816
M_14BIT = 74
M_16BIT = 76
M_16VD = 262144
M_180_DEGREE = 180
M_1D_COLUMNS = 32
M_1D_ROWS = 16
M_1VD = 16384
M_2000 = 1345454336
M_2000C = 1362231552
M_2000NIR = 1379008768
M_270_DEGREE = 270
M_2D = 90
M_2D_CALIBRATION = 1
M_2D_COMPONENT = 134217728
M_2VD = 32768
M_300 = 1355809024
M_300C = 1372586240
M_300NIR = 1389363456
M_3DGEO_DRAW_3D_CONTEXT = 140738025226244
M_3DGEO_GEOMETRY = 140738025226241
M_3DGEO_OBJECT = 140738025226240
M_3DGEO_TRANSFORMATION_MATRIX = 140738025226242
M_3DIM_CALCULATE_MAP_SIZE_CONTEXT = 70369281048577
M_3DIM_FILL_GAPS_CONTEXT = 70369281048704
M_3DIM_MESH_CONTEXT = 70369281048580
M_3DIM_NORMALS_CONTEXT = 70369281048584
M_3DIM_OBJECT = 70369281048576
M_3DIM_PROFILE_RESULT = 70369281048832
M_3DIM_PSEUDO_ID = 10485760
M_3DIM_STATISTICS_CONTEXT = 70369281048592
M_3DIM_STATISTICS_RESULT = 70369281048640
M_3DIM_STAT_PSEUDO_ID = 10682368
M_3DIM_SUBSAMPLE_CONTEXT = 70369281048578
M_3DIM_SURFACE_SAMPLE_CONTEXT = 70369281048608
M_3DMAP_ALIGNMENT_RESULT = 17716740352
M_3DMAP_ALIGN_CONTEXT = 17716741120
M_3DMAP_ALIGN_RESULT = 17716742144
M_3DMAP_DEPTH_CORRECTED_DATA = 17716740128
M_3DMAP_DRAW_3D_CONTEXT = 17716740608
M_3DMAP_GEOMETRY = 17716740100
M_3DMAP_LASER_CALIBRATION_DATA = 17716740112
M_3DMAP_LASER_CONTEXT = 17716740097
M_3DMAP_OBJECT = 17716740096
M_3DMAP_PAIRWISE_ALIGNMENT_CONTEXT = 17716740224
M_3DMAP_POINT_CLOUD_CONTAINER = 17716740160
M_3DMAP_POINT_CLOUD_RESULT = 17716740160
M_3DMAP_STAT_RESULT = 17716740104
M_3DMET_DRAW_3D_CONTEXT = 17716740104
M_3DMET_FIT_CONTEXT = 562950490292226
M_3DMET_FIT_RESULT = 562950490292256
M_3DMET_OBJECT = 562950490292224
M_3DMET_STATISTICS_CONTEXT = 562950490292228
M_3DMET_STATISTICS_RESULT = 562950490292288
M_3DREG_OBJECT = 1125900443713536
M_3DREG_PAIRWISE_REGISTRATION_CONTEXT = 1125900443713537
M_3DREG_PAIRWISE_REGISTRATION_RESULT = 1125900443713540
M_3D_CALIBRATION = 2
M_3D_CONTAINER_CALIBRATION_INITIALIZATION = 4135
M_3D_CONVERTIBLE = 1092
M_3D_COORDINATE_SYSTEM_TYPE = 5103
M_3D_DISPARITY_BASELINE = 33554442
M_3D_DISPARITY_FOCAL_LENGTH = 33554441
M_3D_DISPARITY_PRINCIPAL_POINT_X = 33554443
M_3D_DISPARITY_PRINCIPAL_POINT_Y = 33554444
M_3D_DISPLAY = 550292684801
M_3D_DISPLAYABLE = 1089
M_3D_DISPLAY_OBJECT = 550292684800
M_3D_DISTANCE_UNIT = 5102
M_3D_GRAPHIC = 1100048498690
M_3D_GRAPHIC_LIST = 1100048498689
M_3D_GRAPHIC_LIST_ID = 4111
M_3D_GRAPHIC_LIST_OBJECT = 1100048498688
M_3D_INVALID_DATA_FLAG = 5105
M_3D_INVALID_DATA_VALUE = 33554440
M_3D_OFFSET_X = 33554437
M_3D_OFFSET_Y = 33554438
M_3D_OFFSET_Z = 33554439
M_3D_POINTS_I = 4
M_3D_POINTS_X = 1
M_3D_POINTS_Y = 2
M_3D_POINTS_Z = 3
M_3D_PROCESSABLE = 1088
M_3D_PROCESSABLE_MESHED = 1091
M_3D_PROPERTIES_DEFAULT = 5110
M_3D_REPRESENTATION = 5104
M_3D_ROBOTICS = 16
M_3D_SCALE_X = 33554434
M_3D_SCALE_Y = 33554435
M_3D_SCALE_Z = 33554436
M_3D_SHEAR_X = 33554449
M_3D_SHEAR_Z = 33554450
M_3X3_CROSS = 9437205
M_3X3_RECT = 9437204
M_3_COLORS_COLLINEAR = 668
M_480 = 1342439424
M_480C = 1359216640
M_480NIR = 1375993856
M_4K_ALIGNMENT = 4096
M_4SIGHT = 512
M_4SIGHTGPM_FINGERPRINT = 21056
M_4SIGHTGP_FINGERPRINT = 21184
M_4SIGHTM_FINGERPRINT = 20784
M_4SIGHTX_FINGERPRINT = 21040
M_4SIGHT_EV6 = 1048576
M_4SIGHT_GP = 65536
M_4SIGHT_GPM = 262144
M_4SIGHT_GPM_BT = 524288
M_4SIGHT_GP_NEXIS2 = 131072
M_4SIGHT_II = 1024
M_4SIGHT_M = 32768
M_4SIGHT_X = 8192
M_4VD = 131072
M_4_CONNECTED = 16
M_4_STATE = 134217735
M_4_STATE_NAME = MIL_TEXT("4-State")
M_500 = 1355809280
M_5000 = 1345454080
M_5000C = 1362231296
M_5000NIR = 1379008512
M_500C = 1372586496
M_500NIR = 1389363712
M_5X5_RECT = 9437214
M_64BIT_PHYSICAL_ADDRESS = 32768
M_64BIT_PHYSICAL_ADDRESS_BAND = 6750
M_64BIT_PHYSICAL_ADDRESS_BAND_REMOTE = 6733
M_64BIT_PHYSICAL_ADDRESS_REMOTE = 6701
M_64BIT_RESULT_BUFFERS_SUPPORT = 4378
M_8BIT = 68
M_8_CONNECTED = 32
M_90_DEGREE = 90
M_ABOVE = 4076
M_ABOVE_4GB = 8589934592
M_ABOVE_NORMAL = 9
M_ABS = 12
M_ABSENT = 3
M_ABSOLUTE = 1
M_ABSOLUTE_APERTURE_SIZE = 32837
M_ABSOLUTE_APERTURE_SIZE_INPUT_UNITS = 32840
M_ABSOLUTE_BASE = 5
M_ABSOLUTE_COORDINATE_SYSTEM = 16777216
M_ABSOLUTE_CTL_MASK = 524288
M_ABSOLUTE_DISTANCE_TO_SURFACE = 2986
M_ABSOLUTE_DISTANCE_Z_TO_SURFACE = 2985
M_ABSOLUTE_MODE = 2048
M_ABSOLUTE_VALUE = 50
M_ABS_SUB = 273
M_ABS_SUM_OF_DIFFERENCES = 3
M_AC = 4
M_ACCELERATOR = 1813
M_ACCELERATOR_DISABLE = 32
M_ACCELERATOR_PRESENT = 2322
M_ACCELERATOR_SPEED = 2321
M_ACCELERATOR_USAGE = 2304
M_ACCEPTANCE = 200
M_ACCEPTANCE_LEVEL = 1022
M_ACCEPTANCE_RELEVANCE = 202
M_ACCEPTANCE_TARGET = 201
M_ACCESS_ERROR = 10
M_ACCORDING_TO_CALIBRATION = 1301
M_ACCORDING_TO_REGION = 1073741824
M_ACCORDING_TO_SOURCE = -1
M_ACCUMULATE = 512
M_ACCUMULATE_AND_COMPUTE = 513
M_ACCURACY = 106
M_ACCURACY_MAX_ANGLE_DEVIATION = 107
M_ACQUIRE_WINDOW_FOCUS = 10065
M_ACQUISITION_END = 19
M_ACQUISITION_ERROR = 32784
M_ACQUISITION_PATH = 5329
M_ACQUISITION_START = 18
M_ACQUISITION_TRANSFER_END = 21
M_ACQUISITION_TRANSFER_START = 20
M_ACQUISITION_TRIGGER = 17
M_ACTION_KEYS = 2746
M_ACTION_KEY_AUTO_ROTATE = 4658
M_ACTION_KEY_CANCEL = 2747
M_ACTION_KEY_DELETE = 2748
M_ACTION_KEY_ORBIT_DOWN = 4645
M_ACTION_KEY_ORBIT_LEFT = 4642
M_ACTION_KEY_ORBIT_RIGHT = 4643
M_ACTION_KEY_ORBIT_UP = 4644
M_ACTION_KEY_ORIENTATION_BOTTOM_TILTED = 4666
M_ACTION_KEY_ORIENTATION_BOTTOM_VIEW = 4660
M_ACTION_KEY_ORIENTATION_FRONT_VIEW = 4661
M_ACTION_KEY_ORIENTATION_LEFT_VIEW = 4663
M_ACTION_KEY_ORIENTATION_REAR_VIEW = 4662
M_ACTION_KEY_ORIENTATION_RIGHT_VIEW = 4664
M_ACTION_KEY_ORIENTATION_TOP_TILTED = 4665
M_ACTION_KEY_ORIENTATION_TOP_VIEW = 4659
M_ACTION_KEY_RESET = 4652
M_ACTION_KEY_RESIZE_HEIGHT_DOWN = 2749
M_ACTION_KEY_RESIZE_HEIGHT_UP = 2750
M_ACTION_KEY_RESIZE_WIDTH_DOWN = 2751
M_ACTION_KEY_RESIZE_WIDTH_UP = 2752
M_ACTION_KEY_ROLL_LEFT = 4640
M_ACTION_KEY_ROLL_RIGHT = 4641
M_ACTION_KEY_ROTATE_CLOCKWISE = 2753
M_ACTION_KEY_ROTATE_COUNTER_CLOCKWISE = 2754
M_ACTION_KEY_TRANSLATE_BACKWARD = 4639
M_ACTION_KEY_TRANSLATE_DOWN = 2755
M_ACTION_KEY_TRANSLATE_FORWARD = 4638
M_ACTION_KEY_TRANSLATE_LEFT = 2756
M_ACTION_KEY_TRANSLATE_RIGHT = 2757
M_ACTION_KEY_TRANSLATE_UP = 2758
M_ACTION_KEY_TURN_DOWN = 4649
M_ACTION_KEY_TURN_LEFT = 4646
M_ACTION_KEY_TURN_RIGHT = 4647
M_ACTION_KEY_TURN_UP = 4648
M_ACTION_KEY_ZOOM_IN = 4650
M_ACTION_KEY_ZOOM_OUT = 4651
M_ACTION_MODIFIER_SPEED = 2759
M_ACTION_RESIZE_INCREMENT = 2760
M_ACTION_RESIZE_INCREMENT_ALTERNATE = 2761
M_ACTION_ROTATE_INCREMENT = 2762
M_ACTION_ROTATE_INCREMENT_ALTERNATE = 2763
M_ACTION_TRANSLATE_AXES = 2766
M_ACTION_TRANSLATE_INCREMENT = 2764
M_ACTION_TRANSLATE_INCREMENT_ALTERNATE = 2765
M_ACTIVATE = 1
M_ACTIVE = 1534
M_ACTIVE_AUTHOR_INDEX = 3777
M_ACTIVE_AUTHOR_UPDATE = 3924
M_ACTIVE_EDGELS = 1719
M_ACTIVE_ERROR = 32
M_ACTUAL_SIZE = 3226
M_ADAPTATIVE_AVERAGE = 35
M_ADAPTATIVE_BOB = 37
M_ADAPTATIVE_DISCARD = 36
M_ADAPTIVE = 2048
M_ADAPTIVE_AVERAGE = 35
M_ADAPTIVE_BOB = 37
M_ADAPTIVE_DISCARD = 36
M_ADAPTIVE_FAST = 8192
M_ADAPTIVE_INTENSITY_DELTA = 2023
M_ADAPTIVE_SMOOTHING = 2022
M_ADD = 0
M_ADD_BUFFER_INFO = 2036
M_ADD_CALIBRATION_USE = 17
M_ADD_COLOR_TO_SAMPLE = 4096
M_ADD_CONST = 32768
M_ADD_DESTINATION = 1192
M_ADD_FROM_GRAPHIC_LIST = 12
M_ADD_PERMITTED_CHARS_ENTRY = 2282
M_ADD_POINT = 1745
M_ADD_SCRIPT_REFERENCE = 55
M_ADD_SEARCH_AREA_X = 91
M_ADD_SEARCH_AREA_Y = 92
M_ADV7183 = 1
M_ADV7184 = 2
M_ADVANCED = 4194304
M_ADVANCED_FEATURE = -2147483648
M_ADVANCED_FEATURE_SET_ID = 5192
M_ADVANCED_FEATURE_UNLOCK = 5193
M_AFFINE = 3416
M_AFTER_DISPATCHED = 3
M_AGGRESSIVE_FILTERING = 977
M_AGP_TO_PCI_TRANSFER = 2433
M_ALIGNEMENT_MODE = 51
M_ALIGNMENT_MATRIX = 1950
M_ALIGNMENT_RESERVED_BITS = 255
M_ALIGNMENT_RESULT = 1921
M_ALIGN_COMPLETED = 2777
M_ALIGN_CONTEXT = 4891
M_ALIGN_LEFT = 1073741840
M_ALIGN_RESULT = 4892
M_ALIGN_RMS_ERROR = 1333
M_ALIGN_RMS_ERROR_RELATIVE = 1973
M_ALIGN_RMS_ERROR_RELATIVE_THRESHOLD = 1952
M_ALIGN_RMS_ERROR_THRESHOLD = 1951
M_ALIGN_RMS_ERROR_THRESHOLD_REACHED = 1970
M_ALIGN_TOP = 1073741841
M_ALIGN_XY_DIRECTION = 5363
M_ALIGN_X_POSITION = 5236
M_ALIGN_Z_DIRECTION = 5239
M_ALIGN_Z_POSITION = 5237
M_ALL = 1073741824
M_ALLOC = 65536
M_ALLOCATED_SIZE_BYTE = 8208
M_ALLOCATED_TYPE = 2183
M_ALLOCATED_USING_BUF_CREATE = 1059
M_ALLOCATE_MEMORY = 8206
M_ALLOCATION = 1048576
M_ALLOCATION_FAILURE_REAL_TEST_FLAG = 971
M_ALLOCATION_OVERSCAN = 32768
M_ALLOCATION_OVERSCAN_SIZE = 32769
M_ALLOC_ANGLE = 3329
M_ALLOC_BUF_RGB888_AS_RGB555 = 2044
M_ALLOC_ERROR = 8
M_ALLOC_ERROR_2 = 42
M_ALLOC_ERROR_3 = 55
M_ALLOC_ERROR_4 = 78
M_ALLOC_ERROR_5 = 92
M_ALLOC_ERROR_6 = 105
M_ALLOC_ERROR_7 = 148
M_ALLOC_ERROR_8 = 182
M_ALLOC_ERROR_9 = 197
M_ALLOC_OFFSET_X = 15
M_ALLOC_OFFSET_Y = 16
M_ALLOC_SIGN = 323
M_ALLOC_SIZE_BAND = 321
M_ALLOC_SIZE_BIT = 26
M_ALLOC_SIZE_X = 2
M_ALLOC_SIZE_Y = 3
M_ALLOC_TYPE = 322
M_ALLOC_WITH_FORCED_PITCH_SUPPORT = 4442
M_ALLOW_BUFFER_WITH_REGION = 32768
M_ALLOW_BUFFER_WITH_REGION_MODIFY = 4
M_ALLOW_DEFAULT_ID = 4096
M_ALLOW_DUPLICATES = 134217728
M_ALLOW_GRA_MESSAGE_WITH_NO_UPDATE = 10120
M_ALLOW_LARGER_RECT = 256
M_ALLOW_NONPAGED_BUFFERS_IN_VIDEO_MEMORY = 8548
M_ALLOW_NULL_ID = 2048
M_ALLOW_NULL_VALUE = 2048
M_ALLOW_PSEUDO_ID = 8192
M_ALL_BAND = -1
M_ALL_BANDS = -1
M_ALL_BITS = -1
M_ALL_BLOBS = 1073741824
M_ALL_BUFFER_TYPES = 8796231954500
M_ALL_CHANNEL = 1879031808
M_ALL_CHANNELS = 1879031808
M_ALL_CHAR = 32768
M_ALL_CONSTRAINED_POSITIONS = 1075838976
M_ALL_CRITERIA = 2
M_ALL_DEV_ARE_EQUIVALENT = 4387
M_ALL_DISPLAYS = 8388611
M_ALL_DISPLAY_SCHEMES = -2147483648
M_ALL_EDGELS = 0
M_ALL_EDGES = 2097152
M_ALL_FAIL_TOLERANCES = 518
M_ALL_FEATURES = 256
M_ALL_FERETS = 122
M_ALL_INIT_FLAGS = 1106638383
M_ALL_ITERATIONS = 16777216
M_ALL_METHOD = 4026527744
M_ALL_NEAREST_NEIGHBORS = 128
M_ALL_OBJECTS = 67108864
M_ALL_OCCURRENCES = 1073758207
M_ALL_PASS_TOLERANCES = 514
M_ALL_POINTS = 1998
M_ALL_POINTS_COLINEAR = 1337
M_ALL_POINTS_COLLINEAR = 1337
M_ALL_POINTS_COPLANAR = 4742
M_ALL_PROPERTIES = 4
M_ALL_REF = 1874853888
M_ALL_SELECTED = 67108864
M_ALL_SUBREGIONS = 16383
M_ALL_TOLERANCES = 512
M_ALL_VALID_DISP_DEV_BITS = 462783
M_ALL_WARNING_TOLERANCES = 516
M_ALONG_HEIGHT = 1698
M_ALONG_WIDTH = 1697
M_ALPHA_BLENDING = 8388608
M_ALPHA_VALUE = 5278
M_ALTERNATE_SPEED_FACTOR = 4653
M_ALWAYS = 0
M_ALWAYS_SHOW_AXES = 8388608
M_ALWAYS_SYNCHRONOUS = 1073741824
M_AMD_64 = 10244
M_ANALOG = 1
M_ANCESTOR_APPLICATION = 15505
M_ANCESTOR_ID = 1104
M_ANCESTOR_OFFSET_BAND = 5008
M_ANCESTOR_OFFSET_BIT = 5038
M_ANCESTOR_OFFSET_X = 5005
M_ANCESTOR_OFFSET_Y = 5006
M_ANCESTOR_SIZE_X = 5012
M_AND = 23
M_AND_ARM_ACTIVATION = 16777216
M_AND_CONST = 32791
M_ANGLE = 2048
M_ANGLE_ABSOLUTE = 57
M_ANGLE_ACCURACY = 4096
M_ANGLE_ACCURACY_MAX_DEVIATION = 107
M_ANGLE_AT_POSITION = 1787
M_ANGLE_DELTA_NEG = 512
M_ANGLE_DELTA_POS = 1024
M_ANGLE_END = 2050
M_ANGLE_ID = 536870912
M_ANGLE_MULTIPLE_RANGE = 2803
M_ANGLE_REGION = 3095
M_ANGLE_RELATIVE = 64
M_ANGLE_SNAPPING = 2688
M_ANGLE_SNAPPING_VALUE = 2687
M_ANGLE_START = 2049
M_ANGLE_VALUE = 2048
M_ANGULARITY = 3
M_ANGULAR_DATA_COHERENCE = 2048
M_ANGULAR_DATA_MEAN = 4
M_ANNOTATIONS_DC = 3
M_ANNOTATIONS_DRAW = 60
M_ANNOTATIONS_PIXMAP = 3
M_ANSI_VERIFICATION = 32
M_ANTIALIASING = 4096
M_ANY = 285212672
M_ANY_CRITERIA = 1
M_ANY_EDGE = 50
M_ANY_FIELD = 4
M_ANY_FINGERPRINT = 21472
M_ANY_INTERNAL_FORMAT = 0
M_ANY_SIGN = 67108864
M_ANY_TYPE = 268435456
M_APERTURE_MODE = 32835
M_APERTURE_SIZE_USED = 1655
M_APP = 1
M_APPEARANCE = 4679
M_APPEND = 536870912
M_APPLICATION = 512
M_APPLICATION_ALLOCATED = 15122
M_APPLY_SCALE = 1523
M_APPROXIMATION = 134217728
M_APPROXIMATION_TOLERANCE = 26
M_APP_ALLOC_INIT_FLAGS = 267386880
M_APP_BH_DISPLAY_END = 12099
M_APP_BH_DISPLAY_START = 12000
M_APP_CTRL_INQ_ERROR = 108
M_APP_DIRECTX_RANGE_END = 15374
M_APP_DIRECTX_RANGE_START = 15300
M_APP_DISPLAY_END = 15450
M_APP_DISPLAY_START = 15375
M_APP_FREE_ERROR = 32
M_APP_FREE_ERROR_2 = 134
M_APP_GENERAL_DISPLAY_START = 15375
M_APP_INQUIRE_DIRECT_ACCESS_STRING_END = 15949
M_APP_INQUIRE_DIRECT_ACCESS_STRING_START = 15890
M_APP_INQUIRE_OBJ_DOUBLE_RANGE_END = 20000
M_APP_INQUIRE_OBJ_DOUBLE_RANGE_START = 10000
M_APP_INQUIRE_OBJ_INT64_RANGE_END = 21000
M_APP_INQUIRE_OBJ_INT64_RANGE_START = 20001
M_APP_INQUIRE_OBJ_STRING_END = 105
M_APP_INQUIRE_OBJ_STRING_START = 47
M_APP_INQUIRE_REG_DEF_STRING_2_END = 23959
M_APP_INQUIRE_REG_DEF_STRING_2_START = 23000
M_APP_INQUIRE_REG_DEF_STRING_END = 16296
M_APP_INQUIRE_REG_DEF_STRING_START = 15977
M_APP_INQUIRE_SIZEOF_INT64_END = 6799
M_APP_INQUIRE_SIZEOF_INT64_START = 6700
M_APP_INQUIRE_SYS_END = 30000
M_APP_INQUIRE_SYS_START = 15000
M_APP_LAST_FREE = 31
M_APP_MODIF_ERROR = 80
M_APP_SCREEN_MANAGER_END = 9249
M_APP_SCREEN_MANAGER_START = 9200
M_APP_TRACE_ERROR_1 = 152
M_ARC = 129
M_ARC_STYLE = 1722
M_ARC_THREE_POINTS = 2728
M_AREA = 2
M_AREA_BETWEEN_CURVES = 3194
M_AREA_BETWEEN_CURVES_DEFINE_SIDE = 4067
M_AREA_BETWEEN_CURVES_ONE_SIDE_ONLY = 4066
M_AREA_BETWEEN_CURVES_OPPOSITES_SUBTRACT = 3070
M_AREA_CLOSE = 8
M_AREA_CONVEX_HULL = 3186
M_AREA_IMAGE_SIGN = 334
M_AREA_IMAGE_SIZE_BAND = 333
M_AREA_IMAGE_SIZE_BIT = 332
M_AREA_IMAGE_SIZE_X = 330
M_AREA_IMAGE_SIZE_Y = 331
M_AREA_IMAGE_TYPE = 335
M_AREA_LABEL_VALUE = 802
M_AREA_MATCH_IMAGE_SIZE_X = 1449
M_AREA_MATCH_IMAGE_SIZE_Y = 1450
M_AREA_OPEN = 7
M_AREA_PIXEL_COUNT = 838
M_AREA_SIMPLE = 3184
M_AREA_UNDER_CURVE_ALLOW_NEGATIVE = 3196
M_AREA_UNDER_CURVE_MAX = 3074
M_AREA_UNDER_CURVE_MIN = 3073
M_ARM_CONTINUOUS = 9
M_ARM_CORTEX_A_SERIES = 10245
M_ARM_MONOSHOT = 10
M_ARM_RESET = 11
M_ARRAY = 64
M_ARRAY_ID_MASK = 1048575
M_ARROW_HEAD = 1644
M_ASCENDING = 1
M_ASCII = 1
M_ASCII_CLIENT = 67108864
M_ASPECT_RATIO = 6001
M_ASSIGN = 256
M_ASSOCIATED_AUDIO_BUFFER_ID = 1108
M_ASSOCIATED_CALIBRATION = 125
M_ASSOCIATED_CONTEXT_TYPE = 2968
M_ASSOCIATED_EXT_VIDEO_DEVICE_ID = 2317
M_ASSOCIATED_GRAPHIC_LIST_ID = 10562
M_ASSOCIATED_LUT = 1110
M_ASSOCIATED_NAME = 47
M_ASSOCIATED_NAME_SIZE = 5497558138927
M_ASSOCIATED_REMOTE_DISPLAY_ID = 10572
M_ASSOCIATED_STREAM = 8226
M_ASSOCIATED_VGA_BUFFER_ID = 5078
M_ASSOCIATED_VGA_DEVICE = 2171
M_ASSOCIATED_VIDEO_DEVICE_INDEX = 2316
M_ASSUMED_PERPENDICULAR_TO_MOTION = 1878
M_ASTERISK = 41038
M_ASYNCHRONOUS = 2
M_ASYNCHRONOUS_CALL_SUPPORT = 4376
M_ASYNCHRONOUS_DISPLAY_SURFACE = 1126
M_ASYNCHRONOUS_FUNCTION = 0
M_ASYNCHRONOUS_QUEUED = 3
M_ASYNC_CUSTOM = 2
M_ASYNC_ERROR = 1073741824
M_ASYNC_HOOK = 134217728
M_ASYNC_UPDATE = 10206
M_AS_VALUE = 16384
M_ATAN2 = 270
M_ATTACHED_BUFFER_0_ID = 5076
M_ATTACHED_BUFFER_1_ID = 5077
M_ATTRIBUTE = 1013
M_AUDIO = 8796093022208
M_AUDIO_ADPCM = 2
M_AUDIO_ALAW = 4
M_AUDIO_MODULE = 1048576
M_AUDIO_MONO = 1
M_AUDIO_MULAW = 3
M_AUDIO_RAW_16 = 1
M_AUDIO_STEREO = 2
M_AUGMENTATION_CONTEXT = 18
M_AUGMENTATION_RESULT = 1125899906842624
M_AUGMENTATION_SOURCE = 3841
M_AUGMENTATION_SOURCE_KEY = 3842
M_AUG_ASPECT_RATIO = 3269
M_AUG_ASPECT_RATIO_MODE = 3373
M_AUG_ASPECT_RATIO_OP = 3107
M_AUG_ASPECT_RATIO_OP_MAX = 2879
M_AUG_ASPECT_RATIO_OP_MIN = 2878
M_AUG_ASPECT_RATIO_OP_MODE = 2880
M_AUG_BLUR_MOTION_ANGLE = 3284
M_AUG_BLUR_MOTION_OP = 2923
M_AUG_BLUR_MOTION_OP_ANGLE_MAX = 2927
M_AUG_BLUR_MOTION_OP_ANGLE_MIN = 2926
M_AUG_BLUR_MOTION_OP_SIZE_MAX = 2925
M_AUG_BLUR_MOTION_OP_SIZE_MIN = 2924
M_AUG_BLUR_MOTION_SIZE = 3283
M_AUG_CROP_BOTTOM_RIGHT_X = 3289
M_AUG_CROP_BOTTOM_RIGHT_Y = 3290
M_AUG_CROP_OP = 3102
M_AUG_CROP_OP_FACTOR_X = 2884
M_AUG_CROP_OP_FACTOR_Y = 2885
M_AUG_CROP_OP_RESIZE = 2886
M_AUG_CROP_TOP_LEFT_X = 3287
M_AUG_CROP_TOP_LEFT_Y = 3288
M_AUG_DILATION_ASYM_NB_ITERATIONS = 3274
M_AUG_DILATION_ASYM_OP = 3100
M_AUG_DILATION_ASYM_OP_NB_ITERATIONS_MAX = 2881
M_AUG_DILATION_ASYM_SUBAREA = 3275
M_AUG_DILATION_NB_ITERATIONS = 3272
M_AUG_DILATION_OP = 3098
M_AUG_DILATION_OP_NB_ITERATIONS_MAX = 2873
M_AUG_EROSION_ASYM_NB_ITERATIONS = 3276
M_AUG_EROSION_ASYM_OP = 3101
M_AUG_EROSION_ASYM_OP_NB_ITERATIONS_MAX = 2882
M_AUG_EROSION_ASYM_SUBAREA = 3277
M_AUG_EROSION_NB_ITERATIONS = 3273
M_AUG_EROSION_OP = 3099
M_AUG_EROSION_OP_NB_ITERATIONS_MAX = 2875
M_AUG_FLIP_DIRECTION = 3374
M_AUG_FLIP_OP = 2870
M_AUG_FLIP_OP_DIRECTION = 3120
M_AUG_GAMMA_OP = 2962
M_AUG_GAMMA_OP_DELTA = 2963
M_AUG_GAMMA_OP_MODE = 2942
M_AUG_GAMMA_OP_VALUE = 6672
M_AUG_GAMMA_VALUE_BAND_0 = 3367
M_AUG_GAMMA_VALUE_BAND_1 = 3369
M_AUG_GAMMA_VALUE_BAND_2 = 3371
M_AUG_HSV_VALUE_GAIN = 3280
M_AUG_HSV_VALUE_GAIN_OP = 2914
M_AUG_HSV_VALUE_GAIN_OP_MAX = 2919
M_AUG_HSV_VALUE_GAIN_OP_MIN = 2918
M_AUG_HUE_OFFSET = 3281
M_AUG_HUE_OFFSET_OP = 2917
M_AUG_HUE_OFFSET_OP_MAX = 2916
M_AUG_HUE_OFFSET_OP_MIN = 2915
M_AUG_INTENSITY_ADD_OP = 2887
M_AUG_INTENSITY_ADD_OP_DELTA = 2958
M_AUG_INTENSITY_ADD_OP_MODE = 2883
M_AUG_INTENSITY_ADD_OP_VALUE = 204
M_AUG_INTENSITY_ADD_VALUE = 3366
M_AUG_INTENSITY_MULTIPLY_OP = 2940
M_AUG_INTENSITY_MULTIPLY_OP_DELTA = 2941
M_AUG_INTENSITY_MULTIPLY_OP_MODE = 2959
M_AUG_INTENSITY_MULTIPLY_OP_VALUE = 206
M_AUG_INTENSITY_MULTIPLY_VALUE = 3365
M_AUG_LIGHTING_DIRECTIONAL_ANGLE = 3278
M_AUG_LIGHTING_DIRECTIONAL_OP = 3108
M_AUG_LIGHTING_DIRECTIONAL_OP_ANGLE_MAX = 2894
M_AUG_LIGHTING_DIRECTIONAL_OP_INTENSITY_MAX = 2896
M_AUG_LIGHTING_DIRECTIONAL_OP_INTENSITY_MIN = 2895
M_AUG_NOISE_GAUSSIAN_ADDITIVE_OP = 2955
M_AUG_NOISE_GAUSSIAN_ADDITIVE_OP_STDDEV = 2956
M_AUG_NOISE_GAUSSIAN_ADDITIVE_OP_STDDEV_DELTA = 2957
M_AUG_NOISE_GAUSSIAN_ADDITIVE_STDDEV = 3377
M_AUG_NOISE_MULTIPLICATIVE_OP = 2950
M_AUG_NOISE_MULTIPLICATIVE_OP_DISTRIBUTION = 2954
M_AUG_NOISE_MULTIPLICATIVE_OP_INTENSITY_MIN = 2953
M_AUG_NOISE_MULTIPLICATIVE_OP_STDDEV = 2951
M_AUG_NOISE_MULTIPLICATIVE_OP_STDDEV_DELTA = 2952
M_AUG_NOISE_MULTIPLICATIVE_STDDEV = 3376
M_AUG_NOISE_SALT_PEPPER_DENSITY = 3375
M_AUG_NOISE_SALT_PEPPER_OP = 2947
M_AUG_NOISE_SALT_PEPPER_OP_DENSITY = 2948
M_AUG_NOISE_SALT_PEPPER_OP_DENSITY_DELTA = 2949
M_AUG_OPERATIONS_APPLIED = 3292
M_AUG_OPERATIONS_ENABLED = 3291
M_AUG_OPERATION_ASSOCIATED_WITH_RESULT_TYPES = 3295
M_AUG_OPERATION_RESULT_TYPES = 3293
M_AUG_OPERATION_RESULT_VALUES = 3294
M_AUG_OPTIMAL_SIZE_X = 3419
M_AUG_OPTIMAL_SIZE_Y = 3420
M_AUG_REVERSE_TRANSFORMATION_MATRIX = 3399
M_AUG_RNG_INIT_VALUE = 2867
M_AUG_ROTATION_ANGLE = 3265
M_AUG_ROTATION_OP = 3103
M_AUG_ROTATION_OP_ANGLE_DELTA = 3349
M_AUG_ROTATION_OP_ANGLE_MAX = 2805
M_AUG_ROTATION_OP_ANGLE_MIN = 3351
M_AUG_ROTATION_OP_ANGLE_REF = 3348
M_AUG_ROTATION_OP_ANGLE_STEP = 3350
M_AUG_SATURATION_GAIN = 3279
M_AUG_SATURATION_GAIN_OP = 2910
M_AUG_SATURATION_GAIN_OP_MAX = 2912
M_AUG_SATURATION_GAIN_OP_MIN = 2911
M_AUG_SCALE_FACTOR = 3268
M_AUG_SCALE_OP = 3104
M_AUG_SCALE_OP_FACTOR_MAX = 2876
M_AUG_SCALE_OP_FACTOR_MIN = 2877
M_AUG_SEED_MODE = 3421
M_AUG_SEED_USED = 3423
M_AUG_SHARPEN_DERICHE_OP = 2928
M_AUG_SHARPEN_DERICHE_OP_FACTOR_MAX = 2930
M_AUG_SHARPEN_DERICHE_OP_FACTOR_MIN = 2929
M_AUG_SHARPEN_DERICHE_VALUE = 3285
M_AUG_SHEAR_X = 3270
M_AUG_SHEAR_X_OP = 2892
M_AUG_SHEAR_X_OP_MAX = 2889
M_AUG_SHEAR_X_OP_MIN = 2888
M_AUG_SHEAR_Y = 3271
M_AUG_SHEAR_Y_OP = 2893
M_AUG_SHEAR_Y_OP_MAX = 2891
M_AUG_SHEAR_Y_OP_MIN = 2890
M_AUG_SMOOTH_DERICHE_OP = 2920
M_AUG_SMOOTH_DERICHE_OP_FACTOR_MAX = 2922
M_AUG_SMOOTH_DERICHE_OP_FACTOR_MIN = 2921
M_AUG_SMOOTH_DERICHE_VALUE = 3282
M_AUG_SMOOTH_GAUSSIAN_OP = 2932
M_AUG_SMOOTH_GAUSSIAN_OP_STDDEV_MAX = 2934
M_AUG_SMOOTH_GAUSSIAN_OP_STDDEV_MIN = 2933
M_AUG_SMOOTH_GAUSSIAN_STDDEV = 3286
M_AUG_TRANSLATION_X = 3266
M_AUG_TRANSLATION_X_OP = 3105
M_AUG_TRANSLATION_X_OP_MAX = 2868
M_AUG_TRANSLATION_Y = 3267
M_AUG_TRANSLATION_Y_OP = 3106
M_AUG_TRANSLATION_Y_OP_MAX = 2869
M_AUTHORS = 3769
M_AUTHOR_ADD = 3770
M_AUTHOR_DELETE = 3771
M_AUTHOR_DELETE_BY_KEY = 3772
M_AUTHOR_INDEX_FLAG = 67108864
M_AUTHOR_KEY = 3774
M_AUTHOR_NAME = 3655
M_AUTO = 444
M_AUTOMATIC = 131072
M_AUTO_BIT_RATE_CONTROL = 2
M_AUTO_COLOR = 1048576
M_AUTO_COMPUTE = 134217729
M_AUTO_CONTENT_BASED = 1403
M_AUTO_CONTINUOUS = 445
M_AUTO_CURVE_CLOSED = 3195
M_AUTO_CURVE_OPENED = 3194
M_AUTO_DEFINE = 262144
M_AUTO_EXPOSURE = 5104
M_AUTO_FLIP_FOR_TRUE_COLOR = 2078
M_AUTO_FORMAT = 128
M_AUTO_LOCALIZE = 4096
M_AUTO_MODEL = 2210
M_AUTO_OFFSET_PROFILE = 2147483647
M_AUTO_REGISTER = 268435456
M_AUTO_REGISTER_CANCEL = 536870912
M_AUTO_RESET = 8192
M_AUTO_ROTATE = 4633
M_AUTO_SCALE = 2
M_AUTO_SCALE_ASPECT_RATIO = 1987
M_AUTO_SCALE_PROFILE = 2147483647
M_AUTO_SCALE_XY = 1988
M_AUTO_SCALE_Z = 1989
M_AUTO_SIZE_BASED = 1409
M_AUTO_UNIFORM = 444
M_AUTO_VALUE = 4294967296
M_AUX = 562949953421312
M_AUXILIARY = 65536
M_AUXILIARY_BUF_ID = 1115
M_AUXILIARY_KEEP_DISPLAY_ALIVE = 3207
M_AUXILIARY_KEEP_UNDERLAY_ALIVE = 3211
M_AUX_IO = 1280
M_AUX_IO0 = 1280
M_AUX_IO1 = 1281
M_AUX_IO10 = 1290
M_AUX_IO11 = 1291
M_AUX_IO12 = 1292
M_AUX_IO13 = 1293
M_AUX_IO14 = 1294
M_AUX_IO15 = 1295
M_AUX_IO16 = 1296
M_AUX_IO17 = 1297
M_AUX_IO18 = 1298
M_AUX_IO19 = 1299
M_AUX_IO2 = 1282
M_AUX_IO20 = 1300
M_AUX_IO21 = 1301
M_AUX_IO22 = 1302
M_AUX_IO23 = 1303
M_AUX_IO24 = 1304
M_AUX_IO25 = 1305
M_AUX_IO26 = 1306
M_AUX_IO27 = 1307
M_AUX_IO28 = 1308
M_AUX_IO29 = 1309
M_AUX_IO3 = 1283
M_AUX_IO30 = 1310
M_AUX_IO31 = 1311
M_AUX_IO32 = 1312
M_AUX_IO33 = 1313
M_AUX_IO34 = 1314
M_AUX_IO35 = 1315
M_AUX_IO36 = 1316
M_AUX_IO37 = 1317
M_AUX_IO38 = 1318
M_AUX_IO39 = 1319
M_AUX_IO4 = 1284
M_AUX_IO40 = 1320
M_AUX_IO41 = 1321
M_AUX_IO42 = 1322
M_AUX_IO43 = 1323
M_AUX_IO44 = 1324
M_AUX_IO45 = 1325
M_AUX_IO46 = 1326
M_AUX_IO47 = 1327
M_AUX_IO48 = 1328
M_AUX_IO49 = 1329
M_AUX_IO5 = 1285
M_AUX_IO50 = 1330
M_AUX_IO51 = 1331
M_AUX_IO52 = 1332
M_AUX_IO53 = 1333
M_AUX_IO54 = 1334
M_AUX_IO55 = 1335
M_AUX_IO56 = 1336
M_AUX_IO57 = 1337
M_AUX_IO58 = 1338
M_AUX_IO59 = 1339
M_AUX_IO6 = 1286
M_AUX_IO60 = 1340
M_AUX_IO61 = 1341
M_AUX_IO62 = 1342
M_AUX_IO63 = 1343
M_AUX_IO7 = 1287
M_AUX_IO8 = 1288
M_AUX_IO9 = 1289
M_AUX_IO_ALL = 4095
M_AUX_IO_COUNT = 4450
M_AUX_IO_COUNT_IN = 4451
M_AUX_IO_COUNT_OUT = 4452
M_AUX_SERVICE_ERROR = 91
M_AUX_VISIBLE = 562949953421312
M_AVAILABLE = 70368744177664
M_AVERAGE = 32
M_AVERAGE_2X2 = 4096
M_AVERAGE_IMAGE = 4
M_AVERAGE_MODE = 1891
M_AVERAGE_PIXEL_ERROR = 4096
M_AVERAGE_STRENGTH = 57
M_AVERAGE_WORLD_ERROR = 16384
M_AVG = 272
M_AVG_DISTANCE_TO_NEAREST_NEIGHBOR = 3442
M_AVI_CODEC = 16384
M_AVI_CODEC_UNSUPPORTED = -2
M_AVI_DIB = 256
M_AVI_FILE_ERROR = 51
M_AVI_FILE_ERROR_2 = 59
M_AVI_FILE_ERROR_3 = 61
M_AVI_FILE_ERROR_4 = 138
M_AVI_H264 = 2048
M_AVI_MIL = 128
M_AVI_MJPEG = 512
M_AVI_MJPG = 512
M_AVI_MPEG4 = 1024
M_AVI_MPG4 = 1024
M_AWAY_FROM_POSITION = 3433
M_AXIAL_NONUNIFORMITY = 40968
M_AXIAL_NONUNIFORMITY_GRADE = 36867
M_AXIS_ALIGNED = 262144
M_AXIS_ALIGNED_ELLIPSE = 2727
M_AXIS_ALIGNED_RECT = 2730
M_AXIS_PRINCIPAL_ANGLE = 44
M_AXIS_SECONDARY_ANGLE = 45
M_AXIS_X = 3664
M_AXIS_Y = 3665
M_AXIS_Z = 3666
M_AZIMUTH = 50
M_AZIM_ELEV_ROLL = 4
M_AZTEC = 134217738
M_AZTEC_NAME = MIL_TEXT("Aztec")
M_A_FORWARD = 16385
M_A_REVERSE = 16401
M_BACKCOLOR = 512
M_BACKGROUND_COLOR = 10066
M_BACKGROUND_COLOR_GRADIENT = 4654
M_BACKGROUND_DRAW_COLOR = 32
M_BACKGROUND_IMAGE = 4628
M_BACKGROUND_IMAGE_SIZE_BAND = 4631
M_BACKGROUND_IMAGE_SIZE_X = 4629
M_BACKGROUND_IMAGE_SIZE_Y = 4630
M_BACKGROUND_LABEL = 43
M_BACKGROUND_MODE = 12
M_BACKWARD = 2
M_BACKWARD_TRANSFORMATION = 8192
M_BACK_COLOR = 512
M_BAD_ESTIMATE = 3616
M_BALANCE = 1483
M_BAND = 1900544
M_BAND_MODE = 90
M_BAND_ORDER = 3036
M_BASELINE_THRESHOLD = 2263
M_BASE_BLACK_REF = 4002
M_BASE_FEATURES_ARRAY_SIZE = 1012
M_BASE_SUBFEATURES_ARRAY_SIZE = 1013
M_BASIC = 2097152
M_BASIC_ATTRIBUTE = 16777216
M_BASIC_BUFFER_PURPOSE = 56
M_BASIC_DISPLAY_EVENT = 134217740
M_BASIC_DISPLAY_SYSTEM_ID = 10067
M_BASIN = 2
M_BASIN_4_CONNECTED = 16384
M_BASIN_8_CONNECTED = 32768
M_BATCH_COUNT = 8211
M_BATCH_FLAGS = 8212
M_BATCH_INQUIRE = 8213
M_BAYER_BG = 64
M_BAYER_BIT_SHIFT_MASK = 32505856
M_BAYER_COEFFICIENTS_ID = 5328
M_BAYER_CONVERSION = 5326
M_BAYER_DEMOSAICING = 5350
M_BAYER_GB = 32
M_BAYER_GR = 128
M_BAYER_MASK = 480
M_BAYER_NORMALIZE = 512
M_BAYER_OVERSCAN_DISABLE = 524288
M_BAYER_OVERSCAN_ENABLE = 32768
M_BAYER_PATTERN = 5365
M_BAYER_REVERSE = 4
M_BAYER_RG = 96
M_BAYES_SHRINK = 9437442
M_BC412 = 64
M_BC412_NAME = MIL_TEXT("BC412")
M_BEAD_CONTEXT = 538968080
M_BEAD_EDGE = 2
M_BEAD_OBJECT = 538968064
M_BEAD_RESULT = 538968096
M_BEAD_STRIPE = 1
M_BEAD_TYPE = 1008
M_BEARER_BAR = 20992
M_BEGIN = -1
M_BELOW_4GB = 4294967296
M_BELOW_NORMAL = 7
M_BENCHMARK_ENABLE = 4
M_BENCHMARK_IN_DEBUG_ALLSIZE = 4
M_BENCHMARK_IN_DEBUG_CSTSIZE = 0
M_BENCHMARK_IN_DEBUG_NOTRACE = 0
M_BENCHMARK_IN_DEBUG_OFF = 0
M_BENCHMARK_IN_DEBUG_ON = 1
M_BENCHMARK_IN_DEBUG_TRACE = 2
M_BERNSEN = 1881
M_BEST = 1048576
M_BEST_CLASS_INDEX = 2847
M_BEST_CLASS_SCORE = 2889
M_BEST_DESKTOP_MONITOR = 9201
M_BEST_DESKTOP_RECT = 9202
M_BEST_EXCLUSIVE_MONITOR = 9203
M_BEST_MATCH_INDEX = 804
M_BEST_MATCH_LABEL = 805
M_BGR = 7
M_BGR15 = 3584
M_BGR16 = 3840
M_BGR24 = 4096
M_BGR30 = 4864
M_BGR32 = 4352
M_BGRX32 = 4352
M_BGRX32_COMPOSITION = 5
M_BGRX_ALPHA_VALUE = 5278
M_BGR_TO_BGR = 8
M_BGR_TO_MONO = 7
M_BGR_TO_YCBCRHD = 11
M_BGR_TO_YCBCRSD = 10
M_BGR_TO_YCRCBHD = 11
M_BGR_TO_YCRCBSD = 10
M_BGR_TO_YUV = 9
M_BH_BASE_BUFFER_TYPE = 15705
M_BH_INCOMPATIBLE_BUFFER_ATTRIBUTE = 15707
M_BH_IS_ALLOCATOR = 15710
M_BH_IS_CREATOR = 15711
M_BH_KNOWN_DISPLAY_ATTRIBUTE = 15712
M_BH_NEEDED_BUFFER_ATTRIBUTE = 15706
M_BH_TRANSFER_FUNCTION_SUPPORTED = 15709
M_BH_TRANSFER_METHOD = 15708
M_BICUBIC = 16
M_BIGGEST_ANGLE = 2538
M_BIG_ENDIAN = 524288
M_BILATERAL = 8389632
M_BILINEAR = 8
M_BILINEAR_INTERPOLATION = 8
M_BILINEAR_RENDERING = 1024
M_BIMODAL = 64
M_BINARIZATION_METHOD_MASK = 240
M_BINARIZE = 1048576
M_BINARIZE_ADAPTIVE_CONTEXT = 14
M_BINARIZE_ADAPTIVE_FROM_SEED_CONTEXT = 15
M_BINARY = 4096
M_BINARY2 = 1
M_BINARY3 = 2
M_BINARY_AND_GRAYSCALE = 4608
M_BINARY_ULTIMATE = 1
M_BINARY_ULTIMATE_ACCUMULATE = 2460
M_BIOS_REVISION = 2154
M_BISECTION = 8388608
M_BISECTOR = 54
M_BITBLT_METHOD = 32768
M_BITBLT_MODE = 32768
M_BITMAPINFO = 9026
M_BITMAP_HANDLE = 549755813888
M_BIT_RATE_CONTROL = 4
M_BIT_SHIFT = 3
M_BLACK = 0
M_BLACK_OFFSET = 4334
M_BLACK_REF = 6650
M_BLACK_REF_DOUBLE = 6650
M_BLANK = 2097152
M_BLANK_CHARACTERS = 73
M_BLIND_DETECT_SENSITIVITY_LEVEL = 5415
M_BLIND_DETECT_TEMPORAL_LEVEL = 5416
M_BLOB_CONTEXT = 537133060
M_BLOB_CONTRAST = 48
M_BLOB_FEATURE_LIST = 537133057
M_BLOB_IDENTIFICATION_MODE = 2960
M_BLOB_INCLUSION_STATE = 264
M_BLOB_INDEX_FLAG = 67108864
M_BLOB_OBJECT = 537133056
M_BLOB_ON_ACCELERATED = 60
M_BLOB_RESULT = 537133058
M_BLOB_TOUCHING_IMAGE_BORDERS = 118
M_BLT_ASYNC = 10
M_BLT_DESTRECT = 8
M_BLT_EVEN = 3
M_BLT_EVEN_EVEN = 5
M_BLT_FRAME = 1
M_BLT_MODE = 2
M_BLT_ODD = 2
M_BLT_ODD_ODD = 4
M_BLT_REGION = 1
M_BLT_SCALECONSTANT = 27
M_BLT_SCALELINEAR = 25
M_BLT_SCALENEAR = 26
M_BLT_SCALEYUV = 30
M_BLT_SCALEYUV2BGR = 28
M_BLT_SCALEYUV2Y = 29
M_BLT_SRCCOPY = 20
M_BLT_SRCKEYONBLACK = 21
M_BLT_SRCMIRRORLEFTRIGHT = 22
M_BLT_SRCMIRRORLRUPDN = 24
M_BLT_SRCMIRRORUPDOWN = 23
M_BLT_SRCRECT = 16
M_BLT_SYNC = 11
M_BLT_TYPE = 4
M_BLUE = 32
M_BMP = 64
M_BMP_ERROR = 18
M_BMP_ERROR_2 = 19
M_BMP_ERROR_3 = 53
M_BOARD = 8589934592
M_BOARD_CODE = 2066
M_BOARD_DEFAULTS_PTR = 24792
M_BOARD_DEFAULTS_PTR_OLD = 16548
M_BOARD_HOOK = 0
M_BOARD_REVISION = 2015
M_BOARD_REVISION_DAUGHTER = 2161
M_BOARD_REVISION_SENSOR = 2160
M_BOARD_SUB_REVISION = 2200
M_BOARD_TO_HOST_COLOR_CONVERSION_COEFFICIENTS = 4009754624
M_BOARD_TO_HOST_COLOR_CONVERSION_COEFFICIENTS_MASK = 4294901760
M_BOARD_TYPE = 2014
M_BOARD_TYPE_MASK = 255
M_BOB = 34
M_BOB_METHOD = 4
M_BOOTSTRAP = 3518
M_BORDER_ATTENUATION = 109
M_BOTH = 7
M_BOTH_CORNERS = 4
M_BOTH_FIELDS = 3
M_BOTH_SRC_VALID_LABEL = 255
M_BOTTOM = 2048
M_BOTTOM_HAT = 10
M_BOTTOM_LEFT_X = 1016
M_BOTTOM_LEFT_Y = 1017
M_BOTTOM_RIGHT_X = 1018
M_BOTTOM_RIGHT_Y = 1019
M_BOTTOM_TILTED = 4175
M_BOTTOM_VIEW = 4169
M_BOUNDING_BOX = 3
M_BOUNDING_BOX_ALGORITHM = 1990
M_BOUNDING_BOX_CLAMP_TO_INLIERS = 1997
M_BOUNDING_BOX_OUTLIER_RATIO_X = 1991
M_BOUNDING_BOX_OUTLIER_RATIO_Y = 1992
M_BOUNDING_BOX_OUTLIER_RATIO_Z = 1993
M_BOUNDING_BOX_SECURITY_FACTOR_X = 1994
M_BOUNDING_BOX_SECURITY_FACTOR_Y = 1995
M_BOUNDING_BOX_SECURITY_FACTOR_Z = 1996
M_BOX = 257
M_BOX_ANGLE = 62464
M_BOX_ANGLE_ACCURACY = 78848
M_BOX_ANGLE_DELTA_NEG = 66560
M_BOX_ANGLE_DELTA_POS = 70656
M_BOX_ANGLE_FOUND = 119808
M_BOX_ANGLE_MODE = 58368
M_BOX_ANGLE_REFERENCE = 152576
M_BOX_ANGLE_TOLERANCE = 74752
M_BOX_AREA = 90
M_BOX_ASPECT_RATIO = 91
M_BOX_CENTER = 46080
M_BOX_CENTER_X = 3445
M_BOX_CENTER_Y = 3446
M_BOX_CENTER_Z = 3447
M_BOX_CORNER_BOTTOM_LEFT = 136192
M_BOX_CORNER_BOTTOM_RIGHT = 140288
M_BOX_CORNER_TOP_LEFT = 128000
M_BOX_CORNER_TOP_RIGHT = 132096
M_BOX_EDGEVALUES = 115712
M_BOX_EDGEVALUES_NUMBER = 144384
M_BOX_FILL_RATIO = 92
M_BOX_MARGIN_BOTTOM = 311
M_BOX_MARGIN_LEFT = 308
M_BOX_MARGIN_RIGHT = 309
M_BOX_MARGIN_TOP = 310
M_BOX_OFFSET_X = 312
M_BOX_OFFSET_Y = 313
M_BOX_ORIENTATION = 3814
M_BOX_ORIGIN = 37888
M_BOX_SIZE = 41984
M_BOX_SIZE_X = 314
M_BOX_SIZE_Y = 315
M_BOX_WIDTH_MARGIN = 2
M_BOX_X_MAX = 8
M_BOX_X_MIN = 6
M_BOX_Y_MAX = 9
M_BOX_Y_MIN = 7
M_BREADTH = 49
M_BRIGHTNESS = 5100
M_BRIGHTNESS_REF = 6657
M_BRIGHT_LABEL = 253
M_BROKEN_CHAR = 104
M_BUFCOPY_SUPPORTED = 2113
M_BUFFER_AGP_CAPABLE = 16387
M_BUFFER_COUNT = 1069
M_BUFFER_DEFAULT_LOCATION = 2310
M_BUFFER_DIRECTX_INFO_PTR = 5092
M_BUFFER_DISPLAY_INFO_PTR = 5093
M_BUFFER_FORMAT_TO_SELECT_DIRECTLY = 10141
M_BUFFER_FREE_ERROR = 26
M_BUFFER_ID = 1441792
M_BUFFER_INDEX = 1769472
M_BUFFER_INFO = 5280
M_BUFFER_INFO_COPY = 5279
M_BUFFER_INFO_OLD = 5028
M_BUFFER_KERNEL_MAP = 16388
M_BUFFER_LIMITS = 4672
M_BUFFER_LIST = 24
M_BUFFER_RELEASE = 1066
M_BUFFER_SAMPLE = 1070
M_BUFFER_TOO_SMALL = 1
M_BUFFER_TYPE_ERROR = 189
M_BUFTRANSFER_METHOD = 15047
M_BUF_ALLOC_BUFFER_TYPES = 138674244
M_BUF_CTRL_INQ_ERROR = 82
M_BUF_DIRECTX_END = 14999
M_BUF_DIRECTX_START = 14000
M_BUF_DISPLAY_END = 9193
M_BUF_DISPLAY_START = 9000
M_BUF_DX_LOCK_UNLOCK_END = 32767
M_BUF_DX_LOCK_UNLOCK_START = 20480
M_BUF_INFO_ALL_VALID_FLAGS = 1
M_BUF_INFO_FLAG_LOCKABLE = 1
M_BUF_INQUIRE_DOUBLE_RANGE_END = 67108864
M_BUF_INQUIRE_DOUBLE_RANGE_START = 33554432
M_BUF_INQUIRE_MIL_ID_END = 1199
M_BUF_INQUIRE_MIL_ID_START = 1100
M_BUF_INQUIRE_SIZEOF_INT64_END = 6799
M_BUF_INQUIRE_SIZEOF_INT64_START = 6700
M_BUF_INQUIRE_STRING_END = 6999
M_BUF_INQUIRE_STRING_START = 6900
M_BUF_INQUIRE_UNKNOWN_SIZEOF_END = 6899
M_BUF_INQUIRE_UNKNOWN_SIZEOF_START = 6800
M_BUF_MODIFIED_HANDLER = 5336
M_BUF_MODIFIED_HOOKED = 1030
M_BUF_MTXDMA_END = 16434
M_BUF_MTXDMA_START = 16384
M_BUF_TRANSFER_ERROR = 76
M_BUF_TRANSFER_ERROR_2 = 89
M_BUF_TRANSFER_ERROR_3 = 95
M_BUF_TRANSFER_ERROR_4 = 99
M_BUF_TRANSFER_ERROR_5 = 181
M_BUF_TRANSPARENT_COLOR = 5098
M_BURST_COUNT = 4
M_BURST_MAX_TIME = 1
M_BURST_TRIGGER = 2
M_BUS_MASTER_COPY_FROM_HOST = 2111
M_BUS_MASTER_COPY_MODE = 1815
M_BUS_MASTER_COPY_TO_HOST = 2110
M_BUS_MASTER_PCI_LOCATION = 2580
M_BUS_MASTER_REQUESTER_ID = 2590
M_BYPASS = 0
M_BYTE_ORDER = 1064
M_BYTE_SWAP = 524288
M_B_FORWARD = 16386
M_B_REVERSE = 16402
M_CACHABLE = 16777216
M_CAD_Y_AXIS = 318
M_CALCULATE = 1
M_CALCULATE_MAP_SIZE_CONTEXT = 3378
M_CALCULATION_TYPE = 2531
M_CALIBRATED = 768
M_CALIBRATED_CAMERA_LINEAR_MOTION = 1
M_CALIBRATED_XYZ = 51
M_CALIBRATED_XYZ_UNORGANIZED = 52
M_CALIBRATED_XZ_EXTERNAL_Y = 54
M_CALIBRATED_XZ_UNIFORM_Y = 53
M_CALIBRATED_Z = 55
M_CALIBRATED_Z_EXTERNAL_Y = 56
M_CALIBRATED_Z_UNIFORM_XY = 57
M_CALIBRATED_Z_UNIFORM_X_EXTERNAL_Y = 58
M_CALIBRATING = 6
M_CALIBRATION = 1770
M_CALIBRATION_CATEGORY = 214
M_CALIBRATION_CHILD_OFFSET_X = 141
M_CALIBRATION_CHILD_OFFSET_Y = 142
M_CALIBRATION_COMPUTE_OPTION = 1878
M_CALIBRATION_CONTEXT_PRESENT = 1401
M_CALIBRATION_DEPTHS = 1314
M_CALIBRATION_ID = 4
M_CALIBRATION_IMAGE_POINTS_X = 201
M_CALIBRATION_IMAGE_POINTS_Y = 202
M_CALIBRATION_INPUT_DATA = 1851
M_CALIBRATION_INTENT = 1874
M_CALIBRATION_MODE = 205
M_CALIBRATION_PLANE = 160
M_CALIBRATION_PRESENT = 1400
M_CALIBRATION_PROPAGATE_AT_EACH_FRAME = 4
M_CALIBRATION_PROPAGATE_OFF = 8
M_CALIBRATION_PROPAGATE_ONCE = 0
M_CALIBRATION_STATUS = 159
M_CALIBRATION_STATUS_MODIFIED = 2060
M_CALIBRATION_STREAM_SIZE = 0
M_CALIBRATION_STREAM_SIZE_WITH_CONTEXT = 1405
M_CALIBRATION_STREAM_WITH_CONTEXT = 1406
M_CALIBRATION_TRANSLATIONS = 6
M_CALIBRATION_WORLD_POINTS_X = 203
M_CALIBRATION_WORLD_POINTS_Y = 204
M_CALIBRATION_WORLD_POINTS_Z = 213
M_CALLER_BITNESS = 165
M_CALLER_WORKSPACE = 210
M_CALL_CONTEXT = 33554432
M_CALL_CONTEXT_ERROR = 39
M_CALL_FPGA_PARAM_ERROR = 83
M_CALL_HOOKS = 1034
M_CAL_CONTEXT = 541065217
M_CAL_DRAW_3D_CONTEXT = 541065224
M_CAL_FIXTURING_OFFSET = 541065220
M_CAL_OBJECT = 541065216
M_CAL_PARENT_OFFSETS = 11
M_CAMERA = 4294967296
M_CAMERALINK_CC1_SOURCE = 5200
M_CAMERALINK_CC2_SOURCE = 5201
M_CAMERALINK_CC3_SOURCE = 5202
M_CAMERALINK_CC4_SOURCE = 5203
M_CAMERA_COLOR_LOCK = 5301
M_CAMERA_COLOR_LOCKED = 5305
M_CAMERA_COORDINATE_SYSTEM = 2
M_CAMERA_HOOK = 0
M_CAMERA_IMAGE_SIZE_X = 1303
M_CAMERA_IMAGE_SIZE_Y = 1304
M_CAMERA_LABEL_FLAG = 536870912
M_CAMERA_LABEL_VALUE = 1872
M_CAMERA_LOCK = 5300
M_CAMERA_LOCKED = 5304
M_CAMERA_LOCK_HANDLER_PTR = 5307
M_CAMERA_LOCK_HANDLER_USER_PTR = 5308
M_CAMERA_LOCK_MODE = 5306
M_CAMERA_LOCK_SENSITIVITY = 5302
M_CAMERA_LOCK_THREAD_HANDLE = 5310
M_CAMERA_LOCK_THREAD_ID = 5309
M_CAMERA_MODEL = 7711
M_CAMERA_MODEL_LENGTH = 5497558146591
M_CAMERA_OFFSET = 3
M_CAMERA_POWER = 2560
M_CAMERA_PRESENT = 5315
M_CAMERA_PRESENT_HANDLER_PTR = 5311
M_CAMERA_PRESENT_HANDLER_USER_PTR = 5312
M_CAMERA_PRESENT_SENSITIVITY = 5316
M_CAMERA_PRESENT_THREAD_HANDLE = 5314
M_CAMERA_PRESENT_THREAD_ID = 5313
M_CAMERA_TILT_X = 5375
M_CAMERA_TIME_STAMP = 33554451
M_CAMERA_TIME_STAMP_NS = 6773
M_CAMERA_UNLOCK_SENSITIVITY = 5303
M_CAMERA_VENDOR = 7704
M_CAMERA_VENDOR_ID = 5194
M_CAMERA_VENDOR_LENGTH = 5497558146584
M_CANCEL = 1767
M_CAN_ALLOCATE_CONTIGUOUS_VIDEO_MEMORY = 4595
M_CAN_ALLOCATE_MONO8_IN_VIDEO_MEMORY = 4576
M_CAN_ALLOCATE_VIDEO_MEMORY = 4557
M_CAN_ALLOC_MTX0 = 15375
M_CAN_ALLOC_NON_PAGED_IN_VIDEO_MEMORY = 15346
M_CAN_DO_HARDWARE_COMPOSITION = 10040
M_CAN_GRAB = 4441
M_CAN_GROW_RECT = 256
M_CAPABILITY = 8202
M_CAPTURE_LEVEL_FRAME_END = 4524
M_CAPTURE_QUALITY = 5164
M_CAPTURE_RAW_DATA = 1580
M_CAPTURE_SIZE = 5160
M_CARTESIAN = 2717
M_CBCR = 16384
M_CC1 = 256
M_CC2 = 257
M_CC3 = 258
M_CC4 = 259
M_CCD_ASPECT_RATIO = 148
M_CCIR = 3
M_CC_IO = 256
M_CC_IO1 = 256
M_CC_IO2 = 257
M_CC_IO3 = 258
M_CC_IO4 = 259
M_CC_IO_COUNT = 4453
M_CC_IO_COUNT_IN = 4454
M_CC_IO_COUNT_OUT = 4455
M_CC_OUTPUT_A = 43
M_CC_OUTPUT_B = 44
M_CELL_CONTRAST = 41029
M_CELL_CONTRAST_GRADE = 36934
M_CELL_DEFECTS = 41047
M_CELL_HEIGHT = 41043
M_CELL_MODULATION_GRADE = 36935
M_CELL_NUMBER_X = 32768
M_CELL_NUMBER_X_MAX = 32786
M_CELL_NUMBER_X_MIN = 32784
M_CELL_NUMBER_Y = 32769
M_CELL_NUMBER_Y_MAX = 32787
M_CELL_NUMBER_Y_MIN = 32785
M_CELL_SIZE = 4096
M_CELL_SIZE_INPUT_UNITS = 32842
M_CELL_SIZE_MAX = 16384
M_CELL_SIZE_MIN = 8192
M_CELL_SIZE_MODE = 3408
M_CELL_SIZE_VALUE = 2998
M_CELL_WIDTH = 41042
M_CENTER = 128
M_CENTERED = 65536
M_CENTERED_WINDOW = 8388672
M_CENTER_AND_DIMENSION = 2
M_CENTER_AND_TWO_POINTS = 3875
M_CENTER_AND_TWO_VECTORS = 3876
M_CENTER_DISPLAY = 10019
M_CENTER_ELEMENT = 1073741824
M_CENTER_FRAME = 1073741826
M_CENTER_OBJECT = 268435456
M_CENTER_OF_GRAVITY = 259
M_CENTER_OF_GRAVITY_X = 34
M_CENTER_OF_GRAVITY_Y = 35
M_CENTER_X = 4
M_CENTER_Y = 5
M_CENTER_Z = 3400
M_CENTIMETERS = 2451
M_CENTRAL = 2048
M_CENTROID = 1956
M_CENTROID_X = 3451
M_CENTROID_Y = 3452
M_CENTROID_Z = 3453
M_CERTAINTY = 202
M_CERTAINTY_TARGET = 203
M_CH0 = 1073741824
M_CH0_REF = 1073741824
M_CH1 = 536870912
M_CH10 = 524288
M_CH11 = 262144
M_CH12 = 131072
M_CH13 = 65536
M_CH14 = 32768
M_CH15 = 16384
M_CH1_REF = 536870912
M_CH2 = 134217728
M_CH2_REF = 134217728
M_CH3 = 16777216
M_CH3_REF = 16777216
M_CH4 = 33554432
M_CH4_REF = 33554432
M_CH5 = 67108864
M_CH5_REF = 67108864
M_CH6 = 8388608
M_CH6_REF = 8388608
M_CH7 = 4194304
M_CH7_REF = 4194304
M_CH8 = 2097152
M_CH9 = 1048576
M_CHAIN = 209
M_CHAINS = 209
M_CHAIN_ALL_NEIGHBORS = 888
M_CHAIN_ANGLE = 258
M_CHAIN_APPROXIMATION = 66048
M_CHAIN_CODE = 58
M_CHAIN_INDEX = 67
M_CHAIN_MAGNITUDE = 36
M_CHAIN_X = 65
M_CHAIN_Y = 144
M_CHAMFER_3_4 = 1
M_CHANGE = 99
M_CHANGE_ID_IN_CAL_STREAM = 6
M_CHANNEL = 4000
M_CHANNEL_COLOR = 1
M_CHANNEL_NUM = 4001
M_CHANNEL_SIGNAL = 8096
M_CHANNEL_SYNC = 12192
M_CHARACTER_PAT_MODEL = 65536
M_CHAR_ACCEPTANCE = 25
M_CHAR_ADD = 1
M_CHAR_ANGLE = 794
M_CHAR_ASPECT_RATIO = 787
M_CHAR_ASPECT_RATIO_MAX_FACTOR = 512
M_CHAR_ASPECT_RATIO_MIN_FACTOR = 511
M_CHAR_BASELINE = 4
M_CHAR_BASELINE_DEVIATION = 912
M_CHAR_BASELINE_VALUE = 5
M_CHAR_BOX_BL_X = 928
M_CHAR_BOX_BL_Y = 929
M_CHAR_BOX_BR_X = 926
M_CHAR_BOX_BR_Y = 927
M_CHAR_BOX_SIZE_X = 33
M_CHAR_BOX_SIZE_Y = 34
M_CHAR_BOX_UL_X = 922
M_CHAR_BOX_UL_Y = 923
M_CHAR_BOX_UR_X = 924
M_CHAR_BOX_UR_Y = 925
M_CHAR_CELL_SIZE_X = 33
M_CHAR_CELL_SIZE_Y = 34
M_CHAR_CONSECUTIVE_SPACE = 791
M_CHAR_DELETE = 2
M_CHAR_ERASE = 45
M_CHAR_FONT = 785
M_CHAR_FONT_INDEX = 2279
M_CHAR_FONT_LABEL = 2280
M_CHAR_FONT_USER_LABEL = 229
M_CHAR_HEIGHT = 2312
M_CHAR_HOMOGENEITY_ACCEPTANCE = 27
M_CHAR_HOMOGENEITY_SCORE = 788
M_CHAR_INDEX = 790
M_CHAR_INDEX_VALUE = 2224
M_CHAR_INVALID = 26
M_CHAR_IN_FONT = 42
M_CHAR_LIST = 2281
M_CHAR_MAX_BASELINE_DEVIATION = 513
M_CHAR_MAX_OFFSET_X = 11
M_CHAR_MAX_OFFSET_Y = 13
M_CHAR_MIN_OFFSET_X = 10
M_CHAR_MIN_OFFSET_Y = 12
M_CHAR_M_HEIGHT = 804
M_CHAR_M_THICKNESS = 821
M_CHAR_M_WIDTH = 803
M_CHAR_NAME = 2212
M_CHAR_NORMALIZE = 3
M_CHAR_NORMAL_SIZE_X = 110
M_CHAR_NORMAL_SIZE_Y = 111
M_CHAR_NUMBER = 32
M_CHAR_NUMBER_IN_FONT = 47
M_CHAR_OFFSET_X = 35
M_CHAR_OFFSET_Y = 36
M_CHAR_POSITION_TOLERANCE_X = 91
M_CHAR_POSITION_TOLERANCE_Y = 92
M_CHAR_POSITION_VARIATION_X = 91
M_CHAR_POSITION_VARIATION_Y = 92
M_CHAR_POSITION_X = 6
M_CHAR_POSITION_Y = 7
M_CHAR_SCALE = 786
M_CHAR_SCALE_MAX_FACTOR = 510
M_CHAR_SCALE_MIN_FACTOR = 509
M_CHAR_SCORE = 5
M_CHAR_SIMILARITY_ACCEPTANCE = 26
M_CHAR_SIMILARITY_SCORE = 789
M_CHAR_SIZE_SCORE = 9
M_CHAR_SIZE_X = 37
M_CHAR_SIZE_Y = 38
M_CHAR_SORT = 5
M_CHAR_SPACING = 14
M_CHAR_STATUS = 970
M_CHAR_TEMPLATE = 2223
M_CHAR_THICKNESS = 39
M_CHAR_TYPE = 816
M_CHAR_TYPE_VALUE = 820
M_CHAR_VALID_FLAG = 4
M_CHAR_VALUE = 815
M_CHAR_WIDTH = 2311
M_CHAR_WIDTH_FACTOR = 2387
M_CHECK_DISABLE = 2
M_CHECK_ENABLE = 3
M_CHECK_ERROR = 4606
M_CHECK_FINDER_PATTERN = 32780
M_CHECK_QUIET_ZONE = 32796
M_CHECK_VALID = 3
M_CHECK_VALID_FAST = 4
M_CHESSBOARD = 4
M_CHESSBOARD_GRID = 2
M_CHILDREN = 4685
M_CHILDREN_ONLY = 524288
M_CHILD_ALLOC_LOSABLE_ATTRIBUTE = 576478899613990912
M_CHILD_BUFFER_MOVED = 4194304
M_CHILD_ERROR = 9
M_CHILD_ERROR_2 = 56204
M_CHROMINANCE = 262144
M_CIE94_GRAPHIC_ARTS = 1471
M_CIE94_GRAPHIC_ARTS_SQR = 1476
M_CIE94_TEXTILE = 1472
M_CIE94_TEXTILE_SQR = 1477
M_CIEDE2000 = 1473
M_CIEDE2000_SQR = 1478
M_CIEDE94_GRAPHIC_ARTS = 1471
M_CIEDE94_GRAPHIC_ARTS_SQR = 1476
M_CIEDE94_TEXTILE = 1472
M_CIEDE94_TEXTILE_SQR = 1477
M_CIELAB = 41
M_CIELCH = 1468
M_CIRCLE = 8
M_CIRCLE_ACCURACY = 197632
M_CIRCLE_ASPECT_RATIO = 8216
M_CIRCLE_CENTER_X = 13312
M_CIRCLE_CENTER_Y = 17408
M_CIRCLE_FIT = 25
M_CIRCLE_FIT_CENTER_X = 41
M_CIRCLE_FIT_CENTER_Y = 42
M_CIRCLE_FIT_COVERAGE = 48
M_CIRCLE_FIT_ERROR = 47
M_CIRCLE_FIT_RADIUS = 43
M_CIRCLE_GRID = 1
M_CIRCLE_INSIDE_SEARCH_REGION = 1718
M_CIRCLE_OF_CONFUSION_RADIUS_MAX = 1906
M_CIRCULAR = 1
M_CIRCULAR_OVERSCAN = 65536
M_CITY_BLOCK = 2
M_CL = 2048
M_CLARITY_UHD = 250
M_CLARITY_UHD_H264 = 512
M_CLASSIFICATION_MAP = 2861
M_CLASSIFICATION_MAP_INPUT_SIZE_X = 2871
M_CLASSIFICATION_MAP_INPUT_SIZE_Y = 2872
M_CLASSIFICATION_MAP_OFFSET_X = 3334
M_CLASSIFICATION_MAP_OFFSET_Y = 3335
M_CLASSIFICATION_MAP_SCALE_X = 3332
M_CLASSIFICATION_MAP_SCALE_Y = 3333
M_CLASSIFICATION_MAP_SIZE = 8192
M_CLASSIFICATION_MAP_SIZE_X = 2862
M_CLASSIFICATION_MAP_SIZE_Y = 2863
M_CLASSIFIER_CNN = 2779
M_CLASSIFIER_CNN_PREDEFINED = 2913
M_CLASSIFIER_CNN_PREDEFINED_TYPE = 3978
M_CLASSIFIER_STATUS = 3781
M_CLASSIFIER_TREE_ENSEMBLE = 3265
M_CLASS_ADD = 3740
M_CLASS_CLASSIFIER_CNN_CONTEXT = 275414810625
M_CLASS_CLASSIFIER_CNN_PREDEFINED_CONTEXT = 275414810626
M_CLASS_CLASSIFIER_TREE_ENSEMBLE_CONTEXT = 275414810627
M_CLASS_CNN_EPOCH_HOOK_INFO = 275414777866
M_CLASS_CNN_MINI_BATCH_HOOK_INFO = 275414777867
M_CLASS_CNN_PREDICT_ENTRY_HOOK_INFO = 275414777868
M_CLASS_DATASET_FEATURES = 275414810633
M_CLASS_DATASET_IMAGES = 275414810632
M_CLASS_DEFINITIONS = 3476
M_CLASS_DEF_INDEX_FLAG = 2097152
M_CLASS_DEF_UUID = 3298
M_CLASS_DELETE = 3741
M_CLASS_DELETE_BY_KEY = 3742
M_CLASS_DRAW_COLOR = 3319
M_CLASS_ICON_ID = 2907
M_CLASS_INDEX_GROUND_TRUTH = 3478
M_CLASS_INDEX_PREDICTED = 3738
M_CLASS_KEY = 3574
M_CLASS_MAP_INDEX_IMAGE_TYPE = 3355
M_CLASS_NAME = 3297
M_CLASS_OBJECT = 275414777856
M_CLASS_OBJECT_SAVABLE = 275414810624
M_CLASS_PREDICT_CNN_RESULT = 275414777888
M_CLASS_PREDICT_TREE_ENSEMBLE_RESULT = 275414777862
M_CLASS_SCORES = 2837
M_CLASS_TRAIN_CNN_CONTEXT = 275414810628
M_CLASS_TRAIN_CNN_RESULT = 275414777920
M_CLASS_TRAIN_TREE_ENSEMBLE_CONTEXT = 275414810629
M_CLASS_TRAIN_TREE_ENSEMBLE_RESULT = 275414777863
M_CLASS_TREE_ENSEMBLE_PREDICT_ENTRY_HOOK_INFO = 275414777870
M_CLASS_TREE_ENSEMBLE_TREE_HOOK_INFO = 275414777869
M_CLASS_WEIGHT = 3612
M_CLASS_WEIGHT_MODE = 3529
M_CLEAR = 1
M_CLEAR_BACKGROUND = 8192
M_CLEAR_DATA = 1340
M_CLEAR_DESTINATIONS = 4615
M_CLEAR_ERROR = 15003
M_CLHS = 1024
M_CLIENT_ASCII_ENCODING = 281474976710656
M_CLIENT_ASCII_MODE = 0
M_CLIENT_ENCODING = 0
M_CLIENT_ERROR_ASCII_MODE = 256
M_CLIENT_TEXT_ENCODING = 281474976710656
M_CLIP = 16
M_CLIPPED_OFFSET_X = 1
M_CLIPPED_OFFSET_Y = 2
M_CLIPPED_SIZE_X = 4
M_CLIPPED_SIZE_Y = 8
M_CLIPPING_BOX = 3868
M_CLIP_CENTER = 106
M_CLIP_DST_SUPPORTED = 4063
M_CLIP_LIMIT = 252
M_CLIP_SRC_SUPPORTED = 4062
M_CLOCK = 85
M_CLOCKWISE_PHASE = 65536
M_CLOCK_FREQUENCY = 7301
M_CLOCK_FREQUENCY_FPGA = 7330
M_CLOCK_NOT_ALWAYS_VALID = 4140
M_CLONE_ANGLE = 118
M_CLONE_CONSTRAINTS_FROM = 2285
M_CLONE_FEATURE = 131072
M_CLONE_OFFSET_X = 115
M_CLONE_OFFSET_Y = 116
M_CLONE_PERMITTED_CHARS_FROM = 2296
M_CLONE_SCALE = 117
M_CLOSE = 32
M_CLOSEST = 37
M_CLOSEST_POINT = 12
M_CLOSEST_POINT_MAX_DISTANCE = 176
M_CLOSEST_TEMPLATE = 11
M_CLOSEST_TO_INFINITE_POINT = 2601
M_CLOSEST_TO_ORIGIN_X = 3540
M_CLOSEST_TO_ORIGIN_Y = 3541
M_CLOSEST_TO_ORIGIN_Z = 3542
M_CLOSEST_TO_POINT = 3171
M_CLOSE_FROM_DLL = 64
M_CLOSURE = 77
M_CLUSTER_MASK = 16528
M_CLUSTER_NODE_FROM_ID = 15726
M_CLUSTER_NODE_MASK = 2130706432
M_CLUSTER_NODE_SHIFT = 24
M_CLUSTER_SERVER_NAME = 16848
M_CMC_ACCEPTABILITY = 1470
M_CMC_ACCEPTABILITY_SQR = 1475
M_CMC_PERCEPTIBILITY = 1469
M_CMC_PERCEPTIBILITY_SQR = 1474
M_CNN_TRAIN_ENGINE = 3426
M_CNN_TRAIN_ENGINE_IS_INSTALLED = 3768
M_CNN_TRAIN_ENGINE_USED = 3800
M_CNN_TRAIN_ENGINE_USED_DESCRIPTION = 6272
M_COARSE_SEARCH_ACCEPTANCE = 41
M_CODABAR = 128
M_CODABAR_NAME = MIL_TEXT("Codabar")
M_CODE128 = 32
M_CODE128_NAME = MIL_TEXT("Code128")
M_CODE39 = 1
M_CODE39_NAME = MIL_TEXT("Code39")
M_CODE93 = 134217728
M_CODE93_NAME = MIL_TEXT("Code93")
M_CODEC_ENGINE_ERROR_END = 52999
M_CODEC_ENGINE_ERROR_START = 52000
M_CODEC_ENGINE_SERVICE_ERROR = 143
M_CODEC_TYPE = 1540
M_CODESTREAM_FORMAT = 8210
M_CODESTREAM_OFFSET = 8223
M_CODESTREAM_SIZE = 8224
M_CODEWORD_DECODABILITY = 41025
M_CODEWORD_DECODABILITY_GRADE = 36929
M_CODEWORD_DEFECTS = 41026
M_CODEWORD_DEFECTS_GRADE = 36930
M_CODEWORD_MODULATION = 41027
M_CODEWORD_MODULATION_GRADE = 36931
M_CODEWORD_REFLECTANCE_MARGIN = 41031
M_CODEWORD_REFLECTANCE_MARGIN_GRADE = 36939
M_CODEWORD_YIELD = 41024
M_CODEWORD_YIELD_GRADE = 36928
M_CODE_BLOCK_SIZE_X = 2566
M_CODE_BLOCK_SIZE_Y = 2600
M_CODE_CONTEXT = 545259521
M_CODE_DEFORMED = 1
M_CODE_DETECT_RESULT = 545259536
M_CODE_FLIP = 1413
M_CODE_GRADE_A = 4
M_CODE_GRADE_B = 3
M_CODE_GRADE_C = 2
M_CODE_GRADE_D = 1
M_CODE_GRADE_F = 0
M_CODE_GRADE_NOT_AVAILABLE = 5
M_CODE_GRADE_NOT_COMPUTABLE = -1
M_CODE_GRADE_RESULT = 545259522
M_CODE_MODEL = 545259524
M_CODE_MODEL_ID = 5064
M_CODE_MODEL_INDEX = 5066
M_CODE_MODEL_NUMBER_OF_OCCURRENCES = 2585
M_CODE_NOT_DEFORMED = 0
M_CODE_OBJECT = 545259520
M_CODE_READ_RESULT = 545259552
M_CODE_RESULT_ID = 2583
M_CODE_SEARCH_MODE = 2731
M_CODE_TRAIN_RESULT = 545259528
M_CODE_TYPE = 1
M_CODE_TYPE_NAME = 2711
M_CODE_WRITE_RESULT = 545259584
M_COEFFICIENTS = 3388
M_COEFFICIENT_A = 3401
M_COEFFICIENT_B = 3402
M_COEFFICIENT_C = 3403
M_COEFFICIENT_D = 3404
M_COILS = MIL_TEXT("M_COILS")
M_COLOR = 256
M_COLORED_LABEL_AREA_IMAGE_SIGN = 384
M_COLORED_LABEL_AREA_IMAGE_SIZE_BAND = 383
M_COLORED_LABEL_AREA_IMAGE_SIZE_BIT = 382
M_COLORED_LABEL_AREA_IMAGE_SIZE_X = 380
M_COLORED_LABEL_AREA_IMAGE_SIZE_Y = 381
M_COLORED_LABEL_AREA_IMAGE_TYPE = 385
M_COLORED_LABEL_PIXEL_IMAGE_SIGN = 364
M_COLORED_LABEL_PIXEL_IMAGE_SIZE_BAND = 363
M_COLORED_LABEL_PIXEL_IMAGE_SIZE_BIT = 362
M_COLORED_LABEL_PIXEL_IMAGE_SIZE_X = 360
M_COLORED_LABEL_PIXEL_IMAGE_SIZE_Y = 361
M_COLORED_LABEL_PIXEL_IMAGE_TYPE = 365
M_COLORMAP_DISTINCT_256 = 8388628
M_COLORMAP_HOT = 8388621
M_COLORMAP_HOT_OLD = 8
M_COLORMAP_HUE = 8388622
M_COLORMAP_HUE_OLD = 9
M_COLORMAP_JET = 8388620
M_COLORMAP_JET_OLD = 7
M_COLORMAP_MASK = -24577
M_COLORMAP_SPECTRUM = 8388623
M_COLORMAP_SPECTRUM_OLD = 10
M_COLORMAP_TURBO = 8388624
M_COLOR_AXIS_X = 4689
M_COLOR_AXIS_Y = 4690
M_COLOR_AXIS_Z = 4691
M_COLOR_BAND_0 = 256
M_COLOR_BAND_1 = 512
M_COLOR_BAND_2 = 1024
M_COLOR_BLACK = 1073741824
M_COLOR_BLUE = 1090453504
M_COLOR_BRIGHT_GRAY = 1086374080
M_COLOR_BUFFERS_PROCESSING_SUPPORT = 4377
M_COLOR_CALIBRATION_COMPUTE_OPTION = 1878
M_COLOR_CALIBRATION_RELATIVE = 1024
M_COLOR_COMPONENT = 4678
M_COLOR_COMPONENT_BAND = 4683
M_COLOR_CONVERSION_COEFFICIENTS = 4009754624
M_COLOR_CONVERSION_COEFFICIENTS_MASK = 4294901760
M_COLOR_CORRECTION = 1024
M_COLOR_CYAN = 1090518784
M_COLOR_DARK_BLUE = 1082130432
M_COLOR_DARK_CYAN = 1082163200
M_COLOR_DARK_GREEN = 1073774592
M_COLOR_DARK_MAGENTA = 1082130560
M_COLOR_DARK_RED = 1073741952
M_COLOR_DARK_YELLOW = 1073774720
M_COLOR_DISTANCE = 806
M_COLOR_GRAY = 1082163328
M_COLOR_GREEN = 1073807104
M_COLOR_ITEM_TAG = 67108864
M_COLOR_LIGHT_BLUE = 1089522342
M_COLOR_LIGHT_GRAY = 1084530848
M_COLOR_LIGHT_GREEN = 1086381248
M_COLOR_LIGHT_WHITE = 1089534975
M_COLOR_LIMITS = 4680
M_COLOR_LIMITS_MAX = 4730
M_COLOR_LIMITS_MIN = 4729
M_COLOR_LUT = 3945
M_COLOR_LUT_SIZE = 4681
M_COLOR_LUT_SIZE_BAND = 4682
M_COLOR_MAGENTA = 1090453759
M_COLOR_MATCH = 4194304
M_COLOR_MATCHING = 256
M_COLOR_MATCHING_RESULT = 4096
M_COLOR_MODE = 1018
M_COLOR_PROJECTION = 512
M_COLOR_RED = 1073742079
M_COLOR_SEPARATION = 600
M_COLOR_SPACE = 230
M_COLOR_TEXTURE = 4697
M_COLOR_TEXTURE_SIZE_BAND = 4696
M_COLOR_TEXTURE_SIZE_X = 4694
M_COLOR_TEXTURE_SIZE_Y = 4695
M_COLOR_TO_COLOR = 1479
M_COLOR_USE_LUT = 4684
M_COLOR_USE_TEXTURE = 4693
M_COLOR_WHITE = 1090519039
M_COLOR_YELLOW = 1073807359
M_COLUMN_NUMBER = 117
M_COLUMN_SPACING = 119
M_COL_MATCH_CONTEXT = 9126805505
M_COL_MATCH_RESULT = 9126805512
M_COL_OBJECT = 9126805504
M_COL_PROJECT_CONTEXT = 9126805508
M_COL_RELATIVE_CALIBRATION_CONTEXT = 9126805520
M_COL_SPACE_DEF_CONTEXT = 9126805506
M_COM = 2
M_COMBINATION_KEYS = 7
M_COMMAND_DECODER_ERROR = 29
M_COMMAND_QUEUE_MODE = 4775
M_COMMON_DIRECTX_VIDEO_DEVICE_ID = 10208
M_COMMON_VGA_INDEX = 10208
M_COMPACTNESS = 25
M_COMPACT_PCI_PRESENT = 2123
M_COMPARE_CALIBRATION_INFO = 7
M_COMPARE_CALIBRATION_INFO_NO_OFFSET = 8
M_COMPENSATE = 3713
M_COMPENSATED_REAL_ID = 22
M_COMPENSATION_DISABLE = 4
M_COMPENSATION_ENABLE = 5
M_COMPENSATION_ERROR = 136
M_COMPILE = 250
M_COMPLETE = 0
M_COMPLETE_TYPE = 2147483647
M_COMPLETION_MODE = 12288
M_COMPLEX = 1968
M_COMPLEX_SURFACE_MASK = 7696581394432
M_COMPLEX_SURFACE_OFFSET = 40
M_COMPONENT_ADD = 262144
M_COMPONENT_ALL = 17592186044416
M_COMPONENT_BY_GROUP_ID_FLAG = 3458764513820540928
M_COMPONENT_BY_ID_FLAG = 2305843009213693952
M_COMPONENT_BY_INDEX_FLAG = 1152921504606846976
M_COMPONENT_BY_MASK = 8646911284551352320
M_COMPONENT_BY_REGION_ID_FLAG = 4611686018427387904
M_COMPONENT_BY_SOURCE_ID_FLAG = 5764607523034234880
M_COMPONENT_CONFIDENCE = 6
M_COMPONENT_COUNT = 17
M_COMPONENT_CUSTOM = 65280
M_COMPONENT_DISPARITY = 8
M_COMPONENT_GROUP_ID = 6769
M_COMPONENT_GROUP_ID_LIST = 2097152
M_COMPONENT_ID = 1195
M_COMPONENT_ID_LIST = 1048576
M_COMPONENT_INFRARED = 2
M_COMPONENT_INTENSITY = 1
M_COMPONENT_INVALID = 1087
M_COMPONENT_LIST = 1048576
M_COMPONENT_MESH_MIL = 16777217
M_COMPONENT_METADATA = 32769
M_COMPONENT_METADATA_DA = 16777219
M_COMPONENT_MULTISPECTRAL = 9
M_COMPONENT_NORMALS_MIL = 16777218
M_COMPONENT_RANGE = 4
M_COMPONENT_REFLECTANCE = 5
M_COMPONENT_REGION_ID = 6771
M_COMPONENT_REGION_ID_LIST = 6291456
M_COMPONENT_REGION_NAME = 6904
M_COMPONENT_REGION_OFFSET_X = 5302
M_COMPONENT_REGION_OFFSET_Y = 5303
M_COMPONENT_REMOVE = 2058
M_COMPONENT_RESELECT_DISABLE = 12
M_COMPONENT_RESELECT_ENABLE = 13
M_COMPONENT_SCATTER = 7
M_COMPONENT_SOURCE_ID = 6770
M_COMPONENT_SOURCE_ID_LIST = 12582912
M_COMPONENT_SOURCE_NAME = 6905
M_COMPONENT_TIME_STAMP = 33554433
M_COMPONENT_TIME_STAMP_IS_PTP = 5113
M_COMPONENT_TIME_STAMP_NS = 6774
M_COMPONENT_TYPE = 6768
M_COMPONENT_TYPE_LIST = 8388608
M_COMPONENT_TYPE_NAME = 6902
M_COMPONENT_ULTRAVIOLET = 3
M_COMPONENT_UNDEFINED = 0
M_COMPOSE_TWO_MATRICES = 3766
M_COMPOSE_WITH_CURRENT = 512
M_COMPOSITE = 1
M_COMPOSITECODE = 16777216
M_COMPOSITECODE_NAME = MIL_TEXT("CompositeCode")
M_COMPOSITION = 4096
M_COMPOSITION_ERROR = 100
M_COMPRESS = 16384
M_COMPRESSED_DATA = 1
M_COMPRESSED_DATA_SIZE_BYTE = 8209
M_COMPRESSED_DISPLAY_SURFACE = 1125
M_COMPRESSION = 524288
M_COMPRESSION_ADOBE_DEFLATE = 8
M_COMPRESSION_BOARD_RESET = 2122
M_COMPRESSION_BOARD_TYPE = 2121
M_COMPRESSION_CCITTFAX3 = 3
M_COMPRESSION_CCITTFAX4 = 4
M_COMPRESSION_CCITTRLE = 2
M_COMPRESSION_CCITTRLEW = 32771
M_COMPRESSION_DCS = 32947
M_COMPRESSION_DEFLATE = 32946
M_COMPRESSION_FORMAT_MASK = 146833408
M_COMPRESSION_INTERNAL_BUFFER_SIZE = 2139
M_COMPRESSION_IT8BL = 32898
M_COMPRESSION_IT8CTPAD = 32895
M_COMPRESSION_IT8LW = 32896
M_COMPRESSION_IT8MP = 32897
M_COMPRESSION_JBIG = 34661
M_COMPRESSION_JP2000 = 34712
M_COMPRESSION_JPEG = 7
M_COMPRESSION_LZW = 5
M_COMPRESSION_MODULE_PRESENT = 2104
M_COMPRESSION_NEXT = 32766
M_COMPRESSION_NONE = 1
M_COMPRESSION_OJPEG = 6
M_COMPRESSION_PACKBITS = 32773
M_COMPRESSION_PIXARFILM = 32908
M_COMPRESSION_PIXARLOG = 32909
M_COMPRESSION_PLATFORM = 8202
M_COMPRESSION_SGILOG = 34676
M_COMPRESSION_SGILOG24 = 34677
M_COMPRESSION_SUPPORTED = 2114
M_COMPRESSION_THUNDERSCAN = 32809
M_COMPRESSION_TYPE = 5045
M_COMPRESS_ERROR = 16
M_COMPUTATION_DIRECTION = 3587
M_COMPUTE = 1
M_COMPUTE_CONFUSION_MATRIX = 2
M_COMPUTE_ITEM_PIXELS = 1492
M_COMPUTE_ITEM_STAT = 1491
M_COMPUTE_OUT_OF_BAG_RESULTS = 3527
M_COMPUTE_PROXIMITY_MATRIX = 3513
M_COMP_DISP_RESELECT = 15533
M_COMP_POS_RES_LAYER = 4
M_COM_ABORT = 12
M_COM_CCLINK_FLAGS_MEMORY_BANK = 2
M_COM_CCLINK_FORCE_READ_INPUT = 1
M_COM_CCLINK_INPUT_FLAG = MIL_TEXT("RX")
M_COM_CCLINK_INPUT_FLAGS_MEMORY_BANK = 3
M_COM_CCLINK_INPUT_REGISTER = MIL_TEXT("RWR")
M_COM_CCLINK_INPUT_REGISTERS_MEMORY_BANK = 5
M_COM_CCLINK_OUTPUT_FLAG = MIL_TEXT("RY")
M_COM_CCLINK_OUTPUT_FLAGS_MEMORY_BANK = 2
M_COM_CCLINK_OUTPUT_REGISTER = MIL_TEXT("RWW")
M_COM_CCLINK_OUTPUT_REGISTERS_MEMORY_BANK = 4
M_COM_CCLINK_RAW = MIL_TEXT("RAW")
M_COM_CCLINK_REGISTERS_MEMORY_BANK = 4
M_COM_CCLINK_START = 1000
M_COM_CCLINK_TOTAL_OCCUPIED_STATION = 1001
M_COM_CONTEXT = 69256347649
M_COM_DATA_CHANGE = 5
M_COM_DEVICE_DESCRIPTION = 17
M_COM_DEVICE_DESCRIPTION_SIZE = 5497558138897
M_COM_EMULATION = 8
M_COM_EMULATION_MODE = 20
M_COM_EMULATOR_SYNC = 21
M_COM_ERROR = 1
M_COM_ERROR_NUMBER = 56
M_COM_ERROR_TRIGGER = 4
M_COM_ERR_OFFSET = 47000
M_COM_ETHERNETIP_ASSEMBLY_LIST = 20004
M_COM_ETHERNETIP_CONFIG = MIL_TEXT("112")
M_COM_ETHERNETIP_CONFIG_ID = 112
M_COM_ETHERNETIP_CONFIG_SIZE = 20003
M_COM_ETHERNETIP_CONSUMER = MIL_TEXT("111")
M_COM_ETHERNETIP_CONSUMER_ID = 111
M_COM_ETHERNETIP_CONSUMER_SIZE = 20001
M_COM_ETHERNETIP_PRODUCER = MIL_TEXT("110")
M_COM_ETHERNETIP_PRODUCER_ID = 110
M_COM_ETHERNETIP_PRODUCER_SIZE = 20002
M_COM_ETHERNETIP_START = 20000
M_COM_EVENT_ID = 59
M_COM_FIND_POSITION_REQUEST = 1
M_COM_GET_CONNECTION_STATE = 14
M_COM_GET_HOOK_INFO_SIZE = -9223372036854775808
M_COM_HOOK_ID = 9
M_COM_ID = 99
M_COM_INIT_VALUE = 19
M_COM_INSTANCE_NAME = 22
M_COM_INSTANCE_NAME_SIZE = 5497558138902
M_COM_IS_HARDWARE = 15
M_COM_NO_CONNECT = 2
M_COM_NO_CONNECT_NO_RXYZ_SWAP = 4
M_COM_OBJECT = 69256347648
M_COM_OPCUA_NODESET_LIST = 2001
M_COM_OPCUA_START = 2000
M_COM_PORT_NUMBER = 4724
M_COM_PORT_PCI_BUS_NB = 2361
M_COM_PROFINET_DEVICEID = 7
M_COM_PROFINET_GET_MODULES = 8
M_COM_PROFINET_GET_MODULE_ID = 10000
M_COM_PROFINET_GET_MODULE_ID_RANGE = 500
M_COM_PROFINET_GET_MODULE_INSIZE = 11000
M_COM_PROFINET_GET_MODULE_INSIZE_RANGE = 500
M_COM_PROFINET_GET_MODULE_OUTSIZE = 11500
M_COM_PROFINET_GET_MODULE_OUTSIZE_RANGE = 500
M_COM_PROFINET_GET_PLC_STATE = 13
M_COM_PROFINET_GET_SUBMODULE_ID = 10500
M_COM_PROFINET_GET_SUBMODULE_ID_RANGE = 500
M_COM_PROFINET_INPUT_SIZE = 12001
M_COM_PROFINET_OUTPUT_SIZE = 12002
M_COM_PROFINET_SLOT_CHANGED_COUNT = 57
M_COM_PROFINET_SLOT_CHANGED_LIST = 58
M_COM_PROFINET_START = 12000
M_COM_PROFINET_STATUS_BACKUP = 32
M_COM_PROFINET_STATUS_PRIMARY = 16
M_COM_PROFINET_STATUS_RUN = 2
M_COM_PROFINET_STATUS_STATION_OK = 64
M_COM_PROFINET_STATUS_STOP = 1
M_COM_PROTOCOL_ABB = 5
M_COM_PROTOCOL_CCLINK = 12
M_COM_PROTOCOL_DENSO = 9
M_COM_PROTOCOL_EPSON = 4
M_COM_PROTOCOL_ETHERNETIP = 2
M_COM_PROTOCOL_FANUC = 6
M_COM_PROTOCOL_GENERIC = 11
M_COM_PROTOCOL_KUKA = 7
M_COM_PROTOCOL_MODBUS = 3
M_COM_PROTOCOL_MOTOMAN = 8
M_COM_PROTOCOL_NAME_SIZE = 50
M_COM_PROTOCOL_OPCUA = 13
M_COM_PROTOCOL_PROFINET = 1
M_COM_PROTOCOL_STAUBLI = 10
M_COM_PROTOCOL_TYPE = 16
M_COM_PROTOCOL_TYPE_ALL = 0
M_COM_PROTOCOL_TYPE_PLC = 1
M_COM_PROTOCOL_TYPE_ROBOT = 2
M_COM_PROTOCOL_VERSION = 23
M_COM_REMOTE_ADDRESS = 2
M_COM_REMOTE_ADDRESS_SIZE = 5497558138882
M_COM_REMOTE_PORT = 3
M_COM_ROBOT_COMMAND_ABORT = 109
M_COM_ROBOT_COMMAND_TIMEOUT = 110
M_COM_ROBOT_CONNECT = 106
M_COM_ROBOT_CONNECT_RETRY = 112
M_COM_ROBOT_CONNECT_RETRY_WAIT = 113
M_COM_ROBOT_DISCONNECT = 111
M_COM_ROBOT_FIND_POSITION_RESULT = 2
M_COM_ROBOT_ISCONNECTED = 108
M_COM_ROBOT_TIMEOUT = 107
M_COM_START = 10
M_COM_SUCCESS = 0
M_COM_SUPPORTED = 4399
M_COM_TIMEOUT = 11
M_COM_USER_OPCODE = 1000
M_CONCENTRICITY = 7
M_CONCORD = 4096
M_CONCORDPOE_FINGERPRINT = 21216
M_CONCORD_1394_FINGERPRINT = 20816
M_CONCORD_GIGE_FINGERPRINT = 21008
M_CONCORD_POE = 140
M_CONDITION = 2167
M_CONDITIONAL = 1
M_CONDITION_BUFFER = 2978
M_COND_HIGH = 2172
M_COND_LOW = 2168
M_CONFIDENCE_MAP = 2195
M_CONFIG = 536870912
M_CONFIG_CHANGE_THREAD_PRIORITY = 15341
M_CONFUSION_MATRIX_ENTRIES = 3939
M_CONFUSION_MATRIX_PERCENTAGE = 3940
M_CONNECTION = 0
M_CONNECTION0 = 0
M_CONNECTION1 = 1
M_CONNECTION10 = 10
M_CONNECTION11 = 11
M_CONNECTION12 = 12
M_CONNECTION13 = 13
M_CONNECTION14 = 14
M_CONNECTION15 = 15
M_CONNECTION2 = 2
M_CONNECTION3 = 3
M_CONNECTION4 = 4
M_CONNECTION5 = 5
M_CONNECTION6 = 6
M_CONNECTION7 = 7
M_CONNECTION8 = 8
M_CONNECTION9 = 9
M_CONNECTION_BIT_RATE_DOWN_DIRECTION = 3040
M_CONNECTION_BIT_RATE_UP_DIRECTION = 3024
M_CONNECTION_COUNT = 3000
M_CONNECTION_ERROR = 132
M_CONNECTION_ID = 3056
M_CONNECTION_STATE = 3008
M_CONNECTION_TEST_ERROR_COUNT = 6752
M_CONNECTION_TEST_MODE = 5600
M_CONNECTION_TEST_PACKET_RECEIVED_COUNT = 6784
M_CONNECTION_TEST_PACKET_TRANSMITTED_COUNT = 6768
M_CONNECTION_TYPE = 3232
M_CONNECTIVITY = 2486
M_CONSTANT = 32768
M_CONSTANT_PIXEL_SIZE = 1376
M_CONSTANT_QUALITY = 4
M_CONSTRAINED = 1073741824
M_CONSTRAINED_ORDER = 2335
M_CONSTRAINED_POS_INDEX_VALUE = 2335
M_CONSTRAINED_POS_MASK = 6291456
M_CONSTRAINT = 67108864
M_CONSTRAINT_ALLOC_SIZE = 521
M_CONSTRAINT_FONT = 524
M_CONSTRAINT_INDEX_MASK = 255
M_CONSTRAINT_POSITION = 520
M_CONSTRAINT_TYPE = 32768
M_CONSTRAINT_TYPE_OLD = 134217728
M_CONSTRAIN_ASPECT_RATIO = 1220
M_CONSTRUCTED = 2
M_CONSTRUCTED_FEATURES = 259
M_CONSTRUCTION = 35
M_CONSTRUCTION_DATA = 107
M_CONSTRUCTION_FEATURE_INDEX_TAG = 33554432
M_CONSTRUCTION_FEATURE_LABEL_TAG = 16777216
M_CONST_DEFAULT_HOST = 2130706435
M_CONST_DIV = 33026
M_CONST_EXP = 265
M_CONST_LOG = 268
M_CONST_PASS = 32770
M_CONST_SUB = 32778
M_CONTACT_POINTS = 258
M_CONTAINER = 2147483648
M_CONTAINER_ERROR_1 = 184
M_CONTAINER_ERROR_2 = 56203
M_CONTAINER_ERROR_3 = 56208
M_CONTAINER_ID = 4675
M_CONTEXT = 134217728
M_CONTEXT0 = 805306368
M_CONTEXT1 = 805306369
M_CONTEXT2 = 805306370
M_CONTEXT3 = 805306371
M_CONTEXTUAL_MENU = 10551
M_CONTEXT_CONVERT = 535
M_CONTEXT_ID = 4112
M_CONTEXT_PATH = MIL_TEXT("///INSTALLDIR///contexts\\")
M_CONTEXT_TYPE = 162
M_CONTEXT_VALID = 1543
M_CONTIGUOUS = 1
M_CONTIGUOUS_LABELS = 2713
M_CONTINUE_TRAINING = 1
M_CONTINUOUS = -1
M_CONTOUR = 2048
M_CONTRAST_HYSTERESIS = 965
M_CONTRAST_REF = 6658
M_CONTRAST_UNIFORMITY = 41030
M_CONTRAST_UNIFORMITY_GRADE = 36938
M_CONTROL = 32
M_CONVERSION_GAMMA = 226
M_CONVERSION_MODE = 40
M_CONVERTIBLE = 33
M_CONVERTIBLE_WITH_COMPENSATION = 34
M_CONVERT_TO_PIXEL = 1500
M_CONVERT_TO_WORLD = 1501
M_CONVEX_HULL = 80
M_CONVEX_HULL_AREA = 89
M_CONVEX_HULL_COG_X = 96
M_CONVEX_HULL_COG_Y = 97
M_CONVEX_HULL_FILL_RATIO = 93
M_CONVEX_HULL_PERIMETER = 99
M_CONVEX_HULL_X = 81
M_CONVEX_HULL_XY_PACKED = 83
M_CONVEX_HULL_Y = 82
M_CONVEX_PERIMETER = 20
M_COPY = 131072
M_COPY_ANGLE = 118
M_COPY_ANNOTATIONS_LAYER_TO_CLIPBOARD = 10217
M_COPY_ANNOTATIONS_LAYER_TO_ID = 10218
M_COPY_BUFFER_LAYER_TO_CLIPBOARD = 10215
M_COPY_BUFFER_LAYER_TO_ID = 10216
M_COPY_BY_DRIVER = 2315
M_COPY_CALIBRATION_INFO = 3
M_COPY_DISPLAY_TO_ID = 10204
M_COPY_DISP_HOOK_CONTEXT = 10
M_COPY_EVEN = 8192
M_COPY_FEATURE_EDGELS = 65
M_COPY_FROM_FONT = 2
M_COPY_HISTOGRAM_INFO = 106
M_COPY_HOOK_CONTEXT = 103
M_COPY_NEIGHBORHOOD_INFO = 104
M_COPY_ODD = 16384
M_COPY_OFFSET_X = 115
M_COPY_OFFSET_Y = 116
M_COPY_REG_CONTEXT = 1073741825
M_COPY_REG_RESULT = 1073741826
M_COPY_SCALE = 117
M_COPY_SOURCE_DATA = 1
M_COPY_SRC_DATA = 1
M_COPY_TO_BUFFER = 10204
M_COPY_TO_BUFFER_WITH_SCALE = 10219
M_COPY_TO_CLIPBOARD = 10202
M_COPY_TO_FONT = 1
M_COPY_TO_HWND = 65536
M_CORE_AFFINITY_MASK = 1590
M_CORE_AFFINITY_MASK_ARRAY_SIZE = 1601
M_CORE_AFFINITY_MASK_HARDWARE = 1647
M_CORE_AFFINITY_MASK_PROCESS = 1642
M_CORE_ERROR_END = 56999
M_CORE_ERROR_START = 56000
M_CORE_FORCE_NB = 1603
M_CORE_FORCE_ONE = 1606
M_CORE_ID = 1820
M_CORE_MAX = 1587
M_CORE_MAX_FOR_COPY = 1586
M_CORE_MEMORY_BANK = 1598
M_CORE_MEMORY_BANK_AFFINITY_MASK = 1599
M_CORE_NUM_EFFECTIVE = 1592
M_CORE_NUM_HARDWARE = 1594
M_CORE_NUM_OS = 1651
M_CORE_NUM_PROCESS = 1592
M_CORE_ORIG_ERROR_END = 199
M_CORE_ORIG_ERROR_START = 0
M_CORE_PARKING_STATE = 1789
M_CORE_SHARING = 1591
M_CORE_THROTTLING_STATE = 1790
M_CORE_USE_BIT = 4096
M_CORE_USE_MASK = 8128
M_CORNER_AND_DIMENSION = 1
M_CORNER_BOTTOM_LEFT_X = 1224
M_CORNER_BOTTOM_LEFT_Y = 1228
M_CORNER_BOTTOM_RIGHT_X = 1223
M_CORNER_BOTTOM_RIGHT_Y = 1227
M_CORNER_P1_X = 41049
M_CORNER_P1_Y = 41050
M_CORNER_P2_X = 41051
M_CORNER_P2_Y = 41052
M_CORNER_P3_X = 41053
M_CORNER_P3_Y = 41054
M_CORNER_P4_X = 41055
M_CORNER_P4_Y = 41056
M_CORNER_RADIUS = 239
M_CORNER_TOP_LEFT_X = 1221
M_CORNER_TOP_LEFT_Y = 1225
M_CORNER_TOP_RIGHT_X = 1222
M_CORNER_TOP_RIGHT_Y = 1226
M_CORNER_X_ALL = 3847
M_CORNER_Y_ALL = 3848
M_CORNER_Z_ALL = 3849
M_CORONA = 20
M_CORONA_II = 25
M_CORONA_II_WITH_DIG_MODULE = 281
M_CORONA_LC = 21
M_CORONA_RR = 23
M_CORONA_VIA = 22
M_CORRECTED = 2
M_CORRECTED_DEPTH = 18
M_CORRECTED_DEPTH_MAP = 1
M_CORRECTED_DEPTH_MAP_BUFFER_TYPE = 8
M_CORRECTED_DEPTH_MAP_SIZE_X = 6
M_CORRECTED_DEPTH_MAP_SIZE_Y = 7
M_CORRECTED_SCALES = 5
M_CORRECTION_STATE = 126
M_CORRECT_LENS_DISTORTION_ONLY = 2
M_CORRELATE = 2
M_CORRELATE_NORMALIZED = 1
M_CORRELATION = 1
M_CORRUPT = 16777216
M_CORRUPTED_FRAME = 6923
M_CORRUPTED_FRAME_ERROR = 6924
M_COS = 3
M_COUNTER_END = 512
M_COUNTER_INDEX = 8585216
M_COUNTER_OVERFLOW = 210
M_COUNTER_START = 256
M_COUNT_LIST = 131072
M_COUPLING_MODE = 4380
M_COVARIANCE = 610
M_COVERAGE = 216
M_COVERAGE_MAX = 2457
M_COVERAGE_MIN = 2453
M_CPU = 3427
M_CPU_FAMILY_NUMBER = 10306
M_CPU_FLAG_RANGE = 10240
M_CPU_FLAG_RANGE_END = 12287
M_CPU_MODEL_NUMBER = 10307
M_CPU_SERIAL_NUMBER = 10309
M_CPU_SIMD_BITFIELD = 10310
M_CPU_SPEED = 2320
M_CPU_STEPPING_NUMBER = 10308
M_CPU_SUPPORT_AVX512_WITH_2_FMA_UNITS = 10499
M_CPU_SUPPORT_ENHANCED_REP_MOVSB_STOSB = 10498
M_CPU_SUPPORT_RDTSC = 10497
M_CPU_TRAIN_ENGINE_LOAD_STATUS = 4108
M_CPU_VENDOR_NAME = 10312
M_CPU_VENDOR_NAME_MAX_SIZE = 13
M_CREATE = 1
M_CREATE_REGCONTROL = 15061
M_CREATE_SYSTEM = 8
M_CREST = 2049
M_CREST_BLACK = 2826
M_CREST_WHITE = 2825
M_CRONOSPLUS = 70
M_CRONOSPLUS_FINGERPRINT = 20912
M_CROP_CHAIN = 304
M_CROSS = 8192
M_CROSS_DERIVATIVE_ID = 16777216
M_CRTC0 = 65536
M_CRTC1 = 131072
M_CRTC2 = 196608
M_CRTC3 = 262144
M_CRTC4 = 327680
M_CRTC5 = 393216
M_CRTC6 = 458752
M_CRTC_MASK = 458752
M_CRTC_OFFSET = 16
M_CRYPTO = 5301
M_CRYPTOGRAPHY = 5301
M_CRYPTOGRAPHY_HMAC_KEY = 2386
M_CRYPTOGRAPHY_MODE = 2380
M_CRYPTOGRAPHY_PRIVATE_KEY = 2384
M_CRYPTOGRAPHY_PUBLIC_KEY = 2383
M_CRYPTOGRAPHY_P_KEY = 2381
M_CRYPTOGRAPHY_Q_KEY = 2382
M_CRYPTOGRAPHY_RSA = 2385
M_CRYPTO_MODE = 2380
M_CRYPTO_PRIVATE_KEY = 2384
M_CRYPTO_PUBLIC_KEY = 2383
M_CRYPTO_P_KEY = 2381
M_CRYPTO_Q_KEY = 2382
M_CRYPTO_RSA = 2385
M_CUBE = 260
M_CUDA_FAIL = 4098
M_CUMULATIVE_VALUE = 1
M_CURRENT = 2
M_CURRENTLY_CALCULATING = 2718
M_CURRENTLY_CENTERED_X = 10194
M_CURRENTLY_CENTERED_Y = 10198
M_CURRENTLY_IN_HOOK = 2341
M_CURRENTLY_PREDICTING = 2789
M_CURRENTLY_READING = 2553
M_CURRENTLY_TRAINING = 3425
M_CURRENTLY_USED_CAMERA = 2289
M_CURRENT_APPLICATION = 15021
M_CURRENT_DATAGRAM_ASCII_VERSION = MIL_TEXT("10.00")
M_CURRENT_DATAGRAM_MT_VERSION = MIL_TEXT("10.00")
M_CURRENT_DATAGRAM_VERSION = 1000
M_CURRENT_DIRECTX_VERSION = 15331
M_CURRENT_ERROR_HANDLER_PTR = 15008
M_CURRENT_ERROR_HANDLER_USER_PTR = 15009
M_CURRENT_FCT = 196608
M_CURRENT_FCT_FULL = 262144
M_CURRENT_GRAB_BUFFER_HOST_ADDRESS = 4305
M_CURRENT_GRAB_BUFFER_PHYSICAL_ADDRESS = 4306
M_CURRENT_LINE_COUNT = 4388
M_CURRENT_MONITOR_RECT = 8512
M_CURRENT_MONITOR_WORK_RECT = 8513
M_CURRENT_OVERLAY_ID = 1127
M_CURRENT_RESOLUTION = MIL_TEXT("M_CURRENT_RESOLUTION")
M_CURRENT_SCREEN_RECT = 9265
M_CURRENT_SCREEN_WORK_RECT = 9266
M_CURRENT_SOURCE = 7
M_CURRENT_SUB = 327680
M_CURRENT_SUB_1 = 327680
M_CURRENT_SUB_2 = 393216
M_CURRENT_SUB_3 = 458752
M_CURRENT_SUB_NB = 4
M_CURRENT_THREAD_ID = 1103
M_CURRENT_USER = 65536
M_CURRENT_USER_PP4 = 65536
M_CURRENT_USER_U79 = 3778
M_CURSOR_COLOR_PICKER = 28
M_CURSOR_DEFAULT = 1
M_CURSOR_HAND_CLOSED = 17
M_CURSOR_HAND_OPEN = 16
M_CURSOR_NULL = 0
M_CURSOR_TYPE_MASK = 63
M_CURVE_EDGEL_GAP_SIZE = 3066
M_CURVE_INFO = 3147
M_CUSTOM = 2
M_CUSTOMER_PRODUCT_ID = 2093
M_CUSTOM_BRGG = 256
M_CUSTOM_DISPLAY = 2097152
M_CUSTOM_DISPLAY_BUFFER = 1121
M_CUSTOM_FINGERPRINT = 21264
M_CUSTOM_FPGA_COLUMN = 1
M_CUSTOM_FPGA_PROCESSING = 5240
M_CUSTOM_FPGA_PROCESSING_EROSION = 5241
M_CUSTOM_FPGA_PROCESSING_MAX_SELECTOR = 5242
M_CUSTOM_FPGA_ROW = 2
M_CUSTOM_GGBR = 320
M_CUSTOM_GGRB = 352
M_CUSTOM_MESSAGE_CLIENT = 76
M_CUSTOM_MESSAGE_SERVER = 75
M_CUSTOM_RBGG = 288
M_CUSTOM_SCHEME_CHANGING = 10211
M_CUSTOM_TL = 1536
M_CXP = 512
M_CXP1 = 40
M_CXP10 = 80
M_CXP12 = 88
M_CXP2 = 48
M_CXP3 = 56
M_CXP5 = 64
M_CXP6 = 72
M_CYCLICAL_DECAY = 3491
M_CYLINDER = 3656
M_CYLINDER_BASES = 4688
M_CYLINDRICAL = 2718
M_C_FORWARD = 16387
M_C_REVERSE = 16403
M_D12G = 1048576
M_D3D10_HANDLE = 14040
M_D3D10_TEXTURE = 14041
M_D3D10_TEXTURE_LK = 14044
M_D3D11_BUFFER = 14066
M_D3D11_BUFFER_LK = 14067
M_D3D11_HANDLE = 14060
M_D3D11_TEXTURE = 14061
M_D3D11_TEXTURE_LK = 14064
M_D3D9_HANDLE = 14020
M_D3D9_SURFACE = 14021
M_D3D9_SURFACE_LK = 14028
M_D3D9_SURFACE_RT = 14027
M_D3D9_TEXTURE = 14022
M_D3D9_TEXTURE_LK = 14029
M_D3D_AVAILABLE = 4578
M_D3D_BUFFER = 68719476736
M_D3D_NO_TEARING = 8543
M_D3D_OFFSCREEN_SURFACE = 288230376151711744
M_D3D_SUPPORTED_NO_TEARING_MODE = 8501
M_D3D_VSYNC_INTERVAL_FOUR = 10011
M_D3D_VSYNC_INTERVAL_ONE = 10008
M_D3D_VSYNC_INTERVAL_THREE = 10010
M_D3D_VSYNC_INTERVAL_TWO = 10009
M_D3G = 268435456
M_D6G = 536870912
M_DA = 65536
M_DARK_CONST = 203
M_DARK_IMAGE = 200
M_DARK_IMAGE_HEIGHT = 209
M_DARK_IMAGE_NB_BANDS = 207
M_DARK_IMAGE_TYPE = 210
M_DARK_IMAGE_WIDTH = 208
M_DARK_LABEL = 83
M_DATA = 4
M_DATAMATRIX = 2
M_DATAMATRIX_NAME = MIL_TEXT("Datamatrix")
M_DATAMATRIX_SHAPE = 32788
M_DATASET = 3802
M_DATASET_FEATURES = 3946
M_DATASET_IMAGES = 3473
M_DATA_ALL = 0
M_DATA_ANGLE_POLARITY = 111
M_DATA_ANGLE_RANGE = 110
M_DATA_ANGLE_TOLERANCE = 110
M_DATA_AUGMENT_ERROR = 195
M_DATA_AUGMENT_ERROR_2 = 56211
M_DATA_CODEWORDS = 45065
M_DATA_EXTREMES_GLOBAL = 4673
M_DATA_EXTREMES_PER_BAND = 4674
M_DATA_FIT = 1719
M_DATA_FITTED = 2
M_DATA_FORMAT = 1041
M_DATA_INFO_TYPE = 6766
M_DATA_LATCH_BUFFER_HOST_ADDRESS = 8302
M_DATA_LATCH_BUFFER_TRIGGER_SOURCE = 8432
M_DATA_LATCH_CALLBACK = 8464
M_DATA_LATCH_CLOCK_FREQUENCY = 8301
M_DATA_LATCH_CXP_HEADER_PIXEL_FORMAT = 4
M_DATA_LATCH_CXP_HEADER_X_SIZE_OFFSET = 6
M_DATA_LATCH_CXP_HEADER_Y_SIZE_OFFSET = 5
M_DATA_LATCH_FLUSH_TRIGGER_SOURCE = 8496
M_DATA_LATCH_INDEX_START = 8304
M_DATA_LATCH_INSTANCE_BITSHIFT = 16
M_DATA_LATCH_INSTANCE_MASK = -65536
M_DATA_LATCH_MAX_INDEX = 32
M_DATA_LATCH_MODE = 8400
M_DATA_LATCH_PARSING_MODE = 8300
M_DATA_LATCH_SIZE_BYTE = 8592
M_DATA_LATCH_STATE = 8304
M_DATA_LATCH_TRIGGER_ACTIVATION = 8528
M_DATA_LATCH_TRIGGER_SOURCE = 8368
M_DATA_LATCH_TYPE = 8336
M_DATA_LATCH_VALUE = 8656
M_DATA_LATCH_VALUE_ALL = 8624
M_DATA_LATCH_VALUE_COUNT = 8560
M_DATA_REDUCTION = 1
M_DATA_STORAGE_MODE = 1054
M_DATA_TYPE = 1022
M_DAUBECHIES_1 = 3
M_DAUBECHIES_2 = 4
M_DAUBECHIES_3 = 5
M_DAUBECHIES_3_COMPLEX = 11
M_DAUBECHIES_4 = 6
M_DAUBECHIES_5 = 7
M_DAUBECHIES_5_COMPLEX = 12
M_DAUBECHIES_6 = 8
M_DAUBECHIES_7 = 9
M_DAUBECHIES_7_COMPLEX = 13
M_DAUBECHIES_8 = 10
M_DA_WEB_OFFSET = 4
M_DBCL = 4194304
M_DC = 2
M_DCF_REALLOC = 32
M_DCF_REALLOC_HANDLER_PTR = 4211
M_DCF_REALLOC_HANDLER_USER_PTR = 4212
M_DCF_SUPPORTED = 2050
M_DCH = 131072
M_DCHAR_SEG = 28672
M_DCT = 3
M_DCT8X8 = 2
M_DC_ALLOC = 9000
M_DC_FREE = 9001
M_DC_FREE_NO_MODIFIED_CHECK = 9032
M_DC_HANDLE = 9002
M_DDRAW = 1073741824
M_DDRAW7_HANDLE = 14015
M_DDRAW7_SPECIFIC_BITS = 572055292477440
M_DDRAW_AVAILABLE = 4503
M_DDRAW_EDGE_MODEL = 36864
M_DDRAW_SURFACE = 14015
M_DDRAW_UNDERLAY_FORMAT = 2137
M_DEAD_PIXELS = 80
M_DEAD_PIXELS_IMAGE_ATTRIBUTE = 92
M_DEAD_PIXELS_IMAGE_HEIGHT = 89
M_DEAD_PIXELS_IMAGE_NB_BANDS = 87
M_DEAD_PIXELS_IMAGE_TYPE = 91
M_DEAD_PIXELS_IMAGE_WIDTH = 88
M_DEAD_PIXEL_CONTEXT = 4
M_DEBUG = 30
M_DEBUG_BUFFER_CLEAR = 2100
M_DEBUG_BUFFER_PATH = 7708
M_DEBUG_BUFFER_TO_FILE = 2101
M_DEBUG_COLOR = 10044
M_DEBUG_INFORMATION = 251
M_DEBUG_INFORMATION_PATH = 54
M_DEBUG_INFORMATION_PATH_SIZE = 5497558138934
M_DEBUG_LOG_INFO = 1051
M_DECAY = 3486
M_DECIMATION_STEP_MODEL = 1940
M_DECIMATION_STEP_SCENE = 1941
M_DECODABILITY = 40966
M_DECODABILITY_GRADE = 36875
M_DECODED_SCANS_END_X = 3597
M_DECODED_SCANS_END_Y = 3598
M_DECODED_SCANS_SCORE = 3594
M_DECODED_SCANS_START_X = 3595
M_DECODED_SCANS_START_Y = 3596
M_DECODER_MODE = 4417
M_DECODER_REV_ID = 4318
M_DECODE_ALGORITHM = 2858
M_DECODE_GRADE = 36869
M_DECOMPOSITION_LEVEL = 2562
M_DECREMENT_ASYNC = 2
M_DEFAULT = 268435456
M_DEFAULT_1394 = 1048576
M_DEFAULT_3BITS_3BANDS_DISP_BUFFER_FORMAT = 15379
M_DEFAULT_CLUSTER_NODE = 15724
M_DEFAULT_CLUSTER_NODE_VALUE = 2130706432
M_DEFAULT_CONSTRAINT = 134217728
M_DEFAULT_CONSTRAINT_ALLOC_SIZE = 522
M_DEFAULT_CONSTRAINT_FONT = 525
M_DEFAULT_CONSTRAINT_TYPE = 523
M_DEFAULT_DISPLAY_RESOLUTION = 10108
M_DEFAULT_ERROR_CONTEXT = 8388615
M_DEFAULT_EXTENDED_DEPTH_OF_FIELD_CONTEXT = 8388618
M_DEFAULT_GRAPHIC_CONTEXT = 2130706434
M_DEFAULT_HOST = 2130706433
M_DEFAULT_HOST_FROM_ID = 15290
M_DEFAULT_IO_DEVICE = 6730
M_DEFAULT_LUT = 8388609
M_DEFAULT_MEGA_DISPLAY_SIZE_X = 10158
M_DEFAULT_MEGA_DISPLAY_SIZE_Y = 10159
M_DEFAULT_NO_LAYER = 33816576
M_DEFAULT_PITCH_BYTE_MULTIPLE = 2294
M_DEFAULT_QUANTIZATION_TABLE = 8204
M_DEFAULT_RESOLUTION_X = 72
M_DEFAULT_RESOLUTION_Y = 72
M_DEFAULT_SETTINGS = 67108864
M_DEFAULT_SOURCE_LAYER = 34603008
M_DEFAULT_SYSTEM_ID = 15952
M_DEFAULT_UNIFORM_CALIBRATION = 8388616
M_DEFAULT_VALUE = 3298534883328
M_DEFAULT_WEB_OFFSET = 0
M_DEFECTS = 40965
M_DEFECTS_GRADE = 36874
M_DEFINITION_OFFSET_X = 817
M_DEFINITION_OFFSET_Y = 818
M_DEF_ADD_SEARCH_AREA_X = 0
M_DEF_ADD_SEARCH_AREA_Y = 0
M_DEF_AUTO_PUBLISH = 0
M_DEF_BLOB_ON_ACCELERATED = -9999
M_DEF_CHAR_ACCEPTANCE = 1
M_DEF_CHAR_INVALID = 0
M_DEF_DEBUG = 0
M_DEF_ENHANCE_DOT_CHARS = 0
M_DEF_ENHANCE_MORPHO = 2
M_DEF_EXTRA_CHARACTERS = -9999
M_DEF_KILL_BORDER = -9997
M_DEF_PAT_ON_ACCELERATED = -9999
M_DEF_PROC_ON_ACCELERATED = -9997
M_DEF_READ_ACCURACY = 2
M_DEF_READ_FAST_FIND = 268435456
M_DEF_READ_FIRST_LEVEL = 268435456
M_DEF_READ_LAST_LEVEL = 268435456
M_DEF_READ_MODEL_STEP = 268435456
M_DEF_READ_ROBUSTNESS = 2
M_DEF_READ_SPEED = 2
M_DEF_SKIP_CONTRAST_ENHANCE = -9999
M_DEF_SKIP_SEARCH = -9999
M_DEF_SKIP_STRING_LOCATION = -9999
M_DEF_STRING_ACCEPTANCE = 1
M_DEF_STRING_LOC_GOOD_CHAR_SIZE = 0.9
M_DEF_STRING_LOC_GOOD_NB_CHAR = 4
M_DEF_STRING_LOC_MAX_CHAR_DISTANCE = 0.5
M_DEF_STRING_LOC_MAX_CHAR_SIZE = 1.5
M_DEF_STRING_LOC_MAX_NB_ITER = 2
M_DEF_STRING_LOC_MIN_CHAR_SIZE = 0.66
M_DEF_STRING_LOC_MIN_CHAR_SPACE = 0.66
M_DEF_STRING_LOC_NB_MODELS = 2
M_DEF_STRING_LOC_STOP_ITER = 0.5
M_DEF_STRING_MAX_SLOPE = 0.176327
M_DEF_STRING_READ_BAD_ADD_CHAR = 4
M_DEF_STRING_READ_BAD_SIZE_X = 0.4
M_DEF_STRING_READ_BAD_SIZE_Y = 0.4
M_DEF_STRING_READ_GOOD_SIZE_X = 0.25
M_DEF_STRING_READ_GOOD_SIZE_Y = 0.25
M_DEF_STRING_READ_SIZE_X = 0.33
M_DEF_STRING_READ_SIZE_Y = 0.25
M_DEINTERLACE = 3
M_DEINTERLACE_CONTEXT = 1
M_DEINTERLACE_TYPE = 2
M_DELETE = 3
M_DELETE_ELEMENT = 16
M_DELETE_EXTERNAL_DISPLAY_ID = 9207
M_DELETE_PERMITTED_CHARS_ENTRY = 2714
M_DELTA_E = 4
M_DELTA_E_SQR = 24
M_DENOISE_PSEUDO_ID = 9437440
M_DEPENDENCIES = 1015
M_DEPTH_CORRECTED_DATA = 1902
M_DEPTH_CORRECTION = 2
M_DEPTH_CORRECTION_STATE = 1347
M_DEPTH_FROM_FOCUS = 3
M_DEPTH_FROM_FOCUS_RESULT = 3
M_DEPTH_MAP = 8388608
M_DERICHE = 9437194
M_DERICHE_PREDEFINED_KERNEL = 546308096
M_DERICHE_PREDEFINED_KERNEL_INVALID_FACTOR = 579862528
M_DERICHE_PREDEFINED_KERNEL_INVALID_TYPE = 563085312
M_DERIVED_GEOMETRY_REGION = 206
M_DESCENDING = 2
M_DESCRIPTOR_LOCK = 12000
M_DESKTOP_COMPOSITION = 15399
M_DESKTOP_DEVICE_NAME = 9252
M_DESKTOP_FORMAT = 15349
M_DESKTOP_RESOLUTION = 9250
M_DESKTOP_SIZE_BIT = 15350
M_DEST = 1024
M_DESTINATION_WRITTEN = 2
M_DETAIL_LEVEL = 111
M_DETECTED = 256
M_DETECT_HOOK_THREAD = 1020
M_DETECT_PCI_DEVICE = 1
M_DEV = 0
M_DEV0 = 0
M_DEV1 = 1
M_DEV10 = 10
M_DEV11 = 11
M_DEV12 = 12
M_DEV13 = 13
M_DEV14 = 14
M_DEV15 = 15
M_DEV16 = 16
M_DEV17 = 17
M_DEV18 = 18
M_DEV19 = 19
M_DEV2 = 2
M_DEV20 = 20
M_DEV21 = 21
M_DEV22 = 22
M_DEV23 = 23
M_DEV24 = 24
M_DEV25 = 25
M_DEV26 = 26
M_DEV27 = 27
M_DEV28 = 28
M_DEV29 = 29
M_DEV3 = 3
M_DEV30 = 30
M_DEV31 = 31
M_DEV32 = 32
M_DEV33 = 33
M_DEV34 = 34
M_DEV35 = 35
M_DEV36 = 36
M_DEV37 = 37
M_DEV38 = 38
M_DEV39 = 39
M_DEV4 = 4
M_DEV40 = 40
M_DEV41 = 41
M_DEV42 = 42
M_DEV43 = 43
M_DEV44 = 44
M_DEV45 = 45
M_DEV46 = 46
M_DEV47 = 47
M_DEV48 = 48
M_DEV49 = 49
M_DEV5 = 5
M_DEV50 = 50
M_DEV51 = 51
M_DEV52 = 52
M_DEV53 = 53
M_DEV54 = 54
M_DEV55 = 55
M_DEV56 = 56
M_DEV57 = 57
M_DEV58 = 58
M_DEV59 = 59
M_DEV6 = 6
M_DEV60 = 60
M_DEV61 = 61
M_DEV62 = 62
M_DEV63 = 63
M_DEV7 = 7
M_DEV8 = 8
M_DEV9 = 9
M_DEVIATION_MAX = 1359
M_DEVIATION_MEAN = 1358
M_DEVIATION_MIN = 2907
M_DEVIATION_TOLERANCE = 3035
M_DEVICE_ALLOCATED = 1
M_DEVICE_ENTERVT = 55
M_DEVICE_FREE = 2
M_DEVICE_ID = 4550
M_DEVICE_LEAVEVT = 54
M_DEVICE_LOSING = 45
M_DEVICE_LOST = 46
M_DEVICE_NAME = 68719476736
M_DEVICE_NAME_MAX_SIZE = 1056
M_DEVICE_NUMBER_MASK = 63
M_DEVICE_RESTORED = 48
M_DEVICE_RESTORING = 47
M_DEVICE_SPECIFIC_EVENT = 36864
M_DEV_DATASET = 3704
M_DEV_DATASET_ACCURACY = 3555
M_DEV_DATASET_ACCURACY_AFTER_EACH_TREE = 3808
M_DEV_DATASET_CONFUSION_MATRIX = 3610
M_DEV_DATASET_CONFUSION_MATRIX_SIZE_X = 3611
M_DEV_DATASET_CONFUSION_MATRIX_SIZE_Y = 3983
M_DEV_DATASET_EPOCH_ACCURACY = 3642
M_DEV_DATASET_EPOCH_ERROR_ENTRIES = 3723
M_DEV_DATASET_EPOCH_ERROR_RATE = 3747
M_DEV_DATASET_ERROR_ENTRIES = 3725
M_DEV_DATASET_ERROR_RATE = 3745
M_DEV_DATASET_ERROR_RATE_AFTER_EACH_TREE = 3806
M_DEV_DATASET_ID = 3694
M_DEV_DATASET_PREDICT_SCORES = 3953
M_DEV_DATASET_USED_ENTRIES = 3986
M_DEV_MIN_HEAP_SIZE = 4604
M_DEV_NUMBER = 3
M_DEV_SCREEN_MANAGER_END = 9299
M_DEV_SCREEN_MANAGER_START = 9250
M_DFCL = 16384
M_DFSAS_READ = 12288
M_DFWD = 256
M_DGPRCSS_WATCHOG_ERROR = 302
M_DHT = 16
M_DHTI = 128
M_DIAGONAL_LEVEL_TAG = 67108864
M_DIAMETER = 4769
M_DIAMOND = 32768
M_DIB = 576460752303423488
M_DIBTODEV_METHOD = 131072
M_DIBTODEV_MODE = 131072
M_DIB_HANDLE = 9031
M_DIB_METHOD = 507904
M_DIB_MODE = 507904
M_DIB_ONLY = 2053
M_DIB_OR_DDRAW = 2054
M_DIFFERENCE = 3628
M_DIFFERENCE_BOTH_SIDES = 3087
M_DIFFERENCE_DISTANCE_MODE = 3078
M_DIFFERENCE_MAXIMUM_EXPECTED_GAP_BETWEEN_POINTS = 3189
M_DIFFERENCE_THRESHOLD_HIGH = 3079
M_DIFFERENCE_THRESHOLD_LOW = 3080
M_DIGIT = 262144
M_DIGITAL = 0
M_DIGITAL_MODULE = 256
M_DIGITAL_MODULE_PRESENT = 2105
M_DIGITIZER = 1048576
M_DIGITIZER_CONTROL_LOG = 5187
M_DIGITIZER_DEV0 = 65536
M_DIGITIZER_DEV1 = 131072
M_DIGITIZER_DEV10 = 720896
M_DIGITIZER_DEV11 = 786432
M_DIGITIZER_DEV12 = 851968
M_DIGITIZER_DEV13 = 917504
M_DIGITIZER_DEV14 = 983040
M_DIGITIZER_DEV15 = 1048576
M_DIGITIZER_DEV2 = 196608
M_DIGITIZER_DEV3 = 262144
M_DIGITIZER_DEV4 = 327680
M_DIGITIZER_DEV5 = 393216
M_DIGITIZER_DEV6 = 458752
M_DIGITIZER_DEV7 = 524288
M_DIGITIZER_DEV8 = 589824
M_DIGITIZER_DEV9 = 655360
M_DIGITIZER_DEVx_INDEX_MASK = 16711680
M_DIGITIZER_DEVx_INDEX_OFFSET = 16
M_DIGITIZER_ERROR = 13
M_DIGITIZER_FILTER_MASK = 65535
M_DIGITIZER_FILTER_SIGMA = 6689
M_DIGITIZER_FILTER_TYPE = 5450
M_DIGITIZER_ID = 1835008
M_DIGITIZER_INTERNAL_BUFFERS_NUM = 4605
M_DIGITIZER_MODE = 2290
M_DIGITIZER_NUM = 2004
M_DIGITIZER_NUM_ALLOCATED = 2331
M_DIGITIZER_TYPE = 2400
M_DIGITIZER_TYPE_NUMBER = 2400
M_DIGITS = 262144
M_DIGIT_OLD = 3
M_DIG_ALLOC_ERROR = 156
M_DIG_CONTROL_TYPE_RESERVED_BIT_MASK = 12884901888
M_DIG_DISPATCH_IMMEDIATE = 576460752303423488
M_DIG_INQUIRE_MIL_ID_END = 1199
M_DIG_INQUIRE_MIL_ID_START = 1100
M_DIG_INQUIRE_SIZEOF_DOUBLE_END = 6699
M_DIG_INQUIRE_SIZEOF_DOUBLE_START = 6000
M_DIG_INQUIRE_SIZEOF_INT64_END = 6799
M_DIG_INQUIRE_SIZEOF_INT64_START = 6700
M_DIG_INQUIRE_STRING_END = 7999
M_DIG_INQUIRE_STRING_START = 7700
M_DIG_INQUIRE_SUPPORT_COMPONENT = 4398
M_DIG_INQUIRE_UNKNOWN_SIZEOF_END = 6899
M_DIG_INQUIRE_UNKNOWN_SIZEOF_START = 6800
M_DIG_NON_BITWISE_MASK = 15
M_DIG_OK_TO_BE_FREED = 4427
M_DIG_PRCSS_COUNT_MASK = -32
M_DIG_PRCSS_COUNT_SHIFT = 5
M_DIG_PROCESS_IN_PROGRESS = 5337
M_DIG_PROCESS_PTR = 1040
M_DIG_SERVICE_ERROR = 149
M_DIG_SUPPORT_END_NO = 5949
M_DIG_SUPPORT_END_YES = 5999
M_DIG_SUPPORT_START_NO = 5900
M_DIG_SUPPORT_START_YES = 5950
M_DIG_SYS_TIMER_INQUIRE_SIZEOF_DOUBLE_END = 134072
M_DIG_SYS_TIMER_INQUIRE_SIZEOF_DOUBLE_START = 133072
M_DILATE = 2
M_DIRECTION_MODE = 3431
M_DIRECTION_REFERENCE_X = 3435
M_DIRECTION_REFERENCE_Y = 3436
M_DIRECTION_REFERENCE_Z = 3437
M_DIRECTX = 1073741824
M_DIRECTX_APP_DX_HANDLER_END = 9549
M_DIRECTX_APP_DX_HANDLER_START = 9500
M_DIRECTX_CAN_CREATE_OVER_HOST_MEMORY = 9500
M_DIRECTX_CREATION = 8388608
M_DIRECTX_D3D10 = 10
M_DIRECTX_D3D11 = 11
M_DIRECTX_D3D9 = 9
M_DIRECTX_DDRAW7 = 7
M_DIRECTX_METHOD = 4096
M_DIRECTX_MODE = 4096
M_DIRECTX_NONE = 0
M_DIRECTX_SERVICE = 8388617
M_DIRECTX_SERVICE_ERROR = 142
M_DIRECTX_SERVICE_IS_VALID = 15126
M_DIRECTX_STRUCT_FOR_MAPPABLE_BUFFER = 1019
M_DIRECTX_SURFACE_MAPPABLE = 9036
M_DIRECTX_SURFACE_MAPPED = 9035
M_DIRECTX_UNDETERMINED = -1
M_DIRECTX_USED_FOR_AUXILIARY = 4551
M_DIRECTX_VERSION = 15303
M_DIRECTX_VERSION_FLAG = 8388608
M_DIRECTX_VERSION_MASK = 983040
M_DIRECTX_VERSION_OFFSET = 16
M_DIRECTX_VIDEO_BUFFER_MAPPABLE = 9502
M_DIRECTX_VIDEO_DEVICE_ID = 10012
M_DIRECTX_VIDEO_DEVICE_OBJECT = 1099511627777
M_DIRECT_ACCESS_2_END = 24791
M_DIRECT_ACCESS_2_START = 23000
M_DIRECT_ACCESS_3_END = 25369
M_DIRECT_ACCESS_3_START = 25050
M_DIRECT_ACCESS_END = 16522
M_DIRECT_ACCESS_START = 15832
M_DIRECT_ARROW = 1643
M_DISABLE = -9999
M_DISABLE_BUFTRANSFER_METHOD = 15048
M_DISABLE_CHAR = 969
M_DISABLE_FOR_ALL_FUNCTIONS = 8
M_DISCARD = 33
M_DISCARD_FIELD = 3
M_DISCOVER_DEVICE = 1081
M_DISCOVER_DEVICE_ADDRESS = 35304
M_DISCOVER_DEVICE_ALLOCATION_STATUS = 1712
M_DISCOVER_DEVICE_CAPABILITIES = 35048
M_DISCOVER_DEVICE_COUNT = 1082
M_DISCOVER_DEVICE_DIGITIZER_NUMBER = 1200
M_DISCOVER_DEVICE_INTERFACE_NAME = 34536
M_DISCOVER_DEVICE_INTERFACE_TYPE = 1456
M_DISCOVER_DEVICE_MANUFACTURER_INFO = 33512
M_DISCOVER_DEVICE_MANUFACTURER_NAME = 33256
M_DISCOVER_DEVICE_MAX_COUNT = 256
M_DISCOVER_DEVICE_MODEL_NAME = 33000
M_DISCOVER_DEVICE_SERIAL_NUMBER = 34280
M_DISCOVER_DEVICE_STATISTICS = 34792
M_DISCOVER_DEVICE_USER_NAME = 33768
M_DISCOVER_DEVICE_VERSION = 34024
M_DISCRETE_INPUT = MIL_TEXT("M_DISCRETE_INPUT")
M_DISCRETE_RANGE = 4096
M_DISK = 4895
M_DISK_EDGES_NOT_FOUND = 256
M_DISK_NOT_FOUND = 4096
M_DISP = 32
M_DISPARITY = 59
M_DISPARITY_EXTERNAL_Y = 60
M_DISPARITY_UNIFORM_Y = 61
M_DISPATCH = 2
M_DISPATCH_IMMEDIATE = 3
M_DISPATTRIB_RESERVED = 2305843009213693952
M_DISPLACE_CAMERA_COORD = 256
M_DISPLACE_RELATIVE_COORD = 258
M_DISPLACE_WINDOWS = 10174
M_DISPLAY = 2097152
M_DISPLAYABLE = 30
M_DISPLAYABLE_WITH_CONVERSION = 31
M_DISPLAY_AS_RGB10BIT = 1125899906842624
M_DISPLAY_AS_YUV32 = 36028797018963968
M_DISPLAY_DLL_ERROR_END = 51999
M_DISPLAY_DLL_ERROR_START = 50000
M_DISPLAY_DOUBLE_BUFFERING = 2071
M_DISPLAY_ENABLE = 2
M_DISPLAY_ERROR = 11
M_DISPLAY_ERROR2 = 175
M_DISPLAY_FORMAT = 10112
M_DISPLAY_FORMAT_SUPPORTED = 10113
M_DISPLAY_FRAME_RATE_ON_TITLEBAR = 10212
M_DISPLAY_GRAPHIC_LIST = 10562
M_DISPLAY_INTERLACED = 8
M_DISPLAY_INTERNAL_USE = 2
M_DISPLAY_IS_INTERNALLY_ALLOCATED = 10553
M_DISPLAY_LOCATION = 17
M_DISPLAY_METHOD = 16773120
M_DISPLAY_MODE = 3029
M_DISPLAY_NUMBER_ALLOCATED = 15378
M_DISPLAY_OUTPUT_NUM = 2001
M_DISPLAY_PROGRESSIVE = 4
M_DISPLAY_RESOLUTION = 10107
M_DISPLAY_SCAN_LINE_END = -1
M_DISPLAY_SCAN_LINE_START = 0
M_DISPLAY_SCHEME = 10005
M_DISPLAY_SCHEME_BASE = 10150
M_DISPLAY_SCHEME_CHANGED = 40
M_DISPLAY_SCHEME_COUNT = 10131
M_DISPLAY_SCHEME_ON_TITLEBAR = 10117
M_DISPLAY_SERVICE = 8388614
M_DISPLAY_SUPPORT = 4374
M_DISPLAY_SURFACE = 1121
M_DISPLAY_SYNC = 10047
M_DISPLAY_TYPE = 10114
M_DISPLAY_TYPE_SUPPORTED = 4589
M_DISPLAY_USAGE = 10048
M_DISPLAY_ZOOM_FACTOR_ON_TITLEBAR = 10214
M_DISP_BUFFER_NUMBER_ALLOCATED = 15386
M_DISP_BUF_HOOK = 8388608
M_DISP_CONTROL_DIRECT_STOP = 11000
M_DISP_CONTROL_START = 10000
M_DISP_CTRL_INQ_ERROR = 84
M_DISP_DESELECT_AFTER = 80
M_DISP_DESELECT_BEFORE = 79
M_DISP_EXTERNAL = 4611686018427387904
M_DISP_HOOK_CONTEXT_SIZE = 10
M_DISP_INQUIRE_MIL_ID_END = 1199
M_DISP_INQUIRE_MIL_ID_START = 1100
M_DISP_INQUIRE_SIZEOF_DOUBLE_END = 6699
M_DISP_INQUIRE_SIZEOF_DOUBLE_START = 6600
M_DISP_INQUIRE_SIZEOF_INT64_END = 6799
M_DISP_INQUIRE_SIZEOF_INT64_START = 6700
M_DISP_INQUIRE_STRING_END = 7799
M_DISP_INQUIRE_STRING_START = 7700
M_DISP_INQUIRE_UNKNOWN_SIZEOF_END = 6899
M_DISP_INQUIRE_UNKNOWN_SIZEOF_START = 6800
M_DISP_MESSAGE_ANY = 70
M_DISP_PAN_AFTER = 83
M_DISP_PAN_BEFORE = 82
M_DISP_SELECT_AFTER = 81
M_DISP_SELECT_BEFORE = 86
M_DISP_SERVICE_ERROR = 77
M_DISTANCE = 524288
M_DISTANCE_FROM_BOX_ORIGIN = 1377
M_DISTANCE_FROM_BOX_ORIGIN_SCORE = 274726912
M_DISTANCE_IMAGE_NORMALIZE = 215
M_DISTANCE_IMAGE_SIGN = 344
M_DISTANCE_IMAGE_SIZE_BAND = 343
M_DISTANCE_IMAGE_SIZE_BIT = 342
M_DISTANCE_IMAGE_SIZE_X = 340
M_DISTANCE_IMAGE_SIZE_Y = 341
M_DISTANCE_IMAGE_TYPE = 345
M_DISTANCE_MAX = 18688
M_DISTANCE_MIN = 2
M_DISTANCE_MODE = 2563
M_DISTANCE_PARAM_1 = 221
M_DISTANCE_PARAM_2 = 222
M_DISTANCE_PARAM_3 = 223
M_DISTANCE_PARAM_4 = 224
M_DISTANCE_PARAM_5 = 225
M_DISTANCE_TOLERANCE = 120
M_DISTANCE_TOLERANCE_METHOD = 20
M_DISTANCE_TOLERANCE_MODE = 20
M_DISTANCE_TO_CENTER = 2983
M_DISTANCE_TO_CENTER_AXIS = 3017
M_DISTANCE_TO_CENTER_AXIS_SQUARED = 3034
M_DISTANCE_TO_CENTER_SQUARED = 2984
M_DISTANCE_TO_LINE = 3934
M_DISTANCE_TO_LINE_SQUARED = 3935
M_DISTANCE_TO_MESH = 3543
M_DISTANCE_TO_NEAREST_NEIGHBOR = 3444
M_DISTANCE_TYPE = 1
M_DISTANCE_X = 528384
M_DISTANCE_Y = 532480
M_DISTINCT_ANGLE_DIFFERENCE = 3636
M_DISTORTION_RADIAL_1 = 150
M_DISTRIBUTED_MIL_PROTOCOL = 1055
M_DISTRIBUTED_MIL_REMOTE_COMPUTER_NAME = 7704
M_DISTRIBUTED_MIL_TYPE = 1054
M_DISTRIBUTED_SYSTEM_ON_LOCAL_HOST = 4807
M_DIST_NN_SIGNED_TAG = 512
M_DIST_NN_SIZE_MASK = 127
M_DIST_NN_TAG = 1536
M_DITHERING = 8192
M_DIV = 257
M_DIV_CONST = 33025
M_DMATCH = 32768
M_DMA_ACCESS = 32
M_DMA_DISABLE = 2052
M_DMA_ENABLE = 2051
M_DMA_ERROR = 52
M_DMA_MANAGER_TYPE = 15720
M_DMA_READ_USAGE = 2309
M_DMA_USAGE = 2305
M_DMA_WRITE_UNIT0_USAGE = 2900
M_DMA_WRITE_UNIT1_USAGE = 2901
M_DMA_WRITE_UNIT2_USAGE = 2902
M_DMA_WRITE_UNIT3_USAGE = 2903
M_DMA_WRITE_USAGE = 2305
M_DMILPCIE_TRANSPORT_PROTOCOL = MIL_TEXT("dmilpcie")
M_DMILSHMRT_TRANSPORT_PROTOCOL = MIL_TEXT("dmilshmrt")
M_DMILSHM_TRANSPORT_PROTOCOL = MIL_TEXT("dmilshm")
M_DMILTCP_TRANSPORT_PROTOCOL = MIL_TEXT("dmiltcp")
M_DMIL_AUTO_PUBLISH_ALL = 15519
M_DMIL_CLIENT_CONNECTED = 4
M_DMIL_CLIENT_DISCONNECTED = 5
M_DMIL_CLUSTER_PROTOCOL = MIL_TEXT("dmilcluster")
M_DMIL_CONNECTION = 15518
M_DMIL_CONNECTION_LOST = 134217734
M_DMIL_CONNECTION_PORT = 15517
M_DMIL_CONTROL = 1
M_DMIL_LOCAL_HOST = 1
M_DMIL_MONITOR = 2
M_DMIL_MONITOR_ERROR = 126
M_DMIL_NOT_USED = 0
M_DMIL_PCIE = 5
M_DMIL_PUBLISH = 12
M_DMIL_PUBLISHED_LIST = 1
M_DMIL_PUBLISHED_LIST_SIZE = 2
M_DMIL_PUBLISHED_NAME = 3
M_DMIL_REALLOC_SURFACE = 10571
M_DMIL_REMOTE = 2
M_DMIL_SHM = 4
M_DMIL_SHMRT = 6
M_DMIL_TCPIP = 3
M_DMIL_UNKNOWN_PROTOCOL = 7
M_DMR_CONTEXT = 137975824385
M_DMR_FONT_FILE = 2199
M_DMR_OBJECT = 137975824384
M_DMR_RESULT = 137975824416
M_DMULTIPLE_LINES = 24576
M_DNL = 32
M_DOCR_CALIB = 16384
M_DOCUMENTED_INIT_FLAGS = 16892928
M_DOCUMENT_SCORE = 15
M_DONE_BY_DIRECTX = 1966080
M_DONT_ADD_ALWAYS_LOCAL = 64
M_DONT_CARE = 32768
M_DONT_CONVERT_ID = 1
M_DOTS = 64
M_DOT_DIAMETER = 2229
M_DOT_DIAMETER_MODE = 2228
M_DOT_LONGITUDINAL_DISTANCE = 2242
M_DOT_LONGITUDINAL_DISTANCE_MODE = 2241
M_DOT_MATRIX = 2194
M_DOT_SHAPE = 2999
M_DOT_SIZE = 2997
M_DOT_SPACING_INPUT_UNITS = 32843
M_DOT_SPACING_MAX = 32777
M_DOT_SPACING_MIN = 32776
M_DOT_SPACING_USED = 1656
M_DOT_TRANSVERSE_DISTANCE = 2246
M_DOT_TRANSVERSE_DISTANCE_MODE = 2243
M_DO_INITIAL_COPY = 36
M_DO_SELECT = 10182
M_DP = 8193
M_DPM_CALIBRATION_RESULTS = 1654
M_DPM_FACTOR = 0.0254
M_DQT = 8
M_DQTI = 64
M_DRAWABLE = 1533
M_DRAWDIB_METHOD = 16384
M_DRAWDIB_MODE = 16384
M_DRAW_3D_CONTEXT = 3815
M_DRAW_ABSOLUTE_COORDINATE_SYSTEM = 1445
M_DRAW_ACTIVEMIL_INDEX = 16384
M_DRAW_ACTIVE_EDGELS = 1048576
M_DRAW_ALBEDO_IMAGE = 6
M_DRAW_ALL = 393216
M_DRAW_ALL_EDGELS = 8192
M_DRAW_ANGLE = 27262976
M_DRAW_AREA = 410
M_DRAW_AREA_IMAGE = 410
M_DRAW_AREA_MATCH_USING_COLOR = 404
M_DRAW_AREA_MATCH_USING_LABEL = 403
M_DRAW_AUG_IMAGE = 131072
M_DRAW_AXES = 65536
M_DRAW_AXIS = 512
M_DRAW_BEST_INDEX_CONTOUR_IMAGE = 3356
M_DRAW_BEST_INDEX_IMAGE = 4101
M_DRAW_BEST_SCORE_IMAGE = 4103
M_DRAW_BLOBS = 1024
M_DRAW_BLOBS_CONTOUR = 256
M_DRAW_BOX = 32
M_DRAW_BOX_CENTER = 1
M_DRAW_BOX_MARGIN_X = 801
M_DRAW_BOX_MARGIN_Y = 802
M_DRAW_BUFFER_MASK = 65011712
M_DRAW_CALIBRATION_LINES = 1391
M_DRAW_CALIBRATION_PEAKS = 1678
M_DRAW_CAMERA_COORDINATE_SYSTEM = 3816
M_DRAW_CAMERA_COORDINATE_SYSTEM_NAME = 3865
M_DRAW_CENTER_OF_GRAVITY = 128
M_DRAW_CHAR = 907
M_DRAW_CIRCLE_FIT = 131072
M_DRAW_CLASSIFICATION_SCORE = 4109
M_DRAW_CLASS_COLOR_LUT = 4099
M_DRAW_CLASS_ICON = 3955
M_DRAW_CODE = 128
M_DRAW_COLORED_LABEL_AREA_IMAGE = 404
M_DRAW_COLORED_LABEL_PIXEL_IMAGE = 402
M_DRAW_CONVEX_HULL = 32768
M_DRAW_CONVEX_HULL_CONTOUR = 65536
M_DRAW_COORDINATE_SYSTEM_LENGTH = 3846
M_DRAW_CROSS_DERIVATIVE = 31457280
M_DRAW_CROSS_SIZE = 115
M_DRAW_CS_SHIFT = 16
M_DRAW_DARK_IMAGE = 33554432
M_DRAW_DEAD_PIXELS = 1024
M_DRAW_DECODED_SCANS = 4
M_DRAW_DEPTH_CONFIDENCE_MAP = 4
M_DRAW_DEPTH_INDEX_MAP = 3
M_DRAW_DEPTH_INTENSITY_MAP = 5
M_DRAW_DEPTH_MAP_ROW = 16384
M_DRAW_DIRECTION = 2767
M_DRAW_DISTANCE = 405
M_DRAW_DISTANCE_IMAGE = 405
M_DRAW_DONT_CARE = 8
M_DRAW_EDGE = 4
M_DRAW_EDGELS = 8192
M_DRAW_EDGES = 4
M_DRAW_EDGES_PROFILE = 128
M_DRAW_EDGEVALUE_MIN_IN_PROFILE = 32768
M_DRAW_EDGEVALUE_PEAK_WIDTH_IN_PROFILE = 65536
M_DRAW_EDOF_IMAGE = 2
M_DRAW_ELLIPSE_FIT = 262144
M_DRAW_ERROR_ON_MISSING_CALIBRATION = 64
M_DRAW_EXTENDED_AREA = 8192
M_DRAW_FEATURE = 6
M_DRAW_FERET_BOX = 16
M_DRAW_FERET_GENERAL = 1048576
M_DRAW_FERET_MAX = 8
M_DRAW_FERET_MIN = 4096
M_DRAW_FIDUCIAL_BOX = 2545
M_DRAW_FIRST_DERIVATIVE_X = 6291456
M_DRAW_FIRST_DERIVATIVE_Y = 10485760
M_DRAW_FITTED_EDGELS = 15
M_DRAW_FIXTURING_OFFSET = 1498
M_DRAW_FLAT_IMAGE = 134217728
M_DRAW_FLAT_REGIONS = 16
M_DRAW_FOREGROUND_ON_NON_ZERO_PIXELS = 128
M_DRAW_FOREGROUND_ON_ZERO_PIXELS = 256
M_DRAW_FRAME = 131072
M_DRAW_FRUSTUM = 3819
M_DRAW_FRUSTUM_COLOR = 3838
M_DRAW_GAUSSIAN_CURVATURE_IMAGE = 7
M_DRAW_GEOMETRY = 1357
M_DRAW_GLCM_MATRIX = 1048576
M_DRAW_HDR_FULL_IMAGE = 16
M_DRAW_HDR_IMAGE = 15
M_DRAW_HOLES = 8192
M_DRAW_HOLES_CONTOUR = 16384
M_DRAW_IMAGE = 2
M_DRAW_IMAGE_ORIENTATION = 8192
M_DRAW_IMAGE_POINTS = 1
M_DRAW_INCLUSION_POINT = 16384
M_DRAW_INDEX = 256
M_DRAW_INTENSITY_MAP_ROW = 32768
M_DRAW_IN_BOX = 1048576
M_DRAW_IN_CACHE = 600
M_DRAW_LABEL = 1
M_DRAW_LABEL_AREA_IMAGE = 403
M_DRAW_LABEL_PIXEL_IMAGE = 400
M_DRAW_LASER_LINE_COORDINATE_SYSTEM = 3843
M_DRAW_LASER_PLANE = 3845
M_DRAW_LASER_PLANE_COLOR_FILL = 3905
M_DRAW_LASER_PLANE_COLOR_OUTLINE = 3907
M_DRAW_LASER_PLANE_OPACITY = 3906
M_DRAW_LAST_SIZE_X = 905
M_DRAW_LAST_SIZE_Y = 906
M_DRAW_LEGEND = 327680
M_DRAW_LINE = 2
M_DRAW_LINE_FIT = 512
M_DRAW_LIST = 1022
M_DRAW_LOCAL_CONTRAST_IMAGE = 11
M_DRAW_LOCAL_SHAPE_IMAGE = 9
M_DRAW_MAGNITUDE = 14680064
M_DRAW_MAJOR_MARKS = 196608
M_DRAW_MASK = 2097152
M_DRAW_MAX_IMAGE = 14
M_DRAW_MEAN_CURVATURE_IMAGE = 8
M_DRAW_MIL_FONT_FORMATTED_STRING = 2715
M_DRAW_MIL_FONT_STRING = 32
M_DRAW_MINOR_MARKS = 262144
M_DRAW_MIN_AREA_BOX = 4
M_DRAW_MIN_IMAGE = 13
M_DRAW_MIN_PERIMETER_BOX = 2
M_DRAW_MODEL = 4096
M_DRAW_NAME = 14
M_DRAW_NOISY_EDGELS = 3006
M_DRAW_NULL_VECTORS = 2
M_DRAW_OFFSET_IMAGE = 67108864
M_DRAW_OFFSET_X = 1205
M_DRAW_OFFSET_Y = 1206
M_DRAW_PATH = 512
M_DRAW_PEAKS = 16777216
M_DRAW_PEAKS_LAST = 1305
M_DRAW_PIXEL_COORDINATE_SYSTEM = 1494
M_DRAW_PIXEL_MATCH_USING_COLOR = 402
M_DRAW_PIXEL_MATCH_USING_LABEL = 400
M_DRAW_POSITION = 64
M_DRAW_POSITION_INDEX = 20
M_DRAW_POSITION_IN_PROFILE = 131072
M_DRAW_POSITION_POLYLINE = 2
M_DRAW_POSITION_VARIATION = 16
M_DRAW_POST_REGISTRATION_IMAGE = 1
M_DRAW_PROFILE_SCALE_OFFSET = 1933
M_DRAW_QUIET_ZONE = 4096
M_DRAW_REFLECTANCE_PROFILE = 2
M_DRAW_REGION = 16
M_DRAW_REGION_INTERPOLATED = 1381
M_DRAW_REGION_INVERTED = 1384
M_DRAW_REGION_MISSING_DATA = 1383
M_DRAW_REGION_UNCALIBRATED = 1382
M_DRAW_REGION_VALID = 1380
M_DRAW_RELATIVE_COORDINATE_SYSTEM = 1446
M_DRAW_RELATIVE_COORDINATE_SYSTEM_NAME = 3866
M_DRAW_RELATIVE_XY_PLANE = 3844
M_DRAW_RELATIVE_XY_PLANE_COLOR_FILL = 3836
M_DRAW_RELATIVE_XY_PLANE_COLOR_OUTLINE = 3903
M_DRAW_RELATIVE_XY_PLANE_OPACITY = 3837
M_DRAW_REMAP_FACTOR_MODE = 3353
M_DRAW_REMAP_FACTOR_VALUE = 3354
M_DRAW_ROBOT_BASE_COORDINATE_SYSTEM = 3817
M_DRAW_SAMPLE = 415
M_DRAW_SAMPLE_COLOR_LUT = 420
M_DRAW_SAMPLE_IMAGE = 415
M_DRAW_SAMPLE_MASK = 416
M_DRAW_SAMPLE_MASK_IMAGE = 416
M_DRAW_SAMPLE_MOSAIC = 1622
M_DRAW_SAMPLE_MOSAIC_DONT_CARE = 1623
M_DRAW_SCAN_PROFILES = 1
M_DRAW_SEARCH_BOX = 6
M_DRAW_SEARCH_DIRECTION = 2048
M_DRAW_SEARCH_REGION = 32
M_DRAW_SEARCH_REGION_CENTER = 1
M_DRAW_SECOND_DERIVATIVE_X = 18874368
M_DRAW_SECOND_DERIVATIVE_Y = 23068672
M_DRAW_SEGMENTS = 2048
M_DRAW_SPACING = 256
M_DRAW_STAT_RESULT = 256
M_DRAW_STRING = 1
M_DRAW_STRING_BOX = 4
M_DRAW_STRING_CHAR_BOX = 8
M_DRAW_STRING_CHAR_POSITION = 16
M_DRAW_STRING_CONTOUR = 2
M_DRAW_SUB_POSITIONS = 1024
M_DRAW_TEMPLATE_REFERENCE = 5
M_DRAW_TEXTURE_IMAGE = 12
M_DRAW_TIE_POINTS = 10
M_DRAW_TOLERANCE = 8
M_DRAW_TOLERANCE_AREA = 4058
M_DRAW_TOLERANCE_FEATURES = 12
M_DRAW_TOOL_COORDINATE_SYSTEM = 3818
M_DRAW_TRAINING_IMAGE = 15
M_DRAW_VALID_REGION = 3
M_DRAW_VALID_REGION_FILLED = 4
M_DRAW_VALUE = 32768
M_DRAW_VERTICES = 1024
M_DRAW_WAVELET = 65536
M_DRAW_WAVELET_WITH_PADDING = 2048
M_DRAW_WEIGHT_REGIONS = 256
M_DRAW_WIDTH = 8
M_DRAW_WIDTH_VARIATION = 512
M_DRAW_WITH_NO_RESULT = 2683
M_DRAW_WORLD_BOX = 131072
M_DRAW_WORLD_BOX_CENTER = 262144
M_DRAW_WORLD_FERET_X = 524288
M_DRAW_WORLD_FERET_Y = 1048576
M_DRAW_WORLD_POINTS = 2
M_DRAW_ZOOM_X = 1203
M_DRAW_ZOOM_Y = 1204
M_DRI = 4
M_DRIVER_ASYNC_CALL = 1060
M_DRIVER_ASYNC_CALL_BW = 1038
M_DRIVER_ASYNC_CALL_CANCELLED = 268435456
M_DRIVER_ASYNC_CALL_END = 134217728
M_DRIVER_COMPILATION_TYPE = 4362
M_DRIVER_ERROR_PENDING = 1073741824
M_DRIVER_FPGA_CONTEXT_SIZE = 4801
M_DRIVER_HOOK_CONTEXT = 1610612738
M_DRIVER_HOOK_CONTEXT_ID = 25
M_DRIVER_HOOK_CONTEXT_PTR = 1900544
M_DRIVER_HOOK_CONTEXT_REMOTE_ID = 1170
M_DRIVER_HOOK_CONTEXT_REMOTE_ID_END = 1189
M_DRIVER_ID = 1107
M_DRIVER_INFO_PTR = 2
M_DRIVER_IS_CALLED_INTERNALLY = 15059
M_DRIVER_METHOD = 33554432
M_DRIVER_MODE = 33554432
M_DRIVER_OBSOLETE = 40
M_DRIVER_RESET_HOOK_CONTEXT_ID = 67108864
M_DROP_COLUMN = 3966
M_DSAVE_IMGS = 4096
M_DSAVE_INFO = 8192
M_DSKEW = 20480
M_DUAL_DISP_DX_APP_RANGE_END = 9499
M_DUAL_DISP_DX_APP_RANGE_START = 9400
M_DUAL_HEAD = 15320
M_DUAL_SCREEN = 16384
M_DUAL_ZOOM = 3197
M_DUAL_ZOOM_SUPPORTED = 3198
M_DUMMY_SYS_INQUIRE = 7401
M_DUMP_ALL_ID_INFO = 15954
M_DUMP_ID_TABLE = 15951
M_DUMP_REGISTERS = 5189
M_DVI = 1048576
M_DVI_1 = 1
M_DVI_2 = 32
M_DVI_3 = 64
M_DVI_4 = 128
M_DXF_FILE = 512
M_DX_SURFACE_RESTORED = 20
M_DYADIC = 1825
M_DYNAMIC = 2
M_DYNAMIC_BUFFER_CHANGED = 37
M_DYNAMIC_TEXTURE = 72057594037927936
M_D_FORWARD = 16388
M_D_REVERSE = 16404
M_E1200 = 74240
M_E1200H = 78336
M_E1200HM = 77312
M_E1200HMR = 1125888
M_E1200HR = 1126912
M_E1200R = 1122816
M_E300 = 12800
M_E300C = 13056
M_E300CR = 1061632
M_E300H = 13824
M_E300HM = 15872
M_E300HMR = 1064448
M_E300HR = 1062400
M_E300R = 1061376
M_E700 = 29184
M_E700R = 1077760
M_E700W = 29696
M_E700WR = 1078272
M_EAN13 = 4
M_EAN13_NAME = MIL_TEXT("EAN13")
M_EAN14 = 134217737
M_EAN14_NAME = MIL_TEXT("EAN14")
M_EAN8 = 4194304
M_EAN8_NAME = MIL_TEXT("EAN8")
M_EASY_SELECTION = 2771
M_ECC_200 = 7
M_ECC_4STATE = 34
M_ECC_CHECK_DIGIT = 5
M_ECC_COMPOSITE = 28
M_ECC_CORRECTED_NUMBER = 32800
M_ECC_H = 32
M_ECC_L = 29
M_ECC_M = 30
M_ECC_NONE = 4
M_ECC_Q = 31
M_ECC_REED_SOLOMON = 19
M_ECC_REED_SOLOMON_0 = 10
M_ECC_REED_SOLOMON_1 = 11
M_ECC_REED_SOLOMON_2 = 12
M_ECC_REED_SOLOMON_3 = 13
M_ECC_REED_SOLOMON_4 = 14
M_ECC_REED_SOLOMON_5 = 15
M_ECC_REED_SOLOMON_6 = 16
M_ECC_REED_SOLOMON_7 = 17
M_ECC_REED_SOLOMON_8 = 18
M_ECC_UNKNOWN = 6
M_EDGE = 2
M_EDGEL = 4
M_EDGEL_ANGLE = 2578
M_EDGEL_ANGLE_RANGE = 110
M_EDGEL_DENOISING_MODE = 2558
M_EDGEL_DENOISING_RADIUS = 2565
M_EDGEL_DENOISING_USE_ORDER = 3200
M_EDGEL_ORDERING = 3144
M_EDGEL_POSITION_X = 2576
M_EDGEL_POSITION_Y = 2577
M_EDGEL_PROVIDED_ORDER = 3143
M_EDGEL_PRUNING = 3067
M_EDGEL_RELATIVE_ANGLE = 111
M_EDGEL_RESAMPLING_LINE_ANGLE = 3084
M_EDGEL_RESAMPLING_MODE = 3085
M_EDGEL_RESAMPLING_RADIUS = 3086
M_EDGEL_RESAMPLING_USE_ORDER = 3201
M_EDGEL_SELECTION_RANK = 119
M_EDGEL_TYPE = 107
M_EDGEVALUE_MIN = 87040
M_EDGEVALUE_PEAK_CONTRAST = 4096
M_EDGEVALUE_PEAK_CONTRAST_SCORE = 271581184
M_EDGEVALUE_PEAK_POS_MAX = 111616
M_EDGEVALUE_PEAK_POS_MIN = 107520
M_EDGEVALUE_PEAK_WIDTH = 4194304
M_EDGEVALUE_VAR_MIN = 1711
M_EDGE_CONTEXT = 671088642
M_EDGE_CONTOUR = 671088641
M_EDGE_CONTRAST = 8
M_EDGE_CONTRAST_SCORE = 272629760
M_EDGE_CREST = 671088642
M_EDGE_DETECT = 9437191
M_EDGE_DETECT2 = 9437192
M_EDGE_DETECT_PREWITT_FAST = 9437192
M_EDGE_DETECT_SOBEL_FAST = 9437191
M_EDGE_DETECT_SQR = 9437193
M_EDGE_DETERMINATION_GRADE = 36870
M_EDGE_END = 1713
M_EDGE_FALLING = 13
M_EDGE_FIRST = 536870912
M_EDGE_INSIDE = 128
M_EDGE_INSIDE_SCORE = 277872640
M_EDGE_LIST = 2
M_EDGE_OBJECT = 671088640
M_EDGE_RESULT = 671088644
M_EDGE_RESULT_BUFFER = 671088644
M_EDGE_RISING = 12
M_EDGE_SECOND = 1073741824
M_EDGE_START = 1712
M_EDGE_STRENGTH = 25600
M_EDGE_WIDTH = 4
M_EDITABLE = 1772
M_EDOF_IMAGE_SIZE_X = 1909
M_EDOF_IMAGE_SIZE_Y = 1910
M_EDOF_IMAGE_TYPE = 1912
M_EDOF_STATUS = 1914
M_EEPROM_SIZE = 4369
M_EFFECTIVE_GAIN_CONST = 221
M_EFFECTIVE_SIZE_BIT = 1039
M_EFFECTIVE_VALUE = 16777216
M_ELEMENT_NUMBER_X = 3548
M_ELEMENT_NUMBER_Y = 3549
M_ELEVATION = 49
M_ELLIPSE = 16
M_ELLIPSE_FIT = 97
M_ELLIPSE_FIT_ANGLE = 89
M_ELLIPSE_FIT_CENTER_X = 85
M_ELLIPSE_FIT_CENTER_Y = 86
M_ELLIPSE_FIT_COVERAGE = 96
M_ELLIPSE_FIT_ERROR = 74
M_ELLIPSE_FIT_MAJOR_AXIS = 88
M_ELLIPSE_FIT_MINOR_AXIS = 87
M_ELONGATION = 50
M_EMPTY = 236
M_EMULATED = 1024
M_EMULATED_HOOK_CONTEXT = 1610612752
M_ENABLE = -9997
M_ENABLE_CHAR = 968
M_ENABLE_FOR_ALL_FUNCTIONS = 7
M_ENABLE_ON_MOUSE_CLICK = 3973
M_ENCODER = 1025
M_ENCODER_BRIGHTNESS = 1040
M_ENCODER_CLOCK = 1048
M_ENCODER_CONTRAST = 1039
M_ENCODER_END = 1048
M_ENCODER_FILTER = 1030
M_ENCODER_HUE = 1042
M_ENCODER_INFO_MODE = 1032
M_ENCODER_MODE = 1026
M_ENCODER_OVR_BUF_ID = 1045
M_ENCODER_OVR_LUT = 1044
M_ENCODER_OVR_SHOW = 1043
M_ENCODER_PEDESTAL = 1029
M_ENCODER_PRESENT = 2138
M_ENCODER_RESET = 1033
M_ENCODER_RGB_SYNC = 1031
M_ENCODER_SATURATION = 1041
M_ENCODER_SELECT_FIELD_EVEN = 1038
M_ENCODER_SELECT_FIELD_ODD = 1037
M_ENCODER_START = 1025
M_ENCODER_STATE = 1025
M_ENCODER_SYNC = 1028
M_ENCODER_SYNC_FIELDS = 1047
M_ENCODER_SYNC_LOCK = 1028
M_ENCODER_SYNC_SOURCE = 1028
M_ENCODER_TYPE = 1027
M_ENCODING = 32773
M_ENCODING_START = 60
M_ENC_ALPHA = 1
M_ENC_ALPHANUM = 3
M_ENC_ALPHANUM_PUNC = 2
M_ENC_ASCII = 4
M_ENC_AUSTRALIA_MAIL_C = 17
M_ENC_AUSTRALIA_MAIL_N = 18
M_ENC_AUSTRALIA_MAIL_RAW = 16
M_ENC_AZTEC_COMPACT = 24
M_ENC_AZTEC_FULL_RANGE = 25
M_ENC_AZTEC_RUNE = 26
M_ENC_EAN13 = 32
M_ENC_EAN13_ADDON = 22
M_ENC_EAN8 = 64
M_ENC_EAN8_ADDON = 23
M_ENC_GS1_128_MICROPDF417 = 131072
M_ENC_GS1_128_PDF417 = 512
M_ENC_GS1_DATABAR_EXPANDED = 8192
M_ENC_GS1_DATABAR_EXPANDED_STACKED = 65536
M_ENC_GS1_DATABAR_LIMITED = 4096
M_ENC_GS1_DATABAR_OMNI = 1024
M_ENC_GS1_DATABAR_STACKED = 16384
M_ENC_GS1_DATABAR_STACKED_OMNI = 32768
M_ENC_GS1_DATABAR_TRUNCATED = 2048
M_ENC_ISO8 = 5
M_ENC_KOREA_MAIL = 19
M_ENC_MODE2 = 6
M_ENC_MODE3 = 7
M_ENC_MODE4 = 8
M_ENC_MODE5 = 9
M_ENC_MODE6 = 10
M_ENC_NUM = 0
M_ENC_QRCODE_MODEL1 = 2097152
M_ENC_QRCODE_MODEL2 = 4194304
M_ENC_STANDARD = 11
M_ENC_UK_MAIL = 15
M_ENC_UPCA = 128
M_ENC_UPCA_ADDON = 20
M_ENC_UPCE = 256
M_ENC_UPCE_ADDON = 21
M_ENC_US_MAIL = 14
M_END = -2
M_END_IN_HOST_MEMORY = 128
M_END_IN_VIDEO_MEMORY = 32
M_END_OF_LIST = 67108864
M_END_OF_PROCESSING = 1
M_END_OF_TRANSFER_SIGNAL = 140
M_END_OF_TRANSFER_SIGNAL0 = 140
M_END_OF_TRANSFER_SIGNAL1 = 141
M_END_OF_TRANSFER_SIGNAL2 = 142
M_END_OF_TRANSFER_SIGNAL3 = 143
M_END_POINT_X = 3661
M_END_POINT_Y = 3662
M_END_POINT_Z = 3663
M_END_POS_X = 2822
M_END_POS_Y = 2823
M_END_RADIUS_X = 2798
M_END_RADIUS_Y = 2799
M_END_REGISTER_ADDRESS = 4043309055
M_ENHANCED = 1
M_ENHANCED_BUFFER = 9017
M_ENHANCE_DOT_CHARS = 84
M_ENHANCE_FORMAT = 9003
M_ENHANCE_FROM_ID = 9008
M_ENHANCE_GRAB_CREATE = 9015
M_ENHANCE_MAX_DISPLAY_FORMAT = 9009
M_ENHANCE_MORPHO = 43
M_ENHANCE_SYSTEM_CREATE = 9014
M_ENLARGE_CHAR_THICKNESS = 84
M_ENTRIES = 3571
M_ENTROPY = 3533
M_ENTRY_ADD = 3474
M_ENTRY_DELETE = 3477
M_ENTRY_DELETE_ALL = 3784
M_ENTRY_DELETE_BY_KEY = 3573
M_ENTRY_INDEX = 3653
M_ENTRY_KEY = 3575
M_ENTRY_USER_STRING = 3649
M_ENTRY_WEIGHT = 3576
M_ENUM_PCI_VIDDEV_MEMORY_RANGE = 15343
M_EPH_MARKERS = 8222
M_EPOCH_INDEX = 3678
M_EPOCH_TRAINED = 65025
M_EQUAL = 3
M_EQUAL_CHAIN = 64
M_EQUAL_CONST = 32771
M_EQUAL_PASS_MAX = -4067
M_EQUAL_PASS_MIN = -4066
M_EQUAL_THRESHOLD_HIGH = -3079
M_ERASE_BORDER_BLOBS = 2
M_ERODE = 1
M_ERROR = 1073741824
M_ERRORS = 1
M_ERROR_ACCESS_DENIED = 32774
M_ERROR_ASYNCHRONOUS_LOG = 2081
M_ERROR_BAD_ALIGNMENT = 32773
M_ERROR_BUSY = 32775
M_ERROR_CLEAR = 2099
M_ERROR_CODE_PTR = 15038
M_ERROR_CONTEXT = 67108864
M_ERROR_CORRECTION = 32772
M_ERROR_CURRENT = 1073741826
M_ERROR_DATA_OVERRUN = 32781
M_ERROR_FATAL = 1075118080
M_ERROR_FUNCTION_NAME_SIZE = 32
M_ERROR_GENERIC_ERROR = 36863
M_ERROR_GLOBAL = 1073741832
M_ERROR_HANDLER_PTR = 15019
M_ERROR_HANDLER_USER_PTR = 15020
M_ERROR_HOOKS = 15022
M_ERROR_INVALID_ADDRESS = 32771
M_ERROR_INVALID_HEADER = 32782
M_ERROR_INVALID_PARAMETER = 32770
M_ERROR_INVALID_PROTOCOL = 32778
M_ERROR_LOCAL_PROBLEM = 32776
M_ERROR_MESSAGE_SIZE = 320
M_ERROR_MINIMIZATION_METRIC = 1946
M_ERROR_MSG_MISMATCH = 32777
M_ERROR_NOT_IMPLEMENTED = 32769
M_ERROR_NO_MSG = 32779
M_ERROR_PACKET_AND_PREV_REMOVED_FROM_MEMORY = 32785
M_ERROR_PACKET_NOT_YET_AVAILABLE = 32784
M_ERROR_PACKET_REMOVED_FROM_MEMORY = 32786
M_ERROR_PACKET_UNAVAILABLE = 32780
M_ERROR_POP = 15062
M_ERROR_REMOTE = 16
M_ERROR_REMOTE_CURRENT = 1073741842
M_ERROR_TITLE = 256
M_ERROR_UNUSED_BITS = 182517488
M_ERROR_WRITE_PROTECTED = 32772
M_ERROR_WRONG_CONFIG = 32783
M_ESCAPE_SEQUENCE = 16
M_ESTIMATE_GEOMETRY = 3607
M_ESTIMATION_MODE = 3600
M_EUCLIDEAN = 2
M_EUCLIDEAN_SQR = 22
M_EULER = 2054
M_EULER_NUMBER = 47
M_EVALUATE = 33554432
M_EVEN = 2
M_EVENT = 128
M_EVENT_ALLOC = 1700
M_EVENT_CONTEXT = 2048
M_EVENT_CONTROL = 1703
M_EVENT_CREATE = 512
M_EVENT_FREE = 1701
M_EVENT_LIST = 32768
M_EVENT_MODE = 1709
M_EVENT_SEND = 1702
M_EVENT_SET = 1707
M_EVENT_STATE = 1706
M_EVENT_SYNCHRONIZE = 134217728
M_EVENT_SYNCRONIZE_ALL = 201326592
M_EVENT_TYPE = 4259840
M_EVENT_VALUE = 8
M_EVENT_VALUE_1 = 1
M_EVENT_VALUE_2 = 2
M_EVENT_VALUE_3 = 8
M_EVENT_VALUE_4 = 7
M_EVENT_WAIT = 536870912
M_EVENT_WAIT_ALL = 603979776
M_EVEN_FIELD = 2
M_EVEN_ODD = 2
M_EXACT_IN_DOUBLE = -2147483648
M_EXCLUDE = 2
M_EXCLUDED = 272
M_EXCLUDED_BLOBS = 536870912
M_EXCLUDED_EDGES = 8388608
M_EXCLUDE_FOR_ANY_ADJUSTMENT = 262144
M_EXCLUDE_FOR_INTERSECTION = 524288
M_EXCLUDE_FOR_SYSTEM_SELECTION = 1048576
M_EXCLUDE_FOR_TYPE_ADJUSTMENT = 2097152
M_EXCLUDE_INVALID_POINTS = 67108864
M_EXCLUDE_ONLY = 258
M_EXCLUSIVE = 1024
M_EXCLUSIVE_BANDWIDTH = 268435456
M_EXCLUSIVE_MODE = 10058
M_EXCLUSIVE_MONITOR_RANK = 9254
M_EXCLUSIVE_ON_LAST_MONITOR = 15402
M_EXECUTE_BUFFER_HOOKS = 1002
M_EXECUTING_ON_SUPERSIGHT_MASTER = 15119
M_EXP = 266
M_EXPECTED_OUTLIER_PERCENTAGE = 3606
M_EXPIRATION_DATE = 15727
M_EXPIRY_DATE_STRING = 2990
M_EXPONENTIAL = 2
M_EXPOSURE = 90
M_EXPOSURE_AUTO = 5104
M_EXPOSURE_DELAY = 6654
M_EXPOSURE_DELAY2 = 6660
M_EXPOSURE_END = 200
M_EXPOSURE_GAIN = 70
M_EXPOSURE_MODE = 4333
M_EXPOSURE_OFFSET = 71
M_EXPOSURE_OUTPUT_INVERTER = 4459
M_EXPOSURE_START = 100
M_EXPOSURE_TIME = 6652
M_EXPOSURE_TIME2 = 6659
M_EXPOSURE_TIME_MAX = 6653
M_EXPOSURE_TIME_MAX_FOR_BUFFER = 6612
M_EXP_CONST = 264
M_EXTENDED_AREA_BOTTOM_LEFT_X = 1032
M_EXTENDED_AREA_BOTTOM_LEFT_Y = 1033
M_EXTENDED_AREA_BOTTOM_RIGHT_X = 1034
M_EXTENDED_AREA_BOTTOM_RIGHT_Y = 1035
M_EXTENDED_AREA_CODEWORD_MODULATION = 41034
M_EXTENDED_AREA_CODEWORD_MODULATION_GRADE = 36957
M_EXTENDED_AREA_FIXED_PATTERN_DAMAGE_A1_GRADE = 36967
M_EXTENDED_AREA_FIXED_PATTERN_DAMAGE_A2_GRADE = 36968
M_EXTENDED_AREA_FIXED_PATTERN_DAMAGE_A3_GRADE = 36969
M_EXTENDED_AREA_FIXED_PATTERN_DAMAGE_AVERAGE_GRADE = 36966
M_EXTENDED_AREA_FIXED_PATTERN_DAMAGE_A_GRADE = 36975
M_EXTENDED_AREA_FIXED_PATTERN_DAMAGE_B1_GRADE = 36970
M_EXTENDED_AREA_FIXED_PATTERN_DAMAGE_B2_GRADE = 36971
M_EXTENDED_AREA_FIXED_PATTERN_DAMAGE_B_GRADE = 36976
M_EXTENDED_AREA_FIXED_PATTERN_DAMAGE_CLOCKTRACK_SOLID_GRADE = 36965
M_EXTENDED_AREA_FIXED_PATTERN_DAMAGE_C_GRADE = 36972
M_EXTENDED_AREA_FIXED_PATTERN_DAMAGE_GRADE = 36960
M_EXTENDED_AREA_FIXED_PATTERN_DAMAGE_L1_GRADE = 36961
M_EXTENDED_AREA_FIXED_PATTERN_DAMAGE_L2_GRADE = 36962
M_EXTENDED_AREA_FIXED_PATTERN_DAMAGE_QZL1_GRADE = 36963
M_EXTENDED_AREA_FIXED_PATTERN_DAMAGE_QZL2_GRADE = 36964
M_EXTENDED_AREA_MODULATION_GRADE = 36958
M_EXTENDED_AREA_QUIET_ZONE_INCLUDED = 45067
M_EXTENDED_AREA_REFLECTANCE_CHECK = 1657
M_EXTENDED_AREA_REFLECTANCE_MAXIMUM = 41036
M_EXTENDED_AREA_REFLECTANCE_MINIMUM = 41035
M_EXTENDED_AREA_SYMBOL_CONTRAST = 41037
M_EXTENDED_AREA_SYMBOL_CONTRAST_GRADE = 36959
M_EXTENDED_AREA_TOP_LEFT_X = 1028
M_EXTENDED_AREA_TOP_LEFT_Y = 1029
M_EXTENDED_AREA_TOP_RIGHT_X = 1030
M_EXTENDED_AREA_TOP_RIGHT_Y = 1031
M_EXTENDED_ATTRIBUTE = 6703
M_EXTENDED_ATTRIBUTE_NAME = 6901
M_EXTENDED_CONTEXT_TYPE_DEPRECATED = 10
M_EXTENDED_DEPTH_OF_FIELD = 2
M_EXTENDED_DEPTH_OF_FIELD_RESULT = 2
M_EXTENDED_DISPLAY_SCHEME = 6700
M_EXTENDED_DISPLAY_TYPE = 10115
M_EXTENDED_FORMAT = 6702
M_EXTENDED_FORMAT_NAME = 6900
M_EXTENDED_INIT_FLAG = 6705
M_EXTENDED_INTERSECTION = 66
M_EXTENDED_PARAM_TYPE = 268435456
M_EXTENDED_RESULT_TYPE = 11
M_EXTENT_BOX = 3466
M_EXTERNAL = 262144
M_EXTERNAL_BUFFER_ID = 9043
M_EXTERNAL_CHROMINANCE = 4137
M_EXTERNAL_DISPLAY_NUMBER = 9210
M_EXTERNAL_FEATURE = 68
M_EXTERNAL_LL_MD_ID = 9044
M_EXTERNAL_VIDEO_DEVICE_OBJECT = 1099511627778
M_EXTERN_DISPLAY_AVAILABLE = 9256
M_EXTERN_DISPLAY_SUPPORTED_FORMAT = 9259
M_EXTERN_UNDERLAY_AVAILABLE = 9260
M_EXTRACT = 262144
M_EXTRACTING_FEATURES = 4
M_EXTRACTION_BOX = 1
M_EXTRACTION_BOX_CENTER_X = 1981
M_EXTRACTION_BOX_CENTER_Y = 1982
M_EXTRACTION_BOX_CENTER_Z = 1983
M_EXTRACTION_BOX_DEFINED = 1974
M_EXTRACTION_BOX_MAX_X = 1978
M_EXTRACTION_BOX_MAX_Y = 1979
M_EXTRACTION_BOX_MAX_Z = 1980
M_EXTRACTION_BOX_MIN_X = 1975
M_EXTRACTION_BOX_MIN_Y = 1976
M_EXTRACTION_BOX_MIN_Z = 1977
M_EXTRACTION_BOX_MODEL = 2084
M_EXTRACTION_BOX_SCENE = 2085
M_EXTRACTION_BOX_SIZE_X = 1984
M_EXTRACTION_BOX_SIZE_Y = 1985
M_EXTRACTION_BOX_SIZE_Z = 1986
M_EXTRACTION_CHILD_OFFSET_X = 1308
M_EXTRACTION_CHILD_OFFSET_Y = 1309
M_EXTRACTION_CUMULATIVE = 1311
M_EXTRACTION_FIXED_POINT = 1310
M_EXTRACTION_OVERLAP = 1860
M_EXTRACTION_RANGE_Z = 1913
M_EXTRACTION_RANGE_Z_LIMIT1 = 1904
M_EXTRACTION_RANGE_Z_LIMIT2 = 1905
M_EXTRACTION_SATURATION = 1859
M_EXTRACTION_SCALE = 58
M_EXTRACTION_SCALE_MODE = 1312
M_EXTRACT_DIFFERENCE_EDGELS = 3076
M_EXTRACT_HOLES = 4
M_EXTRACT_LINE = 1338
M_EXTRACT_LUT_X = 2
M_EXTRACT_LUT_Y = 4
M_EXTRACT_MODELS = 1021
M_EXTRA_CANDIDATES = 46
M_EXTRA_CHARACTERS = 115
M_EXTREME = 3393
M_EXTREME_LIST = 65536
M_E_FORWARD = 16389
M_E_REVERSE = 16405
M_FAIL = 4
M_FAILED_IMAGES_ID = 2574
M_FAILED_IMAGES_INDEX = 2582
M_FAILED_NUMBER_OF_IMAGES = 2572
M_FAILURE = 1
M_FAILURE_BAD_TRANSFORM_PARAM = 1
M_FAILURE_CALCULATE_MATH_EXCEPTION = 5
M_FAILURE_CODE = 20
M_FAILURE_HINT_MATH_EXCEPTION = 4
M_FAILURE_IMAGE_NO_INFO = 7
M_FAILURE_IMAGE_TOO_SMALL = 6
M_FAILURE_MESSAGE = 21
M_FAILURE_MESSAGE_LENGTH = 22
M_FAILURE_NOT_FOUND = 3
M_FAILURE_NO_CONVERGENCE = 8
M_FAILURE_TOO_MANY_ELEMENTS = 2
M_FAIL_GAPS = 3676
M_FAIL_GAP_MAX = 9
M_FAIL_INTENSITY_MAX = 13
M_FAIL_INTENSITY_MIN = 12
M_FAIL_INVALID_MESH = 3675
M_FAIL_NOT_FOUND = 11
M_FAIL_OFFSET = 10
M_FAIL_WARNING_OFFSET = 99
M_FAIL_WIDTH_MAX = 8
M_FAIL_WIDTH_MIN = 7
M_FALSE = 0
M_FAST = 8192
M_FAST_ANGLE = 4
M_FAST_EDGE_DETECT = 12
M_FAST_FIND = 34
M_FAST_GRADIENT = 8
M_FAST_LENGTH = 52
M_FAST_MEMORY = 68719476736
M_FAST_MEMORY_FREE = 2325
M_FAST_MEM_TO_VGA = 2080
M_FAST_OVERSCAN = 32768
M_FAST_OVERSCAN_BUFFER = 32768
M_FAST_PHASE = 2048
M_FAST_PREVIEW = 8
M_FAST_SELECT = 10209
M_FAST_UNDERLAY_MODE = 10210
M_FATAL = 1376256
M_FATAL_ERROR_HANDLER_PTR = 15012
M_FATAL_ERROR_HANDLER_USER_PTR = 15013
M_FB_WEB_OFFSET = 3
M_FCNET_COLOR_XL = 536870917
M_FCNET_M = 536870914
M_FCNET_MONO_XL = 536870916
M_FCNET_S = 536870913
M_FCNET_XL = 536870915
M_FEATURE_ACCESS_MODE = 458752
M_FEATURE_BASED = 8192
M_FEATURE_BROWSER_ERROR = 193
M_FEATURE_CACHING_MODE = 589824
M_FEATURE_CACHING_MODE_NONE = 1
M_FEATURE_CACHING_MODE_WRITE_AROUND = 3
M_FEATURE_CACHING_MODE_WRITE_THROUGH = 2
M_FEATURE_CHANGE = 26
M_FEATURE_CHANGE_HOOK = 917504
M_FEATURE_DEPRECATED = 720896
M_FEATURE_DESCRIPTION = 393216
M_FEATURE_DISPLAY_NAME = 196608
M_FEATURE_ENUM_ENTRY = 144115188075855872
M_FEATURE_ENUM_ENTRY_ACCESS_MODE = 144115188076314624
M_FEATURE_ENUM_ENTRY_CACHING_MODE = 144115188076445696
M_FEATURE_ENUM_ENTRY_COUNT = 144115188075921408
M_FEATURE_ENUM_ENTRY_DESCRIPTION = 144115188076249088
M_FEATURE_ENUM_ENTRY_DISPLAY_NAME = 144115188076052480
M_FEATURE_ENUM_ENTRY_INDEX_MASK = 65535
M_FEATURE_ENUM_ENTRY_NAME = 144115188075986944
M_FEATURE_ENUM_ENTRY_STREAMABLE = 144115188076511232
M_FEATURE_ENUM_ENTRY_TOOLTIP = 144115188076183552
M_FEATURE_ENUM_ENTRY_VALUE = 144115188092239872
M_FEATURE_ENUM_ENTRY_VISIBILITY = 144115188076380160
M_FEATURE_ENUM_MASK = 1080863910568919040
M_FEATURE_EXECUTE = 16515072
M_FEATURE_EXECUTE_COMPLETED = 16515072
M_FEATURE_GEOMETRY = 903
M_FEATURE_IMPORTANCE = 3534
M_FEATURE_IMPORTANCE_MODE = 3613
M_FEATURE_IMPORTANCE_SET = 3703
M_FEATURE_INCREMENT = 16711680
M_FEATURE_INDEX_MASK = 65535
M_FEATURE_INDEX_TAG = 33554432
M_FEATURE_LABEL_TAG = 16777216
M_FEATURE_LABEL_VALUE = 1
M_FEATURE_MAX = 16646144
M_FEATURE_MIN = 16580608
M_FEATURE_NAME = 131072
M_FEATURE_NOT_AVAILABLE = 2
M_FEATURE_NOT_IMPLEMENTED = 1
M_FEATURE_OP_MASK = 16711680
M_FEATURE_ORDER = 2536
M_FEATURE_POLLING_INTERVAL = 983040
M_FEATURE_PRESENT = 851968
M_FEATURE_PROPERTY_MASK = 16711680
M_FEATURE_READ_ONLY = 4
M_FEATURE_READ_WRITE = 5
M_FEATURE_REPRESENTATION = 786432
M_FEATURE_REPRESENTATION_BOOLEAN = 3
M_FEATURE_REPRESENTATION_HEX_NUMBER = 5
M_FEATURE_REPRESENTATION_IPV4_ADDRESS = 6
M_FEATURE_REPRESENTATION_LINEAR = 1
M_FEATURE_REPRESENTATION_LOGARITHMIC = 2
M_FEATURE_REPRESENTATION_MAC_ADDRESS = 7
M_FEATURE_REPRESENTATION_PURE_NUMBER = 4
M_FEATURE_SELECTOR = 216172782113783808
M_FEATURE_SELECTOR_COUNT = 216172782113849344
M_FEATURE_SELECTOR_INDEX_MASK = 65535
M_FEATURE_SELECTOR_NAME = 216172782113914880
M_FEATURE_SIZE = 4294967296
M_FEATURE_STREAMABLE = 655360
M_FEATURE_TOOLTIP = 327680
M_FEATURE_TYPE = 262144
M_FEATURE_UNIT = 1048576
M_FEATURE_USER_ARRAY_SIZE_BITS = 6597069766656
M_FEATURE_USER_ARRAY_SIZE_MASK = 2147483647
M_FEATURE_USER_ARRAY_SIZE_SHIFT = 0
M_FEATURE_VALID_VALUE = 288230376168095744
M_FEATURE_VALID_VALUE_COUNT = 288230376151777280
M_FEATURE_VALID_VALUE_INDEX_MASK = 65535
M_FEATURE_VALID_VALUE_LIST = 288230376151711744
M_FEATURE_VALUE = 16384000
M_FEATURE_VALUE_AS_STRING = 16449536
M_FEATURE_VALUE_AS_STRING_INTERNAL = 16449536
M_FEATURE_VISIBILITY = 524288
M_FEATURE_VISIBILITY_BEGINNER = 1
M_FEATURE_VISIBILITY_EXPERT = 2
M_FEATURE_VISIBILITY_GURU = 3
M_FEATURE_VISIBILITY_INVISIBLE = 4
M_FEATURE_WRITE_ONLY = 3
M_FEET = 2455
M_FERETS = 2476
M_FERET_ANGLE_SEARCH_END = 92
M_FERET_ANGLE_SEARCH_START = 90
M_FERET_AT_ANGLE = 4136
M_FERET_AT_PRINCIPAL_AXIS_ANGLE = 119
M_FERET_AT_SECONDARY_AXIS_ANGLE = 120
M_FERET_BOX = 69
M_FERET_CONTACT_POINTS = 196608
M_FERET_CONTACT_POINTS_X1 = 327680
M_FERET_CONTACT_POINTS_X2 = 458752
M_FERET_CONTACT_POINTS_Y1 = 393216
M_FERET_CONTACT_POINTS_Y2 = 524288
M_FERET_DIAMETERS = 122
M_FERET_ELONGATION = 27
M_FERET_GENERAL = 1024
M_FERET_GENERAL_ANGLE = 62
M_FERET_MAX_ANGLE = 17
M_FERET_MAX_DIAMETER = 16
M_FERET_MAX_DIAMETER_ELONGATION = 126
M_FERET_MEAN_DIAMETER = 18
M_FERET_MIN_ANGLE = 15
M_FERET_MIN_DIAMETER = 14
M_FERET_MIN_DIAMETER_ELONGATION = 125
M_FERET_PERPENDICULAR_TO_MAX_DIAMETER = 124
M_FERET_PERPENDICULAR_TO_MIN_DIAMETER = 123
M_FERET_PRINCIPAL_AXIS_ELONGATION = 121
M_FERET_X = 72
M_FERET_Y = 5
M_FFT = 1
M_FIELD = 1835008
M_FIELD_ORDER = 5083
M_FIELD_START = 20
M_FIELD_START_EVEN = 22
M_FIELD_START_EVEN_HANDLER_PTR = 4050
M_FIELD_START_EVEN_HANDLER_USER_PTR = 4051
M_FIELD_START_HANDLER_PTR = 4046
M_FIELD_START_HANDLER_USER_PTR = 4047
M_FIELD_START_HOOK_WHEN_GRAB_ONLY = 4129
M_FIELD_START_ODD = 21
M_FIELD_START_ODD_HANDLER_PTR = 4048
M_FIELD_START_ODD_HANDLER_USER_PTR = 4049
M_FIELD_START_THREAD_HANDLE = 4083
M_FIELD_START_THREAD_ID = 4080
M_FIELD_UPDATE_MODE = 5079
M_FILE = 25
M_FILE_COPY = 768
M_FILE_COPY_MIL_DLL = 1024
M_FILE_COPY_MIL_USER_DLL = 2560
M_FILE_DELETE = 512
M_FILE_DELETE_DIR = 1536
M_FILE_DISPATCH = 1792
M_FILE_ERROR = 31
M_FILE_EXECUTE = 257
M_FILE_EXISTS = 2048
M_FILE_EXISTS_MIL_DLL = 2304
M_FILE_EXISTS_MIL_USER_DLL = 2816
M_FILE_FORMAT = 1015
M_FILE_FORMAT_AVI = 32
M_FILE_FORMAT_H264 = 128
M_FILE_FORMAT_MASK = 2097120
M_FILE_FORMAT_MP4 = 96
M_FILE_FORMAT_MPEGTS = 160
M_FILE_FORMAT_RAW = 192
M_FILE_MAKE_DIR = 1280
M_FILE_MOVE = 3072
M_FILE_NAME_FIND = 3584
M_FILE_NAME_FIND_COUNT = 3328
M_FILE_OPERATION_ERROR = 114
M_FILE_OPERATION_ERROR_2 = 115
M_FILE_OPERATION_ERROR_3 = 171
M_FILE_PATH = 3475
M_FILE_PATH_ABS = 3743
M_FILE_READ = 512
M_FILE_SERVER = 1
M_FILE_WRITE = 1024
M_FILLED = 128
M_FILL_BORDER = 3050
M_FILL_COLOR = 10193
M_FILL_DESTINATION = -1
M_FILL_DISPLAY = 10574
M_FILL_GAPS_CONTEXT = 3759
M_FILL_GAP_ANGLE = 45
M_FILL_GAP_CANDIDATE = 91
M_FILL_GAP_CONTINUITY = 38
M_FILL_GAP_DISTANCE = 44
M_FILL_GAP_MODE = 4
M_FILL_GAP_POLARITY = 46
M_FILL_HOLES = 3
M_FILL_MISSING_DATA_ONLY = 1342
M_FILL_MODE = 3
M_FILL_REGION = 524288
M_FILL_SHARP_ELEVATION = 4
M_FILL_SHARP_ELEVATION_DEPTH = 5
M_FILL_SOURCE = 512
M_FILL_THRESHOLD_X = 1674
M_FILL_THRESHOLD_Y = 1675
M_FILTER_ASPECT_RATIO = 2846
M_FILTER_DEFAULT_SHARPEN_PARAM = 4056
M_FILTER_FORWARD_HIGH_PASS_ID = 1822
M_FILTER_FORWARD_LOW_PASS_ID = 1820
M_FILTER_MODE = 122
M_FILTER_OPERATION = 57
M_FILTER_POWER = 1049
M_FILTER_RESPONSE_TYPE = 2843
M_FILTER_REVERSE_HIGH_PASS_ID = 1823
M_FILTER_REVERSE_LOW_PASS_ID = 1821
M_FILTER_SMOOTHNESS = 108
M_FILTER_SMOOTHNESS_TYPE = 2842
M_FILTER_TYPE = 1046
M_FINAL_GRAB = -9998
M_FIND = 2
M_FINDER_PATTERN_BASE = 2
M_FINDER_PATTERN_DEFECTS = 41048
M_FINDER_PATTERN_EXHAUSTIVE_SEARCH = 1685
M_FINDER_PATTERN_INPUT_UNITS = 1679
M_FINDER_PATTERN_MAX_GAP = 1683
M_FINDER_PATTERN_MINIMUM_LENGTH = 1684
M_FIND_ALL_MODELS = 268435456
M_FIND_BEST_MODELS = 1
M_FIND_ORIENTATION_CONTEXT = 11
M_FIND_ORIENTATION_LIST = 8796093022208
M_FINE_TUNING = 3626
M_FINISHED = 1
M_FINITE = 3016
M_FIRMWARE_BUILDDATE = 2345
M_FIRMWARE_BUILDDATE_GRAB = 2346
M_FIRMWARE_BUILDDATE_IO = 2347
M_FIRMWARE_BUILDDATE_JPEG2000 = 2348
M_FIRMWARE_BUILDDATE_PROCESSING = 2348
M_FIRMWARE_FILE_INDEX = 2367
M_FIRMWARE_REVISION = 2155
M_FIRMWARE_REVISION_GRAB = 2342
M_FIRMWARE_REVISION_IO = 2343
M_FIRMWARE_REVISION_JPEG2000 = 2344
M_FIRMWARE_REVISION_PROCESSING = 2344
M_FIRMWARE_UPDATE = 2340
M_FIRST = 268435456
M_FIRST_DERIVATIVES_ID = 98304
M_FIRST_DERIVATIVE_X = 9437194
M_FIRST_DERIVATIVE_X_ID = 65536
M_FIRST_DERIVATIVE_Y = 9437195
M_FIRST_DERIVATIVE_Y_ID = 32768
M_FIRST_FERET_INDEX = 640
M_FIRST_FIELD = 4
M_FIRST_FRAME = 1073741825
M_FIRST_GRAY = 16384
M_FIRST_IMAGE = 2
M_FIRST_LEVEL = 31
M_FIRST_MIL_BUFFER = 262144
M_FIRST_PARAM_TYPE = 1
M_FIRST_PERCENTILE = 3481
M_FIRST_POINT = 207
M_FIRST_POINT_X = 75
M_FIRST_POINT_Y = 132
M_FIRST_TIMER_MODE = 65536
M_FIRST_VIDEO_DEVICE_ON_DESKTOP = 15340
M_FIT = 32
M_FITTED_EDGELS = 2
M_FITTED_GEOMETRY = 3559
M_FIT_ALL_ANGLE = 256
M_FIT_CONTEXT = 3646
M_FIT_COVERAGE_MIN = 112
M_FIT_DISTANCE_MAX = 101
M_FIT_DISTANCE_OUTLIERS = 3030
M_FIT_DISTANCE_OUTLIERS_VALUE = 3031
M_FIT_ERROR = 5888
M_FIT_ERROR_MAX = 1378
M_FIT_ERROR_WEIGHTING_FACTOR = 221
M_FIT_INTERNAL_NUMBER_OF_POINTS = 2587
M_FIT_ITERATIONS_MAX = 104
M_FIT_PARAM_AX = 1322
M_FIT_PARAM_AY = 1325
M_FIT_PARAM_RADIUS = 1327
M_FIT_PARAM_SIGN = 1331
M_FIT_PARAM_X0 = 1328
M_FIT_PARAM_Y0 = 1329
M_FIT_PARAM_Z0 = 1330
M_FIT_POINT_CLOUD = 3038
M_FIT_RESULT = 3645
M_FIT_RMS_ERROR = 1333
M_FIT_SCALES = 1366
M_FIT_SCORE_MIN = 2458
M_FIT_SRC_DATA = 2
M_FIT_SRC_RANGE = 1
M_FIT_TYPE = 3065
M_FIT_VARIATION_MAX = 113
M_FIXED = 80
M_FIXED_ASPECT_RATIO = 65536
M_FIXED_CENTER = 2689
M_FIXED_CORNER = 2690
M_FIXED_LENGTH_ARROWHEADS = 4
M_FIXED_PATTERN_DAMAGE_A1_GRADE = 36947
M_FIXED_PATTERN_DAMAGE_A2_GRADE = 36948
M_FIXED_PATTERN_DAMAGE_A3_GRADE = 36949
M_FIXED_PATTERN_DAMAGE_AVERAGE_GRADE = 36946
M_FIXED_PATTERN_DAMAGE_A_GRADE = 36973
M_FIXED_PATTERN_DAMAGE_B1_GRADE = 36950
M_FIXED_PATTERN_DAMAGE_B2_GRADE = 36951
M_FIXED_PATTERN_DAMAGE_B_GRADE = 36974
M_FIXED_PATTERN_DAMAGE_CLOCKTRACK_SOLID_GRADE = 36945
M_FIXED_PATTERN_DAMAGE_C_GRADE = 36952
M_FIXED_PATTERN_DAMAGE_GRADE = 36933
M_FIXED_PATTERN_DAMAGE_L1_GRADE = 36941
M_FIXED_PATTERN_DAMAGE_L2_GRADE = 36942
M_FIXED_PATTERN_DAMAGE_QZL1_GRADE = 36943
M_FIXED_PATTERN_DAMAGE_QZL2_GRADE = 36944
M_FIXED_POINT = 16384
M_FIXED_SPACING = 2260
M_FIXTURE = 1771
M_FIXTURE_TO_GEOMETRY = 21
M_FIXTURE_TO_PLANE = 20
M_FIXTURING_MATRIX = 3878
M_FIXTURING_OFFSET = 1369
M_FIX_ERRORS = 536870912
M_FIX_PATTERN_NOISE_CORRECTION = 4332
M_FLAGS = 8453
M_FLAT = 4699
M_FLAT_CONST = 205
M_FLAT_FIELD_CONTEXT = 3
M_FLAT_IMAGE = 202
M_FLAT_IMAGE_HEIGHT = 219
M_FLAT_IMAGE_NB_BANDS = 217
M_FLAT_IMAGE_TYPE = 220
M_FLAT_IMAGE_WIDTH = 218
M_FLAT_REGIONS = 501
M_FLAT_SURFACE = 4894
M_FLEXIBLE = 536870912
M_FLIP = 65536
M_FLIP_BUFFERS_SUPPORT = 15139
M_FLIP_HORIZONTAL = 2
M_FLIP_MODE = 5040
M_FLIP_ONLY = 2055
M_FLIP_VERTICAL = 1
M_FLOAT = 1207959552
M_FLOAT_MODE = 70
M_FLOAT_PROC = 1073741824
M_FOCAL_LENGTH = 1009
M_FOCUS = 5132
M_FOCUS_DEPTH_SIZE = 2193
M_FOCUS_LENGTH = 5137
M_FOCUS_PERSISTENCE = 5134
M_FOCUS_PERSISTENT_VALUE = 5135
M_FOCUS_TEMPERATURE = 6613
M_FOCUS_WAIT = 5133
M_FOLLOW_CORE_MAX = 262144
M_FOLLOW_TIMER_CLOCK = -3
M_FONT = 7
M_FONTLESS = 16384
M_FONT_ADD = 702
M_FONT_ASCII = 16384
M_FONT_AUTO_SELECT = 16777316
M_FONT_BASED = 8192
M_FONT_DEFAULT = 1
M_FONT_DEFAULT_LARGE = 3
M_FONT_DEFAULT_MEDIUM = 2
M_FONT_DEFAULT_SMALL = 1
M_FONT_DEFAULT_TTF = MIL_TEXT("MILFont")
M_FONT_DELETE = 703
M_FONT_DPI = 16777318
M_FONT_ERROR = 106
M_FONT_FILENAME = 16777315
M_FONT_INDEX_FLAG = 8388608
M_FONT_INDEX_FROM_LABEL = 231
M_FONT_INDEX_VALUE = 2226
M_FONT_INIT_FLAG = 41
M_FONT_LABEL_FLAG = 0
M_FONT_LABEL_VALUE = 2216
M_FONT_MASK = 8388608
M_FONT_MIL = 32768
M_FONT_SIZE = 16777312
M_FONT_SIZE_COLUMNS = 2207
M_FONT_SIZE_ROWS = 2208
M_FONT_SIZE_TEMPLATE = 2222
M_FONT_TTF = 4
M_FONT_TYPE = 31
M_FONT_USER_LABEL = 229
M_FONT_X_SCALE = 8
M_FONT_Y_SCALE = 9
M_FORCE = -9998
M_FORCED_LOCAL_DISPLAY_CONTROL = 268435456
M_FORCED_REMOTE_DISPLAY_CONTROL = 134217728
M_FORCE_ASPECT_RATIO_1 = 8
M_FORCE_DISABLE = 2
M_FORCE_DISPLAY_RESOLUTION = 10033
M_FORCE_DISPLAY_SCHEME_CHANGE = 10134
M_FORCE_INTERNAL_GRAB_BUFFER = 5320
M_FORCE_MONO_OVR = 10007
M_FORCE_PITCH_BYTE_MULTIPLE = 4367
M_FORCE_PSEUDO_LIVE_GRAB = 4329
M_FORCE_THREAD_DETACH = 15046
M_FOREGROUND_ANY = 384
M_FOREGROUND_BLACK = 256
M_FOREGROUND_BLACK_OR_WHITE = 512
M_FOREGROUND_VALUE = 4
M_FOREGROUND_WHITE = 128
M_FOREGROUND_ZERO = 2
M_FOREVER = -1
M_FORMAT = 7701
M_FORMAT7_TILE_SIZE_X = 5190
M_FORMAT7_TILE_SIZE_Y = 5191
M_FORMATTED_STRING = 793
M_FORMATTED_STRING_ALLOC_SIZE_BYTE = 592
M_FORMATTED_STRING_CHAR_NUMBER = 2487
M_FORMATTED_STRING_SIZE = 792
M_FORMAT_CSV = 3572
M_FORMAT_DETECTED = 7710
M_FORMAT_DETECTED_LENGTH = 5497558146590
M_FORMAT_DOT = 3864
M_FORMAT_ERROR = 107
M_FORMAT_INFORMATION_1_GRADE = 36953
M_FORMAT_INFORMATION_2_GRADE = 36954
M_FORMAT_INFORMATION_GRADE = 36936
M_FORMAT_LENGTH = 5497558146581
M_FORMAT_SUPPORTED = 7702
M_FORMAT_SUPPORTED_LENGTH = 5497558146582
M_FORMAT_SUPPORTED_NUM = 5181
M_FORMAT_TXT = 3945
M_FORWARD = 1
M_FORWARD_COEFFICIENTS = 65536
M_FORWARD_DISP_MESSAGES_TO_CLIENT = 3233
M_FORWARD_TRANSFORMATION = 4096
M_FOUND_OFFSET_MAX = 99
M_FOV_HORIZONTAL_ANGLE = 4667
M_FOV_VERTICAL_ANGLE = 4668
M_FPGA_ACCESSIBLE = 72057594037927936
M_FPGA_BASE = 4
M_FPGA_BUILD_NUMBER = 4105
M_FPGA_CMD_CTRL_TYPE_MASK = 268431360
M_FPGA_CONFIG = 4104
M_FPGA_CONFIGURATION = 6400
M_FPGA_CONFIGURATION_FILENAME = 4103
M_FPGA_CONFIGURATION_FILENAME_LENGTH = 4102
M_FPGA_CONTEXT_SHARED_API = 4800
M_FPGA_DESCRIPTION = 7713
M_FPGA_DEVICE_NUMBER = 8448
M_FPGA_DONT_INTERSECT = -2147483648
M_FPGA_ERROR_CODE = 1
M_FPGA_ERROR_DELETE = -2147483648
M_FPGA_ERROR_MESSAGE = 2
M_FPGA_ERROR_SYSTEM = 3
M_FPGA_FLAG_TU_FLAVOR_MASK = 1879048192
M_FPGA_FLAG_TYPE = -268435456
M_FPGA_FLIP_HORIZONTAL = 33554432
M_FPGA_FLIP_VERTICAL = 16777216
M_FPGA_FUNC_MAX_NB_PARAM = 16
M_FPGA_MEMORY = 72057594037927936
M_FPGA_MEMORY_ARBITER_GRANT = 4814
M_FPGA_MULTI_CONTEXT = 805306368
M_FPGA_MULTI_STREAM_PORT = 1073741824
M_FPGA_OVERSCAN = 20480
M_FPGA_OVERSCAN_POSITION_MASK = 3840
M_FPGA_PACKAGE_NAME = 4101
M_FPGA_PACKAGE_NAME_LENGTH = 4100
M_FPGA_RESET = 4803
M_FPGA_REVISION = 2155
M_FPGA_STREAM_INPUT_BIT = 268435456
M_FPGA_STREAM_IO_FILTER = -805306369
M_FPGA_STREAM_IO_MASK = 805306368
M_FPGA_STREAM_OUTPUT_BIT = 536870912
M_FPGA_TU_NUMBER = -1610612736
M_FRACTION_OF_POINTS = 3631
M_FRAME = 30
M_FRAME_AXIS = 1726
M_FRAME_END = 10
M_FRAME_INDEX = 33554432
M_FRAME_ORIGIN = 1648
M_FRAME_RATE = 6002
M_FRAME_RATE_1394 = 5208
M_FRAME_RATE_24 = 110
M_FRAME_RATE_24M = 111
M_FRAME_RATE_25 = 112
M_FRAME_RATE_30 = 113
M_FRAME_RATE_30M = 114
M_FRAME_RATE_50 = 115
M_FRAME_RATE_60 = 116
M_FRAME_RATE_60M = 117
M_FRAME_REFERENCE_AXIS = 1725
M_FRAME_SIZE = 8
M_FRAME_START = 9
M_FRAME_START_HANDLER_PTR = 3020
M_FRAME_START_HANDLER_USER_PTR = 3021
M_FRAME_TRANSFER_END = 6
M_FRAME_TRANSFER_START = 5
M_FRAME_TRIGGER = 2
M_FRAME_TYPE = 8225
M_FREE = 131072
M_FREEDMAN = 3
M_FREE_ALL_DEFAULT = 15025
M_FREE_ALL_SHADOWS = 15746
M_FREE_CLUSTER_NODE = 15723
M_FREE_CUR_APPLICATION = 317
M_FREE_DEFAULT_SHADOWS = 15728
M_FREE_EMPTY_CLUSTER_NODE = 15725
M_FREE_EMPTY_WORKSPACE = 15721
M_FREE_ENHANCED_BUFFER = 9016
M_FREE_REMAINING_TUBES = 15729
M_FREE_WITH_CONTAINER = 2097152
M_FREI_CHEN = 9437193
M_FREQUENCY_CUTOFF_RATIO_HIGH = 1831
M_FREQUENCY_CUTOFF_RATIO_LOW = 1830
M_FROM_ACQUISITION_DRIVER = 4096
M_FROM_DERIVED_GEOMETRY_REGION = 1785
M_FROM_FIDUCIAL = -2
M_FROM_GEOMETRY = 3603
M_FROM_GRAPHIC_LIST = 134217728
M_FROM_HOST_AUX_SERVICE = 8192
M_FROM_REFERENCE = 3589
M_FRONT_VIEW = 4172
M_FULLY_CORRECTED = 1351
M_FULL_CALIBRATION = 257
M_FULL_CORRECTION = 1
M_FULL_EXTENT_BOTTOM_LEFT_X = 1024
M_FULL_EXTENT_BOTTOM_LEFT_Y = 1025
M_FULL_EXTENT_TOP_LEFT_X = 1020
M_FULL_EXTENT_TOP_LEFT_Y = 1021
M_FULL_EXTENT_TOP_RIGHT_X = 1022
M_FULL_EXTENT_TOP_RIGHT_Y = 1023
M_FULL_HYSTERESIS = 25
M_FULL_SCREEN = 1073741824
M_FULL_SIZE = 0
M_FULL_UPDATE = -9998
M_FUNCTION_ID = 8195
M_FUNCTION_NAME = 49
M_FUNCTION_NAME_FROM_OPCODE = 48
M_FUNCTION_NAME_SIZE = 5497558138929
M_FUNCTION_START_ERROR = 28
M_FUNC_CALL_ERROR = 74
M_FUNC_CALL_ERROR_2 = 155
M_FUNC_ERROR = 49000
M_FUNC_FCT_ERROR = 3
M_FUNC_INQUIRE_STRING_END = 105
M_FUNC_INQUIRE_STRING_START = 47
M_FUSION = 1
M_FUSION_COVERAGE = 2807
M_FUSION_HIGH_THRESHOLD = 2806
M_FUSION_IMAGE = 5
M_FUSION_LOW_THRESHOLD = 2805
M_FUSION_MODE = 2804
M_FUTUR_METHODE1 = 3
M_FUTUR_METHODE2 = 4
M_F_FORWARD = 16390
M_F_REVERSE = 16406
M_GAB_CONTEXT = 35184908959745
M_GAB_OBJECT = 35184908959744
M_GAB_RESULT = 35184908959746
M_GAIN = 5124
M_GAIN0 = 65536
M_GAIN1 = 65537
M_GAIN10 = 65546
M_GAIN2 = 65538
M_GAIN3 = 65539
M_GAIN4 = 65540
M_GAIN5 = 65541
M_GAIN6 = 65542
M_GAIN7 = 65543
M_GAIN8 = 65544
M_GAIN9 = 65545
M_GAIN_AUTO_BALANCE = 8006
M_GAIN_CONST = 206
M_GAIN_DIGITAL = 6610
M_GAMMA = 6672
M_GAP_AT_ANGLE = 4135
M_GAP_COVERAGE = 216
M_GAP_MAX_LENGTH = 9
M_GAP_TOLERANCE = 216
M_GARBAGE_UV_ADDRESS = 4283
M_GAUSS = 131072
M_GAUSSIAN = 2053
M_GAUSSIAN_CURVATURE = 2691
M_GC_ACQUISITION_MODE = 6908
M_GC_ACTION0 = 0
M_GC_ACTION1 = 65536
M_GC_ACTION10 = 655360
M_GC_ACTION11 = 720896
M_GC_ACTION12 = 786432
M_GC_ACTION13 = 851968
M_GC_ACTION14 = 917504
M_GC_ACTION15 = 983040
M_GC_ACTION16 = 1048576
M_GC_ACTION17 = 1114112
M_GC_ACTION18 = 1179648
M_GC_ACTION19 = 1245184
M_GC_ACTION2 = 131072
M_GC_ACTION20 = 1310720
M_GC_ACTION21 = 1376256
M_GC_ACTION22 = 1441792
M_GC_ACTION23 = 1507328
M_GC_ACTION24 = 1572864
M_GC_ACTION25 = 1638400
M_GC_ACTION26 = 1703936
M_GC_ACTION27 = 1769472
M_GC_ACTION28 = 1835008
M_GC_ACTION29 = 1900544
M_GC_ACTION3 = 196608
M_GC_ACTION30 = 1966080
M_GC_ACTION31 = 2031616
M_GC_ACTION4 = 262144
M_GC_ACTION5 = 327680
M_GC_ACTION6 = 393216
M_GC_ACTION7 = 458752
M_GC_ACTION8 = 524288
M_GC_ACTION9 = 589824
M_GC_ACTION_ACKNOWLEDGE_NUMBER = 4613
M_GC_ACTION_ADD_DEVICE = 1102
M_GC_ACTION_BASE = 0
M_GC_ACTION_CLEAR_DEVICES = 4615
M_GC_ACTION_DEVICE_KEY = 4610
M_GC_ACTION_EXECUTE = 4614
M_GC_ACTION_GROUP_KEY = 4611
M_GC_ACTION_GROUP_MASK = 4612
M_GC_ACTION_MAX = 2031616
M_GC_ACTION_NUMBER_MASK = 16711680
M_GC_ACTION_REMOVE_DEVICE = 1103
M_GC_ACTION_SHIFT = 16
M_GC_ACTION_SUPPORT = 64
M_GC_ACTION_TIME = 7313
M_GC_ALL_IN_SUPPORT = 4
M_GC_BIG_AND_LITTLE_ENDIAN_SUPPORT = -2147483648
M_GC_BROADCAST_MASTER = 2097152
M_GC_CAMERA_SELECT = 2448
M_GC_CAMERA_TIME_STAMP = 4194304
M_GC_CLPROTOCOL = 6974
M_GC_CLPROTOCOL_DEVICEID_LENGTH = 5497558146610
M_GC_CLPROTOCOL_DEVICEID_SIZE = 5497558146610
M_GC_CLPROTOCOL_DEVICE_ID = 7730
M_GC_CLPROTOCOL_DEVICE_ID_DEFAULT = 7859
M_GC_CLPROTOCOL_DEVICE_ID_NUM = 6975
M_GC_CLPROTOCOL_DEVICE_ID_SIZE_MAX = 6976
M_GC_COMMAND_IN_PACKET_SIZE = 6980
M_GC_COMMAND_OUT_PACKET_SIZE = 6981
M_GC_COMMAND_RETRY = 6903
M_GC_COMMAND_TIMEOUT = 6902
M_GC_CONCATENATION_SUPPORT = 1
M_GC_CONTROL_PROTOCOL_CAPABILITY = 4802
M_GC_COUNTER_TICK_FREQUENCY = 6703
M_GC_DEVICE_IP_ADDRESS = 1
M_GC_DEVICE_NAME = 2
M_GC_DEVICE_USER_NAME = 2
M_GC_DHCP_SUPPORT = 2
M_GC_DISCOVERY_ACK_DELAY_SUPPORT = 16777216
M_GC_DISCOVER_DEVICES = 4810
M_GC_DYNAMIC_LINK_AGGREGATION_SUPPORT = 8
M_GC_ETHERNET_LINK_SPEED = 6909
M_GC_EVENT = 4194304
M_GC_EVENT_DATA = 8388608
M_GC_EVENT_DATA_SIZE = 8519680
M_GC_EVENT_DATA_SUPPORT = 16
M_GC_EVENT_SUPPORT = 8
M_GC_EVENT_TRANSFER_SIZE = 6978
M_GC_EVENT_TYPE = 8454144
M_GC_EXTENDED_CHUNK_DATA_SUPPORT = 1
M_GC_EXTENDED_ID_MODE = 4812
M_GC_EXTENDED_STATUS_CODES_1_SUPPORT = 4194304
M_GC_EXTENDED_STATUS_CODES_2_SUPPORT = 262144
M_GC_FEATURE_BROWSER = 6905
M_GC_FEATURE_BROWSER_HWND = 6922
M_GC_FEATURE_BROWSER_NODES = 7709
M_GC_FEATURE_CHANGE_NAME = 8847360
M_GC_FEATURE_EXECUTE_POLLING_MODE = 4813
M_GC_FEATURE_NODEMAP = 6906
M_GC_FEATURE_NODEMAP_MIL = 6951
M_GC_FEATURE_POLLING = 6973
M_GC_FIREWALL_PRESENT = 6971
M_GC_FIREWALL_TRAVERSAL_SUPPORT = -2147483648
M_GC_FIRMWARE_UPDATE_PROGRESS = 27
M_GC_FRAME_BLOCK_ID = 6963
M_GC_FRAME_BLOCK_ID64 = 6749
M_GC_FRAME_BYTES_RECEIVED = 6964
M_GC_FRAME_ERROR_CODE = 6961
M_GC_FRAME_LINE_COUNT = 6962
M_GC_FRAME_MAX_RETRIES = 6944
M_GC_FRAME_OFFSET_X = 6965
M_GC_FRAME_OFFSET_Y = 6966
M_GC_FRAME_PIXEL_TYPE = 6969
M_GC_FRAME_SIZE_X = 6967
M_GC_FRAME_SIZE_Y = 6968
M_GC_FRAME_STATUS_CODE = 6972
M_GC_FRAME_TIMEOUT = 6948
M_GC_FRAME_TIMESTAMP = 6645
M_GC_GENICAM_UI = 7707
M_GC_GENICAM_VERSION = 7311
M_GC_GET_STREAMABLE_FEATURES = 7712
M_GC_GET_STREAMABLE_FEATURES_LENGTH = 5497558146592
M_GC_HEARTBEAT = 6901
M_GC_HEARTBEAT_DISABLE_SUPPORT = 536870912
M_GC_HEARTBEAT_STATE = 6910
M_GC_HEARTBEAT_TIMEOUT = 6901
M_GC_IEEE_1588 = 4809
M_GC_IEEE_1588_CLOCK_ACCURACY = 4810
M_GC_IEEE_1588_CLOCK_ACCURACY_ALTERNATE_PROFILE = 128
M_GC_IEEE_1588_CLOCK_ACCURACY_GREATER_10S = 49
M_GC_IEEE_1588_CLOCK_ACCURACY_UNKNOWN = 254
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_100MS = 45
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_100NS = 33
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_100US = 39
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_10MS = 43
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_10S = 48
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_10US = 37
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_1MS = 41
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_1S = 47
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_1US = 35
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_250MS = 46
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_250NS = 34
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_250US = 40
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_25MS = 44
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_25NS = 32
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_25US = 38
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_2_5MS = 42
M_GC_IEEE_1588_CLOCK_ACCURACY_WITHIN_2_5US = 36
M_GC_IEEE_1588_STATUS = 4811
M_GC_IEEE_1588_STATUS_DISABLED = 2
M_GC_IEEE_1588_STATUS_FAULTY = 1
M_GC_IEEE_1588_STATUS_INITIALIZING = 0
M_GC_IEEE_1588_STATUS_LISTENING = 3
M_GC_IEEE_1588_STATUS_MASTER = 5
M_GC_IEEE_1588_STATUS_PASSIVE = 6
M_GC_IEEE_1588_STATUS_PREMASTER = 4
M_GC_IEEE_1588_STATUS_SLAVE = 8
M_GC_IEEE_1588_STATUS_UNCALIBRATED = 7
M_GC_IEEE_1588_SUPPORT = 524288
M_GC_INTERFACE_NAME = 7860
M_GC_INTERFACE_NAME_LENGTH = 5497558146740
M_GC_INTER_PACKET_DELAY = 6907
M_GC_IP_ADDRESS = 6702
M_GC_IP_ADDRESS_STRING = 7713
M_GC_IP_REASSEMBLY_SUPPORT = 1073741824
M_GC_LEGACY_16BIT_BLOCK_SUPPORT = 1073741824
M_GC_LINK_LOCAL_ADDRESS_SUPPORT = 4
M_GC_LINK_RESET = 6977
M_GC_LINK_SPEED_REGISTER_SUPPORT = 268435456
M_GC_LOCAL_CONTROL_PORT = 6952
M_GC_LOCAL_IP_ADDRESS = 6739
M_GC_LOCAL_IP_ADDRESS_STRING = 7715
M_GC_LOCAL_IP_ADDRESS_STRING_SIZE = 5497558146595
M_GC_LOCAL_MAC_ADDRESS = 6731
M_GC_LOCAL_MAC_ADDRESS_STRING = 7716
M_GC_LOCAL_MAC_ADDRESS_STRING_SIZE = 5497558146596
M_GC_LOCAL_MESSAGE_PORT = 6936
M_GC_LOCAL_STREAM_PORT = 6912
M_GC_MAC_ADDRESS = 6701
M_GC_MAC_ADDRESS_STRING = 7714
M_GC_MANIFEST_ENTRY_BIT = 536870912
M_GC_MANIFEST_ENTRY_MASK = 15
M_GC_MANIFEST_ENTRY_RESERVED_BITS = 64961380352
M_GC_MANIFEST_ENTRY_SHIFT = 32
M_GC_MANIFEST_TABLE_SUPPORT = 67108864
M_GC_MAX_LEADING_PACKET_MISSED = 6947
M_GC_MAX_NBR_PACKETS_OUT_OF_ORDER = 6943
M_GC_MESSAGE_CHANNEL_MULTICAST_ADDRESS = 6748
M_GC_MESSAGE_CHANNEL_MULTICAST_ADDRESS_STRING = 7718
M_GC_MESSAGE_PORT = 6936
M_GC_MESSAGE_PROTOCOL_CAPABILITY = 4804
M_GC_MULTICAST_MASTER = 4194304
M_GC_MULTICAST_MASTER_CONNECTED = 6942
M_GC_MULTICAST_MONITOR = 16777216
M_GC_MULTICAST_SLAVE = 8388608
M_GC_MULTIPLE_LINK_SUPPORT = 2
M_GC_MULTI_ZONE_SUPPORT = 16
M_GC_NETWORK_INTERFACE_CAPABILITY = 4805
M_GC_NETWORK_INTERFACE_CONFIGURATION = 4808
M_GC_NIC_IP_ADDRESS = 6739
M_GC_NIC_IP_ADDRESS_STRING = 7715
M_GC_NIC_MAC_ADDRESS = 6731
M_GC_NIC_MAC_ADDRESS_STRING = 7716
M_GC_NIC_PORT_COUNT = 1080
M_GC_NODES = 72057594037927936
M_GC_NODE_COUNT = 65536
M_GC_NUMBERED_EVENTS_MASK = 255
M_GC_NUMBER_OF_STREAM_CHANNELS = 6932
M_GC_PACKETS_MISSED = 6957
M_GC_PACKETS_RECEIVED = 6958
M_GC_PACKETS_RECOVERED = 6960
M_GC_PACKETS_RESENDS_NUM = 6959
M_GC_PACKET_MAX_RETRIES = 6946
M_GC_PACKET_MAX_TIMEOUT = 6945
M_GC_PACKET_RESEND = 6911
M_GC_PACKET_RESEND_OPTION_SUPPORT = 8
M_GC_PACKET_RESEND_SUPPORT = 4
M_GC_PACKET_SIZE = 6900
M_GC_PACKET_SIZE_NEGOTIATION_SKIP = 16384
M_GC_PACKET_TIMEOUT = 6949
M_GC_PACKET_TIMEOUT_NUM = 6956
M_GC_PAUSE_GENERATION_SUPPORT = 1073741824
M_GC_PAUSE_RECEPTION_SUPPORT = -2147483648
M_GC_PAYLOAD_SIZE = 5197
M_GC_PENDING_ACK_SUPPORT = 32
M_GC_PERSISTENT_IP_SUPPORT = 1
M_GC_PHYSICAL_LINK_CONFIGURATION_CAPABILITY = 4806
M_GC_PIXEL_FORMAT = 5198
M_GC_PIXEL_FORMAT_STRING = 7878
M_GC_PIXEL_FORMAT_SWITCHING = 6918
M_GC_PORT_AND_IP_REGISTER_SUPPORT = 134217728
M_GC_PRIMARY_APP_SWITCHOVER_SUPPORT = 2097152
M_GC_READ_MEMORY = 6916
M_GC_READ_REGISTER = 6914
M_GC_REMOTE_CONTROL_PORT = 6953
M_GC_REMOTE_IP_ADDRESS = 6702
M_GC_REMOTE_IP_ADDRESS_STRING = 7713
M_GC_REMOTE_IP_ADDRESS_STRING_SIZE = 5497558146593
M_GC_REMOTE_MAC_ADDRESS = 6701
M_GC_REMOTE_MAC_ADDRESS_STRING = 7714
M_GC_REMOTE_MAC_ADDRESS_STRING_SIZE = 5497558146594
M_GC_REMOTE_MESSAGE_PORT = 6955
M_GC_REMOTE_STREAM_PORT = 6954
M_GC_SCHEDULED_ACTION_SUPPORT = 131072
M_GC_SCHEMA_MAJOR = 6937
M_GC_SCHEMA_MINOR = 6938
M_GC_SERIAL_NUMBER = 7708
M_GC_SERIAL_NUMBER_LENGTH = 5497558146588
M_GC_SERIAL_NUMBER_SUPPORT = 1073741824
M_GC_SINGLE_LINK_SUPPORT = 1
M_GC_SPECIFIC_INFO = 7706
M_GC_SPECIFIC_INFO_LENGTH = 5497558146586
M_GC_STATIC_LINK_AGGREGATION_SUPPORT = 4
M_GC_STATISTICS_RESET = 6970
M_GC_STREAMING_MODE = 4133
M_GC_STREAMING_START = 6931
M_GC_STREAMING_STOP = 6928
M_GC_STREAMING_STOP_CHECK_PERIOD = 6929
M_GC_STREAMING_STOP_DELAY = 6930
M_GC_STREAMING_TRANSFER_SIZE = 6979
M_GC_STREAM_CHANNEL_CAPABILITY = 4807
M_GC_STREAM_CHANNEL_MULTICAST_ADDRESS = 6747
M_GC_STREAM_CHANNEL_MULTICAST_ADDRESS_STRING = 7717
M_GC_STREAM_PORT = 6912
M_GC_STREAM_PROTOCOL_CAPABILITY = 4803
M_GC_TEST_DATA_SUPPORT = 33554432
M_GC_THEORETICAL_INTER_PACKET_DELAY = 6609
M_GC_TOTAL_BYTES_RECEIVED = 6704
M_GC_TOTAL_FRAMES_CORRUPTED = 6708
M_GC_TOTAL_FRAMES_GRABBED = 6707
M_GC_TOTAL_FRAMES_MISSED = 6717
M_GC_TOTAL_FRAME_CACHE_HITS = 6716
M_GC_TOTAL_PACKETS_MISSED = 6709
M_GC_TOTAL_PACKETS_NOT_COPIED = 6718
M_GC_TOTAL_PACKETS_RECEIVED = 6710
M_GC_TOTAL_PACKETS_RECEIVED_OUT_OF_ORDER = 6714
M_GC_TOTAL_PACKETS_RECOVERED = 6712
M_GC_TOTAL_PACKETS_RESENDS_NUM = 6711
M_GC_TOTAL_PACKETS_TIMEOUT = 6713
M_GC_TOTAL_PACKET_CACHE_HITS = 6715
M_GC_TRIGGER_SELECTOR = 7714
M_GC_TRIGGER_SOFTWARE0 = 8388608
M_GC_TRIGGER_SOFTWARE1 = 8454144
M_GC_TRIGGER_SOFTWARE10 = 9043968
M_GC_TRIGGER_SOFTWARE11 = 9109504
M_GC_TRIGGER_SOFTWARE12 = 9175040
M_GC_TRIGGER_SOFTWARE13 = 9240576
M_GC_TRIGGER_SOFTWARE14 = 9306112
M_GC_TRIGGER_SOFTWARE15 = 9371648
M_GC_TRIGGER_SOFTWARE16 = 9437184
M_GC_TRIGGER_SOFTWARE17 = 9502720
M_GC_TRIGGER_SOFTWARE18 = 9568256
M_GC_TRIGGER_SOFTWARE19 = 9633792
M_GC_TRIGGER_SOFTWARE2 = 8519680
M_GC_TRIGGER_SOFTWARE20 = 9699328
M_GC_TRIGGER_SOFTWARE21 = 9764864
M_GC_TRIGGER_SOFTWARE22 = 9830400
M_GC_TRIGGER_SOFTWARE23 = 9895936
M_GC_TRIGGER_SOFTWARE24 = 9961472
M_GC_TRIGGER_SOFTWARE25 = 10027008
M_GC_TRIGGER_SOFTWARE26 = 10092544
M_GC_TRIGGER_SOFTWARE27 = 10158080
M_GC_TRIGGER_SOFTWARE28 = 10223616
M_GC_TRIGGER_SOFTWARE29 = 10289152
M_GC_TRIGGER_SOFTWARE3 = 8585216
M_GC_TRIGGER_SOFTWARE30 = 10354688
M_GC_TRIGGER_SOFTWARE31 = 10420224
M_GC_TRIGGER_SOFTWARE4 = 8650752
M_GC_TRIGGER_SOFTWARE5 = 8716288
M_GC_TRIGGER_SOFTWARE6 = 8781824
M_GC_TRIGGER_SOFTWARE7 = 8847360
M_GC_TRIGGER_SOFTWARE8 = 8912896
M_GC_TRIGGER_SOFTWARE9 = 8978432
M_GC_TRIGGER_SOFTWARE_BASE = 128
M_GC_TRIGGER_SOFTWARE_MAX = 10420224
M_GC_TRIGGER_SOFTWARE_NUMBER_MASK = 16711680
M_GC_TRIGGER_SOFTWARE_SHIFT = 16
M_GC_UNCONDITIONAL_ACTION_SUPPORT = 1048576
M_GC_UNCONDITIONAL_STREAMING_SUPPORT = 2
M_GC_UNIQUE_ID_STRING = 7714
M_GC_UPDATE_MULTICAST_INFO = 4134
M_GC_USER_DEFINED_NAME_SUPPORT = -2147483648
M_GC_USER_NAME = 7707
M_GC_USER_NAME_LENGTH = 5497558146587
M_GC_VERSION = 7705
M_GC_VERSION_LENGTH = 5497558146585
M_GC_WRITABLE_DISCOVERY_ACK_DELAY_SUPPORT = 8388608
M_GC_WRITE_MEMORY = 6917
M_GC_WRITE_MEM_SUPPORT = 2
M_GC_WRITE_REGISTER = 6915
M_GC_XML_DOWNLOAD_SKIP = 128
M_GC_XML_FORCE_DOWNLOAD = 64
M_GC_XML_MAJOR = 6939
M_GC_XML_MINOR = 6940
M_GC_XML_PATH = 7861
M_GC_XML_PATH_LENGTH = 5497558146741
M_GC_XML_SUBMINOR = 6941
M_GC_XML_TYPE = 8912896
M_GDI = 4294967296
M_GDI_COMPATIBLE_OVERLAY = 10013
M_GDI_OVERLAY = 536870912
M_GEN1 = 1
M_GEN2 = 2
M_GEN3 = 3
M_GENDC = 1048576
M_GENDC_CONTAINER_DESCRIPTOR_POINTER = 5109
M_GENDC_ERROR = 56206
M_GENDC_ERROR_2 = 56209
M_GENERAL = 536870912
M_GENERALIZATION = 1484
M_GENERATE_BEEP = 15142
M_GENERATE_CAPS_FILE = 15345
M_GENERATE_DISTANCE_IMAGE = 310
M_GENERATE_LABEL_PIXEL_IMAGE = 300
M_GENERATE_PENDING_HOOKS = 10049
M_GENERATE_PIXEL_MATCH = 300
M_GENERATE_SAMPLE_COLOR_LUT = 305
M_GENICAM_AVAILABLE = 1079
M_GENICAM_INTERACTIVE_MODAL_DIALOG = 15
M_GENICAM_INTERACTIVE_MODELESS_DIALOG = 16
M_GENTL = 210
M_GENTL_ANNOUNCE_BUFFER = 1103
M_GENTL_BUFFER = 167772160
M_GENTL_DEVICE = 50331648
M_GENTL_DEVICE_COUNT = 2182
M_GENTL_DISCOVERY_TIMEOUT = 4819
M_GENTL_INTERFACE = 33554432
M_GENTL_INTERFACE0 = 33554432
M_GENTL_INTERFACE1 = 68753031168
M_GENTL_INTERFACE10 = 687228321792
M_GENTL_INTERFACE11 = 755947798528
M_GENTL_INTERFACE12 = 824667275264
M_GENTL_INTERFACE13 = 893386752000
M_GENTL_INTERFACE14 = 962106228736
M_GENTL_INTERFACE15 = 1030825705472
M_GENTL_INTERFACE16 = 17592219598848
M_GENTL_INTERFACE17 = 17660939075584
M_GENTL_INTERFACE18 = 17729658552320
M_GENTL_INTERFACE19 = 17798378029056
M_GENTL_INTERFACE2 = 137472507904
M_GENTL_INTERFACE20 = 17867097505792
M_GENTL_INTERFACE21 = 17935816982528
M_GENTL_INTERFACE22 = 18004536459264
M_GENTL_INTERFACE23 = 18073255936000
M_GENTL_INTERFACE24 = 18141975412736
M_GENTL_INTERFACE25 = 18210694889472
M_GENTL_INTERFACE26 = 18279414366208
M_GENTL_INTERFACE27 = 18348133842944
M_GENTL_INTERFACE28 = 18416853319680
M_GENTL_INTERFACE29 = 18485572796416
M_GENTL_INTERFACE3 = 206191984640
M_GENTL_INTERFACE30 = 18554292273152
M_GENTL_INTERFACE31 = 18623011749888
M_GENTL_INTERFACE4 = 274911461376
M_GENTL_INTERFACE5 = 343630938112
M_GENTL_INTERFACE6 = 412350414848
M_GENTL_INTERFACE7 = 481069891584
M_GENTL_INTERFACE8 = 549789368320
M_GENTL_INTERFACE9 = 618508845056
M_GENTL_INTERFACE_COUNT = 2181
M_GENTL_INTERFACE_INDEX = 2105
M_GENTL_PRODUCER_BIT = 2147483648
M_GENTL_PRODUCER_COUNT = 15064
M_GENTL_PRODUCER_DESCRIPTION = 22192
M_GENTL_PRODUCER_DESCRIPTION_SIZE = 5497558161072
M_GENTL_PRODUCER_DESCRIPTOR = 22192
M_GENTL_PRODUCER_DESCRIPTOR_SIZE = 5497558161072
M_GENTL_PRODUCER_MASK = 2130706432
M_GENTL_PRODUCER_SHIFT = 24
M_GENTL_REMOTE_DEVICE = 134217728
M_GENTL_REVOKE_BUFFER = 1104
M_GENTL_STREAM = 150994944
M_GENTL_STREAM0 = 150994944
M_GENTL_STREAM1 = 68870471680
M_GENTL_STREAM10 = 687345762304
M_GENTL_STREAM11 = 756065239040
M_GENTL_STREAM12 = 824784715776
M_GENTL_STREAM13 = 893504192512
M_GENTL_STREAM14 = 962223669248
M_GENTL_STREAM15 = 1030943145984
M_GENTL_STREAM16 = 17592337039360
M_GENTL_STREAM17 = 17661056516096
M_GENTL_STREAM18 = 17729775992832
M_GENTL_STREAM19 = 17798495469568
M_GENTL_STREAM2 = 137589948416
M_GENTL_STREAM20 = 17867214946304
M_GENTL_STREAM21 = 17935934423040
M_GENTL_STREAM22 = 18004653899776
M_GENTL_STREAM23 = 18073373376512
M_GENTL_STREAM24 = 18142092853248
M_GENTL_STREAM25 = 18210812329984
M_GENTL_STREAM26 = 18279531806720
M_GENTL_STREAM27 = 18348251283456
M_GENTL_STREAM28 = 18416970760192
M_GENTL_STREAM29 = 18485690236928
M_GENTL_STREAM3 = 206309425152
M_GENTL_STREAM30 = 18554409713664
M_GENTL_STREAM31 = 18623129190400
M_GENTL_STREAM4 = 275028901888
M_GENTL_STREAM5 = 343748378624
M_GENTL_STREAM6 = 412467855360
M_GENTL_STREAM7 = 481187332096
M_GENTL_STREAM8 = 549906808832
M_GENTL_STREAM9 = 618626285568
M_GENTL_STREAM_COUNT = 2106
M_GENTL_SYSTEM = 16777216
M_GENTL_XML_INDEX_MASK = 18622978195456
M_GENTL_XML_INDEX_MASK_LOWER = 1030792151040
M_GENTL_XML_INDEX_MASK_UPPER = 17592186044416
M_GENTL_XML_INDEX_SHIFT_LOWER = 36
M_GENTL_XML_INDEX_SHIFT_UPPER = 40
M_GENTL_XML_TYPE_MASK = 251658240
M_GEOMETRIC = 8192
M_GEOMETRIC_CONTROLLED = 32768
M_GEOMETRY = 1306
M_GEOMETRY_CENTER = 3794
M_GEOMETRY_DEFINITION_TYPE = 1332
M_GEOMETRY_TYPE = 1321
M_GET_CALIBRATION_ID = 4
M_GET_CALIBRATION_INFO = 1
M_GET_COLOR_2D_END = 33
M_GET_EDGELS = 1
M_GET_END = 32
M_GET_FEATURE_INDEX = 5
M_GET_FEATURE_LABEL = 3
M_GET_FONT_INDEX = 2203
M_GET_FONT_LABEL = 2201
M_GET_NAME = 2
M_GET_STRING_INDEX = 2204
M_GET_STRING_LABEL = 2202
M_GET_SUBEDGELS = 2
M_GET_TOLERANCE_INDEX = 6
M_GET_TOLERANCE_LABEL = 4
M_GEV = 256
M_GIGE_VISION = 180
M_GINI = 3532
M_GLCM_PAIR_OFFSET_X = 2151
M_GLCM_PAIR_OFFSET_Y = 2152
M_GLCM_QUANTIFICATION = 2161
M_GLCM_STAT_TYPE = 2150
M_GLOBAL = 8
M_GLOBAL_AVERAGE_PIXEL_ERROR = 4097
M_GLOBAL_AVERAGE_WORLD_ERROR = 16388
M_GLOBAL_ERROR_HANDLER_PTR = 15010
M_GLOBAL_ERROR_HANDLER_USER_PTR = 15011
M_GLOBAL_FCT = 589824
M_GLOBAL_FRAME = 285212672
M_GLOBAL_MAX = 1885
M_GLOBAL_MAXIMUM_PIXEL_ERROR = 8194
M_GLOBAL_MAXIMUM_WORLD_ERROR = 32776
M_GLOBAL_MEAN_VARIANCE = 1481
M_GLOBAL_MIN = 1886
M_GLOBAL_OFFSET = 1888
M_GLOBAL_OFFSET_SECOND_PASS = 1890
M_GLOBAL_OPTIMIZATION_ERROR = 1879
M_GLOBAL_SEGMENTATION = 21
M_GLOBAL_SUB = 720896
M_GLOBAL_SUB_1 = 720896
M_GLOBAL_SUB_2 = 786432
M_GLOBAL_SUB_3 = 851968
M_GLOBAL_SUB_NB = 655360
M_GLOBAL_WITH_LOCAL_RESEGMENTATION = 4096
M_GOOD_LOCATION_QUALITY_FLAG = 8
M_GOURAUD = 4700
M_GPU = 190
M_GPU_ACCESS = 16
M_GPU_ACCESS_ONLY = 1053
M_GPU_BILINEAR_SUPPORT = 4392
M_GPU_BILINEAR_SUPPORTED = 15342
M_GPU_ERROR = 113
M_GPU_ERROR_D3D10_NOTLOADED = 1812
M_GPU_ERROR_D3D11_NOTLOADED = 1813
M_GPU_ERROR_D3D9_NOTLOADED = 1811
M_GPU_ERROR_DIRECTX_NOTSUPPORTED = 1809
M_GPU_ERROR_END = 1818
M_GPU_ERROR_INVALID_DECODER = 1810
M_GPU_ERROR_START = 1808
M_GPU_ERROR_WINDOWS_SERVICE = 1814
M_GPU_IS_16_BIT_PRECISE = 2179
M_GPU_IS_NON_POWER_OF_2_FULLY_SUPPORTED = 2177
M_GPU_IS_TEXTURE_BORDER_SUPPORTED = 2178
M_GPU_NO_TEARING_AVAILABLE = 15334
M_GPU_NO_TEARING_SUPPORT = 4391
M_GPU_SERIES = 2180
M_GPU_TRAIN_ENGINE_LOAD_STATUS = 4110
M_GPU_TYPE = 7700
M_GPU_UPDATE_EFFECTS = 1022
M_GRAB = 8
M_GRAB_15_BITS_SUPPORTED = 4069
M_GRAB_16_BITS_SUPPORTED = 4226
M_GRAB_24_BITS_SUPPORTED = 4227
M_GRAB_32_BITS_SUPPORTED = 4070
M_GRAB_8_BITS_SUPPORTED = 4068
M_GRAB_ABORT = 6643
M_GRAB_ATTRIBUTE = 4800
M_GRAB_AUTOMATIC_INPUT_GAIN = 4242
M_GRAB_BLOCK_FACTOR = 2442
M_GRAB_BLOCK_SIZE = 4229
M_GRAB_BUFFERS = 5095
M_GRAB_BUFFERS_AFTER_SET_SCHEME = 5238
M_GRAB_BUFFERS_AFTER_SET_SCHEME_NO_LOCK = 5276
M_GRAB_BUFFERS_NO_LOCK = 5096
M_GRAB_BUFFERS_USED = 5277
M_GRAB_BUF_MODIFIED = 4372
M_GRAB_BY_DISPLAY_CAPTURE = 2043
M_GRAB_COLOR = 4325
M_GRAB_CONTINUOUS_END_TRIGGER = 2038
M_GRAB_CONTINUOUS_ERROR = 4801
M_GRAB_CONTINUOUS_ONLY = 1048576
M_GRAB_CONTROL_OFFLOAD = 4390
M_GRAB_DESTRUCTIVE_IN_PROGRESS = 4073
M_GRAB_DIRECTION_X = 4230
M_GRAB_DIRECTION_Y = 4231
M_GRAB_DISPLAY_SCALER_QUALITY = 4243
M_GRAB_DUAL_PHASE = 5230
M_GRAB_END = 3
M_GRAB_END_HANDLER_PTR = 4030
M_GRAB_END_HANDLER_USER_PTR = 4032
M_GRAB_END_HOOK = 4330
M_GRAB_END_THREAD_HANDLE = 4237
M_GRAB_END_THREAD_ID = 4238
M_GRAB_END_WAITS_FOR_HOOK_FUNCTION = 4428
M_GRAB_ERROR_CHECK_PIXEL = 8001
M_GRAB_ERROR_CHECK_SYNC = 8002
M_GRAB_ERROR_COUNT = 8005
M_GRAB_ERROR_HALT_GRAB = 8000
M_GRAB_ERROR_RESET = 8003
M_GRAB_ERROR_STATUS = 8004
M_GRAB_EXPOSURE_END = 200
M_GRAB_EXPOSURE_START = 100
M_GRAB_EXTENDED_DATA = 143360
M_GRAB_EXTRA_LINE = 4071
M_GRAB_FAIL_CHECK = 4120
M_GRAB_FAIL_RETRY_NUMBER = 4122
M_GRAB_FAIL_STATUS = 4121
M_GRAB_FIELD_END = 8
M_GRAB_FIELD_END_EVEN = 7
M_GRAB_FIELD_END_EVEN_HANDLER_PTR = 4040
M_GRAB_FIELD_END_EVEN_HANDLER_USER_PTR = 4041
M_GRAB_FIELD_END_EVEN_THREAD_HANDLE = 4085
M_GRAB_FIELD_END_EVEN_THREAD_ID = 4082
M_GRAB_FIELD_END_HANDLER_PTR = 4036
M_GRAB_FIELD_END_HANDLER_USER_PTR = 4037
M_GRAB_FIELD_END_ODD = 6
M_GRAB_FIELD_END_ODD_HANDLER_PTR = 4038
M_GRAB_FIELD_END_ODD_HANDLER_USER_PTR = 4039
M_GRAB_FIELD_END_ODD_THREAD_HANDLE = 4084
M_GRAB_FIELD_END_ODD_THREAD_ID = 4081
M_GRAB_FIELD_END_THREAD_HANDLE = 4259
M_GRAB_FIELD_END_THREAD_ID = 4260
M_GRAB_FIELD_NUM = 4018
M_GRAB_FIELD_START = 14
M_GRAB_FIELD_START_EVEN = 16
M_GRAB_FIELD_START_EVEN_HANDLER_PTR = 4224
M_GRAB_FIELD_START_EVEN_HANDLER_USER_PTR = 4225
M_GRAB_FIELD_START_HANDLER_PTR = 4220
M_GRAB_FIELD_START_HANDLER_USER_PTR = 4221
M_GRAB_FIELD_START_ODD = 15
M_GRAB_FIELD_START_ODD_HANDLER_PTR = 4222
M_GRAB_FIELD_START_ODD_HANDLER_USER_PTR = 4223
M_GRAB_FIELD_START_THREAD_HANDLE = 4248
M_GRAB_FIELD_START_THREAD_ID = 4249
M_GRAB_FORCE_IN_USER_BUFFER = 11
M_GRAB_FORCE_WITHOUT_UNDERLAY = 12
M_GRAB_FPGA_FAN_RPM = 2365
M_GRAB_FRAME_BURST_COUNT = 4386
M_GRAB_FRAME_BURST_END_SOURCE = 4387
M_GRAB_FRAME_BURST_END_TRIGGER_SOURCE = 4433
M_GRAB_FRAME_BURST_END_TRIGGER_STATE = 4432
M_GRAB_FRAME_BURST_MAX_TIME = 6608
M_GRAB_FRAME_BURST_SIZE = 4429
M_GRAB_FRAME_BURST_START_TRIGGER_SOURCE = 4431
M_GRAB_FRAME_BURST_START_TRIGGER_STATE = 4430
M_GRAB_FRAME_END = 5
M_GRAB_FRAME_END_DELAY = 6644
M_GRAB_FRAME_END_HANDLER_PTR = 4042
M_GRAB_FRAME_END_HANDLER_USER_PTR = 4043
M_GRAB_FRAME_END_SIGNAL = 120
M_GRAB_FRAME_END_SIGNAL0 = 120
M_GRAB_FRAME_END_SIGNAL1 = 121
M_GRAB_FRAME_END_SIGNAL2 = 122
M_GRAB_FRAME_END_SIGNAL3 = 123
M_GRAB_FRAME_END_THREAD_HANDLE = 4261
M_GRAB_FRAME_END_THREAD_ID = 4262
M_GRAB_FRAME_END_TIME_STAMP_BUFFER = 4371
M_GRAB_FRAME_MISSED = 5347
M_GRAB_FRAME_MISSED_COUNTER = 5348
M_GRAB_FRAME_MISSED_RESET = 5349
M_GRAB_FRAME_NUM = 4017
M_GRAB_FRAME_START = 13
M_GRAB_FRAME_START_HANDLER_PTR = 4044
M_GRAB_FRAME_START_HANDLER_USER_PTR = 4045
M_GRAB_FRAME_START_THREAD_HANDLE = 4313
M_GRAB_FRAME_START_THREAD_ID = 4314
M_GRAB_FREQ_MAX = 4232
M_GRAB_HALT_ON_NEXT_FIELD = 4126
M_GRAB_INPUT_GAIN = 4019
M_GRAB_IN_PROGRESS = 4128
M_GRAB_IN_USER_BUFFER = 4375
M_GRAB_LINE = 1048576
M_GRAB_LINESCAN_MODE = 4141
M_GRAB_LINE_COUNT = 4378
M_GRAB_LINE_COUNTER = 4379
M_GRAB_LINE_END = 2097152
M_GRAB_LINE_HANDLER_PTR = 4367
M_GRAB_LINE_HANDLER_USER_PTR = 4368
M_GRAB_LL_SEQ_CONTEXT = 5330
M_GRAB_LUT_PALETTE = 4125
M_GRAB_MODE = 4016
M_GRAB_NEXT_FIELD = 2
M_GRAB_NEXT_FRAME = 1
M_GRAB_OFFLOAD_ENGINE_PRESENT = 4391
M_GRAB_ON_ONE_LINE = 4123
M_GRAB_PATH_OVERRIDE = 4239
M_GRAB_PATH_OVERRIDE_DCF = 4240
M_GRAB_PATH_PCI = 4241
M_GRAB_PATH_RR = 4280
M_GRAB_PENDING = 4130
M_GRAB_PERIOD = 4142
M_GRAB_PROCESSING = 5327
M_GRAB_QUEUE_SIZE = 4369
M_GRAB_READY = 45
M_GRAB_RESTRICTION_CHECK = 4215
M_GRAB_SAMPLING_POSITION = 4311
M_GRAB_SCALE = 6600
M_GRAB_SCALE_INTERPOLATION_MODE = 5452
M_GRAB_SCALE_MODE = 4319
M_GRAB_SCALE_MODE_X = 4320
M_GRAB_SCALE_MODE_Y = 4321
M_GRAB_SCALE_QUALITY = 4362
M_GRAB_SCALE_X = 6601
M_GRAB_SCALE_X_SUPPORTED = 6648
M_GRAB_SCALE_Y = 6602
M_GRAB_SCALE_Y_SUPPORTED = 6649
M_GRAB_START = 4
M_GRAB_START_HANDLER_PTR = 4033
M_GRAB_START_HANDLER_USER_PTR = 4035
M_GRAB_START_HOOK = 4331
M_GRAB_START_MODE = 4074
M_GRAB_START_THREAD_HANDLE = 4235
M_GRAB_START_THREAD_ID = 4236
M_GRAB_SUBSAMPLE = 6603
M_GRAB_SUBSAMPLE_X = 6604
M_GRAB_SUBSAMPLE_Y = 6605
M_GRAB_THREAD_HANDLE = 4233
M_GRAB_THREAD_ID = 4234
M_GRAB_TIMEOUT = 4127
M_GRAB_TIME_STAMP = 64
M_GRAB_TIME_STAMP_NS = 6772
M_GRAB_TRIGGER = 4200
M_GRAB_TRIGGER_ACTIVATION = 4054
M_GRAB_TRIGGER_BUFFERING = 4384
M_GRAB_TRIGGER_DELAY = 6646
M_GRAB_TRIGGER_DELAY_CLOCK_ACTIVATION = 4145
M_GRAB_TRIGGER_DELAY_CLOCK_SOURCE = 4144
M_GRAB_TRIGGER_MISSED = 4460
M_GRAB_TRIGGER_OVERLAP = 4383
M_GRAB_TRIGGER_READY = 91
M_GRAB_TRIGGER_SOFTWARE = 4209
M_GRAB_TRIGGER_SOURCE = 4053
M_GRAB_TRIGGER_STATE = 4200
M_GRAB_TYPE = 5097
M_GRAB_TYPE_ENCODER = 9
M_GRAB_TYPE_LIVE = 6
M_GRAB_TYPE_NO_TEARING = 8
M_GRAB_TYPE_ON_TITLE_BAR = 10051
M_GRAB_TYPE_PSEUDO = 5
M_GRAB_TYPE_PSEUDO_MULTIPLE_BUFFERS = 7
M_GRAB_TYPE_PSEUDO_SINGLE_BUFFER = 10
M_GRAB_USAGE = 2303
M_GRAB_VALID = 4244
M_GRAB_VM = 4282
M_GRAB_WAIT = 4219
M_GRAB_WINDOW_RANGE = 4075
M_GRAB_WINDOW_RANGE_SUPPORTED = 4065
M_GRAB_WRITE_FORMAT = 4124
M_GRADE_QUIET_ZONE = 2557
M_GRADIENT = 3306
M_GRADIENT_SQR = 3307
M_GRADIENT_VERTICAL = 3970
M_GRADING_STANDARD = 32832
M_GRADING_STANDARD_EDITION = 3121
M_GRAPHIC = 3879
M_GRAPHIC_CONTEXT = 16777216
M_GRAPHIC_CONTROL_TYPE = 1761
M_GRAPHIC_CONVERSION_MODE = 1721
M_GRAPHIC_CREATE = 1763
M_GRAPHIC_INDEX_TAG = 16777216
M_GRAPHIC_INTERACTIVE = 1764
M_GRAPHIC_LABEL_TAG = 33554432
M_GRAPHIC_LABEL_VALUE = 1758
M_GRAPHIC_LABEL_VALUE_DESELECTED = 1759
M_GRAPHIC_LIST = 8589934592
M_GRAPHIC_LIST_BOUNDING_RECT = 10570
M_GRAPHIC_LIST_ID = 1755
M_GRAPHIC_LIST_INTERACTIVE = 10567
M_GRAPHIC_LIST_LIMITED_TO_BUFFER_AREA = 10575
M_GRAPHIC_LIST_MODIFIED = 1529
M_GRAPHIC_LIST_MODIFIED_INTERNAL = 1530
M_GRAPHIC_LIST_RELATIVE_TO_ANCESTOR = 10576
M_GRAPHIC_LOAD = 1762
M_GRAPHIC_MODIFIED = 1527
M_GRAPHIC_RESOLUTION = 4676
M_GRAPHIC_SELECTED = 75
M_GRAPHIC_SELECTION_MODIFIED = 1526
M_GRAPHIC_SOURCE_CALIBRATION = 1113
M_GRAPHIC_SUB_INDEX = 1760
M_GRAPHIC_TEXT = 3869
M_GRAPHIC_TYPE = 1518
M_GRAPHIC_TYPE_ARC = 1505
M_GRAPHIC_TYPE_AXIS = 3881
M_GRAPHIC_TYPE_BOX = 3882
M_GRAPHIC_TYPE_COLLECTION = 1661
M_GRAPHIC_TYPE_CYLINDER = 3884
M_GRAPHIC_TYPE_DOT = 1506
M_GRAPHIC_TYPE_DOTS = 1507
M_GRAPHIC_TYPE_GRID = 3885
M_GRAPHIC_TYPE_INFINITE_LINES = 1655
M_GRAPHIC_TYPE_LINE = 1508
M_GRAPHIC_TYPE_LINES = 1509
M_GRAPHIC_TYPE_NODE = 3889
M_GRAPHIC_TYPE_PLANE = 3886
M_GRAPHIC_TYPE_POINT_CLOUD = 3883
M_GRAPHIC_TYPE_POLYGON = 1510
M_GRAPHIC_TYPE_POLYLINE = 1511
M_GRAPHIC_TYPE_QUAD = 3887
M_GRAPHIC_TYPE_RECT = 1512
M_GRAPHIC_TYPE_RING_SECTOR = 1514
M_GRAPHIC_TYPE_SPHERE = 3888
M_GRAPHIC_TYPE_SYMBOLS = 1633
M_GRAPHIC_TYPE_TEXT = 1513
M_GRAYSCALE = 512
M_GRAY_LEVEL_SIZE_Z = 1370
M_GRA_CURSOR_HAND = 27
M_GRA_CURSOR_IN_ROTATION = 26
M_GRA_CURSOR_NO = 24
M_GRA_CURSOR_ROTATE = 25
M_GRA_CURSOR_SIZEALL = 22
M_GRA_CURSOR_SIZEALL_POINTER = 23
M_GRA_CURSOR_SIZENESW = 19
M_GRA_CURSOR_SIZENS = 21
M_GRA_CURSOR_SIZENWSE = 18
M_GRA_CURSOR_SIZEWE = 20
M_GRA_HOOK_CONTEXT = 1610612740
M_GRA_INQUIRE_DOUBLE_RANGE_END = 1299
M_GRA_INQUIRE_DOUBLE_RANGE_START = 1200
M_GRA_INQUIRE_MIL_ID_RANGE_END = 1199
M_GRA_INQUIRE_MIL_ID_RANGE_START = 1100
M_GRA_INTERACTIVE_DISABLED = 78
M_GRA_INTERACTIVE_ENABLED = 77
M_GRA_OPERATION_ERROR = 109
M_GRA_OPERATION_ERROR_2 = 190
M_GREATER = 5
M_GREATER_CONST = 32773
M_GREATER_OR_EQUAL = 7
M_GREATER_OR_EQUAL_CONST = 32775
M_GREEN = 16
M_GREYSCALE = 512
M_GREY_DIAGONAL_RAMP = 2
M_GREY_DIAGONAL_RAMP_MOVING = 3
M_GRID = 1852
M_GRID_FIDUCIAL = 2186
M_GRID_HINT_ANGLE_X = 2187
M_GRID_HINT_PIXEL_X = 162
M_GRID_HINT_PIXEL_Y = 163
M_GRID_NONUNIFORMITY = 41028
M_GRID_NONUNIFORMITY_GRADE = 36932
M_GRID_NOT_FOUND = 4
M_GRID_ORIGIN_X = 109
M_GRID_ORIGIN_Y = 110
M_GRID_ORIGIN_Z = 111
M_GRID_PARTIAL = 2185
M_GRID_SHAPE = 2188
M_GRID_SIZE_X = 3632
M_GRID_SIZE_Y = 3633
M_GRID_SIZE_Z = 3634
M_GRID_TYPE = 206
M_GRID_UNITS = 2394
M_GRID_UNIT_SHORT_NAME = 2395
M_GRID_UNIT_SHORT_NAME_MAX_SIZE = 16
M_GROUP = 70368744177664
M_GROUP_EDGELS = 3077
M_GROUP_EDGEL_GAP_SIZE = 3082
M_GROUP_ID = 18
M_GROUP_MIN_NUMBER_OF_EDGELS = 3169
M_GROUP_SELECTION_MODE = 3166
M_GROUP_SELECTION_OCCURRENCE = 3168
M_GROUP_SELECTION_POINT = 3167
M_GS1_128 = 33554432
M_GS1_128_NAME = MIL_TEXT("GS1_128")
M_GS1_DATABAR = 16384
M_GS1_DATABAR_EXPANDED = 262144
M_GS1_DATABAR_EXPANDED_STACKED = 2097152
M_GS1_DATABAR_LIMITED = 131072
M_GS1_DATABAR_NAME = MIL_TEXT("GS1_DataBar")
M_GS1_DATABAR_OMNI = 32768
M_GS1_DATABAR_STACKED = 524288
M_GS1_DATABAR_STACKED_OMNI = 1048576
M_GS1_DATABAR_TRUNCATED = 65536
M_GS1_FORMAT = 64
M_GS1_HUMAN_READABLE = 130
M_GT1200 = 67112960
M_GT1200C = -2080370688
M_GT1900 = 134221824
M_GT1900C = -2013261824
M_GT300 = 4096
M_GT300C = -2147479552
M_GT5000 = 201330688
M_GTK_MODE = 10152
M_H264 = 32768
M_HAAR = 1
M_HANDLE_MESSAGES = 3227
M_HANDLE_SET_CURSOR_MESSAGE = 3229
M_HARDWARE = 131072
M_HARDWARE_COMPRESSION = 2130
M_HARDWARE_COMPRESSION_TYPE = 2134
M_HARDWARE_DECOMPRESSION = 2131
M_HARDWARE_DEINTERLACING = 5449
M_HARDWARE_LUT_AVAILABLE = 10027
M_HARDWARE_PAN = 3004
M_HARDWARE_PORT_CAMERA = 18
M_HARDWARE_ZOOM = 3005
M_HAS_CUSTOM_COMPONENT_TYPE_NAME = 5111
M_HAS_DONT_CARE_MASK = 2391
M_HAS_FEATURE = 134217728
M_HAS_FLAT_REGIONS_MASK = 2392
M_HAS_TARGET_EDGES_SAVED = 2679
M_HAS_WEIGHT_REGIONS_MASK = 2393
M_HDMI = 8192
M_HDR_IMAGE_LIMITED_TO_SINGLE_COLOR = 6
M_HDR_IMAGE_STATUS = 2000
M_HDR_IMAGE_STATUS_SIZE = 2001
M_HDR_INSUFFICIENT_COLOR_DEPTH = 1
M_HDR_INSUFFICIENT_CONTRIBUTION = 3
M_HDR_MERGE_AREA_GAIN_INCORRECT = 5
M_HDR_MERGE_AREA_SIZE_INSUFFICIENT = 4
M_HDR_STATUS = 2002
M_HDR_SUCCESSFULL = 0
M_HEAP_FREE = 2328
M_HEAP_SIZE = 2327
M_HEIGHT = 317
M_HEMISPHERE = 1354
M_HESSIAN = 3308
M_HEX_UTF16_FOR_ALL = 1048576
M_HEX_UTF16_FOR_NON_BASIC_LATIN = 524288
M_HFPGA_REGISTER_PHYSICAL_ADDRESS = 6702
M_HFPGA_REGISTER_RANGE = 4818
M_HIDE_DEPRECATED_FROM_INTELLISENSE = 0
M_HIGH = 3
M_HIGHER_RESERVED_COLOR_END = 10024
M_HIGHER_RESERVED_COLOR_START = 10023
M_HIGHEST = 10
M_HIGHLVL_ERR_OFFSET = 20000
M_HIGHLVL_ERR_OFFSET_MAX = 48999
M_HIGH_DYNAMIC_RANGE = 5
M_HIGH_DYNAMIC_RANGE_RESULT = 5
M_HIGH_DYNAMIC_RANGE_WORKSPACE = 16
M_HISTOGRAM_BASED = 1480
M_HISTOGRAM_CLASSIFY_PIXEL = 1444
M_HISTOGRAM_EQUALIZE_ADAPTIVE_CONTEXT = 13
M_HISTOGRAM_FREQUENCY_THRESHOLD = 1627
M_HISTOGRAM_MATCHING = 1443
M_HISTOGRAM_VOTE = 1626
M_HIST_BIN_SIZE_MODE = 400
M_HIST_LIST = 8192
M_HIST_REAL_SIZE = 102
M_HIST_SIZE = 253
M_HIST_SMOOTHING_ITERATIONS = 401
M_HIST_VALUE_OFFSET = 103
M_HIST_VALUE_RANGE = 104
M_HIT_OR_MISS = 5
M_HLS_TO_RGB = 10485763
M_HLVLDATATYPE_MASK = 1030792151040
M_HOLDING_REGISTER = MIL_TEXT("M_HOLDING_REGISTER")
M_HOLES_FOUND = 5373
M_HOMOGENEOUS_MATRIX = 0
M_HOOKS = 10170
M_HOOK_AFTER = 268435456
M_HOOK_BEFORE = 536870912
M_HOOK_CANCEL_EVENT_BACKDOOR_INTERNAL = 17508
M_HOOK_CONTEXT = 1610612737
M_HOOK_CONTEXT_OBJECT = 1610612736
M_HOOK_CONTEXT_SIZE = 6
M_HOOK_ENCODING_END = 2304
M_HOOK_ENCODING_STREAM_PTR = 2304
M_HOOK_ERROR = 14
M_HOOK_ERROR_SPECIFIC = 191
M_HOOK_EVENT_BACKDOOR_INTERNAL = 17476
M_HOOK_FOR_PSEUDO_LIVE_GRAB = 4360
M_HOOK_FUNCTION_SUPPORTED = 4064
M_HOOK_MASTER_THREAD_HANDLE = 4278
M_HOOK_MASTER_THREAD_ID = 4279
M_HOOK_MESSAGE_LOOP = 4
M_HOOK_MODIFIED_DIB = 1
M_HOOK_MODIFIED_WINDOW = 2
M_HOOK_OFFSET = 3019
M_HOOK_ON_DEVICE_LOSING = 10554
M_HOOK_ON_ERROR = 10124
M_HOOK_ON_MB_CHILD_RESIZE = 10173
M_HOOK_ON_OUT_OF_MONITOR = 10171
M_HOOK_ON_ZOOM_CHANGE = 10172
M_HOOK_PARAM = 30
M_HOOK_TO_BUFFER_MODIFICATIONS = 5201
M_HOOK_TYPE = 50
M_HORIZONTAL = 2
M_HORIZONTAL_EDGE_PREWITT = 9437201
M_HORIZONTAL_EDGE_SOBEL = 9437199
M_HORIZONTAL_LEVEL_TAG = 16777216
M_HORIZONTAL_MARK_GROWTH = 41040
M_HORIZONTAL_MARK_MISPLACEMENT = 41044
M_HORIZONTAL_PLANE = 1352
M_HORIZONTAL_THICKNESS = 233
M_HORIZ_EDGE = 9437189
M_HOST = 100
M_HOST_ACCESS = 8
M_HOST_ADDRESS = 65536
M_HOST_ADDRESS_BAND = 5205
M_HOST_ADDRESS_BLUE = 65568
M_HOST_ADDRESS_GREEN = 65552
M_HOST_ADDRESS_RED = 65544
M_HOST_ADDRESS_REMOTE = 524288
M_HOST_ADDRESS_REMOTE_BLUE = 524320
M_HOST_ADDRESS_REMOTE_GREEN = 524304
M_HOST_ADDRESS_REMOTE_RED = 524296
M_HOST_ID = 1106
M_HOST_MEMORY = 8589934592
M_HOST_MEMORY_INCOMPATIBLE_BITS = 1153493542719455232
M_HOST_THREAD = 2
M_HSCROLL_VISIBLE = 10014
M_HSL = 2
M_HSL_TO_RGB = 10485763
M_HSV_TO_RGB = 10485772
M_HSYNC = 22
M_HSYNC_ERROR = 2
M_HTML5_MESSAGE = 16777216
M_HTTP_ADDRESS = 109
M_HTTP_ADDRESS_SIZE = 5497558138989
M_HTTP_ERROR_END = 54999
M_HTTP_ERROR_START = 54000
M_HTTP_LISTENING_ADDRESS = MIL_TEXT("localhost")
M_HTTP_LISTENING_PORT = 8080
M_HTTP_MODE = 113
M_HTTP_PORT = 107
M_HTTP_ROOT_DIRECTORY = 108
M_HTTP_ROOT_DIRECTORY_SIZE = 5497558138988
M_HTTP_SERVER = 562949953421312
M_HTTP_SERVICE_ERROR = 188
M_HTTP_START = 110
M_HTTP_STATE = 114
M_HTTP_STOP = 112
M_HUE = 32768
M_HUE_REF = 6655
M_HUFFMAN_AC = 1125
M_HUFFMAN_AC_CHROMINANCE = 1123
M_HUFFMAN_AC_LUMINANCE = 1121
M_HUFFMAN_DC = 1124
M_HUFFMAN_DC_CHROMINANCE = 1122
M_HUFFMAN_DC_LUMINANCE = 1120
M_HV_RESET = 5319
M_HYPER_CUBE_ROOT = 4
M_HYPER_LOG = 5
M_HYSTERESIS = 31
M_I = 2977
M_ICON_EXCLAMATION = 48
M_ICON_MASK = 240
M_ICON_STOP = 16
M_IDEMPOTENT_FOR_WORKSPACE = 16530
M_IDENTICAL = 4194304
M_IDENTIFIER_TYPE = 15
M_IDENTITY = 6
M_IDENTITY_MATRIX = 8388619
M_IDLE = 1
M_ID_IS_ON_LOCAL_CLUSTER = 318
M_ID_KEY_FINGERPRINT = 21360
M_ID_LIST_FREE_ENTRIES = 16582
M_ID_OFFSET_OF_DEFAULT_CONVERT = 10485760
M_ID_OFFSET_OF_DEFAULT_KERNEL = 9437184
M_ID_OFFSET_OF_EDGE_DETECTVAR = 9437440
M_ID_TABLE_LEGACY_MODE = 16583
M_ID_TABLE_SIZE = 16581
M_IEEE_1394_IIDC = 50
M_IGNORE = 8192
M_IGNORED_EXP_DATE = 15745
M_IGNORE_CACHE = 8589934592
M_IGNORE_DISTANCE_MAX_FOR_ROBUST_FIT = 5106
M_IGNORE_REGION = 2048
M_IMAGE = 4
M_IMAGE_FILE_NOT_FOUND = 3793
M_IMAGE_FRAME = 0
M_IMAGE_ID = 67108864
M_IMAGE_INDEX = 134217728
M_IMAGE_OFFSET_X = 8215
M_IMAGE_OFFSET_Y = 8216
M_IMAGE_PATH = MIL_TEXT("///INSTALLDIR///images\\")
M_IMAGE_SIZE_BAND = 1911
M_IMAGE_SIZE_X = 1536
M_IMAGE_SIZE_Y = 1537
M_IMAGE_TYPE = 1
M_IMAGINARY_PART = 8192
M_IMMEDIATE = 10
M_IMPORT_ALL_CHARS = 0
M_IMPORT_JPEG_WITH_VALIDATION = 15145
M_IMPORT_PARAMETERS = 974
M_IMPORT_TRAINING = 975
M_IMPROVED_RECOGNITION = 3
M_IMPULSE = 88
M_IMPULSE_C_STATE = 1085
M_IM_ALLOC_RESULT_BUFFER_TYPES = 8796093280256
M_IM_CONTEXT = 1073741824
M_IM_RESULT_BUFFER_MEMORY_SPECIFIERS = 1256504390562873344
M_IM_RESULT_OBJECT_TYPES = 1445033156804608
M_IN = 512
M_INCH = 2454
M_INCHES = 2454
M_INCLUDE = 1
M_INCLUDED = 265
M_INCLUDED_BLOBS = 134217728
M_INCLUDED_EDGES = 4194304
M_INCLUDE_ALL_POINTS = 0
M_INCLUDE_MISSING_DATA = 262144
M_INCLUDE_ONLY = 257
M_INCLUDE_POINTS_INSIDE_BOX_ONLY = 1140850688
M_INCLUSION_POINT = 1581
M_INCLUSION_POINT_INPUT_UNITS = 1459
M_INCLUSION_POINT_INSIDE_STRIPE = 148480
M_INCREMENT_ASYNC = 1
M_INDEX = 217
M_INDEX_FROM_LABEL = 229
M_INDEX_IN_FORMATTED_STRING_FLAG = 14680064
M_INDEX_IN_STRING_FLAG = 10485760
M_INDEX_VALUE = 217
M_INDIAN_PATTERN = 8388612
M_INDIO = 24
M_INDIO_FINGERPRINT = 20848
M_INDIVIDUAL = 2
M_INDIVIDUAL_WIDTH_NOMINAL = 212
M_INDUSTRIAL25 = 17
M_INDUSTRIAL25_NAME = MIL_TEXT("Industrial25")
M_INFINITE = -1
M_INFINITE_LINES = 256
M_INFINITE_LINES_A_B_C = 512
M_INFO_FORMAT = 5318
M_INITIALIZATION_DELAY = 5321
M_INITIALIZATION_MODE = 2148
M_INITIAL_LEARNING_RATE = 3493
M_INIT_FLAG = 1012
M_INIT_HOOK_CONTEXT = 2
M_INLIER_AMOUNT_THRESHOLD = 3599
M_INLIER_MASK = 3590
M_INNER_FIT = 48
M_INNER_RADIUS = 234
M_INNER_RADIUS_X = 1215
M_INNER_RADIUS_Y = 1216
M_INNER_TO_OUTER_RADIUS = 2793
M_INPUT = 2
M_INPUT0 = 268435456
M_INPUT1 = 268435457
M_INPUT2 = 268435458
M_INPUT3 = 268435459
M_INPUT4 = 268435460
M_INPUT5 = 268435461
M_INPUT6 = 268435462
M_INPUT7 = 268435463
M_INPUT8 = 268435464
M_INPUT9 = 268435465
M_INPUT_DATASET_ID = 3681
M_INPUT_FILTER = 5186
M_INPUT_LOW_PASS_FILTER = 5184
M_INPUT_MODE = 4020
M_INPUT_REGISTER = MIL_TEXT("M_INPUT_REGISTER")
M_INPUT_SELECT_UNITS = 20
M_INPUT_SIGNAL_COLOR_LOCK = 4399
M_INPUT_SIGNAL_HSYNC_LOCK = 4228
M_INPUT_SIGNAL_PRESENT = 4078
M_INPUT_SIGNAL_SOURCE = 4079
M_INPUT_TYPE = 4086
M_INPUT_UNITS = 121
M_INQUIRE_SIZE_BYTE = 2
M_INQ_COMBOFLAGS_MASK = 281406525669376
M_INSERT = 5
M_INSIDE = 1
M_INSIDE_BOX = 300
M_INSIDE_CHAIN = 301
M_INSIDE_EXTRACTION_BOX = 1073741824
M_INSIDE_OR_EQUAL_BOX = 364
M_INSIDE_OR_EQUAL_CHAIN = 365
M_INSPECTION_BAND_RATIO = 1649
M_INSTALLATION_ERROR = 81
M_INSTALLATION_TYPE = 16523
M_INSTALLED_SYSTEM_CAN_GRAB = 24856
M_INSTALLED_SYSTEM_CAN_GRAB_OLD = 15800
M_INSTALLED_SYSTEM_COUNT = 15121
M_INSTALLED_SYSTEM_COUNT_OLD = 15063
M_INSTALLED_SYSTEM_DESCRIPTOR = 22000
M_INSTALLED_SYSTEM_DESCRIPTOR_OLD = 16800
M_INSTALLED_SYSTEM_DESCRIPTOR_SIZE = 5497558160880
M_INSTALLED_SYSTEM_DESCRIPTOR_SIZE_OLD = 5497558155680
M_INSTALLED_SYSTEM_DEVICE_COUNT = 25500
M_INSTALLED_SYSTEM_PRINT_NAME = 22064
M_INSTALLED_SYSTEM_PRINT_NAME_OLD = 16816
M_INSTALLED_SYSTEM_PRINT_NAME_SIZE = 5497558160944
M_INSTALLED_SYSTEM_PRINT_NAME_SIZE_OLD = 5497558155696
M_INSTALLED_SYSTEM_REG_KEY_NAME = 22128
M_INSTALLED_SYSTEM_REG_KEY_NAME_OLD = 16832
M_INSTALLED_SYSTEM_REG_KEY_NAME_SIZE = 5497558161008
M_INSTALLED_SYSTEM_REG_KEY_NAME_SIZE_OLD = 5497558155712
M_INSTALLED_SYSTEM_TYPE = 24920
M_INSTALLED_SYSTEM_TYPE_OLD = 15728
M_INSTALL_DIR = MIL_TEXT("///INSTALLDIR///")
M_INSTANCE_ID = 8196
M_INTEGER_BOUNDING_BOX = 256
M_INTEGRAL = 271
M_INTEL_IA64 = 10242
M_INTEL_X86 = 10241
M_INTENSITY = 52
M_INTENSITY_DELTA_NEG = 83
M_INTENSITY_DELTA_POS = 82
M_INTENSITY_MAP = 2030
M_INTENSITY_MAP_BUFFER_TYPE = 9
M_INTENSITY_MAX = 85
M_INTENSITY_MAX_INDEX = 87
M_INTENSITY_MIN = 84
M_INTENSITY_MIN_INDEX = 86
M_INTENSITY_NOMINAL = 81
M_INTENSITY_NOMINAL_MODE = 80
M_INTERACTIVE = 0
M_INTERACTIVE_ANNOTATIONS_COLOR = 1024
M_INTERACTIVE_GRAPHIC_PREVIOUS_STATE = 1756
M_INTERACTIVE_GRAPHIC_STATE = 1746
M_INTERACTIVE_GRAPHIC_STATE_MODIFIED = 1528
M_INTERACTIVE_MODE = 3218
M_INTERACTIVE_ZOOM = 6619
M_INTERACTIVE_ZOOM_INCREMENT = 6618
M_INTERACTIVE_ZOOM_MAX = 6616
M_INTERACTIVE_ZOOM_MIN = 6617
M_INTERACTIVITY = 1724
M_INTERCEPT = 2477
M_INTERCEPT_0 = 51
M_INTERCEPT_135 = 54
M_INTERCEPT_45 = 52
M_INTERCEPT_90 = 53
M_INTEREST_POINT = 4164
M_INTERLACE = 0
M_INTERLEAVED25 = 16
M_INTERLEAVED25_NAME = MIL_TEXT("Interleaved25")
M_INTERMEDIATE_ITERATION = 327680
M_INTERMOD_MASK = -17179869184
M_INTERMOD_STATE_MASK = 263882790666240
M_INTERMOD_VALUE_MASK = 16492674416640
M_INTERNAL = 917504
M_INTERNAL_BUFFER_HOST_ADDRESS = 5064
M_INTERNAL_CALL = 256
M_INTERNAL_CAMERA_STRUCT_PTR = 2156
M_INTERNAL_CAMERA_STRUCT_SIZE = 2157
M_INTERNAL_COMPLETE_FORMAT = 2147483520
M_INTERNAL_COMPRESSION_BUFFER_ID = 5063
M_INTERNAL_COMPRESSION_BUFFER_SIZE_DIVISION_FACTOR = 5066
M_INTERNAL_CONTEXT_TYPE = 2906
M_INTERNAL_ERROR = 5
M_INTERNAL_FCT = 983040
M_INTERNAL_FFT_NEW = 8
M_INTERNAL_FORMAT = 16128
M_INTERNAL_FORMAT_CHECK = 2064
M_INTERNAL_FORMAT_ENUMERATION = 2063
M_INTERNAL_FORMAT_SHIFT = 8
M_INTERNAL_FORMAT_SIZE = 2062
M_INTERNAL_GRAB_BUFFERS_FORMAT = 4317
M_INTERNAL_GRAB_BUFFERS_ID = 6801
M_INTERNAL_GRAB_BUFFERS_NB = 4315
M_INTERNAL_GRAB_BUFFER_MIL_ID = 6804
M_INTERNAL_JPEG_FRAME_SIZEBYTE = 5065
M_INTERNAL_LIC_BGA = -9205357638345293824
M_INTERNAL_LIC_BLOB = -9223372036586340352
M_INTERNAL_LIC_CAL = -9223372036720558080
M_INTERNAL_LIC_CHEAT = -9223372036854775776
M_INTERNAL_LIC_CHECK = -9223372036854775808
M_INTERNAL_LIC_CLASS = -9223372036854775804
M_INTERNAL_LIC_CODE = -9223372036787666944
M_INTERNAL_LIC_COL = -9218868437227405312
M_INTERNAL_LIC_COM = -9223372036854251520
M_INTERNAL_LIC_DA0 = -9223372036854771712
M_INTERNAL_LIC_DA1 = -9223372036854767616
M_INTERNAL_LIC_DEBUG = -4611686018427387904
M_INTERNAL_LIC_DMIL = -9223372036854775800
M_INTERNAL_LIC_DMILC = -9223372036854774784
M_INTERNAL_LIC_EDGE = -9187343239835811840
M_INTERNAL_LIC_ERROR = -9223372036854775744
M_INTERNAL_LIC_GPU = -9223372036854775680
M_INTERNAL_LIC_IM = -9223372036821221376
M_INTERNAL_LIC_INSPECTOR = -9223372036854773760
M_INTERNAL_LIC_JPEG2000 = -9223372036852678656
M_INTERNAL_LIC_JPEGSTD = -9223372036837998592
M_INTERNAL_LIC_LITE = -6917529027641081856
M_INTERNAL_LIC_MEAS = -9223372036846387200
M_INTERNAL_LIC_MET = -9221120237041090560
M_INTERNAL_LIC_MOD = -9223372036850581504
M_INTERNAL_LIC_OCR = -9223372035781033984
M_INTERNAL_LIC_PAT = -9223372036853727232
M_INTERNAL_LIC_R12 = -9223090561878065152
M_INTERNAL_LIC_R13 = -9079256848778919936
M_INTERNAL_LIC_R15 = -9223372036317904896
M_INTERNAL_LIC_R3 = -9214364837600034816
M_INTERNAL_LIC_R5 = -9223372036854775792
M_INTERNAL_LIC_R7 = -9223372036854775552
M_INTERNAL_LIC_R8 = -9223372036854775296
M_INTERNAL_LIC_REG = -9222809086901354496
M_INTERNAL_LIC_SER = -9151314442816847872
M_INTERNAL_LIC_STR = -9222246136947933184
M_INTERNAL_PARAMETER = 65536
M_INTERNAL_SUB = 1114112
M_INTERNAL_SUB_1 = 1114112
M_INTERNAL_SUB_2 = 1179648
M_INTERNAL_SUB_3 = 1245184
M_INTERNAL_SUB_NB = 1048576
M_INTERNAL_SYNC = 84
M_INTERNAL_SYSTEM_TYPE = 2002
M_INTERNAL_THREAD_CALL = 4
M_INTERNAL_THREAD_ERROR_TOOLS = 2
M_INTERNAL_USE = 4
M_INTERPOLATE = 4
M_INTERPOLATE_ANGLE = 1
M_INTERPOLATION_MODE = 3018
M_INTERPRETER_CSHARP = MIL_TEXT("MilInterpCSharp.dll")
M_INTERPRETER_C_PYTHON27 = MIL_TEXT("MilInterpPython27.dll")
M_INTERPRETER_C_PYTHON36 = MIL_TEXT("MilInterpPython36.dll")
M_INTERPRETER_C_PYTHON37 = MIL_TEXT("MilInterpPython37.dll")
M_INTERPRETER_C_PYTHON38 = MIL_TEXT("MilInterpPython38.dll")
M_INTERPRETER_PATH = 50
M_INTERPRETER_PATH_SIZE = 5497558138930
M_INTERPRETER_VB_DOT_NET = MIL_TEXT("MilInterpVBNet.dll")
M_INTERRUPT_LATENCY = 4602
M_INTERRUPT_MASTER_SWITCH = 2109
M_INTERRUPT_NEW_TECHNIQUE = 2106
M_INTERRUPT_NEW_TECHNIQUE_QUEUE = 2108
M_INTERRUPT_NEW_TECHNIQUE_STAT = 2107
M_INTERRUPT_OVERRUN = 128
M_INTERSECTION = 34
M_INTRA_CLUSTER_NODE_MASK = 16529
M_INVALID = -1
M_INVALIDATE_ALL_DISPLAY = 3
M_INVALIDATE_DISPLAY = 134217744
M_INVALIDATE_OVERLAY = 1
M_INVALIDATE_POINTS_OUTSIDE_BOX = 1073741824
M_INVALIDATE_UNDERLAY = 2
M_INVALID_ATTRIBUTE = 38
M_INVALID_CALIBRATION_POINTS = 7
M_INVALID_CONST = 1073741824
M_INVALID_ID = 35
M_INVALID_INQUIRE = 172
M_INVALID_MDID = 1073741824
M_INVALID_NATURE = 36
M_INVALID_NORMALS = 3735
M_INVALID_NUMBER_OF_FEATURES = 3951
M_INVALID_PARAM_COMB_1 = 167
M_INVALID_PARAM_ERROR = 6
M_INVALID_PARAM_ERROR_10 = 67
M_INVALID_PARAM_ERROR_11 = 86
M_INVALID_PARAM_ERROR_12 = 87
M_INVALID_PARAM_ERROR_13 = 88
M_INVALID_PARAM_ERROR_14 = 94
M_INVALID_PARAM_ERROR_15 = 97
M_INVALID_PARAM_ERROR_16 = 98
M_INVALID_PARAM_ERROR_17 = 103
M_INVALID_PARAM_ERROR_18 = 110
M_INVALID_PARAM_ERROR_19 = 116
M_INVALID_PARAM_ERROR_2 = 37
M_INVALID_PARAM_ERROR_20 = 117
M_INVALID_PARAM_ERROR_21 = 119
M_INVALID_PARAM_ERROR_22 = 120
M_INVALID_PARAM_ERROR_23 = 123
M_INVALID_PARAM_ERROR_24 = 128
M_INVALID_PARAM_ERROR_25 = 131
M_INVALID_PARAM_ERROR_26 = 135
M_INVALID_PARAM_ERROR_27 = 139
M_INVALID_PARAM_ERROR_28 = 140
M_INVALID_PARAM_ERROR_29 = 141
M_INVALID_PARAM_ERROR_3 = 41
M_INVALID_PARAM_ERROR_30 = 147
M_INVALID_PARAM_ERROR_31 = 150
M_INVALID_PARAM_ERROR_32 = 154
M_INVALID_PARAM_ERROR_33 = 157
M_INVALID_PARAM_ERROR_34 = 164
M_INVALID_PARAM_ERROR_35 = 170
M_INVALID_PARAM_ERROR_36 = 174
M_INVALID_PARAM_ERROR_37 = 176
M_INVALID_PARAM_ERROR_38 = 179
M_INVALID_PARAM_ERROR_39 = 185
M_INVALID_PARAM_ERROR_4 = 44
M_INVALID_PARAM_ERROR_40 = 187
M_INVALID_PARAM_ERROR_41 = 194
M_INVALID_PARAM_ERROR_42 = 196
M_INVALID_PARAM_ERROR_43 = 198
M_INVALID_PARAM_ERROR_44 = 199
M_INVALID_PARAM_ERROR_45 = 56201
M_INVALID_PARAM_ERROR_46 = 56205
M_INVALID_PARAM_ERROR_47 = 56210
M_INVALID_PARAM_ERROR_5 = 45
M_INVALID_PARAM_ERROR_6 = 46
M_INVALID_PARAM_ERROR_7 = 47
M_INVALID_PARAM_ERROR_8 = 48
M_INVALID_PARAM_ERROR_9 = 50
M_INVALID_POINTS_ONLY = 3734
M_INVALID_PROCESS_ERROR = 180
M_INVALID_RECT = 9018
M_INVALID_REGISTRATION_TYPE = 0
M_INVALID_SCALE = -999999
M_INVALID_VGA_INDEX = -1
M_INVERSE = 256
M_INVERT = 2
M_INVERTED_COLORS = 1048576
M_INV_DIV = 258
M_IN_BUFFER_DISPLAY = 2097152
M_IN_HIGHLEVEL_MODULE = 15052
M_IN_PROGRESS = 0
M_IN_RANGE = 1
M_IO = 65536
M_IO_CHANGE = 569344
M_IO_CHANGE_HANDLER_PTR = 569345
M_IO_CHANGE_HANDLER_USER_PTR = 573440
M_IO_COMMAND_BIT0 = 0
M_IO_COMMAND_BIT1 = 1
M_IO_COMMAND_BIT2 = 2
M_IO_COMMAND_BIT3 = 3
M_IO_COMMAND_BIT4 = 4
M_IO_COMMAND_BIT5 = 5
M_IO_COMMAND_BIT6 = 6
M_IO_COMMAND_BIT7 = 7
M_IO_COMMAND_BIT_MASK_FLAG = 4294967296
M_IO_COMMAND_CANCEL = 5507
M_IO_COMMAND_COUNTER_ACTIVATION = 5506
M_IO_COMMAND_COUNTER_SOURCE = 6701
M_IO_COMMAND_LIST = 1536
M_IO_COMMAND_LIST1 = 1536
M_IO_COMMAND_LIST2 = 1568
M_IO_COMMAND_LIST3 = 1600
M_IO_COMMAND_LIST4 = 1632
M_IO_COMMAND_LIST_NUMBER = 6702
M_IO_DEBOUNCE_TIME = 557056
M_IO_FORMAT = 532480
M_IO_GLITCH_FILTER_STATE = 577536
M_IO_INTERRUPT_ACTIVATION = 544768
M_IO_INTERRUPT_SOURCE = 565248
M_IO_INTERRUPT_STATE = 561152
M_IO_INTERRUPT_TRANSITION_COUNT = 548864
M_IO_INTERRUPT_TRANSITION_COUNT_RESET = 552960
M_IO_INVERTER = 585728
M_IO_MODE = 540672
M_IO_OBJECT_TYPE = 6703
M_IO_SOURCE = 536576
M_IO_STATUS = 528384
M_IO_STATUS_ALL = 268963840
M_IRIS = 160
M_IRISGTR_FINGERPRINT = 20832
M_IRISGT_FINGERPRINT = 21072
M_IRIS_FINGERPRINT = 20960
M_IRIS_GT = 230
M_IRIS_GTR = 220
M_IRIS_GT_DUAL = 231
M_IRQ_CONTROL = 15018
M_ISO6346_CONTAINER = 1
M_ISO_15415_2011_15416_2000 = 4
M_ISO_15415_2011_15416_2016 = 8
M_ISO_15416_2000 = 1
M_ISO_15416_2016 = 2
M_ISO_29158_2011 = 16
M_ISO_DPM_GRADING = 128
M_ISO_GRADING = 16
M_ISO_VERIFICATION = 16
M_IS_CLIENT_UNICODE = 41
M_IS_DISTRIBUTED_BOARD = 24984
M_IS_DISTRIBUTED_BOARD_OLD = 15816
M_IS_DISTRIBUTED_MIL_INSTALLED = 15958
M_IS_DISTRIBUTED_MIL_SERVER_INSTALLED = 15959
M_IS_DISTRIBUTED_SYSTEM_ON_LOCAL_HOST = 4807
M_IS_EA_EXPIRED = 16587
M_IS_ECI = 2556
M_IS_EMULATED = 5900
M_IS_EXCLUSIVE_MONITOR_AVAILABLE = 9255
M_IS_EXTERNAL_DISPLAY = 9264
M_IS_GPU_AVAILABLE = 15307
M_IS_GS1 = 1499
M_IS_INTERNALLY_ALLOCATED = 1043
M_IS_IN_MEGA_BUFFER_MODE = 10028
M_IS_LOCKED = 8454
M_IS_MIL_HTTP_SERVER_INSTALLED = 15964
M_IS_MIL_WEB_INSTALLED = 15963
M_IS_NOT_INTERNAL_OBJECT = 31
M_IS_NO_MAP = 5300
M_IS_ONE_DISPLAY_15_BITS = 15352
M_IS_ONE_DISPLAY_16_BITS = 15353
M_IS_ONE_DISPLAY_24_BITS = 15354
M_IS_ONE_DISPLAY_32_BITS = 15355
M_IS_ONE_DISPLAY_8_BITS = 15351
M_IS_RETURN_VALUE = 256
M_IS_SCREEN_FORBIDDEN = 9268
M_IS_SCREEN_RECT_USABLE = 9269
M_IS_SET_TO_DEFAULT = 17592186044416
M_IS_VIDEO_DEVICE_ALIVE = 8551
M_IS_VIRTUAL_DEVICE = 8537
M_ITALIC_ANGLE = 2240
M_ITALIC_ANGLE_MODE = 2239
M_ITALIC_CHAR_ANGLE = 3753
M_ITALIC_PITCH = 3698
M_ITALIC_PITCH_MODE = 3699
M_ITERATION_INDEX = 3568
M_J2K = 512
M_J2K_ERROR_1 = 68
M_J2K_ERROR_2 = 69
M_J2K_ERROR_3 = 71
M_J2K_ERROR_4 = 72
M_J2K_ERROR_5 = 73
M_J2K_ERROR_6 = 85
M_J2K_ERROR_7 = 90
M_J2K_ERROR_8 = 96
M_JACOBIAN = 3309
M_JAPANESE = 136
M_JIT_COMPILATION_REQUIRED = 4102
M_JIT_COMPILER_NOT_FOUND = 4100
M_JP2_FORMAT = 2
M_JPEG2000 = 512
M_JPEG2000_COMPATIBILITY_CHECKING = 2362
M_JPEG2000_LOSSLESS = 142606336
M_JPEG2000_LOSSLESS_JP2 = 142606344
M_JPEG2000_LOSSY = 138412032
M_JPEG2000_LOSSY_JP2 = 138412040
M_JPEG2000_USAGE = 2308
M_JPEG2K_JP2 = 8
M_JPEG_AUTO_START_MODE = 4275
M_JPEG_COMPRESS = 5069
M_JPEG_COMPRESS_ERROR = 15
M_JPEG_COMPRESS_ERROR_2 = 17
M_JPEG_COMPRESS_ERROR_3 = 60
M_JPEG_COMPRESS_ERROR_4 = 101
M_JPEG_COMPRESS_MODE = 4276
M_JPEG_DECODING_MODE = 4265
M_JPEG_DECOMPRESS = 5070
M_JPEG_DMA_TRANSFER = 4312
M_JPEG_ENCODING_MODE = 4264
M_JPEG_ERROR = 25
M_JPEG_ERROR_2 = 49
M_JPEG_ERROR_3 = 54
M_JPEG_ERROR_4 = 66
M_JPEG_FIRST_FIELD_SIZEBYTE = 4301
M_JPEG_HW_PROG_MODE = 4277
M_JPEG_IMAGE_FORMAT = 4270
M_JPEG_INPUT_COLOR_MODE = 4268
M_JPEG_LOSSLESS = 4194304
M_JPEG_LOSSLESS_INTERLACED = 12582912
M_JPEG_LOSSY = 8388608
M_JPEG_LOSSY_INTERLACED = 134217728
M_JPEG_LOSSY_RGB = 16777216
M_JPEG_MARKERS_ENABLE = 4266
M_JPEG_NAX = 4271
M_JPEG_NAY = 4272
M_JPEG_NUMBER_OF_SCAN_ENCODED = 4267
M_JPEG_OFFSET_X = 4303
M_JPEG_OFFSET_Y = 4304
M_JPEG_OUTPUT_COLOR_MODE = 4269
M_JPEG_PAX = 4273
M_JPEG_PAY = 4274
M_JPEG_SECOND_FIELD_SIZEBYTE = 4302
M_JTAG_CHAIN = 2092
M_KAISER = 65536
M_KEEP_IN_QUEUE = 256
M_KEEP_POLLING_ON_MODE_CHANGED = 9503
M_KERNEL = 4194304
M_KERNEL_SIZE = 301
M_KEYBOARD_USE = 3155
M_KEYING_COLOR = 4727
M_KEY_0 = 48
M_KEY_1 = 49
M_KEY_2 = 50
M_KEY_3 = 51
M_KEY_4 = 52
M_KEY_5 = 53
M_KEY_6 = 54
M_KEY_7 = 55
M_KEY_8 = 56
M_KEY_9 = 57
M_KEY_A = 65
M_KEY_ADD = 107
M_KEY_ALT = 262144
M_KEY_ALWAYS = 3
M_KEY_ARROW_DOWN = 40
M_KEY_ARROW_LEFT = 37
M_KEY_ARROW_RIGHT = 39
M_KEY_ARROW_UP = 38
M_KEY_B = 66
M_KEY_BACK = 8
M_KEY_C = 67
M_KEY_CAPS_LOCK = 20
M_KEY_CHAR = 72
M_KEY_CLEAR = 12
M_KEY_CONDITION = 3008
M_KEY_CTRL = 131072
M_KEY_CUSTOM_VALUE = 17029
M_KEY_D = 68
M_KEY_DECIMAL = 110
M_KEY_DELETE = 46
M_KEY_DIVIDE = 111
M_KEY_DOWN = 68
M_KEY_E = 69
M_KEY_END = 35
M_KEY_ESC = 27
M_KEY_EXECUTE = 43
M_KEY_F = 70
M_KEY_F1 = 112
M_KEY_F10 = 121
M_KEY_F11 = 122
M_KEY_F12 = 123
M_KEY_F13 = 124
M_KEY_F14 = 125
M_KEY_F15 = 126
M_KEY_F16 = 127
M_KEY_F17 = 128
M_KEY_F18 = 129
M_KEY_F19 = 130
M_KEY_F2 = 113
M_KEY_F20 = 131
M_KEY_F21 = 132
M_KEY_F22 = 133
M_KEY_F23 = 134
M_KEY_F24 = 135
M_KEY_F3 = 114
M_KEY_F4 = 115
M_KEY_F5 = 116
M_KEY_F6 = 117
M_KEY_F7 = 118
M_KEY_F8 = 119
M_KEY_F9 = 120
M_KEY_G = 71
M_KEY_H = 72
M_KEY_HELP = 47
M_KEY_HOME = 36
M_KEY_I = 73
M_KEY_INSERT = 45
M_KEY_J = 74
M_KEY_K = 75
M_KEY_L = 76
M_KEY_M = 77
M_KEY_MASK = 3009
M_KEY_MODE = 3007
M_KEY_MULTIPLY = 106
M_KEY_N = 78
M_KEY_NUMPAD0 = 96
M_KEY_NUMPAD1 = 97
M_KEY_NUMPAD2 = 98
M_KEY_NUMPAD3 = 99
M_KEY_NUMPAD4 = 100
M_KEY_NUMPAD5 = 101
M_KEY_NUMPAD6 = 102
M_KEY_NUMPAD7 = 103
M_KEY_NUMPAD8 = 104
M_KEY_NUMPAD9 = 105
M_KEY_NUM_LOCK = 144
M_KEY_O = 79
M_KEY_OEM_COMMA = 188
M_KEY_OEM_MINUS = 189
M_KEY_OEM_PERIOD = 190
M_KEY_OEM_PLUS = 187
M_KEY_OFF = 2
M_KEY_ON_COLOR = 1
M_KEY_P = 80
M_KEY_PAGEDOWN = 34
M_KEY_PAGEUP = 33
M_KEY_PAUSE = 19
M_KEY_PRINT = 42
M_KEY_Q = 81
M_KEY_R = 82
M_KEY_RETURN = 13
M_KEY_S = 83
M_KEY_SCROLL_LOCK = 145
M_KEY_SELECT = 41
M_KEY_SEPARATOR = 108
M_KEY_SERIAL_NUMBER = 22264
M_KEY_SHIFT = 65536
M_KEY_SPACE = 32
M_KEY_SUBTRACT = 109
M_KEY_SUPPORTED = 3011
M_KEY_T = 84
M_KEY_TAB = 9
M_KEY_U = 85
M_KEY_UP = 69
M_KEY_V = 86
M_KEY_VALUE = 8
M_KEY_W = 87
M_KEY_WIN = 4194304
M_KEY_X = 88
M_KEY_Y = 89
M_KEY_Z = 90
M_KILL_BORDER = 44
M_KILL_SCHEME = 15385
M_KILOMETERS = 2453
M_KOREAN = 146
M_KS0127_REV_ID = 4318
M_L1 = 1
M_LABELED = 4
M_LABELED_MARKER = 1024
M_LABELED_TOUCHING = 5
M_LABELLED = 4
M_LABELLED_MARKER = 1024
M_LABELLING_ERROR = 30
M_LABEL_AREA_IMAGE_SIGN = 374
M_LABEL_AREA_IMAGE_SIZE_BAND = 373
M_LABEL_AREA_IMAGE_SIZE_BIT = 372
M_LABEL_AREA_IMAGE_SIZE_X = 370
M_LABEL_AREA_IMAGE_SIZE_Y = 371
M_LABEL_AREA_IMAGE_TYPE = 375
M_LABEL_EXISTS = 4671
M_LABEL_PIXEL_IMAGE_SIGN = 354
M_LABEL_PIXEL_IMAGE_SIZE_BAND = 353
M_LABEL_PIXEL_IMAGE_SIZE_BIT = 352
M_LABEL_PIXEL_IMAGE_SIZE_X = 350
M_LABEL_PIXEL_IMAGE_SIZE_Y = 351
M_LABEL_PIXEL_IMAGE_TYPE = 355
M_LABEL_VALUE = 1
M_LAB_TO_SRGB = 10486263
M_LAB_TO_SRGB_LINEAR = 10486262
M_LAPLACIAN = 3310
M_LAPLACIAN_4 = 9437185
M_LAPLACIAN_8 = 9437186
M_LAPLACIAN_EDGE = 9437185
M_LAPLACIAN_EDGE2 = 9437186
M_LAPLACIAN_ISO_8 = 9437207
M_LASER = 1
M_LASER_3DMAP = 160
M_LASER_CALIBRATION_DATA = 1901
M_LASER_CONTEXT_TYPE = 1313
M_LASER_DATA = 1
M_LASER_LABEL_FLAG = 1073741824
M_LASER_LABEL_VALUE = 1871
M_LASER_LINE_COORDINATE_SYSTEM = 50331648
M_LASER_LINE_NOT_DETECTED = 2
M_LASER_OFFSET = 16
M_LASER_PLANE_A = 1385
M_LASER_PLANE_B = 1386
M_LASER_PLANE_C = 1387
M_LASER_PLANE_D = 1388
M_LASER_SCAN = 1917
M_LAST = 536870912
M_LAST_CORE_ERROR = 56225
M_LAST_DRIVER_HOOK_CONTEXT_ID = 5366
M_LAST_EPOCH_UPDATED_PARAMETERS = 3839
M_LAST_FRAME = 1073741827
M_LAST_GRAB_BUFFER = 4216
M_LAST_GRAB_BUFFER_INDEX = 4377
M_LAST_GRAB_IN_TRUE_BUFFER = 2046
M_LAST_GRAY = 8192
M_LAST_IMAGE = 3
M_LAST_ITERATION = -1
M_LAST_LABEL = 1520
M_LAST_LAYER_SOFTMAX = 262144
M_LAST_LEVEL = 32
M_LAST_PARAM_TYPE = 17
M_LAST_PLATFORM_USE = 15007
M_LAST_PLATFORM_USED = 15007
M_LAST_SCAN = 536870912
M_LAST_TIMER_MODE = 655360
M_LATCH = 8192
M_LATCH0 = 0
M_LATCH1 = 1
M_LATCH10 = 10
M_LATCH11 = 11
M_LATCH12 = 12
M_LATCH13 = 13
M_LATCH14 = 14
M_LATCH15 = 15
M_LATCH16 = 16
M_LATCH2 = 2
M_LATCH3 = 3
M_LATCH4 = 4
M_LATCH5 = 5
M_LATCH6 = 6
M_LATCH7 = 7
M_LATCH8 = 8
M_LATCH9 = 9
M_LATEST_USED_RESET_TRAINING_VALUES = 3954
M_LATIN = 144
M_LATTICE = 3
M_LAYER_RES_COMP_POS = 0
M_LAYOUT_MODIFICATION_COUNT = 5112
M_LAYOUT_MODIFIED = 55
M_LCH_TO_SRGB = 10486267
M_LCH_TO_SRGB_LINEAR = 10486266
M_LEARNING_RATE_DECAY = 3494
M_LEARN_OFFSET = 131072
M_LED_USER = 1053
M_LEFT = 256
M_LEFT_HALF = 256
M_LEFT_TO_RIGHT = 20
M_LEFT_VIEW = 4170
M_LEGACY = 1
M_LEGACY_COMPENSATION = 15143
M_LEGACY_ELLIPSE = 2726
M_LEGACY_MODE = 0
M_LEGACY_RECT = 2725
M_LENGTH = 8192
M_LENGTH_X = 3
M_LENGTH_Y = 4
M_LESS = 6
M_LESS_CONST = 32774
M_LESS_OR_EQUAL = 8
M_LESS_OR_EQUAL_CONST = 32776
M_LETTER = 131072
M_LETTERS = 131072
M_LETTERS_LOWERCASE = 2318
M_LETTERS_UPPERCASE = 2319
M_LETTER_OLD = 2
M_LEVEL = 11
M_LEVEL_1 = 100
M_LEVEL_1B = 102
M_LEVEL_1_1 = 110
M_LEVEL_1_2 = 120
M_LEVEL_1_3 = 130
M_LEVEL_2 = 200
M_LEVEL_2_1 = 210
M_LEVEL_2_2 = 220
M_LEVEL_3 = 300
M_LEVEL_3_1 = 310
M_LEVEL_3_2 = 320
M_LEVEL_4 = 400
M_LEVEL_4_1 = 410
M_LEVEL_4_2 = 420
M_LEVEL_5 = 500
M_LEVEL_5_1 = 510
M_LEVEL_5_2 = 520
M_LEVEL_HIGH = 15
M_LEVEL_HIGH_END_WHEN_INACTIVE = 64
M_LEVEL_LOW = 14
M_LEVEL_LOW_END_WHEN_INACTIVE = 63
M_LICENSE_3DCA = 134217728
M_LICENSE_3DMAP = 65536
M_LICENSE_3DSUP = 65536
M_LICENSE_BEAD = 16
M_LICENSE_BGA = 256
M_LICENSE_BLOB = 512
M_LICENSE_CAL = 1024
M_LICENSE_CLASS = 131072
M_LICENSE_CODE = 8
M_LICENSE_COL = 32768
M_LICENSE_COM = 268435456
M_LICENSE_DA0 = 4294967296
M_LICENSE_DA1 = 8589934592
M_LICENSE_DEBUG = 2
M_LICENSE_DMIL = 67108864
M_LICENSE_DMILC = 2097152
M_LICENSE_DMR = 8192
M_LICENSE_EDGE = 16777216
M_LICENSE_ERROR_2 = 70
M_LICENSE_EXTERNAL = 0
M_LICENSE_FATAL_ERROR = 134218000
M_LICENSE_FINGERPRINT = 20480
M_LICENSE_GPU = 536870912
M_LICENSE_IM = 4
M_LICENSE_INSPECTOR = 4194304
M_LICENSE_INTERFACE = 8388608
M_LICENSE_INTERNAL = -9223372036854775808
M_LICENSE_JPEG2000 = 128
M_LICENSE_JPEGSTD = 4096
M_LICENSE_KEY_WAIT_TIME = 16586
M_LICENSE_LITE = 1
M_LICENSE_LOCAL_CLIENT_CONTACT_LOST = 3
M_LICENSE_MEAS = 16
M_LICENSE_MET = 16384
M_LICENSE_MOD = 64
M_LICENSE_MODULES = 17002
M_LICENSE_NON_TEMP_MODULES = 15055
M_LICENSE_OCR = 2048
M_LICENSE_PAT = 32
M_LICENSE_PERMISSIONS_CHANGED = 6
M_LICENSE_REG = 262144
M_LICENSE_RESERVED = -9223372036854775808
M_LICENSE_SER = 8388608
M_LICENSE_SERVER_CONTACT_LOST = 1
M_LICENSE_SERVER_EVENT = 134217742
M_LICENSE_SERVER_KEY_DISCONNECTED = 2
M_LICENSE_SERVER_OK = 4
M_LICENSE_SERVER_RECONNECT = 7
M_LICENSE_SERVER_SWITCH = 5
M_LICENSE_STR = 8192
M_LICENSE_TEMP_UNLOCKED_MODULES = 15029
M_LICENSE_UNLOCKED_MODULES = 15026
M_LICENSE_VALID_MODULES = 15026
M_LICENSING_ERROR = 58
M_LICENSING_ERROR_2 = 104
M_LICENSING_ERROR_3 = 151
M_LIC_BOARD_TYPE_1394 = 21
M_LIC_BOARD_TYPE_4SIGHTGP = 44
M_LIC_BOARD_TYPE_4SIGHTGPM = 36
M_LIC_BOARD_TYPE_4SIGHTM = 19
M_LIC_BOARD_TYPE_4SIGHTX = 35
M_LIC_BOARD_TYPE_4SIGHTXV6_OR_SS_UNO = 47
M_LIC_BOARD_TYPE_CLARITY_UHD = 8
M_LIC_BOARD_TYPE_CONCORD_GIGE = 33
M_LIC_BOARD_TYPE_CONCORD_POE = 46
M_LIC_BOARD_TYPE_CRONOSPLUS = 27
M_LIC_BOARD_TYPE_GIGE = 15
M_LIC_BOARD_TYPE_INDIO = 23
M_LIC_BOARD_TYPE_IRIS = 30
M_LIC_BOARD_TYPE_IRIS_GT = 37
M_LIC_BOARD_TYPE_IRIS_GTR = 22
M_LIC_BOARD_TYPE_MORPHIS = 29
M_LIC_BOARD_TYPE_MORPHISQXT = 16
M_LIC_BOARD_TYPE_NEXIS = 17
M_LIC_BOARD_TYPE_NEXIS2 = 40
M_LIC_BOARD_TYPE_NEXIS3 = 26
M_LIC_BOARD_TYPE_ORION_HD = 32
M_LIC_BOARD_TYPE_RADIENT = 38
M_LIC_BOARD_TYPE_RADIENTCLHS = 43
M_LIC_BOARD_TYPE_RADIENTCXP = 42
M_LIC_BOARD_TYPE_RADIENTEVCL = 34
M_LIC_BOARD_TYPE_RADIENTPRO = 41
M_LIC_BOARD_TYPE_RAPIXOCL = 28
M_LIC_BOARD_TYPE_RAPIXOCXP = 24
M_LIC_BOARD_TYPE_SOLIOS = 20
M_LIC_BOARD_TYPE_SUPERSIGHT = 39
M_LIC_BOARD_TYPE_SUPERSIGHT_ARBOR = 25
M_LIC_BOARD_TYPE_USB3_VISION = 45
M_LIC_BOARD_TYPE_VIO = 18
M_LIC_TRACE_DMIL_MIN_REQUIREMENT_LOCALHOST = 37
M_LIC_TRACE_DMIL_MIN_REQUIREMENT_NON_LOCALHOST = 38
M_LIC_TRACE_INFO_AMIL_USING_EXISTING_APP = 30
M_LIC_TRACE_INFO_DA_CALLING_GENCODE = 33
M_LIC_TRACE_INFO_DA_CHECKING_LICENSES_FROM_AGENT = 42
M_LIC_TRACE_INFO_DA_CHECKING_LOCAL_LICENSES = 41
M_LIC_TRACE_INFO_DA_EMULATION_END = 29
M_LIC_TRACE_INFO_DA_EMULATION_PERIOD_EXPIRED = 28
M_LIC_TRACE_INFO_DA_EMULATION_START = 27
M_LIC_TRACE_INFO_DA_EXPIRED = 31
M_LIC_TRACE_INFO_DA_OFFICIAL = 32
M_LIC_TRACE_INFO_DA_PRE_REL = 2000
M_LIC_TRACE_INFO_DA_TEMP_ADD_STEP = 6
M_LIC_TRACE_INFO_DA_TEMP_ADD_SUBFLOWCHART = 19
M_LIC_TRACE_INFO_DA_TEMP_EMULATION = 23
M_LIC_TRACE_INFO_DA_TEMP_LOAD_PROJ = 5
M_LIC_TRACE_INFO_DA_TEMP_PASTE_SUBFLOWCHART = 20
M_LIC_TRACE_INFO_DA_UNLICENSED_ADD_STEP = 8
M_LIC_TRACE_INFO_DA_UNLICENSED_ADD_SUBFLOWCHART = 21
M_LIC_TRACE_INFO_DA_UNLICENSED_DEPLOY_PROJ = 18
M_LIC_TRACE_INFO_DA_UNLICENSED_EMULATION = 24
M_LIC_TRACE_INFO_DA_UNLICENSED_IDE_FROM_AGENT = 44
M_LIC_TRACE_INFO_DA_UNLICENSED_LOAD_PROJ = 7
M_LIC_TRACE_INFO_DA_UNLICENSED_LOCAL_IDE = 43
M_LIC_TRACE_INFO_DA_UNLICENSED_PASTE_STEP = 9
M_LIC_TRACE_INFO_DA_UNLICENSED_PASTE_SUBFLOWCHART = 22
M_LIC_TRACE_INFO_DA_USING_LOCAL_PROVISIONAL_MODULES = 45
M_LIC_TRACE_INFO_DA_USING_PROVISIONAL_MODULES_FROM_AGENT = 46
M_LIC_TRACE_INFO_DMIL_CONNECTION_LOCALHOST = 39
M_LIC_TRACE_INFO_DMIL_CONNECTION_NON_LOCALHOST = 40
M_LIC_TRACE_INFO_GENCODE_MATCH = 35
M_LIC_TRACE_INFO_GENCODE_REG_FILE = 34
M_LIC_TRACE_INFO_GENCODE_REMOVING = 36
M_LIC_TRACE_INFO_GPU_ALLOC = 10
M_LIC_TRACE_INFO_GPU_INTERNAL_ALLOC = 13
M_LIC_TRACE_INFO_GUI_NOT_EVEN_MIL_LITE = 3
M_LIC_TRACE_INFO_GUI_NOT_REQUIRED_LIC = 2
M_LIC_TRACE_INFO_INSP_NO_LICENSE = 14
M_LIC_TRACE_INFO_INTELLICAM_NO_LICENSE = 15
M_LIC_TRACE_INFO_LAST = 2365
M_LIC_TRACE_INFO_MACROVISION_DETECTED = 1
M_LIC_TRACE_INFO_MACROVISION_OK = 4
M_LIC_TRACE_INFO_NET_WRAP_EXPIRED = 16
M_LIC_TRACE_INFO_NET_WRAP_OFFICIAL = 17
M_LIC_TRACE_INFO_NET_WRAP_PRE_REL = 1000
M_LIGHTING_BRIGHT_FIELD = 4382
M_LIGHTING_BRIGHT_FIELD_EFFECTIVE_TIME = 4421
M_LIGHTING_BRIGHT_FIELD_HIDRIVE = 4419
M_LIGHTING_BRIGHT_FIELD_HIDRIVE_TIME = 4420
M_LIGHTING_BRIGHT_FIELD_OFFSET = 4418
M_LIGHTING_BRIGHT_FIELD_OPTIMIZED_EXPOSURE_TIME = 4422
M_LIGHTING_BRIGHT_FIELD_OPTIMIZED_INTENSITY = 4423
M_LIGHTING_DARK_FIELD = 4381
M_LIGHTING_DARK_FIELD_EFFECTIVE_TIME = 4424
M_LIGHTING_DARK_FIELD_OPTIMIZED_EXPOSURE_TIME = 4425
M_LIGHTING_DARK_FIELD_OPTIMIZED_INTENSITY = 4426
M_LIGHT_BRIGHT_FIELD = 4382
M_LIGHT_DARK_FIELD = 4381
M_LIGHT_INDOOR = 0
M_LIGHT_OUTDOOR = 1
M_LIGHT_VECTOR_COMPONENT_1 = 2695
M_LIGHT_VECTOR_COMPONENT_2 = 2696
M_LIGHT_VECTOR_COMPONENT_3 = 2697
M_LIGHT_VECTOR_TYPE = 2694
M_LIMITATION_ERROR = 56
M_LINE = 128
M_LINEAR_COMPONENT = 1073741824
M_LINEAR_FILTER_IIR_CONTEXT = 19
M_LINEAR_INTERPOLATION = 1
M_LINES = 128
M_LINESCAN = 2
M_LINE_A = 12288
M_LINE_ALREADY_EXTRACTED = 1339
M_LINE_ANY_EDGE = 1792
M_LINE_B = 12289
M_LINE_BISECTOR_TYPE = 2535
M_LINE_C = 12290
M_LINE_CHAR_SEPARATOR = 109
M_LINE_ENDS_ARROW_A_ON_END = 12288
M_LINE_ENDS_CIRCLES = 28672
M_LINE_ENDS_CLOSING_ARROWS = 20480
M_LINE_ENDS_DIMENSION = 1641
M_LINE_ENDS_DIMENSION_INPUT_UNITS = 1639
M_LINE_ENDS_H_BOTH_ENDS = 8192
M_LINE_ENDS_MASK = 61440
M_LINE_ENDS_OPENING_ARROWS = 24576
M_LINE_ENDS_PLAIN = 4096
M_LINE_ENDS_STYLE = 1640
M_LINE_END_POINT_FIRST = 16
M_LINE_END_POINT_SECOND = 32
M_LINE_EQUATION = 8388608
M_LINE_EQUATION_SLOPE = 8392704
M_LINE_FALLING_EDGE = 1536
M_LINE_FIT = 80
M_LINE_FIT_A = 82
M_LINE_FIT_B = 83
M_LINE_FIT_C = 31
M_LINE_FIT_ERROR = 32
M_LINE_INDEX = 8716288
M_LINE_LIST = 16
M_LINE_NEGATIVE_BOX = 16384
M_LINE_PRESEARCH = 2801
M_LINE_RISING_EDGE = 1280
M_LINE_THICKNESS = 4001
M_LINE_TYPE = 2824
M_LINK = 1
M_LINK_TOOL_AND_CAMERA = 155
M_LINK_TO_PARENT = 1774
M_LINUX_METHOD = 524288
M_LINUX_MODE = 524288
M_LINUX_MXIMAGE = 576460752303423488
M_LIST = 134217728
M_LIST_TYPE = 201
M_LITTLE_ENDIAN = 512
M_LIVE_GRAB = 2034
M_LIVE_GRAB_DDRAW = 2067
M_LIVE_GRAB_WHEN_DISPLAY_DOES_NOT_MATCH = 2035
M_LIVE_GRAB_WHEN_NOT_VISIBLE = 2082
M_LIVE_VIDEO = 8796093022208
M_LN = 261
M_LOAD = 1
M_LOAD_CHARACTER = 8
M_LOAD_CONSTRAINT = 2
M_LOAD_CONTROL = 4
M_LOCAL = 16777216
M_LOCALIZATION_NB_ITERATIONS_MAX = 1667
M_LOCALIZATION_NB_OUTLIERS_MAX = 1669
M_LOCAL_CONTRAST = 2699
M_LOCAL_DIMENSION = 1884
M_LOCAL_DISPLAY = 16
M_LOCAL_DISPLAY_CONTROL = 1073741824
M_LOCAL_ENGINE = 200
M_LOCAL_FRAME = 131
M_LOCAL_HOOK_RANGE1_END = 4
M_LOCAL_HOOK_RANGE1_START = 1
M_LOCAL_HOOK_RANGE2_END = 14
M_LOCAL_HOOK_RANGE2_START = 12
M_LOCAL_HOOK_RANGE3_END = 39
M_LOCAL_HOOK_RANGE3_START = 17
M_LOCAL_HOOK_RANGE4_END = 43
M_LOCAL_HOOK_RANGE4_START = 43
M_LOCAL_HOOK_RANGE5_END = 60
M_LOCAL_HOOK_RANGE5_START = 45
M_LOCAL_HOOK_RANGE6_END = 73
M_LOCAL_HOOK_RANGE6_START = 64
M_LOCAL_MAX_NOT_STRICT = 201195520
M_LOCAL_MAX_STRICT_MEDIUM = 185466880
M_LOCAL_MEAN = 1882
M_LOCAL_MIN_NOT_STRICT = 167641088
M_LOCAL_MIN_STRICT_MEDIUM = 151912448
M_LOCAL_SHAPE = 2698
M_LOCAL_WITH_RESEGMENTATION = 954
M_LOCATE_EVENT_EXTREMUM_MODE_SHIFT = 17
M_LOCATE_PEAK_1D_CONTEXT = 12
M_LOCATE_PEAK_1D_CONTEXT_ID = 2003
M_LOCATE_PEAK_1D_RESULT = 35184372088832
M_LOCATION = 1048
M_LOCATION_DELTA = 1003
M_LOCK = 20480
M_LOCKABLE = 8255
M_LOCK_ACCESS_MASK = 3
M_LOCK_TRY = 28672
M_LOCK_TYPE = 8452
M_LOCK_TYPE_MASK = 4092
M_LOCK_UNLOCK_MASK = 4095
M_LOG = 269
M_LOG10 = 262
M_LOG2 = 263
M_LOGARITHMIC = 4
M_LOGICAL = 134217728
M_LOGICAL_TO_PHYSICAL_ADDRESS = 7501
M_LOGIC_BLOCK = 288
M_LOGIC_BLOCK0 = 288
M_LOGIC_BLOCK1 = 289
M_LOGIC_BLOCK10 = 298
M_LOGIC_BLOCK11 = 299
M_LOGIC_BLOCK12 = 300
M_LOGIC_BLOCK13 = 301
M_LOGIC_BLOCK14 = 302
M_LOGIC_BLOCK15 = 303
M_LOGIC_BLOCK2 = 290
M_LOGIC_BLOCK3 = 291
M_LOGIC_BLOCK4 = 292
M_LOGIC_BLOCK5 = 293
M_LOGIC_BLOCK6 = 294
M_LOGIC_BLOCK7 = 295
M_LOGIC_BLOCK8 = 296
M_LOGIC_BLOCK9 = 297
M_LOGIC_BLOCK_FUNCTION = 4896
M_LOGIC_BLOCK_INPUT_SOURCE0 = 4928
M_LOGIC_BLOCK_INPUT_SOURCE1 = 4960
M_LOG_CONST = 267
M_LOG_DISABLE = 0
M_LOG_ENABLE = 1
M_LOG_SCALE = 1024
M_LOSING_VIDEO_MEMORY = 10045
M_LOSSLESS = 7
M_LOSSY = 1
M_LOW = 1
M_LOWERCASE = 32768
M_LOWERCASE_OLD = 32768
M_LOWER_HALF = 2048
M_LOWER_RESERVED_COLOR_END = 10022
M_LOWER_RESERVED_COLOR_START = 10021
M_LOWEST = 6
M_LOW_LATENCY = 4096
M_LOW_LEVEL_API_OBJECT = 1024
M_LOW_LEVEL_SYSTEM_ID = 2024
M_LOW_PASS_0 = 1
M_LOW_PASS_1 = 2
M_LOW_PASS_2 = 3
M_LOW_SPEED_21 = 8
M_LOW_SPEED_42 = 16
M_LUMINANCE = 131072
M_LUT = 262144
M_LUT_ADDRESS_ZOOM_2X = 3
M_LUT_ID = 1102
M_LUT_MAP = 2097152
M_LUT_PALETTE0 = 0
M_LUT_PALETTE1 = 1
M_LUT_PALETTE2 = 2
M_LUT_PALETTE3 = 3
M_LUT_PALETTE4 = 4
M_LUT_PALETTE5 = 5
M_LUT_PALETTE6 = 6
M_LUT_PALETTE7 = 7
M_LUT_PRESENT = 6000
M_LUT_REPLICATE_2X = 1
M_LUT_REPLICATE_4X = 2
M_LUT_SUPPORTED = 3033
M_LVDS = 2
M_L_TO_RGB = 10485764
M_MADI_METHOD = 8
M_MAD_BASED_VALUE = -41
M_MAGNITUDE = 256
M_MAGNITUDE_ID = 34816
M_MAGNITUDE_TYPE = 10
M_MAHALANOBIS = 5
M_MAHALANOBIS_SAMPLE = 5
M_MAHALANOBIS_SAMPLE_SQR = 25
M_MAHALANOBIS_TARGET = 8
M_MAHALANOBIS_TARGET_SQR = 28
M_MAIN_D3D10_OBJECT = 8519
M_MAIN_D3D11_OBJECT = 8539
M_MAIN_D3D9_OBJECT = 4579
M_MAIN_DDRAW_OBJECT = 4501
M_MAJOR_VERSION = 8193
M_MAKE_FILE_PATHS_ABSOLUTE = 3750
M_MAKE_FILE_PATHS_RELATIVE = 3749
M_MANHATTAN = 3
M_MANHATTAN_DISTANCE_TO_SURFACE = 3736
M_MANHATTAN_SQR = 23
M_MANUAL = 1
M_MANUAL_RESET = 16384
M_MAP = 1018
M_MAPPABLE = 281474976710656
M_MAP_HOST_ADDRESS = 1031
M_MAP_REMOTE = 1020
M_MAP_VIDEO_MEMORY = 1023
M_MAP_VIDEO_RANGE_A_LA_PIECE = 1021
M_MARKER = 504
M_MARKER_REFERENCE = 91136
M_MARKER_REFERENCE_INPUT_UNITS = 1393
M_MARKER_TYPE = 99328
M_MASK = 4096
M_MASK_CONTRAST_ENHANCEMENT = 620
M_MASK_ID = 67633152
M_MASK_IMAGE = 1020
M_MASK_IMAGE_ATTRIBUTE = 114
M_MASK_IMAGE_HEIGHT = 112
M_MASK_IMAGE_NB_BANDS = 110
M_MASK_IMAGE_TYPE = 113
M_MASK_IMAGE_WIDTH = 111
M_MASK_MIM_INQUIRE_TYPE = 131071
M_MASK_MODIFIED = 2052
M_MASK_SIZE_X = 29
M_MASK_SIZE_Y = 30
M_MASTER = 1
M_MATCH = 6
M_MATCH_CONTEXT = 7
M_MATCH_INDEX = 820
M_MATCH_LABEL = 822
M_MATCH_METHOD = 50
M_MATCH_MODE = 50
M_MATCH_SAMPLE_COLOR_BAND_0 = 145
M_MATCH_SAMPLE_COLOR_BAND_1 = 146
M_MATCH_SAMPLE_COLOR_BAND_2 = 147
M_MATHEMATICAL_EXCEPTION = 8
M_MATRIX_OF_CONFUSION = 959
M_MATRIX_OF_CONFUSION_SIZE = 958
M_MATRIX_OF_COST = 973
M_MATRIX_OF_COST_SIZE = 972
M_MATRIX_PROFILE_PLANE_TO_WORLD = 3899
M_MATRIX_WORLD_TO_PROFILE_PLANE = 3898
M_MATROX_BOARD_FINGERPRINT = 21472
M_MAX = 67108864
M_MAXICODE = 8
M_MAXICODE_NAME = MIL_TEXT("Maxicode")
M_MAXIMA_FILL = 8
M_MAXIMIZE_AREA = -9997
M_MAXIMUM_CALIBRATED_REFLECTANCE = 32833
M_MAXIMUM_ERN = 40967
M_MAXIMUM_NUMBER_NEIGHBORS = 3316
M_MAXIMUM_ORIENTATION_ANGLE_DIFFERENCE = 3315
M_MAXIMUM_PIXEL_ERROR = 8192
M_MAXIMUM_REFLECTANCE = 40963
M_MAXIMUM_VISIBLE_DEST_SIZE_X = 10180
M_MAXIMUM_VISIBLE_DEST_SIZE_Y = 10181
M_MAXIMUM_WAIT_OBJECTS = 64
M_MAXIMUM_WORLD_ERROR = 32768
M_MAX_ABS = 8388608
M_MAX_ABS_VALUE = 8
M_MAX_ASSOCIATION_DISTANCE = 1503
M_MAX_ASSOCIATION_DISTANCE_INPUT_UNITS = 1584
M_MAX_BLOBS = 18
M_MAX_BLOBS_END = 57
M_MAX_BYTE_COUNT = 32764
M_MAX_CHAR_SIZE_X = 823
M_MAX_CHAR_SIZE_Y = 825
M_MAX_CHAR_WIDTH = 50331648
M_MAX_CONST = 67141632
M_MAX_CURSOR = 63
M_MAX_DEPTH = 4294967295
M_MAX_DISTANCE = 12
M_MAX_DISTANCE_POINT = 38
M_MAX_DISTANCE_TO_NEAREST_NEIGHBOR = 3443
M_MAX_DISTANCE_TO_SOURCE = 3321
M_MAX_EPOCH = 3479
M_MAX_FINGERPRINTS_PER_TYPE = 16
M_MAX_FRAMES = 17
M_MAX_GAP = 1683
M_MAX_IMAGE = 2702
M_MAX_INDEX_VALUE = 2197
M_MAX_INITIAL_PEAKS = 1418
M_MAX_INSTALLED_SYSTEM_TYPES = 64
M_MAX_INTENSITY = 2251
M_MAX_INTENSITY_MODE = 2250
M_MAX_INTERMEDIATES = 18
M_MAX_INTERNAL_BUFFERS = 8
M_MAX_ITERATIONS = 1504
M_MAX_ITERATIONS_REACHED = 1965
M_MAX_LABEL = 16
M_MAX_LABEL_VALUE = 2939
M_MAX_LENGTH_OF_SUPPORTED_CODE_TYPES_NAMES = 2702
M_MAX_LENGTH_OF_SUPPORTED_CODE_TYPES_NAMES_1D = 2706
M_MAX_LENGTH_OF_SUPPORTED_CODE_TYPES_NAMES_2D = 2710
M_MAX_LENGTH_OF_SUPPORTED_CODE_TYPES_NAMES_DETECT = 2930
M_MAX_LENGTH_OF_SUPPORTED_CODE_TYPES_NAMES_POSTAL = 2776
M_MAX_LEVEL = 255
M_MAX_NB_GRAB_BUFFERS = 8
M_MAX_NB_OF_PORTS = 255
M_MAX_NB_OF_PUS = 512
M_MAX_NORMALIZE = 0
M_MAX_NUMBER_OF_CLASSES = 2946
M_MAX_OF_MIN_DISTANCE_POINT = 67
M_MAX_PIXEL = 31
M_MAX_PLATFORM_USED = 15060
M_MAX_POINT_PAIR_DISTANCE = 1948
M_MAX_POSSIBLE_INDEX_VALUE = 2097151
M_MAX_POSSIBLE_LABEL_VALUE = 2097151
M_MAX_POSSIBLE_VALUE = 268435457
M_MAX_REFRESH_RATE = 33554432
M_MAX_REPORT_STRING_LENGTH = 128
M_MAX_SCORE = 100
M_MAX_SYSTEMS_PER_TYPE = 16
M_MAX_TIMEOUT = 16777215
M_MAX_TREE_DEPTH = 3318
M_MAX_UART_NB = 255
M_MAX_UNIT_IDLE_TIME = 2307
M_MAX_VALUE = 2199023255552
M_MAX_VIDEO_DEVICE = 64
M_MAX_WEBSOCKET_SERVER = 5
M_MAX_X = 3385
M_MAX_Y = 3386
M_MAX_Z = 3387
M_MEAN = 134217728
M_MEAN_CHAR_WIDTH = 33554432
M_MEAN_CURVATURE = 2692
M_MEAN_DECREASE_IMPURITY = 3614
M_MEAN_LIGHT_CALIBRATION = 1636
M_MEAN_LIGHT_TARGET = 1637
M_MEAN_PIXEL = 32
M_MEASURED = 1
M_MEASURED_FEATURES = 258
M_MEAS_CONTEXT = 538968068
M_MEAS_DRAW_INDEX_BIT_SHIFT = 14
M_MEAS_MARKER = 538968065
M_MEAS_OBJECT = 538968064
M_MEAS_RESULT = 538968066
M_MEDIAN = 65536
M_MEDIUM = 2
M_MEGABUFFER_GRAB = 134217728
M_MEGA_BUFFER_LOW_LIMIT = 10179
M_MEGA_BUFFER_LOW_LIMIT_X = 10207
M_MEGA_BUFFER_SIZE_X_TO_USE = 10565
M_MEGA_BUFFER_SIZE_Y_TO_USE = 10566
M_MEMORY = 15120
M_MEMORY_ALLOC_ALIGNMENT = 15516
M_MEMORY_ALLOC_ALIGNMENT_VALUE = 128
M_MEMORY_ALLOC_PITCH_BYTE = 15515
M_MEMORY_ALLOC_PITCH_BYTE_VALUE = 1
M_MEMORY_ALLOC_POST_PADDING = 15514
M_MEMORY_ALLOC_POST_PADDING_VALUE = 32
M_MEMORY_ALLOC_PRE_PADDING = 15513
M_MEMORY_ALLOC_PRE_PADDING_VALUE = 32
M_MEMORY_BANK_0 = 4503599627370496
M_MEMORY_BANK_1 = 9007199254740992
M_MEMORY_BANK_2 = 13510798882111488
M_MEMORY_BANK_3 = 18014398509481984
M_MEMORY_BANK_4 = 22517998136852480
M_MEMORY_BANK_5 = 27021597764222976
M_MEMORY_BANK_6 = 31525197391593472
M_MEMORY_BANK_AFFINITY_MASK = 1596
M_MEMORY_BANK_AFFINITY_MASK_ARRAY_SIZE = 1602
M_MEMORY_BANK_CORE_AFFINITY_MASK = 1597
M_MEMORY_BANK_DEFAULT = 0
M_MEMORY_BANK_MASK = 31525197391593472
M_MEMORY_BANK_NUM = 1595
M_MEMORY_BANK_OFFSET = 52
M_MEMORY_FREE = 2324
M_MEMORY_FREE_BANK_0 = 2354
M_MEMORY_FREE_BANK_1 = 2355
M_MEMORY_FREE_BANK_2 = 2356
M_MEMORY_FREE_BANK_3 = 2357
M_MEMORY_LIMIT = 908
M_MEMORY_LIMIT_REACHED = 913
M_MEMORY_OFF_SCREEN_AVAILABLE = 2112
M_MEMORY_SIZE = 2323
M_MEMORY_SIZE_BANK_0 = 2350
M_MEMORY_SIZE_BANK_1 = 2351
M_MEMORY_SIZE_BANK_2 = 2352
M_MEMORY_SIZE_BANK_3 = 2353
M_MEM_MAN_INQ_ERROR = 111
M_MERGE = 64
M_MERGE_MODEL = 131072
M_MESH = 3994
M_MESH_BASED = 3301
M_MESH_CONTEXT = 3314
M_MESH_CONTEXT_ORGANIZED = 10489080
M_MESH_CONTEXT_SMOOTHED = 10488857
M_MESH_MODE = 3430
M_MESH_ORGANIZED = 3320
M_MESH_SMOOTHED = 3097
M_MESH_STEP_X = 3322
M_MESH_STEP_Y = 3323
M_MESH_VALID_NEIGHBORS = 16
M_MESH_VALID_POINTS = 8
M_MESSAGE = 536870912
M_MESSAGE_COUNT = 15
M_MESSAGE_LENGTH = 16
M_MESSAGE_MAILBOX = 140737488355328
M_MESSAGE_NOT_PROCESSED = 1658
M_MESSAGE_PROCESSED = 1657
M_MESSAGE_PTR = 101
M_MESSAGE_READ_ASYNC = 2061
M_MESSAGE_RECEIVED = 2053
M_MESSAGE_SIZE_IN = 102
M_MESSAGE_SIZE_OUT = 103
M_MESSAGE_STATUS = 100
M_MESSAGE_TAG = 104
M_METADATA_LINE = 5354
M_METERS = 2452
M_METHOD = 103
M_METHOD_1 = 4096
M_METHOD_2 = 8192
M_METHOD_CONVERT = 535
M_METHOD_CONVERT_OLD = 108
M_METROLOGY_COMPATIBLE = 98
M_MET_CONTEXT = 4831838209
M_MET_DERIVED_GEOMETRY_REGION = 4831838212
M_MET_FEATURE_ID_MAX = 16777215
M_MET_OBJECT = 4831838208
M_MET_RESULT = 4831838210
M_MET_TOLERANCE_ID_MAX = 16777215
M_MICROMETERS = 2449
M_MICROPDF417 = 8388608
M_MICROPDF417_NAME = MIL_TEXT("MicroPDF417")
M_MICROQRCODE = 67108866
M_MICROQRCODE_NAME = MIL_TEXT("MicroQRCode")
M_MIDDLE = 36
M_MIL = 1
M_MILCE_ALLOC_IN_DMA_SIZE = 15040
M_MILCE_ALLOC_IN_MMF_AUTO_COMMIT = 15042
M_MILCE_ALLOC_IN_MMF_SIZE = 15041
M_MILDISPLAY_DLL_IN_DEBUG_MODE = 15403
M_MILES = 2456
M_MILGRABC_VERSION = 4385
M_MILIM_FUNCTION_DEPRECATION_WARNING = 1
M_MILLIMETER = 2450
M_MILLIMETERS = 2450
M_MILS = 1
M_MILUTIL_COMPILATION_TYPE = 15957
M_MIL_BUFFER_WINDOW = 2
M_MIL_CURRENT_ASCII_VERSION = MIL_TEXT("10.00")
M_MIL_CURRENT_INT_VERSION = 4096
M_MIL_CURRENT_MT_VERSION = MIL_TEXT("10.00")
M_MIL_CURRENT_VERSION = 10
M_MIL_DIRECTORY_CONTEXTS = 16854
M_MIL_DIRECTORY_EXAMPLES = 16852
M_MIL_DIRECTORY_IMAGES = 16853
M_MIL_DIRECTORY_INSTALL = 16851
M_MIL_DIRECTX_DLL_LOAD = 1024
M_MIL_DISPLAY_DLL_LOAD = 512
M_MIL_DISPLAY_WND_CLASS_NAME = MIL_TEXT("MIL Default Window")
M_MIL_DLL_COMPILATION_TYPE = 15956
M_MIL_DLL_IN_DEBUG_MODE = 38
M_MIL_EXTENSIONS = MIL_TEXT("*.mim")
M_MIL_FILE_ERROR = 21
M_MIL_FILE_ERROR_2 = 22
M_MIL_FILE_ERROR_3 = 23
M_MIL_FILE_ERROR_4 = 65
M_MIL_HOOK_ERROR = 186
M_MIL_ID = 131072
M_MIL_ID_INTERNAL = 1049
M_MIL_ID_PROXY_OBJECT = 4294967296
M_MIL_KEY_VALUE = 9
M_MIL_LITE = 0
M_MIL_METHOD = 16777216
M_MIL_MODE = 16777216
M_MIL_NATIVE = 21
M_MIL_NET_INFO_PTR = 133
M_MIL_SETUP = 2
M_MIL_SUPPORT_CLASS_CNN_TRAINING = 1
M_MIL_THREAD = 4
M_MIL_TIFF = 1
M_MIL_TRACE_FILENAME = 15024
M_MIL_UNICODE_API = 1
M_MIL_UNIQUE_NUMBER = 15023
M_MIL_USE_64BIT = 1
M_MIL_USE_APP_ALLOC_DEFAULT = 0
M_MIL_USE_DIRECTX_SERVICE = 1
M_MIL_USE_INT64_DATA_FILES = 0
M_MIL_USE_INT64_ID = 1
M_MIL_USE_OS = 1
M_MIL_USE_TTF_UNICODE = 1
M_MIL_USE_UNICODE = 1
M_MIL_USE_WINDOWS = 1
M_MIL_WARN_ON_DEPRECATED = 1
M_MIL_WARN_ON_DEPRECATED_MBLOB = 1
M_MIL_WARN_ON_DEPRECATED_MCODE = 1
M_MIL_WARN_ON_DEPRECATED_MIL3DMAP = 1
M_MIL_WARN_ON_DEPRECATED_MOS = 1
M_MIL_WARN_ON_DEPRECATED_MPAT = 1
M_MIL_WINDOW = 134217728
M_MIM_DRAW_WAVELET = 163
M_MIM_GET_RES_SINGLE = 162
M_MIN = 33554432
M_MINIMAL = 4096
M_MINIMA_FILL = 4
M_MINIMUM_CALIBRATED_REFLECTANCE = 32834
M_MINIMUM_CONTRAST = 600
M_MINIMUM_DISPLAY_SIZE_X = 10138
M_MINIMUM_DISPLAY_SIZE_Y = 10139
M_MINIMUM_EDGE_CONTRAST = 40961
M_MINIMUM_EDGE_CONTRAST_GRADE = 36872
M_MINIMUM_LSIDE_LENGTH = 1684
M_MINIMUM_REFLECTANCE = 40962
M_MINIMUM_REFLECTANCE_GRADE = 36871
M_MINI_BATCH_INDEX = 3679
M_MINI_BATCH_LOSS = 3680
M_MINI_BATCH_PER_EPOCH = 3737
M_MINI_BATCH_SIZE = 3480
M_MINI_BATCH_TRAINED = 65026
M_MINOR_VERSION = 8192
M_MIN_ABS = 2097152
M_MIN_ABS_VALUE = 4
M_MIN_AREA_BOX = 128
M_MIN_AREA_BOX_ANGLE = 142
M_MIN_AREA_BOX_AREA = 137
M_MIN_AREA_BOX_CENTER_X = 140
M_MIN_AREA_BOX_CENTER_Y = 141
M_MIN_AREA_BOX_HEIGHT = 159
M_MIN_AREA_BOX_PERIMETER = 138
M_MIN_AREA_BOX_WIDTH = 158
M_MIN_AREA_BOX_X1 = 129
M_MIN_AREA_BOX_X2 = 131
M_MIN_AREA_BOX_X3 = 133
M_MIN_AREA_BOX_X4 = 135
M_MIN_AREA_BOX_Y1 = 130
M_MIN_AREA_BOX_Y2 = 139
M_MIN_AREA_BOX_Y3 = 134
M_MIN_AREA_BOX_Y4 = 136
M_MIN_CHAR_SIZE_X = 822
M_MIN_CHAR_SIZE_Y = 824
M_MIN_CHAR_WIDTH = 16777216
M_MIN_CONST = 33587200
M_MIN_CONTRAST = 600
M_MIN_CONTRAST_MODE = 2247
M_MIN_DISTANCE_TO_NEAREST_NEIGHBOR = 3441
M_MIN_DIST_VOTE = 51
M_MIN_FERETS = 2
M_MIN_IMAGE = 2701
M_MIN_IMPURITY_DECREASE = 3528
M_MIN_INTENSITY = 12
M_MIN_INTENSITY_MODE = 2248
M_MIN_LEVEL = 0
M_MIN_MAX_OF_SELECTED_BUFFER_CHANGED = 10041
M_MIN_NUMBER_OF_ENTRIES_LEAF = 3525
M_MIN_NUMBER_OF_ENTRIES_LEAF_MODE = 3524
M_MIN_NUMBER_OF_ENTRIES_SPLIT = 3522
M_MIN_NUMBER_OF_ENTRIES_SPLIT_MODE = 3519
M_MIN_OVERLAP = 4
M_MIN_PERIMETER_BOX = 143
M_MIN_PERIMETER_BOX_ANGLE = 156
M_MIN_PERIMETER_BOX_AREA = 152
M_MIN_PERIMETER_BOX_CENTER_X = 154
M_MIN_PERIMETER_BOX_CENTER_Y = 155
M_MIN_PERIMETER_BOX_HEIGHT = 161
M_MIN_PERIMETER_BOX_PERIMETER = 153
M_MIN_PERIMETER_BOX_WIDTH = 160
M_MIN_PERIMETER_BOX_X1 = 157
M_MIN_PERIMETER_BOX_X2 = 146
M_MIN_PERIMETER_BOX_X3 = 148
M_MIN_PERIMETER_BOX_X4 = 150
M_MIN_PERIMETER_BOX_Y1 = 145
M_MIN_PERIMETER_BOX_Y2 = 147
M_MIN_PERIMETER_BOX_Y3 = 149
M_MIN_PERIMETER_BOX_Y4 = 151
M_MIN_PIXEL = 30
M_MIN_SEPARATION_ANGLE = 69
M_MIN_SEPARATION_ASPECT_RATIO = 2016
M_MIN_SEPARATION_SCALE = 68
M_MIN_SEPARATION_X = 35
M_MIN_SEPARATION_Y = 36
M_MIN_SIDE_COVERAGE = 2802
M_MIN_VALUE = 1099511627776
M_MIN_WEIGHT_FRACTION_LEAF = 3523
M_MIN_X = 3382
M_MIN_Y = 3383
M_MIN_Z = 3384
M_MIRROR = 16777313
M_MISC_ERROR_END = 57050
M_MISC_ERROR_START = 57000
M_MISSING_M_DISP_ERROR = 144
M_MISSING_M_GRAB_ERROR = 146
M_MISSING_M_PROC_ERROR = 145
M_MIXED = 1280
M_MIXED_VERTEXPROCESSING = 262144
M_MMX_ENABLED = 268435456
M_MMX_EXTRA_BYTES = 32
M_MODE = 103
M_MODE1 = 1
M_MODEL = 65536
M_MODEL_ASPECT_RATIO = 2219
M_MODEL_ASPECT_RATIO_MAX_FACTOR = 2221
M_MODEL_ASPECT_RATIO_MIN_FACTOR = 2220
M_MODEL_COVERAGE = 5632
M_MODEL_FINDER_COMPATIBLE = 19
M_MODEL_IMAGE = 1019
M_MODEL_IMAGE_ATTRIBUTE = 109
M_MODEL_IMAGE_HEIGHT = 107
M_MODEL_IMAGE_NB_BANDS = 105
M_MODEL_IMAGE_TYPE = 108
M_MODEL_IMAGE_WIDTH = 106
M_MODEL_LIST = 46
M_MODEL_MAX_LEVEL = 1419
M_MODEL_MOD = 48
M_MODEL_OVERLAP = 1947
M_MODEL_PAT = 64
M_MODEL_STEP = 33
M_MODEL_TYPE = 162
M_MODE_CONTROL = 65536
M_MODE_RESIZE = 2684
M_MODE_RESIZE_ALT = 264828
M_MODE_RESIZE_CTRL = 133756
M_MODE_RESIZE_SECONDARY_DIMENSION = 2732
M_MODE_RESIZE_SECONDARY_DIMENSION_ALT = 264876
M_MODE_RESIZE_SECONDARY_DIMENSION_CTRL = 133804
M_MODE_RESIZE_SECONDARY_DIMENSION_SHIFT = 68268
M_MODE_RESIZE_SHIFT = 68220
M_MODE_ROTATE = 2685
M_MODE_ROTATE_ALT = 264829
M_MODE_ROTATE_CTRL = 133757
M_MODE_ROTATE_SHIFT = 68221
M_MODE_TRANSLATE = 2686
M_MODE_TRANSLATE_ALT = 264830
M_MODE_TRANSLATE_CTRL = 133758
M_MODE_TRANSLATE_SHIFT = 68222
M_MODIFICATION_COUNT = 5010
M_MODIFICATION_HOOK = 5082
M_MODIFIED = 4096
M_MODIFIED_ACCESS_COMMAND_PROMPT = 4
M_MODIFIED_ACCESS_OFF = 0
M_MODIFIED_ACCESS_ON = 2
M_MODIFIED_ACCESS_RECTANGULAR_OFF = 0
M_MODIFIED_ACCESS_RECTANGULAR_ON = 1
M_MODIFIED_APP_MENU = 512
M_MODIFIED_BUFFER = 1073741824
M_MODIFIED_BUFFER_DIGITIZER = 21
M_MODIFIED_BUFFER_DIGITIZER_CORRUPT = 23
M_MODIFIED_BUFFER_DIGITIZER_ERROR = 22
M_MODIFIED_BUFFER_DISPLAYABLE_CHANGE = 54
M_MODIFIED_BUFFER_ERROR = 19
M_MODIFIED_BUFFER_HOOK_MODE = 2447
M_MODIFIED_BUFFER_INTERNAL = 12
M_MODIFIED_BY_DIRECTX = 5400
M_MODIFIED_CLOSE_MENUITEM = 6
M_MODIFIED_DIB = 2
M_MODIFIED_DIB_CREATION = 5
M_MODIFIED_DIB_DESTRUCTION = 6
M_MODIFIED_DIGITIZER = 33554432
M_MODIFIED_DIGITIZER_CORRUPT = 8388608
M_MODIFIED_DIGITIZER_WITH_ERROR = 16777216
M_MODIFIED_DISPLAY = 39
M_MODIFIED_LUT = 1
M_MODIFIED_MAXIMIZE_MENUITEM = 5
M_MODIFIED_MENUBAR_MENUITEM = 8
M_MODIFIED_MINIMIZE_MENUITEM = 4
M_MODIFIED_MOVE_MENUITEM = 2
M_MODIFIED_NOZOOM_MENUITEM = 12
M_MODIFIED_OFF = 0
M_MODIFIED_ON = 1
M_MODIFIED_PAN = 4
M_MODIFIED_REGION = 25
M_MODIFIED_RESTORE_MENUITEM = 1
M_MODIFIED_SIZE_MENUITEM = 3
M_MODIFIED_STATE_FROM_PARENT = 16
M_MODIFIED_STATE_FROM_WINDOW = 0
M_MODIFIED_SYS_MENU = 256
M_MODIFIED_TASKLIST_MENUITEM = 7
M_MODIFIED_TITLEOFF_MENUITEM = 9
M_MODIFIED_USER_APP_MENU = 65536
M_MODIFIED_WINDOW_ACTIVE = 17
M_MODIFIED_WINDOW_CLIP_LIST = 19
M_MODIFIED_WINDOW_CREATION = 7
M_MODIFIED_WINDOW_DESTRUCTION = 8
M_MODIFIED_WINDOW_ENABLE = 18
M_MODIFIED_WINDOW_ICONIZED = 12
M_MODIFIED_WINDOW_LOCATION = 9
M_MODIFIED_WINDOW_MENU = 15
M_MODIFIED_WINDOW_OVERLAP = 11
M_MODIFIED_WINDOW_PAINT = 16
M_MODIFIED_WINDOW_PAN = 14
M_MODIFIED_WINDOW_ZOOM = 13
M_MODIFIED_WITH_ERROR = 536870912
M_MODIFIED_ZOOM = 3
M_MODIFIED_ZOOMIN_MENUITEM = 10
M_MODIFIED_ZOOMOUT_MENUITEM = 11
M_MODIFY = 999
M_MODULATION = 40964
M_MODULATION_GRADE = 36873
M_MOD_DEFINE_COMPATIBLE = 330
M_MOD_GEOMETRIC = 603979777
M_MOD_GEOMETRIC_CONTROLLED = 603979784
M_MOD_OBJECT = 603979776
M_MOD_RESULT = 603979780
M_MOD_SHAPE_CIRCLE_CONTEXT = 603979808
M_MOD_SHAPE_ELLIPSE_CONTEXT = 603979840
M_MOD_SHAPE_RECTANGLE_CONTEXT = 603979904
M_MOD_SHAPE_RESULT = 603979792
M_MOD_SHAPE_SEGMENT_CONTEXT = 603980032
M_MOMENT_CENTRAL_X0_Y2 = 42
M_MOMENT_CENTRAL_X1_Y1 = 41
M_MOMENT_CENTRAL_X2_Y0 = 43
M_MOMENT_ELONGATION = 50
M_MOMENT_ELONGATION_ANGLE = 999
M_MOMENT_FIRST_ORDER = 2478
M_MOMENT_GENERAL = 2048
M_MOMENT_GENERAL_MODE = 2471
M_MOMENT_GENERAL_ORDER_X = 2469
M_MOMENT_GENERAL_ORDER_Y = 2470
M_MOMENT_SECOND_ORDER = 2479
M_MOMENT_X0_Y1 = 36
M_MOMENT_X0_Y2 = 39
M_MOMENT_X1_Y0 = 37
M_MOMENT_X1_Y1 = 38
M_MOMENT_X2_Y0 = 40
M_MONITORING_ERROR = 173
M_MONITORS_RECTS_LIST = 9205
M_MONITOR_BITS = 3968
M_MONO = 1
M_MONO1 = 256
M_MONO16 = 768
M_MONO32 = 1024
M_MONO64 = 10496
M_MONO8 = 512
M_MONO8_VIA_RGB = 1024
M_MONOCHROME = 0
M_MONO_EXTENDED_RANGE_END = 12032
M_MONO_EXTENDED_RANGE_START = 10496
M_MONO_RANGE_END = 1280
M_MONO_RANGE_START = 256
M_MONO_TO_BGR = 2
M_MONO_TO_MONO = 1
M_MONO_TO_RGB = 3
M_MONO_TO_YCBCRHD = 6
M_MONO_TO_YCBCRSD = 5
M_MONO_TO_YCRCBHD = 6
M_MONO_TO_YCRCBSD = 5
M_MONO_TO_YUV = 4
M_MORPHIS = 90
M_MORPHISQXT = 170
M_MORPHISQXT_FINGERPRINT = 20736
M_MORPHIS_FINGERPRINT = 20944
M_MORPHOLOGIC_ENHANCEMENT = 43
M_MORPHOLOGIC_FILTERING = 43
M_MOSAIC = 1073741826
M_MOSAIC_COMPOSITION = 8
M_MOSAIC_OFFSET_X = 6
M_MOSAIC_OFFSET_Y = 7
M_MOSAIC_SCALE = 19
M_MOSAIC_SIZE_X = 9
M_MOSAIC_SIZE_Y = 10
M_MOSAIC_STATIC_INDEX = 5
M_MOTION_DETECT_FIELD_SELECT = 5410
M_MOTION_DETECT_MASK_BUFFER_ID = 5411
M_MOTION_DETECT_MATRICE_SIZE_X = 5412
M_MOTION_DETECT_MATRICE_SIZE_Y = 5413
M_MOTION_DETECT_NUM_FRAMES = 5
M_MOTION_DETECT_OUTPUT = 8
M_MOTION_DETECT_REFERENCE_FRAME = 7
M_MOTION_DETECT_RESULT_BUFFER_ID = 5414
M_MOTION_DETECT_SENSITIVITY_LEVEL = 5406
M_MOTION_DETECT_SPATIAL_SENSITIVITY_LEVEL = 5407
M_MOTION_DETECT_TEMPORAL_SENSITIVITY_LEVEL = 5408
M_MOTION_DETECT_THRESHOLD = 6
M_MOTION_DETECT_VELOCITY_LEVEL = 5409
M_MOUSE_CURSOR_CHANGE = 3229
M_MOUSE_DRIVEN = 2
M_MOUSE_LEAVE = 85
M_MOUSE_LEFT_BUTTON = 524288
M_MOUSE_LEFT_BUTTON_DOWN = 56
M_MOUSE_LEFT_BUTTON_UP = 58
M_MOUSE_LEFT_DOUBLE_CLICK = 71
M_MOUSE_MIDDLE_BUTTON = 1048576
M_MOUSE_MIDDLE_BUTTON_DOWN = 66
M_MOUSE_MIDDLE_BUTTON_UP = 67
M_MOUSE_MOVE = 64
M_MOUSE_POSITION_BUFFER_X = 4
M_MOUSE_POSITION_BUFFER_Y = 5
M_MOUSE_POSITION_X = 1
M_MOUSE_POSITION_Y = 2
M_MOUSE_RESTRICTED = 1
M_MOUSE_RIGHT_BUTTON = 2097152
M_MOUSE_RIGHT_BUTTON_DOWN = 57
M_MOUSE_RIGHT_BUTTON_UP = 59
M_MOUSE_USE = 3219
M_MOUSE_WHEEL = 65
M_MOUSE_WHEEL_VALUE = 8
M_MOVABLE = 53
M_MOVE = 65536
M_MOVED = 2031616
M_MOVE_APPEND = 16777328
M_MOVE_ENTRIES = 4057
M_MOVE_INTEREST_POINT = 32768
M_MOVE_RELATIVE = 65536
M_MOVE_REPLACE = 16777344
M_MPEG4 = 146800640
M_MPEG4_USAGE = 2349
M_MPEG_B_FRAME = 2
M_MPEG_I_FRAME = 1
M_MPEG_P_FRAME = 0
M_MP_ACTIVE_THREAD = 15127
M_MP_CORES_NUM = 15133
M_MP_ERROR = 127
M_MP_FORCED_DISABLE = 1593
M_MP_MAX_CORES = 1818
M_MP_MAX_CORES_EFFECTIVE = 1710
M_MP_MAX_CORES_PER_THREAD = 15130
M_MP_PHYSICAL_CORES_NUM = 15134
M_MP_POOL_SIZE = 1604
M_MP_PRE_PROCESS = 15131
M_MP_PRIORITY = 1589
M_MP_SPIN_LOOP_COUNT = 1605
M_MP_SUPPORT = 4388
M_MP_THRESHOLD_RESTRICTION = 1609
M_MP_USE = 15128
M_MP_USER_THREAD = 1588
M_MP_USE_INTERNAL_FORCED = 1608
M_MSERIES_FINGERPRINT = 21328
M_MSG_BUFFER_PHYSICAL_ADDRESS = 2292
M_MSG_BUFFER_SIZE = 2291
M_MTX0 = 17592186044416
M_MTX0_CAPABLE_DIRECTX_OWNER = 9006
M_MTX0_METHOD = 8192
M_MTX0_MODE = 8192
M_MTX0_SERVICE = 9501
M_MTX_MEM_DRIVER_INFORMATION_STRUCT = 15618
M_MTX_MEM_MANAGER_ADDRESS = 15600
M_MTX_MEM_MANAGER_BANK_FLAGS = 15606
M_MTX_MEM_MANAGER_BASE_ADDRESS = 15600
M_MTX_MEM_MANAGER_BIGGEST_BANK = 15624
M_MTX_MEM_MANAGER_BOOT_FLAGS = 15613
M_MTX_MEM_MANAGER_CHUNK_SIZE = 15622
M_MTX_MEM_MANAGER_FREE_MEM_SIZE = 15602
M_MTX_MEM_MANAGER_FREE_MEM_SIZE_IN_BYTE = 15602
M_MTX_MEM_MANAGER_INFO_END = 15639
M_MTX_MEM_MANAGER_INFO_START = 15600
M_MTX_MEM_MANAGER_KERNEL_ADDRESS = 15608
M_MTX_MEM_MANAGER_MAX_NON_PAGED = 15627
M_MTX_MEM_MANAGER_MEM_SIZE = 15601
M_MTX_MEM_MANAGER_MIN_CHUNK_SIZE = 15626
M_MTX_MEM_MANAGER_NONPAGED_MODE = 15621
M_MTX_MEM_MANAGER_NON_PAGED_FLAGS = 15607
M_MTX_MEM_MANAGER_NUM_OF_BANK = 15605
M_MTX_MEM_MANAGER_NUM_USER_BANKS = 15623
M_MTX_MEM_MANAGER_OS_MEMORY_SIZE = 15612
M_MTX_MEM_MANAGER_RAM_INSTALLED = 15629
M_MTX_MEM_MANAGER_REG_CHUNK_SIZE = 15616
M_MTX_MEM_MANAGER_REG_NONPAGED_MODE = 15615
M_MTX_MEM_MANAGER_REG_NONPAGED_SIZE = 15617
M_MTX_MEM_MANAGER_SIZE_IN_BYTE = 15601
M_MTX_MEM_MANAGER_SMALLEST_BANK = 15625
M_MTX_MEM_MANAGER_SPECIAL_MODE = 15628
M_MTX_MEM_MANAGER_STARTUP_CHUNK_SIZE = 15611
M_MTX_MEM_MANAGER_STARTUP_NONPAGED_MODE = 15609
M_MTX_MEM_MANAGER_STARTUP_NONPAGED_SIZE = 15610
M_MTX_MEM_MANAGER_STRUCT_SIZE = 15620
M_MTX_MEM_MANAGER_STRUCT_VERSION = 15619
M_MTX_MEM_MANAGER_THRESHOLD = 15614
M_MTX_MEM_MANAGER_USED_MEM_SIZE = 15603
M_MTX_MEM_MANAGER_USED_MEM_SIZE_IN_BYTE = 15603
M_MTX_MEM_MANAGER_VERSION = 15604
M_MULT = 256
M_MULTIPLE = 4194304
M_MULTIPLE_IDS = 8388625
M_MULTIPLE_LABELS = 805306368
M_MULTIPLE_POINT_ANGLE = 62464
M_MULTIPLE_SELECTION = 1786
M_MULTIPLE_SELECTION_KEY = 2770
M_MULTIPLY_ACCUMULATE_1 = 2
M_MULTIPLY_ACCUMULATE_2 = 4
M_MULTITHREAD_SUPPORT = 4375
M_MULTI_BYTES = 1
M_MULTI_DISP_FOR_GRAB = 2076
M_MULTI_DISP_IN_UNDERLAY = 2075
M_MULTI_MONITOR = 9204
M_MULTI_THREAD = 4096
M_MULTI_THREAD_ERROR = 24
M_MULT_CONST = 33024
M_MUTEX = 268435456
M_N2S1200 = 1543507968
M_N2S300 = 1073745920
M_NAKED_ID_MASK = 1048575
M_NAME = 2097152
M_NAMED_BUFFER_SUPPORTED = 4394
M_NAND = 26
M_NAND_CONST = 32794
M_NATIVE = 3
M_NATIVE_CAMERA_ID = 4060
M_NATIVE_CLUSTER_NUMBER = 2090
M_NATIVE_ID = 1016
M_NATIVE_LAST_GRAB_THREAD_ID = 4750
M_NATIVE_NODE_NUMBER = 2091
M_NATIVE_SYSTEM_NUMBER = 2090
M_NBERRMSGMAX_ORIG = 200
M_NBFCTNAMEMAX = 445
M_NBR_OF_LINES = 74
M_NBR_OF_LINES_FOUND = 86
M_NBR_OF_LINES_READ = 74
M_NBSUBERRMSGMAX = 10
M_NB_BEST_MATCH_SAMPLE = 810
M_NB_BINS_BAND_0 = 1420
M_NB_BINS_BAND_1 = 1421
M_NB_BINS_BAND_2 = 1422
M_NB_CHILD = 5009
M_NB_CHILD_SELECTED_ON_DISPLAY = 5240
M_NB_ELEMENTS = 7696581394432
M_NB_EVENT = 5
M_NB_EXTERN_BUFFER_API_MODULE = 15393
M_NB_ITERATIONS = 1893
M_NB_MATCH_SAMPLE = 811
M_NB_MAX_PARAMETER = 16
M_NB_MAX_SCRIPT_REFERENCE = 256
M_NB_MODELS_MASK = 4095
M_NB_MONITORS_AVAILABLE = 9213
M_NB_NO_MATCH_SAMPLE = 812
M_NB_OF_DESKTOP_VGA_DEVICE = 15329
M_NB_OF_GRAPHIC_ADAPTER = 15332
M_NB_OF_PCI_VIDEO_DEVICE = 15338
M_NB_OF_TRANSFER_METHOD = 19
M_NB_OF_VGA_DEVICE = 15322
M_NB_OF_VIDEO_DEVICE = 15322
M_NB_SEED_ITERATIONS = 1894
M_NB_STRING = 74
M_NB_STRING_FOUND = 86
M_NEAREST_COLOR = 10018
M_NEAREST_NEIGHBOR = 64
M_NEAREST_NEIGHBOR_RADIUS = 116
M_NEED_DEFAULT_COMPENSATION = 16527
M_NEED_LOCK_UNLOCK = 4555
M_NEED_NETWORK_TUBE_DECODER = 16524
M_NEED_UPDATE = 1020
M_NEG = 35
M_NEGATIVE = -2
M_NEG_SUB = 10
M_NEIGHBORHOOD = 3043
M_NEIGHBORHOOD_DISTANCE = 3313
M_NEIGHBORHOOD_INFO_SIZE = 105
M_NEIGHBORHOOD_ORGANIZED_SIZE = 1943
M_NEIGHBOR_ANGLE = 122
M_NEIGHBOR_ANGLE_TOLERANCE = 123
M_NEIGHBOR_DIRECTION = 256
M_NEIGHBOR_DIRECTION_SIGN = 126
M_NEIGHBOR_MAXIMUM_NUMBER = 118
M_NEIGHBOR_MINIMUM_SPACING = 117
M_NEIGHBOR_POLARITY = 122
M_NEIGHBOR_POLARITY_TOLERANCE = 123
M_NEIGHBOR_SEARCH_MODE = 3041
M_NEIGHBOR_SEARCH_RADIUS_MAX = 120
M_NEIGHBOR_SEARCH_RADIUS_MIN = 121
M_NEIGH_SHRINK = 9437444
M_NETWORK = 512
M_NETWORKED = 4386
M_NETWORK_ADDRESS = 7704
M_NETWORK_PORT = 4808
M_NEW_DISPLAYS = 0
M_NEW_EXTERNAL_DISPLAY_ID = 9206
M_NEW_LABEL = 67108864
M_NEW_LIST = 2147
M_NEW_RESULTS = 2
M_NEW_USER_BIT_ALL = 2684358655
M_NEW_VIDEO_DEVICE_ADDED = 9406
M_NEXIS = 130
M_NEXIS2 = 232
M_NEXIS2_FINGERPRINT = 21120
M_NEXIS3 = 221
M_NEXIS3_FINGERPRINT = 20896
M_NEXIS_FINGERPRINT = 20752
M_NEXT = 1073741828
M_NEXT_FRAMES = 11
M_NEXT_FREE_BUFFER = 9011
M_NIBLACK = 1880
M_NIBLACK_BIAS = 1887
M_NIBLACK_BIAS_SECOND_PASS = 1889
M_NIC_FILTERING = 6921
M_NIGHT_DETECT_SENSITIVITY_LEVEL = 5417
M_NIGHT_DETECT_TEMPORAL_LEVEL = 5418
M_NO = 0
M_NODE_MAX_NUMBER_OF_FEATURES = 3517
M_NODE_MAX_NUMBER_OF_FEATURES_MODE = 3516
M_NODE_SELECT = 1816
M_NOISE_PEAK_REMOVAL = 8389634
M_NOISY_EDGELS = 3010
M_NONE = 134217728
M_NONZERO = 128
M_NON_CACHABLE = 35184372088832
M_NON_DISPLAY_METHOD = 4009754624
M_NON_FINITE_VALUE_DETECTED = 4746
M_NON_LOCAL_MEMORY = 34359738368
M_NON_MATROX_OHCI_BOARD = 50
M_NON_PAGED = 2097152
M_NON_PAGED_MEMORY_FREE = 15500
M_NON_PAGED_MEMORY_LARGEST_FREE = 15503
M_NON_PAGED_MEMORY_SIZE = 15502
M_NON_PAGED_MEMORY_USED = 15501
M_NON_PORTABLE_CALL = 8
M_NON_UNIFORMITY_CORRECTION = 2706
M_NON_ZERO = 128
M_NOR = 25
M_NORM = 4000
M_NORMAL = 8
M_NORMALIZATION_FACTOR = 52
M_NORMALIZATION_OFFSET = 2857
M_NORMALIZATION_SCALE = 2856
M_NORMALIZE = 2
M_NORMALIZED = 2
M_NORMALIZE_FONT = 4
M_NORMALIZE_PHASE = 8192
M_NORMALIZE_PHASE_255 = 32768
M_NORMALS_CONTEXT = 3438
M_NORMALS_CONTEXT_MESH = 10489754
M_NORMALS_CONTEXT_ORGANIZED = 10489178
M_NORMALS_CONTEXT_TREE = 10488802
M_NORMALS_FINITE = 2
M_NORMALS_NORMALIZED = 4
M_NORMAL_AND_ANGLE = 3877
M_NORMAL_SIZE = 1
M_NORMAL_X = 3537
M_NORMAL_Y = 3538
M_NORMAL_Z = 3539
M_NORM_CLIP = 4002
M_NORM_CLIP_SQR = 4003
M_NOR_CONST = 32793
M_NOT = 20
M_NOT_AUGMENTED = -1
M_NOT_CALCULATED = 0
M_NOT_CONVERTIBLE = 35
M_NOT_DISPLAYABLE = 32
M_NOT_ENOUGH_GPU_MEMORY = 958494
M_NOT_ENOUGH_MEMORY = 4
M_NOT_ENOUGH_POINT_PAIRS = 1972
M_NOT_ENOUGH_VALID_DATA = 1336
M_NOT_EQUAL = 4
M_NOT_EQUAL_CONST = 32772
M_NOT_INITIALIZED = 3
M_NOT_MODIFIED = 0
M_NOT_OPTIMIZABLE = 1
M_NOT_PROCESSABLE = 29
M_NOT_SIGNALED = 32
M_NOT_TRAINED = 2
M_NOT_WRITE_ANGLE = 1
M_NOT_WRITE_INT = 2
M_NOW = 29
M_NO_4GB_BORDERS = 4096
M_NO_ALIGNMENT = -1
M_NO_BACKGROUND_DEFINED = 650
M_NO_CHANGE = -9998
M_NO_CHECK = 1073741824
M_NO_CLEAR = 2
M_NO_COLOR = 3908
M_NO_COMPRESS = 2
M_NO_CONNECT = 4
M_NO_CONSTRAINT = 131072
M_NO_COPY_SOURCE_DATA = 1048576
M_NO_DISP = 32
M_NO_DMIL_COMPENSATION = 128
M_NO_ERROR = 0
M_NO_ERROR_ON_EMPTY_LIST = 128
M_NO_ERROR_ON_MISSING_CALIBRATION = 32
M_NO_EXTRAPOLATED_POINTS = 16777216
M_NO_FEATURES = 260
M_NO_FILTER = 524288
M_NO_FLIP = 67108864
M_NO_FORCE_IP = 16
M_NO_FPGA_UPGRADE = 536870912
M_NO_GRAB = 4
M_NO_GRAB_WHEN_NO_INPUT_SIGNAL = 2047
M_NO_HOOK = 4
M_NO_HYSTERESIS = 20
M_NO_INPUT_PRESENT = 128
M_NO_INTENSITY = 65536
M_NO_INTERACTIVE_ANNOTATION = 4096
M_NO_INTERRUPT = 16
M_NO_LABEL = 536870912
M_NO_LIMIT = 16384
M_NO_MAP = 67108864
M_NO_MATCH = 7
M_NO_MATCH_INDEX = 824
M_NO_MATCH_LABEL = 826
M_NO_MEMORY = 2251799813685248
M_NO_MEM_ERROR = 112
M_NO_MODIFIED_HOOK = 8
M_NO_NORMALIZE = -1
M_NO_OVERWRITE = 512
M_NO_PARSING = 8192
M_NO_PHYSICAL_ADDRESS = 256
M_NO_POINTS_BEHIND_CAMERA = 262144
M_NO_PROC = 8
M_NO_QUANTIZATION = 0
M_NO_RASTERIZE = 1
M_NO_REFLECTANCE = 3964
M_NO_REFRESH = 4167
M_NO_REGION = 65536
M_NO_REJECTED_DEFINED = 654
M_NO_REPORT = 8
M_NO_RXYZ_SWAP = 1
M_NO_SAMPLING = 3602
M_NO_SCAN = 512
M_NO_SELECTED_DEFINED = 652
M_NO_SKIP = 10002
M_NO_SORT = 0
M_NO_SOURCE_DEFINED = 670
M_NO_SRC_VALID_LABEL = 0
M_NO_SUBSAMPLING = 1048576
M_NO_TEARING = 3188
M_NO_TEARING_ACTIVE = 10032
M_NO_TEARING_ACTIVE_DEVICE = 8506
M_NO_TEARING_ALLOWED = 10559
M_NO_TEARING_DEVICE = 8505
M_NO_TEARING_MODE = 10035
M_NO_TEARING_MODE_MASK = 15728640
M_NO_TEARING_SKIP_MODE = 10001
M_NO_TEARING_SKIP_MODE_MASK = 1048575
M_NO_TIMEOUT = 2048
M_NO_TYPE = 1048576
M_NO_VALID_POINTS = 2097
M_NSCN_1 = 0
M_NSCN_2 = 1
M_NSCN_3 = 2
M_NSCN_4 = 3
M_NSCN_5 = 4
M_NSCN_6 = 5
M_NSCN_7 = 6
M_NSCN_8 = 7
M_NTSC = 2
M_NTSC_RGB = 5
M_NULL_ERROR = 0
M_NULL_PARAMETER = 118
M_NUMBER = 1009
M_NUMBER_FOUND = 90
M_NUMBER_MAX = 1011
M_NUMBER_MIN = 1010
M_NUMBER_MODELS = 302
M_NUMBER_OF_3D_POINTS = 5
M_NUMBER_OF_AREAS = 832
M_NUMBER_OF_AUGMENTED_ENTRIES = 3976
M_NUMBER_OF_AUTHORS = 3773
M_NUMBER_OF_BASIC_IMPLEMENTATIONS = 10185
M_NUMBER_OF_BUFFERS = 5094
M_NUMBER_OF_CALIBRATION_DEPTHS = 1315
M_NUMBER_OF_CALIBRATION_POINTS = 200
M_NUMBER_OF_CALIBRATION_POSES = 199
M_NUMBER_OF_CHAINED_EDGELS = 56
M_NUMBER_OF_CHAINED_PIXELS = 56
M_NUMBER_OF_CHAINS = 1897
M_NUMBER_OF_CHARS = 814
M_NUMBER_OF_CHILDREN = 4686
M_NUMBER_OF_CLASSES = 2848
M_NUMBER_OF_CLASS_SCORES = 2864
M_NUMBER_OF_CODEWORDS = 45059
M_NUMBER_OF_CODE_MODELS = 5065
M_NUMBER_OF_COLOR_ITEMS = 1585
M_NUMBER_OF_COLUMNS = 1317
M_NUMBER_OF_COLUMNS_WITH_INVERSIONS = 1320
M_NUMBER_OF_COLUMNS_WITH_MISSING_DATA = 1318
M_NUMBER_OF_CONSTRAINED_POSITIONS = 2465
M_NUMBER_OF_CONSTRAINTS = 516
M_NUMBER_OF_CONSTRUCTED_FEATURES = 1004
M_NUMBER_OF_CONVEX_HULL_POINTS = 84
M_NUMBER_OF_CURSORS = 29
M_NUMBER_OF_DATA_CODEWORDS = 45063
M_NUMBER_OF_DECODED_ROWS = 3591
M_NUMBER_OF_DECODED_SCANS = 3593
M_NUMBER_OF_ELEMENT_VALUES_VALID = 58
M_NUMBER_OF_ENTRIES = 24
M_NUMBER_OF_ENTRIES_GROUND_TRUTH = 3761
M_NUMBER_OF_ENTRIES_IN_ERROR = 3689
M_NUMBER_OF_ENTRIES_OUT_OF_BAG = 3535
M_NUMBER_OF_ENTRIES_PREDICTED = 3762
M_NUMBER_OF_ERASURES = 45062
M_NUMBER_OF_ERRORS = 45061
M_NUMBER_OF_ERROR_CORRECTION_CODEWORDS = 45060
M_NUMBER_OF_EVENTS = 8201
M_NUMBER_OF_FEATURES = 1002
M_NUMBER_OF_FEATURES_FAIL = 1103
M_NUMBER_OF_FEATURES_PASS = 1102
M_NUMBER_OF_FERETS = 63
M_NUMBER_OF_FIXED_PATTERN_DAMAGE_B_SEGMENT = 36977
M_NUMBER_OF_FONTS = 901
M_NUMBER_OF_FRAMES = 1080
M_NUMBER_OF_GRAB_BLOCKS = 2437
M_NUMBER_OF_GRAB_IN_PROGRESS = 5097
M_NUMBER_OF_GRAPHICS = 1519
M_NUMBER_OF_GROUPS = 3170
M_NUMBER_OF_HOLES = 26
M_NUMBER_OF_IMAGES = 6003
M_NUMBER_OF_INPUTS = 2835
M_NUMBER_OF_INTERLEAVED_BLOCKS = 41046
M_NUMBER_OF_INVERSIONS_PER_COLUMN = 1319
M_NUMBER_OF_KEYS = 21506
M_NUMBER_OF_LEARNERS = 957
M_NUMBER_OF_LEARNERS_MAX = 956
M_NUMBER_OF_LEVELS = 1797
M_NUMBER_OF_MEASURED_FEATURES = 1003
M_NUMBER_OF_MISSING_DATA_LAST_SCAN = 1348
M_NUMBER_OF_MISSING_DATA_PER_COLUMN = 1316
M_NUMBER_OF_NODES_MAX = 955
M_NUMBER_OF_OUTLIERS = 1379
M_NUMBER_OF_OUTPUTS = 2836
M_NUMBER_OF_PEAKS = 4
M_NUMBER_OF_PERMITTED_CHARS_ENTRIES = 2283
M_NUMBER_OF_PIXELS = 70912
M_NUMBER_OF_PIXELS_MISSING_DATA = 1364
M_NUMBER_OF_PIXELS_OUTLIER = 1363
M_NUMBER_OF_PIXELS_TOTAL = 1365
M_NUMBER_OF_PIXELS_VALID = 1362
M_NUMBER_OF_POINTS = 1009
M_NUMBER_OF_POINTS_INLIERS = 3557
M_NUMBER_OF_POINTS_MISSING_DATA = 3484
M_NUMBER_OF_POINTS_OUTLIERS = 3558
M_NUMBER_OF_POINTS_TOTAL = 3485
M_NUMBER_OF_POINTS_VALID = 3440
M_NUMBER_OF_POINT_CLOUDS = 1916
M_NUMBER_OF_PREDICTED_ENTRIES = 3688
M_NUMBER_OF_PU = 4096
M_NUMBER_OF_REGIONS = 3652
M_NUMBER_OF_REGISTRATION_ELEMENTS = 2
M_NUMBER_OF_ROWS = 45056
M_NUMBER_OF_RUNS = 55
M_NUMBER_OF_SAMPLES = 35
M_NUMBER_OF_SCANLINES = 1653
M_NUMBER_OF_SCANS = 45058
M_NUMBER_OF_SCAN_LANES = 131072
M_NUMBER_OF_SCRIPT_REFERENCES = 252
M_NUMBER_OF_STRING_MODELS = 900
M_NUMBER_OF_SUB_ELEMENTS = 1525
M_NUMBER_OF_TEMPLATES = 1
M_NUMBER_OF_TILES_X = 250
M_NUMBER_OF_TILES_Y = 251
M_NUMBER_OF_TOLERANCES = 1005
M_NUMBER_OF_TOLERANCES_FAIL = 1106
M_NUMBER_OF_TOLERANCES_PASS = 1105
M_NUMBER_OF_TOLERANCES_WARNING = 1107
M_NUMBER_OF_TRAINING_IMAGES = 2569
M_NUMBER_OF_TRANSFORM = 1491
M_NUMBER_OF_TREES = 3515
M_NUMBER_OF_TREES_TRAINED = 3813
M_NUMBER_OF_TU = 4097
M_NUMBER_OF_USER_MODULES = 16
M_NUMBER_OF_VERTICES = 73
M_NUMBER_POINTS_PER_CELL = 3317
M_NUMBER_SUBBAND = 2560
M_NUM_CAMERA_PRESENT = 4811
M_OBJECT_BOTTOM = 5259
M_OBJECT_CENTER = 5244
M_OBJECT_FILENAME = 48
M_OBJECT_FILE_EXTENSION = 52
M_OBJECT_FILE_FOLDER = 53
M_OBJECT_FILE_NAME = 54
M_OBJECT_FILE_NAME_NO_EXTENSION = 51
M_OBJECT_FILE_PATH = 48
M_OBJECT_FREE = 65536
M_OBJECT_FREE_REMOTE = 65537
M_OBJECT_ID = 1769472
M_OBJECT_LOCK = 22
M_OBJECT_NAME = 47
M_OBJECT_NAME_SIZE = 5497558138927
M_OBJECT_PROPERTIES_MODIFIED = 2050
M_OBJECT_PTR = 10
M_OBJECT_PUBLISH_DMIL = 30
M_OBJECT_PUBLISH_WEB = 38
M_OBJECT_RESULTS_MODIFIED = 2051
M_OBJECT_SHAPE = 4893
M_OBJECT_SIZE = 2707
M_OBJECT_TOP = 5258
M_OBJECT_TYPE = 136
M_OBJECT_TYPE_EXTENDED = 29
M_OBJECT_TYPE_OLD = 162
M_OBJECT_USER_DATA_PTR = 150
M_OBJECT_VALID = 1038
M_OBJ_CONTROL_SUPPORT_COMPENSATE_REAL_ID = 4396
M_OBJ_HOOK_MODULE_RANGE_END = 65535
M_OBJ_HOOK_MODULE_RANGE_START = 65024
M_OBJ_HOOK_RANGE_END = 2303
M_OBJ_HOOK_RANGE_START = 2048
M_OBJ_HOOK_USER_RANGE_END = 65023
M_OBJ_HOOK_USER_RANGE_START = 64768
M_OBJ_INQUIRE_DOUBLE_RANGE_END = 1407
M_OBJ_INQUIRE_DOUBLE_RANGE_START = 1407
M_OCCURRENCE = 105
M_OCR_A = 10
M_OCR_B = 11
M_OCR_FONT = 537919489
M_OCR_OBJECT = 537919488
M_OCR_PREPROCESSED = 14
M_OCR_RESULT = 537919490
M_OCR_THRESHOLD = 82
M_ODD = 1
M_ODD_EVEN = 1
M_ODD_EVEN_CORRECTION = 4327
M_ODD_FIELD = 1
M_OFF = 0
M_OFFICIAL = 3
M_OFFSCREEN = 128
M_OFFSCREEN_INCOMPATIBLE_BITS = 563224839716864
M_OFFSET = 2
M_OFFSET_BAND_0 = 244
M_OFFSET_BAND_1 = 245
M_OFFSET_BAND_2 = 246
M_OFFSET_CENTER_X = 55
M_OFFSET_CENTER_Y = 56
M_OFFSET_CONST = 204
M_OFFSET_GAIN = 0
M_OFFSET_IMAGE = 201
M_OFFSET_IMAGE_HEIGHT = 214
M_OFFSET_IMAGE_NB_BANDS = 212
M_OFFSET_IMAGE_TYPE = 215
M_OFFSET_IMAGE_WIDTH = 213
M_OFFSET_MAX = 88
M_OFFSET_MAX_INDEX = 89
M_OFFSET_X = 5099
M_OFFSET_Y = 5100
M_OFF_BOARD = 1048576
M_OK_TO_FREE = 2379
M_OLDEST_READY_BUFFER = 9012
M_OLD_CODE_CONTEXT = 545259523
M_OLD_MAX_INSTALLED_SYSTEMS = 16
M_OLD_OBJECT_PUBLISH_WEB = 34
M_OLD_WEB_CLIENT_CONNECTED = 27
M_OLD_WEB_CLIENT_DISCONNECTED = 28
M_OLD_WEB_CONNECTION = 15521
M_OLD_WEB_CONNECTION_LOST = 29
M_OLD_WEB_CONNECTION_PORT = 15522
M_OLD_WEB_PUBLISH = 14
M_OLD_WEB_PUBLISHED_LIST = 4
M_OLD_WEB_PUBLISHED_LIST_SIZE = 5
M_OLD_WEB_PUBLISHED_NAME = 6
M_ON = 1
M_ONCE = 3
M_ONE_SIDED = 2733
M_ONLY_MISSING_DATA = 524288
M_ONLY_SRC1_VALID_LABEL = 85
M_ONLY_SRC2_VALID_LABEL = 170
M_ON_BOARD = 524288
M_ON_BOARD_NATIVE_THREAD_ID = 2314
M_ON_COMPONENT = 33554432
M_ON_DESELECT = 2
M_ON_FOCUS = 100
M_ON_SELECT = 1
M_OPACITY = 4728
M_OPAQUE = 16777304
M_OPAQUE_HOOK_CONTEXT = 1610612768
M_OPEN = 16
M_OPENCL_COMPATIBLE = 144115188075855872
M_OPEN_APPEND = 536870928
M_OPEN_DRAIN = 5
M_OPERATION = 103
M_OPERATION_ERROR = 12
M_OPERATION_ERROR_10 = 177
M_OPERATION_ERROR_11 = 183
M_OPERATION_ERROR_12 = 56200
M_OPERATION_ERROR_13 = 56207
M_OPERATION_ERROR_2 = 57
M_OPERATION_ERROR_3 = 75
M_OPERATION_ERROR_4 = 5
M_OPERATION_ERROR_5 = 4
M_OPERATION_ERROR_6 = 102
M_OPERATION_ERROR_7 = 125
M_OPERATION_ERROR_8 = 129
M_OPERATION_ERROR_9 = 130
M_OPERATION_MODE = 8203
M_OPPOSITE = 3
M_OPTICAL_CENTER_X = 1007
M_OPTICAL_CENTER_Y = 1008
M_OPTICAL_FILTER = 5156
M_OPTIMAL_SIZE_X = 1
M_OPTIMAL_SIZE_Y = 2
M_OPTIMIZABLE = 0
M_OPTIMIZATIONS = 4
M_OPTIMIZE_LOCATION = 1002
M_OPTO = 0
M_OR = 22
M_ORANGE = 48
M_ORBIT_HORIZONTAL = 4177
M_ORBIT_VERTICAL = 4178
M_ORDINARY = 1024
M_ORGANIZATION_SIZE_X = 2981
M_ORGANIZATION_SIZE_Y = 2982
M_ORGANIZATION_TYPE = 3638
M_ORGANIZED = 3418
M_ORGANIZED_NORMALS_NEIGHBORHOOD_RADIUS = 1943
M_ORIENTATION = 9216
M_ORIENTATION_DATA_COHERENCE = 8192
M_ORIENTATION_DATA_MEAN = 4096
M_ORIENTATION_UNCHANGED = 32768
M_ORIENTED_RECT = 2735
M_ORIGINAL = 409
M_ORIGINAL_IMAGE_SIZE_X = 1869
M_ORIGINAL_IMAGE_SIZE_Y = 1870
M_ORIGINAL_X = 6
M_ORIGINAL_Y = 7
M_ORIONHD_FINGERPRINT = 20992
M_ORION_HD = 240
M_ORION_UHD = 250
M_OR_ARM_ACTIVATION = 33554432
M_OR_CONST = 32790
M_OS_CONTROLLED = -9990
M_OS_CURSOR_APPSTARTING = 14
M_OS_CURSOR_ARROW = 2
M_OS_CURSOR_CROSS = 5
M_OS_CURSOR_HAND = 13
M_OS_CURSOR_HELP = 15
M_OS_CURSOR_IBEAM = 3
M_OS_CURSOR_NO = 12
M_OS_CURSOR_SIZEALL = 11
M_OS_CURSOR_SIZENESW = 8
M_OS_CURSOR_SIZENS = 10
M_OS_CURSOR_SIZENWSE = 7
M_OS_CURSOR_SIZEWE = 9
M_OS_CURSOR_UPARROW = 6
M_OS_CURSOR_WAIT = 4
M_OS_DEFAULT = -9991
M_OS_LINUX = 3
M_OS_RTX = 5
M_OS_WINDOWS = 1
M_OS_WINDOWS_CE = 2
M_OUT = 1024
M_OUTER_FIT = 41
M_OUTER_RADIUS = 235
M_OUTER_RADIUS_X = 1217
M_OUTER_RADIUS_Y = 1218
M_OUTER_TO_INNER_RADIUS = 2794
M_OUTLIER_COVERAGE = 808
M_OUTLIER_DRAW_COLOR = 31
M_OUTLIER_LABEL = 30
M_OUTLIER_MASK = 3995
M_OUTPUT = 3
M_OUTPUT0 = 536870912
M_OUTPUT1 = 536870913
M_OUTPUT2 = 536870914
M_OUTPUT3 = 536870915
M_OUTPUT4 = 536870916
M_OUTPUT5 = 536870917
M_OUTPUT6 = 536870918
M_OUTPUT7 = 536870919
M_OUTPUT8 = 536870920
M_OUTPUT9 = 536870921
M_OUTPUT_DATASET_ID = 3682
M_OUTPUT_FRAME = 260
M_OUTPUT_UNITS = 122
M_OUTSIDE = 0
M_OUTSIDE_BOX = 302
M_OUTSIDE_CHAIN = 303
M_OUTSIDE_OR_EQUAL_BOX = 366
M_OUTSIDE_OR_EQUAL_CHAIN = 367
M_OUT_OF_BAG = 3705
M_OUT_OF_BAG_ACCURACY = 3804
M_OUT_OF_BAG_ACCURACY_AFTER_EACH_TREE = 3809
M_OUT_OF_BAG_CONFUSION_MATRIX = 3789
M_OUT_OF_BAG_CONFUSION_MATRIX_SIZE_X = 3805
M_OUT_OF_BAG_CONFUSION_MATRIX_SIZE_Y = 3984
M_OUT_OF_BAG_ERROR_RATE = 3526
M_OUT_OF_BAG_ERROR_RATE_AFTER_EACH_TREE = 3530
M_OUT_OF_BAG_PREDICT_SCORES = 3965
M_OUT_RANGE = 2
M_OVERALL_SYMBOL_GRADE = 36864
M_OVERLAP = 1966
M_OVERLAY = 128
M_OVERLAY_CLEAR = 10006
M_OVERLAY_ID = 1106
M_OVERLAY_LUT = 1104
M_OVERLAY_MEM_SIZE = 2095
M_OVERLAY_SHOW = 3023
M_OVERRIDE_ROUTER = 4143
M_OVERSCAN = 53
M_OVERSCAN_BUFFER = 134217728
M_OVERSCAN_CLEAR = 128
M_OVERSCAN_DISABLE = 524288
M_OVERSCAN_ENABLE = 32768
M_OVERSCAN_ERROR = 7
M_OVERSCAN_FAST = 262144
M_OVERSCAN_REPLACE_MAX = 16
M_OVERSCAN_REPLACE_MIN = 32
M_OVERSCAN_REPLACE_VALUE = 54
M_OVERSCAN_TO_DO = 4
M_OVERWRITE = 1861
M_OVER_CURRENT = 15
M_OVR = 128
M_OVR_INCOMPATIBLE_BITS = 563224839716864
M_OWNER_APPLICATION = 1100
M_OWNER_CONTAINER_ID = 1193
M_OWNER_NODE_ID = 1104
M_OWNER_SYSTEM = 1101
M_OWNER_SYSTEM_TYPE = 1023
M_P1200 = 73728
M_P1200H = 77824
M_P1200HM = 76800
M_P1200HMR = 1125376
M_P1200HR = 1126400
M_P1200R = 1122304
M_P300 = 12288
M_P300C = 12544
M_P300CR = 1061120
M_P300H = 13312
M_P300HM = 15360
M_P300HMR = 1063936
M_P300HR = 1061888
M_P300R = 1060864
M_P700 = 28672
M_P700R = 1077248
M_P700W = 29440
M_P700WR = 1078016
M_PACKED = 131072
M_PACKED_X_Y_ANGLE = 524288
M_PAGED = 33554432
M_PAIRING_MODE = 17
M_PAIRWISE_ALIGNMENT_CONTEXT = 1939
M_PAIRWISE_REGISTRATION_CONTEXT = 3507
M_PAIRWISE_REGISTRATION_RESULT = 3500
M_PAIR_PARTNER = 75
M_PAIR_PARTNER_NUMBER = 74
M_PAL = 4
M_PALETTE_HANDLE = 3151
M_PAL_RGB = 6
M_PAN = 5148
M_PAN_OFFSET_X = 6603
M_PAN_OFFSET_Y = 6604
M_PAN_X = 3000
M_PAN_Y = 3001
M_PARALLEL = 39
M_PARALLELISM = 4
M_PARAM1 = 4325376
M_PARAM2 = 4390912
M_PARAM3 = 4718592
M_PARAMETER = 15004
M_PARAMETER_CHECK = 1
M_PARAMETRIC = 33
M_PARAM_ATTRIBUTES = 67108864
M_PARAM_NB = 1310720
M_PARAM_NUMBER = 20
M_PARAM_SIZE = 16777216
M_PARAM_TYPE_ARRAY_MIL_CHAR = 134217744
M_PARAM_TYPE_ARRAY_MIL_CHAR_ASCII = 150994960
M_PARAM_TYPE_ARRAY_MIL_CHAR_UNICODE = 167772176
M_PARAM_TYPE_ARRAY_MIL_DOUBLE = 134217731
M_PARAM_TYPE_ARRAY_MIL_FLOAT = 134217739
M_PARAM_TYPE_ARRAY_MIL_ID = 134217732
M_PARAM_TYPE_ARRAY_MIL_INT = 134217729
M_PARAM_TYPE_ARRAY_MIL_INT16 = 134217742
M_PARAM_TYPE_ARRAY_MIL_INT32 = 134217733
M_PARAM_TYPE_ARRAY_MIL_INT64 = 134217735
M_PARAM_TYPE_ARRAY_MIL_INT8 = 134217740
M_PARAM_TYPE_ARRAY_MIL_UINT = 134217730
M_PARAM_TYPE_ARRAY_MIL_UINT16 = 134217743
M_PARAM_TYPE_ARRAY_MIL_UINT32 = 134217734
M_PARAM_TYPE_ARRAY_MIL_UINT64 = 134217736
M_PARAM_TYPE_ARRAY_MIL_UINT8 = 134217741
M_PARAM_TYPE_ARRAY_MIL_UUID = 134217745
M_PARAM_TYPE_ASCII = 16777216
M_PARAM_TYPE_CHAR = 10
M_PARAM_TYPE_CONST = 268435456
M_PARAM_TYPE_CONST_ARRAY_MIL_CHAR = 402653200
M_PARAM_TYPE_CONST_ARRAY_MIL_CHAR_ASCII = 419430416
M_PARAM_TYPE_CONST_ARRAY_MIL_CHAR_UNICODE = 436207632
M_PARAM_TYPE_CONST_ARRAY_MIL_DOUBLE = 402653187
M_PARAM_TYPE_CONST_ARRAY_MIL_FLOAT = 402653195
M_PARAM_TYPE_CONST_ARRAY_MIL_ID = 402653188
M_PARAM_TYPE_CONST_ARRAY_MIL_INT = 402653185
M_PARAM_TYPE_CONST_ARRAY_MIL_INT16 = 402653198
M_PARAM_TYPE_CONST_ARRAY_MIL_INT32 = 402653189
M_PARAM_TYPE_CONST_ARRAY_MIL_INT64 = 402653191
M_PARAM_TYPE_CONST_ARRAY_MIL_INT8 = 402653196
M_PARAM_TYPE_CONST_ARRAY_MIL_UINT = 402653186
M_PARAM_TYPE_CONST_ARRAY_MIL_UINT16 = 402653199
M_PARAM_TYPE_CONST_ARRAY_MIL_UINT32 = 402653190
M_PARAM_TYPE_CONST_ARRAY_MIL_UINT64 = 402653192
M_PARAM_TYPE_CONST_ARRAY_MIL_UINT8 = 402653197
M_PARAM_TYPE_CONST_ARRAY_MIL_UUID = 402653201
M_PARAM_TYPE_CONST_DATA_PTR = 402653193
M_PARAM_TYPE_CONST_MIL_TEXT = 402653194
M_PARAM_TYPE_CONST_MIL_TEXT_ASCII = 419430410
M_PARAM_TYPE_CONST_MIL_TEXT_UNICODE = 436207626
M_PARAM_TYPE_DATA_PTR = 134217737
M_PARAM_TYPE_FILENAME = 67108864
M_PARAM_TYPE_FILENAME_ASCII = 218103818
M_PARAM_TYPE_FILENAME_UNICODE = 234881034
M_PARAM_TYPE_INFO = 33554432
M_PARAM_TYPE_MIL_CHAR = 16
M_PARAM_TYPE_MIL_DOUBLE = 3
M_PARAM_TYPE_MIL_FLOAT = 11
M_PARAM_TYPE_MIL_ID = 4
M_PARAM_TYPE_MIL_INT = 1
M_PARAM_TYPE_MIL_INT16 = 14
M_PARAM_TYPE_MIL_INT32 = 5
M_PARAM_TYPE_MIL_INT64 = 7
M_PARAM_TYPE_MIL_INT8 = 12
M_PARAM_TYPE_MIL_TEXT = 134217738
M_PARAM_TYPE_MIL_TEXT_ASCII = 150994954
M_PARAM_TYPE_MIL_TEXT_UNICODE = 167772170
M_PARAM_TYPE_MIL_UINT = 2
M_PARAM_TYPE_MIL_UINT16 = 15
M_PARAM_TYPE_MIL_UINT32 = 6
M_PARAM_TYPE_MIL_UINT64 = 8
M_PARAM_TYPE_MIL_UINT8 = 13
M_PARAM_TYPE_MIL_UUID = 17
M_PARAM_TYPE_POINTER = 134217728
M_PARAM_TYPE_UNICODE = 33554432
M_PARAM_TYPE_VOID = 9
M_PARAM_VALUE = 134217728
M_PARENT = 4687
M_PARENT_ID = 1103
M_PARENT_OFFSET_BAND = 5007
M_PARENT_OFFSET_X = 5003
M_PARENT_OFFSET_Y = 5004
M_PARSE_COMPRESSED_DATA = 5072
M_PARSE_H264_DATA = 5072
M_PARSE_JPEG2000_DATA = 5072
M_PARSE_JPEG_DATA = 5072
M_PARSE_MPEG4_DATA = 5072
M_PARTIAL = 1
M_PARTIALLY_CORRECTED = 1350
M_PARTIALLY_CORRECTED_DEPTH_MAP = 3767
M_PARTIALLY_CORRECTED_DEPTH_MAP_BUFFER_TYPE = 3860
M_PARTIALLY_CORRECTED_DEPTH_MAP_SIZE_X = 3858
M_PARTIALLY_CORRECTED_DEPTH_MAP_SIZE_Y = 3859
M_PARTIAL_WRITE = 134217728
M_PART_OF_DESKTOP = 4580
M_PAR_ENCODER_WAIT_FIELD = 10053
M_PASS = 2
M_PASSED_IMAGES_ID = 2573
M_PASSED_IMAGES_INDEX = 2581
M_PASSED_NUMBER_OF_IMAGES = 2571
M_PATH_LIST = 3
M_PATH_WIDTH_LIST = 7
M_PAT_CONTEXT = 537395204
M_PAT_CONTEXT_TO_MODEL = 33554432
M_PAT_CONTEXT_TO_MODEL_INDEX_MASK = 65535
M_PAT_EVAL_MORE_CANDIDATES = 52
M_PAT_MODEL = 537395201
M_PAT_MODEL_TO_CONTEXT = 16777216
M_PAT_OBJECT = 537395200
M_PAT_ON_ACCELERATED = 59
M_PAT_RESULT = 537395202
M_PC104 = 2048
M_PC104_PRESENT = 2133
M_PCIE_NUMBER_OF_LANES = 2588
M_PCIE_NUMBER_OF_LANES_MAX = 2589
M_PCIE_PAYLOAD_SIZE = 4815
M_PCIE_SPEED = 2598
M_PCIE_SPEED_MAX = 2599
M_PCI_BASE_ADRS0 = 4
M_PCI_BASE_ADRS1 = 5
M_PCI_BASE_ADRS2 = 6
M_PCI_BRIDGE_HOST_WRITE_POSTING = 2079
M_PCI_BRIDGE_ID = 2089
M_PCI_BRIDGE_LATENCY = 2073
M_PCI_CLASS_CODE = 2
M_PCI_COMMAND = 1
M_PCI_CONFIGURATION_SPACE = 0
M_PCI_DEVICE_ID = 0
M_PCI_INT_LINE = 15
M_PCI_INT_PIN = 15
M_PCI_LATENCY = 2048
M_PCI_LATENCY_TIMER = 3
M_PCI_MGA_ID = 2087
M_PCI_REVISION_ID = 2
M_PCI_STATUS = 1
M_PCI_VENDOR_ID = 0
M_PCI_VIA_ID = 2088
M_PDF417 = 256
M_PDF417_NAME = MIL_TEXT("PDF417")
M_PEAK_INTENSITY = 65536
M_PEAK_INTENSITY_MODE = 3
M_PEAK_INTENSITY_RANGE = 32768
M_PEAK_POSITION = 4194304
M_PEAK_POSITION_X = 8388608
M_PEAK_POSITION_Y = 16777216
M_PEAK_VALUE_MODE = 2
M_PEAK_WIDTH = 11
M_PEAK_WIDTH_DELTA = 7
M_PEAK_WIDTH_NOMINAL = 6
M_PERCENTAGE = 2
M_PERCENTILE_VALUE = 16
M_PERCENTILE_VALUE_RESULT_SIZE = 101
M_PERFORMANCE_LOGS = 4601
M_PERIMETER = 3
M_PERIMETER_CONVEX_HULL = 3185
M_PERIMETER_SIMPLE = 2519
M_PERIOD_MEASUREMENT = 67
M_PERMUTATION = 3615
M_PERPENDICULAR = 40
M_PERPENDICULARITY = 1
M_PERPENDICULAR_LINE = 1646
M_PERSPECTIVE = 5
M_PERSPECTIVE_TRANSFORMATION = 2
M_PERSPECTIVE_UNEVEN_GRID_STEP = 7
M_PER_AXIS = 3956
M_PER_BAND = 2966
M_PER_POINT = 3873
M_PF = 16777216
M_PFNC = 4294967296
M_PFNC_COMPACT = 536870912
M_PFNC_GRAB_SUPPORTED = 4403
M_PFNC_NAME = 6903
M_PFNC_SIZE_BIT = 5282
M_PFNC_SUPPORT = 5283
M_PFNC_TARGET_FORMAT = 4131
M_PFNC_VALUE = 5101
M_PF_CLOCK_FREQUENCY = 4805
M_PF_MEMORY_SIZE = 4806
M_PHARMACODE = 8192
M_PHARMACODE_NAME = MIL_TEXT("Pharmacode")
M_PHASE = 512
M_PHASE1 = 1024
M_PHASE2 = 2048
M_PHONG = 4726
M_PHOTOMETRIC_STEREO = 4
M_PHOTOMETRIC_STEREO_CALIBRATED_WORKSPACE = 33
M_PHOTOMETRIC_STEREO_RESULT = 4
M_PHOTOMETRIC_STEREO_UNCALIBRATED_WORKSPACE = 34
M_PHYSICAL_ADDRESS = 1073741824
M_PHYSICAL_ADDRESS_BLUE = 1073741856
M_PHYSICAL_ADDRESS_GREEN = 1073741840
M_PHYSICAL_ADDRESS_ON_BOARD = 6700
M_PHYSICAL_ADDRESS_RED = 1073741832
M_PHYSICAL_ADDRESS_REMOTE = 4194304
M_PHYSICAL_ADDRESS_UNDERLAY = 2029
M_PHYS_ADDRESS_BAND = 5222
M_PHYS_SHOW_TASKBAR = 9200
M_PIPE = 23
M_PITCH = 536870912
M_PITCH_BYTE = 134217728
M_PIXCLK = 27
M_PIXCLK_FREQ = 5185
M_PIXCLK_JPEG_SIGNAL_PRESENT = 4281
M_PIXEL = 4096
M_PIXEL_ASPECT_RATIO = 5
M_PIXEL_ASPECT_RATIO_INPUT = 6
M_PIXEL_ASPECT_RATIO_OUTPUT = 7
M_PIXEL_COORDINATE_SYSTEM = 33554432
M_PIXEL_ERROR = 1
M_PIXEL_FORMAT = 3032
M_PIXEL_MATCH_IMAGE_SIZE_X = 1447
M_PIXEL_MATCH_IMAGE_SIZE_Y = 1448
M_PIXEL_ROTATION = 1373
M_PIXEL_SCALE = 316
M_PIXEL_SCORE_TOLERANCE = 1442
M_PIXEL_SIZE_DIAGONAL = -5
M_PIXEL_SIZE_IN_MM = 32838
M_PIXEL_SIZE_X = 139
M_PIXEL_SIZE_Y = 140
M_PIXEL_TO_WORLD = 1
M_PIXEL_VALUES = 5
M_PIXEL_X = 3891
M_PIXEL_Y = 3892
M_PLANAR = 262144
M_PLANE = 1353
M_PLANET = 1024
M_PLANET_NAME = MIL_TEXT("Planet")
M_PLANE_ANGLE_TOO_SMALL = 5
M_PLATFORM_BITNESS = 16584
M_PLATFORM_OS_TYPE = 16585
M_PLY = 1964
M_PLY_ASCII = 2832
M_PLY_BINARY_LITTLE_ENDIAN = 2833
M_PNG = 8192
M_PNG_ALPHA_CHANNEL = 15138
M_PNG_ERROR = 137
M_POINT = 1
M_POINTS = 16
M_POINTS_X = 4733
M_POINTS_Y = 4734
M_POINTS_Z = 4735
M_POINT_AND_ANGLE = 80
M_POINT_AND_DIRECTION_POINT = 96
M_POINT_AND_DISTANCE = 1743
M_POINT_AND_NORMAL = 3389
M_POINT_AND_TWO_VECTORS = 3391
M_POINT_AND_VECTOR = 4670
M_POINT_BASED = 3300
M_POINT_CLOUD = 3856
M_POINT_CLOUD_INDEX_FLAG = 671088640
M_POINT_CLOUD_INDEX_VALUE = 1938
M_POINT_CLOUD_LABEL_FLAG = 402653184
M_POINT_CLOUD_LABEL_VALUE = 1937
M_POINT_CLOUD_ORGANIZED = 1920
M_POINT_CLOUD_RESULT = 1903
M_POINT_CLOUD_TYPE = 1915
M_POINT_CLOUD_UNORGANIZED = 3857
M_POINT_INPUT_UNITS = 1394
M_POINT_SELECTED = 3635
M_POINT_TO_PLANE = 1958
M_POINT_TO_POINT = 1957
M_POLAR = 5
M_POLARITY = 16384
M_POLAR_TO_RECTANGULAR = 2
M_POLAR_TO_RECTANGULAR_LUT = 65536
M_POLLING_FOR_END_OF_XFER = 4328
M_POLYGON = 64
M_POLYLINE = 32
M_POLYLINE_SEED = 444
M_PORT_NAME = 8704
M_PORT_NAME_LENGTH = 5497558147584
M_POSITION = 1026
M_POSITION_ABSOLUTE = 49
M_POSITION_ACCURACY = 13
M_POSITION_CONSTRAINED_ORDER_FLAG = 2097152
M_POSITION_DELTA_NEG_X = 127
M_POSITION_DELTA_NEG_Y = 129
M_POSITION_DELTA_POS_X = 128
M_POSITION_DELTA_POS_Y = 130
M_POSITION_END = 56
M_POSITION_END_X = 13314
M_POSITION_END_Y = 17410
M_POSITION_IN_STRING_FLAG = 6291456
M_POSITION_RELATIVE = 50
M_POSITION_START = 55
M_POSITION_START_TRIGGER = 213
M_POSITION_START_X = 9
M_POSITION_START_Y = 10
M_POSITION_TRIGGER = 200
M_POSITION_TRIGGER_MULTIPLE = 212
M_POSITION_TYPE = 1524
M_POSITION_VALUE = 1026
M_POSITION_X = 13312
M_POSITION_XY = 1
M_POSITION_XY_ANGLE = 2
M_POSITION_XY_ANGLE_SCALE = 3
M_POSITION_Y = 17408
M_POSITION_Z = 3960
M_POSITIVE = 2
M_POSTNET = 512
M_POSTNET_NAME = MIL_TEXT("Postnet")
M_POST_CONTROL = 67108864
M_POST_DISPDESELECT_OPERATIONS = 10062
M_POST_DISPSELECT_OPERATIONS = 10060
M_POST_FLIP_COMPLEX_BUFFER = 8388610
M_POST_GRAB_BUFFER_CHANGE = 11
M_POST_OVERLAY_ID_CHANGE = 42
M_POST_SCHEME_CHANGE = 11
M_POS_COMP_RES_LAYER = 3
M_POWER = 6
M_POWER_EXTERNAL_SOURCE_PRESENT = 2579
M_POWER_OVER_CABLE = 2560
M_POWER_OVER_CABLE_OVER_CURRENT_DETECTION_DELAY = 2577
M_POWER_OVER_CABLE_STATUS = 3072
M_PPC_7400 = 10243
M_PREALIGNMENT_MODE = 1942
M_PRECINCT_SIZE_X = 2606
M_PRECINCT_SIZE_Y = 2640
M_PRECISE = 262144
M_PRECISION = 1482
M_PRECONVERT_GAMMA = 226
M_PRECONVERT_MODE = 40
M_PREDEFINED = 1967
M_PREDICTED_CLASS_SCORES = 3739
M_PREDICTED_SCORE_AVERAGE = 3765
M_PREDICTED_SCORE_MAX = 3764
M_PREDICTED_SCORE_MIN = 3763
M_PREDICTOR = 5052
M_PREDICT_CNN_RESULT = 3754
M_PREDICT_CONTEXT_ID = 3683
M_PREDICT_ENTRY = 65029
M_PREDICT_MODE = 2859
M_PREDICT_NOT_PERFORMED = 2788
M_PREDICT_SCORE = 3684
M_PREDICT_SCORES_ALL_CLASSES_HISTOGRAM = 3938
M_PREDICT_SCORES_COMPLEMENTS_HISTOGRAM = 3937
M_PREDICT_SCORES_HISTOGRAM = 3936
M_PREDICT_SCORE_AVERAGE = 3687
M_PREDICT_SCORE_MAX = 3686
M_PREDICT_SCORE_MIN = 3685
M_PREDICT_TREE_ENSEMBLE_RESULT = 3756
M_PREFERED_DISPLAY_FORMAT = 10025
M_PREFERRED_BUFFER_FORMAT = 4374
M_PREFERRED_DIGITIZER_FORMAT = 5242
M_PREFERRED_DISPLAY_SYSTEM = 2301
M_PREFER_COLOR_DISPLAY_RESOLUTION = 10162
M_PREFETCH = 32
M_PREPROCESS = 2
M_PREPROCESSED = 14
M_PREPROCESSING = 2
M_PREPROCESS_END = 6
M_PREPROCESS_START = 5
M_PREREGISTRATION_MATRIX = 3560
M_PREREGISTRATION_MODE = 3564
M_PRESEARCH_LONG_STRING = 976
M_PRESENT = 2
M_PRESERVE_SHAPE_AVERAGE = 1783
M_PRETRAINED = 3782
M_PREVIOUS = 1073741827
M_PREVIOUS_FRAME = 101
M_PREVIOUS_LINE = 102
M_PREWITT = 9437192
M_PREWITT_X = 9437205
M_PREWITT_Y = 9437206
M_PRE_APP_FREE = 31
M_PRE_DISPDESELECT_OPERATIONS = 10061
M_PRE_DISPSELECT_OPERATIONS = 10059
M_PRE_FLIP_COMPLEX_BUFFER = 8388609
M_PRE_GRAB_BUFFER_CHANGE = 10
M_PRE_OVERLAY_ID_CHANGE = 41
M_PRE_SCHEME_CHANGE = 10
M_PRIMARY_DIRECTION = 4096
M_PRIMARY_SURFACE = 274877906944
M_PRIMARY_SURFACE_FORMAT = 4510
M_PRIMARY_SURFACE_ID = 1122
M_PRIMARY_SURFACE_ID_CHANGED = 44
M_PRIMARY_SURFACE_PITCH_BYTE = 4514
M_PRIMARY_SURFACE_SIZE_BITS = 4511
M_PRIMARY_SURFACE_SIZE_X = 4512
M_PRIMARY_SURFACE_SIZE_Y = 4513
M_PRINCIPAL_COMPONENTS = 615
M_PRINCIPAL_COMPONENT_PROJECTION = 605
M_PRINCIPAL_POINT_X = 103
M_PRINCIPAL_POINT_Y = 104
M_PRINT_DISABLE = 0
M_PRINT_ENABLE = 1
M_PRINT_GROWTH = 40969
M_PRINT_GROWTH_GRADE = 36866
M_PRIORITY = 16384
M_PROBABILITY = 32768
M_PROC = 16
M_PROCESSABLE = 28
M_PROCESSING = 15006
M_PROCESSING_COMPLETED = 1
M_PROCESSING_ERROR = 34
M_PROCESSING_FPGA_FAN_RPM = 2364
M_PROCESSING_FPGA_REGISTER_PHYSICAL_ADDRESS = 6701
M_PROCESSING_FPGA_REGISTER_RANGE = 4804
M_PROCESSING_FPGA_USAGE = 2600
M_PROCESSING_MODULE_COUNT = 4802
M_PROCESSING_PACK_REVISION = 15833
M_PROCESSING_SYSTEM_TYPE = 2009
M_PROCESSING_UNIT_END = 299
M_PROCESSING_UNIT_START = 0
M_PROCESSOR_NUM = 2006
M_PROCESSOR_TYPE = 10240
M_PROCESS_FRAME_CORRUPTED = 6925
M_PROCESS_FRAME_COUNT = 5335
M_PROCESS_FRAME_MISSED = 5334
M_PROCESS_FRAME_MISSED_RESET = 5333
M_PROCESS_FRAME_RATE = 6607
M_PROCESS_GRAB_MONITOR = 5351
M_PROCESS_NUMBER_OF_FRAME = 5353
M_PROCESS_PENDING_GRAB_NUM = 6926
M_PROCESS_TIMEOUT = 5364
M_PROCESS_TOTAL_BUFFER_NUM = 6927
M_PROCMAN_ATTRIBUTE_BITS = -65536
M_PROC_CURRENT_VERSION = 10.4
M_PROC_FIRST_LEVEL = 50
M_PROC_GPU = 1152921504606846976
M_PROC_HOST_ID = 1105
M_PROC_LAST_LEVEL = 51
M_PROC_ON_ACCELERATED = 61
M_PROC_VERSION_100 = 10
M_PROC_VERSION_100_PP1 = 10.1
M_PROC_VERSION_100_PP2 = 10.2
M_PROC_VERSION_100_PP3 = 10.3
M_PROC_VERSION_100_SP4 = 10.4
M_PROC_VERSION_75 = 7.5
M_PROC_VERSION_75_PP1 = 7.51
M_PROC_VERSION_80 = 8
M_PROC_VERSION_80_PP1 = 8.1
M_PROC_VERSION_80_PP2 = 8.2
M_PROC_VERSION_80_PP3 = 8.3
M_PROC_VERSION_80_PP4 = 8.4
M_PROC_VERSION_90 = 9
M_PROC_VERSION_90_PP1 = 9.1
M_PROC_VERSION_90_PP2 = 9.2
M_PRODUCT_MODEL = 7710
M_PRODUCT_SENSOR = 7711
M_PROFILE_BASELINE = 102
M_PROFILE_CAVLC = 109
M_PROFILE_DEPTH_MAP = 3900
M_PROFILE_EXTENDED = 105
M_PROFILE_HIGH = 104
M_PROFILE_HIGH10 = 106
M_PROFILE_HIGH422 = 107
M_PROFILE_HIGH444 = 108
M_PROFILE_MAIN = 103
M_PROFILE_PLANE_X = 3893
M_PROFILE_PLANE_Y = 3894
M_PROFILE_POINT_CLOUD = 3901
M_PROFILE_RESULT = 3910
M_PROFILE_TYPE = 3890
M_PROFINET_HARDWARE_SUPPORTED = 4400
M_PROFINET_MAC_ADDRESS = 6706
M_PROGRESSION_ORDER = 8214
M_PROGRESSIVE = 1
M_PROJECTION = 3417
M_PROJECT_SHAPE_CONTEXT = 8
M_PROJ_LIST = 16384
M_PROPAGATE_CALIBRATION_TO_OVERLAY = 10063
M_PROPORTIONAL_ARROWHEADS = 8
M_PROXIMITY_MATRIX = 3792
M_PROXIMITY_MATRIX_SIZE_X = 3791
M_PROXIMITY_MATRIX_SIZE_Y = 3981
M_PSEUDO = 8388610
M_PSEUDOMEDIAN = 1883
M_PSEUDO_COLOR = 16384
M_PSEUDO_ID = 8388608
M_PSEUDO_LIVE_GRAB_NB_FIELDS = 2070
M_PSEUDO_LIVE_GRAB_NB_FRAMES = 2069
M_PSEUDO_LIVE_GRAB_TIME = 2072
M_PSEUDO_LIVE_GRAB_WITH_DDRAW = 2074
M_PSEUDO_LUT = 8388610
M_PUBLICATION_ERROR = 133
M_PULSE_GENERATION = 65
M_PULSE_HIGH = 86
M_PULSE_LOW = 87
M_PULSE_MEASUREMENT = 66
M_PUNCTUATION = 1
M_PUNCTUATIONS = 1
M_PU_BASE = 3
M_PU_FID = 5376
M_PU_INSTANCE_NUMBER = 1819
M_PU_LIST = 4098
M_PU_NAME = 4352
M_PU_NAME_LENGTH = 5497558143232
M_PU_SELECT = 4112
M_PWM = 512
M_Q12G = 8388608
M_Q3G = 65536
M_Q6G = 33554432
M_QA = 131072
M_QBCL = 67108864
M_QCH = 524288
M_QD = 8388608
M_QHA = 1048576
M_QRCODE = 67108864
M_QRCODE_NAME = MIL_TEXT("QRCode")
M_QSV = 256
M_QT_MODE = 10151
M_QUAD = 5
M_QUANTIZATION = 1152
M_QUANTIZATION_CHROMINANCE = 1127
M_QUANTIZATION_INTERNAL = 2602
M_QUANTIZATION_LUMINANCE = 1126
M_QUANTIZATION_MODIFIED = 2604
M_QUANTIZATION_STYLE = 2642
M_QUARTER_MAX_CHAR_WIDTH = 67108864
M_QUEUE = 1024
M_QUEUED = 67108864
M_QUEUE_FULL_MODE = 20
M_QUEUE_SIZE = 19
M_QUIET = 134217728
M_QUIET_ZONE_BOTTOM_LEFT_X = 3039
M_QUIET_ZONE_BOTTOM_LEFT_Y = 1025
M_QUIET_ZONE_BOTTOM_RIGHT_X = 1026
M_QUIET_ZONE_BOTTOM_RIGHT_Y = 1027
M_QUIET_ZONE_INCLUDED = 45066
M_QUIET_ZONE_TOP_LEFT_X = 1020
M_QUIET_ZONE_TOP_LEFT_Y = 1021
M_QUIET_ZONE_TOP_RIGHT_X = 1022
M_QUIET_ZONE_TOP_RIGHT_Y = 1023
M_Q_FACTOR = 2564
M_Q_FACTOR_CHROMINANCE = 5057
M_Q_FACTOR_LUMINANCE = 5056
M_RADIAL = 777
M_RADIENT = 10
M_RADIENTCLHS_FINGERPRINT = 21168
M_RADIENTCXP_FINGERPRINT = 21152
M_RADIENTEVCL_FINGERPRINT = 21024
M_RADIENTPRO = 15
M_RADIENTPRO_FINGERPRINT = 21136
M_RADIENT_FINGERPRINT = 21088
M_RADII_DIRECTION = 2795
M_RADIUS = 64
M_RADIUS_SCORE = 270532608
M_RADIUS_X = 1210
M_RADIUS_Y = 1211
M_RANDOM_SAMPLING = 3601
M_RANDOM_SAMPLING_CONFIDENCE = 3604
M_RANDOM_SAMPLING_NUMBER_OF_TEST_POINTS = 3605
M_RANGE_FACTOR_GAUSSIAN_CURVATURE = 3362
M_RANGE_FACTOR_LOCAL_SHAPE = 3364
M_RANGE_FACTOR_MEAN_CURVATURE = 3363
M_RANGE_FINITE = 1
M_RANK_INDEX = 2097152
M_RAPIXO = 110
M_RAPIXOCL_FINGERPRINT = 20928
M_RAPIXOCXP = 110
M_RAPIXOCXP_FINGERPRINT = 20864
M_RAP_GRADE = 36876
M_RASTER = 1416
M_RASTERIZE = 1415
M_RASTERIZE_AND_DISCARD_LIST = 1414
M_RAW = 2
M_RAW_CALL_SUPPORT = 4393
M_RAW_DATA = 148
M_RAW_FORMAT = 0
M_RAYLEIGH = 3
M_READ = 1
M_READY_TO_BE_FREED = 15387
M_READ_ACCURACY = 51
M_READ_BROKEN_CHAR = 104
M_READ_CERTAINTY = 98
M_READ_FAST_FIND = 55
M_READ_FIRST_LEVEL = 52
M_READ_LAST_LEVEL = 53
M_READ_MODEL_STEP = 58
M_READ_NOT_PERFORMED = 2552
M_READ_ONLY = 32
M_READ_OUT = 103
M_READ_OUT_NO_LATCH = 104
M_READ_PREFETCH_ENABLED = 268435456
M_READ_PREFETCH_EXTRA_BYTES = 32
M_READ_ROBUSTNESS = 56
M_READ_SPEED = 50
M_READ_TIMEOUT = 2054
M_READ_TOUCHING_CHAR = 105
M_READ_WRITE = 16
M_REAL = 64
M_REAL_FORMAT = 1050
M_REAL_HOST_ADDRESS = 14002
M_REAL_INDEX_MASK = 255
M_REAL_OFFSET_X = 6614
M_REAL_OFFSET_Y = 6615
M_REAL_OWNER_SYSTEM = 9
M_REAL_PART = 4096
M_REAL_TRACE_LEVEL = 15044
M_REAL_ZOOM_FACTOR_X = 6607
M_REAL_ZOOM_FACTOR_Y = 6608
M_REARRANGE_CONTEXT = 5
M_REAR_VIEW = 4173
M_REBOOT_NEEDED = 15005
M_RECEPTIVE_FIELD_PATCH = 3752
M_RECEPTIVE_FIELD_SIZE_X = 3379
M_RECEPTIVE_FIELD_SIZE_Y = 3380
M_RECOMMENDED_APERTURE_SIZE = 32803
M_RECONSTRUCT = 1892
M_RECONSTRUCTION = 1908
M_RECONSTRUCT_FROM_SEED = 1
M_RECTANGLE = 64
M_RECTANGLE_HEIGHT = 1213
M_RECTANGLE_SELECTION = 1744
M_RECTANGLE_WIDTH = 1212
M_RECTANGULAR = 16
M_RECTANGULARITY = 127
M_RECTANGULAR_TO_POLAR = 1
M_RECTANGULAR_TO_POLAR_LUT = 32768
M_RECTS = 256
M_RECURSIVE = 262144
M_RED = 8
M_REFERENCE = 67108864
M_REFERENCE_ANGLE = 110
M_REFERENCE_FRAME = 205
M_REFERENCE_LATCH_ACTIVATION = 5550
M_REFERENCE_LATCH_STATE = 5600
M_REFERENCE_LATCH_TRIGGER_SOURCE = 5510
M_REFERENCE_LATCH_VALUE = 262144
M_REFERENCE_SAMPLE = 16781311
M_REFERENCE_SAMPLE_INDEX = 4094
M_REFERENCE_SAMPLE_LABEL = 4095
M_REFERENCE_VALUE = 6700
M_REFERENCE_VALUE_CURRENT = 4611686018427387904
M_REFERENCE_X = 100
M_REFERENCE_Y = 101
M_REFLECTANCE_CALIBRATION = 1634
M_REFLECTANCE_MARGIN_GRADE = 36940
M_REFOCUS = 16777216
M_REFRESH_RATE = 4560
M_REF_CHAR_SIZE_Y = 827
M_REF_CHAR_THICKNESS = 826
M_REGION_ACCURACY_HIGH = 99
M_REGION_ACTIVE = 1086
M_REGION_ANGLE = 46
M_REGION_ANGLE_END = 215
M_REGION_ANGLE_END_TYPE = 1735
M_REGION_ANGLE_START = 214
M_REGION_ANGLE_START_TYPE = 1734
M_REGION_ANGLE_TYPE = 1731
M_REGION_BUFFER_ID = 1112
M_REGION_COPY = 1056
M_REGION_DELETE_AT_EACH_FRAME = 32
M_REGION_END = 1778
M_REGION_END_TYPE = 1780
M_REGION_END_X = 220
M_REGION_END_X_TYPE = 1738
M_REGION_END_Y = 221
M_REGION_END_Y_TYPE = 1739
M_REGION_GEOMETRY = 206
M_REGION_GRAPHIC_LIST_ID = 1111
M_REGION_HEIGHT = 210
M_REGION_HEIGHT_TYPE = 1730
M_REGION_INDEX_FLAG = 16777216
M_REGION_INSIDE_COLOR = 3224
M_REGION_INSIDE_SHOW = 3222
M_REGION_KEEP = 0
M_REGION_LINK = 1066
M_REGION_LINK_OFFSET_X = 1067
M_REGION_LINK_OFFSET_Y = 1068
M_REGION_MODIFICATION_COUNT = 1069
M_REGION_OFFSET_X = 4259840
M_REGION_OFFSET_Y = 4325376
M_REGION_OUTSIDE_COLOR = 3223
M_REGION_OUTSIDE_SHOW = 3221
M_REGION_POSITION = 1775
M_REGION_POSITION_TYPE = 1776
M_REGION_POSITION_X = 207
M_REGION_POSITION_X_TYPE = 1727
M_REGION_POSITION_Y = 208
M_REGION_POSITION_Y_TYPE = 1728
M_REGION_PRESENT = 1461
M_REGION_RADIUS = 222
M_REGION_RADIUS_END = 213
M_REGION_RADIUS_END_TYPE = 1733
M_REGION_RADIUS_START = 212
M_REGION_RADIUS_START_TYPE = 1732
M_REGION_RADIUS_TYPE = 1740
M_REGION_SIZE_X = 4390912
M_REGION_SIZE_Y = 4718592
M_REGION_START = 1777
M_REGION_START_TYPE = 1779
M_REGION_START_X = 218
M_REGION_START_X_TYPE = 1736
M_REGION_START_Y = 219
M_REGION_START_Y_TYPE = 1737
M_REGION_STREAM = 6801
M_REGION_STREAM_SIZE_BYTE = 1055
M_REGION_TYPE = 1058
M_REGION_USE = 1065
M_REGION_WIDTH = 209
M_REGION_WIDTH_TYPE = 1729
M_REGISTER = 256
M_REGISTER_EDITOR = 64
M_REGISTER_EXTERN_BUFFER_API_MODULE = 4597
M_REGISTER_FUNCTION = 4294967296
M_REGISTER_HOOK_THREAD = 1
M_REGISTRATION_COMPLETED = 3501
M_REGISTRATION_GLOBAL = 33554432
M_REGISTRATION_INDEX_FLAG = 2097152
M_REGISTRATION_INDEX_VALUE = 3534
M_REGISTRATION_MATRIX = 3504
M_REGISTRATION_TYPE = 1
M_REGULAR = 131072
M_REGULARIZATION_MODE = 2020
M_REGULARIZATION_SIZE = 2021
M_REGULAR_ANGLE = 16
M_REGULAR_EDGE_DETECT = 80
M_REGULAR_GRADIENT = 64
M_REGULAR_MODEL = 2209
M_REG_CONTEXT_MASK = 34896609621
M_REG_DEF_2_END = 24791
M_REG_DEF_2_START = 23000
M_REG_DEF_3_END = 25369
M_REG_DEF_3_START = 25050
M_REG_DEF_END = 16521
M_REG_DEF_START = 15976
M_REG_DFF_CONTEXT = 34896609296
M_REG_DFF_RESULT = 34896609312
M_REG_EDOF_CONTEXT = 34896609284
M_REG_EDOF_RESULT = 34896609288
M_REG_FULL_SIZE = 8198
M_REG_HDR_CONTEXT = 34896609536
M_REG_HDR_RESULT = 34896609792
M_REG_IOCTL_OFFSET = 8200
M_REG_OBJECT = 34896609280
M_REG_OBJECT_MASK = 34896610303
M_REG_PHOTOMETRIC_STEREO_CONTEXT = 34896609344
M_REG_PHOTOMETRIC_STEREO_RESULT = 34896609408
M_REG_RESULT = 34896609282
M_REG_RESULT_MASK = 34896609962
M_REG_STITCHING_CONTEXT = 34896609281
M_REG_STITCHING_RESULT = 34896609282
M_REG_USER_OFFSET = 8199
M_REG_USER_SIZE = 8197
M_REJECTED_EQUAL_BACKGROUND = 662
M_REJECTED_EQUAL_SELECTED = 660
M_REJECTED_LABEL = 73
M_RELATIVE = 21
M_RELATIVE_APERTURE_FACTOR = 32836
M_RELATIVE_COORDINATE_SYSTEM = 0
M_RELATIVE_MODE = 8192
M_RELATIVE_ORIGIN_ANGLE = 115
M_RELATIVE_ORIGIN_X = 112
M_RELATIVE_ORIGIN_Y = 113
M_RELATIVE_ORIGIN_Z = 114
M_RELATIVE_TO_ROOT = 65536
M_RELEVANCE_ACCEPTANCE = 202
M_RELEVANCE_SCORE = 834
M_REMOTE = 0
M_REMOTE_BUFFER_EVENT = 18
M_REMOTE_DISPLAY = 1
M_REMOTE_DISPLAY_CONTROL = 536870912
M_REMOTE_MAPPING_SUPPORT = 4389
M_REMOVE = 4
M_REMOVE_CALIBRATION_USE = 18
M_REMOVE_DESTINATION = 1193
M_REMOVE_LAST_SCAN = 1493
M_REMOVE_NON_FINITE = 1
M_RENDER_BUFFER_ID = 1121
M_RENDER_TO_BUFFER = 4194304
M_REPLACE = 16777312
M_REPLACE_MAX = 16777315
M_REPLACE_MIN = 16777316
M_REPLACE_MISSING_DATA = 3090
M_REPLICATE = 262144
M_REPLICATE_BORDER = 32768
M_REPORT_ERRORS = 799
M_REPORT_NUMBER_OF_ERRORS = 796
M_REPORT_NUMBER_OF_OPTIMIZATIONS = 798
M_REPORT_NUMBER_OF_WARNINGS = 797
M_REPORT_OPTIMIZATIONS = 801
M_REPORT_STRING = 819
M_REPORT_WARNINGS = 800
M_RESEGMENTATION_METHOD = 966
M_RESERVED_ID_END = 2130706500
M_RESERVE_CLUSTER_NODE = 15722
M_RESET = 9
M_RESET_ASSOCIATED_LUT = 5243
M_RESET_CONTINUOUS_GRABBER = 4307
M_RESET_CRTC = 9400
M_RESET_DEFAULTS = 15049
M_RESET_EXTREMES = 8
M_RESET_FROM_DETECTED_RESULTS = 5
M_RESET_FROM_TRAINED_RESULTS = 2586
M_RESET_IMPLICIT_CONSTRAINTS = 2466
M_RESET_PERMITTED_CHARS = 2284
M_RESET_POSITION_TO_IMPLICIT_CONSTRAINTS = 2337
M_RESET_RESOLUTION = MIL_TEXT("M_RESET_RESOLUTION")
M_RESET_SYSDETECT = 15066
M_RESET_TRAINING_VALUES = 3719
M_RESET_WIDTH = 0
M_RESET_WINDOW_SIZE = 10176
M_RESHAPE_FOLLOWING_DISTORTION = 3
M_RESHAPE_FROM_POINTS = 1
M_RESIZABLE = 51
M_RESIZE = 1
M_RESIZED = 2
M_RESIZE_DOWN = 107
M_RESIZE_HEIGHT = 2769
M_RESIZE_UP = 108
M_RESIZE_WIDTH = 2768
M_RESOLUTION = 7
M_RESOLUTION_X = 1062
M_RESOLUTION_Y = 1063
M_RESP_BUTTONS_MASK = 15
M_RESP_CANCEL = 4
M_RESP_NO = 2
M_RESP_OK = 8
M_RESP_YES = 1
M_RESP_YES_NO = 3
M_RESP_YES_NO_CANCEL = 7
M_RESTART_INTERVAL = 5059
M_RESTORE = 16
M_RESTORED_CALIBRATION = 1491
M_RESTORE_RESOLUTION = MIL_TEXT("M_RESTORE_RESOLUTION")
M_RESTORE_VIDEO_MEMORY = 9045
M_RESTRICTED_MOUSE_ACTIVATED = 3217
M_RESTRICT_CURSOR = 10055
M_RESTRICT_FOCUS = 10056
M_RESTRICT_WINDOWS = 10183
M_REST_SERVER = 2
M_RESULT = 4096
M_RESULTS_DISPLACEMENT_MODE = 1898
M_RESULTS_DISPLACEMENT_Y = 1899
M_RESULT_ALL_OCCURRENCES = 1073741824
M_RESULT_ID = 3691
M_RESULT_MET = 128
M_RESULT_MOD = 16
M_RESULT_OUTPUT_UNITS = 1300
M_RESULT_PAT = 32
M_RESULT_POINT_CLOUD_3DMAP = 144
M_RESULT_SIZE = 0
M_RESULT_TYPE = 1
M_RESUSCITATE_SCHEME = 15392
M_RES_LAYER_COMP_POS = 1
M_RES_POS_COMP_LAYER = 2
M_RETURN_DISTANCE = 1048576
M_RETURN_INDEX = 16384
M_RETURN_LABEL = 32768
M_RETURN_PARTIAL_RESULTS = 70
M_RETURN_VALUE_AS_FLOAT_IN_INT = 8192
M_RETURN_X = 2097152
M_REVERSE = 4
M_REVERSE_TRANSFORMATION_MATRIX = 73
M_REVERSE_TRANSFORMATION_MATRIX_ID = 53
M_REVERSE_X = 5087
M_REVERSE_Y = 5088
M_REVISION = 4596
M_RGB = 8
M_RGB15 = 1536
M_RGB16 = 1792
M_RGB192 = 5120
M_RGB24 = 2048
M_RGB3 = 3328
M_RGB32 = 2304
M_RGB48 = 2816
M_RGB555_BUFFER_ALLOCATION = 2045
M_RGB96 = 3072
M_RGBX32 = 2304
M_RGB_BGR_EXTENDED_RANGE_END = 14080
M_RGB_BGR_EXTENDED_RANGE_START = 12288
M_RGB_BGR_RANGE_END = 5120
M_RGB_BGR_RANGE_START = 1536
M_RGB_COLOR = 1073741824
M_RGB_COLOR_MODE = 13
M_RGB_MODULE_NUM = 2012
M_RGB_MODULE_TYPE = 2013
M_RGB_NORMALIZE = 10485770
M_RGB_PIXEL_SWAP = 4373
M_RGB_TO_H = 10485766
M_RGB_TO_HLS = 10485761
M_RGB_TO_HSL = 10485761
M_RGB_TO_HSV = 10485771
M_RGB_TO_L = 10485762
M_RGB_TO_MONO = 12
M_RGB_TO_RGB = 13
M_RGB_TO_Y = 10485765
M_RGB_TO_YCBCRHD = 16
M_RGB_TO_YCBCRSD = 15
M_RGB_TO_YCRCBHD = 16
M_RGB_TO_YCRCBSD = 15
M_RGB_TO_YUV = 14
M_RGB_TO_YUV16 = 10485861
M_RIGHT = 512
M_RIGHT_HALF = 512
M_RIGHT_TO_LEFT = 21
M_RIGHT_VIEW = 4171
M_RIGID = 3411
M_RIGID_MATRIX = 5371
M_RING = 256
M_RING_CENTER = 46080
M_RING_RADII = 193536
M_RING_SECTOR = 512
M_RLE = 4227072
M_RLE_BUFFER_TYPE = 2675
M_RLE_LABEL = 8421376
M_RMS_ERROR = 3502
M_RMS_ERROR_RELATIVE = 3503
M_RMS_ERROR_RELATIVE_THRESHOLD = 3566
M_RMS_ERROR_RELATIVE_THRESHOLD_REACHED = 3570
M_RMS_ERROR_THRESHOLD = 3565
M_RMS_ERROR_THRESHOLD_REACHED = 3569
M_RNG_AUTO = 3422
M_RNG_INIT_VALUE = 3464
M_ROBOT_BASE_COORDINATE_SYSTEM = 3
M_ROBUST = 1999
M_ROBUST_FIT = 3067
M_ROI_AUTO_RESET = 10201
M_ROI_BUFFER_OFFSET_X = 10515
M_ROI_BUFFER_OFFSET_Y = 10516
M_ROI_BUFFER_SIZE_X = 10517
M_ROI_BUFFER_SIZE_Y = 10518
M_ROI_CHANGE = 49
M_ROI_CHANGE_END = 50
M_ROI_DEFINE = 10500
M_ROI_DISPCONTROL_END = 10550
M_ROI_DISPCONTROL_START = 10500
M_ROI_DISPLAY_OFFSET_X = 10511
M_ROI_DISPLAY_OFFSET_Y = 10512
M_ROI_DISPLAY_SIZE_X = 10513
M_ROI_DISPLAY_SIZE_Y = 10514
M_ROI_HANDLE_COLOR = 10509
M_ROI_HANDLE_RELEASE = 51
M_ROI_HANDLE_SIZE = 10510
M_ROI_LINE_COLOR = 10503
M_ROI_LINE_WIDTH = 10508
M_ROI_MINIMUM_SIZE = 10520
M_ROI_RECT_BUFFER = 10506
M_ROI_RECT_DISPLAY = 10505
M_ROI_RESET = 10504
M_ROI_SET_POINT = 10507
M_ROI_SHAPE = 10519
M_ROI_SHOW = 10501
M_ROI_SUPPORT = 10502
M_ROLE_IO_MASK = 17920
M_ROLE_UNUSED_1 = 1
M_ROLL = 51
M_ROOT_NODE = 0
M_ROOT_PATH = 3744
M_ROTARY_ENCODER = 1792
M_ROTARY_ENCODER1 = 1808
M_ROTARY_ENCODER2 = 1824
M_ROTARY_ENCODER3 = 1840
M_ROTARY_ENCODER4 = 1856
M_ROTARY_ENCODER_BIT0_SOURCE = 200704
M_ROTARY_ENCODER_BIT1_SOURCE = 204800
M_ROTARY_ENCODER_DIRECTION = 159744
M_ROTARY_ENCODER_DIVIDER = 172032
M_ROTARY_ENCODER_FORCE_VALUE_SOURCE = 208896
M_ROTARY_ENCODER_FRAME_END_POSITION = 155648
M_ROTARY_ENCODER_FRAME_END_READ = 212992
M_ROTARY_ENCODER_GRAB_LINE_READ = 163840
M_ROTARY_ENCODER_HANDLER_PTR = 5400
M_ROTARY_ENCODER_HANDLER_USER_PTR = 5401
M_ROTARY_ENCODER_INDEX = 8781824
M_ROTARY_ENCODER_MULTIPLIER = 167936
M_ROTARY_ENCODER_ON_GRAB_LINE = 163840
M_ROTARY_ENCODER_OUTPUT1_MODE = 188416
M_ROTARY_ENCODER_OUTPUT2_MODE = 192512
M_ROTARY_ENCODER_OUTPUT_MODE = 184320
M_ROTARY_ENCODER_POSITION = 147456
M_ROTARY_ENCODER_POSITION_START_TRIGGER = 221184
M_ROTARY_ENCODER_POSITION_TRIGGER = 151552
M_ROTARY_ENCODER_POSITION_TRIGGER_DOUBLE = 237568
M_ROTARY_ENCODER_RESET_ACTIVATION = 217088
M_ROTARY_ENCODER_RESET_SOURCE = 176128
M_ROTARY_ENCODER_RESET_VALUE = 180224
M_ROTARY_ENCODER_STATE = 196608
M_ROTARY_MAX_OUTPUT = 16
M_ROTARY_RANGE_DOUBLE_END = 260096
M_ROTARY_RANGE_DOUBLE_START = 237568
M_ROTATABLE = 52
M_ROTATE = 2
M_ROTATED_MODEL_MINIMUM_SCORE = 1395
M_ROTATE_AROUND_CORNER = 1024
M_ROTATE_POINTS = 210
M_ROTATION = 3410
M_ROTATION_AND_SCALE = 3993
M_ROTATION_AXIS = 4636
M_ROTATION_AXIS_ANGLE = 2
M_ROTATION_AXIS_X = 17
M_ROTATION_AXIS_Y = 18
M_ROTATION_AXIS_Z = 19
M_ROTATION_INDICATOR = 4627
M_ROTATION_MATRIX = 5
M_ROTATION_QUATERNION = 3
M_ROTATION_SPEED = 4634
M_ROTATION_X = 7
M_ROTATION_XYZ = 10
M_ROTATION_XZY = 11
M_ROTATION_Y = 8
M_ROTATION_YXZ = 4
M_ROTATION_YZX = 12
M_ROTATION_Z = 9
M_ROTATION_ZXY = 13
M_ROTATION_ZYX = 14
M_ROUGHNESS = 28
M_ROUNDNESS = 5
M_ROW_NUMBER = 116
M_ROW_NUMBER_OF_DECODED_SCANS = 3592
M_ROW_NUMBER_OF_SCANS = 45057
M_ROW_OVERALL_GRADE = 36912
M_ROW_SPACING = 118
M_RS170 = 1
M_RS232 = 1
M_RS422 = 6
M_RS485 = 2
M_RSS14 = 32768
M_RSS14_STACKED = 524288
M_RSS14_STACKED_OMNI = 1048576
M_RSS14_TRUNCATED = 65536
M_RSSCODE = 16384
M_RSS_EXPANDED = 262144
M_RSS_LIMITED = 131072
M_RT_GPU_ACCESS = 4
M_RUNS = 2475
M_RUNTIME_ERROR = 169
M_RUNTIME_ERROR_1 = 93
M_RUN_LENGTH = 2484
M_RUN_X = 2482
M_RUN_Y = 2483
M_R_MAX = 41033
M_R_MIN = 41032
M_S1200HM = 1125376
M_S1200HT = 1126400
M_S1200T = 1122304
M_S12G = 8192
M_S300CT = 1061120
M_S300HM = 1063936
M_S300HT = 1061888
M_S300T = 1060864
M_S700T = 1077248
M_SA = 262144
M_SAFE_FLOATING_POINT_CONTROL = 15065
M_SAFE_MODE = 10109
M_SAGITTA_TOLERANCE = 1969
M_SAME = -1
M_SAME_AS_COLOR = 4692
M_SAME_AS_INPUT_UNITS = 1776
M_SAME_AS_SOURCE = 112
M_SAME_LOCATION = 8192
M_SAME_OR_REVERSE = 5
M_SAME_X = 5362
M_SAME_Y = 5361
M_SAMPLE_8BIT_AVERAGE_COLOR_BAND_0 = 1424
M_SAMPLE_8BIT_AVERAGE_COLOR_BAND_1 = 1425
M_SAMPLE_8BIT_AVERAGE_COLOR_BAND_2 = 1426
M_SAMPLE_ABSOLUTE_TOLERANCE = 160
M_SAMPLE_AVERAGE_COLOR_BAND_0 = 1427
M_SAMPLE_AVERAGE_COLOR_BAND_1 = 1428
M_SAMPLE_AVERAGE_COLOR_BAND_2 = 1429
M_SAMPLE_BUFFER_FORMAT = 210
M_SAMPLE_COLOR_BAND_0 = 140
M_SAMPLE_COLOR_BAND_1 = 141
M_SAMPLE_COLOR_BAND_2 = 142
M_SAMPLE_COLOR_SIGN = 1457
M_SAMPLE_COLOR_SIZE_BAND = 1456
M_SAMPLE_COLOR_SIZE_BIT = 1455
M_SAMPLE_COLOR_TYPE = 1458
M_SAMPLE_COVERAGE = 830
M_SAMPLE_IMAGE_SIGN = 126
M_SAMPLE_IMAGE_SIZE_BAND = 125
M_SAMPLE_IMAGE_SIZE_BIT = 124
M_SAMPLE_IMAGE_SIZE_X = 122
M_SAMPLE_IMAGE_SIZE_Y = 123
M_SAMPLE_IMAGE_TYPE = 127
M_SAMPLE_INDEX_TAG = 33554432
M_SAMPLE_LABEL_SIGN = 1453
M_SAMPLE_LABEL_SIZE_BAND = 1452
M_SAMPLE_LABEL_SIZE_BIT = 1451
M_SAMPLE_LABEL_TAG = 16777216
M_SAMPLE_LABEL_TYPE = 1454
M_SAMPLE_LABEL_VALUE = 1
M_SAMPLE_LUT_SIGN = 154
M_SAMPLE_LUT_SIZE_BAND = 153
M_SAMPLE_LUT_SIZE_BIT = 152
M_SAMPLE_LUT_SIZE_X = 150
M_SAMPLE_LUT_SIZE_Y = 151
M_SAMPLE_LUT_TYPE = 155
M_SAMPLE_MASKED = 135
M_SAMPLE_MASK_SIGN = 132
M_SAMPLE_MASK_SIZE_BAND = 131
M_SAMPLE_MASK_SIZE_BIT = 130
M_SAMPLE_MASK_SIZE_X = 128
M_SAMPLE_MASK_SIZE_Y = 129
M_SAMPLE_MASK_TYPE = 133
M_SAMPLE_MATCH_STATUS = 809
M_SAMPLE_MOSAIC_DONT_CARE_SIGN = 1620
M_SAMPLE_MOSAIC_DONT_CARE_SIZE_BAND = 1619
M_SAMPLE_MOSAIC_DONT_CARE_SIZE_BIT = 1618
M_SAMPLE_MOSAIC_DONT_CARE_SIZE_X = 1616
M_SAMPLE_MOSAIC_DONT_CARE_SIZE_Y = 1617
M_SAMPLE_MOSAIC_DONT_CARE_TYPE = 1621
M_SAMPLE_MOSAIC_SIGN = 1614
M_SAMPLE_MOSAIC_SIZE_BAND = 1613
M_SAMPLE_MOSAIC_SIZE_BIT = 1612
M_SAMPLE_MOSAIC_SIZE_X = 1610
M_SAMPLE_MOSAIC_SIZE_Y = 1611
M_SAMPLE_MOSAIC_TYPE = 1615
M_SAMPLE_PCA_VAR1 = 1439
M_SAMPLE_PCA_VAR2 = 1440
M_SAMPLE_PCA_VAR3 = 1441
M_SAMPLE_PCA_VECTOR1_1 = 1430
M_SAMPLE_PCA_VECTOR1_2 = 1431
M_SAMPLE_PCA_VECTOR1_3 = 1432
M_SAMPLE_PCA_VECTOR2_1 = 1433
M_SAMPLE_PCA_VECTOR2_2 = 1434
M_SAMPLE_PCA_VECTOR2_3 = 1435
M_SAMPLE_PCA_VECTOR3_1 = 1436
M_SAMPLE_PCA_VECTOR3_2 = 1437
M_SAMPLE_PCA_VECTOR3_3 = 1438
M_SAMPLE_PIXEL_COUNT = 832
M_SAMPLE_STDDEV = 33
M_SAMPLE_TYPE = 121
M_SATURATION = 8192
M_SATURATION_REF = 6656
M_SATURATION_SIZE_BIT = 1045
M_SATURATION_TYPE = 1047
M_SAVABLE_OBJECT = 32768
M_SAVE = 256
M_SAVE_ANGLE = 12
M_SAVE_AREA_IMAGE = 315
M_SAVE_BASIC_SELECTED_BUFFER = 10064
M_SAVE_CHAIN_ANGLE = 60
M_SAVE_CHAIN_MAGNITUDE = 59
M_SAVE_CHARACTER = 2048
M_SAVE_CONSTRAINT = 512
M_SAVE_CONTROL = 1024
M_SAVE_DERIVATIVES = 11
M_SAVE_IMAGE = 61
M_SAVE_INTERNAL_BUFFERS = 10026
M_SAVE_MAGNITUDE = 13
M_SAVE_MASK = 39
M_SAVE_REPORT = 512
M_SAVE_RUNS = 14
M_SAVE_SUMS = 55
M_SAVE_TARGET_EDGES = 121
M_SAVE_TO_BUFFER = 10204
M_SAVE_TO_FILE = 10203
M_SAVE_TRAINING_IMAGE = 2
M_SBCL = 134217728
M_SC7MS3 = 1073741824
M_SCALAR_EXPLICIT = 2
M_SCALAR_IMPLICIT = 1
M_SCALE = 32784
M_SCALE_BAND_0 = 241
M_SCALE_BAND_1 = 242
M_SCALE_BAND_2 = 243
M_SCALE_DISPLAY = 10557
M_SCALE_MAX_FACTOR = 211
M_SCALE_MIN_FACTOR = 210
M_SCALE_POINTS = 229
M_SCALE_UNIFORM = 3413
M_SCALE_X = 6601
M_SCALE_Y = 6602
M_SCALING_METHOD = 1112
M_SCALING_Y_AVAILABLE = 4052
M_SCAN = 256
M_SCANLINE_HEIGHT = 20224
M_SCANLINE_INPUT_UNITS = 32839
M_SCANLINE_STEP = 20480
M_SCAN_ALL = 4194304
M_SCAN_ALL_FONTS = 16777317
M_SCAN_DECODABILITY = 40977
M_SCAN_DECODABILITY_GRADE = 36885
M_SCAN_DECODE_GRADE = 36879
M_SCAN_DEFECTS = 40976
M_SCAN_DEFECTS_GRADE = 36884
M_SCAN_EDGE_CONTRAST_MINIMUM = 40978
M_SCAN_EDGE_CONTRAST_MINIMUM_GRADE = 36881
M_SCAN_EDGE_DETERMINATION_GRADE = 36887
M_SCAN_EDGE_DETERMINATION_WARNING = 40985
M_SCAN_ERN_MAXIMUM = 40975
M_SCAN_GUARD_PATTERN = 40979
M_SCAN_GUARD_PATTERN_GRADE = 36888
M_SCAN_INTERCHARACTER_GAP = 40982
M_SCAN_INTERCHARACTER_GAP_GRADE = 36891
M_SCAN_LANE_DIRECTION = 1
M_SCAN_LANE_INDEX = 1048576
M_SCAN_LINE_ORDERING_MODE = 4559
M_SCAN_MINIMUM_REFLECTANCE_MARGIN = 40984
M_SCAN_MODE = 4021
M_SCAN_MODULATION = 40974
M_SCAN_MODULATION_GRADE = 36883
M_SCAN_PRINT_CONTRAST_SIGNAL = 40983
M_SCAN_PROFILE_END_X = 41010
M_SCAN_PROFILE_END_Y = 41011
M_SCAN_PROFILE_START_X = 41008
M_SCAN_PROFILE_START_Y = 41009
M_SCAN_QUIET_ZONE = 40980
M_SCAN_QUIET_ZONE_GRADE = 36889
M_SCAN_REFLECTANCE_MAXIMUM = 40973
M_SCAN_REFLECTANCE_MINIMUM = 40972
M_SCAN_REFLECTANCE_MINIMUM_GRADE = 36882
M_SCAN_REFLECTANCE_PROFILE_GRADE = 36886
M_SCAN_REFLECTANCE_PROFILE_LENGTH = 41013
M_SCAN_REFLECTANCE_PROFILE_VALUES = 41012
M_SCAN_RESULT_OFFSET = 10
M_SCAN_SPEED = 2
M_SCAN_SYMBOL_CONTRAST = 40971
M_SCAN_SYMBOL_CONTRAST_GRADE = 36880
M_SCAN_WIDE_TO_NARROW_RATIO = 40981
M_SCAN_WIDE_TO_NARROW_RATIO_GRADE = 36890
M_SCH = 65536
M_SCHEDULER_TYPE = 3492
M_SCORE = 5120
M_SCORE_BACKWARD_COMPATIBILITY = 201728
M_SCORE_FIT = 2461
M_SCORE_K_PARAM = 252
M_SCORE_MAX_DIST_PARAM = 250
M_SCORE_RELEVANCE = 834
M_SCORE_TARGET = 6144
M_SCORE_TOTAL = 168960
M_SCORE_TYPE = 37
M_SCREEN_ID_FROM_SYSTEM_ID = 9208
M_SCREEN_MANAGER_END = 9374
M_SCREEN_MANAGER_START = 9200
M_SCREEN_MANAGER_SYSTEM_ID = 9209
M_SCREEN_RECT = 10213
M_SCREEN_REFRESH_RATE = 16777216
M_SCRIPT_ERROR_CLASS_MISSING = 49506
M_SCRIPT_ERROR_COMPILATION_ERROR = 49502
M_SCRIPT_ERROR_END = 49600
M_SCRIPT_ERROR_FUNCTION_NOT_FOUND = 49504
M_SCRIPT_ERROR_INCORRECT_PROTO = 49505
M_SCRIPT_ERROR_INVALID_CONTROL = 49507
M_SCRIPT_ERROR_NO_FILE_ACCESS = 49501
M_SCRIPT_ERROR_OTHER = 49503
M_SCRIPT_ERROR_PYTHON_ERROR = 49510
M_SCRIPT_ERROR_REF_NOT_FOUND = 49509
M_SCRIPT_ERROR_START = 49500
M_SCRIPT_ERROR_WRAPPER_NOT_FOUND = 49508
M_SCRIPT_FUNCTION = 1073803264
M_SCRIPT_FUNCTION_NAME = 52
M_SCRIPT_FUNCTION_NAME_SIZE = 5497558138932
M_SCRIPT_MODULE_1 = 1073803776
M_SCRIPT_MODULE_2 = 1073804288
M_SCRIPT_PATH = 53
M_SCRIPT_PATH_SIZE = 5497558138933
M_SCRIPT_REFERENCE = 512
M_SCRIPT_REFERENCE_END = 768
M_SCRIPT_REFERENCE_START = 512
M_SDI = 4096
M_SDI_1 = 256
M_SDI_2 = 512
M_SDI_3 = 1024
M_SDI_4 = 2048
M_SEARCH_ANGLE = 256
M_SEARCH_ANGLE_ACCURACY = 4096
M_SEARCH_ANGLE_ACCURACY_MODE = 1420
M_SEARCH_ANGLE_DELTA_NEG = 512
M_SEARCH_ANGLE_DELTA_POS = 1024
M_SEARCH_ANGLE_INPUT_UNITS = 32841
M_SEARCH_ANGLE_INTERPOLATION_MODE = 32768
M_SEARCH_ANGLE_MODE = 128
M_SEARCH_ANGLE_RANGE = 113
M_SEARCH_ANGLE_SIGN = 126
M_SEARCH_ANGLE_STEP = 1536
M_SEARCH_ANGLE_TOLERANCE = 2048
M_SEARCH_ASPECT_RATIO_CONSTRAINT = 2215
M_SEARCH_CHAR_ANGLE = 951
M_SEARCH_MODE = 2214
M_SEARCH_OFFSET_X = 102
M_SEARCH_OFFSET_Y = 103
M_SEARCH_POSITION_FROM_GRAPHIC_LIST = 1723
M_SEARCH_POSITION_RANGE = 119
M_SEARCH_RADIUS_MAX = 120
M_SEARCH_RADIUS_MIN = 121
M_SEARCH_REGION_ANGLE_INTERPOLATION_MODE = 82944
M_SEARCH_REGION_CLIPPING = 8425472
M_SEARCH_REGION_CLIPPING_MIN_AREA = 1690
M_SEARCH_REGION_CLIPPING_MIN_HEIGHT = 1692
M_SEARCH_REGION_CLIPPING_MIN_WIDTH = 1691
M_SEARCH_REGION_CLIPPING_PRESERVE_CENTER = 1693
M_SEARCH_REGION_INPUT_UNITS = 1392
M_SEARCH_REGION_WAS_CLIPPED = 1467
M_SEARCH_SCALE_RANGE = 114
M_SEARCH_SIZE_X = 104
M_SEARCH_SIZE_Y = 105
M_SEARCH_SKEW_ANGLE = 950
M_SEARCH_STRING_ANGLE = 952
M_SECAM = 8
M_SECAM_RGB = 7
M_SECONDARY_DIRECTION = 8192
M_SECONDARY_GRAB_BUFFER = 4370
M_SECONDARY_SOURCE_OFFSET_X = 4028
M_SECONDARY_SOURCE_OFFSET_Y = 4029
M_SECONDARY_SOURCE_SIZE_X = 4026
M_SECONDARY_SOURCE_SIZE_Y = 4027
M_SECOND_DERIVATIVES_ID = 20480
M_SECOND_DERIVATIVE_X = 9437196
M_SECOND_DERIVATIVE_XY = 9437198
M_SECOND_DERIVATIVE_X_ID = 16384
M_SECOND_DERIVATIVE_Y = 9437197
M_SECOND_DERIVATIVE_Y_ID = 4096
M_SECOND_FERET_INDEX = 257
M_SECOND_PERCENTILE = 3482
M_SECTOR = 768
M_SECTOR_RELATIVE = 53
M_SEED_MODE = 3863
M_SEED_PIXELS_ALL_IN_BLOBS = 1
M_SEED_VALUE = 2867
M_SEGMENT = 130
M_SEGMENT_CONSISTENT_GRADIENT = 2943
M_SELECT = 3977
M_SELECTABLE = 50
M_SELECTABLE_SYSTEM_COUNT = 15144
M_SELECTABLE_THREAD = 4096
M_SELECTED = 1103
M_SELECTED_COLOR = 768
M_SELECTED_EQUAL_BACKGROUND = 664
M_SELECTED_FRAME_RATE = 6606
M_SELECTED_FRAME_RATE_FOR_BUFFER = 6611
M_SELECTED_LABEL = 103
M_SELECTED_LINK_COPY = 10123
M_SELECTION_RADIUS = 1219
M_SELECT_LINE = 256
M_SELECT_STRING = 256
M_SELECT_USER_BUFFER_DIRECTLY_ON_DISPLAY = 10111
M_SELECT_VIDEO_SOURCE = 3210
M_SEMI = 3
M_SEMI_M12_92 = 1
M_SEMI_M13_88 = 2
M_SEMI_T10_0701 = 128
M_SEMI_T10_GRADING = 256
M_SENSE = 10
M_SENSOR = 1
M_SENSOR_BLUE_GAIN = 4403
M_SENSOR_GAIN = 4404
M_SENSOR_GREEN_GAIN = 4402
M_SENSOR_PITCH = 5397
M_SENSOR_RED_GAIN = 4401
M_SENSOR_YAW = 5398
M_SEPARATE = 32768
M_SEQUENCE = 8
M_SEQUENCE_CONTEXT = 4398046511104
M_SEQUENCE_CONTEXT_WARNING = 168
M_SEQUENCE_END = 11
M_SEQUENTIAL = 3154
M_SEQ_COMPRESS = 1
M_SEQ_CONTAINER_DESTINATION = 65536
M_SEQ_CONTAINER_INQUIRE_SIZEOF_INT64_END = 6799
M_SEQ_CONTAINER_INQUIRE_SIZEOF_INT64_START = 6700
M_SEQ_CONTAINER_IO_MASK = 3932160
M_SEQ_CONTAINER_IO_MAX_COUNT = 16
M_SEQ_CONTAINER_MASK = 31
M_SEQ_CONTAINER_MAX_COUNT = 32
M_SEQ_CONTAINER_OUTPUT = 4194304
M_SEQ_CONTAINER_SOURCE = 131072
M_SEQ_DECOMPRESS = 2
M_SEQ_ENCAPSULATION = 4
M_SEQ_FILE_MODE_MASK = 3
M_SEQ_HOOK_CONTEXT = 1610612744
M_SEQ_INTERMOD_VALUE_MASK = 16492691193856
M_SERIAL_DEVICE_PORT_NUMBERS = 2336
M_SERIAL_NUMBER = 7703
M_SERIAL_NUMBER_0 = 2099
M_SERIAL_NUMBER_1 = 2100
M_SERIAL_NUMBER_LENGTH = 5497558146583
M_SERVICE = 1024
M_SERVICE_3D_ERROR = 56202
M_SETTING_AUTO_ADJUSTMENT = 1541
M_SET_BACK_TO_ZERO = 2363
M_SET_CALIBRATION_ID = 5
M_SET_CALIBRATION_INFO = 2
M_SET_CLUSTER_NODE_MASK = 545460846592
M_SET_CLUSTER_NODE_OFFSET = 32
M_SET_CURSOR = 73
M_SET_EXPOSURE_ENABLE = 4290
M_SET_GDI_PALETTE_FROM_LUT = 9047
M_SET_LOCATION_PARAM_1 = 1012
M_SET_LOCATION_PARAM_2 = 1013
M_SET_LOCATION_PARAM_3 = 1014
M_SET_LOCATION_PARAM_4 = 1015
M_SET_LOCATION_PARAM_DATA_1 = 1016
M_SET_LOCATION_PARAM_TYPE = 1011
M_SET_LOCATION_TARGET = 1010
M_SET_LOCKED_BUFFER_HOST_ADDRESS = 1051
M_SET_LOCKED_BUFFER_PHYSICAL_ADDRESS = 1052
M_SET_MODIFIED_RECT_EMPTY = 1042
M_SET_NAME = 1
M_SET_REGION_ERROR = 124
M_SET_REGION_ERROR_2 = 153
M_SET_TRAINING_STATE_ALL = 2584
M_SET_USER_CURSOR = 7872
M_SET_VCOUNT = 4263
M_SET_WIDTH_NOMINAL = 11
M_SET_WORLD_OFFSET_Z = 1367
M_SFCL = 2097152
M_SHADING = 4698
M_SHADING_BOUNDARY_BYPASS_HIGH = 5216
M_SHADING_BOUNDARY_BYPASS_LOW = 5215
M_SHADING_CORRECTION = 5206
M_SHADING_CORRECTION_GAIN = 5205
M_SHADING_CORRECTION_GAIN_FIXED_POINT = 5217
M_SHADING_CORRECTION_GAIN_FIX_POINT = 5217
M_SHADING_CORRECTION_GAIN_ID = 1191
M_SHADING_CORRECTION_OFFSET = 5207
M_SHADING_CORRECTION_OFFSET_ID = 1190
M_SHAPE_CIRCLE = 65536
M_SHAPE_ELLIPSE = 131072
M_SHAPE_MASK = 2704
M_SHAPE_NORMALIZATION = 2703
M_SHAPE_RECTANGLE = 262144
M_SHAPE_SEGMENT = 524288
M_SHAPE_SMOOTHNESS = 2705
M_SHARED = 137438953472
M_SHARED_BANDWIDTH = 512
M_SHARED_EDGES = 220
M_SHARED_MEMORY_FREE = 2326
M_SHARED_MEMORY_SIZE = 2330
M_SHARPEN = 9437187
M_SHARPEN2 = 9437188
M_SHARPEN_4 = 9437188
M_SHARPEN_8 = 9437187
M_SHARPNESS = 5108
M_SHEAR_MATRIX = 5233
M_SHEAR_X = 3
M_SHEAR_Y = 4
M_SHEN = 2050
M_SHEN_PREDEFINED_KERNEL = 277872640
M_SHEN_PREDEFINED_KERNEL_INVALID_FACTOR = 311427072
M_SHEN_PREDEFINED_KERNEL_INVALID_TYPE = 294649856
M_SHOW_COUNTER_IN_TITLE = 15383
M_SHOW_TASKBAR = 10057
M_SHOW_WINDOW_IN_TASKBAR = 10196
M_SHRINK = 3409
M_SHRINK_MEMORY = 8207
M_SHUTTER = 5120
M_SIGMA_PIXEL = 33
M_SIGMOID = 11
M_SIGN = 1014
M_SIGNAL = 4096
M_SIGNALED = 16
M_SIGNAL_GAIN = 5235
M_SIGNAL_OFF = 0
M_SIGNED = 134217728
M_SIGNED_DISTANCE_TO_SURFACE = 2988
M_SIGNED_DISTANCE_Z_TO_SURFACE = 2987
M_SILENT = 256
M_SIMD_ERROR_1 = 1
M_SIMD_ERROR_2 = 2
M_SIMILARITY = 3415
M_SIMPLIFIED_CHINESE = 134
M_SIN = 2
M_SINGLE = 16777216
M_SINGLE_BAND = 65280
M_SINGLE_CLASSIFICATION = 2860
M_SINGLE_COLOR = 3969
M_SINGLE_FRAME = 1
M_SINGLE_THREAD = 8192
M_SIZE = 3072
M_SIZE_AND_SPACING = 3932
M_SIZE_BAND = 1005
M_SIZE_BAND_LUT = 1006
M_SIZE_BIT = 1007
M_SIZE_BIT_MASK = 255
M_SIZE_BYTE = 5061
M_SIZE_BYTE_FIRST_FIELD = 5067
M_SIZE_BYTE_SECOND_FIELD = 5068
M_SIZE_X = 1536
M_SIZE_X_BLUE = 1568
M_SIZE_X_CREATE_RESTRICTION = 2329
M_SIZE_X_GREEN = 1552
M_SIZE_X_RED = 1544
M_SIZE_Y = 1537
M_SIZE_Y_BLUE = 1569
M_SIZE_Y_GREEN = 1553
M_SIZE_Y_RED = 1545
M_SIZE_Z = 1538
M_SIZE_Z_BLUE = 1570
M_SIZE_Z_GREEN = 1554
M_SIZE_Z_RED = 1546
M_SKEW_ANGLE = 795
M_SKEW_INTERPOLATION_MODE = 88
M_SKIP_CHECK = 2
M_SKIP_CONTRAST_ENHANCE = 23
M_SKIP_DEFAULT_CONTRAST_ENHANCE = 23
M_SKIP_LAST_LEVEL = 256
M_SKIP_NEWEST = 10004
M_SKIP_NULL_VECTORS = 1
M_SKIP_OLDEST = 10003
M_SKIP_PFNC_CHECK = 2
M_SKIP_PORTABLE_CHECK = 64
M_SKIP_SEARCH = 21
M_SKIP_SEMI_STRING_UPDATE = 16384
M_SKIP_STRING_LOCATION = 22
M_SLAVE = 0
M_SLAVE_DLL_NAME = 50
M_SLAVE_DLL_NAME_SIZE = 5497558138930
M_SLAVE_ERROR_CURRENT = 7
M_SLAVE_ERROR_GLOBAL = 8
M_SLAVE_ERROR_REMOTE_CURRENT = 35
M_SLAVE_FUNCTION_NAME = 51
M_SLAVE_FUNCTION_NAME_SIZE = 5497558138931
M_SLAVE_FUNCTION_OPCODE = 18
M_SLAVE_FUNCTION_PTR = 13
M_SLOPE = 2844
M_SMALLEST_ANGLE = 2537
M_SMART_SCAN = 2097152
M_SMCL = 524288
M_SMOOTH = 9437184
M_SMOOTHNESS = 108
M_SOBEL = 9437191
M_SOBEL_X = 9437203
M_SOBEL_Y = 9437204
M_SOFTWARE = 65536
M_SOFTWARE1 = 65537
M_SOFTWARE2 = 65538
M_SOFTWARE3 = 65539
M_SOFTWARE4 = 65540
M_SOLID = 64
M_SOLID_WITH_WIREFRAME = 96
M_SOLIOS = 120
M_SOLIOS_FINGERPRINT = 20800
M_SOMEONE_HOOKED_TO_ANNOTATIONS_DRAW = 3220
M_SOP_MARKERS = 8221
M_SORT = 2097152
M_SORT1 = 33554432
M_SORT1_DIRECTION = 2472
M_SORT1_DOWN = 167772160
M_SORT1_UP = 33554432
M_SORT2 = 67108864
M_SORT2_DIRECTION = 2473
M_SORT2_DOWN = 201326592
M_SORT2_UP = 67108864
M_SORT3 = 100663296
M_SORT3_DIRECTION = 2474
M_SORT3_DOWN = 234881024
M_SORT3_UP = 100663296
M_SORT_BY_ASCENDING_DISTANCE = 131072
M_SORT_BY_ASCENDING_INDEX = 262144
M_SORT_BY_DESCENDING_INDEX = 393216
M_SORT_CRITERION = 5
M_SORT_DOWN = 2
M_SORT_UP = 1
M_SOURCE = 2800
M_SOURCE_COMPENSATION = 4324
M_SOURCE_DATA_FORMAT = 6706
M_SOURCE_FIRST_IMAGE = 9
M_SOURCE_FRAME_INDEX = 1082
M_SOURCE_INDEX = 0
M_SOURCE_LABEL = 163
M_SOURCE_MUST_EXIST = 2097152
M_SOURCE_NUMBER_OF_FRAMES = 1080
M_SOURCE_OFFSET_BIT = 4055
M_SOURCE_OFFSET_X = 4024
M_SOURCE_OFFSET_Y = 4025
M_SOURCE_OFFSET_Y_DYNAMIC = 4031
M_SOURCE_READ = 3
M_SOURCE_SIZE_X = 4022
M_SOURCE_SIZE_Y = 4023
M_SOURCE_START_IMAGE = 9
M_SOURCE_VALUE = 65536
M_SPACE = 2390
M_SPACE_CHARACTER = 911
M_SPACE_MAX_CONSECUTIVE = 514
M_SPACE_SIZE = 800
M_SPACE_SIZE_MAX = 2359
M_SPACE_SIZE_MAX_MODE = 2369
M_SPACE_SIZE_MIN = 2358
M_SPACE_SIZE_MIN_MODE = 2459
M_SPACE_WIDTH = 800
M_SPACE_WIDTH_VALUE = 805
M_SPACING = 512
M_SPACING_SCORE = 275775488
M_SPACING_X = 4736
M_SPACING_Y = 4737
M_SPECIFIC_EDGE = 1
M_SPECIFIC_FEATURES_EDITABLE = 1778
M_SPEED = 8
M_SPHERE = 2931
M_SPHERICAL = 2716
M_SPLIT_CONTEXT_DEFAULT = 8392587
M_SPLIT_CONTEXT_FIXED_SEED = 8392588
M_SPLIT_QUALITY_TYPE = 3531
M_SPPD = 0
M_SPPD_DATA_SAMPLE_COUNT = 1071
M_SPPD_FIRST = 1
M_SPPD_FRAME_HEIGHT = 1078
M_SPPD_OUTPUT_FORMAT = 1074
M_SPPD_PEAK_AVERAGE_MINIMUM_CONTRAST = 1077
M_SPPD_PEAK_AVERAGE_WIDTH = 1072
M_SPPD_PEAK_INTENSITY_RANGE = 1083
M_SPPD_PEAK_MAXIMUM_WIDTH = 1076
M_SPPD_PEAK_MINIMUM_WIDTH = 1075
M_SPPD_PEAK_MODE = 1073
M_SPPD_SECOND = 2
M_SPPD_STATE = 1070
M_SPPD_STRONGEST = 0
M_SPPD_THIRD = 3
M_SQRT = 259
M_SQR_NORM = 4001
M_SQUARE = 32
M_SQUARE_ASPECT_RATIO = 8
M_SQUARE_MAGNITUDE = 4096
M_SQUARE_ROOT = 259
M_SRC = 512
M_SRC_INTER_SYSTEM_COPY = 1044
M_SRC_UPDATE_REGION_OFFSET_X = 10016
M_SRC_UPDATE_REGION_OFFSET_Y = 10017
M_SRGB_LINEAR_TO_LAB = 10486260
M_SRGB_LINEAR_TO_LCH = 10486264
M_SRGB_TO_LAB = 10486261
M_SRGB_TO_LCH = 10486265
M_SR_COMMUTE_BLUR_AND_WARP = 22
M_SR_CONDITIONING_TYPE = 12
M_SR_FIXED_POINT = 15
M_SR_FLOAT_MODE = 14
M_SR_MAX_ITER = 20
M_SR_PSF_RADIUS = 11
M_SR_PSF_TYPE = 10
M_SR_SMOOTHNESS = 13
M_SSE_ENABLED = 268435456
M_STACK_BASED_FUNCTION = 33554432
M_STANDALONE_APPLICATION = 2
M_STANDARD = 2
M_STANDARD_DEVIATION = 268435456
M_STANDARD_FIT = 3066
M_START = 2
M_START_EXPOSURE = 19
M_START_IN_HOST_MEMORY = 64
M_START_IN_VIDEO_MEMORY = 16
M_START_POINT_X = 3658
M_START_POINT_Y = 3659
M_START_POINT_Z = 3660
M_START_POS_X = 2820
M_START_POS_Y = 2821
M_START_RADIUS_X = 2796
M_START_RADIUS_Y = 2797
M_START_REGISTER_ADDRESS = 4026531840
M_START_STOP_PATTERN_GRADE = 36878
M_START_THREAD_HANDLE = 4322
M_START_THREAD_ID = 4323
M_STATE = 8
M_STATE_BEING_CREATED = 1754
M_STATE_GRAPHIC_DRAGGED = 1751
M_STATE_GRAPHIC_HOVERED = 1749
M_STATE_HANDLE_DRAGGED = 1752
M_STATE_HANDLE_HOVERED = 1750
M_STATE_IDLE = 1748
M_STATE_MACHINE_POST_BUFFER_MODIFIED = 16
M_STATE_MACHINE_PRE_BUFFER_MODIFIED = 15
M_STATE_WAITING_FOR_CREATION = 1753
M_STATISTICAL = 3
M_STATISTICS_CONTEXT = 16
M_STATISTICS_CUMULATIVE_CONTEXT = 17
M_STATISTICS_RESULT = 281474976710656
M_STATUS = 32770
M_STATUS_CRC_FAILED = 1
M_STATUS_DETECT_FAILED = 16
M_STATUS_DETECT_OK = 15
M_STATUS_ECC_UNKNOWN = 2
M_STATUS_ENCODING_ERROR = 11
M_STATUS_ENC_UNKNOWN = 3
M_STATUS_FOUND = 32
M_STATUS_GAP_MAX = 23
M_STATUS_GAP_TOLERANCE = 22
M_STATUS_GRADE_FAILED = 8
M_STATUS_GRADE_OK = 7
M_STATUS_INTENSITY_MAX = 51
M_STATUS_INTENSITY_MIN = 50
M_STATUS_MASK = 328
M_STATUS_NOT_FOUND = 6
M_STATUS_NO_RESULT_AVAILABLE = 9
M_STATUS_OFFSET = 27
M_STATUS_READ_OK = 0
M_STATUS_REGISTRATION_ELEMENT = 3925
M_STATUS_SCORE = 24
M_STATUS_SEARCH = 26
M_STATUS_TIMEOUT_END = 10
M_STATUS_TRAIN_FAILED = 14
M_STATUS_TRAIN_OK = 13
M_STATUS_UNINITIALIZED = 2989
M_STATUS_WIDTH_MAX = 29
M_STATUS_WIDTH_MIN = 28
M_STATUS_WRITE_FAILED = 5
M_STATUS_WRITE_OK = 4
M_STAT_ABS = 16384
M_STAT_ALL = 32768
M_STAT_ANGULAR_DATA_COHERENCE = 2512
M_STAT_ANGULAR_DATA_MEAN = 2511
M_STAT_BASE = -9997
M_STAT_CONTEXT_BOUNDING_BOX = 10682371
M_STAT_CONTEXT_CENTROID = 10684324
M_STAT_CONTEXT_DISTANCE_TO_NEAREST_NEIGHBOR = 10685812
M_STAT_CONTEXT_MAX = 8391111
M_STAT_CONTEXT_MAX_ABS = 8391113
M_STAT_CONTEXT_MEAN = 8391117
M_STAT_CONTEXT_MIN = 8391110
M_STAT_CONTEXT_MIN_ABS = 8391112
M_STAT_CONTEXT_NUMBER = 8389617
M_STAT_CONTEXT_NUMBER_OF_POINTS = 10683377
M_STAT_CONTEXT_RMS = 8392170
M_STAT_CONTEXT_STANDARD_DEVIATION = 8391118
M_STAT_CONTEXT_SUM = 8391116
M_STAT_CONTEXT_SUM_ABS = 8391114
M_STAT_CONTEXT_SUM_OF_SQUARES = 8391115
M_STAT_GLCM_CONTRAST = 2174
M_STAT_GLCM_CORRELATION = 2173
M_STAT_GLCM_DISSIMILARITY = 2162
M_STAT_GLCM_ENERGY = 2163
M_STAT_GLCM_ENTROPY = 2164
M_STAT_GLCM_HOMOGENEITY = 2165
M_STAT_LIST = 4096
M_STAT_MAX = 2503
M_STAT_MAX_ABS = 2505
M_STAT_MEAN = 2509
M_STAT_MIN = 2502
M_STAT_MIN_ABS = 2504
M_STAT_MIN_DIST = 52
M_STAT_MULTIPLE_CONTEXT = 6
M_STAT_MULTIPLE_RESULT = 274877906944
M_STAT_NEGATIVE = 8192
M_STAT_NUMBER = 1009
M_STAT_ORIENTATION_DATA_COHERENCE = 2514
M_STAT_ORIENTATION_DATA_MEAN = 2513
M_STAT_POSITIVE = 4096
M_STAT_RESULT = 1307
M_STAT_RMS = 3562
M_STAT_STANDARD_DEVIATION = 2510
M_STAT_SUM = 2508
M_STAT_SUM_ABS = 2506
M_STAT_SUM_OF_SQUARES = 2507
M_STAT_TYPE = 2149
M_STEP = 2845
M_STEP_180 = 2818
M_STEP_90 = 2905
M_STEP_ANY = 201
M_STEP_ANY_WHILE_NEGATIVE = 207
M_STEP_ANY_WHILE_POSITIVE = 204
M_STEP_BACKWARD = 203
M_STEP_BACKWARD_WHILE_NEGATIVE = 209
M_STEP_BACKWARD_WHILE_POSITIVE = 206
M_STEP_FORWARD = 202
M_STEP_FORWARD_NEW_POSITIVE = 211
M_STEP_FORWARD_WHILE_NEGATIVE = 208
M_STEP_FORWARD_WHILE_POSITIVE = 205
M_STEP_LENGTH = 5030
M_STEP_SIZE_X = 2153
M_STEP_SIZE_Y = 2160
M_STEP_X = 3971
M_STEP_Y = 3972
M_STEREO = 0
M_STITCHING = 1
M_STITCHING_RESULT = 1
M_STL = 2198
M_STL_ASCII = 3303
M_STL_BINARY = 3304
M_STOP = 4
M_STOPPED_BY_REQUEST = 2555
M_STOP_CALCULATE = 116
M_STOP_DETECT = 2712
M_STOP_EXPERT = 611
M_STOP_FIND = 115
M_STOP_FOCUS = 2
M_STOP_PREDICT = 2785
M_STOP_READ = 610
M_STOP_TRAIN = 2698
M_STOP_TRAINING = 612
M_STOP_UPDATE = 10039
M_STORAGE_SIZE = 5284
M_STRAIGHTNESS = 6
M_STRAIGHT_WATERSHED = 128
M_STREAMER_BASE = 2
M_STREAMING = 64
M_STREAM_ADAPTATIVE_SCALINGLIST = 5120
M_STREAM_BIT_RATE = 3392
M_STREAM_BIT_RATE_MAX = 3584
M_STREAM_BIT_RATE_MODE = 3328
M_STREAM_CONTROL = 3264
M_STREAM_COPY = 5
M_STREAM_ENCODED_FRAME_NUMBER = 5056
M_STREAM_ENCODING_IMPLEMENTATION = 4864
M_STREAM_ENCODING_MODE = 3840
M_STREAM_FILE_MODE = 1068
M_STREAM_FILE_NAME = 3904
M_STREAM_FRAME_PERIOD = 3776
M_STREAM_FRAME_RATE = 3712
M_STREAM_FRAME_RATE_MODE = 1542
M_STREAM_GROUP_OF_PICTURE_I_SIZE = 4288
M_STREAM_GROUP_OF_PICTURE_P_SIZE = 4224
M_STREAM_GROUP_OF_PICTURE_SIZE = 3648
M_STREAM_GROUP_OF_PICTURE_TYPE = 4160
M_STREAM_INPUT_FRAME_NUMBER = 4992
M_STREAM_LAST = 4351
M_STREAM_LAST_PART2 = 5119
M_STREAM_LEVEL = 4096
M_STREAM_OUTPUT_FORMAT = 16384
M_STREAM_PROFILE = 4032
M_STREAM_QUALITY = 3520
M_STREAM_Q_PARAMETER = 3456
M_STREAM_TOTAL_ENCODING_TIME = 4928
M_STREAM_WRITE = 3968
M_STRENGTH = 55
M_STRENGTH_SCORE = 269484032
M_STRETCHBLT_METHOD = 65536
M_STRETCHBLT_MODE = 65536
M_STRETCHDIB_METHOD = 262144
M_STRETCHDIB_MODE = 262144
M_STRICTLY_ROLE_BITS = 65479
M_STRING = 3
M_STRING_ACCEPTANCE = 24
M_STRING_ADD = 700
M_STRING_ALLOC_SIZE = 18
M_STRING_ALLOC_SIZE_BYTE = 591
M_STRING_ANGLE = 87
M_STRING_ANGLE_DELTA_NEG = 106
M_STRING_ANGLE_DELTA_POS = 107
M_STRING_ANGLE_INPUT_UNITS = 2745
M_STRING_ANGLE_INTERPOLATION_MODE = 88
M_STRING_ANGLE_MODE = 2238
M_STRING_ANGLE_SCORE = 113
M_STRING_ANGLE_SMOOTHNESS = 114
M_STRING_ANGLE_SPEED = 112
M_STRING_ARRAY_SIZE_BIT = 6597069766656
M_STRING_ARRAY_SIZE_MASK = 2147483647
M_STRING_ARRAY_SIZE_SHIFT = 0
M_STRING_ASPECT_RATIO = 505
M_STRING_ASPECT_RATIO_MAX_FACTOR = 507
M_STRING_ASPECT_RATIO_MIN_FACTOR = 506
M_STRING_BOX_BL_X = 920
M_STRING_BOX_BL_Y = 921
M_STRING_BOX_BR_X = 918
M_STRING_BOX_BR_Y = 919
M_STRING_BOX_CENTER_MODE = 2230
M_STRING_BOX_CENTER_X = 2231
M_STRING_BOX_CENTER_Y = 2233
M_STRING_BOX_HEIGHT = 2237
M_STRING_BOX_SIZE_MODE = 2236
M_STRING_BOX_UL_X = 914
M_STRING_BOX_UL_Y = 915
M_STRING_BOX_UR_X = 916
M_STRING_BOX_UR_Y = 917
M_STRING_BOX_WIDTH = 2235
M_STRING_CERTAINTY = 526
M_STRING_CHAR_ANGLE = 794
M_STRING_CHAR_NUMBER = 2277
M_STRING_CHAR_SCORE_MAX = 589
M_STRING_CHAR_SCORE_MIN = 588
M_STRING_DELETE = 701
M_STRING_FOREGROUND_VALUE = 508
M_STRING_FORMAT = 72
M_STRING_HEIGHT = 2298
M_STRING_INDEX_FLAG = 4194304
M_STRING_INDEX_FROM_LABEL = 230
M_STRING_INDEX_VALUE = 2313
M_STRING_LABEL_FLAG = 12582912
M_STRING_LABEL_VALUE = 2288
M_STRING_LENGTH = 5497558138880
M_STRING_LENGTH_MAX = 62
M_STRING_LOCATION_BLOB_ONLY = 2
M_STRING_LOCATION_BLOB_THAN_SEARCH = 4
M_STRING_LOCATION_SEARCH_ONLY = 3
M_STRING_LOCATION_SEARCH_THAN_BLOB = 5
M_STRING_LOC_CHAR_SIZE_X = 1
M_STRING_LOC_CHAR_SIZE_Y = 2
M_STRING_LOC_GOOD_CHAR_SIZE = 16
M_STRING_LOC_GOOD_NB_CHAR = 6
M_STRING_LOC_MAX_CHAR_DISTANCE = 15
M_STRING_LOC_MAX_CHAR_SIZE = 13
M_STRING_LOC_MAX_NB_ITER = 3
M_STRING_LOC_MIN_CHAR_SIZE = 12
M_STRING_LOC_MIN_CHAR_SPACE = 64
M_STRING_LOC_NB_MODELS = 57
M_STRING_LOC_STOP_ITER = 5
M_STRING_MASK = 4194304
M_STRING_MAX_SLOPE = 17
M_STRING_MODEL_INDEX = 585
M_STRING_MODEL_LABEL = 2278
M_STRING_MODEL_USER_LABEL = 228
M_STRING_NUMBER = 74
M_STRING_NUMBER_FOUND = 86
M_STRING_PITCH = 3696
M_STRING_PITCH_MODE = 3697
M_STRING_POSITION_X = 586
M_STRING_POSITION_Y = 587
M_STRING_RANK = 2334
M_STRING_READ_BAD_ADD_CHAR = 11
M_STRING_READ_BAD_SIZE_X = 7
M_STRING_READ_BAD_SIZE_Y = 63
M_STRING_READ_GOOD_SIZE_X = 9
M_STRING_READ_GOOD_SIZE_Y = 10
M_STRING_READ_SIZE_X = 18
M_STRING_READ_SIZE_Y = 19
M_STRING_SCALE = 502
M_STRING_SCALE_MAX_FACTOR = 504
M_STRING_SCALE_MIN_FACTOR = 503
M_STRING_SCORE = 5120
M_STRING_SEPARATOR = 910
M_STRING_SIZE = 5497558138880
M_STRING_SIZE_MAX = 62
M_STRING_SIZE_MIN = 500
M_STRING_SIZE_MIN_MAX = 2388
M_STRING_TARGET_ACCEPTANCE = 527
M_STRING_TARGET_CERTAINTY = 528
M_STRING_TARGET_SCORE = 900
M_STRING_TYPE = 515
M_STRING_USER_LABEL = 228
M_STRING_VALIDATION = 48
M_STRING_VALIDATION_HANDLER_PTR = 48
M_STRING_VALIDATION_HANDLER_USER_PTR = 49
M_STRING_VALID_FLAG = 1
M_STRING_WIDTH = 2297
M_STRIPE = 3
M_STRIPE_WIDTH = 2097152
M_STRIPE_WIDTH_SCORE = 276824064
M_STRUCT_ELEMENT = 134217728
M_STR_CONTEXT = 570425345
M_STR_OBJECT = 570425344
M_STR_RESULT = 570425346
M_ST_ERROR_TITLE = 512
M_SUB = 1
M_SUBFEATURE_COUNT = 72057594037993472
M_SUBFEATURE_INDEX_MASK = 65535
M_SUBFEATURE_NAME = 72057594038059008
M_SUBFEATURE_TYPE = 72057594038190080
M_SUBPIXEL_MODE = 1715
M_SUBSAMPLE = 5091
M_SUBSAMPLE_CONTEXT = 3639
M_SUBSAMPLE_CONTEXT_ID = 3641
M_SUBSAMPLE_DECIMATE = 3046
M_SUBSAMPLE_GRID = 3049
M_SUBSAMPLE_MODE = 3630
M_SUBSAMPLE_NORMAL = 3109
M_SUBSAMPLE_NORMAL_MODE = 3637
M_SUBSAMPLE_RANDOM = 3047
M_SUBSAMPLE_X = 5089
M_SUBSAMPLE_Y = 5090
M_SUBSYSTEM_ID = 2299
M_SUB_ABS = 17
M_SUB_CONST = 32769
M_SUB_CONST_ABS = 32785
M_SUB_EDGES_MARKER_INDEX = 223
M_SUB_EDGES_POSITION = 220
M_SUB_EDGES_WEIGHT = 222
M_SUB_FUNCTION_ID = 8203
M_SUB_INDEX_1 = 2488
M_SUB_INDEX_2 = 2489
M_SUB_OBJECT_LIST_MODIFIED = 2049
M_SUB_REGIONS_CHORD_ANGLE = 226
M_SUB_REGIONS_NUMBER = 218
M_SUB_REGIONS_NUMBER_USED = 185344
M_SUB_REGIONS_OFFSET = 224
M_SUB_REGIONS_SIZE = 225
M_SUB_REGION_TAG = 536870912
M_SUB_SYSTEM_ID = 4567
M_SUB_TYPE = 20736
M_SUCCESS = 0
M_SUGGESTED_VALUE = -42
M_SUM = 16384
M_SUM_ABS = 8
M_SUM_I = 66816
M_SUM_II = 67328
M_SUM_IM = 67840
M_SUM_M = 69888
M_SUM_MM = 70400
M_SUM_OF_SQUARES = 1024
M_SUM_PIXEL = 29
M_SUM_PIXEL_SQUARED = 46
M_SUPERSIGHT = 16384
M_SUPERSIGHT_ARBOR_FINGERPRINT = 20880
M_SUPERSIGHT_DESC = 15136
M_SUPERSIGHT_DRIVER_VERSION = 15118
M_SUPERSIGHT_FINGERPRINT = 21104
M_SUPER_RESOLUTION = 1
M_SUPPORTED = 140737488355328
M_SUPPORTED_CODE_TYPES = 2699
M_SUPPORTED_CODE_TYPES_1D = 2703
M_SUPPORTED_CODE_TYPES_2D = 2707
M_SUPPORTED_CODE_TYPES_DETECT = 2928
M_SUPPORTED_CODE_TYPES_NAMES = 2700
M_SUPPORTED_CODE_TYPES_NAMES_1D = 2704
M_SUPPORTED_CODE_TYPES_NAMES_2D = 2708
M_SUPPORTED_CODE_TYPES_NAMES_DETECT = 2929
M_SUPPORTED_CODE_TYPES_NAMES_POSTAL = 2774
M_SUPPORTED_CODE_TYPES_POSTAL = 2773
M_SUPPORTED_DISPLAY_TYPE_STRING = 4553
M_SUPPORTED_INTERFACE = 2159
M_SUPPORT_DEVICE_NAME = 2184
M_SUPPORT_END_NO = 4439
M_SUPPORT_END_YES = 4500
M_SUPPORT_ERROR_REMOTE_CURRENT = 15962
M_SUPPORT_INTERSYSTEM_CALL = 16525
M_SUPPORT_MISSING_GROUND_TRUTH = 3950
M_SUPPORT_MIXED_CLUSTER = 16526
M_SUPPORT_NEW_CONTROL_FEATURE = 4390
M_SUPPORT_START_NO = 4374
M_SUPPORT_START_YES = 4440
M_SUPPORT_SYSTEM_NOTIFICATION = 2183
M_SURE_SHRINK = 9437443
M_SURFACE = 1021
M_SURFACE_LOST = 134217742
M_SURFACE_SAMPLE_CONTEXT = 3799
M_SYMBOL_ANGLE_INPUT_UNITS = 1775
M_SYMBOL_BASED_GRADE = 36877
M_SYMBOL_CONTRAST = 40960
M_SYMBOL_CONTRAST_GRADE = 36865
M_SYMBOL_CONTRAST_SNR = 41039
M_SYMBOL_DIMENSION = 1214
M_SYMBOL_DIMENSION_INPUT_UNITS = 1630
M_SYMBOL_TYPE = 1629
M_SYMLET_1 = 14
M_SYMLET_2 = 15
M_SYMLET_3 = 16
M_SYMLET_4 = 17
M_SYMLET_5 = 18
M_SYMLET_6 = 19
M_SYMLET_7 = 20
M_SYMLET_8 = 21
M_SYMMETRIC = 2734
M_SYNC = 8192
M_SYNCHRONIZE_CHANNEL = 4326
M_SYNCHRONIZE_GRAB_WITH_DISPLAY_REFRESH = 4376
M_SYNCHRONIZE_ON_STARTED = 4218
M_SYNCHRONIZE_OUTPUT = 5453
M_SYNCHRONIZE_OUTPUT_VALUE = 5454
M_SYNCHRONOUS = 1
M_SYNCHRONOUS_FUNCTION = 524288
M_SYNC_TYPE = 1031
M_SYSCLK = 26
M_SYSTEM = 8388608
M_SYSTEMS_ERROR_END = 19999
M_SYSTEMS_ERROR_START = 200
M_SYSTEM_1394 = MIL_TEXT("M_SYSTEM_1394")
M_SYSTEM_1394_TYPE = 22
M_SYSTEM_ALLOCATED = 1
M_SYSTEM_AMD_3DNOW_EXT_TYPE = 29
M_SYSTEM_AMD_3DNOW_TYPE = 27
M_SYSTEM_AMD_MMX_EXT_TYPE = 28
M_SYSTEM_ASSOCIATED_TO_DX_OBJECT = 15302
M_SYSTEM_AVX2_TYPE = 74
M_SYSTEM_AVX512_TYPE = 77
M_SYSTEM_AVX_TYPE = 73
M_SYSTEM_BITBLT_TYPE = 48
M_SYSTEM_CLARITY_UHD = MIL_TEXT("M_SYSTEM_CLARITY_UHD")
M_SYSTEM_CLARITY_UHD_TYPE = 66
M_SYSTEM_CODE = 107
M_SYSTEM_CONCORD_1394_TYPE = 22
M_SYSTEM_CONCORD_POE = MIL_TEXT("M_SYSTEM_CONCORD_POE")
M_SYSTEM_CONCORD_POE_TYPE = 76
M_SYSTEM_CRONOSPLUS = MIL_TEXT("M_SYSTEM_CRONOSPLUS")
M_SYSTEM_CRONOSPLUS_TYPE = 38
M_SYSTEM_DEFAULT = MIL_TEXT("M_DEFAULT")
M_SYSTEM_DESCRIPTOR = 7701
M_SYSTEM_DIBTODEV_TYPE = 50
M_SYSTEM_DIB_TYPE_END = 56
M_SYSTEM_DIB_TYPE_START = 47
M_SYSTEM_DIRECTX_TYPE = 45
M_SYSTEM_DISTRIBUTED_FLAG = 1073741824
M_SYSTEM_DRAWDIB_TYPE = 47
M_SYSTEM_FONT = 12
M_SYSTEM_FREE_ERROR = 27
M_SYSTEM_GENTL = MIL_TEXT("M_SYSTEM_GENTL")
M_SYSTEM_GENTL_TYPE = 65
M_SYSTEM_GIGE_VISION = MIL_TEXT("M_SYSTEM_GIGE_VISION")
M_SYSTEM_GIGE_VISION_TYPE = 60
M_SYSTEM_GPU = MIL_TEXT("M_SYSTEM_GPU")
M_SYSTEM_GPU_TYPE = 58
M_SYSTEM_HDDVR = MIL_TEXT("M_SYSTEM_HDDVR")
M_SYSTEM_HDDVR_TYPE = 71
M_SYSTEM_HOST = MIL_TEXT("M_SYSTEM_HOST")
M_SYSTEM_HOST_TYPE = 1000
M_SYSTEM_ID = 131072
M_SYSTEM_INDIO = MIL_TEXT("M_SYSTEM_INDIO")
M_SYSTEM_INDIO_TYPE = 75
M_SYSTEM_INFORMATION_FLAGS = 1073741824
M_SYSTEM_IRIS = MIL_TEXT("M_SYSTEM_IRIS")
M_SYSTEM_IRIS_GT = MIL_TEXT("M_SYSTEM_IRIS_GT")
M_SYSTEM_IRIS_GTR = MIL_TEXT("M_SYSTEM_IRIS_GTR")
M_SYSTEM_IRIS_GTR_TYPE = 40
M_SYSTEM_IRIS_GT_TYPE = 67
M_SYSTEM_IRIS_TYPE = 37
M_SYSTEM_LOCATION = 1048
M_SYSTEM_MATROXCOMPRESS = MIL_TEXT("M_SYSTEM_MATROXCOMPRESS")
M_SYSTEM_MATROXCOMPRESS_TYPE = 72
M_SYSTEM_MMX_TYPE = 23
M_SYSTEM_MORPHIS = MIL_TEXT("M_SYSTEM_MORPHIS")
M_SYSTEM_MORPHISQXT = MIL_TEXT("M_SYSTEM_MORPHISQXT")
M_SYSTEM_MORPHISQXT_TYPE = 59
M_SYSTEM_MORPHIS_TYPE = 39
M_SYSTEM_MP_TYPE = 64
M_SYSTEM_MTX0_TYPE = 46
M_SYSTEM_MTXAUXILIARY = MIL_TEXT("M_SYSTEM_MTXAUXILIARY")
M_SYSTEM_NAME = 7702
M_SYSTEM_NAME_MAX_SIZE = 64
M_SYSTEM_NEXIS = MIL_TEXT("M_SYSTEM_NEXIS")
M_SYSTEM_NEXIS2 = MIL_TEXT("M_SYSTEM_NEXIS2")
M_SYSTEM_NEXIS2_TYPE = 69
M_SYSTEM_NEXIS3 = MIL_TEXT("M_SYSTEM_NEXIS3")
M_SYSTEM_NEXIS3_TYPE = 41
M_SYSTEM_NEXIS_TYPE = 57
M_SYSTEM_NUM = 2169
M_SYSTEM_NUM_ALLOCATED = 2360
M_SYSTEM_OFFSET = 16531
M_SYSTEM_ORION_HD = MIL_TEXT("M_SYSTEM_ORION_HD")
M_SYSTEM_ORION_HD_TYPE = 68
M_SYSTEM_ORION_UHD = MIL_TEXT("M_SYSTEM_ORION_UHD")
M_SYSTEM_ORION_UHD_TYPE = 66
M_SYSTEM_PRINT_NAME = 7709
M_SYSTEM_RADIENT = MIL_TEXT("M_SYSTEM_RADIENT")
M_SYSTEM_RADIENTCLHS = MIL_TEXT("M_SYSTEM_RADIENTCLHS")
M_SYSTEM_RADIENTCLHS_TYPE = 15
M_SYSTEM_RADIENTCXP = MIL_TEXT("M_SYSTEM_RADIENTCXP")
M_SYSTEM_RADIENTCXP_TYPE = 14
M_SYSTEM_RADIENTEVCL = MIL_TEXT("M_SYSTEM_RADIENTEVCL")
M_SYSTEM_RADIENTEVCL_TYPE = 17
M_SYSTEM_RADIENTPRO = MIL_TEXT("M_SYSTEM_RADIENTPRO")
M_SYSTEM_RADIENTPRO_TYPE = 16
M_SYSTEM_RADIENT_TYPE = 13
M_SYSTEM_RAPIXOCL = MIL_TEXT("M_SYSTEM_RAPIXOCL")
M_SYSTEM_RAPIXOCL_TYPE = 19
M_SYSTEM_RAPIXOCXP = MIL_TEXT("M_SYSTEM_RAPIXOCXP")
M_SYSTEM_RAPIXOCXP_TYPE = 18
M_SYSTEM_RESPONSE_CALIBRATION = 1635
M_SYSTEM_RESPONSE_TARGET = 1638
M_SYSTEM_SOLIOS = MIL_TEXT("M_SYSTEM_SOLIOS")
M_SYSTEM_SOLIOS_TYPE = 42
M_SYSTEM_SSE2_TYPE = 26
M_SYSTEM_SSE3_TYPE = 43
M_SYSTEM_SSE4_TYPE = 62
M_SYSTEM_SSE_TYPE = 24
M_SYSTEM_STRETCHBLT_TYPE = 49
M_SYSTEM_STRETCHDIB_TYPE = 51
M_SYSTEM_STRING_CODE = 10
M_SYSTEM_THREAD = 256
M_SYSTEM_TIME_STAMP_VALUE = 7332
M_SYSTEM_TYPE = 2000
M_SYSTEM_TYPE_NONE = 0
M_SYSTEM_TYPE_STRING = 7705
M_SYSTEM_USB3_VISION = MIL_TEXT("M_SYSTEM_USB3_VISION")
M_SYSTEM_USB3_VISION_TYPE = 63
M_SYSTEM_VGA = MIL_TEXT("M_SYSTEM_HOST")
M_SYSTEM_VIO = MIL_TEXT("M_SYSTEM_VIO")
M_SYSTEM_VIO_TYPE = 44
M_SYS_ALLOC_INIT_FLAGS = 536875007
M_SYS_APP_INQUIRE_STRING_2_END = 22399
M_SYS_APP_INQUIRE_STRING_2_START = 22000
M_SYS_APP_INQUIRE_STRING_END = 16999
M_SYS_APP_INQUIRE_STRING_START = 16800
M_SYS_AUX_END = 7499
M_SYS_AUX_START = 7400
M_SYS_BUFFER_HANDLER_END = 4600
M_SYS_BUFFER_HANDLER_START = 4597
M_SYS_CONFIG_ERROR = 122
M_SYS_CONTROL_SUPPORT_MULTI_TYPE = 4395
M_SYS_CTRL_INQ_ERROR = 79
M_SYS_DATA_LATCH_BUFFER_TRIGGER_SOURCE = 8832
M_SYS_DATA_LATCH_CALLBACK = 8864
M_SYS_DATA_LATCH_CLOCK_FREQUENCY = 8701
M_SYS_DATA_LATCH_FLUSH_TRIGGER_SOURCE = 8896
M_SYS_DATA_LATCH_INDEX_START = 8704
M_SYS_DATA_LATCH_MAX_INDEX = 32
M_SYS_DATA_LATCH_MODE = 8800
M_SYS_DATA_LATCH_PARSING_MODE = 8700
M_SYS_DATA_LATCH_SIZE_BYTE = 8992
M_SYS_DATA_LATCH_STATE = 8704
M_SYS_DATA_LATCH_TRIGGER_ACTIVATION = 8928
M_SYS_DATA_LATCH_TRIGGER_SOURCE = 8768
M_SYS_DATA_LATCH_TYPE = 8736
M_SYS_DATA_LATCH_VALUE = 9056
M_SYS_DATA_LATCH_VALUE_ALL = 9024
M_SYS_DATA_LATCH_VALUE_COUNT = 8960
M_SYS_DISPLAY_END = 4600
M_SYS_DISPLAY_RANGE2_END = 8699
M_SYS_DISPLAY_RANGE2_START = 8500
M_SYS_DISPLAY_START = 4501
M_SYS_INQUIRE_CPU_STRING_END = 10371
M_SYS_INQUIRE_CPU_STRING_START = 10312
M_SYS_INQUIRE_MIL_ID_END = 1199
M_SYS_INQUIRE_MIL_ID_START = 1100
M_SYS_INQUIRE_SIZEOF_DOUBLE_END = 7399
M_SYS_INQUIRE_SIZEOF_DOUBLE_START = 7300
M_SYS_INQUIRE_SIZEOF_INT64_END = 6799
M_SYS_INQUIRE_SIZEOF_INT64_START = 6700
M_SYS_INQUIRE_STRING_END = 7799
M_SYS_INQUIRE_STRING_END_1 = 36000
M_SYS_INQUIRE_STRING_START = 7700
M_SYS_INQUIRE_STRING_START_1 = 33000
M_SYS_INQUIRE_UNKNOWN_SIZEOF_END = 7599
M_SYS_INQUIRE_UNKNOWN_SIZEOF_START = 7500
M_SYS_IO_CONTEXT = 17592186044416
M_SYS_IO_INQUIRE_MIL_ID_END = 1199
M_SYS_IO_INQUIRE_MIL_ID_START = 1100
M_SYS_IO_INQUIRE_SIZEOF_DOUBLE_END = 7399
M_SYS_IO_INQUIRE_SIZEOF_DOUBLE_START = 7300
M_SYS_IO_INQUIRE_SIZEOF_INT64_END = 6799
M_SYS_IO_INQUIRE_SIZEOF_INT64_END2 = 274432
M_SYS_IO_INQUIRE_SIZEOF_INT64_START = 6700
M_SYS_IO_INQUIRE_SIZEOF_INT64_START2 = 262144
M_SYS_IO_INQUIRE_STRING_END = 7799
M_SYS_IO_INQUIRE_STRING_START = 7700
M_SYS_IO_INQUIRE_UNKNOWN_SIZEOF_END = 7599
M_SYS_IO_INQUIRE_UNKNOWN_SIZEOF_START = 7500
M_SYS_USE_WINDOWED_CLASS = 2295
M_TABLES_ONLY = 5
M_TABLES_PRELOAD = 6
M_TAN = 4
M_TAP1 = 1073741824
M_TAP2 = 536870912
M_TARGET = 524288
M_TARGET_BUFFER_ATTRIBUTE = 6751
M_TARGET_BUFFER_OBJECT = 6750
M_TARGET_BUFFER_UPDATE = 5188
M_TARGET_CACHING = 39
M_TARGET_CHAR_POSITION_VARIATION_X = 91
M_TARGET_CHAR_POSITION_VARIATION_Y = 92
M_TARGET_CHAR_SIZE_X = 27
M_TARGET_CHAR_SIZE_X_MAX = 100
M_TARGET_CHAR_SIZE_X_MIN = 99
M_TARGET_CHAR_SIZE_Y = 28
M_TARGET_CHAR_SIZE_Y_MAX = 102
M_TARGET_CHAR_SIZE_Y_MIN = 101
M_TARGET_CHAR_SPACING = 29
M_TARGET_COVERAGE = 5376
M_TARGET_ID = 218
M_TARGET_IMAGE_SIZE_X = 3358
M_TARGET_IMAGE_SIZE_Y = 3359
M_TARGET_SIZE = 5074
M_TARGET_STRING_INDEX = 67108864
M_TARGET_TEMPERATURE = 5176
M_TCH = 262144
M_TEMPERATURE = 5136
M_TEMPERATURE_CPU = 7312
M_TEMPERATURE_FPGA = 7301
M_TEMPERATURE_FPGA_MAX_MEASURED = 7302
M_TEMPERATURE_FPGA_PROCESSING = 7309
M_TEMPERATURE_FPGA_PROCESSING_MAX_MEASURED = 7310
M_TEMPERATURE_IMAGE_SENSOR = 7320
M_TEMPERATURE_SENSOR = 6647
M_TEMPLATE_CIRCLE_CENTER_X = 302
M_TEMPLATE_CIRCLE_CENTER_Y = 303
M_TEMPLATE_CIRCLE_RADIUS = 304
M_TEMPLATE_INDEX_TAG = 33554432
M_TEMPLATE_INPUT_UNITS = 79
M_TEMPLATE_LABEL_TAG = 16777216
M_TEMPLATE_REFERENCE_ID = 50
M_TEMPLATE_REFERENCE_SIZE_BAND = 57
M_TEMPLATE_REFERENCE_SIZE_X = 55
M_TEMPLATE_REFERENCE_SIZE_Y = 56
M_TEMPLATE_REFERENCE_TYPE = 162
M_TEMPLATE_SEGMENT_END_X = 307
M_TEMPLATE_SEGMENT_END_Y = 308
M_TEMPLATE_SEGMENT_START_X = 305
M_TEMPLATE_SEGMENT_START_Y = 306
M_TEMP_DIR = MIL_TEXT("///MILTEMPDIRDIR///")
M_TEMP_LICENSE_DAYS_LEFT = 15057
M_TEST_DESKTOP_RESOLUTION = 9251
M_TEST_FRAME_COUNTER = 2104
M_TEST_FRAME_COUNTER_DRAW = 2103
M_TEST_IMAGE = 2102
M_TEST_OPENGL = 4
M_TEST_UPDATE_IF_ASYNCHRONOUS = 16
M_TEXT = 16
M_TEXTURE_IMAGE = 2700
M_TEXT_ALIGN_HORIZONTAL = 58
M_TEXT_ALIGN_VERTICAL = 71
M_TEXT_ALLOC_SIZE_BYTE = 18
M_TEXT_BORDER = 1785
M_TEXT_DIRECTION = 16777313
M_TEXT_LENGTH = 17
M_TEXT_SCORE = 15
M_TEXT_SHADING = 4747
M_TEXT_SIZE = 17
M_TEXT_STRING_SEPARATOR = 109
M_THICK = 4
M_THICKEN_CHAR = 84
M_THICKNESS = 3
M_THIN = 3
M_THREAD = 256
M_THREAD_ALL = 33554432
M_THREAD_ALLOC = 1800
M_THREAD_CANCEL = 2435
M_THREAD_COMMANDS_ABORT = 1810
M_THREAD_CONTEXT = 1024
M_THREAD_CONTEXT_PTR = 2068
M_THREAD_CONTROL = 1803
M_THREAD_CREATE = 2048
M_THREAD_CREATE_ON_ID = 8192
M_THREAD_CURRENT = 16777216
M_THREAD_DETACH = 128
M_THREAD_END_WAIT = 1073741824
M_THREAD_END_WAIT_ALL = 1140850688
M_THREAD_FREE = 1801
M_THREAD_HALT = 2436
M_THREAD_IO_MODE = 1805
M_THREAD_MODE = 1804
M_THREAD_PRIORITY = 1019
M_THREAD_SELECT = 1708
M_THREAD_TIME_SLICE = 1811
M_THREAD_WAIT = 16777216
M_THREE_POINTS = 3390
M_THRESHOLD = 82
M_THRESHOLDS = 3003
M_THRESHOLDS_ERROR = 121
M_THRESHOLD_HIGH = 3002
M_THRESHOLD_LOW = 3001
M_THRESHOLD_MODE = 33
M_THRESHOLD_TYPE = 3000
M_THRESHOLD_VALUE = 953
M_THRESHOLD_VALUE_HIGH = 3002
M_THRESHOLD_VALUE_LOW = 3001
M_THROW_EXCEPTION = 11
M_THR_CONT_TYPE_MASK = 16777215
M_TIE = 2
M_TIE_EPSILON = 205
M_TIE_POINT_LIST = 4
M_TIFF = 4096
M_TIFF_CCITT_3 = 2
M_TIFF_CCITT_3_T4_ENCODING = 3
M_TIFF_CCITT_4_T6_ENCODING = 4
M_TIFF_COMPRESS = 16
M_TIFF_COMPRESS_2 = 32
M_TIFF_ERROR = 20
M_TIFF_ERROR_2 = 33
M_TIFF_ERROR_3 = 64
M_TIFF_EXTENSIONS = MIL_TEXT("*.tif;*.tiff")
M_TIFF_LEGACY = 4
M_TIFF_NO_COMPRESSION = 1
M_TILES_AND_SPACING = 3933
M_TILE_OFFSET_X = 8217
M_TILE_OFFSET_Y = 8218
M_TILE_SIZE_X = 8219
M_TILE_SIZE_Y = 8220
M_TILT = 5152
M_TIMED = 0
M_TIMEOUT = 2077
M_TIMEOUT_END = 10
M_TIMEOUT_MASK = 16777215
M_TIMEOUT_REACHED = 2554
M_TIMER0 = 0
M_TIMER1 = 1
M_TIMER10 = 10
M_TIMER11 = 11
M_TIMER12 = 12
M_TIMER13 = 13
M_TIMER14 = 14
M_TIMER15 = 15
M_TIMER16 = 16
M_TIMER2 = 2
M_TIMER3 = 3
M_TIMER4 = 4
M_TIMER5 = 5
M_TIMER6 = 6
M_TIMER60 = 60
M_TIMER7 = 7
M_TIMER8 = 8
M_TIMER9 = 9
M_TIMER99 = 99
M_TIMER_ACTIVE = 2048
M_TIMER_ARM = 132272
M_TIMER_ARM_ACTIVATION = 132472
M_TIMER_ARM_SOFTWARE = 132572
M_TIMER_ARM_SOURCE = 132372
M_TIMER_CLOCK_ACTIVATION = 132672
M_TIMER_CLOCK_FREQUENCY = 133372
M_TIMER_CLOCK_SOURCE = 131672
M_TIMER_COMPENSATION = 327680
M_TIMER_DEFAULT = 99
M_TIMER_DELAY = 133272
M_TIMER_DELAY2 = 133772
M_TIMER_DELAY_CLOCK_ACTIVATION = 131372
M_TIMER_DELAY_CLOCK_FREQUENCY = 133872
M_TIMER_DELAY_CLOCK_SOURCE = 131472
M_TIMER_DURATION = 133172
M_TIMER_DURATION2 = 133672
M_TIMER_DURATION_MAX = 133072
M_TIMER_END = 1024
M_TIMER_ERROR = 43
M_TIMER_FLAG_MASK = 16648
M_TIMER_INDEX = 8650752
M_TIMER_INTERRUPT = 4308
M_TIMER_IO = 2
M_TIMER_LOCK_TO_CPU = 458752
M_TIMER_MODE_MASK = 983040
M_TIMER_NUM = 2008
M_TIMER_OUTPUT_INVERTER = 131272
M_TIMER_READ = 196608
M_TIMER_RESET = 131072
M_TIMER_RESET_SOURCE = 132972
M_TIMER_RESOLUTION = 65536
M_TIMER_SET_INTERRUPT = 4310
M_TIMER_START = 768
M_TIMER_STATE = 131072
M_TIMER_STROBE = 60
M_TIMER_TIMEOUT = 133472
M_TIMER_TRIGGER_ACTIVATION = 131572
M_TIMER_TRIGGER_MISSED = 131872
M_TIMER_TRIGGER_MISSED_STATUS = 131972
M_TIMER_TRIGGER_OVERLAP = 132872
M_TIMER_TRIGGER_RATE_DIVIDER = 132072
M_TIMER_TRIGGER_SOFTWARE = 132172
M_TIMER_TRIGGER_SOURCE = 131172
M_TIMER_UNLOCK_FROM_CPU = 524288
M_TIMER_USAGE = 131772
M_TIMER_USE_CPU = 589824
M_TIMER_USE_OS = 655360
M_TIMER_VALUE = 133572
M_TIMER_WAIT = 262144
M_TIMER_WAIT_EXACT = 393216
M_TIME_CRITICAL = 15
M_TIME_STAMP = 64
M_TITLE = 7702
M_TITLE_SIZE = 5497558146582
M_TL_ERROR_CORRECTED_COUNT = 3120
M_TL_ERROR_COUNT = 3216
M_TL_ERROR_CTRL_CRC_COUNT = 3168
M_TL_ERROR_DATA_CRC_COUNT = 3152
M_TL_ERROR_DETECTION_MODE = 3100
M_TL_ERROR_ENCODING_COUNT = 3200
M_TL_ERROR_EVENT_CRC_COUNT = 3184
M_TL_ERROR_LOCK_LOSS_COUNT = 3104
M_TL_ERROR_UNCORRECTED_COUNT = 3136
M_TL_EVENT = 1040
M_TL_EVENT0 = 1040
M_TL_IO = 512
M_TL_IO0 = 512
M_TL_IO1 = 513
M_TL_IO10 = 522
M_TL_IO11 = 523
M_TL_IO12 = 524
M_TL_IO13 = 525
M_TL_IO14 = 526
M_TL_IO15 = 527
M_TL_IO2 = 514
M_TL_IO3 = 515
M_TL_IO4 = 516
M_TL_IO5 = 517
M_TL_IO6 = 518
M_TL_IO7 = 519
M_TL_IO8 = 520
M_TL_IO9 = 521
M_TL_IO_COUNT = 4465
M_TL_IO_COUNT_IN = 4466
M_TL_IO_COUNT_OUT = 4467
M_TL_TRIGGER = 768
M_TL_TRIGGER0 = 769
M_TL_TRIGGER1 = 770
M_TL_TRIGGER2 = 771
M_TL_TRIGGER3 = 772
M_TL_TRIGGER_ACTIVATION = 581632
M_TL_TRIGGER_COUNT = 4456
M_TL_TRIGGER_COUNT_IN = 4457
M_TL_TRIGGER_COUNT_OUT = 4458
M_TOE = 4096
M_TOGGLE = 1895
M_TOLERANCE_INDEX_TAG = 67108864
M_TOLERANCE_LABEL_TAG = 536870912
M_TOLERANCE_TYPE = 902
M_TOLERANCE_VALUE = 0
M_TOLERATE_INVALID_FPGA = 2048
M_TONE_MAPPING = 12
M_TONE_MAPPING_COEFFICIENT = 2801
M_TONE_MAPPING_HIGH_THRESHOLD = 2803
M_TONE_MAPPING_LOW_THRESHOLD = 2802
M_TONE_MAPPING_MODE = 2800
M_TOOL_COORDINATE_SYSTEM = 1
M_TOOL_POSITION_X = 156
M_TOOL_POSITION_Y = 157
M_TOOL_POSITION_Z = 158
M_TOO_MANY_OUTLIERS = 10
M_TOP = 1024
M_TOP_BLACK = 524288
M_TOP_BOTTOM = 4096
M_TOP_HAT = 9
M_TOP_LEFT_X = 1004
M_TOP_LEFT_Y = 1005
M_TOP_RIGHT_X = 1014
M_TOP_RIGHT_Y = 1015
M_TOP_TILTED = 4174
M_TOP_VIEW = 4168
M_TOP_WHITE = 262144
M_TORTUOSITY = 76
M_TOTAL = 3627
M_TOTAL_DISPLACEMENT_Y = 1896
M_TOTAL_NUMBER = 1010
M_TOTAL_NUMBER_OF_CHAINED_PIXELS = 2481
M_TOTAL_NUMBER_OF_CONVEX_HULL_POINTS = 2480
M_TOTAL_NUMBER_OF_FERETS = 2534
M_TOTAL_NUMBER_OF_RUNS = 117
M_TOTAL_STRING_SIZE = 32783
M_TOUCHING_CHAR = 105
M_TOWARDS_DIRECTION = 3434
M_TOWARDS_POSITION = 3432
M_TO_IDEMPOTENCE = -1
M_TO_REFERENCE = 3588
M_TO_SKELETON = -1
M_TRACE = 16640
M_TRACER_BIN_FILE = 2
M_TRACER_CONSOLE = 8
M_TRACER_MEM = 64
M_TRACER_NAME = 16849
M_TRACER_TXT_FILE = 4
M_TRACE_ACTIVE = 16641
M_TRACE_ASCII_INFORMATION = 15397
M_TRACE_END = 2
M_TRACE_END_HANDLER_PTR = 15016
M_TRACE_END_HANDLER_USER_PTR = 15017
M_TRACE_HOOKS = 15002
M_TRACE_INFORMATION = 15381
M_TRACE_LEVEL = 34
M_TRACE_LOG_DISABLE = 4194304
M_TRACE_MARKER = 0
M_TRACE_SAVE_TO_FILE = 16850
M_TRACE_SECTION_END = 2305843009213693952
M_TRACE_SECTION_START = 1152921504606846976
M_TRACE_SET_TAG_INFORMATION = -9223372036854775808
M_TRACE_START = 1
M_TRACE_START_HANDLER_PTR = 15014
M_TRACE_START_HANDLER_USER_PTR = 15015
M_TRACE_STRING_LENGTH = 2048
M_TRAIN = 536870912
M_TRAINABLE_COMPLETE = 3949
M_TRAINABLE_FINE_TUNING = 3975
M_TRAINABLE_TRANSFER_LEARNING = 3974
M_TRAINED = 12
M_TRAINED_BOX_HEIGHT = 49
M_TRAINED_BOX_SPACING = 25
M_TRAINED_BOX_WIDTH = 48
M_TRAINED_CLASSIFIER_CNN = 3640
M_TRAINED_CNN_PARAMETERS_UPDATED = 3775
M_TRAINED_CONTROL_TYPES = 3037
M_TRAINED_FAIL = 9
M_TRAINED_INDEX = 25
M_TRAINED_INDIVIDUAL_WIDTH_NOMINAL = 207
M_TRAINED_NUMBER_OF_MODEL_CONTROL_TYPES = 3312
M_TRAINED_PASS = 11
M_TRAINED_POSITION_X = 210
M_TRAINED_POSITION_Y = 211
M_TRAINED_SIZE = 209
M_TRAINED_TREE_ENSEMBLE = 3695
M_TRAINED_WIDTH_NOMINAL = 92
M_TRAINING_BOX_HEIGHT = 3
M_TRAINING_BOX_INPUT_UNITS = 78
M_TRAINING_BOX_SPACING = 40
M_TRAINING_BOX_WIDTH = 17
M_TRAINING_END = 2
M_TRAINING_ERROR = 2
M_TRAINING_IMAGE_SIZE_X = 15
M_TRAINING_IMAGE_SIZE_Y = 16
M_TRAINING_IMAGE_TYPE = 17
M_TRAINING_ITERATION = 3
M_TRAINING_NOT_PERFORMED = 3424
M_TRAINING_PATH = 1462
M_TRAINING_SCORE = 2570
M_TRAINING_START = 1
M_TRAINING_WIDTH_NOMINAL = 60
M_TRAINING_WIDTH_SCALE_MAX = 62
M_TRAINING_WIDTH_SCALE_MIN = 61
M_TRAIN_CNN = 4213
M_TRAIN_CNN_RESULT = 3755
M_TRAIN_CONTEXT_ID = 3692
M_TRAIN_DATASET_ACCURACY = 3556
M_TRAIN_DATASET_ACCURACY_AFTER_EACH_TREE = 3807
M_TRAIN_DATASET_CONFUSION_MATRIX = 3608
M_TRAIN_DATASET_CONFUSION_MATRIX_SIZE_X = 3609
M_TRAIN_DATASET_CONFUSION_MATRIX_SIZE_Y = 3982
M_TRAIN_DATASET_EPOCH_ACCURACY = 3727
M_TRAIN_DATASET_EPOCH_ERROR_ENTRIES = 3724
M_TRAIN_DATASET_EPOCH_ERROR_RATE = 3748
M_TRAIN_DATASET_ERROR_ENTRIES = 3726
M_TRAIN_DATASET_ERROR_RATE = 3746
M_TRAIN_DATASET_ERROR_RATE_AFTER_EACH_TREE = 3779
M_TRAIN_DATASET_ID = 3693
M_TRAIN_DATASET_MINI_BATCH_LOSS = 3643
M_TRAIN_DATASET_PREDICT_SCORES = 3952
M_TRAIN_DATASET_USED_ENTRIES = 3985
M_TRAIN_ENABLED_CONTROL_TYPES = 3339
M_TRAIN_ENABLED_CONTROL_TYPES_ORIGINAL_VALUE = 3341
M_TRAIN_ENABLED_CONTROL_TYPES_STATE = 3340
M_TRAIN_ENABLED_CONTROL_TYPES_TRAINED_VALUE = 3342
M_TRAIN_ENABLED_NUMBER_OF_MODEL_CONTROL_TYPES = 3343
M_TRAIN_FROM_DISK = 967
M_TRAIN_IMAGE_MIN_SIZE_X = 3729
M_TRAIN_IMAGE_MIN_SIZE_Y = 3730
M_TRAIN_IMAGE_STEP_X = 3731
M_TRAIN_IMAGE_STEP_Y = 3732
M_TRAIN_META_CLASSES = 3
M_TRAIN_NEW_CHAR = 0
M_TRAIN_REPORT = 3944
M_TRAIN_SCORE_MAX = 961
M_TRAIN_SCORE_MEAN = 962
M_TRAIN_SCORE_MEDIAN = 964
M_TRAIN_SCORE_MIN = 960
M_TRAIN_SCORE_VARIANCE = 963
M_TRAIN_TIMEOUT = 2680
M_TRAIN_TREE = 3788
M_TRAIN_TREE_ENSEMBLE = 3521
M_TRAIN_TREE_ENSEMBLE_RESULT = 3757
M_TRANSFER_LEARNING = 3625
M_TRANSFER_METHOD = 4294963200
M_TRANSFER_PRIORITY = 2434
M_TRANSFER_RAW_DATA = 4132
M_TRANSFER_TYPE_KNOWN_BITS = 4294967259
M_TRANSFORMATION_DOMAIN = 1864
M_TRANSFORMATION_MATRIX = 72
M_TRANSFORMATION_MATRIX_ID = 52
M_TRANSFORMATION_MODE = 1824
M_TRANSFORMATION_TYPE = 3
M_TRANSFORMED_BL_X = 27
M_TRANSFORMED_BL_Y = 28
M_TRANSFORMED_BR_X = 29
M_TRANSFORMED_BR_Y = 30
M_TRANSFORMED_UL_X = 23
M_TRANSFORMED_UL_Y = 24
M_TRANSFORMED_UR_X = 25
M_TRANSFORMED_UR_Y = 26
M_TRANSFORM_CACHE = 132
M_TRANSFORM_TYPES_SHIFT = 8
M_TRANSIENT_PATTERN = 8388613
M_TRANSLATABLE = 53
M_TRANSLATE = 5
M_TRANSLATE_POINTS = 8
M_TRANSLATE_X = 1521
M_TRANSLATE_Y = 1522
M_TRANSLATION = 1
M_TRANSLATION_ROTATION = 2
M_TRANSLATION_ROTATION_SCALE = 3
M_TRANSLATION_TOLERANCE = 1907
M_TRANSPARENT = 16777305
M_TRANSPARENT_COLOR = 16777312
M_TRANSPORT_PROTOCOL = 7706
M_TRAVEL = 4162
M_TREE = 3042
M_TREE_DEPTHS_ACHIEVED = 3536
M_TREE_DEPTH_ACHIEVED = 3811
M_TREE_INDEX = 3803
M_TREE_MAX_DEPTH = 3318
M_TREE_MAX_NUMBER_OF_LEAF_NODES = 3780
M_TREE_NUMBER_OF_LEAF_NODES_ACHIEVED = 3810
M_TREE_TRAINED = 65030
M_TRIANGLE = 65536
M_TRIANGLE_BISECTION_BRIGHT = 48
M_TRIANGLE_BISECTION_DARK = 32
M_TRIGGER = 5140
M_TRIGGER_ACTIVATION = 4616
M_TRIGGER_COMMAND = 4619
M_TRIGGER_DELAY = 5196
M_TRIGGER_FOR_FIRST_GRAB = 16
M_TRIGGER_SELECTOR = 7714
M_TRIGGER_SELECTOR_SIZE = 5497558146594
M_TRIGGER_SOURCE = 4617
M_TRIGGER_STATE = 4618
M_TRIGGER_SUPPORTED = 5183
M_TRIGGER_WIDTH = 1
M_TRIPLET = 8
M_TRIPLET_ITEM_SIZE = 1624
M_TRI_STATE = 3
M_TRUE = 1
M_TRUNCATED_PDF417 = 134217733
M_TRUNCATED_PDF417_NAME = MIL_TEXT("Truncated_PDF417")
M_TSAI_BASED = 8
M_TTF_FONT_DEFAULT_SIZE = 12
M_TTL = 1
M_TUNER_FREQUENCY = 4138
M_TUNER_NUM = 2010
M_TUNER_STANDARD = 4139
M_TUNER_TYPE = 2011
M_TU_FID = 5888
M_TU_LIST = 4099
M_TU_NAME = 4864
M_TU_NAME_LENGTH = 5497558143744
M_TWO_POINTS = 3657
M_TYPE = 1008
M_TYPE_ARRAY_ID_PTR = 268435456
M_TYPE_BOOLEAN = 16777216
M_TYPE_CATEGORY = 8192
M_TYPE_CHAR = 68719476736
M_TYPE_COMMAND = 32768
M_TYPE_DOUBLE = 343597383680
M_TYPE_ENUMERATION = 1073741824
M_TYPE_FILENAME = 134217728
M_TYPE_FLOAT = 274877906944
M_TYPE_INDEX = 33554432
M_TYPE_INT64 = 549755813888
M_TYPE_LABEL = 16777216
M_TYPE_LONG = 206158430208
M_TYPE_MASK = 2147483392
M_TYPE_META_FLAGS = 336592896
M_TYPE_MIL_DOUBLE = 343597383680
M_TYPE_MIL_FLOAT = 274877906944
M_TYPE_MIL_ID = 412316860416
M_TYPE_MIL_INT = 549755813888
M_TYPE_MIL_INT16 = 137438953472
M_TYPE_MIL_INT32 = 206158430208
M_TYPE_MIL_INT64 = 549755813888
M_TYPE_MIL_TEXT = 618475290624
M_TYPE_MIL_UINT8 = 687194767360
M_TYPE_MIL_UUID = 755914244096
M_TYPE_PTR = 2097152
M_TYPE_REGISTER = 2147483648
M_TYPE_SHORT = 137438953472
M_TYPE_SIGN_MASK = 201326592
M_TYPE_STRING = 481036337152
M_TYPE_STRING_PTR = 481036337152
M_TYPE_TEXT_CHAR = 618475290624
M_TYPE_UINT8 = 687194767360
M_TYPE_VALUE = 16384
M_TYPICAL_RECOGNITION = 2
M_U = 16
M_U3V = 768
M_UART0 = 0
M_UART1 = 65536
M_UART10 = 655360
M_UART11 = 720896
M_UART12 = 786432
M_UART13 = 851968
M_UART14 = 917504
M_UART15 = 983040
M_UART2 = 131072
M_UART3 = 196608
M_UART4 = 262144
M_UART5 = 327680
M_UART6 = 393216
M_UART7 = 458752
M_UART8 = 524288
M_UART9 = 589824
M_UART_BYTES_READ = 4723
M_UART_BYTES_WRITTEN = 4722
M_UART_DATA_PENDING = 4707
M_UART_DATA_RECEIVED = 17
M_UART_DATA_RECEIVED_HANDLER_PTR = 4719
M_UART_DATA_RECEIVED_HANDLER_USER_PTR = 4720
M_UART_DATA_SIZE = 4703
M_UART_END = 4725
M_UART_FREE = 4725
M_UART_INTERFACE_TYPE = 4721
M_UART_NB_MASK_SHIFT = 16
M_UART_OUTPUT = 4716
M_UART_PARITY = 4701
M_UART_PRESENT = 2132
M_UART_READ_CHAR = 4706
M_UART_READ_STRING = 4710
M_UART_READ_STRING_MAXIMUM_SIZE = 4712
M_UART_READ_STRING_SIZE = 4711
M_UART_SPEED = 4704
M_UART_START = 4701
M_UART_STOP_BITS = 4702
M_UART_STRING_DELIMITER = 4713
M_UART_SYNCHRONOUS = 33554432
M_UART_THREAD_HANDLE = 4717
M_UART_THREAD_ID = 4718
M_UART_TIMEOUT = 4714
M_UART_WRITE_CHAR = 4705
M_UART_WRITE_STRING = 4708
M_UART_WRITE_STRING_SIZE = 4709
M_UNABLE_TO_FIND_CPU_TRAIN_ENGINE = 4072
M_UNABLE_TO_FIND_GPU_TRAIN_ENGINE = 4088
M_UNABLE_TO_FIND_VALID_GPU = 4091
M_UNABLE_TO_LOAD_CPU_TRAIN_ENGINE = 4089
M_UNABLE_TO_LOAD_GPU_TRAIN_ENGINE = 4090
M_UNCALIBRATED_Z = 50
M_UNCHANGED = 1073741829
M_UNCONDITIONAL = 0
M_UNCONSTRAINED = -2
M_UNCORRECTED = 1349
M_UNCORRECTED_DEPTH_MAP = 1341
M_UNCORRECTED_DEPTH_MAP_BUFFER_TYPE = 1346
M_UNCORRECTED_DEPTH_MAP_FIXED_POINT = 1343
M_UNCORRECTED_DEPTH_MAP_SIZE_X = 1344
M_UNCORRECTED_DEPTH_MAP_SIZE_Y = 1345
M_UND = 8388608
M_UNDECIMATED = 1826
M_UNDEFINED = 3948
M_UNDER = 4077
M_UNDERLAY = 8388608
M_UNDERLAY_ALWAYS_ON_TOP = 10119
M_UNDERLAY_DOUBLE_RANGE_END = 4541
M_UNDERLAY_DOUBLE_RANGE_START = 4534
M_UNDERLAY_FORMAT_SUPPORTED = 4529
M_UNDERLAY_ID = 1120
M_UNDERLAY_INCOMPATIBLE_BITS = 1152921513196781696
M_UNDERLAY_LIVE_FORMAT_SUPPORTED = 4527
M_UNDERLAY_MEM_SIZE = 2094
M_UNDERLAY_SHOW = 10137
M_UNDERLAY_SUPPORTED = 4530
M_UNDERLAY_UPDATE_STATE = 10036
M_UNDERLAY_ZOOM_MAX = 4531
M_UNDERLAY_ZOOM_MIN = 4532
M_UNDER_CURRENT = 14
M_UNDETECTED = 512
M_UNENHANCE_FORMAT = 9041
M_UNEVEN_GRID_STEP = 5
M_UNHOOK = 67108864
M_UNICODE = 2
M_UNICODE_CLIENT = 16777216
M_UNIFIED_ZOOM = 3225
M_UNIFORM = 1
M_UNIFORM_TRANSFORMATION = 1368
M_UNINITIALIZED = 195934928
M_UNIT_DIRECTION_VECTOR = 2
M_UNIVERSAL = 4096
M_UNKNOWN = -9999
M_UNKNOWN_OBJECT_TYPE = 0
M_UNKNOWN_TYPE = 10272
M_UNLINK = 2
M_UNLOCK = 24576
M_UNORGANIZED = 1919
M_UNREGISTER_EXTERN_BUFFER_API_MODULE = 4598
M_UNROTATED_MAX_X = 3853
M_UNROTATED_MAX_Y = 3854
M_UNROTATED_MAX_Z = 3855
M_UNROTATED_MIN_X = 3850
M_UNROTATED_MIN_Y = 3851
M_UNROTATED_MIN_Z = 3852
M_UNSIGNED = 0
M_UNSTABLE_POLARITY = 672
M_UNSTABLE_PRINCIPAL_COMPONENTS_012 = 684
M_UNSTABLE_PRINCIPAL_COMPONENTS_12 = 682
M_UNSTABLE_PRINCIPAL_COMPONENT_2 = 680
M_UNSUPPORTED_FORMAT = 5241
M_UNTRAINED = 3733
M_UNUSED_BITS = -9223372036854775808
M_UNUSED_ERROR_212 = 56212
M_UNUSED_ERROR_213 = 56213
M_UNUSED_ERROR_214 = 56214
M_UNUSED_ERROR_215 = 56215
M_UNUSED_ERROR_216 = 56216
M_UNUSED_ERROR_217 = 56217
M_UNUSED_ERROR_218 = 56218
M_UNUSED_ERROR_219 = 56219
M_UNUSED_ERROR_220 = 56220
M_UNUSED_ERROR_221 = 56221
M_UNUSED_ERROR_222 = 56222
M_UNUSED_ERROR_223 = 56223
M_UNUSED_ERROR_224 = 56224
M_UNUSED_ERROR_225 = 56225
M_UNUSED_ERROR_CORRECTION = 40970
M_UNUSED_ERROR_CORRECTION_GRADE = 36868
M_UPCE_COMPRESSED = 129
M_UPC_A = 2048
M_UPC_A_NAME = MIL_TEXT("UPC_A")
M_UPC_E = 4096
M_UPC_E_NAME = MIL_TEXT("UPC_E")
M_UPDATE = 3199
M_UPDATE_DX_VERSION_ON_TITLEBAR = 10043
M_UPDATE_END = 2056
M_UPDATE_FIRMWARES = 16
M_UPDATE_GRAB_TYPE = 10050
M_UPDATE_GRAPHIC_LIST = 10564
M_UPDATE_INTERACTIVE_STATE = 84
M_UPDATE_MEGA_BUFFER_CHILD_POSITION = 10042
M_UPDATE_ON_OVERLAY_MODIFIED_INTERNAL = 10164
M_UPDATE_PANEL = 1
M_UPDATE_PERFORMANCE_COUNTERS = 1050
M_UPDATE_RATE = 6613
M_UPDATE_RATE_DIVIDER = 10038
M_UPDATE_RATE_MAX = 10205
M_UPDATE_START = 2055
M_UPDATE_STATE = 10133
M_UPDATE_SYNCHRONIZATION = 10118
M_UPDATE_THREAD_PRIORITY = 10029
M_UPDATE_TITLE = 10175
M_UPDATE_TRAINED_CNN_PARAMS = 3706
M_UPDATE_TRANSFER_TYPE = 10155
M_UPDATE_WEB = 3187
M_UPDATE_WITH_PAINT_MESSAGE = 10126
M_UPPERCASE = 65536
M_UPPERCASE_OLD = 65536
M_UPPER_HALF = 1024
M_UP_VECTOR = 4165
M_URGENT = 28
M_URL_ERROR_END = 53999
M_URL_ERROR_START = 53000
M_USAGE_METER = 2302
M_USB3_FINGERPRINT = 21200
M_USB3_VISION = 200
M_USE = 4096
M_USED_IN_CONTINUOUS_GRAB = 5096
M_USER = 1
M_USER1_WEB_OFFSET = 1
M_USER2_WEB_OFFSET = 2
M_USER_ALLOCATED = 4294967294
M_USER_ATTRIBUTE = 536870912
M_USER_BIT = 2684354560
M_USER_BIT0 = 2684354560
M_USER_BIT1 = 2684354561
M_USER_BIT10 = 2684354570
M_USER_BIT11 = 2684354571
M_USER_BIT12 = 2684354572
M_USER_BIT13 = 2684354573
M_USER_BIT14 = 2684354574
M_USER_BIT15 = 2684354575
M_USER_BIT16 = 2684354576
M_USER_BIT17 = 2684354577
M_USER_BIT18 = 2684354578
M_USER_BIT19 = 2684354579
M_USER_BIT2 = 2684354562
M_USER_BIT20 = 2684354580
M_USER_BIT21 = 2684354581
M_USER_BIT22 = 2684354582
M_USER_BIT23 = 2684354583
M_USER_BIT24 = 2684354584
M_USER_BIT25 = 2684354585
M_USER_BIT26 = 2684354586
M_USER_BIT27 = 2684354587
M_USER_BIT28 = 2684354588
M_USER_BIT29 = 2684354589
M_USER_BIT3 = 2684354563
M_USER_BIT30 = 2684354590
M_USER_BIT31 = 2684354591
M_USER_BIT32 = 2684354592
M_USER_BIT33 = 2684354593
M_USER_BIT34 = 2684354594
M_USER_BIT35 = 2684354595
M_USER_BIT36 = 2684354596
M_USER_BIT37 = 2684354597
M_USER_BIT38 = 2684354598
M_USER_BIT39 = 2684354599
M_USER_BIT4 = 2684354564
M_USER_BIT40 = 2684354600
M_USER_BIT41 = 2684354601
M_USER_BIT42 = 2684354602
M_USER_BIT43 = 2684354603
M_USER_BIT44 = 2684354604
M_USER_BIT45 = 2684354605
M_USER_BIT46 = 2684354606
M_USER_BIT47 = 2684354607
M_USER_BIT48 = 2684354608
M_USER_BIT49 = 2684354609
M_USER_BIT5 = 2684354565
M_USER_BIT50 = 2684354610
M_USER_BIT51 = 2684354611
M_USER_BIT52 = 2684354612
M_USER_BIT53 = 2684354613
M_USER_BIT54 = 2684354614
M_USER_BIT55 = 2684354615
M_USER_BIT56 = 2684354616
M_USER_BIT57 = 2684354617
M_USER_BIT58 = 2684354618
M_USER_BIT59 = 2684354619
M_USER_BIT6 = 2684354566
M_USER_BIT60 = 2684354620
M_USER_BIT61 = 2684354621
M_USER_BIT62 = 2684354622
M_USER_BIT63 = 2684354623
M_USER_BIT7 = 2684354567
M_USER_BIT8 = 2684354568
M_USER_BIT9 = 2684354569
M_USER_BIT_ALL = 1048575
M_USER_BIT_BIT_MASK_ENABLED = 268435456
M_USER_BIT_CC_A = 43
M_USER_BIT_CC_B = 44
M_USER_BIT_CC_IO = 2684354816
M_USER_BIT_CC_IO0 = 2684354816
M_USER_BIT_CC_IO1 = 2684354817
M_USER_BIT_CC_IO2 = 2684354818
M_USER_BIT_CC_IO3 = 2684354819
M_USER_BIT_CONFIG_ERROR = 62
M_USER_BIT_COUNT = 4364
M_USER_BIT_ERROR = 63
M_USER_BIT_FIELD = 4181
M_USER_BIT_INQUIRE_END = 4366
M_USER_BIT_INQUIRE_START = 4363
M_USER_BIT_INVALID_BIT_MASK = 33554431
M_USER_BIT_IN_ACTIVE_LEVEL = 7402
M_USER_BIT_MASK = 3992977408
M_USER_BIT_OPTOMODULE = 4365
M_USER_BIT_PERFORMANCE_LOGS = 7403
M_USER_BIT_PRESENT = 1073741824
M_USER_BIT_QUEUE_MODE = 4087
M_USER_BIT_STATE = 524288
M_USER_BIT_STATE_ALL = 268959744
M_USER_BIT_TL_IO = 2684355072
M_USER_BIT_TL_IO0 = 2684355072
M_USER_BIT_TL_IO1 = 2684355073
M_USER_BIT_TL_IO10 = 2684355082
M_USER_BIT_TL_IO11 = 2684355083
M_USER_BIT_TL_IO12 = 2684355084
M_USER_BIT_TL_IO13 = 2684355085
M_USER_BIT_TL_IO14 = 2684355086
M_USER_BIT_TL_IO15 = 2684355087
M_USER_BIT_TL_IO2 = 2684355074
M_USER_BIT_TL_IO3 = 2684355075
M_USER_BIT_TL_IO4 = 2684355076
M_USER_BIT_TL_IO5 = 2684355077
M_USER_BIT_TL_IO6 = 2684355078
M_USER_BIT_TL_IO7 = 2684355079
M_USER_BIT_TL_IO8 = 2684355080
M_USER_BIT_TL_IO9 = 2684355081
M_USER_BIT_TL_TRIGGER = 2684355328
M_USER_BIT_TL_TRIGGER0 = 2684355329
M_USER_BIT_TL_TRIGGER1 = 2684355330
M_USER_BIT_TL_TRIGGER2 = 2684355331
M_USER_BIT_TL_TRIGGER3 = 2684355332
M_USER_BIT_VALUE_IN = 2818572288
M_USER_BIT_VALUE_OUT = 2751463424
M_USER_CONFIDENCE = 4013
M_USER_DATA_PTR = 1
M_USER_DATA_SIZE = 8205
M_USER_DEFINED = 21
M_USER_DEFINED_PERCENTAGE = 3943
M_USER_DEFINED_SEED = 3465
M_USER_DEFINED_VALUE = 3942
M_USER_DEFINE_LOW_ATTRIBUTE = 65535
M_USER_DLL_DIR = MIL_TEXT("///MILUSERDLLDIR///")
M_USER_FEED = 27
M_USER_FLAG = 6
M_USER_FPGA_FUNCTION = 1073806336
M_USER_FUNCTION = 1073799168
M_USER_HOOK = 26
M_USER_IN_FORMAT = 134217728
M_USER_LABEL = 228
M_USER_MODULE_1 = 1073799680
M_USER_MODULE_2 = 1073800192
M_USER_MODULE_3 = 1073800704
M_USER_MODULE_4 = 1073801216
M_USER_MODULE_5 = 1073801728
M_USER_MODULE_6 = 1073802240
M_USER_MODULE_7 = 1073802752
M_USER_MODULE_FPGA = 1073806336
M_USER_NAME = 7712
M_USER_OBJECT_1 = 536936448
M_USER_OBJECT_2 = 537001984
M_USER_ONNX = 4761
M_USER_OUT = 1
M_USER_OUT_FORMAT = 67108864
M_USER_OVERLAY_ID = 1123
M_USER_TRACE_TEXT = 15390
M_USER_TRACE_VALUE = 15391
M_USER_TRAINED = 3783
M_USER_WINDOW = 268435456
M_USER_WINDOW_HANDLE = 10121
M_USE_ACCELERATOR = 2102
M_USE_AMD_3DNOW = 10289
M_USE_AMD_3DNOW_EXTENSION = 10291
M_USE_AMD_MMX_EXTENSION = 10290
M_USE_AVX = 10282
M_USE_AVX2 = 10283
M_USE_AVX512_BASE = 10284
M_USE_AVX512_BLOCK1 = 10285
M_USE_AVX512_BLOCK2 = 10286
M_USE_BASELINE = 2262
M_USE_CALIBRATION = 19
M_USE_CERTAINTY = 2264
M_USE_CONVERT_TO_COLOR_DIB = 10147
M_USE_CORDIC = 131072
M_USE_CREATE_OVER_USER_BUFFER = 10145
M_USE_DDRAW = 2300
M_USE_DDRAW_UNDERLAY = 15324
M_USE_DDRAW_UNDERLAY_SURFACE = 15325
M_USE_DESTINATION = 8388608
M_USE_DESTINATION_CALIBRATION = 64
M_USE_DESTINATION_FIRST = 1769
M_USE_DESTINATION_SCALES = 1335
M_USE_DISPLAY_SIZE_BUFFER = 10153
M_USE_DOUBLE_BUFFERING_SCHEME = 10132
M_USE_EXTENSION = 22
M_USE_EXTERNAL_NO_TEARING = 10561
M_USE_FLICKER_FREE_BUFFER = 10146
M_USE_GDI_TO_APPLY_LUT = 10568
M_USE_GIGACOLOR_SCHEME = 10165
M_USE_GRAMMAR = 2261
M_USE_GRID_DECOMPOSITION = 2849
M_USE_HOST_ENTRY_BUFFER = 10149
M_USE_HOST_OVERLAY = 10122
M_USE_INTERNAL_BUFFER_FOR_GRAB_CONTINUOUS = 10034
M_USE_LEGACY_RAW_FORMAT = 15141
M_USE_LIB_TIFF_HANDLER = 15137
M_USE_LIVE_UNDERLAY = 10125
M_USE_MAX_INTERMEDIATES = 2
M_USE_MEGA_BUFFER = 10154
M_USE_MEMORY_DCF = 16
M_USE_MMX = 10274
M_USE_MODEL_NORMALS = 16777216
M_USE_MOUSE_PAN = 3208
M_USE_MOUSE_ZOOM = 3209
M_USE_MP_FOR_TRANSFER = 128
M_USE_NEW_DISPLAYS = 15512
M_USE_NOA = 2102
M_USE_NO_VIDEO_OVERLAY_BUFFER = 10191
M_USE_OS_DPI = 16777217
M_USE_PRESEARCH = 19712
M_USE_PRIMARY_SURFACE = 10037
M_USE_RECT_LIST = 512
M_USE_RESERVED_ANGLE_VALUE = 128
M_USE_RESERVED_COLOR = 10020
M_USE_SCENE_NORMALS = 33554432
M_USE_SET_LOCATION_TARGET = 1
M_USE_SIMD = 10273
M_USE_SOFTWARE_COMPOSITION = 10148
M_USE_SOURCE1_SCALES = 3091
M_USE_SOURCE2_SCALES = 3092
M_USE_SOURCE_FIRST = 1768
M_USE_SSE = 10276
M_USE_SSE2 = 10278
M_USE_SSE2_INT = 10277
M_USE_SSE3 = 10279
M_USE_SSE4_1 = 10280
M_USE_SSE4_2 = 10281
M_USE_SSE_INT = 10275
M_USE_TEMPLATE = 1
M_USE_UNDERLAY = 15325
M_USE_UNDERLAY_IN_ALL_DISPLAY = 15324
M_USE_UNDERLAY_IN_DUALHEAD = 10116
M_USE_USER_BUFFER_FOR_UNDERLAY = 10144
M_USE_VIDEO_MEMORY_BUFFER = 10110
M_USE_WINDOWED_CLASS = 15050
M_USE_YCBCR_RANGE = 10054
M_USE_YUV16_UYVY_SCHEME = 10192
M_USING_OLD_DISP = 15053
M_UTF8 = 150
M_UTILITY_USAGE = 2306
M_V = 32
M_VALID = 1
M_VALIDATE_DISPLAY = 10169
M_VALIDITY_MAP = 2048
M_VALID_FLAG = 123904
M_VALID_RECT = 9019
M_VALUE = 0
M_VALUE_MAX = 5
M_VALUE_MIN = 4
M_VALUE_WARNING_MAX = 8
M_VALUE_WARNING_MIN = 7
M_VARIABLE = 2
M_VARIABLE_MAX = 3
M_VARIANCE = 16777216
M_VCR_INPUT_TYPE = 4061
M_VECTOR = 1411
M_VECTOR_AND_RASTER = 1417
M_VENDOR_ID = 4549
M_VERSION = 15001
M_VERSION_INFORMATION_1_GRADE = 36955
M_VERSION_INFORMATION_2_GRADE = 36956
M_VERSION_INFORMATION_GRADE = 36937
M_VERTICAL = 1
M_VERTICAL_EDGE_PREWITT = 9437202
M_VERTICAL_EDGE_SOBEL = 9437200
M_VERTICAL_LEVEL_TAG = 33554432
M_VERTICAL_MARK_GROWTH = 41041
M_VERTICAL_MARK_MISPLACEMENT = 41045
M_VERTICAL_THICKNESS = 232
M_VERTICES = 108
M_VERTICES_CHAIN_INDEX = 71
M_VERTICES_INDEX = 79
M_VERTICES_X = 68
M_VERTICES_Y = 40
M_VERT_EDGE = 9437190
M_VERY_FAST = 65536
M_VERY_HIGH = 4
M_VERY_LOW = 0
M_VGA_DEVICE_SYSTEM = 8600
M_VGA_DEVICE_SYSTEM_END = 8663
M_VGA_DEVICE_SYSTEM_ID = 10100
M_VGA_DEVICE_SYSTEM_START = 8600
M_VGA_INDEX = 10012
M_VGA_INFO_DISPLAY_DEVICE_NAME = 8510
M_VGA_INFO_DISPLAY_RECT = 8507
M_VGA_SYSTEM_FROM_PHYSICAL_ADDRESS = 15323
M_VIA = 16777216
M_VIA_MEM_SIZE = 2096
M_VIDEO_DEVICE_DESCRIPTION_STRING = 4565
M_VIDEO_DEVICE_ID = 2130706436
M_VIDEO_DEVICE_INDEX = 1057
M_VIDEO_DEVICE_MASK = 3840
M_VIDEO_DEVICE_MODIFIED_AFTER = 53
M_VIDEO_DEVICE_MODIFIED_BEFORE = 52
M_VIDEO_DEVICE_OBJECT = 1099511627776
M_VIDEO_DEVICE_OFFSET = 8
M_VIDEO_DEVICE_REMOVED = 9407
M_VIDEO_DEVICE_SYNC = 8514
M_VIDEO_DEVICE_WAS_MODIFIED = 10052
M_VIDEO_ENCODER = 32768
M_VIDEO_HARDWARE_DEVICE = 524288
M_VIDEO_HD = 8192
M_VIDEO_MEMORY = 17179869184
M_VIDEO_MEMORY_RESTORED = 10046
M_VIDEO_OUTPUT = 8007
M_VIDEO_OUTPUT_CHANNELS = 8009
M_VIDEO_OUTPUT_INTERVAL = 8010
M_VIDEO_OUTPUT_TILE = 8008
M_VIDEO_SYSTEM_ID = 9010
M_VIEWPOINT = 4163
M_VIEW_BIT_SHIFT = 3183
M_VIEW_BOX = 4166
M_VIEW_MATRIX = 4161
M_VIEW_MODE = 3182
M_VIEW_ORIENTATION = 2097152
M_VIO = 150
M_VIO_FINGERPRINT = 20768
M_VIRTUAL_GRAB = 10188
M_VISIBLE = 1533
M_VISIBLE_BUFFER_RECT_SIZE_X = 10030
M_VISIBLE_BUFFER_RECT_SIZE_Y = 10031
M_VLIET = 2051
M_VOLTAGE = 65536
M_VOLTAGE_FGPA_VCCINT = 7303
M_VOLTAGE_FPGA_VCCAUX = 7306
M_VOLTAGE_FPGA_VCCAUX_MAX_MEASURED = 7308
M_VOLTAGE_FPGA_VCCAUX_MIN_MEASURED = 7307
M_VOLTAGE_FPGA_VCCBRAM = 7314
M_VOLTAGE_FPGA_VCCBRAM_MAX_MEASURED = 7316
M_VOLTAGE_FPGA_VCCBRAM_MIN_MEASURED = 7315
M_VOLTAGE_FPGA_VCCINT_MAX_MEASURED = 7305
M_VOLTAGE_FPGA_VCCINT_MIN_MEASURED = 7304
M_VOLTAGE_FPGA_VREFP = 7317
M_VOLUME = 1360
M_VSCROLL_VISIBLE = 10015
M_VSYNC = 23
M_VSYNC_ERROR = 4
M_VSYNC_SIGNAL = 256
M_VTK_TERRAIN = 3
M_VTK_TRACKBALL = 2
M_VTK_WINDOW = 32
M_WAIT = 1
M_WAIT_ON_BUFFER_FREED = 9013
M_WANT_TO_HANDLE_AUXILIARY_UPDATE = 15394
M_WARNING = 3
M_WARNINGS = 306
M_WARNING_GAPS = 3629
M_WARP_4_CORNER = 8388608
M_WARP_4_CORNER_REVERSE = 16777216
M_WARP_COEFFICIENT = 524288
M_WARP_IMAGE = 1
M_WARP_LUT = 4194304
M_WARP_MATRIX = 1048576
M_WARP_POLYNOMIAL = 2097152
M_WARP_TILE = 4
M_WATCHDOG_BITE_WARNING = 2377
M_WATCHDOG_MODE = 2370
M_WATCHDOG_PRESENT = 2378
M_WATCHDOG_REBOOT_TIMEOUT = 2373
M_WATCHDOG_RESET = 2374
M_WATCHDOG_RESET_COUNTER = 2375
M_WATCHDOG_TIMEOUT = 2371
M_WATCHDOG_WARNING = 2372
M_WATCHDOG_WARNING_TIME = 2376
M_WATERSHED = 1
M_WAVELET_COEFFICIENTS_IMAGE_ID = 1850
M_WAVELET_CONTEXT_TYPE = 1828
M_WAVELET_DRAW_SIZE_X = 1871
M_WAVELET_DRAW_SIZE_X_WITH_PADDING = 1857
M_WAVELET_DRAW_SIZE_Y = 1872
M_WAVELET_DRAW_SIZE_Y_WITH_PADDING = 1858
M_WAVELET_LEVEL_PADDING_OFFSET_X = 1866
M_WAVELET_LEVEL_PADDING_OFFSET_Y = 1867
M_WAVELET_LEVEL_SIZE_X = 1798
M_WAVELET_LEVEL_SIZE_Y = 1799
M_WAVELET_SIZE = 1856
M_WAVELET_TRANSFORM_CONTEXT = 9
M_WAVELET_TRANSFORM_CUSTOM_CONTEXT = 10
M_WAVELET_TRANSFORM_RESULT = 2199023255552
M_WAVELET_TYPE = 1802
M_WAVELET_VALIDITY = 1827
M_WAVE_TRANSFORM_COMB = 161
M_WAVE_TRANSFORM_ERROR = 160
M_WAV_DENOISE_COMB = 165
M_WAV_DENOISE_COMB2 = 166
M_WAV_DENOISE_ERROR = 159
M_WAV_VALIDATION_ERROR = 158
M_WEB = 8388608
M_WEB_APPLICATION = 1
M_WEB_CLIENT_CONNECTED = 43
M_WEB_CLIENT_DISCONNECTED = 49
M_WEB_CLIENT_INDEX = 219
M_WEB_CLIENT_TYPE = 220
M_WEB_CONNECTION = 15523
M_WEB_CONNECTION_PORT = 15528
M_WEB_ERROR = 178
M_WEB_ERROR_2 = 192
M_WEB_ERROR_END = 55999
M_WEB_ERROR_START = 55000
M_WEB_PUBLISH = 244
M_WEB_PUBLISHED_LIST = 12
M_WEB_PUBLISHED_LIST_SIZE = 17
M_WEB_PUBLISHED_NAME = 7
M_WEB_PUBLISH_MODE = 115
M_WEIGHTED = 2
M_WEIGHTED_AVERAGE = 1
M_WEIGHT_REGIONS = 502
M_WHEN_COMPLETED = 2
M_WHEN_DISPATCHED = 1
M_WHEN_MINIMIZED = 1
M_WHEN_NOT_VISIBLE = 2
M_WHITE = 1
M_WHITE_BALANCE = 5112
M_WHITE_BALANCE_CALCULATE = 16
M_WHITE_BALANCE_U = 5168
M_WHITE_BALANCE_V = 5172
M_WHITE_REF = 6651
M_WHITE_REF_DOUBLE = 6651
M_WHITE_SHADING = 5204
M_WHOLE_IMAGE = 1
M_WHOLE_SCENE = 8388627
M_WIDTH = 65536
M_WIDTH_AVERAGE = 3
M_WIDTH_DELTA_NEG = 6
M_WIDTH_DELTA_POS = 7
M_WIDTH_MAX = 30
M_WIDTH_MAX_INDEX = 20
M_WIDTH_MIN = 74
M_WIDTH_MIN_INDEX = 10
M_WIDTH_NOMINAL = 5
M_WIDTH_NOMINAL_MODE = 12
M_WIDTH_VALUE = 31
M_WINDOWED = 16777216
M_WINDOWED_DISPLAY_AVAILABLE = 4520
M_WINDOW_ACTION = 61
M_WINDOW_ACTIVE = 3149
M_WINDOW_ACTIVE_AFTER = 34
M_WINDOW_ACTIVE_BEFORE = 33
M_WINDOW_ALPHA_BLENDING = 3214
M_WINDOW_ALPHA_VALUE = 3215
M_WINDOW_ANNOTATIONS = 10556
M_WINDOW_ANNOTATIONS_ENABLED = 4443
M_WINDOW_ANNOTATIONS_STATE = 10558
M_WINDOW_BUF_ID = 1105
M_WINDOW_CLOSE_AFTER = 18
M_WINDOW_CLOSE_BEFORE = 17
M_WINDOW_CURRENTLY_MAXIMIZED = 10177
M_WINDOW_CURRENTLY_MINIMIZED = 10178
M_WINDOW_CURRENTLY_VISIBLE = 10187
M_WINDOW_CURSOR = 10199
M_WINDOW_ENABLE = 3150
M_WINDOW_ENABLE_AFTER = 36
M_WINDOW_ENABLE_BEFORE = 35
M_WINDOW_HANDLE = 3110
M_WINDOW_INITIAL_POSITION_X = 3088
M_WINDOW_INITIAL_POSITION_Y = 3089
M_WINDOW_INITIAL_SIZE_X = 10160
M_WINDOW_INITIAL_SIZE_Y = 10161
M_WINDOW_LAYERED = 3216
M_WINDOW_LBUTTONDOWN = 56
M_WINDOW_LBUTTONUP = 58
M_WINDOW_MAXBUTTON = 3064
M_WINDOW_MAXIMIZE_AFTER = 22
M_WINDOW_MAXIMIZE_BEFORE = 21
M_WINDOW_MAXIMUM_ZOOM_FACTOR = 6609
M_WINDOW_MENU_BAR = 3058
M_WINDOW_MENU_BAR_CHANGE = 3060
M_WINDOW_MINBUTTON = 3063
M_WINDOW_MINIMIZE_AFTER = 20
M_WINDOW_MINIMIZE_BEFORE = 19
M_WINDOW_MINIMUM_ZOOM_FACTOR = 6610
M_WINDOW_MOVE = 3061
M_WINDOW_OFFSET_X = 3111
M_WINDOW_OFFSET_Y = 3112
M_WINDOW_OVERLAP = 3053
M_WINDOW_PAINT = 3083
M_WINDOW_PAINT_AFTER = 32
M_WINDOW_PAINT_BEFORE = 31
M_WINDOW_PAINT_MESSAGES = 3172
M_WINDOW_PALETTE_NOCOLLAPSE = 3069
M_WINDOW_PAN_X = 3115
M_WINDOW_PAN_Y = 3116
M_WINDOW_POSCHANGE_AFTER = 26
M_WINDOW_POSCHANGE_BEFORE = 25
M_WINDOW_PROTECT_AREA = 3056
M_WINDOW_RANGE = 3072
M_WINDOW_RBUTTONDOWN = 57
M_WINDOW_RBUTTONUP = 59
M_WINDOW_RESIZE = 3052
M_WINDOW_RESIZED = 62
M_WINDOW_RESIZE_ON_ZOOM = 10189
M_WINDOW_RESTORE_AFTER = 24
M_WINDOW_RESTORE_BEFORE = 23
M_WINDOW_ROI_BUTTONS = 10200
M_WINDOW_SCROLLBAR = 3054
M_WINDOW_SCROLL_AFTER = 30
M_WINDOW_SCROLL_BEFORE = 29
M_WINDOW_SHOW = 10140
M_WINDOW_SHOW_AFTER = 38
M_WINDOW_SHOW_BEFORE = 37
M_WINDOW_SIZE_X = 3113
M_WINDOW_SIZE_Y = 3114
M_WINDOW_SIZING = 74
M_WINDOW_SYNC_UPDATE = 3165
M_WINDOW_SYSBUTTON = 3062
M_WINDOW_TASKBAR = 10196
M_WINDOW_TASKBAR_ON_FULLSCREEN = 10197
M_WINDOW_THREAD_HANDLE = 3152
M_WINDOW_THREAD_ID = 3153
M_WINDOW_TITLE_BAR = 3057
M_WINDOW_TITLE_BAR_CHANGE = 3059
M_WINDOW_TRANSPARENCY = 3212
M_WINDOW_TRANSPARENT_COLOR = 3213
M_WINDOW_UPDATE_ON_PAINT = 3081
M_WINDOW_VISIBLE = 3202
M_WINDOW_VISIBLE_CHANGE = 43
M_WINDOW_VISIBLE_OFFSET_X = 3141
M_WINDOW_VISIBLE_OFFSET_Y = 3142
M_WINDOW_VISIBLE_SIZE_X = 3145
M_WINDOW_VISIBLE_SIZE_Y = 3146
M_WINDOW_ZOOM = 3051
M_WINDOW_ZOOM_AFTER = 28
M_WINDOW_ZOOM_BEFORE = 27
M_WINDOW_ZOOM_FACTOR_X = 6611
M_WINDOW_ZOOM_FACTOR_Y = 6612
M_WINDOW_ZOOM_X = 3117
M_WINDOW_ZOOM_Y = 3118
M_WIN_MODE = 2017
M_WIREFRAME = 32
M_WITHOUT_REPLACEMENT = 3785
M_WITH_CALIBRATION = 131072
M_WITH_COMPENSATION = 2
M_WITH_REPLACEMENT = 3786
M_WORLD = 8192
M_WORLD_BOX = 1487
M_WORLD_BOX_X_MAX = 1481
M_WORLD_BOX_X_MIN = 1479
M_WORLD_BOX_Y_MAX = 1482
M_WORLD_BOX_Y_MIN = 1480
M_WORLD_FERET_X = 1465
M_WORLD_FERET_Y = 1466
M_WORLD_LINE = 2175
M_WORLD_OFFSET_X = 142
M_WORLD_OFFSET_Y = 143
M_WORLD_OFFSET_Z = 144
M_WORLD_POS_X = 207
M_WORLD_POS_Y = 208
M_WORLD_POS_Z = 1371
M_WORLD_TO_PIXEL = 2
M_WORLD_X = 3895
M_WORLD_X_AT_Y_MAX = 1484
M_WORLD_X_AT_Y_MIN = 1483
M_WORLD_Y = 3896
M_WORLD_Y_AT_X_MAX = 1486
M_WORLD_Y_AT_X_MIN = 1485
M_WORLD_Z = 3897
M_WPF = 1048576
M_WPF_DISPLAY_BUFFER_ID = 1121
M_WRITE = 2
M_WRITE_COMBINING = 16384
M_WRITE_GRAB_VALIDATION_TAG = 5317
M_WRITE_SIZE_X = 2
M_WRITE_SIZE_Y = 5
M_WRITE_TIMEOUT = 2059
M_X = 2975
M_X11_ACC_DEFAULT = 1
M_X11_ACC_NONE = 0
M_X86_FPU_FLAGS = 15043
M_XA = 4096
M_XBGR32 = 4608
M_XCL = 2048
M_XD = 32768
M_XDISPLAY = 10195
M_XDUAL_SCREEN = 4096
M_XNOR = 27
M_XNOR_CONST = 32795
M_XOR = 24
M_XORG_ACCELERATION = 15321
M_XOR_ARM_ACTIVATION = 50331648
M_XOR_CONST = 32792
M_XPIXMAP_ALLOC = 9000
M_XPIXMAP_FREE = 9001
M_XPIXMAP_HANDLE = 9002
M_XRGB32 = 2560
M_XVIDEO_ADAPTOR_INDEX = 9046
M_XYZ = 1935
M_XYZI = 1936
M_XY_AXES = 3926
M_XY_DEAD_PIXELS = 83
M_XY_DEAD_PIXELS_ARRAY_SIZE = 86
M_XY_DESTINATION = 305
M_XY_DESTINATION_ARRAY_SIZE = 314
M_XY_PATH_LIST = 6
M_XY_PLANE = 8388626
M_XY_SIZE = 308
M_XY_SIZE_ARRAY_SIZE = 317
M_XY_SOURCE = 302
M_XY_SOURCE_ARRAY_SIZE = 311
M_XZ_AXES = 3927
M_X_DEAD_PIXELS = 81
M_X_DEAD_PIXELS_ARRAY_SIZE = 84
M_X_DESTINATION = 303
M_X_DESTINATION_ARRAY_SIZE = 312
M_X_MAX_AT_Y_MAX = 22
M_X_MAX_AT_Y_MIN = 59
M_X_MIN_AT_Y_MAX = 58
M_X_MIN_AT_Y_MIN = 21
M_X_PATH_LIST = 4
M_X_SIZE = 306
M_X_SIZE_ARRAY_SIZE = 315
M_X_SOURCE = 300
M_X_SOURCE_ARRAY_SIZE = 309
M_X_THEN_Y = 1
M_Y = 8
M_YC = 9
M_YCBCRHD_TO_BGR = 29
M_YCBCRHD_TO_MONO = 28
M_YCBCRHD_TO_RGB = 30
M_YCBCRHD_TO_YCBCRHD = 32
M_YCBCRHD_TO_YUV = 31
M_YCBCRSD_TO_BGR = 24
M_YCBCRSD_TO_MONO = 23
M_YCBCRSD_TO_RGB = 25
M_YCBCRSD_TO_YCRCBSD = 27
M_YCBCRSD_TO_YUV = 26
M_YCBCR_HD = 2
M_YCBCR_RANGE = 5085
M_YCBCR_SD = 1
M_YCBCR_UHD = 3
M_YCBCR_UHD_SUPPORTED = 4401
M_YCRCBHD_TO_BGR = 29
M_YCRCBHD_TO_MONO = 28
M_YCRCBHD_TO_RGB = 30
M_YCRCBHD_TO_YCRCBHD = 32
M_YCRCBHD_TO_YUV = 31
M_YCRCBSD_TO_BGR = 24
M_YCRCBSD_TO_MONO = 23
M_YCRCBSD_TO_RGB = 25
M_YCRCBSD_TO_YCRCBSD = 27
M_YCRCBSD_TO_YUV = 26
M_YCRCB_RANGE = 5080
M_YES = 1
M_YIELD_FOR_END_OF_XFER = 4361
M_YUV = 4
M_YUV12 = 5632
M_YUV12_1394 = 7936
M_YUV16 = 5888
M_YUV1611 = 5376
M_YUV16_1394 = 7424
M_YUV16_TO_RGB = 10486061
M_YUV16_UYVY = 7424
M_YUV16_YUYV = 7168
M_YUV24 = 6912
M_YUV32 = 8192
M_YUV411 = 5632
M_YUV411_1394 = 7936
M_YUV422 = 5888
M_YUV422_1394 = 7424
M_YUV422_UYVY = 7424
M_YUV422_YUYV = 7168
M_YUV444 = 6912
M_YUV9 = 5376
M_YUV_EXTENDED_RANGE_END = 16128
M_YUV_EXTENDED_RANGE_START = 14336
M_YUV_RANGE_END = 10240
M_YUV_RANGE_START = 5376
M_YUV_TO_BGR = 18
M_YUV_TO_MONO = 17
M_YUV_TO_RGB = 19
M_YUV_TO_YCBCRHD = 22
M_YUV_TO_YCBCRSD = 21
M_YUV_TO_YCRCBHD = 22
M_YUV_TO_YCRCBSD = 21
M_YUV_TO_YUV = 20
M_YX_AXES = 3928
M_YZ_AXES = 3929
M_Y_AXIS_CLOCKWISE = 32
M_Y_AXIS_COUNTER_CLOCKWISE = 16
M_Y_AXIS_DIRECTION = 2389
M_Y_DEAD_PIXELS = 82
M_Y_DEAD_PIXELS_ARRAY_SIZE = 85
M_Y_DESTINATION = 304
M_Y_DESTINATION_ARRAY_SIZE = 313
M_Y_MAX_AT_X_MAX = 61
M_Y_MAX_AT_X_MIN = 24
M_Y_MIN_AT_X_MAX = 23
M_Y_MIN_AT_X_MIN = 60
M_Y_MIRRORED = 5435
M_Y_PATH_LIST = 5
M_Y_SIZE = 307
M_Y_SIZE_ARRAY_SIZE = 316
M_Y_SOURCE = 301
M_Y_SOURCE_ARRAY_SIZE = 310
M_Y_THEN_X = 1773
M_Z = 2976
M_ZERO = 256
M_ZOOM = 5144
M_ZOOMED_DESTINATION_OUT_DESKTOP = 10168
M_ZOOM_ACCURACY = 10560
M_ZOOM_FACTOR_X = 6605
M_ZOOM_FACTOR_Y = 6606
M_ZOOM_MAX_X = 3190
M_ZOOM_MAX_Y = 3192
M_ZOOM_MIN_X = 3191
M_ZOOM_MIN_Y = 3193
M_ZOOM_PAN_HANDLED_BY_SCHEME = 10563
M_ZOOM_X = 3002
M_ZOOM_Y = 3003
M_ZX_AXES = 3930
M_ZY_AXES = 3931
M_Z_DOWN = 5246
M_Z_MAX = 2909
M_Z_MIN = 2908
M_Z_UP = 5245
M_ACCEPTANCE_THRESHOLD = 17
M_ACCUMULATE_AND_FUSION = 513
M_AIMDPM_CALIBRATION_RESULTS = 1654
M_AIMDPM_GRADING = 128
M_ALIGN_RMS_ERROR_RELATIVE_THRESHOLD_REACHED = 1971
M_ARC_ANGLE = 2048
M_ARC_ANGLE_END = 2050
M_ARC_ANGLE_START = 2049
M_ARC_CENTER_X = 13312
M_ARC_CENTER_Y = 17408
M_ARC_COVERAGE = 216
M_ARC_END_X = 13314
M_ARC_END_Y = 17410
M_ARC_LENGTH = 8192
M_ARC_RADIUS = 64
M_ARC_START_X = 9
M_ARC_START_Y = 10
M_AUTO_ASPECT_RATIO = 123
M_BLOB_IDENTIFICATION = 2
M_BULGE = 145
M_BULGES = 145
M_CALIBRATION_SUCCESSFUL = 130
M_CAMERA_MODEL_SIZE = 5497558146591
M_CAMERA_VENDOR_SIZE = 5497558146584
M_CERTAINTY_THRESHOLD = 25
M_CIRCLE_COVERAGE = 216
M_CIRCLE_LENGTH = 8192
M_CIRCLE_RADIUS = 64
M_CLASS_RESULT = 275414777888
M_CLUSTER_SERVER_NAME_SIZE = 5497558155728
M_CODE_RESULT = 545259522
M_CONVOLUTIONAL_NETWORK = 2779
M_COPY_DATA = 65
M_CPU_VENDOR_NAME_SIZE = 5497558149192
M_DATA_POSITION_X = 13312
M_DATA_POSITION_Y = 17408
M_DEBUG_BUFFER_PATH_SIZE = 5497558146588
M_DEVICE_NAME_SIZE = 5566277615616
M_DISTORTION = 32795
M_DISTRIBUTED_MIL_REMOTE_COMPUTER_NAME_SIZE = 5497558146584
M_DOT_SPACING = 32775
M_DRAW_DATA = 1048576
M_DRAW_DATA_ALL = 10
M_DRAW_GENERAL_FERET = 1048576
M_DRAW_NEAREST_EDGELS = 65536
M_DRAW_REFERENCE_FEATURES = 12
M_DRAW_VERTEX = 1024
M_DRAW_VERTEXES = 1024
M_ECC_010 = 20
M_ECC_040 = 21
M_ECC_050 = 0
M_ECC_060 = 22
M_ECC_070 = 23
M_ECC_080 = 1
M_ECC_090 = 24
M_ECC_100 = 2
M_ECC_110 = 25
M_ECC_120 = 26
M_ECC_130 = 27
M_ECC_140 = 3
M_EDGELS_POSITION_X = 13312
M_EDGELS_POSITION_Y = 17408
M_EDOF_IMAGE_SIZE_BAND = 1911
M_EXCLUDED_EDGE = 8388608
M_FARTHEST = 38
M_FEATURE_METHOD = 103
M_FEATURE_OPERATION = 103
M_FERET = 69
M_FORMAT_DETECTED_SIZE = 5497558146590
M_FORMAT_SIZE = 5497558146581
M_FORMAT_SUPPORTED_SIZE = 5497558146582
M_FPGA_DESCRIPTION_SIZE = 5497558146593
M_FROM_REGION_GEOMETRY = 1785
M_FUNCTION_NAME_FROM_OPCODE_SIZE = 5497558138928
M_GC_CLPROTOCOL_DEVICE_ID_SIZE = 5497558146610
M_GC_FEATURE_CHANGE_NAME_SIZE = 5497566986240
M_GC_GENICAM_UI_SIZE = 5497558146587
M_GC_GET_STREAMABLE_FEATURES_SIZE = 5497558146592
M_GC_INTERFACE_NAME_SIZE = 5497558146740
M_GC_IP_ADDRESS_STRING_SIZE = 5497558146593
M_GC_MAC_ADDRESS_STRING_SIZE = 5497558146594
M_GC_MESSAGE_CHANNEL_MULTICAST_ADDRESS_STRING_SIZE = 5497558146598
M_GC_NIC_IP_ADDRESS_STRING_SIZE = 5497558146595
M_GC_NIC_MAC_ADDRESS_STRING_SIZE = 5497558146596
M_GC_PIXEL_FORMAT_STRING_SIZE = 5497558146758
M_GC_SERIAL_NUMBER_SIZE = 5497558146588
M_GC_SPECIFIC_INFO_SIZE = 5497558146586
M_GC_STREAM_CHANNEL_MULTICAST_ADDRESS_STRING_SIZE = 5497558146597
M_GC_TRIGGER_SELECTOR_SIZE = 5497558146594
M_GC_UNIQUE_ID_STRING_SIZE = 5497558146594
M_GC_USER_NAME_SIZE = 5497558146587
M_GC_VERSION_SIZE = 5497558146585
M_GC_XML_PATH_SIZE = 5497558146741
M_GENERAL_FERET = 1024
M_GENERAL_FERET_ANGLE = 62
M_GENERAL_MOMENT = 2048
M_GPU_TYPE_SIZE = 5497558146580
M_GRADE_RESULT_OFFSET = 10
M_GRID_CORNER_HINT_X = 162
M_GRID_CORNER_HINT_Y = 163
M_GS1_RAW_DATA = 148
M_IMAGE_ID_FAILED = 2574
M_IMAGE_ID_PASSED = 2573
M_IMAGE_INDEX_FAILED = 2582
M_IMAGE_INDEX_PASSED = 2581
M_INCLUDED_EDGE = 4194304
M_KEY_SUBSTRACT = 109
M_LINE_ANGLE = 2048
M_LINE_PARAM_A = 12288
M_LINE_PARAM_B = 12289
M_LINE_PARAM_C = 12290
M_LOCAL_FRAME_ANGLE = 2048
M_LOCAL_FRAME_POSITION_X = 13312
M_LOCAL_FRAME_POSITION_Y = 17408
M_MAX_MIN_DISTANCE_POINT = 67
M_MAX_NUMBER_OF_CLASS_DEFINITIONS = 2946
M_MAX_NUMBER_OF_CLASS_DESCRIPTIONS = 2946
M_MET_GEOMETRY = 4831838212
M_MIN_SPACING_X = 35
M_MIN_SPACING_Y = 36
M_MODEL_INDEX = 21504
M_NEIGHBOR_DIRECTION_TOLERANCE = 2048
M_NETWORK_ADDRESS_SIZE = 5497558146584
M_NOPEL = 8389633
M_NO_INVALID_POINT = 67108864
M_NUMBER_FAIL = 2572
M_NUMBER_OF_CLASS_DEFINITIONS = 2848
M_NUMBER_OF_CONSTRUCTION_FEATURE_INDEX = 1013
M_NUMBER_OF_CONSTRUCTION_FEATURE_LABEL = 1012
M_NUMBER_OF_DATA = 1009
M_NUMBER_OF_EDGELS = 1009
M_NUMBER_OF_ELEMENTS = 2
M_NUMBER_OF_FEATURE_FAIL = 1103
M_NUMBER_OF_OCCURRENCES = 18
M_NUMBER_OF_SCANS_PER_ROW = 45057
M_NUMBER_OF_VERTEX = 73
M_NUMBER_OF_VERTEXES = 73
M_NUMBER_PASS = 2571
M_PLANE_INTERSECTION = 1
M_POINT_ANGLE = 2048
M_POINT_CLOUD_CONTAINER = 1903
M_POINT_CLOUD_CONTAINER_3DMAP = 144
M_POINT_POSITION_X = 13312
M_POINT_POSITION_Y = 17408
M_POSITION_UNCERTAINTY_X = 11
M_POSITION_UNCERTAINTY_Y = 12
M_PREDEFINED_CONVOLUTIONAL_NETWORK = 2913
M_PRETRAINED_CONVOLUTIONAL_NETWORK = 2913
M_PRODUCT_MODEL_SIZE = 5497558146590
M_PRODUCT_SENSOR_SIZE = 5497558146591
M_REGION_POSITION_END = 1778
M_REGION_POSITION_END_TYPE = 1780
M_REGION_POSITION_END_X = 220
M_REGION_POSITION_END_Y = 221
M_REGION_POSITION_START = 1777
M_REGION_POSITION_START_TYPE = 1779
M_REGION_POSITION_START_X = 218
M_REGION_POSITION_START_Y = 219
M_RESULT_ALIGNMENT_3DMAP = 176
M_SAME_EDGE = 67
M_SAMPLE_IMAGE_ID = 2907
M_SCRIPT_REFERENCE_SIZE = 5497558139392
M_SEGMENT_ANGLE = 2048
M_SEGMENT_COVERAGE = 216
M_SEGMENT_END_X = 13314
M_SEGMENT_END_Y = 17410
M_SEGMENT_LENGTH = 8192
M_SEGMENT_START_X = 9
M_SEGMENT_START_Y = 10
M_SERIAL_NUMBER_SIZE = 5497558146583
M_STREAM_FILE_NAME_SIZE = 5497558142784
M_SYSTEM_DESCRIPTOR_SIZE = 5497558146581
M_SYSTEM_PRINT_NAME_SIZE = 5497558146589
M_SYSTEM_TYPE_STRING_SIZE = 5497558146585
M_THRESHOLD_VALUES = 3003
M_TOLERANCE_LABEL_VALUE = 1
M_TRANSPORT_PROTOCOL_SIZE = 5497558146586
M_TYPE_ANGLE = 8
M_TYPE_MIL_ANGLE = 4
M_USER_NAME_SIZE = 5497558146592
M_VERTEX = 108
M_VERTEX_X = 68
M_VERTEX_Y = 40
M_WINDOW_TITLE_NAME = 7702
M_WINDOW_TITLE_NAME_SIZE = 5497558146582
M_WRITE_CELL_NUMBER_X = 32789
M_WRITE_CELL_NUMBER_Y = 32790
M_Y_AXIS_DOWN = 32
M_Y_AXIS_UP = 16

