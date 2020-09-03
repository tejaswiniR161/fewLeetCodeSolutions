#pushing the heaviest element to the end in every iteration
# time complexity is O(n*n)

array=input("Enter the numbers to sort them, enter space sepearted integers")
array=array.split(" ")
#for some reason remember this so, if you use list(array) it'll split even the spaces so spaces will also be in the result, like you saw that coming didn't you!
#print(array)
array=[int(i) for i in array]

def bubblesort(array):
    for i in range(len(array)-1):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

print(bubblesort(array))