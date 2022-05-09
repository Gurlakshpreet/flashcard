#This version is made using the dict data type

from posixpath import join
import sys, os
import time
qa = {} #This is the variable that will store all the questions and answers
qu = ""
ru = ""

def j(v):
    return (" ".join(v.split())).lower() #returns string v in lowercase after removing any extra spaces from it

def evaluation(z, x, s): #z is the boolean for tutorial, x is the variable in which the questions and answers are stores, s is the name of objects in dict
    c = 0 #This stores the number of correct answers
    os.system('cls') #this clears the terminal to prevent the user from peeking at the answers
    if z:
        print("The question will be displayed to you, enter the answer. Don't add any extra symbols, Good Luck!")
    for i in range(len(x)):
        qu = j(input(join(x[str(i)]["q"], " ").replace("/", ""))) #Fetching the question using i as the name of object and using it to get input
        if x[str(i)]["a"] == qu:
            print("Correct!")
            c += 1
        else:
            print(join("Wrong answer, the correct answer is ", x[str(i)]["a"], ".").replace("/", ""))
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
                    x = {}
                    code([True, True], x, 0) 
                    break
                elif reply == "start":
                    print("Directing you to a new terminal")
                    time.sleep(2)
                    os.system('cls')
                    x = {}
                    code([False, False], x, 0)
                    break
                else:
                    print("You entered an invalid response. Try again :)")
            reply = input("Enter 'same' if you'd like to answer the same set of questions, 'diff' if you'd like to try again with a new set of questions, or 'edit' if you'd like to add some questions to the existing set of questions. ")
            if reply == 'same':
                evaluation([False, False], x, 0)
            elif reply == 'diff':
                os.system('cls')
                code([False, False], {}, 0)
            elif reply == 'edit':
                os.system('cls')
                code([False, False], x, s + 1)
    elif reply == "no":
        print("Bye bye, and good luck!")
    else:
        print("I'll take that as a no, bye bye.")
    
def code(a, q, n): #a is the boolean value for tutorial, q is the dict variable in which the questions and answers will be stored, and n is used as the name of objects in dict variable. Passing n is important, as it determines if and when the dict variable has to be deleted or overwritten, which is an important part of the evaluate function.
    if a[1]:
        print("First, enter a question")
    qu = j(input("Enter question here: "))
    if a[1]:
        print("Then, enter the answer to the question.")
    while True:
        ru = j(input("Enter answer here: "))
        qu = qu if qu[-1] ==":" else join(qu + ":").replace('/', '')
        q.update({str(n): {"q" : qu, "a" : ru}}) #stores question and answer in dict qa
        n += 1 #updates object name
        if(a[1]):
            print("You can do this as many times as you want to, when you're done inputting your set of questions and answer, instead of typing your question when asked for it, type 'stop' in lowercase. ")
            a = [True, False] #turning one of the Trues to false to prevent printing the above statement again and again
        qu = input("Enter question here: ")
        if qu == "stop":
            if (len(q) == 0):
                print("You didn't write any question! Try again :)")
                a = [True, True] if a[0] else ""
                code(a, q, n)
            if a[0]:
                x = "Now, you will be directed to a fresh terminal where you will be able to quiz/test yourself using the questions and answers which you entered."
                print(x)
                time.sleep(5.2)
            evaluation(a[0], q, n)

print("This is a self-study tool for students, where they can create flashcards and evaluate themselves.") #start here
reply = j(input("Would you like a tutorial? (reply with 'yes' for a tutorial) "))
reply = [True, True] if reply == "yes" else [False, False]
code(reply, qa, 0)