with open("input4.txt", "r") as file_in:
    with open("output4.txt", "w") as file_out:
        
        line = file_in.readline().split()
        # print(line)
        nodes,edges = int(line[0]), int(line[1])
        # print(nodes,edges)
        # adj = []
        dict = {}
        # print(adj)
        for i in range(1, nodes+1):
            dict.update({i:[]})
        # print(dict)

        for i in range(edges):
            read = file_in.readline().split()
            read = [int(i) for i in read]
            adj = dict.get(read[0])
            adj.append(read[1])
        # print(dict)
        
        c = 0
        for k,nodes in dict.items():
            trav = [k] 
            queue_val = [k]

        while True:          
            out = queue_val.pop(0)  
            
            for child in dict[out]:
                if child == k:
                    c = c + 1
                if child not in trav:
                    trav.append(child)
                    queue_val.append(child)

            if queue_val == []:
                break

        if (c != 0):
            file_out.write('" YES! "')
        else:
            file_out.write('" NOO! "')

# 1(a). Yes, I can.
# 1(b). Yes, I can.