import tkinter as tk
import random

wordlist = ["secret","test"] #,"abruptly", "hello","avenue","hangman","civil","awkward","brain","change","comparison","control","crime","regression","normal","force", "degree", "distance"]
words = random.choice(wordlist)
secret_word = words
dashes = "-" * len(secret_word)

def find_index(str, letter, idx):
    for i in range(len(str)):
        if str[i] == letter:
            idx.append(i)
    return idx

def update_dashes(idx, letter, dashlist):
    for i in range(len(idx)):
        dashlist[idx[i]] = letter
    return dashlist

def retrieve_guess():
    guess = entry.get()
    entry.delete(0,tk.END)
    global dashes
    dashlist = list(dashes)
    index = []
    #guesses_left = 25
    #total_guesses = guesses_left
    #print("Welcome to Hangman, you have {} guesses left. Type 'quit' to exit the game".format(guesses_left))
        
    while dashes != secret_word:
#        if guesses_left != total_guesses:
#            print("You have {} guesses left.".format(guesses_left))
#
#        if guesses_left == 0:
#            print("You have run out of guesses, You lose!")
#            break

        guess = guess.lower()

        if guess == "quit":
            result["text"] = "Quitting..."
            window.destroy()

        elif guess.isalpha() == False:
            print("Your guess must be a letter!")
            break

        elif len(guess) != 1:
            result["text"] = "Your guess must have exactly one character!"
            break

        elif secret_word.find(guess) != -1:
            result["text"] = "That letter is in the secret word!"
            dashidx = find_index(secret_word, guess, index)
            dashlist = update_dashes(dashidx, guess, dashlist)
            dashes = "".join(dashlist)
            index.clear()
            print(dashes)
            break

        else:
            result["text"] = "This letter is not in the secret word"
            break
        #guesses_left -= 1
        
    if dashes == secret_word:
        result["text"] = "Congratulations, you've found the secret word, You win!"

    if guess == "quit":
        result["text"] = "Quitting..."
        window.destroy()

    progress["text"] = dashes

    
window = tk.Tk()

greeting = tk.Label(text="Hangman",fg="black",bg="#34A2FE",width="50",height="2")

rules = tk.Label(text="Welcome to Hangman! type a single letter into the box. \n Try to guess the secret word. Type 'quit' to exit the game")

progress = tk.Label(text=dashes)

entry = tk.Entry(fg="black", bg="white", width=50)

button = tk.Button(text="Guess!",width=10,height=2,bg="yellow",fg="black",command=retrieve_guess)

result = tk.Label(text="")

greeting.pack(fill=tk.X)
rules.pack(fill=tk.X)
progress.pack(fill=tk.X)
entry.pack()
button.pack()
result.pack(fill=tk.X)

window.mainloop()
