# task 3

filein = open('input3.txt', 'r')
fileout = open('output3.txt', 'w')

line = filein.readline().strip()
f_line = filein.readline().strip().split()
f_line = [int(x) for x in f_line]
f_line.sort()

done_ALL = []
JACK = []
time_for_JACK = 0
time_for_JILL = 0
s_line = filein.readline()

for item in range(len(s_line)):
    if s_line[item] == "J":
        out = f_line.pop(0)
        JACK.append(out)
        done_ALL.append(str(out))
        time_for_JACK = time_for_JACK + out
    if s_line[item] == "j":
        out = JACK.pop()
        done_ALL.append(str(out))
        time_for_JILL = time_for_JILL + out

for x in done_ALL:
    fileout.write(x)
fileout.write(f"\nJack will work for {time_for_JACK} hours\n")
fileout.write(f"Jill will work for {time_for_JILL} hours")