import Renszarvas

def beolvas():
    lista = []
    beFile = open("fileok/Mikulasszan.txt", "r", encoding="utf-8")
    adatokListaja = beFile.readlines()
    for index in range(1, len(adatokListaja), 1):
        if not ("Santa Claus" in adatokListaja[index]):
            daraboltSor = adatokListaja[index].split("@")
            szarvas = Renszarvas.Renszarvas(daraboltSor[0], daraboltSor[1], daraboltSor[2], daraboltSor[3])
            lista.append(szarvas)


    beFile.close()
    return lista
def angolMegfelelo(nev, lista):
    index = 0
    talalat = True
    while index < len(lista) and talalat:
        if lista[index].nevMagyar == nev:
            talalat = False
        index += 1

    if not talalat:
        print(lista[index - 1].nevAngol)
    else:
        print("Nincsen ilyen rénszarvas")
def hetes():
    #alap
    szarvasokListaja = beolvas()

    #a
    for szarvas in szarvasokListaja:
        print(szarvas.kiir())

    #b
    print(f"A rénszarvasok száma: {len(szarvasokListaja)}.")

    #c
    index = 0
    talalat = True
    while index < len(szarvasokListaja) and talalat:
        if szarvasokListaja[index].nevMagyar == "Pompás":
            talalat = False
        index += 1

    if not talalat:
        print(szarvasokListaja[index-1].nevAngol)
    else:
        print("Nincsen ilyen rénszarvas")

    """    
    for szarvas in szarvasokListaja:
        if szarvas.nevMagyar == "Pompás":
            print(szarvas.nevAngol)
    """