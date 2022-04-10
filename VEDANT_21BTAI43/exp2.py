cordinate = (input("Enter coordinates of x1, x2, y1, y2")).split()
x1=int(cordinate[0])
x2=int(cordinate[1])
y1=int(cordinate[2])
y2=int(cordinate[3])
a=(x2-x1)**2
b=(y2-y1)**2
dist=(a+b)**.5
print(" Thew required distance between two points is: ",round(dist,3))
