label demo_end:

  $roomlabel = ""

  $desc = "\n\n\n\n\n\n\n\n\n\n\n                    This concludes the game demo.\n"
  $desc += "                    Your score was: [right] out of " + str(right + wrong) + "!"
  $desc +="\n\n                    Press <{b}ENTER{/b}> to continue."
  $say()
  
label full_ending:

  python:
  
    hide_val = True
    screenlines = 34  
    
    # Initial Splash and Hold
    size = 15
    linesFromTop = 10
    frames = 10

    colors = [
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "2f4f4f", # SlateGrey
      "696969", # DimGrey
#       "708090", # SlateGrey
      "808080", # Grey
      "a9a9a9", # DarkGrey
      "d3d3d3", # LightGrey
      "f8f8ff", # GhostWhite
      "faf0e6", # Linen
#       "ffdead", # NavajoWhite
      "fffff0", # Ivory
      "ffffff", # White
    ]
    
  
    splash = [                                                                              
      "\"8a                                             88                            ",
      "  \"8a           ,d                              \"\"                            ",
      "    \"8a         88                                                            ",
      "      \"8a     MM88MMM  88       88  8b,dPPYba,  88  8b,dPPYba,    ,adPPYb,d8  ",
      "      a8\"       88     88       88  88P'   \"Y8  88  88P'   `\"8a  a8\"    `Y88  ",
      "    a8\"         88     88       88  88          88  88       88  8b       88  ",
      "  a8\"           88,    \"8a,   ,a88  88          88  88       88  \"8a,   ,d88  ",
      "a8\"             \"Y888   `\"YbbdP'Y8  88          88  88       88   `\"YbbdP\"Y8  ",
      "                                                                  aa,    ,88  ",
      "                                                                   \"Y8bbdP\"   ",
      "",
      "",
      "                           a TEAM JEFF production"
    ]

    # Play title splash music
    renpy.music.play("music/title.ogg", channel="sound")

    splashfreeze = ""

    # Run as many times as there are characters
    for color in colors:
      
      # Clear output
      nvl_clear()
      desc = "{cps=0}{size=" + str(size) + "}{color=" + color + "}"
      
      # Header spacer
      for each in range(linesFromTop):
        desc += "\n"
      
      # Iterate for each line in the splash
      for line in splash:
      
        # Add the thing
        desc += line + "\n"
      
      # String closer and output
      desc += "{/color}{/size}{/cps}"
      splashfreeze = desc
      desc += "{nw}"
      say()

    
    # Make it stick
    desc = splashfreeze + "{cps=1}   {/cps}{nw}"
    nvl_clear()
    say()

    colors.reverse()
  
    # Fade it out now
    for color in colors:
  
      # Clear output
      nvl_clear()
      desc = "{cps=0}{size=" + str(size) + "}{color=" + color + "}"
    
      # Header spacer
      for each in range(linesFromTop):
        desc += "\n"
    
      # Iterate for each line in the splash
      for line in splash:
    
        # Add the thing
        desc += line + "\n"
    
      # String closer and output
      desc += "{/color}{/size}{/cps}{nw}"
      say()
  
  # After ending title splash
  nvl clear

label credits:

  # CREDITS
  $desc = "                        {size=40}TEAM JEFF{/size}{nw}"
  $say()

  $desc = """                      {b}Producer{/b}:
                              Jeff Cho {nw}"""
  $say()

  $desc = """                      {b}Writers{/b}:
                              Shelby Carleton
                              Maddy Hebert
                              Aidan Herron {nw}"""
  $say()

  $desc = """                      {b}Designers{/b}:
                              Jeff Cho
                              Kieran Downs {nw}"""
  $say()
  
  $desc = """                      {b}Composer{/b}:
                              Kieran Downs {nw}"""
  $say()                             

  $desc = """                      {b}Developers{/b}:
                              Jeff Cho
                              Brandon Wieliczko {nw}"""
  $say()         
        
  $desc = """                      {b}Sound Technicians{/b}:
                              Jeff Cho
                              Kieran Downs {nw}"""
  $say()                             
      
  $desc = "                       {color=[ivory]} Thanks for playing!{/color}"
  $say()
  
  $sys.exit()