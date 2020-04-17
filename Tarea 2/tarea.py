'''
Mauricio Peón García                    A01024162
Alexandro Francisco Marcelo González    A01021383
Andrés Campos Tams                      A01024385
28 Feb 2020
Tarea 1: RE -> NFA -> DFA By reading a file containing the RE and the alphabet

REQUIREMENTS:
    graphviz
    PySimpleAutomata
    pydot
    pydot-ng
    pip3 install pysimpleautomata
    sudo apt install python-pydot python-pydot-ng graphviz 
'''

from PySimpleAutomata import DFA, automata_IO,NFA
import json
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
        # Precedence setting & is concatenation, @ is kleen star and # is +
        self.operatorsPrecedence = {'|':1, '&':2, '@':3, '#':3, '?':3}
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

            # If the token is an operator (@,#,|) 
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
        # For the outputfile
        self.output_file = {}
        # for the transition table of the DFA
        self.transition_matrix = []
        # For the DFA
        self.graph = {}
        # For the output of the DFA
        self.DFA_file ={}
        # For the strings to be evaluated
        self.strings=[]

    # Read the file and store the Regular expression
    def readFile(self,filename):
        try:
            f = open(filename,"r")
            if f.mode == 'r':
                RE = ""
                REs = {}
                while True:
                    alphabet = []
                    RE = f.readline().rstrip('\n')
                    alpha = f.readline().rstrip('\n')
                    if not RE or not alpha: break  # EOF
                    for symbol in alpha:
                        if symbol != ',':
                            if symbol != '\n':
                                alphabet.append(symbol)
                    REs[RE]=alphabet

                print("REGULAR EXPRESIONS:",REs)
                f.close() 
                return REs
            else:
                print("ERROR reading file")
            f.close() 
        except:
            print("ERROR verify that the file which contains the RE has the correct format")
    
    # Call the Conversion class which going to convert from infix to postfix the RE
    def convertREToPostfix(self, RE, alphabet):
        conversion = Conversion()
        return conversion.infixToPostfix(RE, alphabet)
        #print(self.REPostfix)

    # Auxiliar functions to make a cleaner code to retrieve information of the transition table
    def startNodeTransition(self, transition):
        return transition[STARTNODE]
    def finalNodeTransition(self, transition):
        return transition[FINALNODE]
    def transitionToken(self, transition):
        return transition[TOKEN]

    # Evaluate a symbol from the alphabet
    def symbolEvaluation(self, token):
        # Get the start and the final node for the transition
        startNode = self.N
        finalNode = self.N+1
        # Storing in the stack the evaluation and in the NFA the transition table
        self.stack.append([startNode, finalNode, token])
        self.NFA.append([startNode, finalNode, token])
        # Adding 2 because of 2 nodes added
        self.N = self.N+2

    # Evaluate the union of two nodes
    def unionEvaluation(self):
        # Get the start and the final node for the transition
        A = self.stack.pop(len(self.stack)-2)
        B = self.stack.pop(len(self.stack)-1)
        # If the first evaluation has an union, then the union has to be with it, otherwise there is a new union 
        if self.transitionToken(A) == '|':
            # Get the start and the final node for the transition
            startNode = self.startNodeTransition(A)
            finalNode = self.finalNodeTransition(A)
            # Storing the following transitions in the NFA table
            self.NFA.append([startNode, self.startNodeTransition(B),'$'])
            self.NFA.append([self.finalNodeTransition(B), finalNode,'$'])
        else:
            # Get the start and the final node for the transition
            startNode = self.N
            finalNode = startNode+1
            # Storing the following transitions in the NFA table
            self.NFA.append([startNode, self.startNodeTransition(A),'$'])
            self.NFA.append([startNode, self.startNodeTransition(B),'$'])
            self.NFA.append([self.finalNodeTransition(A), finalNode,'$'])
            self.NFA.append([self.finalNodeTransition(B), finalNode,'$'])
            # Adding 2 because of 2 nodes added
            self.N = self.N+2
        # Storing in the stack the evaluation    
        self.stack.append([startNode, finalNode, '|'])

    # Evaluation of the kleen star
    def kleeneStarEvaluation(self):
        # Get the previous evaluation
        A = self.stack.pop(len(self.stack)-1)
        # Get the start and the final node for the transition
        startNode = self.N
        finalNode = startNode+1
        # Storing the following transitions in the NFA table
        self.NFA.append([startNode, self.startNodeTransition(A),'$'])
        self.NFA.append([self.finalNodeTransition(A), finalNode,'$'])
        self.NFA.append([self.finalNodeTransition(A), self.startNodeTransition(A),'$'])
        self.NFA.append([startNode, finalNode,'$'])
        # Adding 2 because of 2 nodes added
        self.N = self.N+2
        # Storing in the stack the evaluation
        self.stack.append([startNode, finalNode, '@'])
    
    # Evaluation of the concatenation
    def concatenationEvaluation(self):
         # Get the start and the final node for the transition
        A = self.stack.pop(len(self.stack)-2)
        B = self.stack.pop(len(self.stack)-1)
        # Get the start and the final node for the transition
        startNode = self.startNodeTransition(A)
        finalNode = self.finalNodeTransition(B)-1
        
        # If the B evaluation has a @,|,?,# for the token, then we create a diferents nodes which is concatenated, otherwise, pop the top of the NFA table and concatenate with the previous evaluation 
        if self.transitionToken(B) == '@' or self.transitionToken(B) == '#' or self.transitionToken(B) == '?' or self.transitionToken(B) == '|':
            self.stack.append([startNode, finalNode+1, '&'])
            self.N = self.N
        else:
            self.NFA.pop()
            self.stack.append([startNode, finalNode, '&'])
            self.N = self.N-1
        #self.NFA.append([self.finalNodeTransition(A), self.startNodeTransition(B),self.transitionToken(B)])
        if self.transitionToken(B) in self.alphabet:
            self.NFA.append([self.finalNodeTransition(A), self.startNodeTransition(B),self.transitionToken(B)])
        else:
            self.NFA.append([self.finalNodeTransition(A), self.startNodeTransition(B),"e"])

    # Evaluation of #
    def plusEvaluation(self):
         # Get the previous evaluation
        A = self.stack.pop(len(self.stack)-1)
        # Get the start and the final node for the transition
        startNode = self.startNodeTransition(A)
        finalNode = self.finalNodeTransition(A)
        # Storing in the stack the evaluation and in the NFA the transition table
        self.NFA.append([finalNode, startNode,'$'])
        self.stack.append([startNode, finalNode, '#'])

    # Evaluation of ?
    def zeroOrOneEvaluation(self):
         # Get the previous evaluation
        A = self.stack.pop(len(self.stack)-1)
        # Get the start and the final node for the transition
        startNode = self.N
        finalNode = startNode+1
        # Storing in the stack the evaluation and in the NFA the transition table
        self.NFA.append([startNode, self.startNodeTransition(A),'$'])
        self.NFA.append([self.finalNodeTransition(A), finalNode,'$'])
        self.NFA.append([startNode, finalNode,'$'])
        self.stack.append([startNode, finalNode, '?'])
        self.N = self.N+2

    # Main function to convert the regular expression into a NFA
    def convertREToNFA(self, REPostfix, alphabet):
        self.stack=[]
        self.NFA=[]
        self.N=0
        self.output_file = {}
        self.transition_matrix = []
        self.graph = {}
        self.DFA_file ={}
        self.strings=[]
        self.alphabet = alphabet
        for token in REPostfix:
            if token == '&':
                # Call a concatenation function
                self.concatenationEvaluation()
            elif token == '|':
                # Call a union function
                self.unionEvaluation()
            elif token == '@':
                # Call a kleene star function
                self.kleeneStarEvaluation()
            elif token == '#':
                # Call a one or more function
                self.plusEvaluation()
            elif token == '?':
                # Call a zero or more function
                self.zeroOrOneEvaluation()
            else:
                #evaluate the current symbol
                self.symbolEvaluation(token)
        
        #print()
        #print("The transition table of the NFA is:",self.NFA)
        #print()
        #print("The stack is:",self.stack)
        aux=self.stack.pop()
        self.createOutputFile(str(self.startNodeTransition(aux)), str(self.finalNodeTransition(aux)), alphabet)

    # Creating the output which contains the quintuple of the NFA for graphic
    def createOutputFile(self,starNode,finalNode, alphabet):
        # Storing the quintuple of the NFA
        self.output_file['alphabet'] = alphabet
        self.output_file['states'] = [str(i) for i in range(self.N)]
        self.output_file['initial_states'] = [starNode]
        self.output_file['accepting_states'] = [finalNode]

        for element in self.NFA:
            element[1], element[2] = element[2], element[1]

        self.output_file['transitions'] = [[str(j) for j in i] for i in self.NFA]
        with open('quintuple_NFA.json', 'a') as json_file:
            json.dump(self.output_file, json_file)
            json_file.write('\n')


    # For evaluate each transition for the epsilon closure for a certain state
    def epsilon_closure(self, states):
        # Declaring the variables, to return the set of states and the stack which helps to store new nodes with also epsilon moves
        set_of_states = []
        stack = []
        # For each state in the states for the epsilon movements evaluates if it has more epsilon movements
        for element in states:
            stack.append(element)
            # While is not empty, has no more epsilon moves
            while stack:
                node = stack.pop()
                set_of_states.append(node)
                # Check if has epsilon moves append to the stack to evaluate for more epsilon moves
                if node in self.graph:
                    for i in self.graph[node]:
                        if self.transition_matrix[node][i] == '$':
                            stack.append(i)
        #print("set_", set(set_of_states))
        return set(set_of_states)

    # For creating the transition table for the DFA
    def createTransitionMatrix(self):
        # Create the transition matrix to make it simple when evaluating
        self.transition_matrix = [['' for x in range(self.N)] for y in range(self.N)] 
        #pprint.pprint(self.transition_matrix )
        # For each transition of the NFA store in the DFA table the transition values of the NFA
        for transition in self.NFA:
            #print(transition)
            self.transition_matrix[transition[0]][transition[2]] = transition[1]
            self.graph.setdefault(transition[0], []).append(transition[2]) 
        self.graph.setdefault(self.N-1, [])
        #pprint.pprint(self.graph)

    # The main function for the transformation from NFA to DFA
    def NFA_to_DFA(self):
        # Declaring some variables
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
        # Iterate from each state of the DFA, starting from the initial state of the NFA for evaluate the dfa transition
        for state in DFA_states:
            # Restore the path
            path = {}
            # Check which node in the state goes to another one with a symbol in the alphabet-
            for element in state:
                NFA_states[element] = 1
                if element in self.graph:
                    for i in self.graph[element]:
                            if self.transition_matrix[element][i] != '$':
                                for char in alphabet:
                                    if self.transition_matrix[element][i] == char:
                                        path.setdefault(char,[]).append(i)
            DFA_path[iterator] = path
            for e in DFA_path[iterator]:
                if self.epsilon_closure(DFA_path[iterator][e]) not in DFA_states:
                    DFA_states.append(self.epsilon_closure(DFA_path[iterator][e]))
            iterator+=1
        #print("DFA_STATES", DFA_states)
        # Generate the transition matrix.
        for index, element in enumerate(DFA_states):
            for char in DFA_path[index]:
                transition = []
                transition.append(str(index))
                transition.append(char)
                transition.append(str(DFA_states.index(self.epsilon_closure(DFA_path[index][char]))))
                transitions.append(transition)
        DFA_final_states = [0 for i in range(len(DFA_states))] 
        #Check which state is an accepting one.
        for index,state in enumerate(DFA_states):
            if final_state in state:
                DFA_final_states[index]=1
        # Generate de new dictionary of quintuple.
        self.DFA_file['alphabet'] = alphabet
        self.DFA_file['states'] = [str(i) for i in range(len(DFA_states))]
        self.DFA_file['initial_states'] =['0']
        self.DFA_file['accepting_states'] = [str(i) for i,e in enumerate(DFA_final_states) if e == 1 ]
        self.DFA_file['transitions'] = transitions
        # Write de quintuple in a json
        with open('quintuple_DFA.json', 'a') as json_file:
            json.dump(self.DFA_file, json_file)
            json_file.write('\n')
        #print("The quintuple of the DFA is: ")
        #print(json.dumps(self.DFA_file,indent=2))   

class Lexer():
    def __init__(self):
        # For the tokens to be evaluated
        self.tokens=[]

    # Read the file and store the tokens
    def readFileTokens(self,filename):
        try:
            f = open(filename,"r")
            if f.mode == 'r':
                content = f.read()
                self.tokens = content.split()
                f.close() 
                return(self.tokens)
            else:
                print("ERROR reading file")
            f.close() 
        except:
            print("ERROR verify that the file which contains the RE has the correct format")
    
    # Read the file and store the DFAs
    def readFileDFAs(self,filename):
            f = open(filename,"r")
            if f.mode == 'r':
                DFAs = []
                while True:
                    content = f.readline()
                    print(content)
                    if not content or content == '\n': break
                    #print(content)
                    DFA = json.loads(content)
                    print(DFA)
                    DFAs.append(DFA)
                f.close()
                return DFAs
            else:
                print("ERROR reading file")
            f.close() 
        
    # Function to validate if the given string is in the RE using the transition matrix
    def evalauteTokens(self, DFAs, tokens):
        for token in tokens:
            for DFA in DFAs:
                print("THE TOKEN:",token,"IS:",self.isValidToken(token, DFA))
            
    # Function to validate if the given string is in the RE using the transition matrix
    def isValidToken(self,token,DFA):
        transitions = DFA['transitions']
        final_states = DFA['accepting_states']
        flag = 0
        state = 0
        states = {}
        #print("AKSDNAKSJNDLKASJDNLAKJDNKASNDJKASN",token,DFA)
        # Evaluate with the DFA transition table
        for transition in transitions: 
            if transition[0] == DFA['initial_states'][0] and transition[1] == token[0]:
                state = transition[2]
                flag = 1
        if flag ==1:
            for index,character in enumerate(token[1:]):
                for transition in transitions:
                    if character == transition[1] and state == transition[0]:
                        state = transition[2]
                        break
            if state in final_states:
                return True
            else:
                return False
        else:
            return False
        return True

if __name__ == "__main__":
    automata = Automata()
    '''
    In order to run this program you must to create a file called, i.e., "RE.txt" which has to contain the 
    Regular expresion and the alphabet, such as:
    0@.1.0@.1.0@.1.0@
    0
    1
    Where the first line is the RE and the next ones are the alphabet
    '''
    regular_expressions = automata.readFile("RE.txt")
    with open('quintuple_NFA.json', 'w') as file:
        file.write("")
    with open('quintuple_DFA.json', 'w') as file:
        file.write("")
    for regular_expression in regular_expressions:
        #print(regular_expression)
        alphabet = regular_expressions[regular_expression]
        REPostfix = automata.convertREToPostfix(regular_expression,alphabet)
        #print(REPostfix)
        automata.convertREToNFA(REPostfix, alphabet)
        
        automata.createTransitionMatrix()
        automata.NFA_to_DFA()

    lexer = Lexer()
    DFAs = lexer.readFileDFAs("quintuple_DFA.json")
    tokens = lexer.readFileTokens("code.txt")
    lexer.evalauteTokens(DFAs,tokens)