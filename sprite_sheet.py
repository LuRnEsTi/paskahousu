import pygame
from logiikka import deal_hands, create_pakka

pygame.init()
screen_width, screen_height = (1280, 720)
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SRCALPHA)

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

def draw_hovering_circle(screen, cursor_position, hovering_circle_radius,transparency=220):
    color=(220,220,220,transparency)
    pygame.draw.circle(screen,color, cursor_position, hovering_circle_radius)

def is_card_over_circle(card_rect, hovering_circle_position, hovering_circle_radius):
    circle_center = (hovering_circle_position[0] + hovering_circle_radius, hovering_circle_position[1] + hovering_circle_radius)
    return pygame.Rect(circle_center[0] - hovering_circle_radius, circle_center[1] - hovering_circle_radius, hovering_circle_radius * 2, hovering_circle_radius * 2).colliderect(card_rect)

# Define the initial values for hovering circle position and radius
hovering_circle_position = (screen.get_width() // 2, screen.get_height() // 2)
hovering_circle_radius = 50



def display_kortit(card_ids, kortti_alueet, sprite_sheet_kuva, screen, cursor_position, pressed_buttons):
    if not card_ids:
        print("iha tyhjä")
        return

    kortit_kadessa_list = list(card_ids)
    kortit_copy = kortit_kadessa_list.copy()
    korttien_lkm = len(card_ids)
    kokonaisleveys = (korttien_lkm * (1920 / 13) + (korttien_lkm - 1) * 15)
    positio = (1280 - kokonaisleveys) / 2
    card_width = kortti_alueet[card_ids[0]].width
    card_height = kortti_alueet[card_ids[0]].height

    for i, card_id in enumerate(card_ids):
        x_position = positio + i * (card_width +(1/(korttien_lkm*100**3)))
        y_position = 720 - 1150 /5
        card_rect = pygame.Rect(x_position, y_position, card_width, card_height)

        # Check if cursor is over the card
        if card_rect.collidepoint(cursor_position) and pressed_buttons[0]:
            if hasattr(display_kortit, 'dragging_card') and display_kortit.dragging_card == card_id:
                # Update the position of the card while the mouse button is held down
                x_position, y_position = cursor_position[0] - card_width / 2, cursor_position[1] - card_height / 2
                display_kortit.dragging_card_position = (x_position, y_position)
            if is_card_over_circle(card_rect, hovering_circle_position, hovering_circle_radius):
                # Do something when the card is dragged over the hovering circle
                print("päällä")
                pass
            else:
                display_kortit.dragging_card = card_id
                display_kortit.dragging_card_position = (x_position, y_position)
        elif hasattr(display_kortit, 'dragging_card') and display_kortit.dragging_card == card_id:
            x_position, y_position = cursor_position[0] - card_width / 2, cursor_position[1] - card_height / 2
            display_kortit.dragging_card_position = (x_position, y_position)
        
        display_kortti(card_id, kortti_alueet, sprite_sheet_kuva, screen, (x_position, y_position))
        draw_hovering_circle(screen, hovering_circle_position, hovering_circle_radius,transparency=220)
    
    # Reset dragging state on mouse button release
    if not pressed_buttons[0] and hasattr(display_kortit, 'dragging_card'):
        display_kortit.dragging_card = None

def display_kortti(kortin_id, kortti_alueet, sprite_sheet_kuva, screen, position):
    alue = kortti_alueet.get(kortin_id)
    if alue:
        kortin_kuva = sprite_sheet_kuva.subsurface(alue)
        screen.blit(kortin_kuva, position)
    else:
        print("ei löytynyynyynynyn")