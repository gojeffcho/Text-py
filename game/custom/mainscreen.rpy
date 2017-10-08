label mainscreen:
    $expected = ["look", "l", "help", "?", "mail.app", "chat.app"]
    $pickup = []
    $room = "Electric Sheep Co. - Home"
    $desc = """{cps=150}<PLACEHOLDER: This is the main screen> Login: MOTD, graphics, etc. here{/cps}
    
Available programs: <{color=#87ceeb}mail.app{/color}>, <{color=#87ceeb}chat.app{/color}>"""
    
    $say()
    
    while True:
        $echo()
        
        if inputv not in expected:
            call wait from _call_wait_mainscreen
        
        elif inputv == "look" or inputv == "l":
            if len(argument) == 0:
                $flush_input()
                nvl clear
                jump mainscreen
            else:
                $has_args()
                
        elif inputv == "help" or inputv == "?":
            call help from _call_help_mainscreen
        
        elif inputv == "mail.app":
            if len(argument) == 0:
                $flush_input()
                $desc = "Starting mail.app{cps=2}... ... ...{/cps} {cps=130}Ready!{/cps}\n" \
                        "Press {b}ENTER{/b} to continue to mail."
                $say()
                nvl clear
                jump mail
            else:
                $has_args()
        
        elif inputv == "chat.app":
            if len(argument) == 0:
                $flush_input()
                $desc = "Starting chat.app{cps=2}... ... ...{/cps} {cps=130}Ready!{/cps}\n" \
                        "Press {b}ENTER{/b} to continue to chat."
                $say()
                nvl clear
                jump chat
            else:
                $has_args()
            
    return