label chat:
    $expected = ["look", "l", "help", "?", "chat", "exit"]
    $pickup = []
    $room = "Chat"
    $desc = """{cps=150}<PLACEHOLDER: This is the chat app screen> Fancy ASCII chat graphics{/cps}

Type {b}chat{/b} followed by the number of the person you wish to chat with to proceed, or "exit" to quit.

Example: {b}> chat 2{/b}"""
    
    $say()
    
    while True:
        $echo()
        
        if inputv not in expected:
            call wait from _call_wait_chat
        
        elif inputv == "look" or inputv == "l":
            if len(argument) == 0:
                $flush_input()
                nvl clear
                jump chat
            else:
                $has_args()
                
        elif inputv == "help" or inputv == "?":
            call help from _call_help_chat
            
        elif inputv == "exit":
            if len(argument) == 0:
                $flush_input()
                $desc = "Closing chat.app{cps=2}... ... ...{/cps} Done.\n" \
                        "Press {b}ENTER{/b} to return to main screen."
                $say()
                
                nvl clear
                jump mainscreen
            else:
                $has_args()
        
        elif inputv == "chat":
            if len(argument) == 1:
                if argument[0] in chatlist:
                    $desc = "<PLACEHOLDER> Correct Chat Choice"
                    $say()
                else:  
                    $flush_input()
                    $desc = "Please enter a valid choice for a chat partner."
                    $say()
                
            else:
                $flush_input()
                $desc = "Command 'chat' takes exactly one argument."
                $say()
            
    return