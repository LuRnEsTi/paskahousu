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

def draw_transparent_circle(surface):
    circle_radius = 20
    alpha=128
    circle_color = (0, 0, 0, alpha)  # RGBA, where 128 is the alpha value for transparency
    circle_center = (screen_width // 2, screen_height // 2.3)
    pygame.draw.circle(surface, circle_color, circle_center, circle_radius)

def is_point_inside_circle(point, circle_center, circle_radius):
    x, y = point
    center_x, center_y = circle_center
    distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
    return distance <= circle_radius, circle_center


def display_kortit(card_ids, kortti_alueet, sprite_sheet_kuva, screen, cursor_position, pressed_buttons,surface):
    global dragging_state
    if not card_ids:
        print("iha tyhjä")
        return

    circle_radius = 20
    circle_center = (screen_width // 2, screen_height // 2.3)

    korttien_lkm = len(card_ids)
    kokonaisleveys = (korttien_lkm * (1920 / 13) + (korttien_lkm - 1) * 15)
    positio = (1280 - kokonaisleveys) / 2
    card_width = kortti_alueet[card_ids[0]].width
    card_height = kortti_alueet[card_ids[0]].height

    for i, card_id in enumerate(card_ids):
        n=0
        x_position = positio + i * (card_width +15)
        y_position = 720 - 1150 /5
        card_rect = pygame.Rect(x_position, y_position, card_width, card_height)
        dragging_state = True
        # Check if cursor is over the card
        if not dragging_state or card_rect.collidepoint(cursor_position) and pressed_buttons[0]:
            if hasattr(display_kortit, 'dragging_card') and display_kortit.dragging_card == card_id:
                # Update the position of the card while the mouse button is held down
                x_position, y_position = cursor_position[0] - card_width / 2, cursor_position[1] - card_height / 2
                display_kortit.dragging_card_position = (x_position, y_position)
                #print("Dragging Card Position:", x_position, y_position)
                #print(card_id)
                #print(card_ids)
                #print(i)
                dragging_state = False

            else:
                display_kortit.dragging_card = card_id
                display_kortit.dragging_card_position = (x_position, y_position)
        elif hasattr(display_kortit, 'dragging_card') and display_kortit.dragging_card == card_id:
            x_position, y_position = cursor_position[0] - card_width / 2, cursor_position[1] - card_height / 2
            display_kortit.dragging_card_position = (x_position, y_position)
            #(x_position, y_position)=(circle_center)
            #print("Dragging Card Position:", x_position, y_position)
            #print(card_id)
            #print(card_ids)
            #print(i)
            if (
                circle_center[0] <= x_position + card_width <= circle_center[0] + circle_radius and
                circle_center[1] <= y_position + card_height <= circle_center[1] + circle_radius
                ):
                    n=n+1
                    print("Top-left corner of the card is inside the circle!",card_id,n)
        display_kortti(card_id, kortti_alueet, sprite_sheet_kuva, screen, (x_position, y_position))
        draw_transparent_circle(surface)         
    
    # Reset dragging state on mouse button release
    if not pressed_buttons[0] and hasattr(display_kortit, 'dragging_card'):
        display_kortit.dragging_card = None
        dragging_state = False

def display_kortti(kortin_id, kortti_alueet, sprite_sheet_kuva, screen, position):
    alue = kortti_alueet.get(kortin_id)
    if alue:
        kortin_kuva = sprite_sheet_kuva.subsurface(alue)
        screen.blit(kortin_kuva, position)
    else:
        print("ei löytynyynyynynyn")