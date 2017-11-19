label mail:

    if "spam42" in emaillist.keys() and emaillist["spam42"].getRead() and backdoor == None:
      call spam87 from _call_spam87_1

    $update_avails()
    $expected = ["LOOK", "L", "HELP", "?", "SHOW", "READ", "EXIT"]
    $pickup = []
    $room = "Email"
    $update_roomlabel()
    $desc = ""
    $desc += make_header("mail.app")
#     $desc += """{cps=0}|                                                                        |
# | Type <show emails> to see the list of available emails, <read> followed|
# | by the message number you wish to open, or <exit> to quit.  New emails |
# | are shown in {color=#""" + highlight2 + """}this color{/color} and previously read emails are shown in {color=#""" + highlight1 + """}this   {/color}|
# | {color=#""" + highlight1 + """}color{/color}.                                                                 |
# |                                                                        |
# | Example: {b}> read news0{/b}                                                 |
# |________________________________________________________________________|
# 
# {/cps}

    $desc += """{cps=0}|                                                                        |
| Emails received to your company account.  New emails are highlighted   |
| in {color=[highlight2]}this color{/color} and previously read emails are displayed in {color=[highlight1]}this color{/color}.  |
|                                                                        |
| Available Commands:                                                    |
|    <{color=[skyblue]}show emails{/color}>: display emails (emailtag in square brackets)         |
|    <{color=[skyblue]}read [[emailtag]{/color}>: read selected email                              | 
|    <{color=[skyblue]}exit{/color}>: return to main menu                                         |
|                                                                        |
| Example:                                                               |
|    > {color=[skyblue]}read info3{/color}                                                        |
|________________________________________________________________________|
 
{/cps}     You have ({color=#[errorcolor]}[numEmails]{/color}) unread emails."""
    
    $say()
    
    while True:
        $echo()
        
        if cmd.upper() not in expected:
            python:
                eastered = False
                for word in easters:
                    if cmd == word or args == word or word in args:
                        easter(word)
                        eastered = True
                
                if not eastered:
                    input_error()
        
        elif cmd.upper() == "LOOK" or cmd.upper() == "L":
            if len(args) == 0:
                $flush_input()
                nvl clear
                jump mail
            else:
                $has_args()
                
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
            
        elif cmd.upper() == "EXIT":
            if len(args) == 0:
                $flush_input()
                
                term "Closing mail.app{cps=6}... ... {/cps}{nw}"
                play sound "music/beep2.ogg"
                extend "{cps=130}Done.{/cps} \nPress {b}ENTER{/b} to return to main screen."
                
                nvl clear
                jump mainscreen
            else:
                $has_args()
                
        elif cmd.upper() == "SHOW":
            
            if len(args) == 1 and args[0].upper() == "EMAILS":
                $flush_input()
                if len(emaillist) > 0:
                    python:
                        s = ""
                        for id in sorted(emaillist.keys()):
                            s += "  [[{color=#" + emaillist[id].getReadColor() + "}" + id + "{/color}]: "
                            s += "'" + emaillist[id].getSubj() + "'\n"
                else:
                    $s = "{cps=150}You have no emails.{/cps}"
                    
                $desc = s
                $say()
            
            else:
                $flush_input()
                $desc = "{color=#[errorcolor]}Error{/color}: please type {b}show emails{/b} to view your email list."
                $say()
        
        elif cmd.upper() == "READ":
            
            if len(args) == 1:
                $key = args[0]
                $flush_input()
                if key in emaillist.keys():
                
                    if key.upper() == "SPAM42" and emaillist[key].getRead() != True:
                    
                      term "Downloading email [key]{cps=6}... ... ... {/cps}{nw}"
                      play sound "music/distorted.ogg"
                      extend "\n{color=[errorcolor]}{cps=130}ERROR{/cps}{cps=6}...{/cps} an unexpected override has been engaged{nw}"
                      play sound "music/resistance_start.ogg" fadeout 0.5
                      extend "{cps=2}...{/cps}{/color}{cps=1} {/cps}{nw}"
                      
                      $flush_input()
                      $emaillist[key].setRead()
                      $update_avails()
                      
                      stop music fadeout 2.0
                      play music "music/resistance.ogg" fadein 1.0 loop
                      
                      nvl clear
                      jump resistance_first
                    
                    else:
                    
                      term "Downloading email [key]{cps=6}... ... ... {/cps}{nw}"
                      play sound "music/beep.ogg"
                      extend "{cps=130}Done.{/cps} \nPress {b}ENTER{/b} to continue to mail."

                      $flush_input()
                      nvl clear
                    
                      $desc = emaillist[key].read()
                      $update_avails()
                      $say()
                      
                      if key.upper() == "INFO3":
                        $chatlist.append("max")
                      
                      # Install backdoor app
                      if key.upper() == "SPAM87":
                        $desc = "Install 'exploit.app'? <Yes/No>"
                        $say()
                        
                        while True:
                        
                          if cmd.upper() == "YES" and len(args) == 0:
                            $backdoor = True
                            $desc = "Installing 'exploit.app'{cps=6}... ...{/cps} Done.  \nPress <{b}ENTER{/b}> to return to mail.app."
                            $say()
                            
                            $del emaillist[key]
                            $flush_input()
                            nvl clear
                            jump mail
                          
                          elif cmd.upper() == "NO" and len(args) == 0:
                            $backdoor = False
                            $desc = "You chose not to install 'exploit.app'.  Press <{b}ENTER{/b}> to return to mail.app."
                            $say()
                            
                            $del emaillist[key]
                            $flush_input()
                            nvl clear
                            jump mail
                          
                          else:
                            $flush_input()
                            $desc = "{color=[errorcolor]}ERROR{/color}: Choose <Yes> or <No>."
                            $say()
                    
                      $desc = "     You have ({color=#[errorcolor]}[numEmails]{/color}) unread emails."
                      $say()
                    
                else:  
                    $flush_input()
                    $desc = "Please enter a valid email message."
                    $say()
                
            else:
                $flush_input()
                $desc = "Command 'read' takes exactly one argument."
                $say()
            
    return