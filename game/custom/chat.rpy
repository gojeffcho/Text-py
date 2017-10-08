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
        
        if cmd not in expected:
            $input_error()
        
        elif cmd == "look" or cmd == "l":
            if len(args) == 0:
                $flush_input()
                nvl clear
                jump chat
            else:
                $has_args()
                
        elif cmd == "help" or cmd == "?":
            $help()
            
        elif cmd == "exit":
            if len(args) == 0:
                $flush_input()
                $desc = "Closing chat.app{cps=2}... ... ...{/cps} Done.\n" \
                        "Press {b}ENTER{/b} to return to main screen."
                $say()
                
                nvl clear
                jump mainscreen
            else:
                $has_args()
        
        elif cmd == "chat":
            if len(args) == 1:
                if args[0] in chatlist:
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