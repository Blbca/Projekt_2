'''

projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petr Novák
email: peternovaksson@seznam.cz
discord: Goodchilde#1716

'''

import random

oddelovac = 65 * "-"

def hlavni():
    
    """
    Hlavní fce, která obsahuje všechny dílčí fce.
    """

    pokusu = 0
    intro()
    hadane_cislo = cislo_vygenerovane()
    while True:
        uzivatel_cislo = cislo_uzivatel()
        vyhodnoceni(uzivatel_cislo, hadane_cislo) 
        print(oddelovac)
        pokusu = pocitani_pokusu(uzivatel_cislo, hadane_cislo, pokusu) # Zde si do promněné "pokusu" uložím počet pokusu a ten posílam zpátky do fce, aby se počet buď zvýšil a nebo pomocí printu zobrazil konečný počet pokusů
        # print pro rychlejsí kontrolu:
        #print(hadane_cislo)

def intro() -> None: 
    """
    Tato fce má za úkol uvítat Vás u hry Cow and Bulls a
    představit Vám pravidla.
    """

    print(oddelovac)
    print("Ahoj! Vítám Vás u hry Cows and Bulls!")
    print(oddelovac)
    print("""Pravidla: Program vygeneruje 4 místné tajné číslo, které se bude
skladat ze 4 různých čísel a nebude začínat 0. Poté se hráč snaží 
toto číslo uhodnout. Pokud jsou odpovídající číslice na svých 
správných pozicích, jsou to „bulls", pokud jsou na různých pozicích, 
jsou to „cows“.""")
    print(oddelovac)
    input("Zmáčkni 'Enter' pro pokračování.")


def cislo_vygenerovane() -> list:
    """
    Tato fce má za úkol vrátit čtyřmístné číslo, 
    které musíte uhádnout 
    Příklad: 1234
    """

    while True:
        hadane_cislo = []
        cislo = str(random.randint(1000,9999))
        for c in cislo:
            if c not in hadane_cislo:
                hadane_cislo.append(c)
            else:
                continue

        if len(hadane_cislo) == 4:
            False
            return hadane_cislo
        else:
            continue

def cislo_uzivatel() -> list:
    """
    Do této fce bude hráč zadávat/hádat čtyřmístné číslo, 
    kterým se bude snažit uhádnout číslo, které vychází z fce 'had_cislo'.
    Pokud zadaná hodnota nebude numerická vyskočí chybová hláška.
    Pokud zadaná hodnota bude obsahovat dvakrát stejné číslo vyskočí 
    chybová hláška.
    """
    
    while True:
        uzivatel_cislo = []
        print(oddelovac)
        vstup = input("Zadejte čtyřmístné číslo: ")
        if vstup.isnumeric() and len(vstup) == 4 and vstup[0] != "0":
            for i in vstup:
                if i not in uzivatel_cislo:
                    uzivatel_cislo.append(i)
                else:
                    print("Vaše číslo obsahuje více stejných čísel")
                    break
        else:
            print("Vaše číslo obsahuje nepovolená znaky a nebo 0 nazačátku")
        if len(uzivatel_cislo) == 4:
            False
            return uzivatel_cislo
        else:
            continue

def vyhodnoceni(hracuv_typ: list, cil: list) -> None:
    """
    Tato fce slouží k vyhodnocení a porovnání dvou čísel. 
    Číslo, které vychází z fce 'had_cislo'(hádané číslo) s číslem,
    které vychází z fce 'cislo_uzivatel'. 
    """

    if hracuv_typ == cil:
        print(oddelovac)
        print("Výborně vyhral jste")  
    else:
        bulls = 0
        cows = 0
        for i in range(4):
            if hracuv_typ[i] == cil[i]:
                bulls += 1
            elif hracuv_typ[i] in cil:
                cows += 1
        if bulls == 1:
            print("Bull: ",bulls)
        else:
            print("Bulls: ",bulls)
        if cows == 1:
            print("Cow: ",cows)
        else:
            print("Cows: ",cows)

def pocitani_pokusu(hracuv_typ: list, cil: list, pokusu: int) -> int:
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
