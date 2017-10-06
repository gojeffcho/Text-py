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
        
        elif inputv == "help" or inputv == "?":
            call help from _call_help_mainscreen
            
        elif inputv == "ls":
            $flush_input()
            $desc = "<PLACEHOLDER: directory> Show some stuff."
            $say()
        
        elif inputv == "mail.app":
            $flush_input()
            $desc = "<PLACEHOLDER> Starting mail.exe... \n" \
                    "(Nothing actually here, press ENTER to continue)"
            $say()
            jump mainscreen
        
        elif inputv == "chat.app":
            $flush_input()
            $desc = "<PLACEHOLDER> Starting chat.exe...\n" \
                    "(Nothing actually here, press ENTER to continue)"
            $say()
            jump mainscreen
            
    return