// MiniC.g4
grammar MiniC;

// Parser rules
program         :   declInclude* funcaoPrincipal declFuncoes* EOF;
declInclude     :   '#include' '<' ID '.h' '>';
funcaoPrincipal :   'int' 'main' '(' ')' '{' comando* 'return' INT_LITERAL ';' '}';
declFuncoes     :   tipo ID '(' listaArgumentos ')' '{' comando* 'return' expressao ';' '}';
listaArgumentos :   tipo ID (',' tipo ID)*;
tipo            :   'int' | 'float' | 'double' | 'char';
comando         :   '{' comando* '}'
                |   'if' '(' expRel ')' comando 'else' comando
                |   'if' '(' expRel ')' comando
                |   'while' '(' expRel ')' comando
                |   'printf' '(' expressao ')' ';'
                |   'printint' '(' INT_LITERAL ')' ';'
                |   'printstr' '(' STRING_LITERAL ')' ';'
                |   tipo ID (',' ID)* ';'
                |   tipo ID '=' expressao (',' ID '=' expressao)* ';'
                |   ID '=' expressao ';';
expRel          :   expRelAux opRelacional expRelAux
                |   '!' '(' expRel ')';
expRelAux       :   ID | INT_LITERAL | FLOAT_LITERAL;
opRelacional    :   '>' | '<' | '==' | '>=' | '<=' | '!=';
exprAritmetica  :   exprAritmetica '+' t
                |   exprAritmetica '-' t
                |   t;
t               :   t '*' f
                |   t '/' f
                |   f;
f               :   '(' exprAritmetica ')'
                |   ID
                |   INT_LITERAL
                |   FLOAT_LITERAL
                |   ID '(' parametros* ')';
expressao       :   exprAritmetica
                |   CHAR_LITERAL
                |   STRING_LITERAL;
parametros      :   expressao (',' expressao)*;

// Lexer rules
ID              :   [a-zA-Z_][a-zA-Z_0-9]*;
INT_LITERAL     :   [0-9]+;
FLOAT_LITERAL   :   [0-9]+ '.' [0-9]+;
CHAR_LITERAL    :   '\'' ( ~[\r\n'] | '\\' [rnt\\] ) '\'';
STRING_LITERAL  :   '"' ( ~[\r\n"] | '\\' [rnt\\] )* '"';
COMMENT         :   '/*' .*? '*/' -> skip;
LINE_COMMENT    :   '//' ~[\r\n]* -> skip;
WS              :   [ \t\r\n]+ -> skip;
