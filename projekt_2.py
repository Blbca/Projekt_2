'''

projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petr Novák
email: peternovaksson@seznam.cz
discord: Goodchilde#1716

'''

import random


oddelovac = "-----------------------------------------------"
def hlavni():
    
    """
    Hlavní fce, která obsahuje všechny dílčí fce.
    """
    pokusu = 0
    intro()
    hadane_cislo = had_cislo()
    while True:
        uzivatel_cislo = cislo_uzivatel()
        vyhodnoceni(uzivatel_cislo, hadane_cislo) 
        print(f"{oddelovac}")
        pokusu = pocitani_pokusu(uzivatel_cislo, hadane_cislo, pokusu)
        #print(hadane_cislo) jen pro rychlejsi kontrolu

def intro() -> None: 
    """
    Tato fce má za úkol uvítat Vás u hry Cow and Bulls a
    představit Vám pravidla.
    """
    print(f"{oddelovac}")
    print("Ahoj! Vítám Vás u hry Cows and Bulls!")
    print(f"{oddelovac}")
    
    print("Pravidla: Hráč 1 a hráč 2, reprezentovaní X a O, se střídají"
          "v označení políček v mřížce 3*3. Vyhrává hráč, kterému se podaří umístit "
          "tři své značky do vodorovné, svislé nebo diagonální řady.")
    print(f"{oddelovac}")
    input("Zmáčkni 'Enter' pro pokračování.")


def had_cislo() -> list:
    """
    Tato fce má za úkol vrátit čtyřmístné číslo, 
    které musíte uhádnout 
    Příklad: 1234
    """

    seznam = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    hadane_cislo = random.sample(seznam, 4)
    if hadane_cislo[0] == "0":
        hadane_cislo.reverse()
    return hadane_cislo

def cislo_uzivatel() -> list:
    """
    Do této fce bude hráč zadávat/hádat čtyřmístné číslo, 
    kterým se bude snažit uhádnout číslo, které vychází z fce 'had_cislo'.
    Pokud zadaná hodnota nebude numerická vyskočí chybová hláška.
    Pokud zadaná hodnota bude obsahovat dvakrát stejné číslo vyskočí 
    chybová hláška.
    """
    uzivatel_cislo = []
    while True:
        print(f"{oddelovac}")
        vstup=input("Zadejte čtyřmístné číslo: ")
        if vstup.isnumeric() and len(vstup) == 4 and vstup[0] != "0":
            int(vstup)
            for i in vstup:
                if i not in uzivatel_cislo:
                    uzivatel_cislo.append(i)
                else:
                    print("Vaše číslo obsahuje více stejných čísel")
                    uzivatel_cislo= [] 
        else:
            print("Vaše číslo obsahuje nepovolená znaky a nebo 0 nazačátku")
            uzivatel_cislo= []
        if len(uzivatel_cislo) == 4:
            False
            return uzivatel_cislo
        else:
            uzivatel_cislo= []

def vyhodnoceni(hracuv_typ: list, cil: list) -> None:
    """
    Tato fce slouží k vyhodnocení a porovnání dvou čísel. 
    Číslo, které vychází z fce 'had_cislo'(hádané číslo) s číslem,
    které vychází z fce 'cislo_uzivatel'. 
    """
    if hracuv_typ == cil:
        print(f"{oddelovac}")
        print("Výborně vyhral jste")  
    else:
        bulls = 0
        cows = 0
        for i in range(4):
            if hracuv_typ[i] == cil[i]:
                bulls += 1
            elif hracuv_typ[i] in cil:
                cows += 1
        print("Bulls: ",bulls)
        print("Cows: ",cows)

def pocitani_pokusu(hracuv_typ: list, cil: list, pokusu: int) -> None:
    """
    Tato fce slouží k počítání pokusu, 
    kterých bylo potřeba k dohrání hry. 
    """
    
    if hracuv_typ != cil:
        pokusu += 1
        print(f"Váš aktuální počet pokusů je: {pokusu}")
        return pokusu
    else:
        pokusu += 1
        print(f"K uhádnutí jste potřeboval: {pokusu} pokusů")
        quit()

        
    

if __name__ == "__main__":
    hlavni()   
