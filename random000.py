# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:37:38 2020

@author: mrbacco
"""

import lorem
import time
import random
from datetime import datetime

nouns = ["puppy", "car", "rabbit", "girl", "monkey", "mother", "father", "baby",
         "child", "teenager", "grandmother", "student", "teacher", "minister", 
         "businessperson", "salesclerk", "woman", "man", "lion", "tiger", "bear", 
         "dog", "cat", "alligator", "cricket", "bird", "wolf"]

verbs = ["runs", "hits", "jumps", "drives", "barfs", "enjoys", "lives","is", 
         "has", "does", "says", "makes", "knows", "thinks", "takes", "sees", 
         "comes", "wants", "looks", "uses", "finds", "gives", "tells", "yells"]

adj = ["adorable", "clueless", "dirty", "odd", "stupid", "useless", "funny", 
       "", "attractive", "bald","beautiful", "chubby", "clean", "dazzling", 
       "drab", "elegant", "fancy", "fit", "flabby", "glamorous", "gorgeous",
       "handsome", "long", "magnificent", "muscular", "plain", "plump", "quaint", 
       "scruffy", "shapely", "short", "skinny", "stocky", "ugly", "unkempt", 
       "unsightly"]

adv = ["crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.", 
       "happily.", "boldly", "bravely", "brightly", "cheerfully", "deftly",
       "devotedly", "eagerly", "elegantly", "faithfully", "fortunately", 
       "gleefully", "gracefully", "honestly", "innocently", "justly", "kindly",
       "obediently", "perfectly", "politely", "powerfully", "safely", 
       "victoriously", "warmly", "vivaciously"]

n = 0
while n >= 0:
    s = lorem.sentence() 
    p = lorem.paragraph()
    t = lorem.text()
    now = str(datetime.now().replace(microsecond=0))
    
    appdx = ("%s%s%s%s%s%s%s%s%s%s%s" %(random.choice(nouns), " " ,random.choice(nouns), 
                                        " " ,random.choice(verbs), " ", 
                                        random.choice(adv), " ", s, " ... " , random.choice(adj)))
    n += 1
    
    print("########## iteration number" , n, "########## ")
    print(appdx, "\n", "\n" )

    time.sleep(2)


