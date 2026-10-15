# Print how many lines are present in notes.txt


with open("python_with_saumya_singh/8_file_handling/notes.txt", "r") as f:
    listOfLines = f.readlines()
    print("Output of readLines function\n", listOfLines)
    print("Number of lines in file", len(listOfLines))
