init 0 python:
  captcha["Mon"] = """
           --    ./                 `:/+-`                  :dmmmmh+.       
     my   -MN-   yy                yMMmdMM+    h/     `d.   oMM::+yNM:      
     sM-  ymNd  .m/                MM.  +Mm   `No     -M:   .MN    sM.      
      dm`:M+:m. dm  myys+.         +MNs-dN-   .MmddhhhNM-   /MM--+yMN`      
      :Mo/d  +m.Mo dh   sN-      `yNs:+dMh`   .Mo``  .yM-   `NMNmmho`       
       omm.  .NMN` yN:  oM-      +Md    oMh   :M-     oN    -MM`            
        yh`   /y:   /ydhs-       :MMs/:/mM+   -d`     -s    .MM`            
                                  -odddds:                   /+          
  """
  
  captchaInput["Mon"] = "Wo8HP"
  
  captcha["Tue"] = """ 
     .oooooo..o   .oooo.       .                oooooooo           
    d8P'    `Y8 .dP\"\"Y88b    .o8               dP\"\"\"\"\"\"\"           
    Y88bo.            ]8P' .o888oo    .oooo.o d88888b.    .ooooo.  
     `\"Y8888o.      <88b.    888     d88(  \"8     `Y88b  d88' `88b 
         `\"Y88b      `88b.   888     `\"Y88b.        ]88  888   888 
    oo     .d8P o.   .88P    888 .   o.  )88b o.   .88P  888   888 
    8\"\"88888P'  `8bd88P'     \"888\"   8\"\"888P' `8bd88P'   `Y8bod8P'   
    """
  
  captchaInput["Tue"] = "S3ts5o"
  
  captcha["Wed"] = """ 
              `7MMF\'           ,6*\"*VA.       `7MMF'   `7MF'
                MM            dN     V8         `MA     ,V  
  `7MMpMMMb.    MM            `MN.  ,g9  ,pW\"Wq. VM:   ,V   
    MM    MM    MM             ,MMMMq.  6W'   `Wb MM.  M'   
    MM    MM    MM      ,     6P   `YMb 8M     M8 `MM A'    
    MM    MM    MM     ,M     8b    `M9 YA.   ,A9  :MM;     
  .JMML  JMML..JMMmmmmMMM     `MmmmmM9   `Ybmd9'    VF   
  """
  
  captchaInput["Wed"] = "nL8oV"
  
  captcha["Thu"] = """ 
  """
  
  captchaInput["Thu"] = "a"
  
  captcha["Fri"] = """ 
  """
  
  captchaInput["Fri"] = "a"

# CAPTCHA
label captcha:
    $expected = []
    $pickup = []
    $room = "CAPTCHA"
    $update_roomlabel()
    $desc = """{cps=0}{font=font/AnonymousPro.ttf}{color=#ffd700}"""
    $desc += captcha[day]
    $desc += """{/color}{/font}{/cps}
Please enter the CAPTCHA above to prove that you are human.  Do not include any spaces.  Type {b}captcha{/b} for more details."""
    
    $say()
    
    while True:
        $echo()
        
        if cmd == captchaInput[day]:
            $flush_input()
            $desc = "Your network authentication has been approved.  Press {b}<ENTER>{/b} to proceed."        
            $say()
            $flush_input()
            
            nvl clear
            jump expression daysetup[day]
            
        elif cmd == "":
            $flush_input()
            $desc = "Please enter the CAPTCHA text."
            $say()
            
        elif cmd.upper() == "CAPTCHA":
            $flush_input()
            $desc = "Enter the characters above exactly as you see them, in case-sensitive format, using only letters and numbers.  No punctuation, special characters, or spaces should be included."
            $say()
        
        else:
            $flush_input()
            $desc = "Your response has been flagged for Human Resources review.  Press {b}<ENTER>{/b} to proceed."
            $say()

            $flush_input()
            nvl clear
            if day == "Mon":
              jump expression daysetup["Mon"]
            else:
              jump update_score
            
    return