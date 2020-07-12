# Biblioteca para calcular a data 

from datetime import date 

# Pegar os dados do cliente:


# Pegar a data
data = input("Qual dia da semana gostaria de levar seu cãozinho? (Ex.: 03/08/2018): ")

# Pegar Quantidade de Cães Pequenos
qntCaoPequeno = input("Você levará algum cãozinho que tem o porte pequeno, se sim quantos? (Se não pode informar 0):  ")


#Pegar Quantidade de Cães Grandes

qntCaoGrande = input("Você levará algum cãozinho que tem o porte grande, se sim quantos? (Se não pode informar 0):  ")

# Lista para converter o dia da semana
Dias = [
    'Segunda',
    'Terça',
    'Quarta',
    'Quinta',
    'Sexta',
    'Sabado',
    'Domingo'
]

# selecionar a data correta de acordo com a informações inserida 

dataselect = date(day=int(data.split("/",1)[0]),month=int(data.split("/",2)[1]),year=int(data.split("/",3)[2]))

# Calcula o dia da semana

diaDaSemana = Dias[dataselect.weekday()]

# Função do Petshop MeuCaninoFeliz para calcular o valor dos banhos de acordo com o dia da semana

def MeuCaninoFeliz(qntCaoPequeno, qntCaoGrande, diaDaSemana):

    distancia = 2000

    if int(qntCaoPequeno) > 0: 
        if (diaDaSemana == 'Segunda') or (diaDaSemana == 'Terça') or (diaDaSemana =='Quarta') or (diaDaSemana == 'Quinta') or (diaDaSemana =='Sexta'):
            VcaopequenoM = (int(qntCaoPequeno) * 20)
            nomePetShop = "Meu Canino Feliz"
        
   
        if (diaDaSemana == 'Sabado') or (diaDaSemana == 'Domingo'):
            VcaopequenoM = (int(qntCaoPequeno) * 24)
            nomePetShop = "Meu Canino Feliz"
    else:
            VcaopequenoM = 0


    if int(qntCaoGrande) > 0:
        if (diaDaSemana == 'Segunda') or (diaDaSemana == 'Terça') or (diaDaSemana == 'Quarta') or (diaDaSemana == 'Quinta') or (diaDaSemana == 'Sexta'):
            VcaograndeM = (int(qntCaoGrande) * 40)
            nomePetShop = "Meu Canino Feliz"
    
        if (diaDaSemana == 'Sabado') or (diaDaSemana == 'Domingo'):
            VcaograndeM = (int(qntCaoGrande) * 48)
            nomePetShop = "Meu Canino Feliz"
    else:
        VcaograndeM = 0
    
    Vtotal = VcaopequenoM + VcaograndeM

    return distancia, Vtotal, nomePetShop

# Função do Petshop VaiRex para calcular o valor dos banhos de acordo com o dia da semana    

def VaiRex(qntCaoPequeno, qntCaoGrande, diaDaSemana): # feriados

    distancia = 1700

    if int(qntCaoPequeno) > 0:
        if (diaDaSemana == 'Segunda') or (diaDaSemana == 'Terça') or (diaDaSemana == 'Quarta') or (diaDaSemana == 'Quinta') or (diaDaSemana =='Sexta'):
            VcaopequenoV = (int(qntCaoPequeno) * 15)
            nomePetShop = "Vai Rex"

        if (diaDaSemana == 'Sabado') or (diaDaSemana == 'Domingo'):
            VcaopequenoV = (int(qntCaoPequeno) * 20)
            nomePetShop = "Vai Rex"
    else:
        VcaopequenoV = 0
 
    if int(qntCaoGrande) > 0:
        if (diaDaSemana == 'Segunda') or (diaDaSemana == 'Terça') or (diaDaSemana == 'Quarta') or (diaDaSemana == 'Quinta') or (diaDaSemana == 'Sexta'):
            VcaograndeV = (int(qntCaoGrande) * 50)
            nomePetShop = "Vai Rex"

        if (diaDaSemana == 'Sabado') or (diaDaSemana == 'Domingo'):
            VcaograndeV = (int(qntCaoGrande) * 55)
            nomePetShop = "Vai Rex"
    else:
        VcaograndeV = 0

    Vtotal = VcaopequenoV + VcaograndeV

    return distancia, Vtotal, nomePetShop

# Função do Petshop ChowChawgas para calcular o valor dos banhos de acordo com o dia da semana

def ChowChawgas(qntCaoPequeno, qntCaoGrande, diaDaSemana):

    distancia = 800

    if int(qntCaoPequeno) > 0:
        if (diaDaSemana == 'Segunda') or (diaDaSemana == 'Terça') or (diaDaSemana == 'Quarta') or (diaDaSemana == 'Quinta') or (diaDaSemana == 'Sexta') or (diaDaSemana == 'Sabado') or (diaDaSemana == 'Domingo'):
            VcaopequenoC = (int(qntCaoPequeno) * 30)
            nomePetShop = "ChowChawgas"
    else:
        VcaopequenoC = 0

    if int(qntCaoGrande) > 0:
        if (diaDaSemana == 'Segunda') or (diaDaSemana == 'Terça') or (diaDaSemana == 'Quarta') or (diaDaSemana == 'Quinta') or (diaDaSemana == 'Sexta') or (diaDaSemana == 'Sabado') or (diaDaSemana == 'Domingo'):
            VcaograndeC = (int(qntCaoGrande) * 45)
            nomePetShop = "ChowChawgas"
    else:
        VcaograndeC = 0

    Vtotal = VcaopequenoC + VcaograndeC

    return distancia, Vtotal, nomePetShop


# Chama as funções de com o retorno (distancia, valor total do banho, nome do petshop)

resultMeuCaninoFeliz =  MeuCaninoFeliz(qntCaoPequeno, qntCaoGrande, diaDaSemana)
resultVaiRex =  VaiRex(qntCaoPequeno, qntCaoGrande, diaDaSemana)
resultChowChawgas =  ChowChawgas(qntCaoPequeno, qntCaoGrande, diaDaSemana)


# Identifica qual o Petshop mais em conta Eduardo poderá levar seus cachorros

# Se os valores forem iguais o desempate será a distância

if resultVaiRex[1] == resultChowChawgas[1]:
    if resultVaiRex[0] > resultChowChawgas[0]:
        print("Olá Eduardo, irei te ajudar a escolher o melhor Petshop neste dia da semana, n(o) {0} o Petshop {1} que fica a {2} metros de distância,o valor total dos banhos é de R${3},00 e de acordo com os demais Petshops este é o melhor da região.".format(diaDaSemana, resultChowChawgas[2],resultChowChawgas[0],resultChowChawgas[1]))
    else:
       print("Olá Eduardo, irei te ajudar a escolher o melhor Petshop neste dia da semana, n(o) {0} o Petshop {1} que fica a {2} metros de distância,o valor total dos banhos é de R${3},00 e de acordo com os demais Petshops este é o melhor da região.".format(diaDaSemana,resultVaiRex[2],resultVaiRex[0],resultVaiRex[1]))
    
if resultMeuCaninoFeliz[1] == resultChowChawgas[1]:
    if resultMeuCaninoFeliz[0] > resultChowChawgas[0]:
       print("Olá Eduardo, irei te ajudar a escolher o melhor Petshop neste dia da semana, n(o) {0} o Petshop {1} que fica a {2} metros de distância,o valor total dos banhos é de R${3},00 e de acordo com os demais Petshops este é o melhor da região.".format(diaDaSemana,resultChowChawgas[2],resultChowChawgas[0],resultChowChawgas[1]))
    else:
       print("Olá Eduardo, irei te ajudar a escolher o melhor Petshop neste dia da semana, n(o) {0} o Petshop {1} que fica a {2} metros de distância,o valor total dos banhos é de R${3},00 e de acordo com os demais Petshops este é o melhor da região.".format(diaDaSemana,resultMeuCaninoFeliz[2],resultMeuCaninoFeliz[0],resultMeuCaninoFeliz[1]))

# Calcula qual será o mais em conta.

if resultVaiRex[1] < resultMeuCaninoFeliz[1] and resultVaiRex[1] < resultChowChawgas[1]:
   print("Olá Eduardo, irei te ajudar a escolher o melhor Petshop neste dia da semana, n(o) {0} o Petshop {1} que fica a {2} metros de distância,o valor total dos banhos é de R${3},00 e de acordo com os demais Petshops este é o melhor da região.".format(diaDaSemana,resultVaiRex[2],resultVaiRex[0],resultVaiRex[1]))
        
if resultMeuCaninoFeliz[1] < resultVaiRex[1] and resultMeuCaninoFeliz[1] < resultChowChawgas[1]:
   print("Olá Eduardo, irei te ajudar a escolher o melhor Petshop neste dia da semana, n(o) {0} o Petshop {1} que fica a {2} metros de distância,o valor total dos banhos é de R${3},00 e de acordo com os demais Petshops este é o melhor da região.".format(diaDaSemana,resultMeuCaninoFeliz[2],resultMeuCaninoFeliz[0],resultMeuCaninoFeliz[1]))

if resultChowChawgas[1] < resultMeuCaninoFeliz[1] and resultChowChawgas[1] < resultVaiRex[1]:
   print("Olá Eduardo, irei te ajudar a escolher o melhor Petshop neste dia da semana, n(o) {0} o Petshop {1} que fica a {2} metros de distância,o valor total dos banhos é de R${3},00 e de acordo com os demais Petshops este é o melhor da região.".format(diaDaSemana,resultChowChawgas[2],resultChowChawgas[0],resultChowChawgas[1]))

