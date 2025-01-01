#E-books Numpy: https://agoraprogramacion.gumroad.com/
import numpy as np
print(np.__version__)

array_3d_1 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])

array_3d_2 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])

array_3d_3 = np.concatenate((array_3d_1, array_3d_2))
#print(array_3d_3)
#print(np.where(array_3d_3 == 27))
print(np.sort(array_3d_3))

'''array_3d_3 = np.array_split(array_3d_3, 6)
for matrix in array_3d_3:
    print(matrix)

for matrix in array_3d:
    for row in matrix:
        for column in row:
            print(column)

print(array_3d.ndim)
print(array_3d.shape)
print(array_3d[2, 2, 2])

array_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8] ])
print(array_2d)

array_2d = array_2d.reshape(4, 2)
print(array_2d)'''

#https://www.youtube.com/watch?v=yhKW4XsXa5c&list=PLbi7Cp2PebjaW1eYFXklBWyouayV6EH3R&index=2