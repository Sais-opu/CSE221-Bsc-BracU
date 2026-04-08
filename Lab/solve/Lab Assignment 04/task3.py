with open("input3.txt", "r") as file_in:
    with open("output3.txt", "w") as file_out:
        
        line = file_in.readline().split()
        # print(line)
        nodes,edges  = int(line[0]), int(line[1])
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

        trav_node = [1] 
        stack_val = [1] 

        # print(dict)

        while True:          
            out = stack_val.pop()
            # print(out, end = " ")
            file_out.write(str(out) + " ") 

            for child in dict[out]:
                if child not in trav_node:
                    trav_node.append(child)
                    stack_val.append(child)
                    
            if stack_val == []:
                break