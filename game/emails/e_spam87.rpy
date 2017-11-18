label spam87:
  python:
  
    key = "spam87"
    
    subj = "Are You Alive?"
    
    tx = "deaddropbw73nk@fwdnet.stablebase.kz"
    
    rx = username[:5] + "713@electricsheep.ca"
  
    text = """If you're willing to help us, please install this 
app on your computer. From there, you should be
able to gain access to the list you worked 
through today. First, you'll have to break the
firewall, which our sources indicate is rather 
archaic, with a simple alphanumeric key you'll 
have to identify. Process of elimination should 
be sufficient to identify it, but be aware if you 
guess wrong too many times the firewall is liable 
to lock you out, even with the app installed. 

We have complete faith in your abilities, and 
remember: innocent lives depend on you.  This
email will wipe itself from your computer and the
server after it's been read."""
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email

