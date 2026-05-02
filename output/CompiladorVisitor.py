# Generated from Compilador.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CompiladorParser import CompiladorParser
else:
    from CompiladorParser import CompiladorParser

# This class defines a complete generic visitor for a parse tree produced by CompiladorParser.

class CompiladorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CompiladorParser#inicio.
    def visitInicio(self, ctx:CompiladorParser.InicioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#instrucciones.
    def visitInstrucciones(self, ctx:CompiladorParser.InstruccionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#Declaracion.
    def visitDeclaracion(self, ctx:CompiladorParser.DeclaracionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#Asignacion.
    def visitAsignacion(self, ctx:CompiladorParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#SumRes.
    def visitSumRes(self, ctx:CompiladorParser.SumResContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#Numero.
    def visitNumero(self, ctx:CompiladorParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#Variable.
    def visitVariable(self, ctx:CompiladorParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#MulDiv.
    def visitMulDiv(self, ctx:CompiladorParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiladorParser#Parentesis.
    def visitParentesis(self, ctx:CompiladorParser.ParentesisContext):
        return self.visitChildren(ctx)



del CompiladorParser