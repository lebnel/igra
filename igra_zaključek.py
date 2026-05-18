import pygame, random, os

mapa_slike = os.path.dirname(os.path.abspath(__file__))

def nalaganje_slik(ime_slike):
    pot_do_slike = os.path.join(mapa_slike, ime_slike)
    return pygame.image.load(pot_do_slike).convert_alpha()

def klik(x, y, vrstni_red, smer):
    if tipka[pygame.K_RIGHT]:
        vrstni_red += 1
        smer = "desno"
    if tipka[pygame.K_LEFT]:
        vrstni_red += 1
        smer ="levo"
    if tipka[pygame.K_UP]:
        vrstni_red += 1
    if tipka[pygame.K_DOWN]:
        vrstni_red += 1
    return x, y , vrstni_red, smer

def skatla_premikanje(skatle, zavitki):
    if tipka[pygame.K_RIGHT]:
        for i in range(len(skatle)):
            skatle[i][0] -= 3
        for i in range(len(zavitki)):
            zavitki[i][0] -= 3
    if tipka[pygame.K_LEFT]:
        for i in range(len(skatle)) :
            skatle[i][0] += 3
        for i in range(len(zavitki)):
            zavitki[i][0] += 3
    if tipka[pygame.K_UP]:
        for i in range(len(skatle)):
            skatle[i][1] += 3
        for i in range(len(zavitki)):
            zavitki[i][1] += 3
    if tipka[pygame.K_DOWN] :
        for i in range(len(skatle)):
            skatle[i][1] -= 3
        for i in range(len(zavitki)):
            zavitki[i][1] -= 3

pygame.init()

# zaslon:
zaslon = pygame.display.set_mode((900, 700))

# ura:
ura = pygame.time.Clock()

# slike (liki):

# muca: 
slika1 = nalaganje_slik("muca_stoji.png")
slika2 = nalaganje_slik("muca_sklanja1.png")
slika3 = nalaganje_slik("muca_sklanja2.png")
slika4 = nalaganje_slik("muca_sklanja3.png")

slika1 = pygame.transform.scale_by(slika1, 0.25)
slika2 = pygame.transform.scale_by(slika2, 0.25)
slika3 = pygame.transform.scale_by(slika3, 0.25)
slika4 = pygame.transform.scale_by(slika4, 0.25)

slik1 = nalaganje_slik("muca2_stoji.png")
slik2 = nalaganje_slik("muca2_sklanja1.png")
slik3 = nalaganje_slik("muca2_sklanja2.png")

slik1 = pygame.transform.scale_by(slik1, 0.25)
slik2 = pygame.transform.scale_by(slik2, 0.25)
slik3 = pygame.transform.scale_by(slik3, 0.25)


#ozadje:
ozadje = nalaganje_slik("parket.jpg")
ozadje = pygame.transform.scale(ozadje, (900, 700))

#tipke:
tipka_O = nalaganje_slik("tipka_o.png")
tipka_X = nalaganje_slik("tipka_X.png")

#gumbi:
gumb_play = nalaganje_slik("play_gumb.png")
gumb_play = pygame.transform.scale_by(gumb_play, 0.25)
gumb_kvadrat = gumb_play.get_rect(topleft= (570, 240))
tacka = nalaganje_slik("tacka.png")
tacka = pygame.transform.scale_by(tacka, 0.5)
tacka_kvadrat = tacka.get_rect(topleft= (670, 400))
puscica_levo = nalaganje_slik("puščica2.png")
puscica_desno = nalaganje_slik("puščica.png")
puscica_levo = pygame.transform.scale_by(puscica_levo, 0.5)
puscica_desno = pygame.transform.scale_by(puscica_desno, 0.5)
puscica_kvadrat = puscica_levo.get_rect(topleft= (100, 300))
puscica2_kvadrat = puscica_desno.get_rect(topleft= (500, 300))


#napis:
napis = nalaganje_slik("mucke_napis.png")
napis = pygame.transform.scale_by(napis, 2.5)

#muca spi:
animacija_spanja = [
    nalaganje_slik("muca_spi1.png"),
    nalaganje_slik("muca_spi2.png"),
    nalaganje_slik("muca_spi3.png"),
    nalaganje_slik("muca_spi2.png"),
    nalaganje_slik("muca_spi1.png"),
]

#skatle:
skatla = nalaganje_slik("skatla2.png")
skatla = pygame.transform.scale_by(skatla, 0.5)

skatle = [
    # 1 vrsta
    [130, -195], [250, -195], [367, -195], [480, -195], [590, -195], [699, -195], [810, -195], [925, -195],  [1040, -195], [1155, -195],
    #2 vrsta
    [130, -65], [1155, -65],
    #3 vrsta
    [10, 70], [130, 70], [367, 70], [480, 70], [590, 70], [699, 70], [810, 70], [925, 70], [1155, 70],
    #4 vrsta
    [-350, 205], [-230, 205], [-107, 205] ,[480, 205], [1155, 205], 
    #5 vrsta
    [-350, 340], [-107, 340], [130, 340],  [480, 340], [699, 340], [810, 340], [925, 340],  [1040, 340], [1155, 340],
    #6 vrsta
    [-350, 475], [-107, 475], [10, 475], [130, 475], [250, 475], [480, 475], [1155, 475],
    #7 vrsta
    [-350, 605], [250, 605], [367, 605], [480, 605], [589, 605], [699, 605], [810, 605], [925, 605], [1155, 605],
    # 8 naloga
    [-350, 735], [-230, 735], [-107, 735], [10, 735], [1155, 735],
    #9 vrsta
    [130, 865], [250, 865], [367, 865], [480, 865], [590, 865], [699, 865], [810, 865], [925, 865],  [1040, 865], [1155, 865],   

]

skatle_zacetek = [s.copy() for s in skatle]

#zavitki:
zavitek = nalaganje_slik("zavitek.png")
zavitek = pygame.transform.scale_by(zavitek, 0.125)

zavitki_slike =[
    nalaganje_slik("zavitek3.png"),
    nalaganje_slik("zavitek4.png"),
    nalaganje_slik("zavitek5.png"),
    nalaganje_slik("zavitek6.png"),
    nalaganje_slik("zavitek7.png"),
]

zavitki = [
    [40, 340],
    [699, -65],
    [810, 475],
    [425, 775],
    [-230, 340]
]

# izbira muce(barve muce):

# animacija hoje:
hoja = [slika1, slika2, slika3, slika4]
hoja2 = [slik1, slik2, slik3]
vrstni_red = 0

# delovanje programa: 
delovanje = True

# kordinate muce
x = 390
y = 350

zavitek_animacija = False
prikaz = False
smer = "desno"
barva = "siva"
st = 0

igra = False
uvod = True
izbira = False

while delovanje:
    while uvod:
        
        zaslon.fill((36, 48, 62))
        spanje = True
        
        for el in pygame.event.get():
            if el.type == pygame.QUIT:
                delovanje = False
                uvod = False
            if el.type == pygame.MOUSEBUTTONDOWN:
                    if gumb_kvadrat.collidepoint(el.pos):
                        uvod = False
                        igra = True
            if el.type == pygame.MOUSEBUTTONDOWN:
                    if tacka_kvadrat.collidepoint(el.pos):
                        uvod = False
                        izbira = True

        tipka = pygame.key.get_pressed()
            
        zaslon.blit(napis, (20, 340))
        zaslon.blit(tacka, (670, 400))
        zaslon.blit(gumb_play, (570, 240))
        zaslon.blit(animacija_spanja[st], (10, 100))
        if st == len(animacija_spanja)-1:
            st = 0
        else:
            st += 1

        pygame.time.wait(500)

        if tipka[pygame.K_SPACE]:
            uvod = False
            igra = True
            break
    

        pygame.display.update()
    
    
    while izbira:
        uvod = False
        zaslon.fill((36, 48, 62))
        zaslon.blit(gumb_play, (730, 540))
        zaslon.blit(puscica_levo, (100, 300))
        zaslon.blit(puscica_desno, (500, 300))
        
        for el in pygame.event.get():
            gumb_kvadrat = gumb_play.get_rect(topleft= (730, 540))
            if el.type == pygame.QUIT:
                delovanje = False
                uvod = False
                igra = False
                izbira = False
            if el.type == pygame.MOUSEBUTTONDOWN:
                    if gumb_kvadrat.collidepoint(el.pos):
                        izbira = False
                        igra = True
            if el.type == pygame.MOUSEBUTTONDOWN:
                    if puscica_kvadrat.collidepoint(el.pos):
                        if barva == "siva":
                            barva = "oranžna"
                        else:
                            barva = "siva"
                            
            if el.type == pygame.MOUSEBUTTONDOWN:
                    if puscica2_kvadrat.collidepoint(el.pos):
                        if barva == "siva":
                            barva = "oranžna"
                        else:
                            barva = "siva"
            
        if barva == "siva":
            zaslon.blit(slika1, (450, 350))
        else:
            zaslon.blit(slik1, (450, 350))
                


        pygame.display.update()


    while igra:
        ura.tick(60)
        zaslon.blit(ozadje, (0,0))

        for el in pygame.event.get():
            if el.type == pygame.QUIT:
                delovanje = False
                igra = False

        #tipka:
        tipka = pygame.key.get_pressed()

        stari_x = x
        stari_y = y
        if barva == "siva":
            if tipka[pygame.K_LEFT] or tipka[pygame.K_RIGHT] or tipka[pygame.K_UP] or tipka[pygame.K_DOWN]:
                x, y, vrstni_red, smer = klik(x, y ,vrstni_red, smer)
            else:
                vrstni_red = 0

            if vrstni_red >= len(hoja) * 5:
                vrstni_red = 0

            trenutna_slika = hoja[vrstni_red // 5]
        else:
            if tipka[pygame.K_LEFT] or tipka[pygame.K_RIGHT] or tipka[pygame.K_UP] or tipka[pygame.K_DOWN]:
                x, y, vrstni_red, smer = klik(x, y ,vrstni_red, smer)
            else:
                vrstni_red = 0

            if vrstni_red >= len(hoja2) * 4:
                vrstni_red = 0

            trenutna_slika = hoja2[vrstni_red // 4]

        if smer == "levo":
            trenutna_slika = pygame.transform.flip(trenutna_slika, True, False)

        # da ne gre čez rob okna
        if x < 25 - trenutna_slika.get_width()//2 :
            x = 25 - trenutna_slika.get_width()//2

        if x > 900 - trenutna_slika.get_width():
            x = 900 - trenutna_slika.get_width()

        if y < 10 - trenutna_slika.get_height()//2:
            y = 10- trenutna_slika.get_height()//2

        if y > 700 - trenutna_slika.get_height():
            y = 700 - trenutna_slika.get_height()

        muca_kvadrat = trenutna_slika.get_rect(topleft = (x, y))

        star_x_y = [s.copy() for s in skatle]
        zavitek_x_y = [s.copy() for s in zavitki]

        if tipka[pygame.K_RIGHT] or tipka[pygame.K_LEFT] or tipka[pygame.K_DOWN] or tipka[pygame.K_UP]:
            skatla_premikanje(skatle, zavitki)

        trk = False
        for skatla_x, skatla_y in skatle:
            sktala_kvadrat = skatla.get_rect(topleft = (skatla_x, skatla_y))
            if muca_kvadrat.colliderect(sktala_kvadrat):
                trk = True
                break
            if skatla_x >= 1850 or skatla_y >= 1265 or skatla_y <= - 700 or skatla_x <= -1020:
                trk = True

        if trk:
            skatle = star_x_y
            zavitki = zavitek_x_y

        for skatla_x, skatla_y in skatle:
            zaslon.blit(skatla, (skatla_x, skatla_y))
        
        for zavitek_x, zavitek_y in zavitki:
            zaslon.blit(zavitek, (zavitek_x, zavitek_y))

        #če se dotakne zavitka
        for zavitek_x, zavitek_y in zavitki:
            zavitek_kvadrat = zavitek.get_rect(topleft = (zavitek_x, zavitek_y))
            if muca_kvadrat.colliderect(zavitek_kvadrat):
                nakljucni_zavitek = random.choice(zavitki_slike)
                zavitek_animacija = True
                zaslon.blit(tipka_O, (800, 600))
                #igra = False
            if muca_kvadrat.colliderect(zavitek_kvadrat) and tipka[pygame.K_o]:
                prikaz = True
       
        if prikaz:
            break
        

        zaslon.blit(trenutna_slika, (x, y))
        pygame.display.update()


    while zavitek_animacija:
        #zaslon.blit(ozadje, (0, 0))
        tipka = pygame.key.get_pressed()

        for el in pygame.event.get():
            if el.type == pygame.QUIT:
                zavitek_animacija = False
                igra = False
                delovanje = False
            
        if tipka[pygame.K_o]:
            zaslon.blit(tipka_X, (0, 600))
            zaslon.blit(nakljucni_zavitek, (150, 50))
        
        if tipka[pygame.K_x]:
            zavitek_animacija = False
            prikaz = False
            igra = True 
            break



        pygame.display.update()

    pygame.display.update()
pygame.quit()
