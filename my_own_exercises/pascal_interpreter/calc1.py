# A simple Pascal interpreter that just adds two single-digit integers

# Token types
# 
# EOF token indicates no more input left for lexical analysis
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

class Token(object):
  def __init__(self, type, value):
    # token type: INTEGER, PLUS, or EOF
    self.type = type
    # token value: 0-9, '+', or None
    self.value = value

  def __str__(self):
    """String representation of the instance

    Examples:
      Token(INTEGER, 3)
      Token(PLUS '+')
    """
    return 'Token({type}, {value})'.format(
        type=self.type,
        value=repr(self.value)
    )

    def __repr__(self):
      return self.__str__()

class Interpreter(object):
  def __init__(self, text):
    # client string input, e.g. "3+5"
    self.text=text
    # self.pos is an index to into self.text
    self.pos = 0
    # current token instance
    self.current_token = None

  def error(self):
    raise Exception('Error parsing output')

  def get_next_token(self):
    
