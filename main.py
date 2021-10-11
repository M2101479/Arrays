import array as arr
from collections import Counter
a=arr.array("i",[2,4,6,8])
print("First element",a[0])
print("second element",a[1])
print("third element",a[2])

arr =list(a)
print("Before reversal Array is :",arr)
 
arr.reverse() #reversing using reverse()
print("After reversing Array:",arr)

double=(arr)+(arr)
number=dict(Counter(double))
print(number)

arr.remove(8)
print(arr)

index=2
arr.pop(index)
print(arr)

print(a.buffer_info())
