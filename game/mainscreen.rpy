label mainscreen:
    $expected = ["help", "?", "ls", "mail.app", "chat.app"]
    $pickup = []
    $room = "Electric Sheep Co. - Home"
    $desc = """
<PLACEHOLDER: This is the main screen> Login: MOTD, graphics, etc. here
    
Available programs: <mail.app>, <chat.app>"""
    
    $say()
    
    while True:
        $echo()
        
        if inputv not in expected:
            call wait from _call_wait_mainscreen
        
        elif inputv == "ls":
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