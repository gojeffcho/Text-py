label misc22:
  python:
  
    key = "misc22"
    
    subj = "Tech Pro Tips"
    
    tx = "tech_tips@electricsheep.ca"
    
    rx = "+info_all@intern.electricsheep.ca"
  
    text = """Have any tech problems you need solved? Send us
a message and you could be in our next issue!

Rachael writes: Hey guys, I'm having a problem 
with my phone. I told it to call me a cab and 
now it won't stop calling me 'Cab'. Any 
suggestions?

Our reply: Use Uber. Dumbass.

That's all for this issue. See you next week!
"""
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email