with open("input1a.txt", 'r') as file_in:
    with open("output1a.txt", 'w') as file_out:
        line = file_in.readline()
        var = int(line)
        for i in range(var):
            final = int(file_in.readline())
            if final % 2 == 0:
                r = str(final) + " is an Even number." + "\n"
            else:
                r = str(final) + " is an Odd number." + "\n"
            file_out.write(r)