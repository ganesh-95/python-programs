# to generate random numbers
import random



   print random.random()*100  # between 0 to 100

 print random.random()*100-5 # between 5 to 95

 print random.choice([i for i in range(11) if i%2 == 0]) # random even number between 0 to 10

print random.choice([i for i in range(201) if i%5 == 0 and i%7 == 0]) #random number divisible by both 5 & 7 upto 200


print random.sample([i for i in range(100,201), 5]) # 5 random numbers between 100 to 200

print random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5) # 5 random numbers between 1 to 1000 divisible by  both 5 and 7
