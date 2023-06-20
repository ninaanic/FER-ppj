from sys import exit
# procitaj sa stdin
ulaz = []   # lista lista 
while True:
    try: 
        line = input()
        line = line.split()
        if line:
            ulaz.append(line)
        else: 
            break
    except EOFError:
        break # dosli smo do kraja file-a

#print(ulaz)

# micanje nepotrebnih stvari iz ulaza
ulaz.remove(['<program>'])
while ['<lista_naredbi>'] in ulaz:
    ulaz.remove(['<lista_naredbi>'])
while ['<naredba>'] in ulaz:
    ulaz.remove(['<naredba>'])
while ['<E>'] in ulaz:
    ulaz.remove(['<E>'])
while ['<T>'] in ulaz:
    ulaz.remove(['<T>'])
while ['<P>'] in ulaz:
    ulaz.remove(['<P>'])
while ['<T_lista>'] in ulaz:
    ulaz.remove(['<T_lista>'])
while ['<E_lista>'] in ulaz:
    ulaz.remove(['<E_lista>'])
while ['$'] in ulaz:
    ulaz.remove(['$'])

ulaz.append(['$']) # kraj 


# napravit 3 liste lista: inic glob var, inic lok var, kor var
inic_glob = []
kor = []

pomocna = []
pomocna2 = []
pomocna3 = []

def dodaj_u_lok(var):
    global broj_redaka

    pomocna2.append(var)
    pomocna2.append(broj_redaka)
    inic_lok.append(pomocna2[:])
    pomocna2.clear()

def popuni_inic_glob(pomocna):
    global broj_redaka

    if (len(inic_glob) > 0):
        for k in range (0, len(inic_glob)):
            if (pomocna[0][2] == inic_glob[k][0] and broj_redaka != inic_glob[k][1]):
                inic_glob[k][1] = broj_redaka
                return

    pomocna2.append(pomocna[0][2])
    pomocna2.append(broj_redaka)
    inic_glob.append(pomocna2[:])
    pomocna2.clear()

def popuni_inic_lok(pomocna):
    global broj_redaka

    if (len(inic_lok) > 0):
        for k in range (0, len(inic_lok)):
            if (pomocna[0][2] == inic_lok[k][0] and broj_redaka != inic_lok[k][1]):
                inic_lok[k][1] = broj_redaka
                return

    if (pomocna[0][2] == 'za'):
        pomocna2.append(pomocna[1][2])
        pomocna2.append(broj_redaka)
        inic_lok.append(pomocna2[:])
        pomocna2.clear()

    else:
        pomocna2.append(pomocna[0][2])
        pomocna2.append(broj_redaka)
        inic_lok.append(pomocna2[:])
        pomocna2.clear()
    
def popuni_kor_lok(pomocna, j):
    global broj_redaka

    koristi_lok = 0

    if (len(inic_lok) > 0):
        for k in range (0, len(inic_lok)):
            if (pomocna[j][2] == inic_lok[k][0]):
                pomocna3.append(broj_redaka)
                pomocna3.append(inic_lok[k][1])
                pomocna3.append(pomocna[j][2])
                koristi_lok = 1

    if (koristi_lok == 0):
        popuni_kor_glob(pomocna, j)

    else:
        print(' '.join(map(str, pomocna3[:])))
        kor.append(pomocna3[:])
        pomocna3.clear()

def popuni_kor_glob(pomocna, j):

    global broj_redaka

    pomocna3.append(broj_redaka)
    for k in range (0, len(inic_glob)):
        if (pomocna[j][2] == inic_glob[k][0]):
            pomocna3.append(inic_glob[k][1])
    pomocna3.append(pomocna[j][2])

    print(' '.join(map(str, pomocna3[:])))
    kor.append(pomocna3[:])
    pomocna3.clear()

def provjeri_jel_kor_inic_lok(pomocna, j):
    for k in range (0, len(inic_lok)):
        if (pomocna[j][2] == inic_lok[k][0]):
            return True
                
    return False

def provjeri_jel_kor_inic_glob(pomocna, j):
    for k in range (0, len(inic_glob)):
        if (pomocna[j][2] == inic_glob[k][0]):
            return True
                
    return False

def pridruzi_izvan_za(ulaz):
    global broj_redaka
    i = 0

    while (len(ulaz[i]) > 1 and ulaz[i][1] == str(broj_redaka)):
        pomocna.append(ulaz[i])
        ulaz.remove(ulaz[i])

    samo_koristenje = 1
    for j in range(1, len(pomocna)):
        if (pomocna[0][2] == pomocna[j][2]):
            samo_koristenje = 0
    
    if (samo_koristenje == 1):
        popuni_inic_glob(pomocna)
            
    if (len(pomocna) >= 3):
        je_inic = 0

        for j in range(2, len(pomocna)):
            if (pomocna[j][2].isalpha()):
                for k in range (0, len(inic_glob)):
                    if (pomocna[j][2] == inic_glob[k][0]):
                        popuni_kor_glob(pomocna, j)
                        je_inic = 1

                if (je_inic == 0):
                    print('err', broj_redaka, pomocna[j][2])
                    exit()
        
    pomocna.clear()

def pridruzi_unutar_za(pom):
    global broj_redaka
    i = 0

    if (len(pom[i]) == 1):
        pom.remove(pom[0])

    while (len(pom[i]) > 1 and pom[i][1] == str(broj_redaka)):
        pomocna.append(pom[i])
        pom.remove(pom[i])

    if (pomocna[0][2] == 'za'):
        for j in range(2, len(pomocna)):
            if (pomocna[1][2] == pomocna[j][2]):
                print('err', broj_redaka, pomocna[1][2])
                exit()

        # TODO dodaj inic lok za var izmedu za i od
        dodaj_u_lok(pomocna[1][2])

        # TODO provjerit dal ovo dobro dodaje ili treba nap novu fju za elem izmdeu za i od i nakon od i do
        if (len(pomocna) == 6):
            if (pomocna[3][2].isalpha()):
                if (provjeri_jel_kor_inic_lok(pomocna, 3) == True):
                    popuni_kor_lok(pomocna, 3)
                elif (provjeri_jel_kor_inic_glob(pomocna, 3) == True):
                    popuni_kor_glob(pomocna, 3)
                else:
                    print('err', broj_redaka, pomocna[3][2])
                    exit()

            if (pomocna[5][2].isalpha()):
                if (provjeri_jel_kor_inic_lok(pomocna, 5) == True):
                    popuni_kor_lok(pomocna, 5)
                elif (provjeri_jel_kor_inic_glob(pomocna, 5) == True):
                    popuni_kor_glob(pomocna, 5)
                else:
                    print('err', broj_redaka, pomocna[5][2])
                    exit()
        else:
            for j in range(3, len(pomocna)):
                if (pomocna[j][2].isalpha() and pomocna[j][2] != 'od' and pomocna[j][2] != 'do'):
                    if (provjeri_jel_kor_inic_lok(pomocna, j) == True):
                        popuni_kor_lok(pomocna, j)
                    elif (provjeri_jel_kor_inic_glob(pomocna, j) == True):
                        popuni_kor_glob(pomocna, j)
                    else:
                        print('err', broj_redaka, pomocna[j][2])
                        exit()

    else:
        samo_koristenje = 1
        for j in range(1, len(pomocna)):
            if (pomocna[0][2] == pomocna[j][2]):
                samo_koristenje = 0
        
        if (samo_koristenje == 1):
            popuni_inic_lok(pomocna)
     
        if (len(pomocna) >= 3):
            for j in range(2, len(pomocna)):
                je_inic = 0
                kor_lok = 0

                if (pomocna[j][2].isalpha()):
                    for k in range (0, len(inic_lok)):
                        if (pomocna[j][2] == inic_lok[k][0]):
                            popuni_kor_lok(pomocna, j)
                            je_inic = 1
                            kor_lok = 1

                    if (kor_lok == 0):
                        for k in range (0, len(inic_glob)):
                            if (pomocna[j][2] == inic_glob[k][0]):
                                popuni_kor_glob(pomocna, j)
                                je_inic = 1

                    if (je_inic == 0):
                        print('err', broj_redaka, pomocna[j][2])
                        exit()
            
    pomocna.clear()

def za_petlja(ulaz):
    global broj_redaka

    br_za = 0
    br_az = 0
    pom = []
    ok = True

    while(ok):
        if (ulaz[0][0] == 'KR_ZA'):
            br_za += 1

        elif (ulaz[0][0] == 'KR_AZ'):
            br_az += 1

        if (br_za != br_az):
            pom.append(ulaz[0])
            ulaz.remove(ulaz[0])
        
        else:
            ok = False

    pom.append(ulaz[0])
    ulaz.remove(ulaz[0])

    mini = int(pom[0][1])
    maxi = int(pom[len(pom)-1][1])

    for br_red in range(mini, maxi+1):
        if (pom[0][0] == 'KR_AZ'):
            broj_redaka += 1
            pom.remove(pom[0])

        else:
            broj_redaka = br_red
            pridruzi_unutar_za(pom)



broj_redaka = 1
while (ulaz):
    if (ulaz[0] == ['<naredba_pridruzivanja>']):
        ulaz.remove(ulaz[0])
        pridruzi_izvan_za(ulaz)

    elif (ulaz[0] == ['<za_petlja>']):
        inic_lok = []
        ulaz.remove(ulaz[0])
        za_petlja(ulaz)

    elif (ulaz[0] == ['$']):
        ulaz.remove(ulaz[0])
        break

    broj_redaka += 1

#print()
#print()
#print('inic_glob:', inic_glob)

#print()
#print()
#print('inic_lok:', inic_lok)

#print()
#print()
#print('kor:', kor)




# 2t
# test 14, 15 ne radi 
# test 16,17,18,19 provjerit 