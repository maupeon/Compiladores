'''
Mauricio Peón García                    A01024162
Alexandro Francisco Marcelo González    A0102183
Andrés Campos Tams                      
28 Feb 2020
Tarea 1: RE -> NFA -> DFA By reading a file containing the RE and the alphabet

pip3 install pysimpleautomata
sudo apt install python-pydot python-pydot-ng graphviz 

'''

from PySimpleAutomata import DFA, automata_IO,NFA
import json

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
        self.operatorsPrecedence = {'|':1, '.':2, '*':3, '+':3, '?':3}
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

    # The main function that converts given infix expression to postfix expression 
    def infixToPostfix(self, infix, alphabet): 
        currentExpression=[]
        # Iterate over the expression for conversion 
        for token in infix: 
            # If the token is an operand, add it to output
            if token in alphabet:
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
                self.alphabet=[line.rstrip('\n') for line in f]
                print("ALPHABET:",self.alphabet)
                print("REGULAR EXPRESION:",self.RE)
            else:
                print("ERROR reading file")
            f.close() 
        except:
            print("ERROR file not found")
    
    # Call the Conversion class which going to convert from infix to postfix the RE
    def convertREToPostfix(self):
        conversion = Conversion()
        self.REPostfix = conversion.infixToPostfix(self.RE, self.alphabet)
        print(self.REPostfix)

    # Auxiliar functions to make a cleaner code to retrieve information of the transition table
    def startNodeTransition(self, transition):
        return transition[STARTNODE]
    def finalNodeTransition(self, transition):
        return transition[FINALNODE]
    def transitionToken(self, transition):
        return transition[TOKEN]

    def symbolEvaluation(self, token):
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
        
        if self.transitionToken(B) == '*' or self.transitionToken(B) == '+' or self.transitionToken(B) == '?':
            print("POPO")
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

    def plusEvaluation(self):
        A = self.stack.pop(len(self.stack)-1)
        startNode = self.startNodeTransition(A)
        finalNode = self.finalNodeTransition(A)
        self.NFA.append([finalNode, startNode,'e'])
        self.stack.append([startNode, finalNode, '+'])

    def zeroOrOneEvaluation(self):
        A = self.stack.pop(len(self.stack)-1)
        startNode = self.N
        finalNode = startNode+1
        self.NFA.append([startNode, self.startNodeTransition(A),'e'])
        self.NFA.append([self.finalNodeTransition(A), finalNode,'e'])
        self.NFA.append([startNode, finalNode,'e'])
        self.stack.append([startNode, finalNode, '?'])
        self.N = self.N+2

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
                #A = self.stack.pop()
                # Call a one or more function
                self.plusEvaluation()
            elif token == '?':
                #A = self.stack.pop()
                # Call a zero or more function
                self.zeroOrOneEvaluation()
            else:
                #evaluate the current symbol
                self.symbolEvaluation(token)
        
        print()
        print("The transition table of the NFA is:",self.NFA)
        print()
        self.stack
        print("The stack is:",self.stack)
    
    def createOutputFile(self,starNode,finalNode):
        output_file ={}
        print("NFA",self.NFA)
        output_file['alphabet'] = list(set([i[-1] for i in self.NFA]))
        output_file['states'] = [str(i) for i in range(self.N)]
        output_file['initial_states'] = [starNode]
        output_file['accepting_states'] = [finalNode]

        for element in self.NFA:
            element[1], element[2] = element[2], element[1]

        output_file['transitions'] = [[str(j) for j in i] for i in self.NFA]

        with open('input_test.json', 'w') as json_file:
            json.dump(output_file, json_file)

        return output_file
        


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
                
            self.createOutputFile(str(self.startNodeTransition(aux)), str(self.finalNodeTransition(aux)))

          
        elif automataType == "DFA":
            pass
        else:
            print("ERROR writing to file, type not matched")

        f.close() 
if __name__ == "__main__":
    automata = Automata()
    '''
    In order to run this program you must to create a file called, i.e., "RE.txt" which has to contain the 
    Regular expresion and the alphabet, such as:
    0*.1.0*.1.0*.1.0*
    0
    1
    Where the first line is the RE and the next ones are the alphabet
    '''
    automata.readFile("RE.txt")
    automata.convertREToPostfix()
    automata.convertREToNFA()
    automata.writeToFile("NFA.txt","NFA")


    nfa_example = automata_IO.nfa_json_importer('input_test.json')
   


    automata_IO.nfa_to_dot(nfa_example, 'output', './')

