label teststart:

    $chatlist.append("l0_14")
    $chatlist.remove("l0_14")
    $chatlist.append("l0_14")

label mainscreen:
    $update_avails()
    $expected = ["look", "l", "help", "?", "mail.app", "chat.app"]
    $pickup = []
    $room = "Home"
    $desc = """{cps=150}<PLACEHOLDER: This is the main screen> Login: MOTD, graphics, etc. here{/cps}

You have ({color=#f00}[numChats]{/color}) chat partners and ({color=#f00}[numEmails]{/color}) new emails.
Available programs: <{color=#87ceeb}mail.app{/color}>, <{color=#87ceeb}chat.app{/color}>"""
    
    $say()
    
    while True:
        $echo()
        
        if cmd not in expected:
            python:
                eastered = False
                for word in easters:
                    if cmd == word or args == word or word in args:
                        easter(word)
                        eastered = True
                
                if not eastered:
                    input_error()
        
        elif cmd == "look" or cmd == "l":
            if len(args) == 0:
                $flush_input()
                nvl clear
                jump mainscreen
            else:
                $has_args()
                
        elif cmd == "help" or cmd == "?":
            $help()
        
        elif cmd == "mail.app":
            if len(args) == 0:
                $flush_input()
                $desc = "Starting mail.app{cps=2}... ... ...{/cps} {cps=130}Ready!{/cps}\n" \
                        "Press {b}ENTER{/b} to continue to mail."
                $say()
                nvl clear
                jump mail
            else:
                $has_args()
        
        elif cmd == "chat.app":
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