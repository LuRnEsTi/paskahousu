import pygame
from sprite_sheet import load_sprite_sheet, maarita_alueet, display_kortit,display_kortti
#from kortti import korttien_maara, leveys, korkeus, vali, kokonaisleveys, paikka
from kortti import kortti
from logiikka import deal_hands, create_pakka, shuffle_pakka, pakan_vahennys,pakan_lisays


##pygame setuppi
pygame.init()
ruutu_leveys= 1280
ruutu_korkeus= 720
screen = pygame.display.set_mode((ruutu_leveys,ruutu_korkeus))
running = True
sprite_sheet_kuva=load_sprite_sheet()


taustakuva = pygame.image.load("casino_texture.jpg")
taustakuva_rect = taustakuva.get_rect()

    



unshuffled_pakka = create_pakka()
shuffle_pakka(unshuffled_pakka)

kasi1, loput_kortit,_ = deal_hands(unshuffled_pakka)

#print("Pelaaja 1:", kasi1)
#print("Pelaaja 2:", kasi2)g/1
#print("Loppu pakka: ",loput_kortit)
print("Pakassa olevien korttien määrä",len(loput_kortit))
print("ensimmäinen kortti on: ",kasi1)


kortti_alueet = maarita_alueet()
card_ids_to_display = kasi1


poistettavat_kortit = kasi1[:1]
running = True
while running:
  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(taustakuva, taustakuva_rect) 
    cursor_position = pygame.mouse.get_pos()
    pressed_buttons = pygame.mouse.get_pressed()

    card_ids_to_display = kasi1[:5]
    
    pakan_vahennys(kasi1,poistettavat_kortit)
    pakan_lisays(kasi1,loput_kortit)


    display_kortit(card_ids_to_display, kortti_alueet, sprite_sheet_kuva, screen, cursor_position, pressed_buttons)
    #display_kortti(card_ids_to_display, kortti_alueet, sprite_sheet_kuva, screen, (5,5))
    



    

    pygame.display.update()

 
print(unshuffled_pakka)
pygame.quit()
