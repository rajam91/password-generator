from random import randint, choice

alpha_min = [ chr(i) for i in range(97,123) ]
alpha_maj = [ chr(i) for i in range(65,91) ]
chiffres = [ chr(i) for i in range(48,58) ]
caractere_speciaux = [ '&', '$', '%', '§', '@', '#', '_', '-' ]

def password(n,min = True, maj= True, chif= True, cs= True):
    alphabets = dict()
    key = 0
    if min:
        alphabets[key] = alpha_min
        key += 1
    if maj:
        alphabets[key] = alpha_maj
        key += 1
    if chif:
        alphabets[key] = chiffres
        key +=1
    if cs:
        alphabets[key] = caractere_speciaux
        key += 1
    
    mdp = ''
    for i in range(n):
        clef = randint(0,key - 1)
        mdp += choice(alphabets[clef])
    return mdp
print(password(5))