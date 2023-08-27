#questions in python
def my_function(*score):
    print("only a single name required and it should start with a capital letter")
     
    name = input("who is the president of keny? ")
    score = 0

    if name == "Ruto":
        print("correct")
        score += 1
    else:
        print("wrong")
    quiz = input("who was mother of Jesus? ")

    if quiz == "Mary":
        print("correct")
        score +=1
    else:
        print("wrong")

    quiz2 = int(input("when did Kenya get independence? "))

    if quiz2 == 1963:
        print("correct")
        score +=1
    else:
        print("wrong")

    quiz3 = int(input("which year did Kenyatta die?"))

    if quiz3 == 1978:
        print("correct")
        score +=1
    else:
        print("wrong")

    quiz4 = int(input("How old was kenyatta during his death? "))
    if quiz4 == 78:
        print("correct")
        score +=1
    else:
        print("wrong")

    print("Results: " + str(score))

    if score > 4:
        print("excellent")
    else:
        print("good trial")
    while True:
        repeat = input("do you want to repeat the questions? (Y/N)")
        if repeat == "Y":
            my_function()
            continue
        else:
            print("thank you for your time")
            break
my_function()