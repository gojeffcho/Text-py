# LOGIN: first day login prompt
label login_first:
    $expected = ["ls", "help", "?", "new"]
    $pickup = []
    $room = "Electric Sheep Co. - New User"
    $desc = """{cps=0}{font=AnonymousPro-Regular.ttf}{color=#ffd700}
              ___                  __                         
             /\_ \                /\ \__         __            
           __\//\ \      __    ___\ \ ,_\  _ __ /\_\    ___    
         /'__`\\\ \ \   /'__`\ /'___\ \ \/ /\`'__\/\ \  /'___\  
        /\  __/ \_\ \_/\  __//\ \__/\ \ \_\ \ \/ \ \ \/\ \__/  
        \ \____\/\____\ \____\ \____\\\ \__\\\ \_\  \ \_\ \____\ 
         \/____/\/____/\/____/\/____/ \/__/ \/_/   \/_/\/____/ 
               __                                                       
              /\ \                                 __                   
          ____\ \ \___      __     __   _____     /\_\    ___     ___   
         /',__\\\ \  _ `\  /'__`\ /'__`\/\ '__`\   \/\ \ /' _ `\  /'___\ 
        /\__, `\\\ \ \ \ \/\  __//\  __/\ \ \L\ \   \ \ \/\ \/\ \/\ \__/ 
        \/\____/ \ \_\ \_\ \____\ \____\\\ \ ,__/    \ \_\ \_\ \_\ \____\ 
         \/___/   \/_/\/_/\/____/\/____/ \ \ \/      \/_/\/_/\/_/\/____/ 
                                          \ \_\                         
                                           \/_/                           
{/color}{/font}{/cps}
Welcome, new user!  

Please type {b}new{/b} to set up your account.  You can type {b}help{/b} or {b}?{/b} at any time to see the list of commands available to you."""
    
    $say()
    
    while True:
        $echo()
        
        if inputv not in expected:
            call wait from _call_wait_login
            
        elif inputv == "ls":
            if len(argument) == 0:
                $flush_input()
                nvl clear
                jump login_first
            else:
                $has_args()
        
        elif inputv == "help" or inputv == "?":
            call help from _call_help_login
            
        elif inputv == "new":
            if len(argument) == 0:
                $flush_input()
                nvl clear
                jump login_new
            else:
                $has_args()
    return
    
# LOGIN: login new user
label login_new:
    $flush_input()
    $expected = ["ls", "help", "?", "create"]
    $pickup = []
    $room = "Electric Sheep Co. - Create New User"
    $desc = """{cps=0}{font=AnonymousPro-Regular.ttf}{color=#ffd700}
              ___                  __                         
             /\_ \                /\ \__         __            
           __\//\ \      __    ___\ \ ,_\  _ __ /\_\    ___    
         /'__`\\\ \ \   /'__`\ /'___\ \ \/ /\`'__\/\ \  /'___\  
        /\  __/ \_\ \_/\  __//\ \__/\ \ \_\ \ \/ \ \ \/\ \__/  
        \ \____\/\____\ \____\ \____\\\ \__\\\ \_\  \ \_\ \____\ 
         \/____/\/____/\/____/\/____/ \/__/ \/_/   \/_/\/____/ 
               __                                                       
              /\ \                                 __                   
          ____\ \ \___      __     __   _____     /\_\    ___     ___   
         /',__\\\ \  _ `\  /'__`\ /'__`\/\ '__`\   \/\ \ /' _ `\  /'___\ 
        /\__, `\\\ \ \ \ \/\  __//\  __/\ \ \L\ \   \ \ \/\ \/\ \/\ \__/ 
        \/\____/ \ \_\ \_\ \____\ \____\\\ \ ,__/    \ \_\ \_\ \_\ \____\ 
         \/___/   \/_/\/_/\/____/\/____/ \ \ \/      \/_/\/_/\/_/\/____/ 
                                          \ \_\                         
                                           \/_/                                            
{/color}{/font}{/cps}
We're {cps=50}thrilled to have you join our company!{/cps}  Let's create your account.  Please type {b}create{/b} followed by your desired username (at least five characters long) to create your login.
    
Example: {b}> create shelby{/b}"""

    $say()
    
    while True:
        $echo()
        
        if inputv not in expected:
            call wait from _call_wait_login_2
            
        elif inputv == "ls":
            if len(argument) == 0:
                $flush_input()
                nvl clear
                jump login_new
            else:
                $has_args()
                
        elif inputv == "help" or inputv == "?":
            call help from _call_help_login_2
        
        elif inputv == "create":

            if len(argument) == 1:
                if len(argument[0]) < 5:
                    $flush_input()
                    $desc = "Your username must be at least five characters long."
                    $say()
                
                else: 
                    $set_username(argument[0])
                    $flush_input()
                    nvl clear
                    
                    $desc = "Your username has been set to {u}" + username + "{/u}.  {b}Please remember this username{/b} as you will use it to log in each day along with your bio-authentication.\n\nPress {b}<ENTER>{/b} to continue when you are ready."
                    $say()

                    nvl clear                
                    jump login

            else:
                $flush_input()
                $desc = "{color=#f00}Error{/color}: Please enter a valid username."
                $say()

        else:
            call wait from _call_wait_login_33
    
    return
    
# LOGIN: regular login prompt
label login:
    $expected = ["ls", "help", "?", "login"]
    $pickup = []
    $room = "Electric Sheep Co. - Login"
    $desc = """{cps=0}{font=AnonymousPro-Regular.ttf}{color=#ffd700}
              ___                  __                         
             /\_ \                /\ \__         __            
           __\//\ \      __    ___\ \ ,_\  _ __ /\_\    ___    
         /'__`\\\ \ \   /'__`\ /'___\ \ \/ /\`'__\/\ \  /'___\  
        /\  __/ \_\ \_/\  __//\ \__/\ \ \_\ \ \/ \ \ \/\ \__/  
        \ \____\/\____\ \____\ \____\\\ \__\\\ \_\  \ \_\ \____\ 
         \/____/\/____/\/____/\/____/ \/__/ \/_/   \/_/\/____/ 
               __                                                       
              /\ \                                 __                   
          ____\ \ \___      __     __   _____     /\_\    ___     ___   
         /',__\\\ \  _ `\  /'__`\ /'__`\/\ '__`\   \/\ \ /' _ `\  /'___\ 
        /\__, `\\\ \ \ \ \/\  __//\  __/\ \ \L\ \   \ \ \/\ \/\ \/\ \__/ 
        \/\____/ \ \_\ \_\ \____\ \____\\\ \ ,__/    \ \_\ \_\ \_\ \____\ 
         \/___/   \/_/\/_/\/____/\/____/ \ \ \/      \/_/\/_/\/_/\/____/ 
                                          \ \_\                         
                                           \/_/                           
{/color}{/font}{/cps}
Please type {b}login <username>{/b} to log in, or {b}help{/b} for a list of available commands."""
    
    $say()
    
    while True:
        $echo()
        
        if inputv not in expected:
            call wait from _call_wait_login_1
        
        elif inputv == "ls":
            if len(argument) == 0:
                $flush_input()
                nvl clear
                jump login
            else:
                $has_args()
                
        elif inputv == "help" or inputv == "?":
            call help from _call_help_login_1
        
        elif inputv == "login":
            if len(argument) == 1:
                if argument[0] == username:
                    $desc = "Press and hold {b}<ENTER>{/b} for one second for bioauthentication..."
                    $say()
                    
                    $desc = "{cps=3}...{/cps} {nw}"
                    $say()
            
                    $desc = "{color=#87ceeb}Login successful{/color}!  Welcome, " + username + ".  Press {b}<ENTER>{/b} to proceed."
                    $say()
                    $flush_input()
                    nvl clear
                    jump mainscreen
                                    
                else:
                    $s = " ".join(argument)
                    $flush_input()
                    $desc = "{color=#f00}Error{/color}: Incorrect login '" + s + "'!  Please try again."
                    $say()
            elif len(argument) == 0:
                $flush_input()
                $desc = "{color=#f00}Error{/color}: You must supply a username after {b}login{/b}."
                $say()
            else:
                $flush_input()
                $desc = "{color=#f00}Error{/color}: Please type {b}login <username>{/b} to log in.  Your username is only one word."
                $say()
            
    return
