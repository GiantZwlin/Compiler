from parser.compsent import compsent
from parser.consexpl import consexpl
from parser.procdefi import procdefi
from parser.varexl import varexl


def block():
    consexpl()
    varexl()
    procdefi()
    compsent()
