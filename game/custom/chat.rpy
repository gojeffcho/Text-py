label chat:
    $update_avails()
    $expected = ["LOOK", "L", "HELP", "?", "CHAT", "SHOW", "EXIT"]
    $pickup = []
    $room = "Chat"
    $desc = """{cps=150}<PLACEHOLDER: This is the chat app screen> Fancy ASCII chat graphics{/cps}

You can see the users you can chat with by typing {b}show chats{/b}.  Type {b}chat{/b} followed by the number of the person you wish to chat with to proceed, or "exit" to quit.

Example: {b}> chat c_demo0{/b}

You have ({color=#f00}[numChats]{/color}) chat partners to screen."""
    
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
                jump chat
            else:
                $has_args()
                
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
            
        elif cmd.upper() == "EXIT":
            if len(args) == 0:
                $flush_input()
                $desc = "Closing chat.app{cps=2}... ... ...{/cps} Done.\n" \
                        "Press {b}ENTER{/b} to return to main screen."
                $say()
                
                nvl clear
                jump mainscreen
            else:
                $has_args()

        elif cmd.upper() == "SHOW":
            
            if len(args) == 1 and args[0] == "chats":
                $flush_input()
                $s = "{cps=150}{color=#faebd7}" + "    * " + "\n    * ".join(chatlist) + "{/color}{/cps}"
                $desc = s
                $say()
            
            else:
                $flush_input()
                $desc = "{color=#f00}Error{/color}: please type {b}show chats{/b} to view your chat list."
                $say()
                
        elif cmd.upper() == "CHAT":
            $t = args
            if len(t) == 1:
                if t[0] in chatlist:
                    $desc = "Initiating chat with [t[0]]{cps=2}... ... ...{/cps} Done.\n" \
                            "Press {b}ENTER{/b} to enter chat."
                    $say()
                    
                    $flush_input()
                    $chatlist.remove(t[0])   # can't re-engage this target
                    nvl clear
                    jump expression t[0]
                    
                else:  
                    $flush_input()
                    $desc = "Please enter a valid choice for a chat partner."
                    $say()
                
            else:
                $flush_input()
                $desc = "Command 'chat' takes exactly one argument."
                $say()
            
    return