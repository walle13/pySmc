# import os
# for root, dirs, files in os.walk('.'):
#     for file in files:
#         if file.endswith('.ui'):
#             os.system('pyuic4 -o %s.py -x %s' \
#                       % (file.rsplit('.', 1)[0], file))
#         elif file.endswith('.qrc'):
#          os.system('pyrcc4 -o %s_rc.py %s' \
#                       % (file.rsplit('.', 1)[0], file))
#传入数组的例子
from ctypes import *
cdll.LoadLibrary("libc.so.6") # doctest: +LINUX
libc = CDLL("libc.so.6")     #
IntArray5 = c_int * 5
ia = IntArray5(5, 1, 7, 33, 99)
qsort = libc.qsort
qsort.restype = None
CMPFUNC = CFUNCTYPE(c_int, POINTER(c_int), POINTER(c_int))
def py_cmp_func(a, b):
     print "py_cmp_func", a[0], b[0]
     return a[0] - b[0]
cmp_func = CMPFUNC(py_cmp_func)
qsort(ia, len(ia), sizeof(c_int), cmp_func)
for i in ia: print i,
