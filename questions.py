import random as rd

from prettier.prettierprint import prettierprint as pprint

letters = ["A", "B", "C", "D", "E", "F", "G", "H"]

c = ["Grifinória", "Corvinal", "Lufa-Lufa", "Sonserina"]

grif = """
                      ░▒▓██▓▒                      
                 ▒▓█████████████▓▓▒                
        ░▒▓████████▓▓▒░      ░▒▓████████▓▒░        
     ███████▓▓▒▒▓█▓                 ░▒▓███████▓    
     ██▒          ▒██░                      ███    
     ██             ░█▓░▒▓▓▓▓███▓           ▒█▓    
     ██           ▒▓▓▓██▓▒▒▒░░  ▓█▒         ▓█▓    
     ██         ▓█▓▒   ▓█         ██░       ▒█▓    
     ██       ▓██▒      ██       ▓▓▒██      ▒██    
     ██      █▓  █░      █░     ▓█   ▒█▓    ▒██    
     ██    ░█▒   ▓█      ▓█     █▒ ███▓▓█▒  ▒██    
     ██    █▒     █      ░█     █▒  ░░   █▒ ▒██    
     ██░  ██     ▒█       █     █▓      ▓█  ▒██    
     ██▒  █     ░█▒      ░█     █▓     ░█   ▓█▓    
     ▓█▓ ░█     █▒       ▓█     █▓░▒▒  █▓   ██▒    
     ░██  ██             █░     ██▓▓▓███    ██     
      ██░  ██           █▓      █▒         ▓█▓     
      ▒██   ██        ▒█▒       █          ██░     
       ██▒   ██     ▓██        ▓▓ ▒▓████▓▒▓██      
       ░██    █▓░▓██▓░         ███▓▒     ▓██       
        ▓██    ██░            ██░        ██░       
         ███    █▓          ░█▓         ██▒        
          ███    █▓       ░██░        ░██▒         
           ▓██    █▓   ▒▓██▓         ▒██▒          
            ▒██▓   ████▓▓░          ███            
              ███░                ▓██▓             
               ▒███░            ▓███░              
                 ▒███▓       ░▓███░                
                   ░████▒ ░▓███▓                   
                      ░▓████▓                      
"""

corv = """
                         ▓▓                        
                       ░████▒                      
                   ░▓████▒░████▓░                  
      ▓▒▒▒▒▒▒▓▓███████▓      ▒███████▓▓▒▒▒▒▒▒▓     
      ███████████▓▒       ░      ▒▓███████████░    
      ██                 █▓▓▓▓▓▒            ██     
      ██            ▒▓▓▓█▓ ░ ░▒██           ██░    
      ██    ▓▓     ██▒  ░██▒    ██          ██░    
      ██  ▓██▒    ██▓▓▓▓▓█▓      █▒         ██░    
      ██▒█▓░█     ░     ░▒█▓     ░█         ██     
      ██▓  ░█              █▒     ▓█        ██     
      ██   ░█              ▒█      █▒       ██     
      ██    █               ██     ▓█       ██     
      ██    █▓               █     ▒█▓      ██     
      ██░   ▒█               █░    ▓▓█▒     ██     
      ██▒    ▓█             ▒█     █░▒█░   ▒██     
      ▓█▓     ▓█▒          ▒█░    ░█  ██▓▒▓██▓     
      ▒█▓      ░██▓▒    ░▓██      █▓  █░░▒ ▓█▓     
      ░██         ▒▓█████▓░      ██   █░   ██░     
       ██▒                      ██    █   ░██      
       ░██                    ▓█▓    ▓█   ██▒      
        ▓██▒               ░▓██      █░  ██▓       
         ▓███▓▓▒▒░   ░░▒▓▓██▓       █▓  ███        
          ▓██▒░▒▓▓▓███▓▓▒▒         █▓ ░██▓         
           ░███░                  █▓ ███░          
             ▒███▓░             ▒█████▒            
                ▓███▓░        ▒████▓░              
                  ░▓███▓    ▓███▓░                 
                     ░▓██▓▓███░                    
                        ▒██▒                       
"""

lufa = """
                      ▒▓█████▓▒                    
                   ▓█████▓▓▓█████▓                 
                ▓███▓▒         ▒████▓              
      ░▓░  ░▒████▓                ░████▓▒░ ░░▓     
      ▒███████▓                      ▒████████░    
      ▒██      ▒▓▓▓                         ██     
      ▒██     ▒█  ██▒▒▒▒░                   ██░    
      ▒██      ▓█▓█▓▒▒▒▓██▓░                ██     
      ▒██      ▒█░        ░▓█▓▒             ██     
      ▒██     ▒█▓▓▓▓███▒▒█▓▒ ░▓▓▓▓▒░▒░      ██     
      ░██     ██░     ░▓████▓  ░▒▓███▒      ██     
      ░██    ██            ░▒▓▓▒▒░ ▓█       ██     
       ██   ░█░                 ░▒▓▓        ██     
       ██   ██░        ▓████▓█████▓░       ░██     
       ██   █▓█      ▒█▓░         ▒▓██▓    ░██     
       ██░ ░█ ▓█     █░              ░██▒  ▒██     
       ██▒  █  ▒█▓   █                 ░█▓ ▒█▓     
       ▓█▓  ██   ▓██▒██                  █▒▓█▒     
       ░██   █▒    ░▓▓██▓                 ███      
        ██░  ░█        ░▓██░              ▓██      
        ▒██   ██          ▒█▓             ██░      
         ███  ██            █▓           ██▓       
          ██▓▒█             ░█          ██▓        
           ▓██               █▒       ▒██▓         
            ▒███░            █▒     ▒███░          
              ▓███▓          █    ▓███▒            
                ▒████▒      ▒█ ▒████░              
                   ▒████▒   █████▒                 
                      ▒███▓███▒                    
                         ██▓                       
"""

sons = """
                         ▓░                        
                       ▒███▓                       
                    ▒████░▓███▓░                   
               ░▒█████▒     ░▓████▓▒░              
      ▓▓▓▓████████▓▒     ▒▓     ▒█████████▓▓▓      
      ██████▓▒░      ░▓██▓▓██░       ▒▓▓█████      
      ▓█▒         ▒▓█▓▓░    ▒██▒           ██      
      ▓█▓       ▒█▓▒ ░        ░██░        ▒██      
      ▓██       █▓ ▓██          ▒█▒       ▓██      
      ▒██       █▓       ▓██     ▒█       ▓█▓      
      ▒██        ███▓▒▒▓█░ █▒     █       ▓█▓      
      ░██    ░███▓░ ░▓▓░ ▒█▓     ▒█       ██▒      
      ░██      ▓█      ▓█▓      ▓█░       ██▒      
       ██           ▒██▒      ▓██         ██░      
       ██         ▓██░     ░██▓           ██       
       ██      ▒██▓      ▓██▒     ░▓▓▓▒   ██       
       ██░   ▓██▒      ▓█▓░    ░▓██▓▒▒▓█▓░██       
       ▓██ ▒█▓░     ░██▓     ▒██▓       ▓██▓       
        ███▓      ▒██▒     ▓██▒         ▒██        
         ██▒     ██     ▒██▓           ▒██         
          ██▓    ▒█▓▓▓███▒            ▒██░         
           ███     ░▒▒░       ░██░   ▓██           
            ███░            ▒██▓    ███            
             ▒██▓        ░▓██▒    ▓██▓             
               ███▒  ░▒▓██▓     ░███               
                ░████▒▒▒       ███▒                
                  ▒██▓       ▓██▓                  
                    ▓███   ▓███                    
                      ▓██████                      
                        ▒█▓                        
"""

casas = ["G", "C", "L", "S"]

pontos = [0, 0, 0, 0]

questions = [
    #0
    [
        [
            "Amanhecer ou Anoitecer?",["Amanhecer", "Anoitecer"], ["G C", "L S"]
        ], [
            "Floresta ou Rio?", ["Floresta", "Rio"], ["G C", "L S"]
        ], [
            "Lua ou Estrelas?", ["Lua", "Estrelas"], ["S C", "G L"]
        ]
    ],
    #1
    [
        [
            "Do que você mais odiaria que as pessoas te chamassem?", 
            ["Comum", "Ignorante", "Covarde", "Egoísta"],
            ["S", "C", "G", "L"],
        ],
        [
            "Depois de morrer, o que você mais gostaria que as pessoas fizessem ao ouvir seu nome?",
            ["Sentir sua falta, mas sorrir", "Saber mais sobre as suas aventuras", "Pensar em você com admiração pelas suas conquistas", "Não me importo com o que as pessoas pensam de mim depois que estou morto"],
            ["L", "G", "C", "S"]
        ],
        [
            "Como você gostaria de ser conhecido na história?",
            ["Sábio", "Bom", "Grandioso", "Ousado"],
            ["C", "L", "S", "G"]
        ],
        [
            "Se pudesse escolher, você preferiria inventar uma poção que te garantisse:",
            ["Amor", "Gloria", "Sabedoria", "Poder"],
            ["L", "G","C", "S"]
        ],
    ],
    #2
    [
        [
            "Quatro taças são colocadas diante de você. Qual você escolheria para beber?",
            ["O líquido espumoso e prateado que cintila como se contivesse diamantes moídos dentro.", "A bebida macia, espessa e roxa que exala um cheiro delicioso de chocolate e ameixas.", "O líquido dourado tão brilhante que machuca os olhos e que faz as manchas solares dançarem por toda a sala.", "O misterioso líquido negro que brilha como tinta e exala vapores que o fazem ter estranhas visões."],
            ["C", "L", "G", "S"]
        ],
        [
            "Que tipo de instrumento agrada mais ao seu ouvido?",
            ["Violino", "Trompete", "Piano", "Tambor"],
            ["S", "L", "C", "G"]
        ],
        [
            "Você entra em um jardim encantado. O que você gostaria de examinar primeiro?",
            ["A árvore de folhas prateadas com maçãs douradas", "Os cogumelos vermelhos gordos que parecem estar conversando", "A piscina borbulhante, em cujas profundezas algo luminoso está girando", "A estátua de um velho mago com um olho estranhamente cintilante"],
            ["C", "L", "S", "G"]
        ],
        [
            "Quatro caixas são colocadas diante de você. Qual você tentaria abrir?", 
            ["A pequena caixa de tartaruga, adornada com ouro, dentro da qual alguma pequena criatura parece grunir.", "A caixa preta reluzente com uma fechadura e uma chave de prata, marcada com uma runa misteriosa que você sabe ser a marca de Merlin.", "A caixa de ouro ornamentado, apoiado em pés com garras, cuja inscrição avisa que tanto o conhecimento secreto quanto a tentação insuportável estão dentro dela.", "A pequena caixa de estanho, despretensiosa e simples, com uma mensagem riscada que diz 'Eu abro apenas para os dignos.'"],
            ["L", "S", "C", "G"],
        ],
        [
            "Um arbusto mágico produz flores que adaptam seu perfume de acordo com o que agrada quem sente seu aroma, para você teria o cheiro de:",
            ["Uma lareira crepitante", "De mar", "Livro novo", "Sua casa"],
            ["G", "S", "C", "L"]
        ],
    ],
    #3
    [
        [
            "Qual das opções a seguir você acha mais difícil de lidar?",
            ["Fome", "Frio", "Solidão", "Tédio", "Ser Ignorado"],
            ["C C L L", "L L S S", "G G L", "G G S", "C C S"]
        ],
        [
            "Um troll enfurecido está no escritório do diretor em Hogwarts. Ele está prestes a esmagar e rasgar vários itens e tesouros insubstituíveis.\nOs itens são:\n * A cura para varíola de Dragão\n * Registro de estudantes de mais de 1000 anos\n * Um livro de runas estranhas escrito a mão\nEm que ordem você resgataria esses objetos do alcance do troll, se pudesse?",
            ["A Cura, Os Registros e O Livro", "A Cura, O livro e Os Registros", "O Livro, A Cura e Os Registros", "O Livro, Os Registros e A Cura", "Os Registros, A Cura e O Livro", "Os Registros, O Livro e A Cura"],
            ["L L G", "G G C", "C C S", "S S C", "L L S", "S S L"]
        ],
        [
            "O que você prefere ser:",
            ["Envejado", "Uma Inspiração", "Confiável", "Elogiado", "Apreciado", "Temido"],
            ["C S", "C", "G L", "G", "L", "S"]
        ]
    ],
    #4
    [
        [
            "Se você pudesse ter qualquer poder, qual escolheria?",
            ["Ler Mentes", "Invisibilidade", "Força Sobre Humana", "Falar com Animais", "Mudar o Passado", "Mudar Aparência"],
            ["C S", "G", "L S", "L", "S G", "C"]
        ],
        [
            "O que você está mais ansioso para aprender em Hogwarts?",
            ["Aparatação e Desaparatação", "Transfiguração", "Voar com a Vassoura", "Feitiços e Azarações", "Criaturas Magicas", "Segredos do Castelo", "Todas as Áreas Possíveis"],
            ["G S", "C", "G L", "S", "L", "G", "C"]
        ],
        [
            "Qual das criaturas a seguir você mais gostaria de estudar?",
            ["Centauros", "Goblins", "Sereianos", "Fantasmas", "Vampiros", "Lobisomens", "Trolls"],
            ["G C", "C", "L S", "G C", "S", "G L", "S L"]
        ],
    ],
    #5
    [
        [
            "Você e dois amigos precisam cruzar uma ponte guardada por um troll do rio que insiste em lutar contra um de vocês antes de deixar todos vocês passarem. Você:",
            ["Tentar confundir o troll para deixar vocês três passarem sem lutar.", "Sugerir sorteio para decidir qual de vocês lutará.", "Sugerir que vocês três lutem (sem contar ao troll).", "Se voluntaria a lutar sozinho."],
            ["C", "L", "S", "G"]
        ],
        [
            "Um de seus colegas de casa colou em um exame de Hogwarts usando uma pena de escrita automática. Agora ele é o primeiro da classe em Feitiços, colocando você em segundo lugar. O professor Flitwick suspeita do que aconteceu. Ele te puxa para um lado após a aula e pergunta se seu colega usou ou não uma pena proibida. O que você faz?",
            ["Mente e diz que não sabe (mas espero que outra pessoa diga a verdade ao professor Flitwick).", "Sugere ao professor Flitwick que pergunte ao seu colega (e decida dizer ao seu colega que se ele não disser a verdade, você o fará).", "Diz a verdade ao professor Flitwick. Se seu colega está preparado para vencer trapaceando, ele merece ser descoberto.", "Você não esperaria ser convidado a dizer a verdade ao professor Flitwick. Se você soubesse que alguém estava usando uma pena proibida, você contaria ao professor antes do início do exame."],
            ["L", "G", "C", "S"]
        ],
        [
            "Um trouxa o confronta e diz que eles têm certeza de que você é um bruxo. O que você faz?",
            ["Pergunta o que os faz pensar assim?", "Concorde e pergunte se eles gostariam de uma amostra grátis de um feitiço.", "Concordar e ir embora, deixando-o se perguntando se você está blefando?", "Diga a eles que você está preocupado com a saúde mental deles e ofereça-se para chamar um médico."],
            ["C", "S", "G", "L"]
        ],
        [
            "Qual pesadelo o deixaria mais assustado?",
            ["Estar em um lugar muito alto e perceber de repente que não há apoio para as mãos ou para os pés, nem barreira para impedi-lo de cair.", "Estar em uma sala escura e sem janelas, trancado, e perceber que há um olho no buraco da fechadura te observando.", "Acordar e descobrir que nem seus amigos nem sua família têm ideia de quem você é.", "Ser forçado a falar com uma voz tão boba que quase ninguém consegue entender você, e todos riem de você."],
            ["C", "G", "L", "S"]
        ],
        [
            "Qual estrada chama mais sua atenção?",
            ["A estrada larga, gramada e ensolarada.", "O beco estreito, escuro e iluminado apenas por lanternas", "O caminho sinuoso e cheio de folhas através da floresta.", "A rua de paralelepípedos repleta de edifícios antigos."],
            ["L", "S", "G", "C"]
        ],
        [
            "Tarde da noite, caminhando sozinho pela rua, você ouve um grito peculiar que acredita ter uma fonte mágica. O que você faz?",
            ["Prossiga com cuidado, mantendo uma mão na sua varinha escondida e atento a qualquer perturbação", "Pega sua varinha e tenta descobrir a origem do ruído", "Pega sua varinha e defende seus arredores", "Retira-se para as sombras e aguarda, enquanto analisa mentalmente os feitiços defensivos e ofensivos mais apropriados"],
            ["L", "G", "S", "C"]
        ]
    ],
    #6
    [
        "Se você fosse para Hogwarts, que animal de estimação escolheria para levar com você?",
        [
            "Gatos",
            ["Gato Malhado", "Gato Siamês", "Gato Ruivo", "Gato Preto", "Gato Branco"],
            ["G G S", "S S", "S S", "S S", "S S"]
        ],
        [
            "Corujas",
            ["Coruja Comum", "Coruja Parda", "Coruja Marrom", "Coruna da Neve", "Coruja do Celeiro"],
            ["C C", "C C", "C C", "C C L L", "C C"]
        ],
        [
            "Sapos",
            ["Sapo Comum", "Sapo Corredor", "Sapo Dragão", "Sapo Arlequim", "Sapo Arbóreo de Três Dedos"],
            ["L L", "L L", "L L G G", "L L", "L L C C"]
        ]
    ],
    #7
    [
        [
            "Preto ou Branco", ["Preto", "Branco"], ["G S", "C L"]
        ],[
            "Cara ou Coroa", ["Cara", "Coroa"], ["C L", "G S"]
        ], [
            "Esquerda ou Direita", ["Esquerda", "Direita"], ["C S", "G L"]
        ]
    ],
    #8 CORINGA
    [
        ["O Chapéu Seletor leva em consideração sua opinião.\nPara qual casa você NÃO gostaria de ser selecionado?",
        ["Grifinória", "Corvinal", "Lufa-Lufa", "Sonserina"],
        ["C C C C L L L L S S S S C C C C L L L L S S S S", "G G G G L L L L S S S S G G G G L L L L S S S S", "G G G G C C C C S S S S G G G G C C C C S S S S", "G G G G C C C C L L L L G G G G C C C C L L L L"]]
    ]
]

def cab(i):
    if i>=0:
        pprint("CHAPEU SELETOR", "title", "title")
        if i < 8:
            pprint("RESPONDA AS PERGUNTAS PARA SABER A QUAL CASA VOCÊ PERTENCE", colorstyle="blue")
    
    elif i == -1:
        pprint("     CHAPEU SELETOR", "title", "title")
        pprint("""
               ▒              ▒▓█▒                         
                █▒         ▒▓█████                         
                ▓███▒ ▒▓███████████▒                       
                 ▓██████████████████▒                      
                  ████████▓▓█████████▒                     
                   ▒▓▒▒     ██████████▒                    
                            ███████████▒                   
                            ████████████                   
                            █████████████                  
                           ██████████████                  
                          ███████████████                  
                         ████████████████                  
                        █████████████████                  
                       ██████████████████                  
                      ███████████████████                  
                     ████████████████████                  
                    █████████████████████▓                 
                   ███████████████████████                 
                  ████████████████████████▒                
                 ██████████████████████████▒               
               ▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓▓▓▓               
              ▓▓▓▓▓▓▓▓  ██████  ▓▓▓▓▓▓▓▓▓▓▓▓▓              
  ▒▓▓█████████▓▓▓▓▓▓▓▓  ██████  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████▓▓▒▒    
██████████████████████  ██████  ██████████████████████████▓
 ▒████████████████████          ███████████████████████████
   ▒████████████████████████████████████████████████████▓  
      ▓██████████████████████████████████████████████▓▒    
         ▒████████████████████████████████████████▓        
             ▒▓███████████████████████████████▓▒           
                   ▒▒▓▓▓▓████████████▓▓▓▒▒                  

""", colorstyle="title")

        pprint("                 PRESSIONE [ENTER] PARA COMEÇAR", colorstyle="blue")

def printQuestion(i):
    question = questions[i]
    q = rd.randint(0, len(question)-1)
    #print(f"{question[q][0]}\n")
    pprint(f"\n[{i+1}/9] {question[q][0]}\n", colorstyle="info")
    for i in range(0,len(question[q][1])):
        print(f"[{letters[i]}] {question[q][1][i]}\n")
    return q

def printQ6():
    pprint(f"[6/9] {questions[6][0]}\n", colorstyle="info")
    for i in range(1, len(questions[6][1:])+1):
        print(f"[{letters[i-1]}] {questions[6][i][0]}\n")
    
    resp = input("> ").upper()

    op = letters.index(resp)+1

    for i in range(0, len(questions[6][op][1])):
        print(f"\n[{letters[i]}] {questions[6][op][1][i]}")
    
    resp = input("\n> ").upper()
    contaPonto(6, op, letters.index(resp))    

def contaPonto(item, quest, resp):
    for casa in questions[item][quest][2][resp].split(" "):
        pontos[casas.index(casa)] += 1

def result(pts):
    casa = casas[pontos.index(max(pts))]

    if casa == 'G':
        pprint(grif, colorstyle="error")
        pprint("       GRIFINORIA", "title", "error")
    elif casa == 'C':
        pprint(corv, colorstyle="info")
        pprint("       CORVINAL", "title", "info")
    elif casa == 'L':
        pprint(lufa, colorstyle="warning")
        pprint("       LUFA LUFA", "title", "warning")
    else:
        pprint(sons, colorstyle="green")
        pprint("      SONSERINA", "title", "green")


        


