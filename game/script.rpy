# Disable rollback
define config.rollback_enabled = False

# Styles for characters
style terminal is text:
    size 16
    font "font/Dotrice.otf"
    color "#15db15"
    line_spacing 2
    
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
    
    # Remove MENU keymaps
    config.keymap['game_menu'] = []
    
    # Fix skip control
    config.keymap['skip'] = []
    config.keymap['toggle_skip'] = []
    config.keymap['fast_skip'] = []
    
    # Remove mouseclick skip
    config.keymap['dismiss'].remove('mouseup_1')
    
    # Remove a bunch of other stuff
    config.keymap['full_inspector'] = []
    config.keymap['hide_windows'] = []
    config.keymap['inspector'] = []
    config.keymap['developer'] = []
    config.keymap['progress_screen'] = []
    config.keymap['rollforward'] = []
    config.keymap['focus_left'] = []
    config.keymap['focus_right'] = []
    config.keymap['focus_up'] = []
    config.keymap['focus_down'] = []
    
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
    
    # Track Lola's name for display in chat
    global lolaName
    lolaName = "10-14"
    
    # Colors
    global usercolor
    usercolor = "ff1493"  # default user color
    
    global errorcolor
    errorcolor = "f00"
    
    global sheepcolor
    sheepcolor = "ffd700"
    
    global highlight
    highlight = "FFA500"
    
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
    
    global darkgreen
    darkgreen = "006400"
    
    global springgreen
    springgreen = "00fa9a"
    
    # Random Colour
    global colourList
    colourList = [crimson, skyblue, darkcyan, ivory, highlight2, sheepcolor, darkgreen, springgreen]
    
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
    global mailnum
    emaillist = {}
    numEmails = len(emaillist)
    mailnum = 0
    
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
    global wrong
    wrong = 0
    
    # Track AI sympathy
    global sympathy
    sympathy = 0
    global exploited
    exploited = 0
    global todayexploited
    todayexploited = False
    global prevexploited
    prevexploited = False
    
    # Resistance Tracking
    global firstResponse
    firstResponse = None
    global backdoor
    backdoor = None
    
    # Finale Variables
    global lolaFinal
    lolaFinal = False
    global adamsFinal
    adamsFinal = False
    
    global lolaHuman
    lolaHuman = None
    global kevinHuman
    kevinHuman = None
    global adamsHuman
    adamsHuman = None

    
    # Room and Command Globals
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

    # Hacking Tracking
    global hacked
    hacked = False



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

    # DEBUG START        
    $day = "Wed"
    play music "music/bg0.mp3" fadein 2.5 loop
    $backdoor = False
#     jump captcha
#     jump force_logout
    jump expression daysetup[day]
    
#     $chatlist.append("p_adams")
#     jump mainscreen
#     jump exploit

    # ENDING DEBUG
#     $lolaHuman = -1
#     $adamsHuman = 1
#     $kevinHuman = 1
#     jump outro
#     jump ending
#     jump credits


    # MAIN GAME START
    # call hackgame

    jump logosplash

#     $chatlist.append("sheep_1014")
#     call news4
#     call info3
#     call attk7
# 
#     jump mail






