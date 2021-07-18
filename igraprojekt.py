import random

class Igra:
    def __init__(self):
        self.st_vrstic = 4
        self.baloni = []
        for i in range(self.st_vrstic):
            self.baloni.append([1 for k in range(2 * i + 1)])
        self.st_balonov_v_vrstici = [sum(self.baloni[i]) for i in range(self.st_vrstic)]
        self.racunalnik = 1
        self.igralec = 2
        self.kdo_je_na_vrsti = random.randint(1, 2)


    def __str__(self):
        s = ''
        niz = ''
        for i in range(len(self.baloni)):
            for znak in self.baloni[i]:
                if znak == 1:
                    s += 'o' + ' '
                else:
                    s += '  '
            niz += s + '(' + str(self.st_balonov_v_vrstici[i]) + ')\n'
            s = ''
        return niz


    def naredi_potezo_racunalnik(self):
        if self.kdo_je_na_vrsti == self.racunalnik:
            for i in range(len(self.st_balonov_v_vrstici)):
                if self.st_balonov_v_vrstici[i] > 0:
                        # ce so poceni vsi baloni razen nekaj balonov v eni vrstici, naj racunalnik poci vse razen enega
                        if sum(self.st_balonov_v_vrstici) == self.st_balonov_v_vrstici[i]:
                            st_pocenih = self.st_balonov_v_vrstici[i] - 1
                            self.st_balonov_v_vrstici[i] -= st_pocenih

                        # ce je v neki vrstici en balon in v neki drugi eden ali vec, v ostalih pa 0 balonov, naj racunalnik poci vse v vrstici z vec baloni
                        elif sum(self.st_balonov_v_vrstici) == self.st_balonov_v_vrstici[i] + 1:
                            st_pocenih = self.st_balonov_v_vrstici[i]
                            self.st_balonov_v_vrstici[i] -= st_pocenih                  

                        # v ostalih primerih naredi nakljucno veljavno potezo
                        else:
                            st_pocenih = random.randint(1, self.st_balonov_v_vrstici[i])
                            if sum(self.st_balonov_v_vrstici) - st_pocenih != 0:
                                self.st_balonov_v_vrstici[i] -= st_pocenih


                        for j in range(len(self.baloni[i])):
                            if self.baloni[i][j] == 1 and st_pocenih > 0: 
                                self.baloni[i][j] = 0
                                st_pocenih -= 1
                        self.kdo_je_na_vrsti = (self.kdo_je_na_vrsti % 2) + 1
                        break

    # n je stevilo balonov, ki jih hocem pociti v i-ti vrstici. funkcija naj vrne True, ce je poteza uspesna, spremeni kdo je na vrsti in popoka balone. sicer vrne False
    def naredi_potezo_igralec(self, i, n):
        if self.kdo_je_na_vrsti == self.igralec:
            if i >= len(self.baloni) or i < 0 or n > self.st_balonov_v_vrstici[i] or n < 1 or sum(self.st_balonov_v_vrstici) - n == 0:
                return False
            else:
                poceni = 0
                for k in range(len(self.baloni[i])):
                    if self.baloni[i][k] == 1 and poceni < n:
                        self.baloni[i][k] = 0
                        poceni += 1
                self.st_balonov_v_vrstici[i] -= n
                self.kdo_je_na_vrsti = (self.kdo_je_na_vrsti % 2) + 1
                return True

    # funkcija vrne 1, ce zmaga racunalnik, 2 ce zmaga igralec in 0 ce igre se ni konec
    def konec_igre(self):
        if sum(self.st_balonov_v_vrstici) == 1 and self.kdo_je_na_vrsti == 2:
            return 1
        elif sum(self.st_balonov_v_vrstici) == 1 and self.kdo_je_na_vrsti == 1:
            return 2
        else:
           return 0 


    def igraj(self):
        # self.kdo_je_na_vrsti = random.randint(1, 2) 

        print('------------------------')
        if self.kdo_je_na_vrsti == 1:
            print('zacne igralec', self.racunalnik)
        else:
            print('zacne igralec', self.igralec)

        while self.konec_igre() == 0: 
            if self.kdo_je_na_vrsti == 2:
                vrst = input('vnesi vrstico:')
                st = input('vnesi stevilo balonov, ki jih hoces pociti:')
                while self.naredi_potezo_igralec(int(vrst), int(st)) == False:
                    print('neveljavno stevilo vrstic ali balonov! Poskusi ponovno')
                    vrst = input('vnesi vrstico:')
                    st = input('vnesi stevilo balonov, ki jih hoces pociti:')                    
            else:
                self.naredi_potezo_racunalnik()
            print('stevilo balonov v vrstici:', sum(self.st_balonov_v_vrstici))
            print(self)
            print()
        print('zmagal je', self.konec_igre())



igra = Igra()
print(igra)

igra.igraj()

print(igra)
