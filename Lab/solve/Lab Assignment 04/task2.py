with open('input2.txt','r') as file_in:
    with open('output2.txt','w') as file_out:

        line = file_in.readline().split()
        # print(line)
        nodes,edges = int(line[0]), int(line[1])
        # print(nodes, edges)
        # adj = []
        dict = {}

        for i in range(1,nodes+1):
            dict.update({i:[]})
        # print(dict)

        for i in range(edges):
            read=file_in.readline().split()
            # print(read[0])
            read = [int(i) for i in read]
            adj = dict.get(read[0])
            adj.append(read[1])
        # print(dict)
        
        trav_node = [1]
        queue_val = [1] 
        
        while True:          
            out = queue_val.pop(0)
            o = str(out)
            node = o[-1]
            # print(node)
            # print(out, end = " ")

            for child in dict[out]:
                if child not in trav_node:
                    trav_node.append(child)
                    queue_val.append(child)
            file_out.write(node + " ")

            if queue_val == []:
                break
        # print(trav_node)