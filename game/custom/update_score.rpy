label update_score:

    $right += prevright
    $wrong += prevwrong

    $room = "Review"
    $update_roomlabel()
        
    $desc = """







    
    
    
    
{cps=0}EMPLOYEE STATUS UPDATE:{/cps}
    
After external review of your screenings, it has been determined that you screened {color=[skyblue]}[prevright] out of """ + str(prevright + prevwrong) + """{/color} candidates correctly and {color=[errorcolor]}[prevwrong] out of """ + str(prevright + prevwrong) + """{/color} candidates incorrectly yesterday.  These statistics have been updated in your employee standings.  You currently have an overall {color=[usercolor]}""" + "{0:.1f}%".format((float(right)/(right + wrong)) * 100) + """{/color} accuracy rating in screenings to date.
    
Press {b}<ENTER>{/b} to continue."""
    $say()

    $prevright = 0
    $prevwrong = 0
    
    nvl clear
    jump mainscreen
            
    return