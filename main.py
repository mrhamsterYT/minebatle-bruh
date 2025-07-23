import pygame#импортировали БИБЛИОТЕКУ с книжками
import sys#импортировали модуль суслика для работы с компухтром
import random
pygame.init()
poroh_dly_oruzhiay = 0

a = 700

b = 650

c = 750

d = 600

e = 970

f = 600




sistemskin = 1

two_b_two_t = random.randint(1,3)
if two_b_two_t == 1:
    two = 100
if two_b_two_t == 2:
    two = 10
if two_b_two_t == 3:
    two = 12.5

i_snowa = 0

aboba = pygame.display.Info()
print(aboba)
screen = pygame.display.set_mode((1536, 864))

pygame.display.set_caption("minebatle")#назвали что-то без названия(экран)


ocherednoe_nechto = 1#нелогическая переменая отвечает за видимость менюшек - scp0192


iconka = pygame.image.load("o_o/nyshka.png")#загрузили кортинку
pygame.display.set_icon(iconka)#установили иконку, иконка стала иконкой

scorlupa = pygame.image.load("o_o/groundback.PNG.png").convert()
scorlupa = pygame.transform.scale(scorlupa,(1536, 864))
ne_razdrazhaussiy = (255,255,230)

exit_batonchik = pygame.image.load("o_o/exit.png")
exits_x = 966
exits_y = 721
exitf_x = 1343
exitf_y = 655

options = pygame.image.load("o_o/options.png")

soloplayay = pygame.image.load("o_o/soloplayay.png")

pistolet = pygame.image.load("o_o/pistolet.png")

zombi = pygame.image.load("o_o/zombu.png")
zombi = pygame.transform.scale(zombi,(146,181))

start_x = 400
start_y = 500
finish_x = 1191
finish_y = 566

serwer = pygame.image.load("o_o/serwer.png")

herobrine = pygame.image.load("o_o/herobrin_model.png")

bisnes_kripi = pygame.image.load("o_o/bisnes_kripi_szadi.png")

bisnes_kripi = pygame.transform.scale(bisnes_kripi,(146, 181))

mr_hamster = pygame.image.load("o_o/mr_hamster_back.png")

mr_hamster = pygame.transform.scale(mr_hamster,(146, 181))

girl = pygame.image.load("o_o/girl.png")

girl = pygame.transform.scale(girl,(146, 181))

herobrine = pygame.transform.scale(herobrine,(146, 181))


zombinet = pygame.Rect(400, 200, 146, 181)

skin = pygame.Rect(50, 800, 50, 50)

skin2 = pygame.Rect(200, 800, 50, 50)

woda1 = pygame.Rect(0, 0, 300, 864)#создали левую воду - rect objekt

woda2 = pygame.Rect(1236, 0, 300, 864)






beg_v_levo = False
beg_v_verh = False
beg_v_pravo =False
beg_v_vniz = False
logicheskay_peremenay = True
while logicheskay_peremenay != False:
    # 1(4 отступа) отвечают за действия мышкой и клавиатурой в игровом цикле
    for event in pygame.event.get():
        #print(event)

        if event.type == pygame.QUIT:
            logicheskay_peremenay = False
        if event.type == pygame.KEYDOWN:#отслеживаем тык по кнопке
            if event.key == 97:#a
                beg_v_levo = True
            if event.key == 119:#w
                beg_v_verh = True
            if event.key == 100:#d
                beg_v_pravo = True
            if event.key == 115:#s
                beg_v_vniz = True

        if event.type == pygame.KEYUP:
            if event.key == 97:
                beg_v_levo = False
            if event.key == 119:
                beg_v_verh = False
            if event.key == 100:
                beg_v_pravo = False
            if event.key == 115:
                beg_v_vniz = False

        mouse_batonchik = pygame.mouse.get_pressed()#этот метод оследит и отслеживает нажатие мышки
        if mouse_batonchik[0] and ocherednoe_nechto == 1:#если клик левой кнопкой то это ничего туцтуцтуцтуцтуц
            #print(event.pos)
            if skin2.collidepoint(event.pos):
                sistemskin += 1
                if sistemskin == 5:
                    sistemskin = 1
            if skin.collidepoint(event.pos):
                sistemskin -= 1
                if sistemskin == 0:
                    sistemskin = 4

            pos_x = event.pos[0]
            pos_y = event.pos[1]
            if pos_x >= start_x and pos_x <= finish_x and pos_y >= start_y and pos_y <= finish_y:#огромная махина отслеживания тыка по кнопке на координтах

                ocherednoe_nechto = 2#прячем меню номер 101 (ой, 1)


            if pos_x >= 966 and pos_x <= 1343 and pos_y >= 655 and pos_y <= 721:
                print("хомяяяяяяяяяяяяяяяяяяяяк")
                logicheskay_peremenay = False
    #2 логические операции в игре
        #print("крипер? нет нажали мышкой",mouse_batonchik,exitmouse_batonchik)

    if ocherednoe_nechto == 2:
        bullet = pygame.Rect(c, d, 10, 20)  # обьект прям(угольник забрали :(  ) x,y,w,h

        dimon = pygame.Rect(a, b, 146, 181)

        if beg_v_levo == True:
            a -= 0.65
            c -= 0.65
            e -= 0.65

            if woda1.colliderect(dimon):
                beg_v_levo = False
                #print("print(print())")

        if beg_v_pravo == True:
            a += 0.65
            c += 0.65
            e += 0.65

            if woda2.colliderect(dimon):
                beg_v_pravo = False

        if zombinet.colliderect(bullet):
            i_snowa = 1
        if d != 100:
            d -= two
        if d == 100:
            d += 500

    #3 отбражение элементов на экране
    screen.fill(ne_razdrazhaussiy)#пролили краску на экран    :(
    if ocherednoe_nechto == 1:
        screen.blit(scorlupa, (0, 0))
        screen.blit(soloplayay,(400,500))#размЫщаем Ызображение на Ыкране
        screen.blit(exit_batonchik, (960, 650))
        pygame.draw.rect(screen, (0, 191, 255), skin)
        pygame.draw.rect(screen, (0, 191, 255), skin2)
        #nazad = pygame.image.load("o_o/nazad.png")
        #screen.blit(nazad, (4, 809))
        screen.blit(options,(399,659))
        screen.blit(serwer,(400,400))
    if ocherednoe_nechto == 2:
        if sistemskin == 1:
            screen.blit(herobrine,(a,b))
            screen.blit(herobrine, (0, 0))
        if sistemskin == 2:
            screen.blit(bisnes_kripi,(a,b))
            screen.blit(bisnes_kripi, (0, 0))
        if sistemskin == 3:
            screen.blit(mr_hamster, (a, b))
        if sistemskin == 4:
            screen.blit(girl, (a, b))
        #screen.blit(pistolet, (e, f))

        pygame.draw.rect(screen,(201,148,42),bullet)#разместили в центр центрального центра экрана
        pygame.draw.rect(screen, (0, 191, 255),woda1)
        if i_snowa == 0:
            screen.blit(zombi, (400, 200))
        pygame.draw.rect(screen, (0, 191, 255),woda2)
    pygame.display.flip()#обновляем экран(FPS FPS FPS)