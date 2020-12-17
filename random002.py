# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:37:38 2020

@author: mrbacco
"""

###################### imports START ######################

import csv
import random
import time
import os, sys
from datetime import datetime
import tweepy
import logging
import lorem

###################### imports END ######################

###################### logger setup START ######################

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

###################### logger setup END ######################

###################### tw_api func START ######################

auth = tweepy.OAuthHandler("xxx", 
                           "xxx")
auth.set_access_token("xxx-xxx",
                          "xxx")

# API object to use for everything
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    logger.info("logged in, thanks")
except:
    logger.info("errors during authentication, try again")

###################### tw_api func END ######################

with open('adverbs.txt', "r") as f1:
    spamreader = csv.reader(f1, delimiter=',')
    adv=[i for row in spamreader for i in row]

with open('adjectives.txt', "r") as f2:
    spamreader = csv.reader(f2, delimiter=',')
    adj=[i for row in spamreader for i in row]
    
with open('nouns.txt', "r") as f3:
    spamreader = csv.reader(f3, delimiter=',')
    nouns=[i for row in spamreader for i in row]
    
with open('verbs.txt', "r") as f4:
    spamreader = csv.reader(f4, delimiter=',')
    verbs=[i for row in spamreader for i in row]
    
punct = [" ", " yours ", ", ", " they ", " ", " you ", " ", " he ", ": ", 
         " she ", " it ", "; ", " which ", " him ", " ... ", " ", " her ", ]

marks = ["!", ".", ".", "?", ".", "!!!", ".", ".", "."]

pron = [ "yours", "it", "who", "whom", "what"]

print(len(nouns), " length nouns\n")
print(len(adv), "length adv\n")
print(len(adj), "length adj\n")
print(len(verbs), "length verbs\n")

count = 0                               # counting iterations in the loop

while count >= 0:

    num1 = random.randrange(0,8778)     # nouns
    num2 = random.randrange(0,90962)    # nouns
    num3 = random.randrange(0,90962)    # nouns
    num33 = random.randrange(0,90962)   # nouns
    num22 = random.randrange(0,90962)   # nouns
    num23 = random.randrange(0,90962)   # nouns
    
    num4 = random.randrange(0,30801)    # verbs
    num5 = random.randrange(0,30801)    # verbs
    num6 = random.randrange(0,30801)    # verbs 
    
    num7 = random.randrange(0,5301)     # adj
    num8 = random.randrange(0,5301)     # adj
    num9 = random.randrange(0,5301)     # adj
    
    num10 = random.randrange(0,6276)    # adv
    num11 = random.randrange(0,6276)    # adv
    num12 = random.randrange(0,6276)    # adv
    
    num44 = random.randrange(0,17)      # punct
    num45 = random.randrange(0,17)      # punct
    num46 = random.randrange(0,17)      # punct
    num47 = random.randrange(0,17)      # punct
    num48 = random.randrange(0,17)      # punct
    
    num54 = random.randrange(0,9)       # mark
    num55 = random.randrange(0,9)       # mark
    num56 = random.randrange(0,9)       # mark
    num57 = random.randrange(0,9)       # mark
    num58 = random.randrange(0,9)       # mark
    
    num64 = random.randrange(0,7)       # pron
    num65 = random.randrange(0,7)       # pron
    num66 = random.randrange(0,7)       # pron
    num67 = random.randrange(0,7)       # pron
    num68 = random.randrange(0,7)       # pron

    s = lorem.sentence()                # random latin sentence
    p = lorem.paragraph()               # random latin paragraph
    t = lorem.text()                    # random latin text

    sentence = (nouns[num1] + " " + verbs[num4] + punct[num46] + nouns[num2] + " " 
                + nouns[num22] + punct[num44] + "\n" + nouns[num3] +  punct[num48] 
                + verbs[num5] + punct[num46] + adv[num10] + "\n" + verbs[num6]
                + " " + adj[num7] + " " + adv[num11] + marks[num54] + "\n" 
                + "\n" + s + marks[num55])

    now = str(datetime.now().replace(microsecond=0))

    print("########## iteration" , count, "########## ", "\n")
    print(sentence, "\n", "date and time: ", now, "\n" )

    count +=1                           # incrementing the count of total iterations

    # api.update_status(sentence)         # updating twitter status
    time.sleep(2)

    output = open("output.txt", "a")    # file to write the output on
    count_str = str(count)
    item_to_write = "##### iteration number " + count_str + " \n" + sentence + "\n" + "\n"
    output.write("{}\n".format(item_to_write))

output.close("output.txt")

