

label mainscreen:

    $update_avails()
    
    if numChats + numEmails == 0:
        jump force_logout

    if day == "Mon":
      if "sheep_1014" in chatlist:
        $motd = """|                                                                        |
| Welcome to Electric Sheep, Inc!  We're excited to have you join our    |
| company.  Your first day will be spent training on the system you will |
| be using to pre-screen candidates for human-designated jobs.  Please   |
| take the time to acquaint yourself with the system and read any recent |
| news, then proceed to the chat app when you are ready to begin your    |
| training.                                                              |
"""
      else:
        $motd = """|                                                                        |
| This is the MOTD that shows after the Lola chat is completed.          |
"""        
    
    $expected = ["LOOK", "L", "HELP", "?", "MAIL.APP", "CHAT.APP"]
    $pickup = []
    $room = "Home"
    $update_roomlabel()
    $desc = "{cps=0}"
    $desc += make_header("System Home")
    $desc += motd
    $desc += """|                                                                        |
| Available Programs:                                                    |
|    <{color=#""" + skyblue + """}mail.app{/color}>: read news and emails                                    |
|    <{color=#""" + skyblue + """}chat.app{/color}>: screen candidates                                       |
|________________________________________________________________________|

{/cps}     You have ({color=#""" + errorcolor + """}[numChats]{/color}) chats waiting and ({color=#""" + errorcolor + """}[numEmails]{/color}) new emails."""
    
    $say()
    
    while True:
        $echo()
        
        if cmd.upper() not in expected:
            python:
                eastered = False
                for word in easters:
                    if cmd == word or args == word or word in args:
                        easter(word)
                        flush_input()
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
                $desc = "Starting mail.app{cps=6}... ... ... {/cps}{cps=130}Ready!{/cps}\n" \
                        "Press {b}ENTER{/b} to continue to mail."
                $say()
                nvl clear
                jump mail
            else:
                $has_args()
        
        elif cmd.upper() == "CHAT.APP":
            if len(args) == 0:
                $flush_input()
                $desc = "Starting chat.app{cps=6}... ... ... {/cps}{cps=130}Ready!{/cps}\n" \
                        "Press {b}ENTER{/b} to continue to chat."
                $say()
                nvl clear
                jump chat
            else:
                $has_args()
            
    return