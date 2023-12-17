from antlr4 import FileStream, CommonTokenStream
from antlr4.MiniGPLexer import MiniGPLexer
from antlr4.MiniGPParser import MiniGPParser

def parse(input_file):
    input_stream = FileStream(input_file)
    lexer = MiniGPLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniGPParser(stream)
    tree = parser.prog() 
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    print ('\n----- Test 1 -----\n')
    parse('test1.mgp')
    print('\n----- Test 2 -----\n')
    parse('test2.mgp')
    print('\n----- Test 3 -----\n')
    parse('test3.mgp')
    print('\n----- Test 4 -----\n')
    parse('test4.mgp')
    print('\n----- Test 5 -----\n')
    parse('test5.mgp')