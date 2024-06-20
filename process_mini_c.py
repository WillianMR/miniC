# process_mini_c.py
import sys
from antlr4 import *
from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser
from antlr4.error.ErrorListener import ErrorListener

class SyntaxErrorListener(ErrorListener):
    def __init__(self):
        super(SyntaxErrorListener, self).__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Syntax error at line {line}, column {column}: {msg}")

def process_file(file_path):
    input_stream = FileStream(file_path)
    lexer = MiniCLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniCParser(stream)
    
    error_listener = SyntaxErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)
    
    tree = parser.program()
    
    if error_listener.errors:
        for error in error_listener.errors:
            print(error)
    else:
        print(f"{file_path} is syntactically correct.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_mini_c.py <path_to_mini_c_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    process_file(file_path)
