import math
filein = open('input4.txt', 'r')
fileout = open('output4.txt', 'w')
array = []

while True:
    line = filein.readline().strip()
    read = line.split()
    # print(read)
    count = 0
    read = [int(x) for x in read]

    if (read[0] != 0 and read[1] != 0):
        for i in range(read[0], read[1]+1):
            if ((math.sqrt(i)) % 1) == 0:
                # print(i)
                count = count + 1
    else:
        break
    
    fileout.write(f"{count}\n")