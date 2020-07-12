def bubbleSort(arr):
    a = len(arr)

    for m in range(a-1):

        for n in range(0, a-m-1):

            if arr[n] > arr[n+1]:
                arr[n], arr[n+1] = arr[n+1], arr[n]


arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Implementing Bubble Sort")
for m in range(len(arr)):
    print("%d" % arr[m]),
