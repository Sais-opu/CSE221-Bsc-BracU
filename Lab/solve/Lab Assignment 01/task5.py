with open("input5.txt", "r") as filein:
    with open("output5.txt", "w") as fileout:

        line = int(filein.readline())
        emlst = [] 

        for i in range(line):
            emlst.append(filein.readline().split())

        for item in range(len(emlst)):
            for itr in range(item, len(emlst)):

                if emlst[itr][0] < emlst[item][0]:
                    emlst[item],emlst[itr] = emlst[itr],emlst[item] #SWAP
        
        for item in range(len(emlst)):
            for itr in range(item, len(emlst)):

                if emlst[itr][0] == emlst[item][0]:
                    if emlst[itr][-1] > emlst[item][-1]:  
                        emlst[item],emlst[itr] = emlst[itr],emlst[item]  # SWAP

        for i in range(line):
            fileout.write(" ".join(emlst[i]) + "\n")