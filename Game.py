import random
import time

MAX_NUMBER = 15
MIN_NUMBER = 3
PROBLEM_STATEMENT = 10
OPERATION = ['+','-','*']
def generate():
    left = random.randint(MIN_NUMBER,MAX_NUMBER)
    right = random.randint(MIN_NUMBER,MAX_NUMBER)
    opearation = random.choice(OPERATION)
    expr = str(left) + " "+ opearation +" "+str(right)
    ans = eval(expr)
    return expr,ans
input("Press Any key to start the Game!!")
print("-----------------------------------")
start_time = time.time()
wrong =0
for i in range(PROBLEM_STATEMENT):
    expr , ans = generate()
    while True:
        guess = input("Problem #" + str(i+1) + " : " + expr +" = ")
        if guess ==str(ans):
            break
        else:
            wrong +=1
end_time = time.time()
total_time  = round(end_time - start_time,2)
print("-------------------------------------")
print("Nice Work! ,Total time taken",total_time,"Seconds!")
print("Count of reattempt",wrong,"Times!")
