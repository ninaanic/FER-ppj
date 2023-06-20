import os
import sys

# procitaj sa stdin
ulaz = []
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


# fje, za svaki prijelaz svoja (pomocu PRIMIJENI)
def E_lista(ulaz, f, broj_razmaka):
    global i 

    f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz='<E_lista>\n'))
    broj_razmaka += 1

    try:
        if (ulaz[i][0] == 'OP_PLUS' or ulaz[i][0] == 'OP_MINUS'):
            redak = ' '.join(ulaz[i])
            f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz=redak + '\n'))

            i += 1
            E(ulaz, f, broj_razmaka)

        else:
            f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz='$\n'))

    except:
        f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz='$\n'))
        return
        
    return  

def T_lista(ulaz, f, broj_razmaka):
    global i 

    f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz='<T_lista>\n'))
    broj_razmaka += 1

    try:
        if (ulaz[i][0] == 'OP_PUTA' or ulaz[i][0] == 'OP_DIJELI'):
            redak = ' '.join(ulaz[i])
            f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz=redak + '\n'))

            i += 1
            T(ulaz, f, broj_razmaka)
    
        else:
            f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz='$\n'))

    except:
        f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz='$\n'))
        return

    return 

def P(ulaz, f, broj_razmaka):
    global i 

    f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz='<P>\n'))
    broj_razmaka += 1

    if (ulaz[i][0] == 'IDN' or ulaz[i][0] == 'BROJ'):
        redak = ' '.join(ulaz[i])
        f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz=redak + '\n'))

        i += 1  
        

    elif (ulaz[i][0] == 'OP_PLUS' or ulaz[i][0] == 'OP_MINUS'):
        redak = ' '.join(ulaz[i])
        f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz=redak + '\n'))

        i += 1
        if (i == len(ulaz)):
            sys.exit('err kraj')
        P(ulaz, f, broj_razmaka)

    elif (ulaz[i][0] == 'L_ZAGRADA'):
        redak = ' '.join(ulaz[i])
        f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz=redak + '\n'))

        i += 1
        if (i == len(ulaz)):
            sys.exit('err kraj')

        E(ulaz, f, broj_razmaka)

        if (ulaz[i][0] == 'D_ZAGRADA'):
            redak = ' '.join(ulaz[i])
            f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz=redak + '\n'))
        
        i += 1

    else:
        redak = ' '.join(ulaz[i])
        sys.exit('err ' + redak)

    return 

def T(ulaz, f, broj_razmaka):
    global i 

    f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz='<T>\n'))
    broj_razmaka += 1

    P(ulaz, f, broj_razmaka)
    T_lista(ulaz, f, broj_razmaka)    

    return 

def E(ulaz, f, broj_razmaka):
    global i 

    f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz='<E>\n'))
    broj_razmaka += 1

    T(ulaz, f, broj_razmaka)
    E_lista(ulaz, f, broj_razmaka)

    return 

def naredba_pridruzivanja(ulaz, f, broj_razmaka):
    global i

    f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz='<naredba_pridruzivanja>\n'))
    broj_razmaka += 1
    redak = ' '.join(ulaz[i])
    f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz=redak + '\n'))

    i += 1
    if (i == len(ulaz)):
        sys.exit('err kraj')

    else:
        if (ulaz[i][0] == 'OP_PRIDRUZI'):
            redak = ' '.join(ulaz[i])
            f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz=redak + '\n'))

            i += 1
            if (i == len(ulaz)):
                sys.exit('err kraj')

            E(ulaz, f, broj_razmaka)

        else:
            redak = ' '.join(ulaz[i])
            sys.exit('err ' + redak)
        
    return

def za_petlja(ulaz, f, broj_razmaka):
    global i 

    f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz='<za_petlja>\n'))
    broj_razmaka += 1

    if (ulaz[i][0] == 'KR_ZA'):
        redak = ' '.join(ulaz[i])
        f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz=redak + '\n'))

        i += 1
        if (i == len(ulaz)):
            redak = ' '.join(ulaz[i-1])
            sys.exit('err ' + redak)

        else: 
            if (ulaz[i][0] == 'IDN'):   
                redak = ' '.join(ulaz[i])
                f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz=redak + '\n'))

                i += 1
                if (i == len(ulaz)):
                    redak = ' '.join(ulaz[i-1])
                    sys.exit('err ' + redak)

                else:
                    if (ulaz[i][0] == 'KR_OD'):
                        redak = ' '.join(ulaz[i])
                        f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz=redak + '\n'))

                        i += 1
                        if (i == len(ulaz)):
                            redak = ' '.join(ulaz[i-1])
                            sys.exit('err ' + redak)

                        else:
                            E(ulaz, f, broj_razmaka)
                            
                            if (ulaz[i][0] == 'KR_DO'):
                                redak = ' '.join(ulaz[i])
                                f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz=redak + '\n'))

                                i += 1
                                if (i == len(ulaz)):
                                    redak = ' '.join(ulaz[i-1])
                                    sys.exit('err ' + redak)
                                
                                else:
                                    E(ulaz, f, broj_razmaka)
                                    lista_naredbi(ulaz, f, broj_razmaka) # tu padnemo 

                                    if (ulaz[i][0] == 'KR_AZ'):
                                        redak = ' '.join(ulaz[i])
                                        f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz=redak + '\n'))

                                        i += 1

                                    else:
                                        redak = ' '.join(ulaz[i])
                                        sys.exit('err ' + redak)  

                            else:
                                redak = ' '.join(ulaz[i])
                                sys.exit('err ' + redak)

                    else:
                        redak = ' '.join(ulaz[i])
                        sys.exit('err ' + redak)

            else:
                redak = ' '.join(ulaz[i])
                sys.exit('err ' + redak)

    else:
        redak = ' '.join(ulaz[i])
        sys.exit('err ' + redak)

    return 

def naredba(ulaz, f, broj_razmaka):
    global i

    f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz='<naredba>\n'))
    broj_razmaka += 1

    if (ulaz[i][0] == 'IDN'):
        naredba_pridruzivanja(ulaz, f, broj_razmaka)
    
    elif (ulaz[i][0] == 'KR_ZA'):
        za_petlja(ulaz, f, broj_razmaka)
    
    else:
        try: 
            redak = ' '.join(ulaz[i])
            sys.exit('err ' + redak)
        except:
            sys.exit('err kraj')

    return 

def lista_naredbi(ulaz, f, broj_razmaka):
    global i 
    f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz='<lista_naredbi>\n'))
    broj_razmaka += 1

    if (i == len(ulaz) or ulaz[i][0] == 'KR_AZ'):
        f.write('{br_razm} {izraz}'.format(br_razm=' '*broj_razmaka, izraz='$\n'))
        return

    else:
        if (ulaz[i][0] == 'IDN' or ulaz[i][0] == 'KR_ZA'):
            naredba(ulaz, f, broj_razmaka)
            lista_naredbi(ulaz, f, broj_razmaka)

        else:
            redak = ' '.join(ulaz[i])
            sys.exit('err ' + redak)

    return

def pocetak():
    global i
    i = 0


# main
f = open("testniFile.txt", "w+") # kreiraj pomocni file u kojem cemo gradit rj i ispisat ga ako nema gresaka 

if (len(ulaz) > 0):
    broj_razmaka = 0
    pocetak()

    f.write("<program>\n")
    lista_naredbi(ulaz, f, broj_razmaka)

else:
    f.write("<program>\n")
    f.write('{br_razm} {izraz}'.format(br_razm=' ', izraz='<lista_naredbi>\n'))
    f.write('{br_razm} {izraz}'.format(br_razm='  ', izraz='$\n'))

f.seek(0)
print(f.read())



os.remove("testniFile.txt") # brisi pomocni file jer inace nam nece dat da ga opet stvorimo kad nanovo pokrenemo program

