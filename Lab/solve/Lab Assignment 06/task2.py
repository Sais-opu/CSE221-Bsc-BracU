filein = open('input2.txt', 'r')
fileout = open('output2.txt', 'w')

line = filein.readlines()
array = []

def activity(array, start, end):
    array.sort(key = lambda a: a[1])
    count = end
    peps = array[:end+1]

    for i in range(end, len(array)):
        for j in range(len(peps)):
            if (array[i][0] >= peps[j][1]):
                count = count + 1
                peps[j] = array[i]
                break
    
    fileout.write(str(count))

filein.seek(0)
read = filein.readline().split()
a, b = read[0], read[1]
start,end = int(a), int(b)

for i in range(1, start+1):
    array1 = []
    c, d = line[i].split()
    N, M = int(c), int(d)
    array1.append(N)
    array1.append(M)
    array.append(array1)

activity(array, start, end)