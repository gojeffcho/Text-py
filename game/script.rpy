# Disable rollback
define config.rollback_enabled = False

# Styles for characters
style terminal is text:
    size 16
    font "font/Dotrice.otf"
    color "#15db15"
    
style terminalinput is text:
    size 18
    font "font/Dotrice.otf"
    color "#15db15"

# Declare characters used by this game.
define term = Character(None, kind=nvl, what_style="terminal")

# Backgrounds and Overlays
image bg black = "#000000"
image overlay = "img/overlay.png"

init -2 python:
    
    ############################
    ### Game Initializations ###    
    ############################

    # Fix spacebar entry
    config.keymap['dismiss'].remove('K_SPACE')
    
    # Remove help keymap function
    config.keymap['help'] = []
    
    # Fix skip control
    config.keymap['skip'] = []
    config.keymap['toggle_skip'] = []
    config.keymap['fast_skip'] = []
    
    # Remove mouseclick skip
    config.keymap['dismiss'].remove('mouseup_1')    
    
    global captcha
    captcha = {}
    
    global captchaInput
    captchaInput = {}


init 0 python:
    
    #########################
    ### NVL Configuration ###
    #########################
    
    # hide_val False to go with terminal input box at the bottom
    global hide_val
    hide_val = False
    
    # How many historical interactions (including echoes) are shown on the screen 
    config.nvl_list_length = 10

    # Set NVL Background Image
#     style.nvl_window.background = im.FactorScale("img/protoLarge.png", 0.5)

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

    config.window_auto_hide = [ 'scene', 'alma' ]

    
    ########################
    ### Global Variables ###
    ########################
    
    # Track username, user color
    global username
    username = "assblaster"
    
    global displayname
    displayname = "logged out"
    
    # Colors
    global usercolor
    usercolor = "ff1493"  # default user color
    
    global errorcolor
    errorcolor = "f00"
    
    global sheepcolor
    sheepcolor = "ffd700"
    
    global highlight1
    highlight1 = "faebd7"
    
    global highlight2
    highlight2 = "ff1493"
    
    global ivory
    ivory = "fffff0"
    
    global darkcyan
    darkcyan = "008b8b"
    
    global skyblue
    skyblue = "87ceeb"
    
    global crimson
    crimson = "dc143c"
    
    # Track easter eggs
    global easters
    easters = ["permeable", "fuck", "goddamn", "shit", "bitch", "cunt", "friggin", "dick", "ass", "asshole", "penis", "cock", "pussy", "damn", "hell", "fucking", "motherfucker", "motherfucking"]

    # Track available chats
    global chatlist
    global numChats
    chatlist = []
    numChats = len(chatlist)
    
    # Track available emails
    global emaillist
    global numEmails
    emaillist = {}
    numEmails = len(emaillist)
    
    # Track current time
    global day
    global hour
    global min
    global ampm
    day = "Mon"
    hour = 9
    min = 00
    ampm = "am"
    
    # Setup variable
    global daysetup
    daysetup = {}
    daysetup["Mon"] = "setup_mon"
    daysetup["Tue"] = "setup_tue"
    daysetup["Wed"] = "setup_wed"
    daysetup["Thu"] = "setup_thu"
    daysetup["Fri"] = "setup_fri"
    
    # Track previous day's performance
    global prevright
    prevright = 0
    global prevwrong
    prevwrong = 0
 
    # Track stars
    global right
    right = 0

    # Track AI sympathy
    global wrong
    wrong = 0
    
    global cmd
    cmd = ""
    
    global expected
    expected = []
    
    global args
    args = ""

    global desc
    desc = ""
    
    global append
    append = ""
    
    global roomlabel
    roomlabel = ""
    
    global room
    room = ""


    ######################
    ### GAME VARIABLES ###
    ######################
    
    # Game variables here... maybe find non-persistent way?
    renpy.image("red1", "#220000")
    renpy.image("red2", "#440000")
    renpy.image("red3", "#660000")
    renpy.image("red4", "#880000")
    renpy.image("red5", "#BB0000")
    renpy.image("red6", "#FF0000")
    
    flash = Fade(.25, 0, .75, color="#fff")
    

    ########################
    ### CUSTOM FUNCTIONS ###
    ########################
    
    
# The game starts here.
label start:
#     python:
        
    # GOTO first scene
    scene bg black

    # MAIN GAME START
#     jump logosplash

    # DEBUG START
    jump login_first

#     $day = "Tue"
#     $prevright = 1
#     $prevwrong = 5
#     jump update_score

#     $chatlist.append("courtney")
#     jump chat

#     $chatlist.append("sheep_1014")
#     call news4
#     call info3
#     call attk7
# 
#     jump mail






