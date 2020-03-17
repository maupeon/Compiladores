'''
Mauricio Peón García                    A01024162
Alexandro Francisco Marcelo González    A0102183
Andrés Campos Tams                      A01024385
28 Feb 2020
Tarea 1: RE -> NFA -> DFA By reading a file containing the RE and the alphabet

pip3 install pysimpleautomata
sudo apt install python-pydot python-pydot-ng graphviz 

REQUIREMENTS:
    graphviz
    PySimpleAutomata
    pydot
    pydot-ng
'''

from PySimpleAutomata import DFA, automata_IO,NFA
import json
import numpy as np
import pprint

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
  
        #print("RE to Postfix:","".join(self.postfix))
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
        self.output_file = {}
        self.transition_matrix = []
        self.graph = {}

        self.DFA_file ={}

    # Read the file and store the Regular expression
    def readFile(self,filename):
        try:
            f = open(filename,"r")
            if f.mode == 'r':
                self.RE=f.readline()
                self.alphabet=[line.rstrip('\n') for line in f]
                #print("ALPHABET:",self.alphabet)
                #print("REGULAR EXPRESION:",self.RE)
            else:
                print("ERROR reading file")
            f.close() 
        except:
            print("ERROR file not found")
    
    # Call the Conversion class which going to convert from infix to postfix the RE
    def convertREToPostfix(self):
        conversion = Conversion()
        self.REPostfix = conversion.infixToPostfix(self.RE, self.alphabet)
        #print(self.REPostfix)

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
        
        if self.transitionToken(B) == '*' or self.transitionToken(B) == '+' or self.transitionToken(B) == '?' or self.transitionToken(B) == '|':
            self.stack.append([startNode, finalNode+1, '.'])
            self.N = self.N
        else:
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
        
        #print()
        #print("The transition table of the NFA is:",self.NFA)
        #print()
        self.stack
        #print("The stack is:",self.stack)
    
    def createOutputFile(self,starNode,finalNode):
        
        #print("NFA",self.NFA)
        self.output_file['alphabet'] = list(set([i[-1] for i in self.NFA]))
        self.output_file['states'] = [str(i) for i in range(self.N)]
        self.output_file['initial_states'] = [starNode]
        self.output_file['accepting_states'] = [finalNode]

        for element in self.NFA:
            element[1], element[2] = element[2], element[1]

        self.output_file['transitions'] = [[str(j) for j in i] for i in self.NFA]

        
        with open('input_NFA.json', 'w') as json_file:
            json.dump(self.output_file, json_file)



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

    def epsilon_closure(self, states):
        set_of_states = []
        stack = []
        
        for element in states:
            stack.append(element)
            while stack:
                node = stack.pop()
                set_of_states.append(node)
                for i in self.graph[node]:
                    if self.transition_matrix[node][i] == 'e':
                        stack.append(i)
        #print("set_", set(set_of_states))
        return set(set_of_states)

    def createTransitionMatrix(self):
        w, h = self.N, self.N
        self.transition_matrix = [['' for x in range(w)] for y in range(h)] 
        for transition in self.NFA:
            self.transition_matrix[transition[0]][transition[2]] = transition[1]
            self.graph.setdefault(transition[0], []).append(transition[2]) 
        self.graph.setdefault(self.N - 1, [])
        

    def NFA_to_DFA(self):
        iterator = 0
        transitions = []
        NFA_states = [1 for i in range(self.N)] 
        initial_state = int(self.output_file["initial_states"][0])
        final_state = int(self.output_file["accepting_states"][0])
        alphabet = self.alphabet
        DFA_states = []
        path = {}
        DFA_path = {}
        DFA_states.append(self.epsilon_closure([initial_state]))
        NFA_states[initial_state] = 1
        for state in DFA_states:
            path = {}
            for element in state:
                NFA_states[element] = 1
                for i in self.graph[element]:
                        if self.transition_matrix[element][i] != 'e':
                            for char in alphabet:
                                if self.transition_matrix[element][i] == char:
                                    path.setdefault(char,[]).append(i)
            DFA_path[iterator] = path
            for e in DFA_path[iterator]:
                if self.epsilon_closure(DFA_path[iterator][e]) not in DFA_states:
                    DFA_states.append(self.epsilon_closure(DFA_path[iterator][e]))
            iterator+=1
        
        for index, element in enumerate(DFA_states):
            for char in DFA_path[index]:
                transition = []
                transition.append(str(index))
                transition.append(char)
                transition.append(str(DFA_states.index(self.epsilon_closure(DFA_path[index][char]))))
                transitions.append(transition)
        
        DFA_final_states = [0 for i in range(len(DFA_states))] 

        for index,state in enumerate(DFA_states):
            if final_state in state:
                DFA_final_states[index]=1

        self.DFA_file['alphabet'] = alphabet
        self.DFA_file['states'] = [str(i) for i in range(len(DFA_states))]
        self.DFA_file['initial_state'] ='0'
        self.DFA_file['accepting_states'] = [str(i) for i,e in enumerate(DFA_final_states) if e == 1 ]
        self.DFA_file['transitions'] = transitions

        with open('input_DFA.json', 'w') as json_file:
            json.dump(self.DFA_file, json_file)

        print(json.dumps(self.DFA_file,indent=2))
            
        


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
    nfa_example = automata_IO.nfa_json_importer('input_NFA.json')
    automata_IO.nfa_to_dot(nfa_example, 'output_NFA', './')
    
    automata.createTransitionMatrix()
    automata.NFA_to_DFA()
    dfa_example = automata_IO.dfa_json_importer('input_DFA.json')
    automata_IO.dfa_to_dot(dfa_example, 'output_DFA', './')

