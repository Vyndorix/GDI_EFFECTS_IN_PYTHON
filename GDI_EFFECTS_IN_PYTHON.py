before hand:
from win32api import *
from win32con import *
from win32gui import *
import numpy as np
import numba
from numba import *

#or 

from winapy_gdi import *
from winapy_con import *
from winapy_user import *
import numba
import numpy as np
from numba import *

#pip install pywin32

#pip install winapy **needs c++ build tools**

#:starting script:

from win32api import *
from win32con import *#winapy is only for some functions use pywin32 for the normal gdi 
from win32gui import *

from win32api import *
from win32con import *
from win32gui import *
import numba
import numpy as np
from numba import *

w = GetSystemMetrics(SM_CXSCREEN)
h = GetSystemMetrics(SM_CYSCREEN)
x,y = GetSytemMetrics(0),GetSystemMetrics(1)

hdc = GetDC(0)
#----------------------------------------------


Bitblt:
for i in range(100):
    BitBlt(hdc, 1, 1, sw, sh, hdc, 0, 0, SRCCOPY)

#---------------------------------------


#Stretchblt:

for i in range(100):
    StretchBlt(hdc, 50, 50, x - 100, y - 100, HDC, 0, 0, x, y, SRCCOPY)
    #                                                            ^ you can change this to a few things like SRCCOPY, NOTSRCCOPY, SRCINVERT, SRCAND, SRCERASE, NOTSRCERASE, and SRCPAINT you can also do it to bitblt and plgblt
#---------------------------------------


#Patblt:

for i in range(100):
    brush = CreateSolidBrush(RGB(

        randrange(255), randrange(255), randrange(255)
        #         ^red             ^green          ^blue  | 255 is the max put it higher or lower depending how strong you want the color to be

    ))
    SelectObject(hdc, brush)
    PatBlt(hdc, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
    #                                                                      ^you can also change this to PATCOPY

#or 


for i in range(100):
    brush = CreateSolidBrush(RGB(

        randrange(255), randrange(255), randrange(255)

    ))
    SelectObject(hdc, brush)
    PatBlt(desk, x2, y2, x_2, y_2, PATINVERT)
    x2 += 9999
    y2 += 9999#edit these values
    x_2 -= 9999
    y_2 -= 9999
    

#----------------------------------------------------

Plgblt:

points = ((60, 60), (x, -99), (50, y))#change this it does weird stuff
for i in range(100):
    PlgBlt(hdc, points, hdc, 0, 0, x, y, None, 0, 0)

#-------------------------------------------------------

Pie:
for i in range(200000):
    brush = CreateSolidBrush(RGB(

        randrange(255), randrange(255), randrange(255)

    ))
    SelectObject(hdc, brush)
    Pie(hdc, randrange(1,x),randrange(1,y),randrange(1,x),randrange(1,y), randrange(1,x),randrange(1,y), randrange(1,x),randrange(1,y) )
#-----------------------------------------------------------------

#Shaders:

@numba.njit(parallel=True)
def shader(arr, w, h, i):
    for x in numba.prange(w):
        for y in range(h):
            #edit this   [______↓↓_______] right now its on a scrolling xor thing
            arr[x, y, 0] = x ^ y + i * 10
            #         ^ you can also change this to 1, 2, or 3 or 0 I cant remember I just know it changes the color
    return arr


for i in range(100):
    SelectObject(dcMem, bmp)
    BitBlt(dcMem, 0, 0, w, h, hdc, 0, 0, SRCINVERT)

    buf = GetBitmapBits(bmp, True)


    arr_f = np.frombuffer(buf, dtype=np.uint8)
    arr = np.array(arr_f)


    bs = arr.shape

    arr.shape = (h, w, 4)

    shader(arr,h,w,i)


    arr.shape = bs
    SetBitmapBits(bmp, arr.tobytes())

    BitBlt(hdc, 0, 0, w, h, dcMem, 0, 0, SRCCOPY)
    
#k now you read all of this and now you know how to make gdi effects in python star this repository because where else would you have learnt this?
    
    
