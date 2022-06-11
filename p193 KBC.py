# 5 ques
##life line 50-50 flip the question

class questions:
    def q1(self):
        print("Question 1")
        print("In which continent is india located?")
        print("(A) Asia ")
        print("(B) Africa")
        print("(C) North America")
        print("(D) Europe")
        a="a"or"A"

    def q2(self):
        print("Question 2")
        print("What is 2+2")
        print("(A) -4 ")
        print("(B) 0")
        print("(C) 4")
        print("(D) 6")
        a = "c" or "C"

    def q3(self):
        print("Question 3")
        print("What is 22-33=")
        print("(A) -10 ")
        print("(B) -11")
        print("(C) 10")
        print("(D) 11")
        a = "b"or "B"

    def q4(self):
        print("Question 4")
        print("Where is ahmedabad located?")
        print("(A) Maharastra ")
        print("(B) Delhi")
        print("(C) Tamil Nadu")
        print("(D) Gujarat")
        a = "d"or"D"

    def q5(self):
        print("Question 4")
        print("what is pakistan to India")
        print("(A) friend ")
        print("(B) brother")
        print("(C) Son")
        print("(D) father")
        a = "c", "C"

    def q6(self):
        print("you have choose flip the question")
        print("by which other name is india also known?")
        print("(A) pakistan ")
        print("(B) Bharat")
        print("(C) Hindu")
        print("(D) Bha")
        a="b"or"B"

    def lifeline(self):
        print("Do you want to use life line?")
        x = input("1 => YES\t 2 => NO")


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




print("Question 1")
print("In which continent is india located?")
print("(A) Asia ")
print("(B) Africa")
print("(C) North America")
print("(D) Europe")

print("Do you want to use life line?")
x=input("1 => YES\t 2 => NO")
if x=="1":
    print("*" * 20)
    print("\tLife-Lines")
    print("1 => 50-50")
    print("2 => Flip the question")
    print("*" * 20)
    l=input("Which life line would you like to use?")
    if l=="1":
        print("You have choose 50-50")
        print("Question 1")
        print("In which continent is india located?")
        print("(A) Asia ")
        print("(B) ")
        print("(C) North America")
        print("(D) ")
        a = input("Your answer =>")
        if (a == "a" or a == "A"):
            print("Correct Answer")
            print("congratulaions")
            print("Next Round")

            #2nd question

            print("Question 2")
            print("What is 2+2")
            print("(A) -4 ")
            print("(B) 0")
            print("(C) 4")
            print("(D) 6")

            print("Do you want to use life line?")
            x = input("1 => YES\t 2 => NO")
            if x == "1":
                print("*" * 20)
                print("\tLife-Lines")
                print("1 => Flip the question")
                print("*" * 20)
                l = input("Which life line would you like to use?")
                if l == "1":
                    print("you have choose flip the question")
                    print("Question 1")
                    print("by which other name is india also known?")
                    print("(A) pakistan ")
                    print("(B) Bharat")
                    print("(C) Hindu")
                    print("(D) Bha")
                    a = input("Your answer =>")
                    if (a == "b" or a == "B"):
                        print("Correct Answer")
                        print("congratulaions")
                        print("Next Round")

                        # 3rd question

                        print("Question 3")
                        print("What is 22-33=")
                        print("(A) -10 ")
                        print("(B) -11")
                        print("(C) 10")
                        print("(D) 11")

                        print("You don't have any life-line left.")

                        a = input("Your answer =>")
                        if (a == "b" or a == "B"):
                            print("Correct Answer")
                            print("congratulaions")
                            print("Next Round")

                            # round4

                            print("Question 4")
                            print("Where is ahmedabad located?")
                            print("(A) Maharastra ")
                            print("(B) Delhi")
                            print("(C) Tamil Nadu")
                            print("(D) Gujarat")

                            print("You don't have any life-line left.")

                            a = input("Your answer =>")
                            if (a == "d" or a == "D"):
                                print("Correct Answer")
                                print("congratulaions")
                                print("Next Round")

                                # round5

                                print("Question 4")
                                print("what is pakistan to India")
                                print("(A) friend ")
                                print("(B) brother")
                                print("(C) Son")
                                print("(D) father")

                                print("You don't have any life-line left.")

                                a = input("Your answer =>")
                                if (a == "c" or a == "C"):
                                    print("*" * 30)
                                    print("*" * 30)
                                    print("Correct Answer")
                                    print("congratulaions")
                                    print("You have won the game")
                                    print("*"*30)
                                    print("*"*30)

                                elif (a == "d" or a == "D" or a == "a" or a == "A" or a == "b" or a == "B"):
                                    print("Wrong Answer")
                                    print("I'm Sorry your game ends here.")
                                    print("Bye")
                                else:
                                    print("choose a valid option")

                            elif (a == "c" or a == "C" or a == "a" or a == "A" or a == "b" or a == "B"):
                                print("Wrong Answer")
                                print("I'm Sorry your game ends here.")
                                print("Bye")
                            else:
                                print("choose a valid option")

                        elif (a == "c" or a == "C" or a == "a" or a == "A" or a == "d" or a == "D"):
                            print("Wrong Answer")
                            print("I'm Sorry your game ends here.")
                            print("Bye")
                        else:
                            print("choose a valid option")


                    elif (a == "a" or a == "A" or a == "c" or a == "C" or a == "d" or a == "D"):
                        print("Wrong Answer")
                        print("I'm Sorry your game ends here.")
                        print("Bye")
                    else:
                        print("choose a valid option")

            elif x == "2":
                a = input("Your answer to the question=>")
                if (a == "c" or a == "C"):
                    print("Your Answer (C) 4")
                    print("Correct Answer")
                    print("congratulaions")
                    print("Next Round")

                    # 3rd question



                elif (a == "b" or a == "B" or a == "a" or a == "A" or a == "d" or a == "D"):
                    print("Wrong Answer")
                    print("I'm Sorry your game ends here.")
                    print("Bye")
                else:
                    print("choose a valid option")

        elif (a == "b" or a == "B" or a == "c" or a == "C" or a == "d" or a == "D"):
            print("Wrong Answer")
            print("I'm Sorry your game ends here.")
            print("Bye")
        else:
            print("choose a valid option")
    elif l=="2":
        print("you have choose flip the question")
        print("Question 1")
        print("by which other name is india also known?")
        print("(A) pakistan ")
        print("(B) Bharat")
        print("(C) Hindu")
        print("(D) Bha")
        a = input("Your answer =>")
        if (a == "b" or a == "B"):
            print("Correct Answer")
            print("congratulaions")
            print("Next Round")

            # 2nd question

            print("Question 2")
            print("What is 2+2")
            print("(A) -4 ")
            print("(B) 0")
            print("(C) 4")
            print("(D) 6")

            print("Do you want to use life line?")
            x = input("1 => YES\t 2 => NO")
            if x == "1":
                print("*" * 20)
                print("\tLife-Lines")
                print("1 => 50-50")
                print("*" * 20)
                l = input("Which life line would you like to use?")
                if l == "1":
                    print("you have choose 50-50")
                    print("Question 2")
                    print("What is 2+2")
                    print("(A)  ")
                    print("(B) 0")
                    print("(C) 4")
                    print("(D)  ")
                    a = input("Your answer =>")
                    if (a == "c" or a == "C"):
                        print("Correct Answer")
                        print("congratulaions")
                        print("Next Round")
                        # 2nd question
                    elif (a == "a" or a == "A" or a == "a" or a == "A" or a == "d" or a == "D"):
                        print("Wrong Answer")
                        print("I'm Sorry your game ends here.")
                        print("Bye")
                    else:
                        print("choose a valid option")
            elif x == "2":
                a = input("Your answer to the question=>")
                if (a == "c" or a == "C"):
                    print("Your Answer (C) 4")
                    print("Correct Answer")
                    print("congratulaions")
                    print("Next Round")

                    # 3rd question



                elif (a == "b" or a == "B" or a == "a" or a == "A" or a == "d" or a == "D"):
                    print("Wrong Answer")
                    print("I'm Sorry your game ends here.")
                    print("Bye")
                else:
                    print("choose a valid option")

        elif (a == "b" or a == "B" or a == "c" or a == "C" or a == "d" or a == "D"):
            print("Wrong Answer")
            print("I'm Sorry your game ends here.")
            print("Bye")
        else:
            print("choose a valid option")


        elif (a == "a" or a == "A" or a == "c" or a == "C" or a == "d" or a == "D"):
            print("Wrong Answer")
            print("I'm Sorry your game ends here.")
            print("Bye")
        else:
            print("choose a valid option")
elif x=="2":
    a=input("Your answer to the question=>")
    if (a=="a" or a=="A"):
        print("Your Answer (A)Asia")
        print("Correct Answer")
        print("congratulaions")
        print("Next Round")
        # 2nd question



    elif (a=="b" or a=="B" or a=="c" or a=="C" or a=="d" or a=="D"):
        print("Wrong Answer")
        print("I'm Sorry your game ends here.")
        print("Bye")
    else:
        print("choose a valid option")