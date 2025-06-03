import numpy as np 
# the basics
a=np.array([1,2,3], dtype='int32')
print(a)
# creating a 2D array
b=np.array([[1.0,2.0,3.0],[4.0,5.0,6.0]])
print(b)
#get dimensions of the array
print(a.ndim)
print(b.ndim)
# get shape of the array
print(a.shape)
print(b.shape)
#get the size of the array
print(a.size)
print(b.size)
# get the data type of the array
print(a.dtype)
print(b.dtype)
# get the item size of the array
print(a.itemsize)
print(b.itemsize)
# get the total size of the array
print(a.nbytes)
print(b.nbytes)
#get a sprecific element from the array
print(a[0])
print(b[0,1])
print(b[1,-3])#from the 2nd row the last coulym index is -1 then in left -2 and go on
# get a specific row from the array
print(b[0,:])#first row
print(b[1,:])#second row
# get a specific column from the array
print(b[:,0])#first column
print(b[:,2])#third column
# getting a little fancy
print(b[0,0:-1:1])#from first row get the first element to the last element with step of 1
# getting a little fancier
a[0]=5#change the first element of a to 5
print(a)
b[1,2]=10#change the second row and third column to 10
print(b)
b[:,2]=[1,2]#change the third column to 1 and 2
print(b)
# 3D array
c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)
# get a specific element from the 3D array(work outside in method)
print(c[0,1,1])#first 2D array, second row, second column
print(c[:,1,:])#all 2D arrays, second row, all columns
#replace
c[:,1,:]=[[10,20],[30,40]]#replace the second row of all 2D arrays with 10,20 and 30,40
print(c)
#initializing different types of arrays
#all zeros
d=np.zeros((2,3))#2 rows and 3 columns
print(d)
e=np.zeros((2,3,3,2))#2 3D arrays with 3 rows and 3 columns
print(e)
# all ones
f=np.ones((4,2,2))#4 2D arrays with 2 rows and 2 columns
print(f)
# all other numbers
g=np.full((4,2,2),5, dtype='float32')#4 2D arrays with 2 rows and 2 columns filled with 5
print(g)
#Any other number(full_like)
h=np.full_like(b,4) #b is the shape of the array
print(h)
# random decimal numbers
i=np.random.rand(4,3) #2 rows and 3 columns with random decimal numbers
print(i)
# random integer numbers
j=np.random.randint(0,99,size=(4,2)) #4 rows and 2 columns with random integer numbers between 0 and 99(exclusive)
print(j)
#identical array
k=np.identity(3) #3x3 identity matrix
print(k)
# repeat an array
l=np.repeat(a,3) #repeat array a 3 times
print(l)
#repeating with rows
m=np.repeat(a,3,axis=0) #repeat array a 3 times along the rows
print(m)
#replcing one matrix with another
output=np.ones((5,5)) #5x5 array with all ones
z=np.full((3,3),9) #3x3 array with all 9s
output[1:4,1:4]=z #replace the middle 3x3 array with 9s
print(output)
#copying matrices
q=b.copy() #copy array b to q
print(q)
#never use b=q because it will create a reference to the same array and make the same changes to both arrays
#mathematical operations
print(a + 2) #add 2 to each element of a
print(b * 2) #multiply each element of b by 2
print(b - 1) #subtract 1 from each element of b
print(b / 2) #divide each element of b by 2
print(np.sqrt(b)) #square root of each element of b
print(np.exp(b)) #exponential of each element of b
print(np.log(b)) #natural logarithm of each element of b
print(np.sin(b)) #sine of each element of b
print(np.cos(b)) #cosine of each element of b
print(np.tan(b)) #tangent of each element of b
x=a.copy() #copy array a to x
x=np.full_like(x, 2) #replace all elements of x with 2
print(x)
print(a + x) #add x to a
print(np.add(a, x)) #add a and x using numpy add function
print(np.subtract(a, x)) #subtract x from a
print(np.multiply(a, x)) #multiply a and x
print(np.divide(a, x)) #divide a and x
print(np.power(a, x)) #raise a to the power of x
print(np.mod(a, x)) #modulus of a and x
print(np.dot(a, x)) #dot product of a and x
print(a)
# Linear algebra
y=np.identity(3) #3x3 identity matrix
z=np.full((3,2),2) #3x2 array with all 2s
print(np.matmul(y, z)) #matrix multiplication of y and z
# Transpose
print(y.T) #transpose of y
# Find the determinant of a matrix
print(np.linalg.det(y)) #determinant of y
# Find the inverse of a matrix
print(np.linalg.inv(y)) #inverse of y -> this will raise an error because y is not invertible (determinant is 0)
# Find the eigenvalues and eigenvectors of a matrix
eigenvalues, eigenvectors = np.linalg.eig(y) #eigenvalues and eigenvectors of y
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
# Find the rank of a matrix
print(np.linalg.matrix_rank(y)) #rank of y
# Find the trace of a matrix
print(np.trace(y)) #trace of y
# Find the condition number of a matrix
print(np.linalg.cond(y)) #condition number of y
#Statistics
print(np.mean(b)) #mean of b
print(np.median(b)) #median of b
print(np.std(b)) #standard deviation of b
print(np.var(b)) #variance of b
print(np.min(b)) #minimum of b
print(np.max(b)) #maximum of b
print(np.max(b, axis=0)) #maximum of b along the rows
print(np.max(b, axis=1)) #maximum of b along the columns
#reshaping arrays
print(b.reshape(3,2)) #reshape b to 3 rows and 2 columns
print(b.reshape(2,3)) #reshape b to 2 rows and 3 columns
print(b.reshape(6,1)) #reshape b to 6 rows and 1 column
#vertical stacking
v=np.vstack((a,b,b,a)) #stack a and b vertically and repeat b and a
print(v)
#horizontal stacking
#h=np.hstack((a,b)) #stack a and b horizontally
#size is mismatched so it will raise an error
h1=np.ones((2,4))
h2=np.zeros((2,2))
print(np.hstack((h2,h1)))
#h=np.hstack((h1,h2)) #this will raise an error because the number of rows is not the same
#indexing and advanced slicing
print(b[0:2, 0:2]) #get the first two rows and first two columns of b
print(b[0:2, 1:3]) #get the first two rows and second and third columns of b
print(b[[0,1]])#get the first and second rows of b
print(b[0:2, 1:3])#get the first two rows and second and third columns of b
print(b[[0,1],[0,1]])#get the first and second elements of the first and second rows of b
print(b)