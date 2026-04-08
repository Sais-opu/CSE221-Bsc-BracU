filein = open('input1.txt', 'r')
fileout = open('output1.txt', 'w')

line = int(filein.readline().strip())
array = []

for i in range(line):
    read = filein.readline().split()
    r1, r2 = read[1], read[0]
    start, end = int(r1), int(r2)
    array.append([start, end])
# print(array)
array.sort()
# print(array)

init_start = array[0][0]
activity1 = [array[0]]

for i in range(1, len(array)):
    if (init_start <= array[i][1]):
        activity1.append(array[i])
        init_start = array[i][0]

fileout.write(str(len(activity1))  +  "\n")

for x in activity1:
    fileout.write(f"{x[1]} {x[0]}\n")