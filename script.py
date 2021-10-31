# select random word from words.txt
    # import random module **
    # open txt file using with syntax **
    # put words from txt file into list of strings **
    # select one word from list to use for testing **

# show mystery word as underscores to user **
    # ask for user guess (upper or lowercase does not matter)
    # validate user input if user enters more than one letter
        # show user error: "You can only guess letter a a time. Guess again: "
    
# Show user if guess is part of word **
    # replace underscore with letter **
    # Show letters that have not been guessed
    

# limit number of user guesses to 8
    # keep track of user guess count
    # show user how many guesses are left
    # user only loses guess if guess is incorrect
    # display mystery word if user runs out of guesses
    # show user error if they guess same letter twice. Do not count as a guess in this case.

# Prompt user to play again when the game ends
# Add levels of difficulty based on random word length

import random
words = []
guesses = []
guess_count = 1


# turn words.txt into a list of strings
all_words = open("words.txt")
words_strings = all_words.read()
words_strings = words_strings.lower().split()

# this function will pick a level and return random word
def pick_level():
    level = input("Pick a level: easy, medium or hard: ").lower()
    if level == "easy":
            easy_word_list = []
            for word in words_strings:
                if len(word) >= 4 and len(word) <= 6:
                    easy_word_list.append(word)
            random_word = random.choice(easy_word_list)
            # print(random_word)
    elif level == "medium":
            medium_word_list = []
            for word in words_strings:
                if len(word) >= 6 and len(word) <= 8:
                    medium_word_list.append(word)
            random_word = random.choice(medium_word_list)
            # print(random_word)
    elif level == "hard":
            hard_word_list = []
            for word in words_strings:
                if len(word) >= 8:
                    hard_word_list.append(word)
            random_word = random.choice(hard_word_list)
    # word_length = range(len(random_word))
    print(random_word)

    return(random_word)
# pick_level()
# print(word_length)

# def gameplay():
underscores = []
end_game = False

random_word = pick_level()
word_length = range(len(random_word))
for num in word_length:
    underscores.append('_')
underscores = "".join(underscores)

print(underscores)
user_input = input('Make a guess... ').lower()

while user_input != 'Quit' and end_game == False:

    for index in range(len(random_word)):
        if random_word[index] == user_input:
            underscores = underscores[0:index] + user_input + underscores[index+1:]
    print(underscores)
    user_input = input('Guess again... ')

if user_input == 'Quit':
    end_game = True

# gameplay()
# below here is a copy of the game engine following jeanettes random word choice

# random_word = 'random'
# word_length = range(len(random_word))
# for num in word_length:
#     underscores.append('_')
# underscores = "".join(underscores)

# print(underscores)
# user_input = input('Make a guess... ').lower()

# while user_input != 'Quit' and end_game == False:
#     if guess_count == 8:
#         print('You have run out of guesses')

#     for index in range(len(random_word)):
#         if random_word[index] == user_input:
#             underscores = underscores[0:index] + user_input + underscores[index+1:]
#     print(underscores)
#     user_input = input('Guess again... ')

#     if user_input == 'Quit':
#         end_game = True
                

       












# this will pick a random word and gameplay

# with open('words.txt') as file:
#     strings = file.readlines()

#     for string in strings:
#         words.append(string)
#         words.replace("\n", " ")
#         print(words)
#     random_word = random.choice(words)

#     print(random_word)

#     word_length = range(len(random_word))
#     for num in word_length:
#         underscores.append('_')
#     underscores = "".join(underscores)

#     print(underscores)
#     user_input = input('Make a guess... ').lower()

#     while user_input != 'Quit' and end_game == False:
#         if guess_count == 8:
#             print('You have run out of guesses')

#         for index in range(len(random_word)):
#             if random_word[index] == user_input:
#                 underscores = underscores[0:index] + user_input + underscores[index+1:]
#         print(underscores)
#         user_input = input('Guess again... ')

#         if user_input == 'Quit':
#             end_game = True
