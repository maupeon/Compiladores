'''
Mauricio Peon Garcia
Alexandro Francisco Marcelo Gonzalez A0102183
Andres Campos Tams
28 Feb 2020
Tarea 1: RE -> NFA -> DFA
'''

# Declaration of global constants
STARTNODE=0
FINALNODE=1
TOKEN=2

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
        # For the transition table of the NFA
        self.NFA=[]
        # For the number of nodes in the NFA
        self.N=0
        # For the alphabet
        self.alphabet=set()

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

    # Auxiliar functions to make a cleaner code to retrieve information of the transition table
    def startNodeTransition(self, transition):
        return transition[STARTNODE]
    def finalNodeTransition(self, transition):
        return transition[FINALNODE]
    def transitionToken(self, transition):
        return transition[TOKEN]

    def symbolEvaluation(self, token):
        self.alphabet.add(token)
        startNode = self.N
        finalNode = self.N+1
        self.stack.append([startNode, finalNode, token])
        self.NFA.append([startNode, finalNode, token])
        self.N = self.N+2

    def unionEvaluation(self):
        A = self.stack.pop(len(self.stack)-2)
        B = self.stack.pop(len(self.stack)-1)
        if self.transitionToken(A) == '|':
            startNode = self.startNodeTransition(A)
            finalNode = self.finalNodeTransition(A)
            self.NFA.append([startNode, self.startNodeTransition(B),'e'])
            self.NFA.append([self.finalNodeTransition(B), finalNode,'e'])
        else:
            startNode = self.N
            finalNode = startNode+1
            self.NFA.append([startNode, self.startNodeTransition(A),'e'])
            self.NFA.append([startNode, self.startNodeTransition(B),'e'])
            self.NFA.append([self.finalNodeTransition(A), finalNode,'e'])
            self.NFA.append([self.finalNodeTransition(B), finalNode,'e'])
            self.N = self.N+2
        self.stack.append([startNode, finalNode, '|'])

    def kleeneStarEvaluation(self):
        A = self.stack.pop(len(self.stack)-1)
        startNode = self.N
        finalNode = startNode+1
        self.NFA.append([startNode, self.startNodeTransition(A),'e'])
        self.NFA.append([self.finalNodeTransition(A), finalNode,'e'])
        self.NFA.append([self.finalNodeTransition(A), self.startNodeTransition(A),'e'])
        self.NFA.append([startNode, finalNode,'e'])
        self.N = self.N+2
        self.stack.append([startNode, finalNode, '*'])
    
    def concatenationEvaluation(self):
        A = self.stack.pop(len(self.stack)-2)
        B = self.stack.pop(len(self.stack)-1)
        startNode = self.startNodeTransition(A)
        finalNode = self.finalNodeTransition(B)-1
        
        if self.transitionToken(B) == '*':
            self.stack.append([startNode, finalNode+1, '.'])
            
            self.N = self.N
        else:
            new=self.NFA.pop()
            self.stack.append([startNode, finalNode, '.'])
            self.N = self.N-1
        #self.NFA.append([self.finalNodeTransition(A), self.startNodeTransition(B),self.transitionToken(B)])
        if self.transitionToken(B) in self.alphabet:
            self.NFA.append([self.finalNodeTransition(A), self.startNodeTransition(B),self.transitionToken(B)])
        else:
            self.NFA.append([self.finalNodeTransition(A), self.startNodeTransition(B),"e"])
       
        '''
        if self.transitionToken(A) == '.':
            pass
        else:
            self.stack.append([startNode, finalNode, '.'])
        self.N = self.N-1
        '''

    # Function to convert the regular expression into a NFA
    def convertREToNFA(self):
        for token in self.REPostfix:
            if token == '.':
                #A = self.stack.pop()
                #B = self.stack.pop()
                # Call a concatenation function
                self.concatenationEvaluation()
            elif token == '|':
                #A = self.stack.pop()
                #B = self.stack.pop()
                # Call a union function
                self.unionEvaluation()
            elif token == '*':
                #A = self.stack.pop()
                # Call a kleene star function
                self.kleeneStarEvaluation()
            elif token == '+':
                pass
                #A = self.stack.pop()
                # Call a one or more function
            else:
                #evaluate the current symbol
                self.symbolEvaluation(token)
        
        print()
        print("The transition table of the NFA is:",self.NFA)
        print()
        self.stack
        print("The stack is:",self.stack)

    def writeToFile(self, filename, automataType):
        f = open(filename,"w+")
        aux=self.stack.pop()
        #listToStr = '\n'.join([[' '.join([str(elem) for elem in s]) ]' '.join(str(elem)) for elem in self.NFA]) 
        
        if automataType == "NFA":
            '''
            Writing the quintuple of the NFA, where:
            alphabet
            number set of states (0,1,2,...,n-1)
            final states
            start state
            transition function
            '''
            f.write(" ".join(self.alphabet))
            f.write("\n"+str(self.N))
            f.write("\n"+str(self.finalNodeTransition(aux)))
            f.write("\n"+str(self.startNodeTransition(aux)))
            for transition in self.NFA:
                element = ' '.join([str(elem) for elem in transition]) 
                f.write("\n"+element)
        elif automataType == "DFA":
            pass
        else:
            print("ERROR writing to file, type not matched")

        f.close() 
if __name__ == "__main__":
    automata = Automata()
    automata.readFile("RE.txt")
    automata.convertREToPostfix()
    automata.convertREToNFA()
    automata.writeToFile("NFA.txt","NFA")



