n Mon, Sep 22, 2014 at 12:34 AM, Koteswara Rao Ruvva <ruvva@...> wrote:
> I have the following getData function in a DLL that allocates memory and
> fill its contents.
>
> extern "C" __declspec(dllexport) int getData(int *data) {
>     int size = 20;
>     data = (int*) malloc(size*sizeof(int));
>
>     for (int i = 0; i < size; i++) {
>         data[i] = i*i;
>     }
>
>     return size;
> }
>
> I have the following Python code to call the getData function:
>
>        mydll = ctypes.cdll.LoadLibrary('MathFuncs.dll')
>
>        mydll.getData.argtypes = [ctypes.POINTER(ctypes.c_int)]
>        mydll.getData.restype  = ctypes.c_int
>
>        data = ctypes.POINTER(ctypes.c_int)
>        size = mydll.getData(ctypes.POINTER(data))
>
> When I execute, I get the following error:
> ctypes.ArgumentError: argument 1: <type 'exceptions.TypeError'>: expected
> LP_c_long instance instead of _ctypes.PyCPointerType
>
> I am not able to figure out the mistake. Could someone please correct me.

POINTER returns a pointer type that can be set in a function's
argtypes. Subsequently calling the function requires that the
corresponding argument is an instance of the type. So the immediate
problem here is that `data` needs to be an instance of the pointer
type.

That said, don't pass the pointer by value (initially NULL). Instead
pass by reference in order to receive the address of the malloc'd
buffer. For example:

// mathfuncs.cpp

#include <stdlib.h>

// The data paramater has to be a pointer to a pointer, i.e.
// an int **. The address of the malloc'd buffer gets stored
// to the caller's pointer, i.e. *data.

extern "C" __declspec(dllexport) int getData(int **data) {
    int size = 20;
    int *arr = (int *)malloc(size * sizeof(int));
    for (int i = 0; i < size; i++)
        arr[i] = i*i;
    *data = arr;
    return size;
}


# test_mathfuncs.py

import ctypes

# Use CDLL instead of cdll.LoadLibrary. Windows appends the .dll
# extension for you.
mydll = ctypes.CDLL('mathfuncs')

c_int_p = ctypes.POINTER(ctypes.c_int)
c_int_pp = ctypes.POINTER(c_int_p)

mydll.getData.argtypes = [c_int_pp]
mydll.getData.restype  = ctypes.c_int

# Instantiate an int * pointer.
data = c_int_p()

# Use byref to pass the address of the pointer.
size = mydll.getData(ctypes.byref(data))

print("data.contents is", data.contents)
# data.contents is c_long(0)

print("size ==", size)
# size == 20

print("data[size-1] ==", data[size-1])
# data[size-1] == 361

print("data[:3] ==", data[:3])
# data[:3] == [0, 1, 4]

# Casting the result to an array requires
# a pointer cast to int (*)[size]; then
# a pointer dereference.
# typedefs
array_t = ctypes.c_int * size
array_t_p = ctypes.POINTER(array_t)
# pointer cast
p_data_array = ctypes.cast(data, array_t_p)
# pointer dereference
data_array = p_data_array.contents

# array_t is an aggregate type consisting of 20 elements
# that are each 4 bytes.

print("sizeof(data_array) ==",  ctypes.sizeof(data_array))
print("len(data_array) ==", len(data_array))
# sizeof(data_array) == 80
# len(data_array) == 20
