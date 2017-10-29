label info3:
  python:
  
    key = "info3"
    
    subj = "fwd: Natural Language AI Advocate..."
    
    tx = "ai_news@electricsheep.ca"
    
    rx = "+info_all@electricsheep.ca"
  
    text = """Interviewer: What do you want?
    
AI Advocate: Natural Language Processing!

Interviewer:  When do you want it?

AI Advocate: When do we want what?"""
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email
    
# force update