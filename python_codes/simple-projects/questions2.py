#questions
def my_function(*score):
    score = 0
    quiz = input("who is kenyan president? ")
    
    if quiz == "ruto":
        print("correct")
        score +=1
    else:
        print("wrong")
    print(score)
    
    while True:
        name = input("do you want to continue? (Y/N)")
        if name == "Y":
            my_function()
            continue
        else:
            break
my_function()