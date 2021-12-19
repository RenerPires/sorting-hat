# MODULO CRIADO POR RENER PIRES PARA AUXILIAR NO PROCESSO DE CRIAÇÃO DE CABEÇALHOS E PRINTS COLORIDOS EM PYTHON
# NADA ALÉM DE UMA FRESCURINHA PARA DEIXAR A APLICAÇÃO TEXTO MAIS BONITA E REDUZIR A VERBOSIDADE DA PERSONALIZAÇÃO
# E CLARO, UM ESTUDO A RESPEITO DA CRIAÇÃO DE LIBS E MODULES EM PYTHON ALÉM DE DEF"S COM PARÂMETROS OPCIONAIS E AFINS
# FAÇA BOM PROVEITO ;)

from .charbase import prettifystring as pstr

def prettierprint(string, type="default", colorstyle="default"):
    strColors = {"title" : "\033[34m",
    "default" : "\033[37m",
    "info" : "\033[35m",
    "blue" : "\033[36m",
    "green" : "\033[32m",
    "warning" : "\033[33m",
    "error" : "\033[31m",
    "bold" : "\033[1m",
    "underline" : "\033[4m",
    "end" : "\033[0m"}
    
    if type != "default":
        string = pstr(string, type)

    string = """{}{}{}""".format(strColors[colorstyle], string, strColors["end"])

    print(string)