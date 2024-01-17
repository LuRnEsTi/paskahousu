import pygame

screen_width, screen_height = (1280, 720)

def load_sprite_sheet():
    sprite_sheet_kuva = pygame.image.load("kortti_sheet.png")
    print("kuva ladattu")
    return sprite_sheet_kuva

def maarita_alueet():
    kortin_leveys_kuvassa = 1920 / 13
    kortin_korkeus_kuvassa = 1150 / 5

    kortti_alueet = {}
    suits = ['risti', 'ruutu', 'hertta', 'pata']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    for suit_index, suit in enumerate(suits):
        for rank_index, rank in enumerate(ranks):
            kortin_id = f'{suit}_{rank}'
            x = rank_index * kortin_leveys_kuvassa
            y = suit_index * kortin_korkeus_kuvassa
            kortti_alueet[kortin_id] = pygame.Rect(x, y, kortin_leveys_kuvassa, kortin_korkeus_kuvassa)

    return kortti_alueet

def draw_transparent_circle(screen, update_circle_radius,circle_radius):

    if update_circle_radius==True:
        circle_radius = 80
        print(circle_radius)
    elif update_circle_radius == False:
        circle_radius = 50

    circle_center = (screen_width // 2, screen_height // 2.3)
    alpha = 50
    circle_color = (0, 0, 0, alpha)
    pygame.draw.circle(screen, circle_color, circle_center, circle_radius)

    return circle_center, circle_radius


update_circle_radius = None
circle_radius=50


def is_point_inside_circle(card_rect, circle_center, circle_radius):
    return (
        circle_center[0] - circle_radius < card_rect.left
        and circle_center[0] + circle_radius > card_rect.right
        and circle_center[1] - circle_radius < card_rect.top
        and circle_center[1] + circle_radius > card_rect.bottom
    )

def display_kortit(card_ids, kortti_alueet, sprite_sheet_kuva, screen, cursor_position, pressed_buttons,surface):
    global circle_radius
    global update_circle_radius

    if not card_ids:
        print("iha tyhjä")
        return

    korttien_lkm = len(card_ids)
    kokonaisleveys = (korttien_lkm * (1920 / 13) + (korttien_lkm - 1) * 15)
    positio = (1280 - kokonaisleveys) / 2
    card_width = kortti_alueet[card_ids[0]].width
    card_height = kortti_alueet[card_ids[0]].height

    # Clear the screen with a white background
    #screen.fill((255, 255, 255))

    
    draw_transparent_circle(surface, update_circle_radius,circle_radius)
    screen.blit(surface,(0,0))
    

    #print("tapahtuu päivitys")
    for i, card_id in enumerate(card_ids):
        circle_center = (screen_width // 2, screen_height // 2.3)
        x_position = positio + i * (card_width + 15)
        y_position = 720 - 1150 / 5
        card_rect = pygame.Rect(x_position, y_position, card_width, card_height)

        if card_rect.collidepoint(cursor_position) and pressed_buttons[0]:
            if hasattr(display_kortit, 'dragging_card') and display_kortit.dragging_card == card_id:
                x_position, y_position = cursor_position[0] - card_width / 2, cursor_position[1] - card_height / 2
                display_kortit.dragging_card_position = (x_position, y_position)
                update_circle_radius = False

            else:
                display_kortit.dragging_card = card_id
                display_kortit.dragging_card_position = (x_position, y_position)
        elif hasattr(display_kortit, 'dragging_card') and display_kortit.dragging_card == card_id:
            x_position, y_position = cursor_position[0] - card_width / 2, cursor_position[1] - card_height / 2
            display_kortit.dragging_card_position = (x_position, y_position)
            circle_center = (screen_width // 2, screen_height // 2.3)
            distance_to_center = ((x_position - circle_center[0]) ** 2 + (y_position - circle_center[1]) ** 2) ** 0.5

            if distance_to_center <= circle_radius:
                print("Top-left corner of the card is inside the circle!", card_id)
                update_circle_radius = True
            else:
                update_circle_radius=False
  
        #print("Card ID:", card_id, "Update Circle Radius:", update_circle_radius, "Circle Radius:", circle_radius)

        display_kortti(card_id, kortti_alueet, sprite_sheet_kuva, screen, (x_position, y_position))
        

    #pygame.display.flip()

    if not pressed_buttons[0] and hasattr(display_kortit, 'dragging_card'):
        display_kortit.dragging_card = None
        update_circle_radius = False
    
    
   



    
    

def display_kortti(kortin_id, kortti_alueet, sprite_sheet_kuva, screen, position):
    alue = kortti_alueet.get(kortin_id)
    if alue:
        kortin_kuva = sprite_sheet_kuva.subsurface(alue)
        screen.blit(kortin_kuva, position)
    else:
        print("ei löytynyynyynynyn")
