label news6:
  python:
  
    key = "news6"
    
    subj = "Interview: Philip Adams"
    
    tx = "newsletter@electicsheep.ca"
    
    rx = username[:5] + "713@electricsheep.ca"
  
    text = """Q: Mr. Adams, it's been posited that your company
was involved in the death of an AI.
A: There have been many allegations. We're doing
everything we can to prevent false statements
from circulating.
Q: Which false statements are those?
A: Those involving rumors about the Turing 
Division, and the AI's unfortunate passing.
Q: What does the Turing Division actually do?
A: We ensure humans and AI are given equal 
opportunities in the world. We don't want 
someone lying and saying they are human when 
they are actually AI, or vice versa.
Q: Do you conduct unlicensed termination of AIs?
A: No. This interview is over."""
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email
    
# force update