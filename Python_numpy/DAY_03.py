# data type
import numpy as np
arr = np.array([2,3,4,5])
print(arr)
print(arr.dtype)

#dtype='i8' → means integer of 8 bytes (64-bit integer).

a1 =np.array([1,2,3,4,5],dtype='i8')
print(a1)
print(a1.dtype)

#arr = np.array(['a', '2', '3'], dtype='i')
# ValueError: invalid literal for int() with base 10: 'a'

# astype('i') → converts float to integer (decimal part removed, not rounded)

arr = np.array([1.1, 2.1, 3.1])
print(arr)
print(arr.dtype)

newarr = arr.astype(bool)
print("new array:", newarr)
print("new array datatype:", newarr.dtype)
'''
# | Question                                                   | Short Answer                                               |
| ---------------------------------------------------------- | ---------------------------------------------------------- |
| What is dtype in NumPy?                                    | It defines the data type of array elements.                |
| How is NumPy faster than lists?                            | Because arrays use fixed-size typed memory blocks (dtype). |
| What happens if you give a non-convertible value to dtype? | It raises a `ValueError`.                                  |
| How to convert a float array to integer?                   | Using `.astype(int)` method.                               |
| Difference between `'i4'` and `'i8'`?                      | `'i4'` → 4 bytes (32-bit), `'i8'` → 8 bytes (64-bit).      |
'''
# copy and view
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()

arr[0] = 42
print(arr)  # [42  2  3  4  5]
print(x)    # [1  2  3  4  5]


import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()

arr[0] = 42
print(arr)  # [42  2  3  4  5]
print(x)    # [42  2  3  4  5]
# True → it’s a view (shares data)
# False → it’s a copy (independent)

print(x.base is arr)


arr = np.array([10, 20, 30])
x = arr.view()
y = arr.copy()

arr[1] = 99

print("arr:", arr)  # [10 99 30]
print("x:", x)      # [10 99 30]  (view changes)
print("y:", y)      # [10 20 30]  (copy stays same)

'''| Question                                                    | Short Answer                                                 |
| ----------------------------------------------------------- | ------------------------------------------------------------ |
| What is the difference between `copy()` and `view()`?       | `copy()` creates a new array, `view()` shares the same data. |
| If you modify the original array, will `copy()` reflect it? | No.                                                          |
| If you modify the original array, will `view()` reflect it? | Yes.                                                         |
| How to check if an array owns its data?                     | `arr.base is None` → means it owns the data (not a view).    |
| Which uses less memory?                                     | `view()`                                                     |
'''