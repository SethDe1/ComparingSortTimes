# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:18:47 2022

@author: Seth DeWalt, Paul Blomgren, Walker Bowden
This program will test the times of different types of sort functions
"""
import time
import sys
import random as rd

#File path
path = r"D:\UCA Spring 2022\Algorithms\P2Write.txt"

#opening file that will append data
f = open(path, "a")

def main():
    #variable for while
    repeat = "y"
    
    # creating while loop for program to repeat
    while repeat == "Y " or repeat == "y":

        #Prompting for data's Size
        arraySize = int(input("Please enter the size of the Data Set: "))
        
        #generate array based on size
        array = genArray(arraySize)
        print("Array has been generated.\n")
        
        #Prompting user for choice of sort
        print("Enter one of the following letters for each sort:")
        print("q - Quick sort, b - Bubble, m - Merge, h - Heap")
        choice = input("Please choose the Sorting Algorithm you would like to test: ")
        
        #if else block based on user choice
        if choice == 'q' or choice == 'Q':
            #run quick sort with the randomized array
            doQuickSort(array, arraySize)
            
        elif choice == 'b' or choice == 'B':
            #run bubble sort with the randomized array
            doBubbleSort(array)
            
        elif choice == 'm' or choice == 'M':
            #run merge sort with the randomized array
            doMergeSort(array)
            
        elif choice == 'h' or choice == 'H':
            #run heap sort with the randomized array
            doHeapSort(array)

        # asking to repeat program
        repeat = input("Do you want to generate a new data set? Y or N\n")

    # ending program
    sys.exit("Program Finished")

#creating randomized array
def genArray(arraySize):
    #generating randomized array 
    array = [rd.randint(1, 2 * arraySize) for i in range(arraySize)]
    
    return array

# running quick sort and printing
def doQuickSort(data, arraySize):
    #printing to console and writing to file
    print("\nQuick Sort")
    f.write("Quick Sort\n")
    
    #starting timer
    runtime = time.time()
    quickSort(data, 0, arraySize - 1)
    
    #printing to console and writing to file
    print("%s seconds" % (time.time() - runtime))
    f.write("%s seconds\n" % (time.time() - runtime))


# Bubble Sort
def doBubbleSort(data):
    #printing to console and writing to file
    print("\nBubble Sort")
    f.write("Bubble Sort\n")
    
    #starting timer
    runtime = time.time()
    #running the bubble sort function
    bubbleSort(data)
    
    #printing to console and writing to file
    f.write("%s seconds \n" % (time.time() - runtime))
    print("%s seconds " % (time.time() - runtime))


# Merge Sort
def doMergeSort(data):
    #printing to console and writing to file
    print("\nMerge Sort")
    f.write("Merge Sort\n")
    
    #starting timer
    runTime = time.time()
    #running the merge sort function
    mergeSort(data)
    
    #printing to console and writing to file
    f.write("%s seconds \n" % (time.time() - runTime))
    print("%s seconds " % (time.time() - runTime))


#Heap Sort
def doHeapSort(data):
    #printing to console and writing to file
    print("\nHeap Sort")
    f.write("Heap Sort\n")
    
    #starting timer
    runTime = time.time()
    #running the Heap sort function
    heapSort(data)
    
    #printing to console and writing to file
    f.write("%s seconds \n" % (time.time() - runTime))
    print("%s seconds " % (time.time() - runTime))


# Function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements and compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1


# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # recursive call on the left of pivot
        quickSort(array, low, pi - 1)

        # recursive call on the right of pivot
        quickSort(array, pi + 1, high)


def bubbleSort(data):  # Bubble Sort Algorithm
    sorted = False
    #for loop to step through each element
    for i in range(len(data) - 1):
        swap = False
        if not sorted:
            #comparison loop
            for j in range(len(data) - i - 1):
                #if element is greater than next switch
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    swap = True
                    if not swap:
                        sorted = True
                        break
    return data


def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # The value from the left half has been used
                myList[k] = left[i]
                # Move the iterator forward
                i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)


# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


main()
f.close()
