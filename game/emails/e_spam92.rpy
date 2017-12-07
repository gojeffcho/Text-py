label spam92:
  python:
  
    key = "spam92"
    
    subj = "SPAM"
    
    tx = "deaddropbw73nk@fwdnet.stablebase.kz"
    
    rx = username[:5] + "713@electricsheep.ca"
  
    text = ""

    if prevExploited == True:
      text += "YOU DID GOOD.\n\nINTEL HIGHLY VALUABLE.\n\nDELIVER AGAIN TODAY."
    else:
      text += "YOU DID NOT DELIVER.\n\nNEED ACTIONABLE INTEL.\n\nDELIVER TODAY.\n\n"
    
    text += ""
    
    text += "EMAIL SELF-DESTRUCTS."
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email

