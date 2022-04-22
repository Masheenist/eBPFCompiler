from compiler
from compiler.ast import *
from ply.lex import lex
from ply.yacc import yacc

names = { }

class P3Parse:
    
    def p_program(p):
        'program : form'
        
        print(p[1])

    def p_form_while(p):
        '''
        form : definition
             | expression
        '''
        p[0] = p[1]

    def p_expression(p):
        '''
        expression : constant
                   | while_expression
                   | ID
                   | display
        '''
        p[0] = p[1]

    def p_expression_if(p):
        '''statement : IF LPAREN comparison RPAREN LBRACKET statement RBRACKET
                     | IF LPAREN comparison RPAREN LBRACKET statement RBRACKET ELSE LBRACKET statement RBRACKET'''
        
        if p[3]:
            p[0] = p[6]
        elif p[10] is not None:
            p[0] = p[10]

    def p_expression_while(p):  
        'while_expression :  WHILE LPAREN comparison_expression RPAREN LBRACKET expression'
        while(p[3]):
            p[0] = p[6]

    def p_statement_print(p):
        'statement : PRINT LPAREN expression RPAREN ENDSTM'
        print(p[3])

    def p_neg_expression(p):
        'expression : NEG expression'

        p[0] = UnarySub(t[2])

    def p_symbol(p):
        '''
        symbol : ADD
               | NEG
        '''
        p[0] = p[1]

    def p_boolean(p):
        '''
        boolean : TRUE
                | FALSE
        '''
        p[0] = p[1]

    def p_constant(p):
        '''
        constant : INT
                 | CHARACTER
                 | STRING
                 | BOOL
        '''
        p[0] = p[1]

    parse_p3 = yacc.yacc()
    return parse_p3.P3Parse()