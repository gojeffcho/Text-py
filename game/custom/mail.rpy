label mail:
    $update_avails()
    $expected = ["LOOK", "L", "HELP", "?", "SHOW", "READ", "EXIT"]
    $pickup = []
    $room = "Email"
    $desc = """{cps=150}<PLACEHOLDER: This is the email app screen> Fancy ASCII email graphics{/cps}

Type {b}show emails{/b} to see the list of available emails, {b}read{/b} followed by the message number you wish to open, or "exit" to quit.  New emails are shown in {color=#""" + highlight2 + """}this color{/color} and previously read emails are shown in {color=#""" + highlight1 + """}this color{/color}.

Example: {b}> read news0{/b}

You have ({color=#f00}[numEmails]{/color}) unread emails."""
    
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
                $desc = "Closing mail.app{cps=2}... ... ... Done.{/cps} \n" \
                        "Press {b}ENTER{/b} to return to main screen."
                $say()
                
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
                        for id in emaillist.keys():
                            s += "  [[{color=#" + emaillist[id].getReadColor() + "}" + id + "{/color}]: "
                            s += "'" + emaillist[id].getSubj() + "'\n"
                else:
                    $s = "{cps=150}You have no emails.{/cps}."
                    
                $desc = s
                $say()
            
            else:
                $flush_input()
                $desc = "{color=#f00}Error{/color}: please type {b}show emails{/b} to view your email list."
                $say()
        
        elif cmd.upper() == "READ":
            
            if len(args) == 1:
                $key = args[0]
                $flush_input()
                if key in emaillist.keys():
                    
                    $desc = "Downloading email [key]{cps=2}... ... ...{/cps} Done.\n" \
                            "Press {b}ENTER{/b} to open email."
                    $say()
                    
                    $flush_input()
                    nvl clear
                    
                    $desc = emaillist[key].read()
                    $say()
                    
                    $help()
                    
                else:  
                    $flush_input()
                    $desc = "Please enter a valid email message."
                    $say()
                
            else:
                $flush_input()
                $desc = "Command 'read' takes exactly one argument."
                $say()
            
    return