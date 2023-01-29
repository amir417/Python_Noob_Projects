import requests
import urllib.parse
import json

from collections import Counter
from collections import OrderedDict




sentences = [
    "I felt a deep sense of sadness when I heard the news.",
    "The sight of the sunset filled me with a sense of awe and wonder.",
    "The thought of losing my best friend filled me with dread.",
    "The sound of her laughter brought a smile to my face and warmth to my heart.",
    "The love I feel for my family is overwhelming and unconditional.",
    "The betrayal cut me deeply and left me feeling empty and alone.",
    "His words of encouragement lifted me up when I was feeling down.",
    "The beauty of the forest left me breathless and in awe.",
    "My triumph was short-lived as disappointment soon set in.",
    "The memories of our time together bring a tear to my eye and a smile to my face.",
    "The feeling of accomplishment after finishing a difficult task is indescribable.",
    "The sight of the city skyline at night fills me with a sense of wonder and excitement.",
    "The thought of never seeing her again broke my heart into a million pieces.",
    "The taste of my mother's cooking brings back fond memories of my childhood.",
    "The fear of failure grips my heart every time I try something new.",
    "The warmth of the sun on my face on a summer day brings a sense of happiness and contentment.",
    "The loss of my pet left me feeling lost and alone.",
    "The excitement of starting a new chapter in my life is overwhelming.",
    "The touch of my loved one's hand brings a sense of safety and comfort.",
    "The beauty of a snow-covered landscape fills me with a sense of serenity and tranquility.",
    "The frustration of dealing with constant setbacks is overwhelming.",
    "The hope for a better future is a beacon of light that guides me through difficult times.",
    "The joy of being reunited with an old friend is overwhelming.",
    "The anger and betrayal I feel towards someone who wronged me is hard to contain.",
    "The pain of a broken heart is unbearable.",
    "The excitement of traveling to a new place fills me with anticipation and wonder.",
    "The feeling of nostalgia when thinking about the past is bittersweet.",
    "The satisfaction of a job well done is unparalleled.",
    "The longing for the company of someone who is far away is palpable.",
    "The sense of belonging in a community brings warmth to my heart.",
     "I feel like I'm on top of the world!",
    "I'm so angry I could scream!",
    "I'm so excited for the weekend!",
    "I'm feeling so down today.",
    "I'm so in love with you.",
    "I'm so proud of you.",
    "I can't stop laughing!",
    "I'm so scared right now.",
    "I'm so grateful for all I have.",
    "I'm so confused about what to do.",
    "I'm so excited for what's to come.",
    "I'm so sad to see you go.",
    "I'm so nervous for my presentation.",
    "I'm so happy to see you again.",
    "I'm so content with where I am in life.",
    "I'm so stressed out right now.",
    "I'm so in awe of your talents.",
    "I'm so mesmerized by your beauty.",
    "I'm so touched by your kind words.",
    "I'm so in shock from the news.",
    "I'm so in love with my new job.",
    "I'm so proud of my accomplishments.",
    "I'm so excited for my vacation.",
    "I'm so sad to leave my friends.",
    "I'm so nervous for my exam.",
    "I'm so happy to be home.",
    "I'm so content with my life.",
    "I'm so stressed out with work.",
    "I'm so in awe of nature.",
    "I'm so mesmerized by the stars.",
    "I'm so touched by your generosity.",
    "I'm so in shock by the accident.",
    "I'm so in love with the city.",
    "I'm so proud of my team.",
    "I'm so excited for the concert.",
    "I'm so sad to break up.",
    "I'm so nervous for my interview.",
    "I'm so happy to be engaged.",
    "I'm so content with my relationship.",
    "I'm so stressed out about money.",
    "I'm so in awe of art.",
    "I'm so mesmerized by music.",
    "I'm so touched by your support.",
    "I'm so in shock by the news.",
    "I'm so in love with my new hobby."
]

# encoded_sentences = []
# for sentence in sentences:
#     encoded_sentences.append(urllib.parse.quote(sentence))

# print(encoded_sentences)

emotions = []
allEmotions = []
singleEmotion = []

for sentence in sentences:
    urlSentence = urllib.parse.quote(sentence)
    response = requests.get(f'https://x.roya.vc/api/?class=emotion&key=0c77fe89a829541f25c4e35b9014f4ae&query={urlSentence} ')
    # print(response.json())
    emotions.append(response.json())
    

for i in range (len(emotions)):
    allEmotions.append(list(emotions[i].keys()))    

for i in range(len(allEmotions)):
    for j in range(len(allEmotions[i])):
        singleEmotion.append(allEmotions[i][j])

# for i in range(len(emotions)):
#     print (emotions[i].keys())
    # print (emotions[i].values())
print (len(emotions))
# print(allEmotions)
# print(singleEmotion)

count_dict = dict(Counter(singleEmotion))
count_dict = OrderedDict(sorted(count_dict.items(), key=lambda x: x[1], reverse=True))

print (count_dict)