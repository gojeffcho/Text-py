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
  """
  
  captchaInput["Tue"] = "a"
  
  captcha["Wed"] = """ 
  """
  
  captchaInput["Wed"] = "a"
  
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
            
        elif cmd.upper() == "captcha":
            $flush_input()
            $desc = "Enter the characters above exactly as you see them, in case-sensitive format, using only letters and numbers.  No punctuation, special characters, or spaces should be included."
            $say()
        
        else:
            $flush_input()
            $desc = "Your response has been flagged for Human Resources review.  Press {b}<ENTER>{/b} to proceed."
            $say()

            $flush_input()
            nvl clear
            jump expression daysetup[day]
            
    return