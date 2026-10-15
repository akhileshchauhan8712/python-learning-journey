# question on slicing
# take input and print middle 3 characters, last 2 character
# green 5
str = input("Enter the value: ")
mid = len(str) // 2  # 5//2->2.5
output1 = str[mid - 1 : mid + 2]  # str[1:4]
print("Middle 3 Characters")
print(output1)

output2 = str[-2:]
print("Last 2 Characters")
print(output2)
