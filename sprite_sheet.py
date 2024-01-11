import pygame

pygame.init()

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

kortti_alueet = maarita_alueet()

kokonaisleveys = (5 * (1920 / 13) + (5 - 1) * 15)
positio = (1280 - kokonaisleveys) / 2

def display_kortit(card_ids, kortti_alueet, sprite_sheet_kuva, screen, cursor_position, pressed_buttons):
    card_width = kortti_alueet[card_ids[0]].width  # Assuming all cards have the same width
    card_height = kortti_alueet[card_ids[0]].height  # Assuming all cards have the same height

    for i, card_id in enumerate(card_ids):
        x_position = positio + i * (card_width + 15)
        y_position = 720 - 1150 / 5
        card_rect = pygame.Rect(x_position, y_position, card_width, card_height)

        # Check if cursor is over the card
        if card_rect.collidepoint(cursor_position) and pressed_buttons[0]:  # M1 pressed
            if hasattr(display_kortit, 'dragging_card') and display_kortit.dragging_card == card_id:
                # Update the position of the card while mouse button is held down
                x_position, y_position = cursor_position[0] - card_width / 2, cursor_position[1] - card_height / 2
                display_kortit.dragging_card_position = (x_position, y_position)
            else:
                display_kortit.dragging_card = card_id
                display_kortit.dragging_card_position = (x_position, y_position)
        elif hasattr(display_kortit, 'dragging_card') and display_kortit.dragging_card == card_id:
            x_position, y_position = cursor_position[0] - card_width / 2, cursor_position[1] - card_height / 2
            display_kortit.dragging_card_position = (x_position, y_position)

        display_kortti(card_id, kortti_alueet, sprite_sheet_kuva, screen, (x_position, y_position))

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