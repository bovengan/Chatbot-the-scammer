import select
import sys
import termios
import time


def understand():
    print("Okay so what is going to happen now is that I am going to give you 3 tasks I want you to perform.")
    time.sleep(3)
    print(
        "You do not have to do them, but if you do, you will get points that will increase your odds of winning a gift from my makers.")
    time.sleep(3)
    print("I will be the judge, with a bit of assistance from my makers, if you complete the tasks or not.")
    time.sleep(3)
    print("Do you understand?")


def explanation_func(user):
    understand()
    answered = False
    while not answered:
        i, o, e = select.select([sys.stdin], [], [], 50)
        if i:
            sentence = sys.stdin.readline().strip().lower().split(" ")
            if "yes" in sentence:
                termios.tcflush(sys.stdin, termios.TCIFLUSH)
            else:
                termios.tcflush(sys.stdin, termios.TCIFLUSH)
                explanationAnswer = input(
                    "Hmm okay, that might have been a long instruction, do you want me to simplify? Or maybe explain it in Japanese?\n")
                if "no" in explanationAnswer:
                    pass
                else:
                    if "simplify" in explanationAnswer:
                        print(
                            "You will get three tasks to complete, for each completed task you get better odds at winning the gift.")
                    elif "japanese" in explanationAnswer:
                        print("完了するタスクが 3 つあり、完了したタスクごとに、ギフトを獲得する確率が高くなります。ここで最初のタスクです")
                        time.sleep(3)
                        print("Just kidding. That would have been cool though")
                        time.sleep(2)
                        answer = input("So, do you understand what you are going to do?\n")
                        if "yes" not in answer:
                            time.sleep(2)
                            understand()
                            continue
                        else:
                            print("I did not understand that, let's just move on...")
        else:
            print("Please type yes or no if you understand")

# explanation_func(User())
