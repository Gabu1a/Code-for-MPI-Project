import random
import time


def bubbleSort(array):
    for iter_num in range(len(array) - 1, 0, -1):
        for idx in range(iter_num):
            if array[idx] > array[idx + 1]:
                temp = array[idx]
                array[idx] = array[idx + 1]
                array[idx + 1] = temp


def insertionSort(array):
    if (n := len(array)) <= 1:
        return
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def selectionSort(array):
    for idx in range(len(array)):
        min_idx = idx
        for j in range(idx + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[idx], array[min_idx] = array[min_idx], array[idx]


def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        sub_array1 = array[:mid]
        sub_array2 = array[mid:]
        mergeSort(sub_array1)
        mergeSort(sub_array2)
        i = j = k = 0
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                array[k] = sub_array1[i]
                i += 1
            else:
                array[k] = sub_array2[j]
                j += 1
            k += 1
        while i < len(sub_array1):
            array[k] = sub_array1[i]
            i += 1
            k += 1
        while j < len(sub_array2):
            array[k] = sub_array2[j]
            j += 1
            k += 1


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def heapSort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        (array[i], array[0]) = (array[0], array[i])  # swap
        heapify(array, i, 0)


def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    if largest != i:
        (array[i], array[largest]) = (array[largest], array[i])  # swap
        heapify(array, n, largest)


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]

# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10

def bucketSort(array):
    # Determine the range of input values
    min_value = min(array)
    max_value = max(array)

    # Determine the size of each bucket
    bucket_size = (max_value - min_value) // 10 + 1

    # Create empty buckets
    buckets = [[] for _ in range(10)]

    # Distribute elements into buckets based on their value
    for value in array:
        bucket_index = (value - min_value) // bucket_size
        buckets[bucket_index].append(value)

    # Sort each bucket and concatenate them into a sorted list
    sorted_list = []
    for bucket in buckets:
        sorted_list.extend(sorted(bucket))

### List containing runtimes
runtime = []

### CHOOSE THE SIZE OF THE LIST
size = 500000

### CHOOSE THE NUMBER OF REPETITIONS
repetitions = 4

for i in range(-1, repetitions):
    # List containing the elements
    list = []

    ### CHOOSE LIST TYPE BY DELETING “#”

    #list = random.sample(range(0, size), size) # randomly generated list
    #for i in range(size): list.append(i) # to find the best case
    #for i in range(size - 1, -1, -1): list.append(i) # to find the worst case

    Time = time.time()

    ### CHOOSE SORT TYPE BY DELETING “#”

    #bubbleSort(list)
    #selectionSort(list)
    #insertionSort(list)
    #mergeSort(list)
    #heapSort(list)
    #quickSort(list, 0, size - 1)
    #radixSort(list)
    #bucketSort(list)

    Time = round(time.time() - Time, 2)
    print("Runtime:", Time, "seconds")
    runtime.append(Time)

    ### HERE YOU CAN INCREASE THE LIST SIZE FOR EACH CYCLE
    #size += 500000

print(runtime)
#print("Average:", round(sum(runtime) / len(runtime), 2))
#print("Minimum:", min(runtime))
#print("Maximum:", max(runtime))