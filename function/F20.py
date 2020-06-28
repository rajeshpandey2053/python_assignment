def interSection(arr1,arr2): 
     result = list(filter(lambda x: x in arr1, arr2))  
     print ("Intersection : ",result) 
  
# Driver program 
arr1 = []
no = int(input("Enter how many numbers in first list: "))
for _ in range(no):
    arr1.append(int(input("Enter item: ")))

arr2 = []
noo = int(input("Enter how many numbers in second list: "))
for _ in range(noo):
    arr2.append(int(input("Enter item: ")))
   

interSection(arr1,arr2) 