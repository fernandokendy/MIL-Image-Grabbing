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
# Copyright © Matrox Electronic Systems Ltd., 1992-2021.
# All Rights Reserved
##########################################################################

import ctypes
if ctypes.sizeof(ctypes.c_voidp) > 4:
   from mil64 import *
else:
   from mil32 import *