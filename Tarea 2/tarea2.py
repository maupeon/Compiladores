import re

class Lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):

        tokens = []

        source_code = self.source_code.split()

        print("source_code",source_code)
        source_index = 0

        while source_index < len(source_code):

            word = source_code[source_index]

            print("word: ",word)

            if word == "var":
                tokens.append(["VAR_DECLARATION", word])

            
            elif re.match(r'\d+(\.\d*)?',word):

                if word[len(word) - 1] == ";":
                    #tokens.append(['FLOAT', word[0:len(word) - 1]])

                    number = float( word[0:len(word) - 1]) if '.' in  word[0:len(word) - 1] else int( word[0:len(word) - 1])

                    check_int = isinstance(number, int)

                    if check_int:
                        tokens.append(['INT', word[0:len(word) - 1]])
                    else:
                        tokens.append(['FLOAT', word[0:len(word) - 1]])
                    
                    #print(check_int)
                else:

                    number = float( word[0:len(word) - 1]) if '.' in  word[0:len(word) - 1] else int( word[0:len(word) - 1])

                    check_int = isinstance(number, int)
                    if check_int:
                        tokens.append(['INT', word[0:len(word) - 1]])
                    else:
                        tokens.append(['FLOAT', word[0:len(word) - 1]])

                    #tokens.append(['FLOAT', word])

            elif re.match('[0-9]',word):
                if word[len(word) - 1] == ";":
                    tokens.append(['INTEGER', word[0:len(word) - 1]])
                else:
                    tokens.append(['INTEGER', word])

            elif re.match('[a-z]',word) or re.match('[A-Z]',word):
                if word[len(word) - 1] == ";":
                    tokens.append(['IDENTIFIER', word[0:len(word) - 1]])
                else:
                    tokens.append(['IDENTIFIER', word])

            elif word in "=/*=-+<>":
               
               tokens.append(['OPERATOR', word])

            if word[len(word) - 1] == ";":
                    tokens.append(['STATEMENT_END', ';'])

            source_index += 1

        print(tokens)

        return tokens



if __name__ == "__main__":
    
   
    content = ""

    with open('test.txt','r') as file:
        content = file.read()


    print("content: ",content)
    lexer = Lexer(content)

    tokens = lexer.tokenize()