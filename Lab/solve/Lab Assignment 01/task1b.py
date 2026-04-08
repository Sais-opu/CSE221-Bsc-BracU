with open("input1b.txt", 'r') as file_in:
    with open("output1b.txt", 'w') as file_out:
        line = file_in.readline()
        var = int(line)
        for i in range(var):
            fs = file_in.readline().split()
            if str(fs[2]) == "+":
                # result = int(fs[1]) + int(fs[3])
                file_out.write(f'The result of {int(fs[1])} + {int(fs[3])} is {int(fs[1])+int(fs[3])}\n')
            if str(fs[2]) == "-":
                file_out.write(f'The result of {int(fs[1])} - {int(fs[3])} is {int(fs[1])-int(fs[3])}\n')
                # result = int(fs[1]) - int(fs[3])
            if str(fs[2]) == "*":
                file_out.write(f'The result of {int(fs[1])} * {int(fs[3])} is {int(fs[1])*int(fs[3])}\n')
                # result = int(fs[1]) * int(fs[3])
            if str(fs[2]) == "/":
                file_out.write(f'The result of {int(fs[1])} / {int(fs[3])} is {int(fs[1])/int(fs[3])}\n')
                # result = int(fs[1]) / int(fs[3])

            # file_out.write(str(result))