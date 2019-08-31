import numpy as np
t = 6
cont = 0
kosegen = np.eye(t,t)
kosegen = np.array(kosegen)
kosegen = kosegen.tolist()
kosegen2 = []
for i in kosegen:
    for j in i:
        kosegen2.append(j)


while True:
    matris1 = np.random.random((t,t))
    matris2 = np.random.random((t,t))
    dif_list = matris1 - matris2
    liste = []

    for i in dif_list:
        for j in i:
            if -0.1 < j < 0.1:
                liste.append(1.)
            else:
                liste.append(0.)

    liste = np.array(liste)
    liste = liste.tolist()

    if liste == kosegen2:
        liste = np.array(liste).reshape(t,t)
        print(liste)
        print("program", cont, "kez calisti ve basardi")
        break
    else:
        cont += 1
        print("program", cont, "kez calisti daha bulamadi")
