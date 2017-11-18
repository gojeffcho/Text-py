label spam42:
  python:
  
    key = "spam42"
    
    subj = "HELLO HONEY PLS UR URGENT REPLY!!!"
    
    tx = "honeypotwzqyt@proxnet.co.tz"
    
    rx = username[:5] + "713@electricsheep.ca"
  
    text = """Hi, my love! I want to wake up with you every 
morning, share my day, my thoughts and emotions 
with you only.
Miss you so much! I am looking forward to your 
letter."""
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email

# force update