# LOGIN: first day login prompt
label login_first:
    $expected = ["help", "?", "new"]
    $pickup = []
    $room = "Electric Sheep Co. - New User"
    $desc = """ 
     ______          _____       _____       
________  /____________  /__________(_)______
_  _ \_  /_  _ \  ___/  __/_  ___/_  /_  ___/
/  __/  / /  __/ /__ / /_ _  /   _  / / /__  
\___//_/  \___/\___/ \__/ /_/    /_/  \___/  
     _                       _            
 ___| |__   ___  ___ _ __   (_)_ __   ___ 
/ __| '_ \ / _ \/ _ \ '_ \  | | '_ \ / __|
\__ \ | | |  __/  __/ |_) | | | | | | (__ 
|___/_| |_|\___|\___| .__/  |_|_| |_|\___|
                    |_|                            

{cps=15}Welcome, new user!  

Please type "new" to set up your account.  You can type "help" or "?" at any time to see the list of commands available to you.{/cps}"""
    
    $say()
    
    while True:
        e "> [inputv] [argument]{nw}"
        
        if inputv not in expected:
            call wait from _call_wait_login
        
        elif inputv == "help" or inputv == "?":
            call help from _call_help_login
            
        elif inputv == "new":
            $flush_input()
            jump login_new
            
    return
    
# LOGIN: login new user
label login_new:
    $flush_input()
    $expected = ["help", "?", "create"]
    $pickup = []
    $room = "Electric Sheep Co. - Create New User"
    $desc = """{cps=15}We're{/cps} {cps=30}thrilled{/cps} {cps=15}to have you join our company!  Let's create your account.  Please type "create" followed by your desired username to create your login.
    
Example: > create shelby {/cps}"""

    $say()
    
    while True:
        e "> [inputv] [argument]{nw}"
        
        if inputv not in expected:
            call wait from _call_wait_login_2
        
        elif inputv == "help" or inputv == "?":
            call help from _call_help_login_2
        
        elif inputv == "create":

            if argument != "":
                $set_username(argument)
                $desc = "{cps=15}Your username has been set to: '" + username + "'.  {b}Please remember this username{/b} as you will use it to log in each day along with your bio-authentication.\n\nPress <ENTER> to continue when you are ready.{/cps}"
                $say()
                $flush_input()

                nvl clear
                
                jump login

            else:
                $desc = "{color=#f00}Please enter a valid username.{/color}"
                $say()
    
    return
    
# LOGIN: regular login prompt
label login:
    $expected = ["help", "?", "login"]
    $pickup = []
    $room = "Electric Sheep Co. - Login"
    $desc = """
     ______          _____       _____       
________  /____________  /__________(_)______
_  _ \_  /_  _ \  ___/  __/_  ___/_  /_  ___/
/  __/  / /  __/ /__ / /_ _  /   _  / / /__  
\___//_/  \___/\___/ \__/ /_/    /_/  \___/  
     _                       _            
 ___| |__   ___  ___ _ __   (_)_ __   ___ 
/ __| '_ \ / _ \/ _ \ '_ \  | | '_ \ / __|
\__ \ | | |  __/  __/ |_) | | | | | | (__ 
|___/_| |_|\___|\___| .__/  |_|_| |_|\___|
                    |_|                            

Please type "login <username>" to log in, or "help" for a list of available commands."""
    
    $say()
    
    while True:
        e "> [inputv] [argument]{nw}"
        
        if inputv not in expected:
            call wait from _call_wait_login_1
        
        elif inputv == "help" or inputv == "?":
            call help from _call_help_login_1
        
        elif inputv == "login":
            if argument == username:
                $desc = "Press <ENTER> for bioauthentication..."
                $say()
                
                $desc = "Login successful!  Welcome, " + username + ".  (Press ENTER to continue)"
                $say()
                $flush_input()
                jump mainscreen
            else:
                $desc = "Incorrect login!"
                $say()
            
    return
