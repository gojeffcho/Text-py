label news5:
  python:
  
    key = "news5"
    
    subj = "Suspicious AI Casualty"
    
    tx = "newsletter@electicsheep.ca"
    
    rx = username[:5] + "713@electricsheep.ca"
  
    text = """New evidence has come forward in the case of
Max Rosen, found dead Monday night.

Rosen was found in their apartment bathtub,
apparently electrocuted via toaster. The death
was ruled suspicious after forensic technicians
discovered that the sockets were faulty and
unlikely to carry a lethal current.

Analysis of Rosen's computer revealed a chat
with Electric Sheep's Turing Division hours
before the approximate time of death. Turing
Division head Philip Adams declined to comment."""
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email
    
# force update