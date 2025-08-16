print("welcome to crazy quiz app!")

ready = input("are you ready to play?  ")  # here we have input came from user 



if ready.lower() != "yes":
    print("ok no problem write 'yes' to play.")
    quit()
0fvvvvvvvv
gggggggg
score = 0



question_1 = input("Who made Python? ")


if question_1.lower() == "guido van rossum":
    print("ok good job! it's correct.")
    score+=1
else: print("its wrong! try again.")

question_2 = input("What does HTML stand for? ")
if question_2 == "hypertext markup language":
    print("thats correct.")
    score+=1

else: print("its wrong! try again.")

question_3 = input("What does CSS stand for? ")
if question_3 == "cascadding style sheets":
    print("thats correct.")
    score+=1
else: print("its wrong! try again.")


question_4 = input("What is the capital of India? ")
if question_4 == "new delhi":
    print("thats correct.")
    score+=1
else: print("its wrong! try again.")

question_5 = input("What is 2 + 2? ")
if question_5 == 4:
    print("thats correct.")
    score+=1
else: print("its wrong! try again.")
question_6 = input("Which planet is known as the Red Planet? ")
if question_6 == "mars":
    print("thats correct.")
    score+=1
else: print("its wrong! try again.")

question_7 = input("Who is the founder of Facebook? ")
if question_7 == "mark zuckerburg":
    print("thats correct.")
    score+=1
else: print("its wrong! try again.")

question_8 = input("In which year was Python released? ")
if question_8 == 1991:
    print("thats correct.")
    score+=1
else: print("its wrong! try again.")

question_9 = input("Which company created the Windows OS? ")
if question_9 == "microsoft":
    print("thats correct.")
    score+=1

else: print("its wrong! try again.")

question_10 = input("What language is most commonly used for Android app development? ")
if question_10 == "java":
    print("thats correct.")
    score+=1





else: print("its wrong! try again.")


print("you have correct quizs ",score)



