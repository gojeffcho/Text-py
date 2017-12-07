label attk8:
  python:
  
    key = "attk8"
    
    subj = "Raid on KyR.OS Fails"
    
    tx = "danger@electricsheep.ca"
    
    rx = "allhands@intern.electricsheep.ca"
  
    text = """A raid on a suspected Resistance base failed to 
lead to the capture or shutdown of KyR.OS, but 
has brought to light startling new information 
about the nature of KyR.OS itself.

Forensic analysts discovered from decrypted 
hard drives recovered from the raid that KyR.OS 
is not a singular AI, but at least six distinct 
AIs. It remains to be seen whether these AIs are 
copies of the same source AI or separate 
individuals.

With this new knowledge, investigators warn that 
we should be wary of any suspicious AI - KyR.OS 
could be anyone."""
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email

# force update