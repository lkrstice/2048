import random
class Kvadratic(object):
    #kljuc je broj, vrijednosti su naziv i bodovi
    __kvadratic_info = {
        2: ('2', 2),
        4: ('4', 4),
        8: ('8', 8),
        16: ('16', 16),
        32: ('32', 32),
        64: ('64', 64),
        128: ('128', 128),
        256: ('256', 256),
        512: ('512', 512),
        1024:('1024', 1024),
        2048:('2048', 2048)
    }
    
    @staticmethod
    def brojevi():
        return Kvadratic.__kvadratic_info.keys()
    
    def __init__(self, broj, vidljiv = True):
        self.__broj = broj
        self.__vidljiv = vidljiv

    @property
    def broj(self):
        return self.__broj

    @property
    def naziv(self):
        return Kvadratic.__kvadratic_info[self.__broj][0]
    @property
    def bodovi(self):
        return Kvadratic.__kvadratic_info[self.__broj][1]

    @property
    def vidljiv(self):
        return self.__vidljiv

    @vidljiv.setter
    def vidljiv(self,value):
        self.__vidljiv = value

    def __repr__(self):
        return self.__class__.__name__ + '(%r, %r)' % (self.__broj, self.__vidljiv)
        
    def __str__(self):
        return self.naziv.title()

class Matrica(object):
    '''
    klasa sa metodama za formiranje matrice

    '''
    def __init__(self):
        
        #bodove na pocetku igre postaviti na nulu
        self.__bodovi=0

        #formiranje matrice 4x4
        self.__matrica=[[0 for i in range(4)]for j in range(4)]

        #dodavanje pocetnih dva kvadratica matrici
        for i in range(2):

            #kvadratici koji se generiraju na pocetku
            # mogu biti vrijednosti 2 ili 4
            lista = [2,4]

            #biramo random index reda i stupca u intervalu(0,3)
            r = random.randint(0,3)
            c = random.randint(0,3)

            while(self.__matrica[r][c] != 0):
                r = random.randint(0,3)
                c = random.randint(0,3)

            #dodamo kvadratic u matricu
            self.__matrica[r][c] = random.choice(lista)
    

    def dodaj_kvadratic(self):

        '''
        metoda dodaj_2_nova uzima matricu te dodaje jedan
        novi kvadratic koji ima vrijednost 2 ili 4
        '''

        #uzimamo random red i stupac matrice
        r = random.randint(0, 3)
        c = random.randint(0, 3)

        lista = [2,4]

        #provjeravamo je li kvadratic koji se nalazi
        # u 'r' redu i 's' stupcu prazan, tj. je li jednak 0,
        # ako nije prazan trazimo novi kvadratic
        while(self.__matrica[r][c] != 0):

            r = random.randint(0, 3)
            c = random.randint(0, 3)

        #smjestit cemo novu vrijednost u kvadratic
        self.__matrica[r][c] = random.choice(lista)

        #vracamo matricu
        return self.__matrica


    def trenutno_stanje(self):

        '''
        Metoda trenutno_stanje() prima matricu, ide po
        do svakog kvadratica u matrici po redu i
        vraca poruku o statusu matrice
        '''

        # u trenutku kada se u matrici stvori kvadratic
        # s vrijednosti 2048 - znaci POBJEDA
        for i in range(4):
            for j in range(4):
                if(self.__matrica[i][j] == 2048):
                    return 'POBJEDA!'

        # ako se u matrici nalazi barem jedan kvadratic
        # s vrijednosti 0 - znaci IGRA NIJE GOTOVA
        for i in range(4):
            for j in range(4):
                if(self.__matrica[i][j] == 0):
                    return 'IGRA NIJE GOTOVA...'

        # ako u matrici ne postoji niti jedan prazan kvadratic, tj.
        # nisi jedan kvadratic vrijednosti 0, a u matrici se nalaze
        # iste vrijednosti jedna pored druge ili jedna ispod druge
        # znaci da IGRA NIJE GOTOVA
        for i in range(3):
            for j in range(3):
                if(self.__matrica[i][j] == self.__matrica[i + 1][j] or self.__matrica[i][j] == self.__matrica[i][j + 1]):
                    return 'IGRA NIJE GOTOVA...'


        for k in range(3):
            if(self.__matrica[3][k] == self.__matrica[3][k + 1]):
                return 'IGRA NIJE GOTOVA...'

        for j in range(3):
            if(self.__matrica[j][3] == self.__matrica[j + 1][3]):
                return 'IGRA NIJE GOTOVA...'

        #ako nema praznih kvadratica niti vrijednosti koje bi se
        #mogle spojiti tu je KRAJ
        return 'KRAJ! VISE SRECE DRUGI PUT :)'


    def komprimiraj(self):

        '''
        funkcija za komprimiranje matrice
        nakon svakog koraka
        prije i nakon spajanja u matrici
        '''

        #bool varijabla 'promjena' za odredivanje
        #je li se dogodila ijedna promjena ili ne
        promjena = False

        #prazna matrica
        nova_mat = []

        # sa svim praznim kvadraticima
        for j in range(4):
            nova_mat.append([0]*4)

        #ovdje cemo pomaknuti unose
        #svakog kvadratica lijevo
        #red po red
        for i in range(4):
            br = 0

            #petlja za prelazak svakog stupca u
            # odgovarajucem redu
            for j in range(4):
                if(self.__matrica[i][j] != 0):

                    #ako kvadratic nije prazan tada
                    #cemo pomaknuti taj kvadratic s vrijednosti na
                    #prethodni prazni kvadratic u tom retku koji je oznacen
                    # s br varijablom
                    nova_mat[i][br] = self.__matrica[i][j]

                    if(j != br):
                        promjena = True
                    br += 1

        self.__matrica = nova_mat

        #vratit novu komprimiranu matricu i bool varijablu promjene
        return self.__matrica, promjena


    def spojene(self):

        #funkcija spojene() spaja kvadratice iste vrijednosti
        # u matrici nakon komprimiranja

        promjena = False

        for i in range(4):
            for j in range(3):

                #ako trenurni kvadratic ima istu vrijednost
                #kao i sljedeci kvadratic u retku i ako nisu prazni
                if(self.__matrica[i][j] == self.__matrica[i][j + 1] and self.__matrica[i][j] != 0):

                    #vrijednost jednog kvadratica novog koji
                    # nastaje spajanjem bit ce duplo veca,
                    # a vrijednost drugog kvadratica ce biti 0
                    self.__matrica[i][j] = self.__matrica[i][j] * 2
                    self.__matrica[i][j + 1] = 0
                    self.__bodovi+=self.__matrica[i][j]

                    #nakon spajanja postaviti promjenu na True
                    promjena = True

        #vratiti matricu i bool varijablu promjene
        return self.__matrica, promjena,self.__bodovi

    def obrnuta(self):

        #funkcija za obrnutu matricu
        #znaci preokretanje sadrzaja
        #svaki redak (preokretanje niza)

        #nova matrica
        nova_mat = []

        #petlja koja ide po retcima i pravi obrnuti redosljed
        for i in range(4):
            nova_mat.append([])
            for j in range(4):
                nova_mat[i].append(self.__matrica[i][3 - j])
        self.__matrica = nova_mat

        return self.__matrica
    
    def transponirana(self):

        #funkcija za dobivanje transponiranja matrice
        #za medusobnu izmjenu redaka i stupaca
        nova_mat = []
        for i in range(4):
            nova_mat.append([])
            for j in range(4):
                nova_mat[i].append(self.__matrica[j][i])
        self.__matrica = nova_mat
        return self.__matrica


    def pomakni_lijevo(self):

        #funkcija pomakni_lijevo() sluzi za
        # azuriranje matrice
        #ako se pomaknemo u lijevo

        #prvo kompimirati matricu
        novi_grid, promjena1 = self.komprimiraj()

        #zatim spojiti kvadratice
        novi_grid, promjena2,self.__bodovi = self.spojene()

        promjena = promjena1 or promjena2

        #zatim je ponovno komprimirati i spojiti
        novi_grid, temp = self.komprimiraj()

        self.__matrica = novi_grid

        #vratiti novu matricu i bool vrijednost promjene
        return self.__matrica, promjena,self.__bodovi

    def pomakni_desno(self):

        #funkcija za azuriranje matrice
        #pomicanje u desno

        #da bismo je pomjerili udesno
        #prvo matricu treba obrnuti
        novi_grid = self.obrnuta()

        novi_grid, promjena,self.__bodovi = self.pomakni_lijevo()

        novi_grid = self.obrnuta()
        self.__matrica = novi_grid
        return self.__matrica, promjena,self.__bodovi

    def pomakni_gore(self):

        #fukcija za azuriranje matrice
        #pomicanje gore

        #prvo matricu transponirati
        novi_grid = self.transponirana()

        #pomaknuti u lijevo
        novi_grid, promjena,self.__bodovi = self.pomakni_lijevo()

        #ponovno transponirati
        novi_grid = self.transponirana()

        self.__matrica = novi_grid
        return self.__matrica, promjena,self.__bodovi

    def pomakni_dolje(self):

        #funkcija za azuriranje matrice
        #pomicanje dolje

        #prvo treba matricu transponirati
        novi_grid = self.transponirana()

        #pamaknuti je udesno
        novi_grid, promjena,self.__bodovi = self.pomakni_desno()

        #ponovno transponirati
        novi_grid = self.transponirana()

        self.__matrica = novi_grid
        return self.__matrica, promjena,self.__bodovi

    
class Igrac(object):

    '''
    Klasa u kojoj se nalaze podaci
    o korisnikovom unosu
    '''
    def __init__(self, unos):
        self.__unos = unos


    @property
    def unos(self):
        return self.__unos
    
    def __str__(self):
        return self.__unos


class PrikazIgre(object):

    '''
    view klasa
    '''
    
    def prikaziPocetakIgre(self):

        #ispisuje se naziv igre i upute za igranje

        print('*' * 50)
        print ('*' * 22 + ' 2048 ' + '*' * 22)
        print('*' * 50)
        print("Naredbe su sljedeće : ")
        print("'W' ili 'w' : Pomakni gore")
        print("'S' ili 's' : Pomakni dolje")
        print("'A' ili 'a' : Pomakni lijevo")
        print("'D' ili 'd' : Pomakni desno")
        
    def unos_naredbe(self):

        #funkcija za korisnikov onos poteza

        x = input("Potez: ")
        return x


p = PrikazIgre()
m = Matrica()

print(m.dodaj_kvadratic())

class Igra(object):

    '''
    controler klasa
    '''


    pocetak = True
    
    while pocetak:

        #prikazuje se pocetak igre
        p.prikaziPocetakIgre()

        #trazi se korisnikov potez
        x = p.unos_naredbe()

        flag = 0

        #provjera unosa
        #ako je unos w, znaci da se treba
        #matrica pomjeriti gore
        if(x == 'W' or x == 'w'):

            m.__matrica, flag ,bodovi= m.pomakni_gore()

            #trazi se trenutno stanje u matrici
            status = m.trenutno_stanje()

            #ispis trenutnog stanja
            print(status)

            #provjera stanja
            if(status == 'IGRA NIJE GOTOVA...'):
                m.dodaj_kvadratic()

            else:
                break

        #ako je unos s, znaci da se treba
        #matrica pomjeriti dolje
        elif(x == 'S' or x == 's'):

            m.__matrica, flag,bodovi = m.pomakni_dolje()

            #trazi se trenutno stanje u matrici
            status = m.trenutno_stanje()

            #ispisuje se stanje
            print(status)

            if(status == 'IGRA NIJE GOTOVA...'):
                m.dodaj_kvadratic()

            else:
                break

        #ako je unos a
        # pomakni matricu ulijevo
        elif(x == 'A' or x == 'a'):

            m.__matrica, flag ,bodovi= m.pomakni_lijevo()

            #trazi se trenutno stanje u matrici
            status = m.trenutno_stanje()

            #ispisuje se stanje
            print(status)

            if(status == 'IGRA NIJE GOTOVA...'):
                m.dodaj_kvadratic()

            else:
                break

        #ako je unos d
        #pomakni matricu u desno
        elif(x == 'D' or x == 'd'):

            m.__matrica, flag ,bodovi= m.pomakni_desno()

            #trazi se trenutno stanje u matrici
            status = m.trenutno_stanje()

            #ispis stanja
            print(status)

            if(status == 'IGRA NIJE GOTOVA...'):
                m.dodaj_kvadratic()

            else:
                break


        #ako korisnikov unos nije valjan
        else:
            print("Netočan unos!")

        #ispis bodova
        print("Bodovi: ",bodovi)
        #ispis dobivene matrice
        print(m.__matrica)

def main():
    
    prikaz = PrikazIgre()
    igra =Igra(prikaz)
    igra.PrikazIgre()

main()
    


        
