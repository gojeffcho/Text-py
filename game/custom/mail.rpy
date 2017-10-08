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
        
        if cmd not in expected:
            $input_error()
        
        elif cmd == "look" or cmd == "l":
            if len(args) == 0:
                $flush_input()
                nvl clear
                jump mail
            else:
                $has_args()
                
        elif cmd == "help" or cmd == "?":
            $help()
            
        elif cmd == "exit":
            if len(args) == 0:
                $flush_input()
                $desc = "Closing mail.app{cps=2}... ... ... Done.{/cps} \n" \
                        "Press {b}ENTER{/b} to return to main screen."
                $say()
                
                nvl clear
                jump mainscreen
            else:
                $has_args()
        
        elif cmd == "email":
            if len(args) == 1:
                if args[0] in emaillist:
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