with open('input1a.txt','r') as file_in:
    with open('output1a.txt','w') as file_out:
        line = file_in.readline().split()
        val = file_in.readlines()
        # print(line)
        nodes,edges = int(line[0]), int(line[1])
        # edges = int(line[1])
        main_matrix = []

        for i in range(len(val)):
            line = val[i].strip().split()
            main_matrix.append(line)
        # print(main_matrix)

        for i in range(len(main_matrix)):
            for j in range(len(main_matrix[i])):
                main_matrix[i][j] = int(main_matrix[i][j])

        matrixx = [[0 for i in range(nodes+1)] for j in range(nodes+1)]
        for i in range(len(matrixx)-2):
            matrixx[main_matrix[i][0]][main_matrix[i][1]] = main_matrix[i][2]
        # n = matrixx[i][i]
        # print(str(matrixx))
        for i in matrixx:
            file_out.write(str(i) + "\n")