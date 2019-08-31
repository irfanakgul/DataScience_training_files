import numpy as np
import time

start = time.time()
t = 10
satir = 0
sutun = 0
satir2 = satir+1

while True:
    matris1 = np.random.random((t,t))
    matris2 = np.random.random((t,t))
    dif_list = matris1 - matris2
    liste = []
    for elem in dif_list:
        for j in elem:
            if (-0.1 < j < 0.1):
                liste.append(1.0)

            else:
                liste.append(0.0)

    liste = np.array(liste)
    liste = liste.reshape(t,t)


    while True:

        if liste[satir][satir] == liste[satir2][satir2]:
            satir += 1
            print(liste)

        else:
            continue

