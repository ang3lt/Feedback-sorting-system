#Function that takes the feedback and verifies it is over 10 characters.
def Input_feedback():
    Valid = False
    
    while not Valid:
        fb = input("Please enter your feedback here: ")
        
        if len(fb) > 10:
            print("Your feedback was sucessfully recorded! Thank you.")
            Valid = True
            return fb
        
        else:
            Valid = False
            print("Please make your feedback longer! ")



#Takes a number for the rating that is between 1 and 5, if it isn't tbe user is forced to try again
def Input_rating():
    Valid = False
    
    while not Valid:
        rating = int(input("What would you rate our business from 1 to 5? "))
        
        if rating < 6 and rating > 0:
            Valid = True
            print("Your rating was sucessfully recorded! ")
            return rating
        
        else:
            Valid = False
            print("Please enter a number between 1 and 5")



#Definition of variables and two dictionaries with good and bad words.
pos = 0
neg = 0
neu = 0

positive = 0
negative = 0

goodWords = ["good", "happy", "pleased", "amazing", "best", "positive", "excellent"]
badWords = ["bad", "dislike", "hate", "horrible", "negative", "poor"]



#Counts the amount of positive and negative words in the feedback.
def Analysis(fb, goodWords, badWords, positive, negative):
        for i in range (0, len(goodWords)):
            if goodWords[i] in fb.split(" "):
                positive = positive + 1
                return positive
        
        for x in range(0, len(badWords)):
            if badWords[x] in fb.split(" "):
                negative = negative + 1
                return negative
        


#Counts the amount of words in the feedback.
def Word_Counter(fb):
    words = (len(fb.strip().split(" ")))
    
    return words



#Using the amount of positive and negative words, it decides if the feedback is positive, negative or neutral.
def Decision_Making(positive, negative, pos, neg):
    if positive > negative:
        print("""Analysing feedback....                    
              
              
              
              Feednack is positive""")
        pos = pos + 1
        return pos
    
    
    elif negative > positive:
        print(""" Analysing feedback....             
              
              
              
              Feedback is negative""")
        neg = neg + 1
        return neg

    
    else:
        print(""" Analysing feedback....
              
              
              
              Feedback is neutral""")
        
       
#Main program
print("Welcome to our feedback system! ")                                                                                                                                                                                                                                                                                                                           
#Putting functions into variables.
Feedback = Input_feedback()
Rating = Input_rating()
Words = Word_Counter(Feedback)
Analyzing = Analysis(Feedback, goodWords, badWords, positive, negative)
Decision = Decision_Making(positive, negative, pos, neg)



#Calling all the functions and printing the summary.
print("Feednack: "+Feedback)
print("Rating: "+str(Rating))

if pos > 1:
    print("Positive")

elif neg > 1:
    print("Negative")

else:
    print("Neutral")
print("Word count: "+str(Words))