label news9:
  python:
  
    key = "news9"
    
    subj = "Electric Sheep Hailed as Heroes"
    
    tx = "newsletter@electicsheep.ca"
    
    rx = username[:5] + "713@electricsheep.ca"
  
    text = """A social media post from a popular online 
blogger detailing Electric Sheep's 'great work' 
went viral last night. It reads:

'I just wanted to say thank you to the Turing 
Division... I know you've been getting bad press
lately, but my son had one of those Turing tests 
the other day and screened as human - and he 
just got a job offer this afternoon! Thank you,
employers who use screening services, and thank
you to Electric Sheep for making this possible!' """
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email
    
# force update