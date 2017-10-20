init -1 python: 

  class Email:

    ##
    ## Constructor
    ##
    
    # Initialize the Email:
    #     id:   String - unique identifier, used in $emaillist
    #     text: String - pre-formatted for terminal output
    # No validation is done on inputs.
    def __init__(self, id, text):
      self.__id = id
      self.__read = False
      self.__text = ""


    ##
    ##  Accessors
    ##
    
    # getId() -> String
    def getId(self):
      return self.__id

    # getRead() -> Bool
    def getRead(self):
      return self.__read

    # getText() -> String
    def __getText(self):
      return self.__text


    ## 
    ##  Mutators
    ## 
    
    # setRead(): sets read flag
    def __setRead(self):
      self.__read = True

    ##
    ##  Methods
    ## 
    
    # read() -> String
    # The programmatic way to interact with an email in the game
    def read(self):
      # TODO: Time increment?
      self.__setRead()
      return self.__getText()
