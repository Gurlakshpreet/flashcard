#This version is made using list data type

from posixpath import join
import sys, os
import time
que = [] #this will store the questions
ans = [] #this will store the answers
qu = ""
ru = ""

def j(v):
    return (" ".join(v.split())).lower() #returns string v in lowercase after removing any extra spaces from it

def evaluation(x, y, z):
    c = 0 #stores number of correct answers
    os.system('cls')
    if z:
        print("The question will be displayed to you, enter the answer. Don't add any extra symbols, Good Luck!")
    for i in range(len(x)):
        qu = j(input(join(x[i], " ").replace("/", "")))
        if y[i] == qu:
            print("Correct!")
            c += 1
        else:
            print(join("Wrong answer, the correct answer is ", y[i], ".").replace("/", ""))
    if z:
        print("Tutorial over.")
    w = join("You got 1 correct answer out of ", str(len(x)), "!").replace("/", "") if c == 1 else join("You got ", str(c), " correct answers out of ", str(len(x)), "!").replace("/", "")
    print(w)
    print("Thanks for using :)")
    reply = j(input("Would you like to try again? (reply with a 'yes' or 'no') "))
    if reply == "yes":
        while True:
            if z:
                reply = input("Enter 'tuto' if you'd like to revisit the tutorial, and 'start' if you'd like to try it without the tutorial: ")
                if reply == "tuto":
                    print("Directing you to the tutorial")
                    time.sleep(2)
                    os.system('cls')
                    x = []
                    y = []
                    code([True, True], x, y)
                    break
                elif reply == "start":
                    print("Directing you to a new terminal")
                    time.sleep(2)
                    os.system('cls')
                    x = []
                    y = []
                    code([False, False], x, y)
                    break
                else:
                    print("You entered an invalid response. Try again :)")
            reply = input("Enter 'same' if you'd like to answer the same set of questions, 'diff' if you'd like to try again with a new set of questions, or 'edit' if you'd like to add some questions to the existing set of questions. ")
            if reply == 'same':
                evaluation(x, y, "")
            elif reply == 'diff':
                x = []
                y = []
                os.system('cls')
                code([False, False], x, y)
            elif reply == 'edit':
                os.system('cls')
                code([False, False], x, y)
    elif reply == "no":
        print("Bye bye, and good luck!")
    else:
        print("I'll take that as a no, bye bye.")
    
def code(a, q, r): #variable a stores boolean for tutorial, and q and r store the list for questions and answers respectively
    if a[1]:
        print("First, enter a question")
    qu = j(input("Enter question here: "))
    if a[1]:
        print("Then, enter the answer to the question.")
    while True:
        ru = j(input("Enter answer here: "))
        if qu[-1] ==":":
            q.append(qu) #adding qu to list
        else:
            q.append(join(qu, ":").replace('/', ''))
        r.append(ru) #adding ru to list
        if(a[1]):
            print("You can do this as many times as you want to, when you're done inputting your set of questions and answer, instead of typing your question when asked for it, type 'stop' in lowercase. ")
            a = [True, False] #turning one of the Trues to false to prevent printing the above statement again and again
        qu = input("Enter question here: ")
        if qu == "stop":
            if (len(q) == 0):
                print("You didn't write any question! Try again :)")
                reply = [True, True] if q[0] else ""
                code(reply)
            if a[0]:
                x = "Now, you will be directed to a fresh terminal where you will be able to quiz/test yourself using the questions and answers which you entered."
                print(x)
                time.sleep(5.2) #belates execution of next line of code by 5.2 seconds
            evaluation(q, r, a[0])

print("This is a self-study tool for students, where they can create flashcards and evaluate themselves.")
reply = j(input("Would you like a tutorial? (reply with 'yes' for a tutorial) "))
reply = [True, True] if reply == "yes" else [False, False]
code(reply, que, ans)