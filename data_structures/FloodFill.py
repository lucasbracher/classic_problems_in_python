"""
Classic Floodfill algorithm with Queue
How to use this script:

1) Insert the number of lines you want to input
2) Input the board, one line each time
3) Input the command you want. There are just 2 commands: quit and paint
    - in order to quit, just type q and <Enter>
    - in order to paint, just insert the coordinates of the square you want to paint with the desired color.
      Coordinates are zero based.

Usage examples:
> python FloodFill.py
6
aaaaaaaa
aaaxxaaa
aaxxxxaa
axxxxxxa
aaaxxaaa
axxxxxxa
3 3 k
aaaaaaaa
aaakkaaa
aakkkkaa
akkkkkka
aaakkaaa
akkkkkka
q

"""

from Queue import Queue

# Get the number of lines
n = int(input())

# Read the board
b = []
for _ in range(n):
    l = list(input())
    m = len(l)
    b.append(l)

while True:
    # Read the command
    l = input().split()
    if l[0] == 'q':
        break
    x = int(l[0])
    y = int(l[1])
    target_color = l[2]

    # Setup before first iteration
    orig_color = b[x][y]
    painted = [[False] * m for i in range(n)]
    q = Queue()

    # Insert first position in queue
    q.insert([x, y])

    while not q.isempty():
        # Remove element from queue
        x, y = q.remove()

        # Change color if it's equal to the color of the first square
        if b[x][y] == orig_color:
            b[x][y] = target_color
    
        # Mark it as painted
        painted[x][y] = True

        # Insert 8 neighboring elements in the queue
        if x < n-1 and y > 0 and not painted[x+1][y-1]:
            q.insert([x+1, y-1])
        if x < n-1 and not painted[x+1][y]:
            q.insert([x+1, y])
        if x < n-1 and y < m-1 and not painted[x+1][y+1]:
            q.insert([x+1, y+1])
        if y < m-1 and not painted[x][y+1]:
            q.insert([x, y+1])
        if y > 0 and not painted[x][y-1]:
            q.insert([x, y-1])
        if x > 0 and y > 0 and not painted[x-1][y-1]:
            q.insert([x-1, y-1])
        if x > 0 and not painted[x-1][y]:
            q.insert([x-1, y])
        if x > 0 and y < m-1 and not painted[x-1][y+1]:
            q.insert([x-1, y+1])

    for line in b:
        print("".join(line))
