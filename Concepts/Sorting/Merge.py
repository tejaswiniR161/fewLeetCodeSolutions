#Merge sort uses the divide and conquer technique

#time complexity is O(nlogn)
#space however is 

array=input("Enter the numbers to sort them, enter space sepearted integers")
array=array.split(" ")
#for some reason remember this so, if you use list(array) it'll split even the spaces so spaces will also be in the result, like you saw that coming didn't you!
#print(array)
array=[int(i) for i in array]
#print(array)

def mergesort(array):
    if len(array)>1:
        mid=len(array)//2 # // for floor division
        left=array[:mid]
        print("Split left", left,end='')
        right=array[mid:]
        print("Split right", right,end='')
        left=mergesort(left)
        #print("All the ones on the left until the end : ",left,end='')
        right=mergesort(right)
        #print("All the ones on the right until the end : ",right,end='')

        array=[]
        #print("Here")
        while len(left)>0 and len(right)>0:
            #print("here")
            if left[0]<=right[0]:
                array.append(left[0])
                left.pop(0)
            else:
                array.append(right[0])
                right.pop(0)
        
        for j in left:
            array.append(j)
        for j in right:
            array.append(j)
    
    return array

print(mergesort(array))