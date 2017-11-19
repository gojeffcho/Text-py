label spam87:
  python:
  
    key = "spam87"
    
    subj = "Are You Alive?"
    
    tx = "deaddropbw73nk@fwdnet.stablebase.kz"
    
    rx = username[:5] + "713@electricsheep.ca"
  
    text = """If you're willing to help us, install this app 
on your computer. It contains a sophisticated
encryption-breaking tool that will extract the
data we need from your network and relay it
back to us. It can cover its own tracks, but
only use it once per day, or you could be 
compromised.

We have complete faith in your abilities, and 
remember: innocent lives depend on you.  This
email will wipe itself from your computer and 
the server after it has been read."""
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email

