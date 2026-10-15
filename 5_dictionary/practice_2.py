# you are given a list of programming language:
# ["Python","Java","C++","Python","Java","C"].
# Convert it into a set and print how many unique languages Divya knows.

programmingList = ["Python", "Java", "C++", "Python", "Java", "C"]
print(type(programmingList))

# how to convert a list into set
programmingSet = set(programmingList)
print(type(programmingSet))
print("Divya knows these many languages", len(programmingSet))
