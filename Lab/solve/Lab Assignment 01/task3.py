with open("input3.txt", "r") as file_in:
    with open("output3.txt", "w") as file_out:

        line = int(file_in.readline())
        inp1 = file_in.readline().split()

        def bubbleSort(arr): 
            for i in range(len(arr)-1):        
                flag = False  
                for j in range(len(arr)-i-1):             
                    if arr[j] > arr[j+1]:                
                        arr[j+1], arr[j]=arr[j], arr[j+1]         
                        flag = True              
                if flag == False:            
                    break
            return arr


        for i in range(len(inp1)):
            inp1[i] = int(inp1[i])
        calling = bubbleSort(inp1)

        for i in range(len(calling)):
            file_out.write(str(calling[i]) + " ")

# I have used a flag for breaking the loop when the aray is already sorted.
# In this way, I have achieved the θ(n) for the best-case scenario.