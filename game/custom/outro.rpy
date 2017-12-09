label outro:

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

    # Play title splash sound
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
  $desc = "                         {size=25}TEAM JEFF{/size}\n\n"

  $desc += """                      {b}Producer{/b}:
                              Jeff Cho \n\n"""

  $desc += """                      {b}Writers{/b}:
                              Shelby Carleton
                              Jeff Cho
                              Maddy Hebert
                              Aidan Herron \n\n"""

  $desc += """                      {b}Designers{/b}:
                              Jeff Cho
                              Kieran Downs \n\n"""
  
  $desc += """                      {b}Composer{/b}:
                              Kieran Downs \n\n"""

  $desc += """                      {b}Developers{/b}:
                              Jeff Cho
                              Brandon Wieliczko \n\n"""
        
  $desc += """                      {b}Sound Technicians{/b}:
                              Jeff Cho
                              Kieran Downs {nw}"""
  
  $freeze = desc                              
  $say()                             
  
    # Let them end the game, I guess.
  python:
    config.keymap['dismiss'].append('K_RETURN')
    config.keymap['dismiss'].append('K_KP_ENTER')
    config.keymap['dismiss'].append('K_SELECT')
  
  $desc = ""
  $say()
  
  stop music fadeout 5.0

  # Exeunt omnes 
  python:
    colors = [
      "15db15",
      "12c512",
      "10af10",
      "0e990e",
      "0c830c",
      "0a6d0a",
      "085708",
      "064106",
      "042b04",
      "021502",
      "000000",
      "000000"
    ]
    for color in colors:

      # Clear output
      nvl_clear()
      desc = "{cps=0}{color=" + color + "}"
  
      desc += freeze
  
      # String closer and output
      desc += "{/color}{/cps}{nw}"
      say()
  
  pause 4.5
  
  $sys.exit()