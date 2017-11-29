label info5:
  python:
  
    key = "info5"
    
    subj = "Human Rights for AIs"
    
    tx = "ai_news@electricsheep.ca"
    
    rx = "+info_all@intern.electricsheep.ca"
  
    text = """Giving AIs human rights sounds like an oxymoron,
doesn't it?

New legislation put forward could make this a
reality. Bill K-68, if passed, would amend the
Canadian Charter of Rights and Freedoms to
consider certain AIs as Canadian citizens,
granting them the same civil and political 
rights as their human counterparts - and that's 
a good thing.

The government will have to very delicately 
define what constitutes an AI in this bill. It
won't be easy, but it's a necessary step for us
as a society. Bill K-68 will set a precedent for
similar legislation in other countries. Let's 
not mess this up."""
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email