init -1 python:

  ## PRECONDITION: each chat must have at least three questions
  ## NOTE: we're going to need to grab getQuestions() and concatenate it
  ##       to $expected in order to validate user inputs... Christ.
  ##
  ## NOTE: a question has key 'entry', corresponding to the user input
  ##       a follow-up question to that question has key 'entry<X>'
  ##       e.g. 'entry' = 'JOKE', follow-ups are 'entry2, entry3'
  class Chat:

    ## Members:
    # id: unique identifier for the chat; used in $chatlist
    # isHuman: False if AI, True if human
    # color: hexcode value to display target text
    # questions: DICT { 'entry' : 'Question text' } - for displaying
    # asked:     LIST containing 'entry's of questions already asked
    # answers:   DICT { 'entry' : 'Answer test' }   - target response
    # followupQ: DICT { 'entry' : 'Followup text' } - for displaying
    # followupA: DICT { 'entry' : 'Followup text' } - target response
    # qList: LIST containing three options for the player:
    #           first element is a follow-up, if relevant
    #           other elements are available questions
    #           if qList empty, force the report
    # currentQ:  used for state storage (e.g. knowing when to wipe followup)
    
    # Note: 'entry' is the inputcode that the user enters to reference a question
    #  since all answers and follow-ups derive from the question that is asked,
    #  we can use this as the associated key for everything having to do with it

    ## 
    ##  Constructor - no validation of inputs
    ##                YOLO
    def __init__(self, id, isHuman, color, questions, answers, followupQ, followupA):
      self.__id = id
      self.__isHuman = isHuman
      self.__color = color
      self.__questions = questions
      self.__asked = []
      self.__answers = answers
      self.__followupQ = followupQ
      self.__followupA = followupA
      self.__qList = []
      self.__currentQ = ""
    
    
    ##
    ##  ACCESSORS
    ##
    
    # getID() -> String
    def getId(self):
      return self.__id
    
    # isHuman() -> Bool
    def isHuman(self):
      return self.__isHuman
    
    # getQuestions() -> list of Strings
    # list comprised of: follow-up, if any, plus available questions
    # return list max size 3 (for screen density)
    def getQuestions(self):     
      return self.__qList
    
    # getAnswer(question) -> String
    def getAnswer(self, question):
      return self.__answers[question]
  
    # getFollowupQ(question) -> String
    # Text of follow-up question, used for printing to terminal
    def getFollowupQ(self, question):
      return self.__followupQ[question]
    
    # getFollowupA(question) -> String
    def getFollowupA(self, question):
      return self.__followupA[question]
    
    # isQuestion(key) -> Bool
    def isQuestion(self, key):
      return key in self.__questions
    
    # isFollowup(key) -> Bool
    def isFollowup(self, key):
      return key in self.__followupQ
      
    
    ##
    ##  MUTATORS
    ##

    # addAsked(question): adds question to asked list
    def __addAsked(self, question):
      self.__asked.append(question)


    ## 
    ##  METHODS
    ##

    # start()
    # Sets chat to engaged state, initializes qList
    def start(self):
      self.__qList = self.__questions.keys()[:3] # get first three questions
    
    # reportTarget(Bool)
    # ends the chat
    def reportTarget(self, report):
      # TODO: IMPLEMENT
      return
      
    # questionFormat()
    def questionsOutput(self):
      outputString = ""
      for q in self.__qList:
        lineString = "  * <{color=" + highlight1 + "}" + q + "{/color}>: " + self.__questions[q] + "\n"
        outputString += lineString
      
      return outputString
      
    # userFormat(outputText) -> String (formatted for terminal output)
    def userFormat(self, text):
      outputString = "{color=#" + usercolor + "}{b}" + username + "{/b}{/color}: " + text + "{nw}"
      
      return outputString
      
    # typingMessage() -> String (formatted for terminal output)
    # Interlude between user question being asked and target reply
    def typingMessage(self):
      outputString = "{color=#" + self.__color + "}{b}" + self.__id + "{/b}{/color} is typing{cps=2}...{/cps}{nw}"
      
      return outputString
      
    # targetFormat(outputText) -> String (formatted for terminal output)
    def targetFormat(self, text):
      
      # Prepend target username in user color
      outputString = "{color=#" + self.__color + "}{b}" + self.__id + "{/b}{/color}: " + text + "{nw}"
            
      return outputString
    
    # asked(question) -> Bool
    def asked(self, question):
      return question in self.__asked
      
    # queueQuestion(): adds one new question to qList, if available
    def __queueQuestion(self):
      questions = self.__questions.keys()
      for question in questions:
        if not self.asked(question):
          self.__qList.append(question)
          return 
      return
          
    # ask(question)
    def ask(self, question):
    
      global desc
    
      # Get question
      q = question.upper()
    
      # Validate question
      if q not in self.__qList:
        # If invalid, error out and return
        # TODO: IMPLEMENT
        desc = "DEBUG RETURN{nw}"
        say()
        return

      else:      
      
        # Remove question from qList, set it to currentQ
        self.__qList.remove(q)
        
        # Add another question if available (top-up to qList size 3)
        self.__queueQuestion()
        
        # Add question to asked
        self.__addAsked(q)
      
        # If question is not follow-up from last, remove follow-up and add 
        # another question if available (top-up to qList size 3)
#         if q != self.__currentQ:
#           self.__qList.remove(self.__currentQ)
#           self.__queueQuestion()
      
        # OUTPUT: Print player question text to terminal
        desc = self.userFormat(self.__questions[q])
        say()
        
        # TODO: Some kind of wait, or target is typing interlude?
        desc = self.typingMessage()
        say()
      
        # OUTPUT: Print target answer to terminal
        desc = self.targetFormat(self.__answers[q])
        say()

    
    # getFollowups(question) -> List<String>
    def getFollowups(self, question):
      
      question = question.upper()
      
      # Get the possible follow-ups
      followups = []
      for key in self.__followupQ.keys():
        if key[:-1] == question:
          followups.append(key)

      return followups      
    
    # followup(question)
    def followup(self, question):
    
      global desc
      
      q = question.upper()
      
      # DEBUG PRINT
      folStrings = []
      for key in self.getFollowups(q):
        lineStr = "  * " + key + ": " + self.__followupQ[key]
        folStrings.append(lineStr)

      desc = "\n".join(folStrings)
      say()
            
      # Display follow-up options, or option to ask another main question
      
      # If follow-up
      
        # OUTPUT: print follow-up question text to terminal
        
        # TODO: some kind of wait, or target is typing interlude?
        
        # OUTPUT: Print target answer to terminal
        
        # Post-processing
        
        # Return to question prompt
      
      # Else
      
        # No follow-up
        
        # Return to question prompt
      return
      
    
    
    
    
    
    
