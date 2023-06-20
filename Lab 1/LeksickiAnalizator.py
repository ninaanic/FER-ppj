# procitaj sa stdin 
lines = []

# citaj dok ne dobijes naredbu za EOF (naredba: ctrl D)
try:
    while True:
        line = input()
        if line:
            lines.append(line)
except EOFError:
    pass

# fja za provjeru je li cijeli red kom
def provjeriKom(line):
    if (line[0] == '/' and line[1] == '/'):
        return False
    else:
        return True

def formatiraj(string):
    novi = []
    i = 0
    while(i < len(string)):
        pomocna = []

        if ((ord(string[i]) >= 40 and ord(string[i]) <= 43) or ord(string[i]) == 45 or ord(string[i]) == 47 or ord(string[i]) == 61):
            novi.append(string[i])

        else:
            if (string[i].isdigit()):
                pomocna.append(string[i])
                j = i + 1

                while (j < len(string) and string[j].isdigit()):
                    pomocna.append(string[i+1])
                    j += 1
                    i += 1

                broj = ''.join(pomocna)
                novi.append(broj)
            
            elif (string[i].isalpha()):
                pomocna.append(string[i])
                j = i + 1

                while (j < len(string) and string[j].isalnum()):
                    pomocna.append(string[i+1])
                    j += 1
                    i += 1

                idn = ''.join(pomocna)
                novi.append(idn)

        i += 1

    return novi

# leksicki analizator za svaki znak/rijec
def leksickiAnalizator(string):
    # OP_PRIDRUZI
    if (string == '='):
        return 'OP_PRIDRUZI'
    
    # OP_PLUS
    if (string == '+'):
        return 'OP_PLUS'

    # OP_MINUS
    if (string == '-'):
        return 'OP_MINUS'

    # OP_PUTA
    if (string == '*'):
        return 'OP_PUTA'

    # OP_DIJELI
    if (string == '/'):
        return 'OP_DIJELI'

    #L_ZAGRADA
    if (string == '('):
        return 'L_ZAGRADA'

    #D_ZAGRADA
    if (string == ')'):
        return 'D_ZAGRADA'

    #KR_ZA
    if (string == 'za'):
        return 'KR_ZA'

    #KR_OD
    if (string == 'od'):
        return 'KR_OD'

    #KR_DO
    if (string == 'do'):
        return 'KR_DO'

    #KR_AZ
    if (string == 'az'):
        return 'KR_AZ'

    # BROJ
    if (string.isdigit()):
        return 'BROJ' 

    # IDN
    if (string.isalnum()):
        return 'IDN'


# main
brojacRedova = 0
for line in lines:

    brojacRedova += 1
    line = line.strip()

    if (line == '/n'):
        continue

    # provjeri je li cijeli rad komentar, ako da preskoci ga
    if (provjeriKom(line) == False):
        continue

    else:
        # splitaj line po razmacima
        listaStringova = line.split()

        # brisi kom u retcima 
        i = -1
        for string in listaStringova:
            i += 1
            if (string == '//'):
                del listaStringova[i:]
            else:
                continue
        
        #print("Lista stringova: ", listaStringova)
        

        # obradi svaki znak/rijec
        novaLista = []
        for string in listaStringova:

            if (len(string) == 1):
                novaLista.append(string)
            
            else:
                # formatiraj po pravilima opisanim u tekstu zad (BROJ, IDN...)
                novaLista .append(formatiraj(string))

        #print("Nova lista stringova (formatiran): ", novaLista)

        finalnaLista = []
        for listaClanova in novaLista:
            for clan in listaClanova:
                finalnaLista.append(clan)

        #print("Finalan lista: ", finalnaLista)

        for string in finalnaLista:
            unifZnak = leksickiAnalizator(string)
            print(unifZnak, brojacRedova, string)
        
    #print()
            
