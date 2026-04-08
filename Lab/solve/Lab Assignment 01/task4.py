with open("input4.txt", "r") as file_in:
    with open("output4.txt", "w") as file_out:

        line = int(file_in.readline())
        idNo = file_in.readline().split()
        marks = file_in.readline().split()

        for item in range(len(idNo)):
            idNo[item] = int(idNo[item])
        for items in range(len(marks)):
            marks[items]= int(marks[items])

        for i in range(1, len(marks)):  
            mark_val = marks[i]
            id_val = idNo[i]
            j = i - 1 

            while (j >= 0 and mark_val > marks[j]):  
                marks[j + 1] = marks[j]
                idNo[j + 1] = idNo[j]  
                j = j - 1  
            marks[j+1] = mark_val 
            idNo[j+1] = id_val  
####################################################

        dic={}

        for read in range(line):
            if marks[read] in dic:
                append = dic.get(marks[read]).append(idNo[read])
            else:
                dic.update({marks[read]:[idNo[read]]})


        dicValues = list(dic.values())
        dicKeys = list(dic.keys())

        for itr in dicValues:
            for elem in range(1, len(itr)):      
                mark_val = itr[elem]     
                j = elem - 1  

                while (j >= 0 and mark_val < itr[j]):  
                    itr[j + 1] = itr[j]  
                    j = j - 1  

                itr[j + 1] = mark_val
                  
            dic.update({dicKeys[dicValues.index(dicValues[elem])]:dicValues[elem]})

        for key in range(len(dicKeys)):
            for vals in range(len(dicValues[key])):
                file_out.write(f"ID: {dicValues[key][vals]} Mark: {dicKeys[key]}\n")