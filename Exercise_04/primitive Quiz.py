score = 0
 
question = input("What is the capital of France")                       #input is for user to write the answer
if question.lower() == "paris":                                          #.lower() so if the user write the answer in small alphabet be acceptable
    print("correct")
    scoer = score + 1                                                    # +1 it will increase the score if answer will be correct
else:
    print("wrong")
question = input("What is the capital of Pakistan")                       
if question.lower() == "islamabad":                                         #repeating the steps again
    print("correct")
    scoer = score + 1                                                    #repeating the steps again
else:
    print("wrong") 
question = input("What is the capital of India")                       
if question.lower() == "new delhi":                                         #repeating the steps again
    print("correct")
    scoer = score + 1                                                    #repeating the steps again
else:
    print("wrong") 
question = input("What is the capital of Germany")                       #repeating the steps again
if question.lower() == "berlin":                                         #repeating the steps again
    print("correct")
    scoer = score + 1                                                    #repeating the steps again
else:
    print("wrong") 
question = input("What is the capital of United States")                       #repeating the steps again
if question.lower() == "washington,d.c.":                                         #repeating the steps again
    print("correct")
    scoer = score + 1                                                         #repeating the steps again
else:
    print("wrong") 
question = input("What is the capital of United Kingdom")                       #repeating the steps again
if question.lower() == "london":                                         #repeating the steps again
    print("correct")
    scoer = score + 1                                                    #repeating the steps again
else:
    print("wrong") 
question = input("What is the capital of Turkey")                       #repeating the steps again
if question.lower() == "ankara":                                         #repeating the steps again
    print("correct")
    scoer = score + 1                                                    #repeating the steps again
else:
    print("wrong") 
question = input("What is the capital of Uzbekistan")                       #repeating the steps again
if question.lower() == "tashkent":                                         #repeating the steps again
    print("correct")
    scoer = score + 1                                                    #repeating the steps again
else:
    print("wrong") 
question = input("What is the capital of Saudia")                       #repeating the steps again
if question.lower() == "riyadh":                                         #repeating the steps again
    print("correct")
    scoer = score + 1                                                    #repeating the steps again
else:
    print("wrong") 
question = input("What is the capital of Bangladesh")                       #repeating the steps again
if question.lower() == "dhaka":                                         #repeating the steps again
    print("correct")
    scoer = score + 1                                                    #repeating the steps again
else:
    print("wrong") 
print("Your total score is:",score,"/10")                                #It will give the total score of the users answers.
