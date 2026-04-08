# task 5

with open("input5.txt", "r") as file_in:
    with open("output5.txt", "w") as file_out:
        
        line = file_in.readline().split()
        # print(line)
        nodes, edges, goal = int(line[0]), int(line[1]), int(line[2])
        # print(nodes,edges,goal)
        # adj = []
        dict = {}
        dict2={}
        main={}
        for i in range(1, nodes+1):
            dict[i]=[]
            dict2[i]=0
            main[i]=0

        for i in range(edges):
            read=file_in.readline().split()
            keys=int(read[0])
            values=int(read[1])

            if keys in dict.keys():
                if values not in dict[keys]:
                    dict[keys].append(int(read[1]))

            if values in dict.keys():
                if keys not in dict[values]:
                    dict[values].append(keys)


        queue_val = [1]
        trav = []

        while True:
            out = queue_val.pop(0)
            trav.append(out)
            
            for key, j in dict.items():
                if key == out:
                    for kk in dict[key]:
                        if kk not in queue_val:
                            if kk not in trav:
                                queue_val.append(kk)

                        if dict2[kk] == 0:
                            if kk != 1:
                                dict2[kk] = (dict2[out] + 1)
                                main[kk] = key
            if queue_val == []:
                break

        traveled = []
        achiv = goal
        # print(achiv)
        while (achiv != 0):
            for key, vals in main.items():
                if (key == achiv):
                    traveled.append(key)
                    achiv = vals
                    break

        file_out.write(f"Time: {dict2[goal]}\n")
        
        for i in range(len(traveled)-1,-1,-1):
            final = traveled[i]
            final = str(final)
            file_out.write(final + " ")