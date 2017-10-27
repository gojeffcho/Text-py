label info3:
  python:
  
    key = "info3"
    
    subj = "Interview with Natural Language AI Advocate"
    
    tx = "ai_news@electrosheep.ca"
    
    rx = username[:5] + "713@electrosheep.ca"
  
    text = """Interviewer: What do you want?
    
AI Advocate: Natural Language Processing!

Interviewer:  When do you want it?

AI Advocate: When do we want what?"""
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email