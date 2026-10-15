with open("../8_file_handling/newTextFile.txt", "r") as f:
    # line1 = f.readline()
    # line2 = f.readline()
    # data = f.read()
    # print("Line 1", line1)
    # print("Line 2", line2)
    # print("Data File", data)
    readLinesMethod = f.readlines()
    print(readLinesMethod)
