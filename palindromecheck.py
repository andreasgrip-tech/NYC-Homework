#Check if a word given by the user is a palindrome or not. Example of a palindromes: "kayak", "level", "was it a car or a cat i saw".
#first step is to ask the user to give a word and store it in a variable.
word = input("Please enter a word to check if it's a palindrome: ").lower()
#second step is to reverse the word and store it in a variable. 
reversed_word = word[::-1]
#third step is to compare the original word with the reversed word and display if it's a palindrome
if word == reversed_word:
    print(f"{word} is a palindrome.")   
else:
    print(f"{word} is not a palindrome.")
