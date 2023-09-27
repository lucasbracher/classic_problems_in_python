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

How this works:

 - It checks only the position you want to insert, immediate left and immediate right.
   If it can't insert there, it looks for the proper position recursively.
 - For the sake of code explanation, I'll denote the immediate left, the position, and the right as | * * | .
   Yes, immagine those as little cells.
 - Cell represented between asterisks is the considered cell.
 - Occupied cell is represented with an o

TODO:
 - tests
 - container equals 1 or 0
 - test for input conditions
 - look for optimizations
"""

def accomodate(arr, pos):
    # Not the beginning or the end of the array
    if pos > 0 and pos < len(arr) - 1: 
        # | * * |  or  |o* * |  or  | * *o|
        if (arr[pos-1] == arr[pos] == arr[pos+1]) or \
            (arr[pos-1] > arr[pos] and (arr[pos+1] == arr[pos-1] or arr[pos+1] + 1 == arr[pos-1])) or \
            (arr[pos+1] > arr[pos] and (arr[pos-1] == arr[pos+1] or arr[pos-1] + 1 == arr[pos+1])):
            arr[pos] += 1
        elif arr[pos] > arr[pos-1]:
            # | *o* |  or  | *o*o|
            arr = accomodate(arr, pos - 1)
        elif arr[pos] > arr[pos+1]:
            # | *o* |  or  |o*o* |
            arr = accomodate(arr, pos + 1)
    elif pos == 0:
        if arr[pos] <= arr[pos+1]:
            # * * | |  or  * *o| |
            arr[pos] += 1
        else:
            # *o* | |
            arr = accomodate(arr, pos+1)
    elif pos == len(arr) - 1:
        if arr[pos] <= arr[pos-1]:
            # | | * *  or  | |o* *
            arr[pos] += 1
        else:
            # | | *o*
            arr = accomodate(arr, pos-1)
    return arr

length, position, number_of_grains = map(int, input().split())
sandbox = [0] * length

for _ in range(number_of_grains):
    sandbox = accomodate(sandbox, position)
    print(sandbox)
