nb = int(input("Donnez un nombre entier : "))

# Nombre premier ?
liste_premiers = [2]
nbtest = 3
while nbtest <= nb :
    diviseur = 0
    non = 0
    while diviseur < len(liste_premiers) and non == 0 :
        if nbtest % liste_premiers[diviseur] == 0 :
            non = 1
        diviseur += 1
    if non == 0 :
        liste_premiers += [nbtest]
    nbtest += 1

# Fait parti d'un couple de nombres premiers jumeaux ?
couple = 0
if liste_premiers[-1] == nb :
    nbtest = nb - 2
    diviseur = 2
    non = 0
    while non == 0 :
        if nbtest % diviseur == 0 :
            non = 1
        elif diviseur == nbtest - 1 :
            non = 2
        diviseur += 1
    if non == 2 :
        couple = 1
    else :
        nbtest = nb + 2
        diviseur = 2
        non = 0
        while non == 0 :
            if nbtest % diviseur == 0 :
                non = 1
            elif diviseur == nbtest - 1 :
                non = 2
            diviseur += 1
        if non == 2 :
            couple = 2

# Décomposition en facteurs premiers
if not nb == 0 and not nb == 1 :
    decomp = []
    liste_premiers_test = liste_premiers
    nb2 = nb
    while nb2 > 1 :
        if nb2 % liste_premiers_test[-1] == 0 :
            nb2 = nb2/liste_premiers_test[-1]
            decomp += [liste_premiers_test[-1]]
        else :
            liste_premiers_test = liste_premiers_test[0:-1]

# Diviseurs
liste_diviseurs = []
for i in range (1,nb+1,1) :
    if nb % i == 0 :
        liste_diviseurs += [i]

# Factorielle
factorielle = 1
if not nb == 0 :
    for i in range (1,nb+1,1) :
        factorielle = factorielle * i

# Nombre de Fibonacci
liste_fibonacci = [1,1]
while liste_fibonacci[-1] < nb :
    liste_fibonacci += [liste_fibonacci[-2]+liste_fibonacci[-1]]

# Binaire
if not nb == 0 :
    binaire = ""
    puissance = 0
    while not 2**puissance > nb :
        puissance += 1
    puissance -= 1
    nb2 = nb
    for loop in range (puissance+1) :
        if 2**puissance <= nb2 :
            nb2 -= 2**puissance
            binaire += "1"
        else :
            binaire += "0"
        puissance -= 1
else :
    binaire = "0"

# base 8
if nb == 0 :
    base8 = "0"
else :
    base8 = ""
    r = 0
    q = nb
    while not q == 0 :
        r = q%8
        q = q//8
        base8 += str(r)
    for i in range (1,len(base8),1) :
        base8 = base8[i]+base8[0:i]+base8[i+1:len(base8)]

# base 16 / hexadécimal
if nb == 0 :
    base16 = "0"
else :
    base16 = ""
    lnb = "0123456789ABCDEF"
    r = 0
    q = nb
    while not q == 0 :
        r = q%16
        q = q//16
        base16 += lnb[r]
    for i in range (1,len(base16),1) :
        base16 = base16[i]+base16[0:i]+base16[i+1:len(base16)]

# Ascii
ascii =""
for i in range (len(str(nb))) :
    ascii += "3"+str(nb)[i]

# Morse
encode_morse = ["-----","•----","••---","•••--","••••-","•••••","-••••","--•••","---••","----•"]
morse = ""
for i in range (len(str(nb))) :
    morse += encode_morse[int(str(nb)[i])]

# Jour de l'année
jour1 = ""
if not nb > 365 :
    mois = ["Janvier",31,"Février",28,"Mars",31,"Avril",30,"Mai",31,"Juin",30,"Juillet",31,"Août",31,"Septembre",30,"Octobre",31,"Novembre",30,"Décembre",31]
    nb2 = nb
    i = 1
    while nb2 > 0 :
        if nb2-mois[i] > 0 :
            nb2 -= mois[i]
        else :
            jour1 = str(nb2)+" "+mois[i-1]
            nb2 = 0
        i += 2

jour2 = ""
if not nb > 365 :
    mois = ["Janvier",31,"Février",29,"Mars",31,"Avril",30,"Mai",31,"Juin",30,"Juillet",31,"Août",31,"Septembre",30,"Octobre",31,"Novembre",30,"Décembre",31]
    nb2 = nb
    i = 1
    while nb2 > 0 :
        if nb2-mois[i] > 0 :
            nb2 -= mois[i]
        else :
            jour2 = str(nb2)+" "+mois[i-1]
            nb2 = 0
        i += 2

# Triangulaire ?
liste_triangulaires = [1]
cote = 1
while liste_triangulaires[-1] < nb :
    cote += 1
    liste_triangulaires += [liste_triangulaires[-1]+cote]

# Carré parfait ?
liste_carres = [0]
cote = 0
while liste_carres[-1] < nb :
    cote += 1
    liste_carres += [cote**2]

# Pentagonal ?
liste_pentagonaux = [1]
cote = 1
while liste_pentagonaux[-1] < nb :
    cote += 1
    liste_pentagonaux += [liste_pentagonaux[-1]+cote*2+(cote-2)]

# Hexagonal ?
liste_hexagonaux = [1]
cote = 0
while liste_hexagonaux[-1] < nb :
    cote += 1
    liste_hexagonaux += [liste_hexagonaux[-1]+cote*6-(len(liste_hexagonaux)-1)*2-1]

# Heptagonal ?
liste_heptagonaux = [1]
cote = 0
while liste_heptagonaux[-1] < nb :
    cote += 1
    liste_heptagonaux += [liste_heptagonaux[-1]+cote*7-(len(liste_heptagonaux)-1)*2-1]

# Octogonal ?
liste_octogonaux = [1]
cote = 0
while liste_octogonaux[-1] < nb :
    cote += 1
    liste_octogonaux += [liste_octogonaux[-1]+cote*8-(len(liste_octogonaux)-1)*2-1]

# Ennéagonal ?
liste_enneagonaux = [1]
cote = 0
while liste_enneagonaux[-1] < nb :
    cote += 1
    liste_enneagonaux += [liste_enneagonaux[-1]+cote*9-(len(liste_enneagonaux)-1)*2-1]

# Décagonal ?
liste_decagonaux = [1]
cote = 0
while liste_decagonaux[-1] < nb :
    cote += 1
    liste_decagonaux += [liste_decagonaux[-1]+cote*10-(len(liste_decagonaux)-1)*2-1]

# Triangulaire centré ?
liste_triangulaires_centre = [1]
cote = 0
while liste_triangulaires_centre[-1] < nb :
    cote += 1
    liste_triangulaires_centre += [liste_triangulaires_centre[-1]+cote*3]

# Carré centré ?
liste_carres_centre = [1]
cote = 0
while liste_carres_centre[-1] < nb :
    cote += 1
    liste_carres_centre += [liste_carres_centre[-1]+cote*4]

# Pentagonal centré ?
liste_pentagonaux_centre = [1]
cote = 0
while liste_pentagonaux_centre[-1] < nb :
    cote += 1
    liste_pentagonaux_centre += [liste_pentagonaux_centre[-1]+cote*5]

# Hexagonal centré ou étoilé ?
liste_hexagonaux_centre = [1]
liste_etoile = [1]
cote = 1
while liste_hexagonaux_centre[-1] < nb :
    liste_hexagonaux_centre += [cote*6+liste_hexagonaux_centre[-1]]
    if liste_etoile[-1] < nb :
        total_triangle = 0
        for i in range (1,cote+1,1) :
            total_triangle += i
        liste_etoile += [liste_hexagonaux_centre[-1]+total_triangle*6]
    cote += 1

# Heptagonal centré ?
liste_heptagonaux_centre = [1]
cote = 0
while liste_heptagonaux_centre[-1] < nb :
    cote += 1
    liste_heptagonaux_centre += [liste_heptagonaux_centre[-1]+cote*7]

# Octogonal centré ?
liste_octogonaux_centre = [1]
cote = 0
while liste_octogonaux_centre[-1] < nb :
    cote += 1
    liste_octogonaux_centre += [liste_octogonaux_centre[-1]+cote*8]

# Ennéagonal centré ?
liste_enneagonaux_centre = [1]
cote = 0
while liste_enneagonaux_centre[-1] < nb :
    cote += 1
    liste_enneagonaux_centre += [liste_enneagonaux_centre[-1]+cote*9]

# Décagonal centré ?
liste_decagonaux_centre = [1]
cote = 0
while liste_decagonaux_centre[-1] < nb :
    cote += 1
    liste_decagonaux_centre += [liste_decagonaux_centre[-1]+cote*10]

# Polygonal
total_polygonaux = 0
liste_polygonaux = liste_triangulaires + liste_carres + liste_pentagonaux + liste_hexagonaux + liste_heptagonaux + liste_octogonaux + liste_enneagonaux + liste_decagonaux
for i in range (1,nb+1,1) :
    for j in range (len(liste_polygonaux)) :
        if liste_polygonaux[j] == i :
            total_polygonaux += 1
            break

# Polygonal centré
total_polygonaux_centre = 0
liste_polygonaux_centre = liste_triangulaires_centre + liste_carres_centre + liste_pentagonaux_centre + liste_hexagonaux_centre + liste_heptagonaux_centre + liste_octogonaux_centre + liste_enneagonaux_centre + liste_decagonaux_centre
for i in range (1,nb+1,1) :
    for j in range (len(liste_polygonaux_centre)) :
        if liste_polygonaux_centre[j] == i :
            total_polygonaux_centre += 1
            break


print()
print("Propriétés de",nb,":")
print()

if liste_premiers[-1] == nb and nb == 2 :
    print(str(len(liste_premiers))+"er nombre premier")
elif liste_premiers[-1] == nb :
    print(str(len(liste_premiers))+"e nombre premier")
elif nb > 1 :
    total = 0
    for i in range (len(liste_premiers)-1) :
        total += liste_premiers[i+1] - liste_premiers[i] - 1
    total += nb - liste_premiers[-1]
    if total == 1 :
        print("1er nombre composé")
    else :
        print(str(total)+"e nombre composé")

    oui = 0
    for i in range (len(liste_premiers)) :
        for j in range (len(liste_premiers)) :
            if liste_premiers[i] * liste_premiers[j] == nb :
                oui = 1

    if oui == 1 :
        total = 0
        for i in range (nb) :
            for j in range (len(liste_premiers)) :
                for k in range (len(liste_premiers)) :
                    if liste_premiers[j] * liste_premiers[k] == i :
                        total += 1

        if total == 0 :
            print("1er nombre semi-premier")
        else :
            print(str(total+1)+"e nombre semi-premier")

if couple == 1 :
    print(nb,"forme un couple de nombres premiers jumeaux avec",nb-2)
elif couple == 2 :
    print(nb,"forme un couple de nombres premiers jumeaux avec",nb+2)

if not nb == 0 and not nb == 1 :
    mess = str(decomp[-1])
    for i in range (2,len(decomp)+1,1) :
        mess += " * "+str(decomp[-i])
    print("La décomposotion en facteurs premiers de",nb,"est :",mess)

if not nb == 0 and not nb == 1 :
    mess = str(liste_diviseurs[0])
    for i in range (1,len(liste_diviseurs)-1,1) :
        mess += ", "+str(liste_diviseurs[i])
    mess += " et "+str(liste_diviseurs[-1])
    print(nb,"a",len(liste_diviseurs),"diviseurs qui sont :",mess)
elif nb == 1 :
    print(nb,"a",len(liste_diviseurs),"diviseur qui est :",nb)

print("La factorielle de",nb,"est :",factorielle)

if liste_fibonacci[-1] == nb and nb == 1 :
    print("1er et 2e nombre de Fibonacci")
elif liste_fibonacci[-1] == nb :
    print(str(liste_fibonacci[-1])+"e nombre de Fibonacci")

print()

print("Base 2 (binaire) :",binaire)
print("Base 8 :",base8)
print("Base 16 (hexadécimal) :",base16)
print("Ascii :",ascii)
print("Morse :",morse)

print()

if nb <= 118 and nb > 0 :
    liste_elements = ["Hydrogène","Hélium","Lithium","Béryllium","Bore","Carbone","Azote","Oxygène","Fluor","Néon","Sodium","Magnésium","Aluminium","Silicium","Phosphore","Soufre","Chlore","Argon","Potassium","Calcium","Scandium","Titane","Vanadium","Chrome","Mangasène","Fer","Cobalt","Nickel","Cuivre","Zinc","Gallium","Germanium","Arsenic","Sélénium","Brome","Krypton","Rubidium","Strontium","Yttrium","Zirconium","Niobium","Molybdène","Technétium","Ruthénium","Rhodium","Palladium","Argent","Cadmin","Indium","Etain","Antimoine","Tellure","Iode","Xénon","Césium","Baryum","Lanthane","Cérium","Praséodyme","Néodyme","Prométhium","Samarium","Europium","Gadolinium","Terbium","Dysprosium","Holmium","Erbium","Thulium","Ytterbium","Lutétium","Hafnium","Tantale","Tungstène","Rhénium","Osmium","Iridium","Platine","Or","Mercure","Thallium","Plomb","Bismuth","Polonium","Astate","Radon","Francium","Radium","Actinium","Thorium","Protactinium","Uranium","Neptunium","Plutonium","Américium","Curium","Berkélium","Californium","Einsteinium","Fermium","Mendélévium","Nobélium","Lawrencium","Rutherfordium","Dubnium","Seaborgium","Bohrium","Hassium","Meitnerium","Darmstadtium","Roentgenium","Copernicium","Ununtrium","Flérovium","Ununpentium","Livermorium","Ununseptium","Ununoctium"]
    if liste_elements[nb-1][0] == "H" or liste_elements[nb-1][0] == "A" or liste_elements[nb-1][0] == "E" or liste_elements[nb-1][0] == "I" or liste_elements[nb-1][0] == "O" or liste_elements[nb-1][0] == "U" or liste_elements[nb-1][0] == "Y" :
        print("numéro atomique de l'"+str(liste_elements[nb-1]))
    else :
        print("numéro atomique du",liste_elements[nb-1])

if nb == 1 :
    print(str(nb)+"er jour de l'année lors d'une année normale :",jour1)
    print(str(nb)+"er jour de l'année lors d'une année bissextile :",jour2)
else :
    if not jour1 == "" :
        print(str(nb)+"e jour de l'année lors d'une année normale :",jour1)
    if not jour2 == "" :
        print(str(nb)+"e jour de l'année lors d'une année bissextile :",jour2)

print()

oui = 0
if liste_triangulaires[-1] == nb and nb == 1 :
    print(str(len(liste_triangulaires))+"er nombre triangulaire")
    oui = 1
elif liste_triangulaires[-1] == nb :
    print(str(len(liste_triangulaires))+"e nombre triangulaire")
    oui = 1

if liste_carres[-1] == nb and nb == 0 :
    print(str(len(liste_carres))+"er carré parfait")
    oui = 1
elif liste_carres[-1] == nb :
    print(str(len(liste_carres))+"e carré parfait")
    oui = 1

if liste_pentagonaux[-1] == nb and nb == 1 :
    print(str(len(liste_pentagonaux))+"er nombre pentagonal")
    oui = 1
elif liste_pentagonaux[-1] == nb :
    print(str(len(liste_pentagonaux))+"e nombre pentagonal")
    oui = 1

if liste_hexagonaux[-1] == nb and nb == 1 :
    print(str(len(liste_hexagonaux))+"er nombre hexagonal")
    oui = 1
elif liste_hexagonaux[-1] == nb :
    print(str(len(liste_hexagonaux))+"e nombre hexagonal")
    oui = 1

if liste_heptagonaux[-1] == nb and nb == 1 :
    print(str(len(liste_heptagonaux))+"er nombre heptagonal")
    oui = 1
elif liste_heptagonaux[-1] == nb :
    print(str(len(liste_heptagonaux))+"e nombre heptagonal")
    oui = 1

if liste_octogonaux[-1] == nb and nb == 1 :
    print(str(len(liste_octogonaux))+"er nombre octogonal")
    oui = 1
elif liste_octogonaux[-1] == nb :
    print(str(len(liste_octogonaux))+"e nombre octogonal")
    oui = 1

if liste_enneagonaux[-1] == nb and nb == 1 :
    print(str(len(liste_enneagonaux))+"er nombre ennéagonal")
    oui = 1
elif liste_enneagonaux[-1] == nb :
    print(str(len(liste_enneagonaux))+"e nombre ennéagonal")
    oui = 1

if liste_decagonaux[-1] == nb and nb == 1 :
    print(str(len(liste_decagonaux))+"er nombre décagonal")
    oui = 1
elif liste_decagonaux[-1] == nb :
    print(str(len(liste_decagonaux))+"e nombre décagonal")
    oui = 1

if oui == 1 :
    if total_polygonaux == 1 :
        print("1er nombre polygonal")
    else :
        print(str(total_polygonaux)+"e nombre polygonal")

print()

oui = 0
if liste_triangulaires_centre[-1] == nb and nb == 1 :
    print(str(len(liste_triangulaires_centre))+"er nombre triangulaire centré")
    oui = 1
elif liste_triangulaires_centre[-1] == nb :
    print(str(len(liste_triangulaires_centre))+"e nombre triangulaire centré")
    oui = 1

if liste_carres_centre[-1] == nb and nb == 1 :
    print(str(len(liste_carres_centre))+"er nombre carré centré")
    oui = 1
elif liste_carres_centre[-1] == nb :
    print(str(len(liste_carres_centre))+"e nombre carré centré")
    oui = 1

if liste_pentagonaux_centre[-1] == nb and nb == 1 :
    print(str(len(liste_pentagonaux_centre))+"er nombre pentagonal centré")
    oui = 1
elif liste_pentagonaux_centre[-1] == nb :
    print(str(len(liste_pentagonaux_centre))+"e nombre pentagonal centré")
    oui = 1

if liste_hexagonaux_centre[-1] == nb and nb == 1 :
    print(str(len(liste_hexagonaux_centre))+"er nombre hexagonal centré")
    oui = 1
elif liste_hexagonaux_centre[-1] == nb :
    print(str(len(liste_hexagonaux_centre))+"e nombre hexagonal centré")
    oui = 1

if liste_heptagonaux_centre[-1] == nb and nb == 1 :
    print(str(len(liste_heptagonaux_centre))+"er nombre heptagonal centré")
    oui = 1
elif liste_heptagonaux_centre[-1] == nb :
    print(str(len(liste_heptagonaux_centre))+"e nombre heptagonal centré")
    oui = 1

if liste_octogonaux_centre[-1] == nb and nb == 1 :
    print(str(len(liste_octogonaux_centre))+"er nombre octogonal centré")
    oui = 1
elif liste_octogonaux_centre[-1] == nb :
    print(str(len(liste_octogonaux_centre))+"e nombre octogonal centré")
    oui = 1

if liste_enneagonaux_centre[-1] == nb and nb == 1 :
    print(str(len(liste_enneagonaux_centre))+"er nombre ennéagonal centré")
    oui = 1
elif liste_enneagonaux_centre[-1] == nb :
    print(str(len(liste_enneagonaux_centre))+"e nombre ennéagonal centré")
    oui = 1

if liste_decagonaux_centre[-1] == nb and nb == 1 :
    print(str(len(liste_decagonaux_centre))+"er nombre décagonal centré")
    oui = 1
elif liste_decagonaux_centre[-1] == nb :
    print(str(len(liste_decagonaux_centre))+"e nombre décagonal centré")
    oui = 1

if liste_etoile[-1] == nb and nb == 1 :
    print(str(len(liste_etoile))+"er nombre étoilé")
    oui = 1
elif liste_etoile[-1] == nb :
    print(str(len(liste_etoile))+"e nombre étoilé")
    oui = 1

if oui == 1 :
    if total_polygonaux_centre == 1 :
        print("1er nombre polygonal centré")
    else :
        print(str(total_polygonaux_centre)+"e nombre polygonal centré")

input("\nPause...")
