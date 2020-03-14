'''
Mauricio Peon Garcia
Alexandro Francisco Marcelo Gonzalez A0102183
Andres Campos Tams
28 Feb 2020
Tarea 1: RE -> NFA -> DFA
'''

# Class to convert the regular expression in infix to postfix
class Conversion: 
    # Constructor
    def __init__(self): 
        # The stack  
        self.stack = [] 
        # Precedence setting 
        self.operatorsPrecedence = {'|':1, '.':2, '*':3, '+':3}
        # Output    
        self.postfix = [] 
  
    # Check if the precedence of operator is less than top of stack or not 
    def notGreater(self, operator): 
        try: 
            a = self.operatorsPrecedence[operator] 
            b = self.operatorsPrecedence[self.stack[-1]] 
            return True if a <= b else False
        except KeyError:  
            return False
    
    def isOperand(self, token):
        try:
            if token.isalpha() or isinstance(int(token), int):
                return True
            else:
                False
        except:
            False
        

    # The main function that converts given infix expression to postfix expression 
    def infixToPostfix(self, infix): 
        currentExpression=[]
        # Iterate over the expression for conversion 
        for token in infix: 
            # If the token is an operand, add it to output
            if self.isOperand(token):
                self.postfix.append(token) 
              
            # If the token is an '(', push it to stack 
            elif token  == '(': 
                self.stack.append(token) 
  
            # If the token is an ')', pop and output from the stack until and '(' is found and remove '(' and ')'
            elif token  == ')': 
                while((len(self.stack) > 0) and (self.stack[-1] != '(')):
                    self.postfix.append(self.stack.pop())
                    if self.stack[-1] == '(':
                        self.stack.pop()
                        break

            # If the token is an operator (*,+,|) 
            elif token in self.operatorsPrecedence: 
                while((len(self.stack) > 0) and (self.notGreater(token))): 
                    self.postfix.append(self.stack.pop()) 
                self.stack.append(token) 
  
        # pop all the operator from the stack 
        while self.stack: 
            self.postfix.append(self.stack.pop()) 
  
        print("RE to Postfix:","".join(self.postfix))
        return self.postfix

class Automata():
    def __init__(self):
        # For storing the regular expression read from the file
        self.RE=""
        # For the postfix from the regular expression
        self.REPostfix=[]
        # For storing tempoarlly the evaluated symbols
        self.stack=[]
        # For the transition table
        self.transitionTable=[]

    # Read the file and store the Regular expression
    def readFile(self,filename):
        try:
            f = open(filename,"r")
            if f.mode == 'r':
                self.RE=f.readline()
                print(self.RE)
            else:
                print("ERROR reading file")
            f.close() 
        except:
            print("ERROR file not found")

    # Call the Conversion class which going to convert from infix to postfix the RE
    def convertREToPostfix(self):
        conversion = Conversion()
        self.REPostfix = conversion.infixToPostfix(self.RE)
        print(self.REPostfix)

    # Function to convert the regular expression into a NFA
    def convertREToNFA(self):
        for token in self.REPostfix:
            if token == '.':
                pass
                #A = self.stack.pop()
                #B = self.stack.pop()
                # Call a concatenation function
            elif token == '|':
                pass
                #A = self.stack.pop()
                #B = self.stack.pop()
                # Call a union function
            elif token == '*':
                pass
                #A = self.stack.pop()
                # Call a kleene star function
            elif token == '+':
                pass
                #A = self.stack.pop()
                # Call a one or more function
            else:
                pass
                #evaluate the current symbol
            

if __name__ == "__main__":
    automata = Automata()
    automata.readFile("RE.txt")
    automata.convertREToPostfix()
    automata.convertREToNFA()


