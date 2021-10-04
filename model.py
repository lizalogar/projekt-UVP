import random
import bottle


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
        if self.kdo_je_na_vrsti == self.racunalnik:
            self.naredi_potezo_racunalnik()


    def __str__(self):
        s = ''
        niz = ''
        print(self.baloni)
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
            #self.naredi_zmagovalno_kombinacijo()
            #naredi zmagovalno potezo
            for i in range(self.st_vrstic):
                if self.st_balonov_v_vrstici[i] > 0:
                    # ce so poceni vsi baloni razen nekaj balonov v eni vrstici, naj racunalnik poci vse razen enega
                    if sum(self.st_balonov_v_vrstici) == self.st_balonov_v_vrstici[i]:
                        st_pocenih = self.st_balonov_v_vrstici[i] - 1
                        self.st_balonov_v_vrstici[i] -= st_pocenih

                        self.poci_balone(i, st_pocenih)                        
                        return

                    # ce je v neki vrstici en balon in v neki drugi eden ali vec, v ostalih pa 0 balonov, naj racunalnik poci vse v vrstici z vec baloni
                    elif sum(self.st_balonov_v_vrstici) == self.st_balonov_v_vrstici[i] + 1:
                        st_pocenih = self.st_balonov_v_vrstici[i]
                        self.st_balonov_v_vrstici[i] -= st_pocenih
                    
                        self.poci_balone(i, st_pocenih)
                        return  
                        

            
            # naredi dobro potezo
            # naredi kombinacijo 1 2 3 iz 1 2 0 *
            if 1 in self.st_balonov_v_vrstici and 2 in self.st_balonov_v_vrstici and 0 in self.st_balonov_v_vrstici:
                for i in range(self.st_vrstic):
                    if self.st_balonov_v_vrstici[i] > 3:
                        st_pocenih = self.st_balonov_v_vrstici[i] - 3
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return      


            # naredi kombinacijo 1 2 3
            if 1 in self.st_balonov_v_vrstici and 2 in self.st_balonov_v_vrstici and 3 in self.st_balonov_v_vrstici:
                for i in range(self.st_vrstic):
                    if self.st_balonov_v_vrstici[i] > 3:
                        st_pocenih = self.st_balonov_v_vrstici[i]
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return 
                    elif (self.st_balonov_v_vrstici[i] == 1 and self.st_balonov_v_vrstici.count(1) == 2) or (self.st_balonov_v_vrstici[i] == 2 and self.st_balonov_v_vrstici.count(2) == 2) or (self.st_balonov_v_vrstici[i] == 3 and self.st_balonov_v_vrstici.count(3) == 2):     
                        st_pocenih = self.st_balonov_v_vrstici[i]
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return 

            # naredi kombinacijo 1 2 3
            if 1 in self.st_balonov_v_vrstici and 3 in self.st_balonov_v_vrstici and 0 in self.st_balonov_v_vrstici:
                for i in range(self.st_vrstic):
                    if self.st_balonov_v_vrstici[i] > 3:
                        st_pocenih = self.st_balonov_v_vrstici[i] - 2
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return 
                    elif self.st_balonov_v_vrstici[i] == 3 and self.st_balonov_v_vrstici.count(3) == 2:
                        st_pocenih = self.st_balonov_v_vrstici[i] - 2
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return                         

            # naredi kombinacijo 1 2 3
            if 2 in self.st_balonov_v_vrstici and 3 in self.st_balonov_v_vrstici and 0 in self.st_balonov_v_vrstici:
                for i in range(self.st_vrstic):
                    if self.st_balonov_v_vrstici[i] > 3:
                        st_pocenih = self.st_balonov_v_vrstici[i] - 1
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return
                    elif (self.st_balonov_v_vrstici[i] == 3 and self.st_balonov_v_vrstici.count(3) == 2) or (self.st_balonov_v_vrstici[i] == 2 and self.st_balonov_v_vrstici.count(2) == 2):
                        st_pocenih = self.st_balonov_v_vrstici[i] - 1
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return          

            #naredi kombinacijo 3 3 0 0 iz 3 k 0 0 ce k > 3                           
            if 3 in self.st_balonov_v_vrstici and self.st_balonov_v_vrstici.count(0) == 2:
                for i in range(self.st_vrstic):
                    if self.st_balonov_v_vrstici[i] > 3:
                        st_pocenih = self.st_balonov_v_vrstici[i] - 3
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return 
            
            #naredi kombinacijo 3 3 0 0 iz 0 3 3 k ce k > 0
            if 0 in self.st_balonov_v_vrstici and self.st_balonov_v_vrstici.count(3) == 2:
                for i in range(self.st_vrstic):
                    if self.st_balonov_v_vrstici[i] != 3 and self.st_balonov_v_vrstici[i] != 0:
                        st_pocenih = self.st_balonov_v_vrstici[i]
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return 
            elif self.st_balonov_v_vrstici.count(3) == 3 and 0 in self.st_balonov_v_vrstici:
                for i in range(self.st_vrstic):
                    if self.st_balonov_v_vrstici[i] == 3:
                        st_pocenih = self.st_balonov_v_vrstici[i]
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return                 
            

            #naredi kombincijo 4 4 0 0 iz 4 k 0 0 ce k > 4
            if 4 in self.st_balonov_v_vrstici and self.st_balonov_v_vrstici.count(0) == 2:
                for i in range(self.st_vrstic):
                    if self.st_balonov_v_vrstici[i] > 4:
                        st_pocenih = self.st_balonov_v_vrstici[i] - 4
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return

            #naredi kombinacijo 4 4 0 0 iz 0 4 4 k ce k > 0
            if 0 in self.st_balonov_v_vrstici and self.st_balonov_v_vrstici.count(4) == 2:
                for i in range(self.st_vrstic):
                    if self.st_balonov_v_vrstici[i] != 4 and self.st_balonov_v_vrstici[i] != 0:
                        st_pocenih = self.st_balonov_v_vrstici[i]
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return 
            elif self.st_balonov_v_vrstici.count(4) == 3 and 0 in self.st_balonov_v_vrstici:
                for i in range(self.st_vrstic):
                    if self.st_balonov_v_vrstici[i] == 4:
                        st_pocenih = self.st_balonov_v_vrstici[i]
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return     

            #naredi kombincijo 5 5 0 0 iz 5 k 0 0 ce k > 5
            if 5 in self.st_balonov_v_vrstici and self.st_balonov_v_vrstici.count(0) == 2:
                for i in range(self.st_vrstic):
                    if self.st_balonov_v_vrstici[i] > 5:
                        st_pocenih = self.st_balonov_v_vrstici[i] - 5
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return

            #naredi kombinacijo 5 5 0 0 iz 0 5 5 k ce k > 0
            if 0 in self.st_balonov_v_vrstici and self.st_balonov_v_vrstici.count(5) == 2:
                for i in range(self.st_vrstic):
                    if self.st_balonov_v_vrstici[i] != 5 and self.st_balonov_v_vrstici[i] != 0:
                        st_pocenih = self.st_balonov_v_vrstici[i]
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return      

            # naredi kombinacijo 2 2
            if self.st_balonov_v_vrstici.count(2) == 2 and 0 in self.st_balonov_v_vrstici:
                for i in range(self.st_vrstic):
                    if self.st_balonov_v_vrstici[i] != 2 and self.st_balonov_v_vrstici[i] != 0:
                        st_pocenih = self.st_balonov_v_vrstici[i]
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return    

            # naredi kombinacijo 2 2
            if self.st_balonov_v_vrstici.count(0) == 2 and 2 in self.st_balonov_v_vrstici:
                for i in range(self.st_vrstic):
                    if self.st_balonov_v_vrstici[i] > 2:
                        st_pocenih = self.st_balonov_v_vrstici[i] - 2
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return    
            
            # naredi kombinacijo 1 1 1
            if self.st_balonov_v_vrstici.count(1) == 2 and 0 in self.st_balonov_v_vrstici:
                for i in range(self.st_vrstic):
                    if self.st_balonov_v_vrstici[i] > 1:
                        st_pocenih = self.st_balonov_v_vrstici[i] - 1
                        self.st_balonov_v_vrstici[i] -= st_pocenih 
                        self.poci_balone(i, st_pocenih)
                        return    

            # v ostalih primerih naredi nakljucno veljavno potezo v prvi mozni vrstici
            for i in range(self.st_vrstic):
                if self.st_balonov_v_vrstici[i] > 0:            
                    st_pocenih = random.randint(1, self.st_balonov_v_vrstici[i])
                    if sum(self.st_balonov_v_vrstici) - st_pocenih != 0:
                        self.st_balonov_v_vrstici[i] -= st_pocenih

                        self.poci_balone(i, st_pocenih)
                        return

    def poci_balone(self, vrstica, st_pocenih):

        for j in range(len(self.baloni[vrstica])):
            if self.baloni[vrstica][j] == 1 and st_pocenih > 0: 
                self.baloni[vrstica][j] = 0
                st_pocenih -= 1
        self.kdo_je_na_vrsti = (self.kdo_je_na_vrsti % 2) + 1
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
            #print('stevilo balonov v vrstici:', sum(self.st_balonov_v_vrstici))
            print(self)
            print()
        print('zmagal je', self.konec_igre())
        
    def igraj_spletni_vmesnik(self, i, n):
        # self.kdo_je_na_vrsti = random.randint(1, 2) 

        if self.konec_igre() == 0: 
            if self.naredi_potezo_igralec(i, n) == False:
                raise IndexError("Neveljavna poteza! poskusi ponovno")

            self.naredi_potezo_racunalnik()

if __name__ == "__main__":
    igra = Igra()
    print(igra)

    igra.igraj()

    print(igra)
