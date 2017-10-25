label mainscreen:
    $update_avails()
    
    if numChats + numEmails == 0:
        jump force_logout
    
    $expected = ["LOOK", "L", "HELP", "?", "MAIL.APP", "CHAT.APP"]
    $pickup = []
    $room = "Home"
    $desc = """{cps=150}<PLACEHOLDER: This is the main screen> Login: MOTD, graphics, etc. here{/cps}

You have ({color=#f00}[numChats]{/color}) chat partners and ({color=#f00}[numEmails]{/color}) new emails.
Available programs: <{color=#87ceeb}mail.app{/color}>, <{color=#87ceeb}chat.app{/color}>"""
    
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
                jump mainscreen
            else:
                $has_args()
                
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
        
        elif cmd.upper() == "MAIL.APP":
            if len(args) == 0:
                $flush_input()
                $desc = "Starting mail.app{cps=2}... ... ...{/cps} {cps=130}Ready!{/cps}\n" \
                        "Press {b}ENTER{/b} to continue to mail."
                $say()
                nvl clear
                jump mail
            else:
                $has_args()
        
        elif cmd.upper() == "CHAT.APP":
            if len(args) == 0:
                $flush_input()
                $desc = "Starting chat.app{cps=2}... ... ...{/cps} {cps=130}Ready!{/cps}\n" \
                        "Press {b}ENTER{/b} to continue to chat."
                $say()
                nvl clear
                jump chat
            else:
                $has_args()
            
    return