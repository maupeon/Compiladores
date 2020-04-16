import re

class Lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):

        tokens = []

        source_code = self.source_code.split()

        #print("source_code",source_code)
        i = 0

        while i < len(source_code):
            
            word = source_code[i]

            #print("word: ",word)

            # 'cad' is the same as string
            # 'ent' is the same as integer
            # 'dec' is the same as float
            if word == "cad" or word == "ent" or word == "dec":
                tokens.append(["VAR_DECLARATION", word])

            # Check if the word is a number
            elif re.match(r'\d+(\.\d*)?',word):

                if word[len(word) - 1] == ";":
                    number = float( word[0:len(word) - 1]) if '.' in  word[0:len(word) - 1] else int( word[0:len(word) - 1])
                    check_int = isinstance(number, int)

                    if check_int:
                        tokens.append(['INT', word[0:len(word) - 1]])
                    else:
                        tokens.append(['FLOAT', word[0:len(word) - 1]])
                    
                else:
                    number = float( word[0:len(word) - 1]) if '.' in  word[0:len(word) - 1] else int( word[0:len(word) - 1])
                    check_int = isinstance(number, int)

                    if check_int:
                        tokens.append(['INT', word[0:len(word) - 1]])
                    else:
                        tokens.append(['FLOAT', word[0:len(word) - 1]])
            
            # Check if the word is an identifier
            elif re.match('[a-z]',word) or re.match('[A-Z]',word):
                if word[len(word) - 1] == ";":
                    tokens.append(['IDENTIFIER', word[0:len(word) - 1]])
                else:
                    tokens.append(['IDENTIFIER', word])

            # Check if the word is an operator
            elif word in "=/*=-+<>":
               tokens.append(['OPERATOR', word])
            
            # Check if the word is a semicollon
            if word[len(word) - 1] == ";":
                    tokens.append(['STATEMENT_END', ';'])

            i += 1

        print(tokens)

        return tokens



if __name__ == "__main__":
    
    content = ""

    with open('code.txt','r') as file:
        content = file.read()

    #print("content: ",content)
    lexer = Lexer(content)

    tokens = lexer.tokenize()