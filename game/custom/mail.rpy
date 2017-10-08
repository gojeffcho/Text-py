label mail:
    $expected = ["look", "l", "help", "?", "email", "exit"]
    $pickup = []
    $room = "Email"
    $desc = """{cps=150}<PLACEHOLDER: This is the email app screen> Fancy ASCII email graphics{/cps}

Type {b}email{/b} followed by the message number you wish to open, or "exit" to quit.

Example: {b}> email 5{/b}"""
    
    $say()
    
    while True:
        $echo()
        
        if inputv not in expected:
            call wait from _call_wait_mail
        
        elif inputv == "look" or inputv == "l":
            if len(argument) == 0:
                $flush_input()
                nvl clear
                jump mail
            else:
                $has_args()
                
        elif inputv == "help" or inputv == "?":
            call help from _call_help_mail
            
        elif inputv == "exit":
            if len(argument) == 0:
                $flush_input()
                $desc = "Closing mail.app{cps=2}... ... ... Done.{/cps} \n" \
                        "Press {b}ENTER{/b} to return to main screen."
                $say()
                
                nvl clear
                jump mainscreen
            else:
                $has_args()
        
        elif inputv == "email":
            if len(argument) == 1:
                if argument[0] in emaillist:
                    $desc = "<PLACEHOLDER> Correct Email Choice"
                    $say()
                else:  
                    $flush_input()
                    $desc = "Please enter a valid email message."
                    $say()
                
            else:
                $flush_input()
                $desc = "Command 'email' takes exactly one argument."
                $say()
            
    return