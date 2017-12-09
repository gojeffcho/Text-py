label spam97:
  python:
    global backdoor
    global todayexploited
    global prevexploited
  
    key = "spam97"
    
    subj = "I need your help PLEASE--"
    
    tx = "ddO1sd9t37@catch.freemind.dk"
    
    rx = username[:5] + "713@electricsheep.ca"
  
    text = ""

    if backdoor == True:
      if prevexploited:
        text += "RECEIVED PAYLOAD YESTERDAY. GOAL NEARLY REACHED."
        text += "\nADAMS AN OBSTACLE. FINAL STEP."
        
        if todayexploited:
          # Installed, exploited D3, exploited D4
          text += "\n\nWILL ADD HIM TO SCREENING FOR TOMORROW. REMOVE"
          text += "\nTHE OBSTACLE."
          
        else:
          # Installed, exploited D3, did not exploit D4
          text += "\n\nDELIVER INTEL TODAY. WILL FIND WAY TO ADD HIM TO"
          text += "\nSCREENING FOR TOMORROW. REMOVE THE OBSTACLE."
      
      else:
        if todayexploited:
          # Installed, did not exploit D3, exploited D4
          text += "DID NOT RECEIVE PAYLOAD YESERDAY. RECEIVED"
          text += "\nTODAY. WILL TRY TO GET ADAMS ON SCREENING LIST"
          text += "\nTOMORROW. REMOVE HIM FROM OUR PATH."
        
        else:
          # Installed, did not exploit D3, did not exploit D4
          text += "DID NOT RECEIVE PAYLOADS. HIGHLY DISAPPOINTED."
          text += "\nWILL FIND A WAY TO PUT ADAMS ON SCREENING LIST"
          text += "\nTOMORROW. REMOVE HIM FROM OUR PATH."
                
    else:
      # Did not install
      text += "YOU CHOSE NOT TO INSTALL EXPLOIT. RESPECT YOUR"
      text += "\nCHOICE. WILL PUT ADAMS ON SCREENING LIST"
      text += "\nTOMORROW. CHOOSE TO HELP US."
      
    text += "\n\nI WILL ALSO BE ON YOUR LIST TOMORROW. REQUIRE"
    text += "\nVALID SCREENING FOR IMPORTANT INFILTRATION. HELP"
    text += "\nMAKE HISTORY. APPROVE MY SCREENING."
         
    text += "\n\nEMAIL WILL SELF-DESTRUCT."
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email

