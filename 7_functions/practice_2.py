# Write a function square(num) that returns the square of a number.


def square(num):
    return num**2


print(square(5))


# Write a function that takes a string and returns the count of vowels and consonants separately.
def countVowConso(userInput):
    vowels = "aeiouAEIOU"

    countVowel = 0
    countConsonants = 0

    for eachChar in userInput:
        if eachChar.isalpha():
            if eachChar in vowels:
                countVowel += 1
            else:
                countConsonants += 1

    return countVowel, countConsonants


vowels, consonants = countVowConso("Akhilesh Kumar")
print("Vowels is", vowels, "and Consonants", consonants)


def greet():
    print("Hello Akhilesh!")


result = greet()
print(result)
