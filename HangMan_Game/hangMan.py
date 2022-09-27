import random
import requests
import string

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
wordss = response.content.splitlines()
words = []
rw = []
already_guessed = []
EXIT = "zz"

for k in wordss:
    if len(k) > 5 and len(k) < 12:
        words.append(k)
      
randomWord = list(random.choice(words))
rw = "".join([chr(c) for c in randomWord])
alphabet_string = string.ascii_uppercase + string.ascii_lowercase 
al = list(alphabet_string)
life = len(randomWord)
print ("Welcome to Hang Man game. You will be guessing a word with", len(randomWord), "letters. \nYou have", life, "lives to start with. Let's get started!")
print ("The words were pulled from: ", word_site)
# print (rw)
my_dict = {i:rw.count(i) for i in rw}
# print (my_dict)
final = list("_" * len(rw))
updatedList =""

num = len(randomWord)
game = True
while (game):

    response = input("choose a letter in alphabet (type 'zz' to quit): ")
    if response == EXIT:
        break
    elif response not in al:
        print ("wrong input. Try again.")
        continue
    elif response in already_guessed:
        print ("You have already guessed this letter. Choose another letter. \n")
        continue
    already_guessed.append(response)
   
    if response not in rw:
        life -= 1
        print (response, "isn't in the word. You have", life, "lives left. \n")
        if life == 0:
            break
    elif response in rw:
        print(response, "is in the word. You have", life, "lives left. \n")
        num = num - my_dict[response]
        print ("You have", num, "more letters to guess. \n")
        for i in (range(len(rw))):
            if (rw[i] == response):
                final[i] = response
        updatedList = "".join(final)
    print(updatedList)
    if updatedList == rw:
        print ("You have guessed the word correctly. Congrats!")
        quit()
        
                       
print ("The secret word was: ", rw)   
if life == 0:
    print ("You lost. Better luck next time!") 
else:
    print ("You exited because you are scared to play the game. LOL JK Anyways, Have a good day!")     

        


        


