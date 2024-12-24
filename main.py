import pygame#импортировали БИБЛИОТЕКУ с книжками
import sys#импортировали модуль суслика для работы с компухтром
import random
a = 300

b = 400

c = 300

d =400

sistemskin = random.randint(1,2)
pygame.init()

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

start_x = 400
start_y = 500
finish_x = 1191
finish_y = 566

serwer = pygame.image.load("o_o/serwer.png")

herobrine = pygame.image.load("o_o/herobrin_model.png")

bisnes_kripi = pygame.image.load("o_o/bisnes_kripi.png")
beg_v_levo = False
beg_v_verh = False
beg_v_pravo =False
beg_v_vniz = False
logicheskay_peremenay = True
while logicheskay_peremenay != False:
    # 1(4 отступа) отвечают за действие в игровом цикле
    for event in pygame.event.get():
        print(event)
        #2(8 пультов от ядерки)отвечают за что-то неведомое(ой за действия мышкой,кошкой и клавиатурой)
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
        if mouse_batonchik [0] :#если клик левой кнопкой то это ничего туцтуцтуцтуцтуц
            #print(event.pos)
            pos_x = event.pos[0]
            pos_y = event.pos[1]
            if pos_x >= start_x and pos_x <= finish_x and pos_y >= start_y and pos_y <= finish_y:#огромная махина отслеживания тыка по кнопке на координтах

                ocherednoe_nechto = 2#прячем меню номер 101 (ой, 1)

        if mouse_batonchik[0]:
            pos_x = event.pos[0]
            pos_y = event.pos[1]
            if pos_x >= 966 and pos_x <= 1343 and pos_y >= 655 and pos_y <= 721:
                print("хомяяяяяяяяяяяяяяяяяяяяк")
                logicheskay_peremenay = False
        #print("крипер? нет нажали мышкой",mouse_batonchik,exitmouse_batonchik)


    screen.fill(ne_razdrazhaussiy)#пролили краску на экран    :(
    screen.blit(scorlupa, (0, 0))
    if ocherednoe_nechto == 1:
        screen.blit(soloplayay,(400,500))#размЫщаем Ызображение на Ыкране
        screen.blit(exit_batonchik, (960, 650))
        #nazad = pygame.image.load("o_o/nazad.png")
        #screen.blit(nazad, (4, 809))
        screen.blit(options,(699,809))
        screen.blit(serwer,(400,400))
    if ocherednoe_nechto == 2:
        if beg_v_levo == True:
            a -= 1
        if beg_v_verh == True:
            b-=1
        if beg_v_pravo == True:
            a += 1
        if beg_v_vniz == True:
            b+=1
        if sistemskin == 1:
            screen.blit(herobrine,(a,b))
        if sistemskin == 2:
            screen.blit(bisnes_kripi,(a,b))
    pygame.display.flip()#обновляем экран(FPS FPS FPS)