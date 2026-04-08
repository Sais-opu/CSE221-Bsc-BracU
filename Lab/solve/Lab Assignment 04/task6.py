with open("input6.txt", "r") as file_in:
    with open("output6.txt", "w") as file_out:
        import numpy as np
        line = file_in.readline().split()
        nodes, egdes = int(line[0]), int(line[1])
        diamonds=[]

        for i in range(nodes):
            read = file_in.readline().strip()
            ap = [i for i in read]
            diamonds.append(ap)
        diamonds = np.array(diamonds)

        trav=[]
        D_count=[]
        i = 0

        # for up coordinate
        def up(diamonds, x, y, queue_val):
            try:
                x = (x - 1)
                read = file_in.readline().strip()
                read=diamonds[x][y]
                if [x,y] not in trav:
                    if (x >= 0 and y >= 0):
                        if diamonds[x][y] != "#":
                            trav.append([x,y])
                            queue_val.append([x,y])
            except:
                pass

        # for down coordinate
        def down(diamonds, x, y, queue_val):
            try:
                x = (x + 1)
                read = file_in.readline().strip()
                read=diamonds[x][y]
                if [x,y] not in trav:
                    if x >= 0 and y >= 0:
                        if diamonds[x][y] != "#":
                            trav.append([x,y])
                            queue_val.append([x,y])

            except:
                pass

        # for left coordinate    
        def left(diamonds, x, y, queue_val):
            try:
                y = (y - 1)
                read = file_in.readline().strip()
                read=diamonds[x][y]
                if [x,y] not in trav:
                    if x >= 0 and y >= 0:
                        if diamonds[x][y] != "#":
                            trav.append([x,y])
                            queue_val.append([x,y])

            except:
                pass

        # for right coordinate
        def right(diamonds, x, y, queue_val):
            try:
                y = (y + 1)
                read = file_in.readline().strip()
                read=diamonds[x][y]
                if [x,y] not in trav :
                    if  x>=0 and y>=0:
                        if diamonds[x][y] != "#":
                            trav.append([x,y])
                            queue_val.append([x,y])

            except:
                pass
            
        def dot_ck(diamonds):
            for i in range(len(diamonds)):
                if "." in diamonds[i]:
                    for j in range(len(diamonds[i])):
                        if diamonds[i][j] == ".":
                            return [i,j]
            i = (i + 1)

        while (i == 0):
            queue_val = [dot_ck(diamonds)]
            
            c = 0

            while True:          
                out = queue_val.pop(0)

                try:
                    up(diamonds, out[0], out[1], queue_val)
                    down(diamonds, out[0], out[1], queue_val)
                    left(diamonds, out[0], out[1], queue_val)
                    right(diamonds, out[0], out[1], queue_val)

                    if diamonds[out[0]][out[1]] == "D":
                        c = (c + 1)

                    diamonds[out[0]][out[1]]=1

                except:
                    i = (i + 1)

                if queue_val == []:
                    break

            D_count.append(c)
            maxRes = max(D_count)
        file_out.write(str(maxRes))