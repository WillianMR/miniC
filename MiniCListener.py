# Generated from A:/GitHub/miniC/MiniC.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete listener for a parse tree produced by MiniCParser.
class MiniCListener(ParseTreeListener):

    # Enter a parse tree produced by MiniCParser#program.
    def enterProgram(self, ctx:MiniCParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniCParser#program.
    def exitProgram(self, ctx:MiniCParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniCParser#declInclude.
    def enterDeclInclude(self, ctx:MiniCParser.DeclIncludeContext):
        pass

    # Exit a parse tree produced by MiniCParser#declInclude.
    def exitDeclInclude(self, ctx:MiniCParser.DeclIncludeContext):
        pass


    # Enter a parse tree produced by MiniCParser#funcaoPrincipal.
    def enterFuncaoPrincipal(self, ctx:MiniCParser.FuncaoPrincipalContext):
        pass

    # Exit a parse tree produced by MiniCParser#funcaoPrincipal.
    def exitFuncaoPrincipal(self, ctx:MiniCParser.FuncaoPrincipalContext):
        pass


    # Enter a parse tree produced by MiniCParser#declFuncoes.
    def enterDeclFuncoes(self, ctx:MiniCParser.DeclFuncoesContext):
        pass

    # Exit a parse tree produced by MiniCParser#declFuncoes.
    def exitDeclFuncoes(self, ctx:MiniCParser.DeclFuncoesContext):
        pass


    # Enter a parse tree produced by MiniCParser#listaArgumentos.
    def enterListaArgumentos(self, ctx:MiniCParser.ListaArgumentosContext):
        pass

    # Exit a parse tree produced by MiniCParser#listaArgumentos.
    def exitListaArgumentos(self, ctx:MiniCParser.ListaArgumentosContext):
        pass


    # Enter a parse tree produced by MiniCParser#tipo.
    def enterTipo(self, ctx:MiniCParser.TipoContext):
        pass

    # Exit a parse tree produced by MiniCParser#tipo.
    def exitTipo(self, ctx:MiniCParser.TipoContext):
        pass


    # Enter a parse tree produced by MiniCParser#comando.
    def enterComando(self, ctx:MiniCParser.ComandoContext):
        pass

    # Exit a parse tree produced by MiniCParser#comando.
    def exitComando(self, ctx:MiniCParser.ComandoContext):
        pass


    # Enter a parse tree produced by MiniCParser#expRel.
    def enterExpRel(self, ctx:MiniCParser.ExpRelContext):
        pass

    # Exit a parse tree produced by MiniCParser#expRel.
    def exitExpRel(self, ctx:MiniCParser.ExpRelContext):
        pass


    # Enter a parse tree produced by MiniCParser#expRelAux.
    def enterExpRelAux(self, ctx:MiniCParser.ExpRelAuxContext):
        pass

    # Exit a parse tree produced by MiniCParser#expRelAux.
    def exitExpRelAux(self, ctx:MiniCParser.ExpRelAuxContext):
        pass


    # Enter a parse tree produced by MiniCParser#opRelacional.
    def enterOpRelacional(self, ctx:MiniCParser.OpRelacionalContext):
        pass

    # Exit a parse tree produced by MiniCParser#opRelacional.
    def exitOpRelacional(self, ctx:MiniCParser.OpRelacionalContext):
        pass


    # Enter a parse tree produced by MiniCParser#exprAritmetica.
    def enterExprAritmetica(self, ctx:MiniCParser.ExprAritmeticaContext):
        pass

    # Exit a parse tree produced by MiniCParser#exprAritmetica.
    def exitExprAritmetica(self, ctx:MiniCParser.ExprAritmeticaContext):
        pass


    # Enter a parse tree produced by MiniCParser#t.
    def enterT(self, ctx:MiniCParser.TContext):
        pass

    # Exit a parse tree produced by MiniCParser#t.
    def exitT(self, ctx:MiniCParser.TContext):
        pass


    # Enter a parse tree produced by MiniCParser#f.
    def enterF(self, ctx:MiniCParser.FContext):
        pass

    # Exit a parse tree produced by MiniCParser#f.
    def exitF(self, ctx:MiniCParser.FContext):
        pass


    # Enter a parse tree produced by MiniCParser#expressao.
    def enterExpressao(self, ctx:MiniCParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by MiniCParser#expressao.
    def exitExpressao(self, ctx:MiniCParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by MiniCParser#parametros.
    def enterParametros(self, ctx:MiniCParser.ParametrosContext):
        pass

    # Exit a parse tree produced by MiniCParser#parametros.
    def exitParametros(self, ctx:MiniCParser.ParametrosContext):
        pass



del MiniCParser