with open('input1b.txt','r') as file_in:
    with open('output1b.txt','w') as file_out:

        line = file_in.readline().split()
        # print(line)
        nodes,edges = int(line[0]), int(line[1])

        dict = {}

        for i in range(nodes+1):
            dict.update({i:[]})

        for i in range(edges):
            read = file_in.readline().split()
            for x in range(len(read)):
                read[x] = int(read[x])
            val = dict.get(read[0])
            val.append((read[1],read[2],))

        keys = list(dict.keys())
        values = list(dict.values())

        for i in range(len(keys)):
            keys[i] = str(keys[i])
        for i in range(len(values)):
            values[i] = str(values[i])
        
        for i in range(len(keys)):
            vals = values[i][1:-1:]
            file_out.write(f"{keys[i]} : {vals}\n")

# 1(a). I will connect child nodes to parent nodes
# 1(b). No 
