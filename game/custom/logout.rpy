label force_logout:

    $expected = ["HELP", "?", "LOOK", "L", "LOGOUT"]
    $pickup = []
    $room = "Logout"
    $update_roomlabel()
    $desc = "{cps=0}"
    $desc += make_header("System Home")
    $desc += """|                                                                        |
| Your screenings for the day are complete.  Please log out of your      |
| session with the <{color=[ivory]}logout{/color}> command.                                     |
|________________________________________________________________________|

{/cps}     You have ({color=#[errorcolor]}[numChats]{/color}) chats waiting and ({color=#[errorcolor]}[numEmails]{/color}) new emails."""
    
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
                jump force_logout
            else:
                $has_args()
                
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
        
        elif cmd.upper() == "LOGOUT":
            if len(args) == 0:
                $flush_input()
                
                if day == "Fri":
                  jump ending
                  
                else:
                
                  $desc = """Your screenings for today have been registered with the system and will be corroborated with external interviews with the candidates.  You will be rewarded for each screening you classified correctly, and your employee status will be updated upon your next login.  Goodbye."""
                  $say()
                  $flush_input()
                
                  $displayname = "logged out"
                  nvl clear
                  jump next_day
                  
            else:
                $has_args()
            
    return
    
label next_day:

    $new_day()
    stop music fadeout 3.0
    $renpy.pause(5.5)
  
    jump login
    
                