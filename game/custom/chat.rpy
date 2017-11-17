label chat:
    $update_avails()
    $expected = ["LOOK", "L", "HELP", "?", "CHAT", "SHOW", "EXIT"]
    $pickup = []
    $room = "Chat"
    $update_roomlabel()
    $desc = ""
    $desc += make_header("chat.app")
    $desc += """{cps=0}|                                                                        |
| You can see the users you can chat with by typing <show chats>.  Type  |
| <chat> followed by the identifier tag of the candidate with whom you   |
| wish to chat, or <exit> to return to the main screen.                  |
|                                                                        |
| Example: {b}> chat demo0{/b}                                                 |
|________________________________________________________________________|

{/cps}     You have ({color=#[errorcolor]}[numChats]{/color}) chat partners to screen."""
    
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
                
                term "Closing chat.app{cps=6}... ... {/cps}{nw}"
                play sound "music/beep2.ogg"
                extend "{cps=130}Done.{/cps} \nPress {b}ENTER{/b} to return to main screen."
                
                nvl clear
                jump mainscreen
            else:
                $has_args()

        elif cmd.upper() == "SHOW":
            
            if len(args) == 1 and args[0] == "chats":
                $flush_input()
                python:
                  s = "{cps=150}"
                  for chat in chatlist:
                    s += "   [[{color=#[highlight1]}" + chat + "{/color}]: "
                    if chat == "sheep_1014":
                      s += "Assistant bot on standby.\n"
                    elif chat == "p_adams":
                      s += "Supervisor wishes to chat with you."
                    else:
                      s += "Candidate ready for screening\n"
                  s += "{/cps}"
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
                    term "Initiating chat with [t[0]]{cps=6}... ... ... {/cps}{nw}"
                    play sound "music/beep.ogg"
                    extend "{cps=130}Done.{/cps} \nPress {b}ENTER{/b} to begin."
                                    
                    $flush_input()
                    $chatlist.remove(t[0])   # can't re-engage this target
                    nvl clear
                    jump expression t[0]
                    
                else:  
                    $flush_input()
                    $desc = "{color=#[errorcolor]}ERROR{/color}: Please enter a valid choice for a chat partner."
                    $say()
                
            else:
                $flush_input()
                $desc = "{color=#[errorcolor]}ERROR{/color}: Command 'chat' must be followed by a single valid candidate tag."
                $say()
            
    return