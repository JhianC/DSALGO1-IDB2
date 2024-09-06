#1. Bubble Sort Algorithm (ASC)
arr1=[23, 89, 7, 56, 44]
print("#1. Array before Bubble Sort(ASC)")
print(arr1)
for i in range(0, len(arr1)):
    for j in range(0, len(arr1)-i-1):
        if arr1[j] > arr1[j+1]:
            arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
print("Array 1 after Bubble Sort(ASC)")
print(arr1)
print()

#2. Insertion Sort Algorithm (ASC)
arr2=[12, 78, 91, 34, 62]
print("#2. Array 2 Before Insertion Sort(ASC)")
print(arr2)
for i in range(1, len(arr2)):
    key = arr2[i]
    j = i-1
    while j >= 0 and key < arr2[j]:
        arr2[j+1]=arr2[j]
        j-=1
    arr2[j+1] = key
print("Array 2 After Insertion Sort(ASC)")
print(arr2)
print()

#3. Selection Sort Algorithm (DSC)
arr3=[5, 99, 48, 15, 67]
print("#3. Array 3 Before Selection Sort(DSC)")
print(arr3)
for i in range(len(arr2)):
    min_idx=i
    for j in range(i+1, len(arr3)):
        if arr3[min_idx] < arr3[j]:
            min_idx = j
    arr3[i],arr3[min_idx] = arr3[min_idx],arr3[i]
print("Array 3 Values After Selection Sort")
print(arr3)
print()

#4. Insertion Sort Algorithm (DSC)
arr4=[38, 82, 25, 74, 13]
print("#4. Array 4 Before Insertion Sort(DSC)")
print(arr4)
for i in range(1, len(arr4)):
    key = arr4[i]
    j = i-1
    while j >= 0 and key > arr4[j]:
        arr4[j+1]=arr4[j]
        j-=1
    arr4[j+1] = key
print("Array 4 After Insertion Sort(DSC)")
print(arr4)
print()

#5. Ascending and Descending Order of values from index 2 and 3 in the previous data sets
arrA=[44, 56, 62, 78, 48, 15, 38, 25]
arrB=[44, 56, 62, 78, 48, 15, 38, 25]
print("#5. Arrays before being sorted in Ascending & Descending Order")
print(arrA)
for i in range(1, len(arrA)):
    key = arrA[i]
    j = i-1
    while j >= 0 and key < arrA[j]:
        arrA[j+1]=arrA[j]
        j-=1
    arrA[j+1] = key
print("Array After being sorted using Insertion Sort(ASC)")
print(arrA)
for i in range(1, len(arrB)):
    key = arrB[i]
    j = i-1
    while j >= 0 and key > arrB[j]:
        arrB[j+1]=arrB[j]
        j-=1
    arrB[j+1] = key
print("Array After being sorted using Insertion Sort(DSC)")
print(arrB)
print()

#6. Ascending & Descending order for all the values from 1-4 using Selection Sort
arrAll=[23, 89, 7, 56, 44, 12, 78, 91, 34, 62, 5, 99, 48, 15, 67, 38, 82, 25, 74, 13]
print("#6. Array for all values from 1-3 (Unsorted)")
print(arrAll)
for i in range(len(arrAll)):
    min_idx=i
    for j in range(i+1, len(arrAll)):
        if arrAll[min_idx] > arrAll[j]:
            min_idx = j
    arrAll[i],arrAll[min_idx] = arrAll[min_idx],arrAll[i]
print("Array after being sorted to Ascending")
print(arrAll)
for i in range(len(arrAll)):
    min_idx=i
    for j in range(i+1, len(arrAll)):
        if arrAll[min_idx] < arrAll[j]:
            min_idx = j
    arrAll[i],arrAll[min_idx] = arrAll[min_idx],arrAll[i]
print("Array after being sorted to Descending")
print(arrAll)
print()

#7. Printing Even and Odd values of the array of number 6
arrnum6=[23, 89, 7, 56, 44, 12, 78, 91, 34, 62, 5, 99, 48, 15, 67, 38, 82, 25, 74, 13]
print("7. Even and Odd values of the array of number 6")
print("Base Array:")
print(arrnum6)
oddnums=[num for num in arrnum6 if num % 2==0]
evennums=[num for num in arrnum6 if num % 2 != 0]
print("Odd Numbers:", oddnums)
print("Even Numbers:", evennums)
