label info4:
  python:
  
    key = "info4"
    
    subj = "Ones and Zeroes"
    
    tx = "ai_news@electricsheep.ca"
    
    rx = "+info_all@intern.electricsheep.ca"
  
    text = """A new survey suggests that it may be 
discriminatory to call humans 'ones' and AIs 
'zeroes'.

45% of respondents said that calling humans 
'ones' was empowering, and 60% said that 
calling AIs 'zeroes' marginalizes them. The 
terms were coined in 2017 by Electric Sheep 
Inc. during their public image reparation 
campaign.

In the interest of equality, we have included
a binary translation of our article for our 
AI readers:

01010100 01101000 01101001 01110011 00100000 
01101001 01110011 00100000 01101110 01101111 
01110100 00100000 01100001 01101110 00100000 
01100101 01100001 01110011 01110100 01100101 
01110010 00100000 01100101 01100111 01100111 
00101110"""
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email