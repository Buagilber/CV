import random
import easygui
secret = random.randint(1, 99)
guess = 0
tries = 0
easygui.msgbox('''AHOY! I'm the Dread Pirate Roberts, and I have a secret!
It is a number from 1 to 99. I'll give you 6 tries.''')
while guess != secret and tries < 6:
    guess = easygui.integerbox("What is your guess?\n(a number from 1 to 99)")
    if not guess:
        break
    if guess < secret:
        easygui.msgbox(str(guess) + "is too low, scurvy dog!")
    elif guess > secret:
        easygui.msgbox(str(guess) + "is too high, landlubber!")
    tries += 1
if guess == secret:
    easygui.msgbox("Anough! You got it! Found my secret, you did!")
else:
    easygui.msgbox("No more guesses! The number was " + str(secret))
