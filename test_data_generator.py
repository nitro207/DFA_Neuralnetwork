"""
Created on Tue May 14 12:41:07 2024

@author: nitro
"""

import numpy as np


file = open("test_DFA_data.csv", "a")

wordCount = int(input("how many words would you like to generate: "))

#creates correct words
for i in range(wordCount):
    curentWord = ""
    randnum = np.random.randint(456)
    
    for num in range(randnum):
        decision = np.random.randint(2)
        
        if decision == 1:
            curentWord += "a"
        else:
            continue
    curentWord += "b"
    
    for num in range(randnum):
        decision = np.random.randint(2)
        
        if decision == 1:
            curentWord += "a"
        else:
            continue
    
    curentWord += ",1\n"
    
    file.write(curentWord)

#creates incorrect words
for i in range(wordCount):
    curentWord = ""
    randnum = np.random.randint(456)
    
    for num in range(randnum):
        decision = np.random.randint(3)
        
        if decision == 0:
            continue
        elif decision == 1:
            curentWord += "a"
        elif decision == 2:
            curentWord += "b"
    
    
    if curentWord.count('b') == 1:
        curentWord += 'b'
            
    curentWord += ",0\n"
    
    file.write(curentWord)




file.close()