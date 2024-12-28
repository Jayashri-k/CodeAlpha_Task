import nltk
from nltk.tokenize import word_tokenize
import random
import time

#downloaded NLTK using cmd prompt 
#nltk.download('punkt_tab')

#function to process and tokenize input
def process_input(text):
    tokens=word_tokenize(text.lower())  #convert input to lowercase for case-insensitive matching
    return tokens

#simple response function with using tokenization
def respond():
    print(" HELLO ! THIS IS A SIMPLE CHATBOX\n\n\t Instructions: \n")
    print("1.IT CAN RESPOND  TO GREETINGS\n"
          "2.GIVE MOTIVATIONAL QUOTES\n"
          "3.PROVIDE CURRENT TIME\n"
          "4.MOVIE RECOMMENDATIONS\n"
          "5.PROVIDE HELP\n"
          "6.A DEFAULT RESPONSE TO UNKNOWN QUERIES\n"
          "7.TO EXIT GIVE 1 AS YOUR INPUT \n")
    while True:
        user_input=input("You: ")
        tokens=process_input(user_input)

        #exit the CHATBOT when user gives 1 as input
        if '1' in tokens:
            print("Exiting!")
            break
        
        #Greetings Response
        elif 'hello' in tokens or 'hi' in tokens or 'hey' in tokens:
            print("Hey there!")

        elif 'bye' in tokens or 'good bye' in tokens:
            print("TAKE CARE ! SEE YOU LATER")
              
        elif 'sup' in tokens or 'how is it going' in tokens:
            print("I'm fine, how about you!")

        elif 'fine' in tokens or 'good' in tokens:
            print("ha ! Good to know ")
        
        #Motivstional response
        elif 'sad' in tokens or 'bad' in tokens or 'motivation' in tokens:
            quotes=["DONT WORRY","IT WILL HAPPEN GOOD","IT WILL CHANGE","BELEIVE YOURSELF"]
            print(random.choice(quotes))
        
        #time response
        elif 'what time' in tokens or 'time' in tokens:
            print("The current time is: ", time.strftime("%H:%M:%S"))
        
        #Help response
        elif 'help' in tokens or 'need help' in tokens:
            print("I'm here to help!")

        #movie response
        elif 'movie' in tokens or 'suggest' in tokens:
            m=["BABY JOHN - HINDI","G.O.A.T - TAMIL","KALKI 2898 AD - TELUGU","MANJUMMEL BOYS - MALAYALAM","K.G.F - KANNADA"]
            print(random.choice(m))

        
        #Default response if none matches
        else:
            print("Sorry! I'm not programmed for your query")

#Start the conversation
respond()
