import select
import sys
import termios
import time
from random import choice

ageNotWritten = ["Please write your age", "Please tell me your age"]
notUnderstood = ["I am sorry, I did not quite understand what you said, how old are you?",
                 "Oh sorry, I did not quite catch that, can you repeat your age?",
                 "Sorry, can you say your age one more time?"]


def askage_func(user):
    print("How old are you?")
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 5)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            try:
                user.age = int(sentence[0])
            except ValueError:
                if sentence[0] in ["i'm", "im"]:
                    user.age = int(sentence[1])
                elif sentence[1] == "am":
                    user.age = int(sentence[2])
                else:
                    print(choice(notUnderstood))
                    continue
            time.sleep(2)
            if user.age < 4:
                print("You must be the smartest baby I've ever encountered...")
                time.sleep(1)
                print("Now come on, what is your real age?")
                continue
            elif user.age < 18:
                print(
                    "Hmmm I have a very hard time believing since the age requirement for interacting with me is 18... Don't know why that is though...")
                time.sleep(1)
                print("Now come on, what is your real age?")
                continue
            elif 80 < user.age < 130:
                print("Wow you are really old! That is awesome, you do not look a day older than 25")
            elif user.age > 129:
                print("That is insane, almost unbelievable... Which it is, you little prankster...")
                time.sleep(1)
                print("Now come on, what is your real age?")
                continue
            else:
                print("Nice, being " + str(user.age) + " must be great")

            time.sleep(3)
            chatbotAge = 47  # Gabriel's age
            difference = chatbotAge - user.age
            if difference < 0:
                print("This means that you are " + str(
                    difference) + " years older than me because I am just as old as my inventor, I'm 47 years old")
            elif difference > 0:
                print("This means that you are " + str(
                    difference) + " years younger than me because I am just as old as my inventor, I'm 47 years old")
            else:
                print("This means that you, me and my inventor are the same age")
            answered = True
            time.sleep(5)
        else:
            print(choice(ageNotWritten))
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

    answered = False
    ready = input(
        "But now let's move onto more important things. Are you ready to hear about what we are going to do today?\n").lower().strip().split()
    while not answered:
        if "ready" in ready or "yes" in ready:
            answered = True
        else:
            time.sleep(5)
            ready = input("Okay, are you ready now?\n").lower().strip().split()

# askage_func(User())
