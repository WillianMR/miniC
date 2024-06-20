import os
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

def process_code(input_stream):
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
        print("The code is syntactically correct.")

def process_file(file_path):
    input_stream = FileStream(file_path, encoding='utf-8')
    process_code(input_stream)

def process_directory(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.c'):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}...")
                process_file(file_path)
                print("\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_tests.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    process_directory(directory_path)
