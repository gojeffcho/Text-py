label news5:
  python:
  
    key = "news5"
    
    subj = "Suspicious AI Casualty"
    
    tx = "newsletter@electicsheep.ca"
    
    rx = username[:5] + "713@electricsheep.ca"
  
    text = """New evidence has come forward in the case of
Dakota Rosen, an AI found inactive last night.

Rosen was found collapsed in the street last
evening with no evidence of trauma to their 
frame. Emergency IT specialists' attempts to
jump-start their battery proved unsucessful.

Police analysis of Rosen's black box revealed a
transcript from an earlier conversation with
Electric Sheep Inc. followed by a remote 
deactivation command from an unidentified 
source. Electric Sheep declined to comment."""
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email
    
# force update