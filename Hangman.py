from random_word import RandomWords

initialize = RandomWords()
word = str(initialize.get_random_word())
word_length = len(word)

while word_length >= 8:
    word = str(initialize.get_random_word())
    word_length = len(word)

output = ""
for char in range(0, word_length):
    output += "_"
print(output)

output_list = list(output)
output_string = ""

condition = 0
guesses = 0
while condition == 0:
    try:
        guesses = int(input("INPUT A NUMBER OF LIVES: "))
        condition = 1
    except ValueError:
        print("ERROR")

status = 0
count = 0
letters_used = ""

while status == 0 and count < guesses:

    guess_letter = str(input("INPUT A LETTER TO GUESS: "))

    while not len(guess_letter) == 1 or not guess_letter.isalpha() or guess_letter in letters_used:
        print("ERROR -- INVALID GUESS")
        guess_letter = str(input("INPUT A LETTER TO GUESS: "))
    guess_letter = guess_letter.lower()

    count2 = 0
    for letter in range(0, word_length):
        if word[letter] == guess_letter:
            output_list[letter] = guess_letter
            count2 += 1
    if count2 == 0:
        count += 1

    counter = 0
    for letter in output_list:
        if not letter == "_":
            counter += 1

    if counter == word_length:
        print("\nWINNER -- THE WORD WAS " + output_string.join(output_list).upper())
        status = 1
    else:
        print(output_string.join(output_list) + "  NUMBER OF LIVES: " + str(guesses-count))

    letters_used += guess_letter


print("LOSER -- THE WORD WAS " + word.upper())
