import pygame

ruutu_leveys= 1280
ruutu_korkeus= 720
korttien_maara=5
leveys=174
korkeus=267
vali=15
kokonaisleveys=(korttien_maara*leveys+(korttien_maara-1)*vali)
paikka=(ruutu_leveys-kokonaisleveys)/2
rectangles=[]

def kortti(screen):

    for i in range (korttien_maara):
        rect = pygame.Rect((paikka+i * (leveys + vali), ruutu_korkeus - korkeus), (leveys, korkeus))
        rectangles.append(rect)
    for rect in rectangles:
        pygame.draw.rect(screen, (255, 255, 255), rect)
    #return korttien_maara, leveys, korkeus, vali, kokonaisleveys