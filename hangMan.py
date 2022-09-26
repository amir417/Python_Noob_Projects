import random
import requests
import string

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
wordss = response.content.splitlines()
words = []
rw = []
EXIT = "zz"

for k in wordss:
    if len(k) > 5 and len(k) < 12:
        words.append(k)
      
randomWord = list(random.choice(words))
rw = "".join([chr(c) for c in randomWord])
alphabet_string = string.ascii_uppercase + string.ascii_lowercase 
al = list(alphabet_string)
print ("Welcome to HangMan game. You will be guessing a word with ", len(randomWord), "letters. \nYou have five lives to start with. Let's get started!")
print (rw)
my_dict = {i:rw.count(i) for i in rw}
print (my_dict)
final = list("_" * len(rw))

life = 7
num = len(randomWord)
game = True
while (game or life!=0):

    response = input("choose a letter in alphabet (type 'zz' to quit): ")
    if response == EXIT:
        break
    elif response not in al:
        print ("wrong input. Try again.")
        continue
        
    if response not in rw:
        life -= 1
        print (response, "isn't in the word. You have", life, "lives left.")
    elif response in rw:
        print(response, "is in the word. You have", life, "lives left.")
        print(response, "was repeated", my_dict[response], "times.")
        num = num - my_dict[response]
        print ("You have", num, "more letters to guess.")
        for i in (range(len(rw))):
            if (rw[i] == response):
                final[i] = response
        updatedList = "".join(final)
        print(updatedList)

                

    
print ("You exited either because you are scared to play the game or you're a loser. Anyways, Have a good day!")

        


        


