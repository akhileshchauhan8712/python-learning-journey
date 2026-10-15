# Read only the first line of bio.txt

with open("python_with_saumya_singh/8_file_handling/bio.txt", "r") as f:
    line1 = f.readline()
    print("Read Line 1\n", line1)
