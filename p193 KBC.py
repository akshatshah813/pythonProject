# 5 ques
##life line 50-50 flip the question

class bank_question:

    def q1(self):
        print("Question 1")
        print("In which continent is india located?")
        print("(A) Asia ")
        print("(B) Africa")
        print("(C) North America")
        print("(D) Europe")
        a=("a"or"A")

    def q2(self):
        print("Question 2")
        print("What is 2+2")
        print("(A) -4 ")
        print("(B) 0")
        print("(C) 4")
        print("(D) 6")
        a =( "c" or "C")

    def q3(self):
        print("Question 3")
        print("What is 22-33=")
        print("(A) -10 ")
        print("(B) -11")
        print("(C) 10")
        print("(D) 11")
        a = ("b"or "B")

    def q4(self):
        print("Question 4")
        print("Where is ahmedabad located?")
        print("(A) Maharastra ")
        print("(B) Delhi")
        print("(C) Tamil Nadu")
        print("(D) Gujarat")
        a = ("d"or"D")

    def q5(self):
        print("Question 5")
        print("what is pakistan to India")
        print("(A) friend ")
        print("(B) brother")
        print("(C) Son")
        print("(D) father")
        a = ("c" or "C")

    def q6(self):
        print("you have choose flip the question")
        print("by which other name is india also known?")
        print("(A) pakistan ")
        print("(B) Bharat")
        print("(C) Hindu")
        print("(D) Bha")
        a=("b"or"B")

    def lifeline(self):
        print("Do you want to use life line?")


    def entervalid(self):
        print("Choose valid option!")

    def won(self):
        print("*"*30)
        print("*" * 30)
        print("Congratulations")
        print("You have WON the game")
        print("*" * 30)
        print("*" * 30)

b1=bank_question()

print("*"*20)
print(" **Welcome to KBC**")
print("Kaun Banega Crorepati")
print("*"*20)
print("Total Questions => 5")
print("*"*20)
print("\tLife-Lines")
print("1 => 50-50")
print("2 => Flip the question")
print("*"*20)


user=input("What is your name?")

print("Welcome",user)
print("Let's Start the Game")


while True:
    b1.q1()
    b1.lifeline()
    x = input("1 => YES\t 2 => NO")
# question 1
# using life line
    if x=="1":    #use life line
        print("*" * 20)
        print("\tLife-Lines")
        print("1 => 50-50")
        print("2 => Flip the question")
        print("*" * 20)
        l = input("Which life line would you like to use?")
    # 50-50 q1
        if l=="1":
            print("Question 1")
            print("In which continent is india located?")
            print("(A) Asia ")
            print("(B) ")
            print("(C) ")
            print("(D) Europe")
            a = ("a"or "A")
            ans = input("Answer to the Question =>")     #answer q1
            if ans == a:
                print("Correct answer")
                print("Moving to next round")
        # ________________________________
        #question 2 start
                b1.q2()
                b1.lifeline()
                x = input("1 => YES\t 2 => NO")
            # q2 using life-line
                if x=="1":
                    print("*" * 20)
                    print("\tLife-Lines")
                    print("50-50 (Already Used)")
                    print("1 => Flip the question")
                    print("*" * 20)
                    l = input("Which life line would you like to use?")
            # flip the question 2
                    if l=="1":
                        b1.q6()
                        ans = input("Answer to the Question =>")
                        if ans == a:
                            print("Correct answer")
                            print("Moving to next round")
                # ________________________________
                # question 3 start
                            b1.q3()
                            print("Both life-lines used")
                            ans = input("Anwer to the Question =>")
                            if ans == a:
                                print("Correct answer")
                                print("Moving to next round")
                    # ________________________________
                    # question 4 start
                                b1.q4()
                                print("Both life-lines used")
                                ans = input("Anwer to the Question =>")
                                if ans == a:
                                    print("Correct answer")
                                    print("Moving to next round")
                        # ________________________________
                        # question 5 start
                                    b1.q5()
                                    print("Both life-lines used")
                                    ans = input("Anwer to the Question =>")
                                    if ans == a:
                                        print("Correct answer")
                                        b1.won()
                                    else:
                                        print("Wrong answer")
                                        print("sorry your game ends here")
                                        break
                        # question 5 end
                        # ________________________________
                                else:
                                    print("Wrong answer")
                                    print("sorry your game ends here")
                                    break
                    # question 4 end
                    # ________________________________
                            else:
                                print("Wrong answer")
                                print("sorry your game ends here")
                                break
                # question 3 end
                # ________________________________
                        else:
                            print("Wrong answer")
                            print("sorry your game ends here")
                            break
                    else:
                        b1.entervalid()
        # q2 not using life-line
        # flip the question left
                elif x=="2":
                    ans = input("Answer to the Question =>")
                    if ans == a:
                        print("Correct answer")
                        print("Moving to next round")
            # ________________________________
            #question 3 start
            #flip the q left
                        b1.q3()
                        b1.lifeline()
                        x = input("1 => YES\t 2 => NO")
                # q3 using flip the q life-line
                        if x=="1":
                            b1.q6()
                            ans = input("Answer to the Question =>")
                            if ans == a:
                                print("Correct answer")
                                print("Moving to next round")
                    # ________________________________
                    # question 4 start
                    #no life-line left
                                b1.q4()
                                print("Both life-lines used")
                                ans = input("Answer to the Question =>")
                                if ans == a:
                                    print("Correct answer")
                                    print("Moving to next round")
                        # ________________________________
                        # question 5 start
                                    b1.q5()
                                    print("Both life-lines used")
                                    ans = input("Answer to the Question =>")
                                    if ans == a:
                                        print("Correct answer")
                                        b1.won()
                                    else:
                                        print("Wrong answer")
                                        print("sorry your game ends here")
                                        break
                        # question 5 end
                        # ________________________________
                                else:
                                    print("Wrong answer")
                                    print("sorry your game ends here")
                                    break
                    # question 4 end
                    # ________________________________
                            else:
                                print("Wrong answer")
                                print("sorry your game ends here")
                                break

                # q3 not using life-line
                # flip the question left
                        elif x=="2":
                            ans = input("Anwer to the Question =>")
                            if ans == a:
                                print("Correct answer")
                                print("Moving to next round")
                    # ________________________________
                    # question 4 start
                    # flip the question left
                                b1.q4()
                                b1.lifeline()
                                x = input("1 => YES\t 2 => NO")
                        #q4 using life-line
                                if x=="1":
                                    b1.q6()
                                    ans = input("Answer to the Question =>")
                                    if ans == a:
                                        print("Correct answer")
                                        print("Moving to next round")
                            # ________________________________
                            # question 5 start
                            # no life-line left
                                        b1.q5()
                                        print("Both life-lines used")
                                        ans = input("Answer to the Question =>")
                                        if ans == a:
                                            print("Correct answer")
                                            b1.won()
                                        else:
                                            print("Wrong answer")
                                            print("sorry your game ends here")
                                            break
                            # question 5 end
                            # ________________________________
                                    else:
                                        print("Wrong answer")
                                        print("sorry your game ends here")
                                        break
                        # q4 not using life-line
                        # flip the question left
                                elif x=="2":
                                    ans = input("Anwer to the Question =>")
                                    if ans == a:
                                        print("Correct answer")
                                        print("Moving to next round")
                            # ________________________________
                            # question 5 start
                            # flip the question left
                                        b1.q5()
                                        b1.lifeline()
                                        x = input("1 => YES\t 2 => NO")
                                #q5 using life-line
                                        if x=="1":
                                            b1.q6()
                                            ans = input("Answer to the Question =>")
                                            if ans == a:
                                                print("Correct answer")
                                                b1.won()
                                            else:
                                                print("Wrong answer")
                                                print("sorry your game ends here")
                                                break
                                #q5 not using life-line
                                # flip the question left
                                        elif x=="2":
                                            ans = input("Answer to the Question =>")
                                            if ans == a:
                                                print("Correct answer")
                                                b1.won()
                                            else:
                                                print("Wrong answer")
                                                print("sorry your game ends here")
                                                break
                                        else:
                                            b1.entervalid()

                            # question 5 end
                            # ________________________________
                                    else:
                                        print("Wrong answer")
                                        print("sorry your game ends here")
                                        break
                                else:
                                    b1.entervalid()
                    # question 4 end
                    # ________________________________
                            else:
                                print("Wrong answer")
                                print("sorry your game ends here")
                                break
                        else:
                            b1.entervalid()
            # question 3 end
            # ________________________________
                    else:
                        print("Wrong answer")
                        print("sorry your game ends here")
                        break
                else:
                    b1.entervalid()
        # question 2 end
        #________________________________
            else:
                print("Wrong answer")
                print("sorry your game ends here")
                break
    # flip the question 1
    # 50-50 left
        elif l=="2":
            b1.q6()
            ans = input("Answer to the Question =>")
            if ans == a:
                print("Correct answer")
                print("Moving to next round")
        #_________________________
        #question2 start
        #50-50 left
                b1.q2()
                b1.lifeline()
                x = input("1 => YES\t 2 => NO")
            # q2 using life-line
                if x=="1":
                    print("*" * 20)
                    print("\tLife-Lines")
                    print("1 => 50-50 ")
                    print("Flip the question (Already Used)")
                    print("*" * 20)
                    l = input("Which life line would you like to use?")
                #q2 using 50-50
                    if l=="1":
                        print("Question 2")
                        print("What is 2+2")
                        print("(A) -4 ")
                        print("(B)  ")
                        print("(C) 4")
                        print("(D)  ")
                        a = "c" or "C"
                        ans = input("Answer to the Question =>")
                        if ans == a:
                            print("Correct answer")
                            print("Moving to next round")
                    #___________________________________
                    # question 3 start
                    # no life-line available
                            b1.q3()
                            print("All life-lines used")
                            ans = input("Answer to the Question =>")
                            if ans == a:
                                print("Correct answer")
                                print("Moving to next round")
                        # ___________________________________
                        # question 4 start
                        # no life-line available
                                b1.q4()
                                print("All life-lines used")
                                ans = input("Answer to the Question =>")
                                if ans == a:
                                    print("Correct answer")
                                    print("Moving to next round")
                            # ___________________________________
                            # question 5 start
                            # no life-line available
                                    b1.q5()
                                    print("All life-lines used")
                                    ans = input("Answer to the Question =>")
                                    if ans == a:
                                        print("Correct answer")
                                        b1.won()
                                    else:
                                        print("Wrong answer")
                                        print("sorry your game ends here")
                                        break
                            # question 5 end
                            # __________________________________
                                else:
                                    print("Wrong answer")
                                    print("sorry your game ends here")
                                    break
                        # question 4 end
                        # __________________________________
                            else:
                                print("Wrong answer")
                                print("sorry your game ends here")
                                break
                    # question 3 end
                    # __________________________________
                        else:
                            print("Wrong answer")
                            print("sorry your game ends here")
                            break
                    else:
                        b1.entervalid()
            # q2 without using life-line
            #50-50 left
                elif x=="2":
                    ans = input("Answer to the Question =>")
                    if ans == a:
                        print("Correct answer")
                        print("Moving to next round")
                #___________________
                # question3 start
                #50-50 life-line left
                        b1.q3()
                        b1.lifeline()
                        x = input("1 => YES\t 2 => NO")
                    #Q3 using life-line
                        if x=="1":
                            print("*" * 20)
                            print("\tLife-Lines")
                            print("1 => 50-50 ")
                            print("Flip the question (Already Used)")
                            print("*" * 20)
                            l = input("Which life line would you like to use?")
                        # q3 using 50-50
                            if l=="1":
                                print("Question 3")
                                print("What is 22-33=")
                                print("(A)    ")
                                print("(B) -11")
                                print("(C)   ")
                                print("(D) 11")
                                a = "b" or "B"
                                ans = input("Answer to the Question =>")
                                if ans == a:
                                    print("Correct answer")
                                    print("Moving to next round")
                            # ___________________________________
                            # question 4 start
                            # no life-line available
                                    b1.q4()
                                    print("All life-lines used")
                                    ans = input("Answer to the Question =>")
                                    if ans == a:
                                        print("Correct answer")
                                        print("Moving to next round")
                                # ___________________________________
                                # question 5 start
                                # no life-line available
                                        b1.q5()
                                        print("All life-lines used")
                                        ans = input("Answer to the Question =>")
                                        if ans == a:
                                            print("Correct answer")
                                            b1.won()
                                        else:
                                            print("Wrong answer")
                                            print("sorry your game ends here")
                                            break
                                # question 5 end
                                # __________________________________
                                    else:
                                        print("Wrong answer")
                                        print("sorry your game ends here")
                                        break
                            # question 4 end
                            # __________________________________
                                else:
                                    print("Wrong answer")
                                    print("sorry your game ends here")
                                    break
                            else:
                                b1.entervalid()
                    # Q3 without using life-line
                    # 50-50 life-line left
                        elif x=="2":
                            ans = input("Answer to the Question =>")
                            if ans == a:
                                print("Correct answer")
                                print("Moving to next round")
                        # __________________________________
                        # question 4 start
                        # 50-50 life-line left
                                b1.q4()
                                b1.lifeline()
                                x = input("1 => YES\t 2 => NO")
                            #q4 using life-line
                                if x=="1":
                                    print("*" * 20)
                                    print("\tLife-Lines")
                                    print("1 => 50-50 ")
                                    print("Flip the question (Already Used)")
                                    print("*" * 20)
                                    l = input("Which life line would you like to use?")
                                # q4 using 50-50
                                    if l=="1":
                                        print("Question 4")
                                        print("Where is ahmedabad located?")
                                        print("(A)  ")
                                        print("(B) Delhi")
                                        print("(C) ")
                                        print("(D) Gujarat")
                                        a = "d" or "D"
                                        ans = input("Answer to the Question =>")
                                        if ans == a:
                                            print("Correct answer")
                                            print("Moving to next round")
                                    # __________________________________
                                    # question 5 start
                                    # no life-line left
                                            b1.q5()
                                            print("All life-lines used")
                                            ans = input("Answer to the Question =>")
                                            if ans == a:
                                                print("Correct answer")
                                                b1.won()
                                            else:
                                                print("Wrong answer")
                                                print("sorry your game ends here")
                                                break
                                    # question 5 end
                                    # __________________________________

                                        else:
                                            print("Wrong answer")
                                            print("sorry your game ends here")
                                            break
                                    else:
                                        b1.entervalid()
                            # q4 without using life-line
                            # 50-50 life-line left
                                elif x=="2":
                                    ans = input("Answer to the Question =>")
                                    if ans == a:
                                        print("Correct answer")
                                        print("Moving to next round")
                                # __________________________________
                                # question 5 start
                                # 50-50 life-line left
                                        b1.q5()
                                        b1.lifeline()
                                        x = input("1 => YES\t 2 => NO")
                                    #q5 using life-line
                                        if x=="1":
                                            print("*" * 20)
                                            print("\tLife-Lines")
                                            print("1 => 50-50")
                                            print("Flip the question (Already used)")
                                            print("*" * 20)
                                            l = input("Which life line would you like to use?")
                                            if l=="1":
                                                print("Question 5")
                                                print("what is pakistan to India")
                                                print("(A)  ")
                                                print("(B) brother")
                                                print("(C) Son")
                                                print("(D) ")
                                                a = "c", "C"
                                                ans = input("Answer to the Question =>")
                                                if ans == a:
                                                    print("Correct answer")
                                                    b1.won()
                                                else:
                                                    print("Wrong answer")
                                                    print("sorry your game ends here")
                                                    break
                                            else:
                                                b1.entervalid()
                                    # q5 without using life-line
                                        elif x=="2":
                                            ans = input("Answer to the Question =>")
                                            if ans == a:
                                                print("Correct answer")
                                                b1.won()
                                            else:
                                                print("Wrong answer")
                                                print("sorry your game ends here")
                                                break
                                        else:
                                            b1.entervalid()
                                # question 5 end
                                # __________________________________
                                    else:
                                        print("Wrong answer")
                                        print("sorry your game ends here")
                                        break
                                else:
                                    b1.entervalid()
                        # question 4 end
                        # __________________________________
                            else:
                                print("Wrong answer")
                                print("sorry your game ends here")
                                break
                        else:
                            b1.entervalid()
                # question3 end
                # _________________________
                    else:
                        print("Wrong answer")
                        print("sorry your game ends here")
                        break
                else:
                    b1.entervalid()
        #question2 end
        # _________________________
            else:
                print("Wrong answer")
                print("sorry your game ends here")
                break
        else:
            b1.entervalid()

# question 1
#  not using life-line
    elif x=="2":   #not using life-line
        ans = input("Answer to the Question =>")
        if ans == a:
            print("Correct answer")
            print("Moving to next round")
    #__________________________________
    # question2 starts
    #both life-line available
            b1.q2()
            b1.lifeline()
            x = input("1 => YES\t 2 => NO")
        #q2 using life-line
            if x=="1":
                print("*" * 20)
                print("\tLife-Lines")
                print("1 => 50-50")
                print("2 => Flip the question")
                print("*" * 20)
                l = input("Which life line would you like to use?")
            # q2 using 50-50
                if l=="1":
                    print("Question 2")
                    print("What is 2+2")
                    print("(A) -4 ")
                    print("(B)  ")
                    print("(C) 4")
                    print("(D)  ")
                    a = "c" or "C"
                    ans = input("Answer to the Question =>")
                    if ans == a:
                        print("Correct answer")
                        print("Moving to next round")
                # __________________________________
                # question3 starts
                # flip the question available
                        b1.q3()
                        b1.lifeline()
                        x = input("1 => YES\t 2 => NO")
                    # q3 using life-line
                        if x=="1":
                            print("*" * 20)
                            print("\tLife-Lines")
                            print("50-50 (Already used)")
                            print("1 => Flip the question")
                            print("*" * 20)
                            l = input("Which life line would you like to use?")
                        #q3 using flip the q
                            if l=="1":
                                b1.q6()
                                ans = input("Answer to the Question =>")
                                if ans == a:
                                    print("Correct answer")
                                    print("Moving to next round")
                            # __________________________________
                            # question 4 starts
                            # no life-line available
                                    b1.q4()
                                    print("Both life-lines used")
                                    ans = input("Answer to the Question =>")
                                    if ans == a:
                                        print("Correct answer")
                                        print("Moving to next round")
                                    # ________________________________
                                    # question 5 start
                                        b1.q5()
                                        print("Both life-lines used")
                                        ans = input("Answer to the Question =>")
                                        if ans == a:
                                            print("Correct answer")
                                            b1.won()
                                        else:
                                            print("Wrong answer")
                                            print("sorry your game ends here")
                                            break
                                    # question 5 end
                                    # ________________________________
                                    else:
                                        print("Wrong answer")
                                        print("sorry your game ends here")
                                        break
                            # question 4 ends
                            # __________________________________
                                else:
                                    print("Wrong answer")
                                    print("sorry your game ends here")
                                    break
                            else:
                                b1.entervalid()
                    # q3 not using life-line
                    # flip the question available
                        elif x=="2":
                            ans = input("Answer to the Question =>")
                            if ans == a:
                                print("Correct answer")
                                print("Moving to next round")
                        # __________________________________
                        # question 4 starts
                        # flip the question available
                                b1.q4()
                                b1.lifeline()
                                x = input("1 => YES\t 2 => NO")
                            #q4 using life-line
                                if x=="1":
                                    print("*" * 20)
                                    print("\tLife-Lines")
                                    print("50-50 (Already used)")
                                    print("1 => Flip the question")
                                    print("*" * 20)
                                    l = input("Which life line would you like to use?")
                                # q4 using flip the q
                                    if l=="1":
                                        b1.q6()
                                        ans = input("Answer to the Question =>")
                                        if ans == a:
                                            print("Correct answer")
                                            print("Moving to next round")
                                    # __________________________________
                                    # question 5 starts
                                    # no life-line available
                                            b1.q5()
                                            print("Both life-lines used")
                                            ans = input("Answer to the Question =>")
                                            if ans == a:
                                                print("Correct answer")
                                                b1.won()
                                            else:
                                                print("Wrong answer")
                                                print("sorry your game ends here")
                                                break
                                    # question  ends
                                    # __________________________________
                                        else:
                                            print("Wrong answer")
                                            print("sorry your game ends here")
                                            break
                                    else:
                                        b1.entervalid()
                            # q4 not using life-line
                            # flip the question available
                                elif x=="2":
                                    ans = input("Answer to the Question =>")
                                    if ans == a:
                                        print("Correct answer")
                                        print("Moving to next round")
                                # __________________________________
                                # question 5 starts
                                # flip the question available
                                        b1.q5()
                                        b1.lifeline()
                                        x = input("1 => YES\t 2 => NO")
                                    # q5 using life-line
                                        if x=="1":
                                            print("*" * 20)
                                            print("\tLife-Lines")
                                            print("50-50 (Already used)")
                                            print("1 => Flip the question")
                                            print("*" * 20)
                                            l = input("Which life line would you like to use?")
                                        #q5 using flip the question
                                            if l=="1":
                                                b1.q6()
                                                ans = input("Answer to the Question =>")
                                                if ans == a:
                                                    print("Correct answer")
                                                    b1.won()
                                                else:
                                                    print("Wrong answer")
                                                    print("sorry your game ends here")
                                                    break
                                            else:
                                                b1.entervalid()
                                    #not using life-line
                                        elif x=="2":
                                            ans = input("Answer to the Question =>")
                                            if ans == a:
                                                print("Correct answer")
                                                b1.won()
                                            else:
                                                print("Wrong answer")
                                                print("sorry your game ends here")
                                                break
                                        else:
                                            b1.entervalid()
                                # question 5 ends
                                # __________________________________
                                    else:
                                        print("Wrong answer")
                                        print("sorry your game ends here")
                                        break
                                else:
                                    b1.entervalid()

                        # question 4 ends
                        # __________________________________
                            else:
                                print("Wrong answer")
                                print("sorry your game ends here")
                                break
                        else:
                            b1.entervalid()
                # question3 ends
                # __________________________________
                    else:
                        print("Wrong answer")
                        print("sorry your game ends here")
                        break
            # q2 using flip the question
                #50-50 left
                elif l=="2":
                    b1.q6()
                    ans = input("Answer to the Question =>")
                    if ans == a:
                        print("Correct answer")
                        print("Moving to next round")
                # __________________________________
                # question 3 starts
                # 50-50 available
                        b1.q3()
                        b1.lifeline()
                        x = input("1 => YES\t 2 => NO")
                    # q3 using life-line
                        if x=="1":
                            print("*" * 20)
                            print("\tLife-Lines")
                            print("1 => 50-50 ")
                            print("Flip the question (Already used)")
                            print("*" * 20)
                            l = input("Which life line would you like to use?")
                    #q3 using 50-50
                            if l=="1":
                                print("You have choose 50-50 life-line")
                                print("Question 3")
                                print("What is 22-33=")
                                print("(A) -10 ")
                                print("(B) -11")
                                print("(C)    ")
                                print("(D)    ")
                                a = "b" or "B"
                                ans = input("Answer to the Question =>")
                                if ans == a:
                                    print("Correct answer")
                                    print("Moving to next round")
                        # __________________________________
                        # question 4 starts
                        # no life-line left
                                    b1.q4()
                                    print("Both life-lines used")
                                    ans = input("Answer to the Question =>")
                                    if ans == a:
                                        print("Correct answer")
                                        print("Moving to next round")
                            # ________________________________
                            # question 5 start
                                        b1.q5()
                                        print("Both life-lines used")
                                        ans = input("Answer to the Question =>")
                                        if ans == a:
                                            print("Correct answer")
                                            b1.won()
                                        else:
                                            print("Wrong answer")
                                            print("sorry your game ends here")
                                            break
                            # question 5 end
                            # ________________________________
                                    else:
                                        print("Wrong answer")
                                        print("sorry your game ends here")
                                        break
                        # question 4 starts
                        # __________________________________
                                else:
                                    print("Wrong answer")
                                    print("sorry your game ends here")
                                    break
                            else:
                                b1.entervalid()
                    # q3 not using life-line
                    #50-50 available
                        elif x=="2":
                            ans = input("Answer to the Question =>")
                            if ans == a:
                                print("Correct answer")
                                print("Moving to next round")
                        # __________________________________
                        # question 4 starts
                        #50-50 available
                                b1.q4()
                                b1.lifeline()
                                x = input("1 => YES\t 2 => NO")
                            # q4 using life-line
                                if x=="1":
                                    print("*" * 20)
                                    print("\tLife-Lines")
                                    print("1 => 50-50 ")
                                    print("Flip the question (Already used)")
                                    print("*" * 20)
                                    l = input("Which life line would you like to use?")
                                #using 50-50
                                    if l=="1":
                                        print("Question 4")
                                        print("Where is ahmedabad located?")
                                        print("(A) ")
                                        print("(B) Delhi")
                                        print("(C) ")
                                        print("(D) Gujarat")
                                        a = "d" or "D"
                                        ans = input("Answer to the Question =>")
                                        if ans == a:
                                            print("Correct answer")
                                            print("Moving to next round")
                                    # __________________________________
                                    # question 5 starts
                                    # no life-line available
                                            b1.q5()
                                            print("Both life-lines used")
                                            ans = input("Answer to the Question =>")
                                            if ans == a:
                                                print("Correct answer")
                                                b1.won()
                                            else:
                                                print("Wrong answer")
                                                print("sorry your game ends here")
                                                break
                                    # question 5  ends
                                    # __________________________________
                                        else:
                                            print("Wrong answer")
                                            print("sorry your game ends here")
                                            break
                                    else:
                                        b1.entervalid()
                            # q4 not using life-line
                            #50-50available
                                elif x=="2":
                                    ans = input("Answer to the Question =>")
                                    if ans == a:
                                        print("Correct answer")
                                        print("Moving to next round")
                                # __________________________________
                                # question 5 starts
                                # 50-50available
                                        b1.q5()
                                        b1.lifeline()
                                        x = input("1 => YES\t 2 => NO")
                                    # q5 using life-line
                                        if x=="1":
                                            print("*" * 20)
                                            print("\tLife-Lines")
                                            print("1 => 50-50 ")
                                            print("Flip the question (Already used)")
                                            print("*" * 20)
                                            l = input("Which life line would you like to use?")
                                        #q5 using 50-50
                                            if l=="1":
                                                print("Question 5")
                                                print("what is pakistan to India")
                                                print("(A) ")
                                                print("(B) brother")
                                                print("(C) Son")
                                                print("(D) ")
                                                a = "c", "C"
                                                ans = input("Answer to the Question =>")
                                                if ans == a:
                                                    print("Correct answer")
                                                    b1.won()
                                                else:
                                                    print("Wrong answer")
                                                    print("sorry your game ends here")
                                                    break
                                            else:
                                                b1.entervalid()
                                    # q5 without using life-line
                                        elif x=="2":
                                            ans = input("Answer to the Question =>")
                                            if ans == a:
                                                print("Correct answer")
                                                b1.won()
                                            else:
                                                print("Wrong answer")
                                                print("sorry your game ends here")
                                                break
                                        else:
                                            b1.entervalid()
                                # question 5  ends
                                # __________________________________
                                    else:
                                        print("Wrong answer")
                                        print("sorry your game ends here")
                                        break
                                else:
                                    b1.entervalid()

                        # question 4 starts
                        # __________________________________
                            else:
                                print("Wrong answer")
                                print("sorry your game ends here")
                                break
                        else:
                            b1.entervalid()
                # question 3 ends
                # __________________________________
                    else:
                        print("Wrong answer")
                        print("sorry your game ends here")
                        break
                else:
                    b1.entervalid()

        # q2 not using life-line
        #both life line available
            elif x=="2":
                ans = input("Answer to the Question =>")
                if ans == a:
                    print("Correct answer")
                    print("Moving to next round")
            # __________________________________
            # question 3 starts
            # both life-line available
                    b1.q3()
                    b1.lifeline()
                    x = input("1 => YES\t 2 => NO")
                #q3 using life-line
                    if x=="1":
                        print("*" * 20)
                        print("\tLife-Lines")
                        print("1 => 50-50")
                        print("2 => Flip the question")
                        print("*" * 20)
                        l = input("Which life line would you like to use?")
                    #q3 using 50-50
                    #flip the question left
                        if l=="1":
                            print("Question 3")
                            print("What is 22-33=")
                            print("(A)  ")
                            print("(B) -11")
                            print("(C) ")
                            print("(D) 11")
                            a = "b" or "B"
                            ans = input("Answer to the Question =>")
                            if ans == a:
                                print("Correct answer")
                                print("Moving to next round")
                            # __________________________________
                            # question 4 starts
                                b1.q4()
                                b1.lifeline()
                                x = input("1 => YES\t 2 => NO")
                            # q4 using life-line
                                if x=="1":
                                    print("*" * 20)
                                    print("\tLife-Lines")
                                    print("50-50 (Already used)")
                                    print("1 => Flip the question")
                                    print("*" * 20)
                                    l = input("Which life line would you like to use?")
                                    if l=="1":
                                        b1.q6()
                                        ans = input("Answer to the Question =>")
                                        if ans == a:
                                            print("Correct answer")
                                            print("Moving to next round")
                                # __________________________________
                                # question 5 starts
                                # no life-line
                                            b1.q5()
                                            print("Both life-lines used")
                                            ans = input("Answer to the Question =>")
                                            if ans == a:
                                                print("Correct answer")
                                                b1.won()
                                            else:
                                                print("Wrong answer")
                                                print("sorry your game ends here")
                                                break
                                # question 5  ends
                                # __________________________________
                                        else:
                                            print("Wrong answer")
                                            print("sorry your game ends here")
                                            break
                                    else:
                                        b1.entervalid()
                            # q4 without using life-line
                                elif x=="2":
                                    ans = input("Answer to the Question =>")
                                    if ans == a:
                                        print("Correct answer")
                                        print("Moving to next round")
                                    # __________________________________
                                    # question 5 starts
                                    # flip the question available
                                        b1.q5()
                                        b1.lifeline()
                                        x = input("1 => YES\t 2 => NO")
                                        # q5 using life-line
                                        if x == 1:
                                            print("*" * 20)
                                            print("\tLife-Lines")
                                            print("50-50 (Already used)")
                                            print("1 => Flip the question")
                                            print("*" * 20)
                                            l = input("Which life line would you like to use?")
                                            # q5 using flip the question
                                            if l == 1:
                                                b1.q6()
                                                ans = input("Answer to the Question =>")
                                                if ans == a:
                                                    print("Correct answer")
                                                    b1.won()
                                                else:
                                                    print("Wrong answer")
                                                    print("sorry your game ends here")
                                                    break
                                            else:
                                                b1.entervalid()
                                        # not using life-line
                                        elif x == 2:
                                            ans = input("Answer to the Question =>")
                                            if ans == a:
                                                print("Correct answer")
                                                b1.won()
                                            else:
                                                print("Wrong answer")
                                                print("sorry your game ends here")
                                                break
                                        else:
                                            b1.entervalid()
                                    # question 5  ends
                                    # __________________________________
                                    else:
                                        print("Wrong answer")
                                        print("sorry your game ends here")
                                        break
                                else:
                                    b1.entervalid()
                            # question 4 ends
                            # __________________________________
                            else:
                                print("Wrong answer")
                                print("sorry your game ends here")
                                break
                    # q3 with using flip the question
                    # 50-50 available
                        elif l=="2":
                            b1.q3()
                            b1.lifeline()
                            x = input("1 => YES\t 2 => NO")
                        # q3 using life-line
                            if x=="1":
                                print("*" * 20)
                                print("\tLife-Lines")
                                print("1 => 50-50 ")
                                print("Flip the question (Already used)")
                                print("*" * 20)
                                l = input("Which life line would you like to use?")
                            # q3 using 50-50
                                if l=="1":
                                    print("Question 3")
                                    print("What is 22-33=")
                                    print("(A)  ")
                                    print("(B) -11")
                                    print("(C) 10")
                                    print("(D) ")
                                    a = "b" or "B"
                                    ans = input("Answer to the Question =>")
                                    if ans == a:
                                        print("Correct answer")
                                        print("Moving to next round")
                                # __________________________________
                                # question 4 starts
                                # no life-line left
                                        b1.q4()
                                        print("Both life-lines used")
                                        ans = input("Answer to the Question =>")
                                        if ans == a:
                                            print("Correct answer")
                                            print("Moving to next round")
                                    # ________________________________
                                    # question 5 start
                                            b1.q5()
                                            print("Both life-lines used")
                                            ans = input("Answer to the Question =>")
                                            if ans == a:
                                                print("Correct answer")
                                                b1.won()
                                            else:
                                                print("Wrong answer")
                                                print("sorry your game ends here")
                                                break
                                    # question 5 end
                                    # ________________________________
                                        else:
                                            print("Wrong answer")
                                            print("sorry your game ends here")
                                            break
                                # question 4 starts
                                # __________________________________
                                    else:
                                        print("Wrong answer")
                                        print("sorry your game ends here")
                                        break
                                else:
                                    b1.entervalid()
                        # q3 without using life-line
                        # 50-50 available
                            elif x=="2":
                                ans = input("Answer to the Question =>")
                                if ans == a:
                                    print("Correct answer")
                                    print("Moving to next round")
                            #____________________________________
                            #question 4 start
                            # 50-50 available
                                    b1.q4()
                                    b1.lifeline()
                                    x = input("1 => YES\t 2 => NO")
                                # q4 using life-line
                                    if x=="1":
                                        print("*" * 20)
                                        print("\tLife-Lines")
                                        print("1 => 50-50 ")
                                        print("Flip the question (Already used)")
                                        print("*" * 20)
                                        l = input("Which life line would you like to use?")
                                    #q4 using 50-50
                                        if l=="1":
                                            print("Question 4")
                                            print("Where is ahmedabad located?")
                                            print("(A)  ")
                                            print("(B) Delhi")
                                            print("(C) ")
                                            print("(D) Gujarat")
                                            a = "d" or "D"
                                            ans = input("Answer to the Question =>")
                                            if ans == a:
                                                print("Correct answer")
                                                print("Moving to next round")
                                        # ________________________________
                                        # question 5 start
                                        # no life-line
                                                b1.q5()
                                                print("Both life-lines used")
                                                ans = input("Answer to the Question =>")
                                                if ans == a:
                                                    print("Correct answer")
                                                    b1.won()
                                                else:
                                                    print("Wrong answer")
                                                    print("sorry your game ends here")
                                                    break
                                        # question 5 end
                                        # ________________________________
                                            else:
                                                print("Wrong answer")
                                                print("sorry your game ends here")
                                                break
                                        else:
                                            b1.entervalid()
                                # q4 without using life-line
                                # 50-50 available
                                    elif x=="2":
                                        ans = input("Answer to the Question =>")
                                        if ans == a:
                                            print("Correct answer")
                                            print("Moving to next round")
                                    # ________________________________
                                    # question 5 start
                                    # 50-50 available
                                            b1.q5()
                                            b1.lifeline()
                                            x = input("1 => YES\t 2 => NO")
                                        #q5 using life-line
                                            if x=="1":
                                                print("*" * 20)
                                                print("\tLife-Lines")
                                                print("1 => 50-50 ")
                                                print("Flip the question (Already used)")
                                                print("*" * 20)
                                                l = input("Which life line would you like to use?")
                                            # q5 using 50-50
                                                if l=="1":
                                                    print("Question 5")
                                                    print("what is pakistan to India")
                                                    print("(A)  ")
                                                    print("(B) brother")
                                                    print("(C) Son")
                                                    print("(D) ")
                                                    a = "c", "C"
                                                    ans = input("Answer to the Question =>")
                                                    if ans == a:
                                                        print("Correct answer")
                                                        b1.won()
                                                    else:
                                                        print("Wrong answer")
                                                        print("sorry your game ends here")
                                                        break
                                                else:
                                                    b1.entervalid()
                                        # q5 without using life-line
                                        # 50-50 available
                                            elif x=="2":
                                                ans = input("Answer to the Question =>")
                                                if ans == a:
                                                    print("Correct answer")
                                                    b1.won()
                                                else:
                                                    print("Wrong answer")
                                                    print("sorry your game ends here")
                                                    break
                                            else:
                                                b1.entervalid()
                                    # question 5 end
                                    # ________________________________
                                        else:
                                            print("Wrong answer")
                                            print("sorry your game ends here")
                                            break
                                    else:
                                        b1.entervalid()
                            # question 4 end
                            # ____________________________________
                                else:
                                    print("Wrong answer")
                                    print("sorry your game ends here")
                                    break
                            else:
                                b1.entervalid()
                        else:
                            b1.entervalid()
                # q3 without using life-line
                # both life-line available
                    elif x=="2":
                        ans = input("Answer to the Question =>")
                        if ans == a:
                            print("Correct answer")
                            print("Moving to next round")
                    # __________________________________
                    # question 4 starts here
                    # both life-line available
                            b1.q4()
                            b1.lifeline()
                            x = input("1 => YES\t 2 => NO")
                        #q4 using life-line
                            if x=="1":
                                print("*" * 20)
                                print("\tLife-Lines")
                                print("1 => 50-50 ")
                                print("2 => Flip the question")
                                print("*" * 20)
                                l = input("Which life line would you like to use?")
                            #q4 using 50-50(flip left)
                                if l=="1":
                                    b1.q6()
                                    ans = input("Answer to the Question =>")
                                    if ans == a:
                                        print("Correct answer")
                                        print("Moving to next round")
                                # __________________________________
                                # question 5 starts here
                                # flip the question life-line available
                                        b1.q5()
                                        b1.lifeline()
                                        x = input("1 => YES\t 2 => NO")
                                    # q5 using life-line
                                        if x == 1:
                                            print("*" * 20)
                                            print("\tLife-Lines")
                                            print("50-50 (Already used)")
                                            print("1 => Flip the question")
                                            print("*" * 20)
                                            l = input("Which life line would you like to use?")
                                        # q5 using flip the question
                                            if l == 1:
                                                b1.q6()
                                                ans = input("Answer to the Question =>")
                                                if ans == a:
                                                    print("Correct answer")
                                                    b1.won()
                                                else:
                                                    print("Wrong answer")
                                                    print("sorry your game ends here")
                                                    break
                                            else:
                                                b1.entervalid()
                                        # not using life-line
                                        elif x == 2:
                                            ans = input("Answer to the Question =>")
                                            if ans == a:
                                                print("Correct answer")
                                                b1.won()
                                            else:
                                                print("Wrong answer")
                                                print("sorry your game ends here")
                                                break
                                        else:
                                            b1.entervalid()
                                # question 5 ends
                                # __________________________________
                                    else:
                                        print("Wrong answer")
                                        print("sorry your game ends here")
                                        break
                            #q4 using flip the question life-line(50-50 left)
                                elif l=="2":
                                    b1.q6()
                                    ans = input("Answer to the Question =>")
                                    if ans == a:
                                        print("Correct answer")
                                        print("Moving to next round")
                                # __________________________________
                                # question 5 starts here
                                # 50-50 available
                                        b1.q5()
                                        b1.lifeline()
                                        x = input("1 => YES\t 2 => NO")
                                    # q5 using life-line
                                        if x == 1:
                                            print("*" * 20)
                                            print("\tLife-Lines")
                                            print("1 => 50-50 ")
                                            print("Flip the question (Already used)")
                                            print("*" * 20)
                                            l = input("Which life line would you like to use?")
                                        # q5 using 50-50
                                            if l == 1:
                                                print("Question 5")
                                                print("what is pakistan to India")
                                                print("(A) ")
                                                print("(B) brother")
                                                print("(C) Son")
                                                print("(D) ")
                                                a = "c", "C"
                                                ans = input("Answer to the Question =>")
                                                if ans == a:
                                                    print("Correct answer")
                                                    b1.won()
                                                else:
                                                    print("Wrong answer")
                                                    print("sorry your game ends here")
                                                    break
                                            else:
                                                b1.entervalid()
                                        # q5 without using life-line
                                        elif x == 2:
                                            ans = input("Answer to the Question =>")
                                            if ans == a:
                                                print("Correct answer")
                                                b1.won()
                                            else:
                                                print("Wrong answer")
                                                print("sorry your game ends here")
                                                break
                                        else:
                                            b1.entervalid()
                                # question 5 ends
                                # __________________________________
                                    else:
                                        print("Wrong answer")
                                        print("sorry your game ends here")
                                        break
                                else:
                                    b1.entervalid()
                        # q4 without using life-line
                        # both life-line available
                            elif x=="2":
                                b1.q4()
                                b1.lifeline()
                                x = input("1 => YES\t 2 => NO")
                            #q4 using life-line
                                if x=="1":
                                    print("*" * 20)
                                    print("\tLife-Lines")
                                    print("1 => 50-50 ")
                                    print("2 => Flip the question")
                                    print("*" * 20)
                                    l = input("Which life line would you like to use?")
                                # q4 using 50-50 (flip the q left)
                                    if l=="1":
                                        print("Question 4")
                                        print("Where is ahmedabad located?")
                                        print("(A)  ")
                                        print("(B) Delhi")
                                        print("(C) ")
                                        print("(D) Gujarat")
                                        a = "d" or "D"
                                        ans = input("Answer to the Question =>")
                                        if ans == a:
                                            print("Correct answer")
                                            print("Moving to next round")
                                        # __________________________________
                                        # question 5 ends
                                        # flip the question life-line available
                                            b1.q5()
                                            b1.lifeline()
                                            x = input("1 => YES\t 2 => NO")
                                            # q5 using life-line
                                            if x == 1:
                                                print("*" * 20)
                                                print("\tLife-Lines")
                                                print("50-50 (Already used)")
                                                print("1 => Flip the question")
                                                print("*" * 20)
                                                l = input("Which life line would you like to use?")
                                            # q5 using flip the question
                                                if l == 1:
                                                    b1.q6()
                                                    ans = input("Answer to the Question =>")
                                                    if ans == a:
                                                        print("Correct answer")
                                                        b1.won()
                                                    else:
                                                        print("Wrong answer")
                                                        print("sorry your game ends here")
                                                        break
                                                else:
                                                    b1.entervalid()
                                            # not using life-line
                                            elif x == 2:
                                                ans = input("Answer to the Question =>")
                                                if ans == a:
                                                    print("Correct answer")
                                                    b1.won()
                                                else:
                                                    print("Wrong answer")
                                                    print("sorry your game ends here")
                                                    break
                                            else:
                                                b1.entervalid()
                                        # question 5 ends
                                        # __________________________________
                                        else:
                                            print("Wrong answer")
                                            print("sorry your game ends here")
                                            break
                                # q4 using flip (50-50 remain)
                                    elif l=="2":
                                        b1.q6()
                                        ans = input("Answer to the Question =>")
                                        if ans == a:
                                            print("Correct answer")
                                            print("Moving to next round")
                                    # __________________________________
                                    # question 5 starts here
                                    # 50-50 available
                                            b1.q5()
                                            b1.lifeline()
                                            x = input("1 => YES\t 2 => NO")
                                        # q5 using life-line
                                            if x == 1:
                                                print("*" * 20)
                                                print("\tLife-Lines")
                                                print("1 => 50-50 ")
                                                print("Flip the question (Already used)")
                                                print("*" * 20)
                                                l = input("Which life line would you like to use?")
                                            # q5 using 50-50
                                                if l == 1:
                                                    print("Question 5")
                                                    print("what is pakistan to India")
                                                    print("(A) ")
                                                    print("(B) brother")
                                                    print("(C) Son")
                                                    print("(D) ")
                                                    a = "c", "C"
                                                    ans = input("Answer to the Question =>")
                                                    if ans == a:
                                                        print("Correct answer")
                                                        b1.won()
                                                    else:
                                                        print("Wrong answer")
                                                        print("sorry your game ends here")
                                                        break
                                                else:
                                                    b1.entervalid()
                                        # q5 without using life-line
                                            elif x == 2:
                                                ans = input("Answer to the Question =>")
                                                if ans == a:
                                                    print("Correct answer")
                                                    b1.won()
                                                else:
                                                    print("Wrong answer")
                                                    print("sorry your game ends here")
                                                    break
                                            else:
                                                b1.entervalid()
                                # question 5 ends
                                # __________________________________
                                        else:
                                            print("Wrong answer")
                                            print("sorry your game ends here")
                                            break
                                    else:
                                        b1.entervalid()
                            # q4 without using life-line
                            # both life-line available
                                elif x=="2":
                                    ans = input("Answer to the Question =>")
                                    if ans == a:
                                        print("Correct answer")
                                        print("Moving to next round")
                                # __________________________________
                                # question 5 starts here
                                # both life-line available
                                        b1.q5()
                                        b1.lifeline()
                                        x = input("1 => YES\t 2 => NO")
                                    # q5 using life-line
                                        if x=="1":
                                            print("*" * 20)
                                            print("\tLife-Lines")
                                            print("1 => 50-50")
                                            print("2 => Flip the question")
                                            print("*" * 20)
                                            l = input("Which life line would you like to use?")
                                        # q5 using 50-50
                                            if l=="1":
                                                print("Question 5")
                                                print("what is pakistan to India")
                                                print("(A) ")
                                                print("(B) brother")
                                                print("(C) Son")
                                                print("(D) ")
                                                a = "c", "C"
                                                ans = input("Answer to the Question =>")
                                                if ans == a:
                                                    print("Correct answer")
                                                    b1.won()
                                                else:
                                                    print("Wrong answer")
                                                    print("sorry your game ends here")
                                                    break
                                        #q5 using flip the question
                                            elif l=="2":
                                                b1.q6()
                                                ans = input("Answer to the Question =>")
                                                if ans == a:
                                                    print("Correct answer")
                                                    b1.won()
                                                else:
                                                    print("Wrong answer")
                                                    print("sorry your game ends here")
                                                    break
                                            else:
                                                b1.entervalid()
                                    # q5 without using life-line
                                        elif x=="2":
                                            ans = input("Answer to the Question =>")
                                            if ans == a:
                                                print("Correct answer")
                                                b1.won()
                                            else:
                                                print("Wrong answer")
                                                print("sorry your game ends here")
                                                break
                                        else:
                                            b1.entervalid()

                                # question 5 ends
                                # __________________________________
                                    else:
                                        print("Wrong answer")
                                        print("sorry your game ends here")
                                        break
                                else:
                                    b1.entervalid()

                            else:
                                b1.entervalid()
                    # question 4 ends
                    # __________________________________
                        else:
                            print("Wrong answer")
                            print("sorry your game ends here")
                            break
                    else:
                        b1.entervalid()
            # question 3 ends
            # __________________________________
                else:
                    print("Wrong answer")
                    print("sorry your game ends here")
                    break
            else:
                b1.entervalid()
    #question2 ends
    #__________________________________

        else:
            print("Wrong answer")
            print("sorry your game ends here")
            break
    else:
        b1.entervalid()