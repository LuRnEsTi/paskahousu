import pygame
from sprite_sheet import load_sprite_sheet, maarita_alueet, display_kortit,draw_transparent_circle, update_circle_radius
from logiikka import deal_hands, create_pakka, shuffle_pakka, pakan_vahennys, pakan_lisays, kortteja_kadessa
# pygame setuppi
pygame.init()
ruutu_leveys = 1280
ruutu_korkeus = 720
screen = pygame.display.set_mode((ruutu_leveys, ruutu_korkeus), pygame.SRCALPHA)
surface=pygame.Surface((ruutu_leveys,ruutu_korkeus) ).convert_alpha()
running = True
sprite_sheet_kuva = load_sprite_sheet()
screen.set_alpha(None)
fps=60
timer=pygame.time.Clock()

taustakuva = pygame.image.load("casino_texture.jpg")
taustakuva_rect = taustakuva.get_rect()

unshuffled_pakka = create_pakka()
shuffle_pakka(unshuffled_pakka)

kasi1, loput_kortit = deal_hands(unshuffled_pakka)

kortti_alueet = maarita_alueet()
card_ids_to_display = kasi1

poistettavat_kortit = kasi1[:0]



#dragging_state=True #Variable to track dragging state
while running:
    timer.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    cursor_position = pygame.mouse.get_pos()
    pressed_buttons = pygame.mouse.get_pressed()
    
  
    surface.fill((0, 0, 0, 0))  
    screen.blit(taustakuva, taustakuva_rect)

    
    

    card_ids_to_display = kasi1[:kortteja_kadessa]
    display_kortit(card_ids_to_display, kortti_alueet, sprite_sheet_kuva, screen, cursor_position, pressed_buttons,surface)



    pakan_lisays(kasi1, loput_kortit)
    pakan_vahennys(kasi1, poistettavat_kortit)



    


  
    

 
    pygame.display.flip()

pygame.quit()

