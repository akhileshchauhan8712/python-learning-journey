languages = {"python", "java", "c++", "python", "js"}  # non-empty set
print(type(languages))
print(languages)
languages.add("ruby")
print(languages)
languages.remove("js")
print(languages)

# sets do not entertain dublicacy
emptySet = set()  # empty set
print(type(emptySet))
