import json

class Lexer():
    def __init__(self):
        # For the tokens to be evaluated
        self.tokens=[]

    # Read the file and store the tokens
    def readFileTokens(self,filename):
        try:
            f = open(filename,"r")
            tokens = []
            while True:
                content = f.readline()
                if not content: break  # EOF
                print(content)
                for token in list(content.split(" ")):
                    if "\n" in token and len(token) > 2:
                        tokens.append(token.strip("\n"))
                        tokens.append("\n")
                    else:
                        tokens.append(token)
                #tokens.append(content)
            f.close()
            return tokens
        except:
            print("ERROR verify that the file which contains the RE has the correct format")
    
    # Read the file and store the DFAs
    def readFileDFAs(self,filename):
            f = open(filename,"r")
            if f.mode == 'r':
                DFAs = []
                while True:
                    content = f.readline()
                    #print(content)
                    if not content or content == '\n': break
                    #print(content)
                    DFA = json.loads(content)
                    #print(DFA)
                    DFAs.append(DFA)
                f.close()
                return DFAs
            else:
                print("ERROR reading file")
            f.close() 
        
    # Function to validate if the given string is in the RE using the transition matrix
    def evalauteTokens(self, DFAs, tokens):
        with open('output.txt', 'w') as file:
            for token in tokens:
                type_token = "INVALID"
                if token != "\n":
                    for DFA in DFAs:
                        type_token = self.typeToken(token.strip(';'), DFA)
                        if type_token != "INVALID":
                            break
                    print(token.strip(';'),"->",type_token)
                    file.write(type_token.strip(';')+" ")
                    if ";" in token:
                        file.write(";")
                else:
                    file.write(token)
           
            
    # Function to validate if the given string is in the RE using the transition matrix
    def typeToken(self,token,DFA):
        transitions = DFA['transitions']
        final_states = DFA['accepting_states']
        flag = 0
        state = 0
        states = {}
        transitions_states = {}#{a:[[b,c]] for a,b,c in transitions}
        aux = []
        #{char:[[from,to]...]}
        for a,b,c in transitions:
            if b in transitions_states:
                transitions_states[b].update({a:c})
                aux=[]
            else:
                transitions_states[b] = {a:c}
        #print(transitions_states)
        # Evaluate with the DFA transition table
        if token[0] in transitions_states:
            #print("kakakakaa:",str(DFA['initial_state'][0]), transitions_states[token[0]])
            if DFA['initial_state'][0] in transitions_states[token[0]]:
                #print("STATE:",'0', "Character:", token[0])
                state = transitions_states[token[0]][DFA['initial_state'][0]]
                for character in token[1:]:
                    #print("STATE:",state, "Character:", character)
                    if character in transitions_states:
                        if state in transitions_states[character]:
                            state = transitions_states[character][state]
                        else:
                            return "INVALID"
                    else:
                        return "INVALID"
                if state in final_states:
                    return DFA['identifier']
                else:
                    return "INVALID"
            else:
                return "INVALID"
        else:
            return "INVALID"
        return "INVALID"
