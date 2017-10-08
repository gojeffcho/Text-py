# Disable rollback
define config.rollback_enabled = False

# Styles for characters
style my_text is text:
    size 16
    font "ufonts.com_terminal.ttf"
#     font "AnonymousPro-Regular.ttf"
    color "#00cc00"

# Declare characters used by this game.
define term = Character(None, kind=nvl, what_style="my_text")

image bg black = "#000000"

# NVL configuration
            
init -2 python:

    # Fix spacebar entry
    config.keymap['dismiss'].remove('K_SPACE')
    
    # Remove mouseclick skip
    config.keymap['dismiss'].remove('mouseup_1')
    
    global hide_val
    hide_val = False
        
    # Track username
    global username
    username = ""
    
    # Track easter eggs
    global easters
    easters = ["fuck", "goddamn"]
    
    # Track available chats
    global chatlist
    chatlist = []

    # Track available emails
    global emaillist
    emaillist = []
    
    # Track current time
    global hour
    global min
    global ampm
    hour = 8
    min = 00
    ampm = "am"
        
    # Track stars
    global stars
    stars = 0
    
    # Track AI sympathy
    global sympathy
    sympathy = 0
    
    global inputv
    inputv = ""
    
    # TODO: REMOVE or alter items mechanic
    global items
    items = []
    
    # TODO: REMOVE or alter think mechanic
    global think_message
    think_message = ""
    
    # TODO: REMOVE or alter pickup mechanic
    global pickup
    pickup = [""]
    
    global expected
    expected = []
    
    global argument
    argument = ""
    
    global desc
    desc = ""
    
    global append
    append = ""
    
    global room
    room = ""
    
    
init 0 python:
    
    # TODO: NVL length - could this be how many outputs are shown on the terminal display? 
    config.nvl_list_length = 7

    # Game variables here... maybe find non-persistent way?
    renpy.image("red1", "#220000")
    renpy.image("red2", "#440000")
    renpy.image("red3", "#660000")
    renpy.image("red4", "#880000")
    renpy.image("red5", "#BB0000")
    renpy.image("red6", "#FF0000")
    
    flash = Fade(.25, 0, .75, color="#fff")
    
    
    menu = nvl_menu

    # The color of a menu choice when it isn't hovered.
    style.nvl_menu_choice.idle_color = "#ccccccff"

    # The color of a menu choice when it is hovered.
    style.nvl_menu_choice.hover_color = "#ffffffff"

    # The color of the background of a menu choice, when it isn't
    # hovered.
    style.nvl_menu_choice_button.idle_background = "#00000000"

    # The color of the background of a menu choice, when it is
    # hovered.
    style.nvl_menu_choice_button.hover_background = "#ff000044"

    # How far from the left menu choices should be indented.
    style.nvl_menu_choice_button.left_margin = 20


    #style.nvl_window.background = "nvl_window.png"
    style.nvl_window.xpadding = 55
    style.nvl_window.ypadding = 55

    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve
    
    config.say_attribute_transition = dissolve
    
    config.default_text_cps = 15

    config.window_auto_hide = [ 'scene', 'alma' ]
    
    # TODO: add all strings to argument, instead of only the second one
    def update_input(value=""): 
        global argument
        global inputv

        # Flush command and args before setting
        inputv = ""
        argument = ""

        words = str.split(str(value))
        if len(words) == 0 or len(words) == 1:
            inputv = value.strip()
        if len(words) >= 2:
            inputv = words[0].strip()
            argument = words[1:]
        
    def echo():
        cmd = inputv 
        args = " ".join(argument)
        if args != "":
            cmd = cmd + " " + args
        term("{cps=0}> " + cmd + "{/cps}{nw}")
        
    def flush_input():
        global inputv
        global argument
        inputv = ""
        argument = ""
        
    def has_args():
        s = inputv
        flush_input()
        term("{cps=125}Command '" + s + "' takes no additional arguments.")
        
    def set_username(name):
        global username
        username = name
        
    # TODO: we can probably use this for our different applications
    def change_background_color(fantasyval):
        global append
        append = fantasy_message()
        if fantasyval < 100 and fantasyval >= 80:
            renpy.scene()
            renpy.show("red1")
        
        if fantasyval < 80 and fantasyval >= 60:
            renpy.scene()
            renpy.show("red2")
            
        if fantasyval < 60 and fantasyval >= 40:
            renpy.scene()
            renpy.show("red3")
            
        if fantasyval < 40 and fantasyval >= 20:
            renpy.scene()
            renpy.show("red4")
        
        if fantasyval < 20 and fantasyval >= 0:
            renpy.scene()
            renpy.show("red5")
        
        if fantasyval < 0:
            renpy.scene()
            renpy.show("red6")
    
    def say():
        global desc
        global append
        
        term(desc + "\n" + append)
        desc = ""
        append = ""

    
# The game starts here.
label start:
    python:
    
        # Track username
        global username
        username = ""
        
        # Track easter eggs
        global easters
        easters = ["fuck", "goddamn", "shit"]
    
        # Track available chats
        global chatlist
        chatlist = []
        
        # Track available emails
        global emaillist
        emaillist = []
        
        # Track current time
        global hour
        global min
        global ampm
        hour = 9
        min = 00
        ampm = "am"
     
        # Track stars
        global stars
        stars = 0
    
        # Track AI sympathy
        global sympathy
        sympathy = 0
        
        global inputv
        inputv = ""
        
        global items
        items = []
        
        global think_message
        think_message = ""
        
        global pickup
        pickup = [""]
        
        global expected
        expected = []
        
        global argument
        argument = ""
        
    # GOTO first scene
    scene bg black
    jump login_first