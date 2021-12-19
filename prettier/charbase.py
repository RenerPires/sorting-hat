# INSPIRADO PELA FONTE CALVIN S

lettersTitle = [(' ','  \n  \n  \n'),('!','╦\n║\no\n'),('?','╔═╗\n ╔╝\n o \n'),('A','╔═╗\n╠═╣\n╩ ╩\n'),('B','╔╗ \n╠╩╗\n╚═╝\n'),('C','╔═╗\n║  \n╚═╝\n'),('D','╔╦╗\n ║║\n═╩╝\n'),('E','╔═╗\n║╣ \n╚═╝\n'),('F','╔═╗\n╠╣ \n╚  \n'),('G','╔═╗\n║ ╦\n╚═╝\n'),('H','╦ ╦\n╠═╣\n╩ ╩\n'),('I','╦\n║\n╩\n'),('J',' ╦\n ║\n╚╝\n'), ('K','╦╔═\n╠╩╗\n╩ ╩\n'),('L','╦  \n║  \n╩═╝\n'),('M','╔╦╗\n║║║\n╩ ╩\n'),('N','╔╗╔\n║║║\n╝╚╝\n'),('O','╔═╗\n║ ║\n╚═╝\n'),('P','╔═╗\n╠═╝\n╩  \n'),('Q','╔═╗ \n║═╬╗\n╚═╝╚\n'),('R','╦═╗\n╠╦╝\n╩╚═\n'),('S','╔═╗\n╚═╗\n╚═╝\n'),('T','╔╦╗\n ║ \n ╩ \n'),('U','╦ ╦\n║ ║\n╚═╝\n'),('V','╦  ╦\n╚╗╔╝\n ╚╝ \n'),('W','╦ ╦\n║║║\n╚╩╝\n'),('X','═╗ ╦\n╔╩╦╝\n╩ ╚═\n'),('Y','╦ ╦\n╚╦╝\n ╩ \n'),('Z','╔═╗\n╔═╝\n╚═╝\n')]

lettersSubtitle = [(' ','  \n  \n  \n'),('!','╦\n║\no\n'),('?','╔═╗\n ╔╝\n o \n'),('A','┌─┐\n├─┤\n┴ ┴\n'),('B','┌┐ \n├┴┐\n└─┘\n'),('C','┌─┐\n│  \n└─┘\n'),('D','┌┬┐\n ││\n─┴┘\n'),('E','┌─┐\n├┤ \n└─┘\n'),('F','┌─┐\n├┤ \n└  \n'),('G','┌─┐\n│ ┬\n└─┘\n'),('H','┬ ┬\n├─┤\n┴ ┴\n'),('I','┬\n│\n┴\n'),('J',' ┬\n │\n└┘\n'), ('K','┬┌─\n├┴┐\n┴ ┴\n'),('L','┬  \n│  \n┴─┘\n'),('M','┌┬┐\n│││\n┴ ┴\n'),('N','┌┐┌\n│││\n┘└┘\n'),('O','┌─┐\n│ │\n└─┘\n'),('P','┌─┐\n├─┘\n┴  \n'),('Q','┌─┐ \n│─┼┐\n└─┘└\n'),('R','┬─┐\n├┬┘\n┴└─\n'),('S','┌─┐\n└─┐\n└─┘\n'),('T','┌┬┐\n │ \n ┴ \n'),('U','┬ ┬\n│ │\n└─┘\n'),('V','┬  ┬\n└┐┌┘\n └┘ \n'),('W','┬ ┬\n│││\n└┴┘\n'),('X','─┐ ┬\n┌┴┬┘\n┴ └─\n'),('Y','┬ ┬\n└┬┘\n ┴ \n'),('Z','┌─┐\n┌─┘\n└─┘\n')]

def prettifystring(string, style):
    # NORMALIZE STRING
    string = string.upper().replace('\n', ' ')

    # style = 0: TITLE
    # style = 1: subtitle

    if style == "title":
        for char, result in lettersTitle:
            string = string.replace(char, result)
    else:
        for char, result in lettersSubtitle:
            string = string.replace(char, result)

    string = string.split('\n')
    
    ln1 = ""
    ln2 = ""
    ln3 = ""

    for i in range(0, len(string)):
        if i%3 == 0:
            ln1 += string[i]
        elif i%3 == 1:
            ln2 += string[i]
        elif i%3 == 2:
            ln3 += string[i]

    string = """{}
{}
{}""".format(ln1, ln2, ln3)

    return string