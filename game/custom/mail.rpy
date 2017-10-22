label mail:
    $expected = ["LOOK", "L", "HELP", "?", "SHOW", "EMAIL", "EXIT"]
    $pickup = []
    $room = "Email"
    $desc = """{cps=150}<PLACEHOLDER: This is the email app screen> Fancy ASCII email graphics{/cps}

Type {b}show emails{/b} to see the list of available emails, {b}email{/b} followed by the message number you wish to open, or "exit" to quit.

Example: {b}> email e_boss0{/b}"""
    
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
                $s = "{cps=150}{color=#faebd7}" + "    * " + "\n    * ".join(emaillist) + "{/color}{/cps}"
                $desc = s
                $say()
            
            else:
                $flush_input()
                $desc = "{color=#f00}Error{/color}: please type {b}show emails{/b} to view your email list."
                $say()
        
        elif cmd.upper() == "EMAIL":
            $t = args
            if len(t) == 1:
                if t[0] in emaillist:
                    
                    $desc = "Downloading email [args[0]]{cps=2}... ... ...{/cps} Done.\n" \
                            "Press {b}ENTER{/b} to open email."
                    $say()
                    
                    $flush_input()
                    nvl clear
                    jump expression t[0]
                    
                else:  
                    $flush_input()
                    $desc = "Please enter a valid email message."
                    $say()
                
            else:
                $flush_input()
                $desc = "Command 'email' takes exactly one argument."
                $say()
            
    return