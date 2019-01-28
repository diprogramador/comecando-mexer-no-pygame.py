git commit -m "primeiro commit" cando-mexer -no-pygame.py.git
import pygame

def main():         #cria janela
    #As definições dos objetos(variaveis)
    pygame.init()
    tela = pygame.display.set_mode([300, 300]) #VARIAVEL QUE MUDA TAMANHO DA JANELA
    pygame.display.set_caption("Bem vindo soldado!") #titulo da janela
    relogio = pygame.time.Clock()#VARIAVEL QUE A PAGINA ATUALIZA EM FLAMES
    cor_branca = (255,255,255)#VARIAVEL QUE DEFINE COR DE FUNDO DA JANELA
    cor_azul = (108, 194, 236)#VARIAVEL DE COR DO OBJETO
    cor_verde = (54, 182, 112)#VARIAVEL DE COR DO OBJETO
    cor_vermelha = (227, 57, 9)#VARIAVEL DE COR DO OBJETO
    cor_rosa = (253, 147, 226)#VARIAVEL DE COR DO OBJETO
    sup = pygame.Surface((200, 200))#define o tamanho do objeto
    sup.fill(cor_azul)#define a cor do objeto (---+--- OBJETO 1 ---+---)

    sup2 = pygame.Surface((100, 100))#define o tamanho do objeto
    sup2.fill(cor_verde)#define a cor do objeto   (---+--- OBJETO 2 ---+---)

    ret = pygame.Rect(10, 10, 45, 45)#VARIAVEL RETÂNGULO
    ret2 = pygame.Rect(80, 100, 100, 60)#VARIAVEL RETÂNGULO

    pygame.font.init() #CHAVE PARA INICIAR AS FONTES

    font_padrao = pygame.font.get_default_font() #variaveis de textos que aparecerão quando colidir objetos
    fonte_perdeu = pygame.font.SysFont(font_padrao,45)
    fonte_ganhou = pygame.font.SysFont(font_padrao,30)

    audio_explosao = pygame.mixer.Sound('c.ogg')#VARIAVEL DO SOM DA EXPLOSAO
    
    
    #---------+-----------------+-------------+--------------------+------#
    
    sair = False    #VARIAVEL QUE FAZ COM QUE O BOTÃO X DA JANELA FECHE A JANELA

    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #MODULO QUE FAZ O X DA JANELA FECHA-LA
                sair = True
                
                
            #if event.type == pygame.MOUSEBUTTONDOWN:        #O MOUSE CONTROLA  OBJETO
                #ret = ret.move(10, 10)                      #DEFINE DIREÇÃO QUE O OBJETO IRA SE MOVER
                

            #if event.type == pygame.MOUSEMOTION:         #SO EM MECHER COM O MOUSE, MECHE O OBJETO
                #ret = ret.move(-10, -10)                 #DEFINE EM X & Y A DIREÇÃO

            if event.type == pygame.KEYDOWN:#SOLICITA CLICAR UMA TECLA
                if event.key == pygame.K_LEFT: #SETA PRA ESQUERDA (10 PIXEL)
                    ret.move_ip(-10, 0)#SERVE PRA MOVIMENTAR OBJETO, BASEADO NA AÇÃO DO TECLADO

                if event.key == pygame.K_RIGHT:#SETA PRA DIREITA (10 PIXEL)
                    ret.move_ip(10, 0)#SERVE PRA MOVIMENTAR OBJETO, BASEADO NA AÇÃO DO TECLADO

                if event.key == pygame.K_UP:#SETA PRA CIMA (10 PIXEL)
                    ret.move_ip(0, -10)#SERVE PRA MOVIMENTAR OBJETO, BASEADO NA AÇÃO DO TECLADO

                if event.key == pygame.K_DOWN:#SETA PRA BAIXO (10 PIXEL)
                    ret.move_ip(0, 10)#SERVE PRA MOVIMENTAR OBJETO, BASEADO NA AÇÃO DO TECLADO



                    


                
        relogio.tick(350)#JANELA ATUALIZA FLAMES POR SEGUNDOS(Maior o valor, o objeto segue mouse mais rapido)
        tela.fill(cor_branca)#COR DE FUNDO DA JANELA
        tela.blit(sup, [50, 50])#Define a distancia X & Y do objeto
        tela.blit(sup2, [250, 50])#Define a distancia X & Y do objeto
        tela.blit(sup2, [250, 150])#Define a distancia X & Y do objeto

        (xant, yant) = (ret.left, ret.top)#COLIZÃO COM OUTRO OBJETO
        (ret.left, ret.top) = pygame.mouse.get_pos()#OBJETO MECHE JUNTO COM O MOUSE
        ret.left -= ret.width/2#CENTRALIZA O MOUSE NO OBJETO
        ret.top -= ret.height/2#CENTRALIZA O MOUSE NO OBJETO
        if ret.colliderect(ret2):#COLISÃO COM OUTRO OBJETO
            text = fonte_perdeu.render('COLIDIU', 1, (255,255,255))
            audio_explosao.play()
            audio_explosao.set_volume(0.10)#VOLUME DO SOOM DA EXPLOSÃO
            tela.blit(text, (150, 150))#TEXTO APARECE NA ALTURA DECLARADA QUANDO COLIDIR NOS OBJETOS
            (ret.left, ret.top) = (xant, yant)#COLIZÃO COM OUTRO OBJETO
            
        
        pygame.draw.rect(tela, cor_vermelha, ret)#DEFINE COR E LOCAL DO OBJETO NA TELA
        pygame.draw.rect(tela, cor_rosa, ret2)#DEFINE COR E LOCAL DO OBJETO NA TELA
        pygame.display.update()#atualiza a janela
        
    pygame.quit() 


main()
    
    
