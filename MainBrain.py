#import the wikipedia search module
import wikipedia
#import the IPWhois module
from ipwhois import IPWhois
#import the caesarciper module
from caesarcipher import CaesarCipher

#predefinied variables
user_input = ""
number_1 = None
number_2 = None
answer = None
iplookup = None
cipher = None

#start main program loop with exit command "quit"
while user_input != "quit":
    #reset the answer to None
    answer = None
    #get user input
    user_input = input(">> ")

    #define variables
    def wikisearch(criteria):
        #return the summary of the article (this will print 2 sentences)
        return wikipedia.summary(criteria, sentences = 2)
    def whois(ip):
        #set new variable iplookup to the ip of the target
        iplookup = IPWhois(ip)
        #return the details of the ip lookup
        return iplookup.lookup()
    def caesarcrack(message):
        #set new variable cipher equal to the message that you want to crack
        cipher = CaesarCipher(message)
        #return the cracked message
        return cipher.cracked


    #split the user input into each word
    words = user_input.split(' ')
    #search every word in the user input
    for item in words:
        #check to see if the item is a times sign
        if item == 'x' or item == '*':
            #check for numbers to times
            for item in words:
                if item.isdigit() == True:
                    if number_1 == None:
                        number_1 = int(item)
                    elif number_2 == None:
                        number_2 = int(item)
            answer = number_1 * number_2
        #check to see if the item is a division sign
        elif item == '/':
            for item in words:
                if item.isdigit() == True:
                    if number_1 == None:
                        number_1 = int(item)
                    elif number_2 == None:
                        number_2 = int(item)
            answer = number_1 / number_2
        #check to see if the item is a minus
        elif item == '-':
            for item in words:
                if item.isdigit() == True:
                    if number_1 == None:
                        number_1 = int(item)
                    elif number_2 == None:
                        number_2 = int(item)
            answer = number_1 - number_2
        #check to see if the item is a plus
        elif item == '+':
            for item in words:
                if item.isdigit() == True:
                    if number_1 == None:
                        number_1 = int(item)
                    elif number_2 == None:
                        number_2 = int(item)
            answer = number_1 + number_2
    #check if an answer has not been found
    if answer == None:
        if "what is" in user_input:
            #remove what is from the user input
            user_input = user_input.split("what is ")
            #search for the user's criteria
            answer = wikisearch(user_input[1])
        elif "who is" in user_input:
            #remove who is from the user input
            user_input = user_input.split("who is ")
            #search for the user's criteria
            answer = wikisearch(user_input[1])
        elif "who was" in user_input:
            #remove who was from the user input
            user_input = user_input.split("who was ")
            #search for the user's criteria
            answer = wikisearch(user_input[1])
        elif "what was" in user_input:
            #remove what was from the user input
            user_input = user_input.split("what was ")
            #search for the user's criteria
            answer = wikisearch(user_input[1])
        elif "whois" in user_input:
            #remove whois from the user input
            user_input = user_input.split("whois ")
            #lookup the details provided
            answer = whois(user_input[1])
        elif "caesar" in user_input:
            #remove caesar from the user input
            user_input = user_input.split("caesar ")
            #send the cipher to the caesarcrack function
            answer = caesarcrack(user_input[1])
        else:
        	answer = wikisearch(user_input)

    #check if answer is not empty
    if answer != None:
        #print the answer
        print(answer)
