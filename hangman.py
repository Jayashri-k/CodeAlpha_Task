import random

choices=['raspberry', 'swift', 'python', 'kotlin', 'java']
word=random.choice(choices)

print("WELCOME TO THE HANGMAN GAME\nLET'S START!!!")
print("NUMBER OF LETTERS: ", len(word))

chances=8
guessed=[]
correct=[]

while chances>0:
    letter=input("\nGuess a letter: ")
    if letter in guessed:
        print("You already guessed that letter! Try again.")
        continue

    guessed.append(letter)

    if letter in word:
        position=[i + 1 for i, char in enumerate(word) if char == letter]
        print("Good! The letter'"+letter+"'is in the word at position: "+str(position))
        correct.append(letter)
    else:
        print("Sorry, the letter'"+letter+"'is not in the word")
        chances=chances-1
        print("Remaining chances: "+str(chances))

    if all(char in correct for char in word):
        print("\nCongratulations! You guessed the word: "+ word)
        break

if not all(char in correct for char in word):
    print("\nGame Over! The man is HANGED!")
    print("The word was: "+word)

