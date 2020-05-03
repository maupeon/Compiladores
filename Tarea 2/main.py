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
import automata
import Lexer


if __name__ == "__main__":
    automata = automata.Automata()
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
        identifier = regular_expressions[regular_expression][0]
        alphabet = regular_expressions[regular_expression][1]
        REPostfix = automata.convertREToPostfix(regular_expression,alphabet)
        #print(REPostfix)
        automata.convertREToNFA(identifier, REPostfix, alphabet)
        '''
        nfa_example = automata_IO.nfa_json_importer('quintuple_NFA.json')
        automata_IO.nfa_to_dot(nfa_example, 'graphic_NFA', './')
        '''
        automata.createTransitionMatrix()
        automata.NFA_to_DFA()
    
    '''
    dfa_example = automata_IO.dfa_json_importer('quintuple_DFA.json')
    automata_IO.dfa_to_dot(dfa_example, 'graphic_DFA', './')
    '''
    lexer = Lexer.Lexer()
    DFAs = lexer.readFileDFAs("quintuple_DFA.json")
    tokens = lexer.readFileTokens("code.txt")
    lexer.evalauteTokens(DFAs,tokens)