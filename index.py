import pyautogui as bot
from pyautogui import click, moveTo
from time import sleep
import pygetwindow
import datetime

marca = """
    ___  ___                          _____   _____           _             
    |  \/  |                         |  _  | /  __ \         | |            
    | .  . | __ _ _ __ ___ ___  ___  | | | | | /  \/ __ _ ___| |_ _ __ ___  
    | |\/| |/ _` | '__/ __/ _ \/ __| | | | | | |    / _` / __| __| '__/ _ \ 
    | |  | | (_| | | | (_| (_) \__ \ \ \_/ / | \__/\ (_| \__ \ |_| | | (_) |
    \_|  |_/\__,_|_|  \___\___/|___/  \___/   \____/\__,_|___/\__|_|  \___/ 

==============================================================================
============ ^_^ Have I helped you in any way? All I ask is a tip!^_^ ========
============ ^_^ Faça sua boa ação de hoje, manda aquela gorjeta! ^_^ ========
==============================================================================
=============================== SEN BCOIN BUSD BNB ===========================
=================== 0x4fbF7EA40E39E6e9A283d7a2b4e2194a11f1C27E ===============
==============================================================================
==============================================================================
==============================================================================

            ===== Pressione "ctrl" + "c" para finalizar o BOT. =====
"""

print(marca)

aviso = """
================================= AVISO =================================
 O BOT só vai rodar se digitar o número de navegadores com o BombCrypto!!
      Infelizmente só funciona até 3 navegadores e no Google Chrome!
=========================================================================
"""
print(aviso)

while True:
    nb = int(input('Digite o número de navegadores abertos com o BombCrypto:'))
    if nb in (1, 2, 3):
        if nb == (1):
            print('Ok, colocando o código para rodar em 1 navegador...')
        else:
            print(f'Ok, colocando o código para rodar em {nb} navegadores...')
        break
    else:
        print('Esse BOT só aceita até 3 navegadores simultâneos. :(')


#=======================================AREA DOS DEF's==========================================

#============Def para o login===========
def login():
    print('Procurando o botão "connect"...')
    sleep(1)
    connect = bot.locateCenterOnScreen('./Imagens/connect.png')
    moveTo(connect)
    click()
    print('Procurando o botão connect da metamask...')
    sleep(1)
    connect2 = bot.locateCenterOnScreen('./Imagens/connect-2.png')
    moveTo(connect2)
    click()
    print('Procurando o botão assinar da carteira...')
    sleep(10)
    assinar = bot.locateCenterOnScreen('./Imagens/assinar.png')
    moveTo(assinar)
    click()

#============Processo dos heróis============
def herois():
    contador = 1
    while contador < 6:
        print('{} herois verificados'.format(contador))
        sleep(0.5)
        herois = bot.locateCenterOnScreen('./Imagens/green-bar.png')
        work = bot.locateCenterOnScreen('./Imagens/go-work.png')
        if herois:
            moveTo(work)
            click()
        contador += 1

#============Processo de arrastar a barra de herois===========
def scroll():
        print('Rolando a tela para procurar mais herois...')
        sleep(1.5)
        arrastar = bot.locateCenterOnScreen('./Imagens/vertical-bar.png')
        if arrastar:
            moveTo(arrastar)
            click()
            bot.drag(0,-300, 1.5)

#============Roteiro principal============
def roteiro():
    sleep(16)
    print('Acessando a tela dos heróis...')
    heroes = bot.locateCenterOnScreen('./Imagens/heroes.png')
    moveTo(heroes)
    click()
    #==Colocando para trabalhar==
    #=====5 herois por vez=======
    print('Colocando 5 heróis para trabalhar...')
    herois()
    #==Scroll para mais herois==
    sleep(0.5)
    scroll()
    #==Mais 5 herois agora==
    sleep(3)
    print('Colocando mais 5 heróis para trabalhar...')
    herois()
    #==Scroll para mais herois==
    sleep(0.5)
    scroll()
    sleep(2)
    #==Mais 5 para inteirar 15==
    print('Colocando mais 5 heróis para trabalhar, totalizando 15...')
    herois()
    #==Fechando menu de heróis==
    sleep(1)
    print('fechando a tela de heróis...')
    fechar = bot.locateCenterOnScreen('./Imagens/fechar.png')
    moveTo(fechar)
    click()
    sleep(1)
    print('Acessando o modo Amazon Survival...')
    amazon()
    bot.move(0,150)

#============Acessar o modo Amazon Survival============
def amazon():
    amazon = bot.locateCenterOnScreen('./Imagens/amazon.png')
    moveTo(amazon)
    click()

#======================================FIM DA AREA DOS DEF'S=======================================

#======Inicio do BOT propriamente dito======

print('BOT já vai selecionar uma janela do Google Chrome com o BombCrypto')

sleep(2)
#======Identificando o primeiro navegador======
time = datetime.datetime.now()
timenow = time.strftime('%d/%m/%Y %H:%M:%S')
print(f'Selecionando o primeiro navegador...---{timenow}---')
title = 'Bombcrypto - Google Chrome'
window1 = pygetwindow.getWindowsWithTitle(title) [0]
window1.activate()
window1.maximize()

login()

#======Repetição infinita do código abaixo======
while True: 
    roteiro()

    sleep(1)

    if nb == 1:
        afk = 0
        while afk < 7:
            time = datetime.datetime.now()
            timenow = time.strftime('%d/%m/%Y %H:%M:%S')
            print(f'Em 8 minutos o bot vai para o menu e volta (Anti-AFK) ---{timenow}---')

            sleep(480)
            voltar = bot.locateCenterOnScreen('./Imagens/back.png')
            moveTo(voltar)
            click()

            sleep(1)
            print('Retornando ao modo Amazon Survival...')
            amazon()
            afk += 1
            if afk < 7:
                print(f'Rodada {afk} de 7 concluída, até voltar a procurar os herois novamente!')
            else:
                print(f'Rodada {afk} de 7 concluída!')
            sleep(1)


    #======================Código com 2 navegadores (Se houver)=========================
    
    #======Identificando o segundo navegador======

    if nb == (2):
        time = datetime.datetime.now()
        timenow = time.strftime('%d/%m/%Y %H:%M:%S')
        print(f'Selecionando o segundo navegador...---{timenow}---')
        window2 = pygetwindow.getWindowsWithTitle(title) [1]
        window2.activate()
        window2.maximize()

        sleep(1)

        login()

        roteiro()

        sleep(3)
        print('Selecionando o primeiro navegador...')
        window1.activate()

        #===========Sistema Anti-AFK (2 navegadores)===========   
        sleep(1)
        afk = 0
        while afk < 5:
            time = datetime.datetime.now()
            timenow = time.strftime('%d/%m/%Y %H:%M:%S')
            print(f'Em 8 minutos o bot vai para o menu e volta (Anti-AFK) ---{timenow}---')

            sleep(480)
            voltar = bot.locateCenterOnScreen('./Imagens/back.png')
            moveTo(voltar)
            click()

            sleep(1)
            print('Retornando ao modo Amazon Survival...')
            amazon()
                
            sleep(1)
            print('Selecionando o segundo navegador...')
            window2.activate()

            time = datetime.datetime.now()
            timenow = time.strftime('%d/%m/%Y %H:%M:%S')
            print(f'Em 1 minuto o bot vai para o menu e volta (anti-afk) ---{timenow}---')

            sleep(60)
            voltar = bot.locateCenterOnScreen('./Imagens/back.png')
            moveTo(voltar)
            click()

            sleep(1)
            print('Retornando ao modo Amazon Survival...')
            amazon()
                
            sleep(1)
            print('Selecionando o primeiro navegador...')
            window1.activate()        
            afk += 1
            if afk < 5:
                print(f'Rodada {afk} de 5 concluída, até voltar a procurar os herois novamente!')
            else:
                print(f'Rodada {afk} de 5 concluída!')
            sleep(1)

    #=================Código para 3 navegadores (Se houver)=========================
    
    #======Identificando o segundo navegador======

    if nb == (3):
        time = datetime.datetime.now()
        timenow = time.strftime('%d/%m/%Y %H:%M:%S')
        print(f'Selecionando o segundo navegador...---{timenow}---')
        window2 = pygetwindow.getWindowsWithTitle(title) [1]
        window2.activate()
        window2.maximize()

        sleep(1)

        login()

        roteiro()
             
        #======Identificando o terceiro navegador======
        sleep(3)       
        time = datetime.datetime.now()
        timenow = time.strftime('%d/%m/%Y %H:%M:%S')
        print(f'Selecionando o terceiro navegador...---{timenow}---')
        window3 = pygetwindow.getWindowsWithTitle(title) [2]
        window3.activate()
        window3.maximize()

        sleep(1)

        login()

        roteiro()
          
        sleep(3)
        print('Selecionando o primeiro navegador...')
        window1.activate()

        #===========Sistema Anti-AFK (3 navegadores)===========   
        sleep(1)
        afk = 0
        while afk < 5:
            time = datetime.datetime.now()
            timenow = time.strftime('%d/%m/%Y %H:%M:%S')
            print(f'Em 8 minutos o bot vai para o menu e volta (Anti-AFK) ---{timenow}---')

            sleep(480)
            voltar = bot.locateCenterOnScreen('./Imagens/back.png')
            moveTo(voltar)
            click()

            sleep(1)
            print('Retornando ao modo Amazon Survival...')
            amazon()
                
            sleep(1)
            print('Selecionando o segundo navegador...')
            window2.activate()

            time = datetime.datetime.now()
            timenow = time.strftime('%d/%m/%Y %H:%M:%S')
            print(f'Em 1 minuto o bot vai para o menu e volta (anti-afk) ---{timenow}---')

            sleep(60)
            voltar = bot.locateCenterOnScreen('./Imagens/back.png')
            moveTo(voltar)
            click()

            sleep(1)
            print('Retornando ao modo Amazon Survival...')
            amazon()
                
            sleep(1)
            print('Selecionando o terceiro navegador...')
            window3.activate()        
            
            time = datetime.datetime.now()
            timenow = time.strftime('%d/%m/%Y %H:%M:%S')
            print(f'Em 1 minuto o bot vai para o menu e volta (anti-afk) ---{timenow}---')

            sleep(60)
            voltar = bot.locateCenterOnScreen('./Imagens/back.png')
            moveTo(voltar)
            click()

            sleep(1)
            print('Retornando ao modo Amazon Survival...')
            amazon()
                
            sleep(1)
            print('Selecionando o primeiro navegador...')
            window1.activate()        
            afk += 1
            if afk < 5:
                print(f'Rodada {afk} de 5 concluída, até voltar a procurar os herois novamente!')
            else:
                print(f'Rodada {afk} de 5 concluída!')
            sleep(1)
        
    #==================Saindo do Anti-AFK==================
    time = datetime.datetime.now()
    timenow = time.strftime('%d/%m/%Y %H:%M:%S')
    print(f'Fim do loop Anti-AFK...---{timenow}---')
    print('Em 30 segundos o BOT irá retornar para o inicio do Script e recomeçar...')
    sleep(30)
    print('Entrando no loop inicial...')
    voltar = bot.locateCenterOnScreen('./Imagens/back.png')
    moveTo(voltar)
    click()
    if nb == (2):
        sleep(1)
        window2.activate()
        sleep(2)
        bot.move(10,100)
        sleep(0.5)
        voltar = bot.locateCenterOnScreen('./Imagens/back.png')
        if voltar:
            moveTo(voltar)
            click()
        sleep(2)
        window1.activate()
        sleep(1)

    if nb == (3):
        sleep(1)
        window2.activate()
        sleep(2)
        bot.move(10,100)
        sleep(0.5)
        voltar = bot.locateCenterOnScreen('./Imagens/back.png')
        if voltar:
            moveTo(voltar)
            click()
        sleep(1)
        window3.activate()
        sleep(2)
        bot.move(10,100)
        sleep(0.5)
        voltar = bot.locateCenterOnScreen('./Imagens/back.png')
        if voltar:
            moveTo(voltar)
            click()
        sleep(2)
        window1.activate()
        sleep(1)

    #==================Sistema de Erro==================
    erro = bot.locateCenterOnScreen('./Imagens/error.png')
    ok = bot.locateCenterOnScreen('./Imagens/ok.png')
    connect = bot.locateCenterOnScreen('./Imagens/connect.png')

    print('Procurando alguma tela de erro...')
    if erro:
        print('Tela de erro identificada...')
        sleep(1)
        moveTo(ok)
        click()
        sleep(12)
        login()

    if connect:
        login()

    if nb == (2):
        sleep(1)
        window2.activate()
        sleep(1)
        erro = bot.locateCenterOnScreen('./Imagens/error.png')
        ok = bot.locateCenterOnScreen('./Imagens/ok.png')
        if erro:
            print('Tela de erro identificada...')
            sleep(1)
            moveTo(ok)
            click()
        sleep(1)
        window1.activate()
        sleep(1)

    if nb == (3):
        sleep(1)
        window2.activate()
        sleep(1)
        erro = bot.locateCenterOnScreen('./Imagens/error.png')
        ok = bot.locateCenterOnScreen('./Imagens/ok.png')
        if erro:
            print('Tela de erro identificada...')
            sleep(1)
            moveTo(ok)
            click()
        sleep(1)
        window3.activate()
        sleep(1)
        erro = bot.locateCenterOnScreen('./Imagens/error.png')
        ok = bot.locateCenterOnScreen('./Imagens/ok.png')
        if erro:
            print('Tela de erro identificada...')
            sleep(1)
            moveTo(ok)
            click()
        sleep(1)
        window1.activate()
        sleep(1)
    else:
        print('Nenhuma tela de erro...')
    print('Recomeçando o Script...')