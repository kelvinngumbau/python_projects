#finally statement

#it executes some code no matter whats happen in between
try:
    print(10/0)
except:
    print("zero devision Error")
finally:
    print("Always Excuted!")
    