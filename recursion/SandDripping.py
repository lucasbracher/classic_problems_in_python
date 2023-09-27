"""
SandDripping.py

Emulates the accumulation of sand grains in a container.
Usage:

> python SandDripping.py
<length of the container> <zero-based position in container> <number of grains>

Example:
> python SandDripping.py
7 3 20
[0, 0, 0, 1, 0, 0, 0]
[0, 0, 1, 1, 0, 0, 0]
[0, 0, 1, 1, 1, 0, 0]
[0, 0, 1, 2, 1, 0, 0]
[0, 1, 1, 2, 1, 0, 0]
[0, 1, 2, 2, 1, 0, 0]
[0, 1, 2, 2, 1, 1, 0]
[0, 1, 2, 2, 2, 1, 0]
[0, 1, 2, 3, 2, 1, 0]
[1, 1, 2, 3, 2, 1, 0]
[1, 2, 2, 3, 2, 1, 0]
[1, 2, 3, 3, 2, 1, 0]
[1, 2, 3, 3, 2, 1, 1]
[1, 2, 3, 3, 2, 2, 1]
[1, 2, 3, 3, 3, 2, 1]
[1, 2, 3, 4, 3, 2, 1]
[2, 2, 3, 4, 3, 2, 1]
[2, 3, 3, 4, 3, 2, 1]
[2, 3, 4, 4, 3, 2, 1]
[2, 3, 4, 4, 3, 2, 2]

TODO:
 - tests
 - container equals 1 or 0
 - test for input conditions
"""

def accomodate(arr, pos):
    if pos > 0 and pos < len(arr) - 1: 
        if (arr[pos-1] == arr[pos] == arr[pos+1]) or \
            (arr[pos-1] > arr[pos] and (arr[pos+1] == arr[pos-1] or arr[pos+1] + 1 == arr[pos-1])) or \
            (arr[pos+1] > arr[pos] and (arr[pos-1] == arr[pos+1] or arr[pos-1] + 1 == arr[pos+1])):
            arr[pos] += 1
        elif arr[pos] > arr[pos-1]:
            arr = accomodate(arr, pos - 1)
        elif arr[pos] > arr[pos+1]:
            arr = accomodate(arr, pos + 1)
    elif pos == 0:
        if arr[pos] <= arr[pos+1]:
            arr[pos] += 1
        else:
            arr = accomodate(arr, pos+1)
    elif pos == len(arr) - 1:
        if arr[pos] <= arr[pos-1]:
            arr[pos] += 1
        else:
            arr = accomodate(arr, pos-1)
    return arr

length, position, number_of_grains = map(int, input().split())
sandbox = [0] * length

for _ in range(number_of_grains):
    sandbox = accomodate(sandbox, position)
    print(sandbox)
