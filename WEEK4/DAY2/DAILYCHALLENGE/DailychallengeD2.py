date = input("Enter your date of birth")
[jj, mm, aa] = date.split("/")
j, m, a = int(jj), int(mm), int(aa)
nb_j = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
age = 2020 - a
B = tuple(str(age))
c = len(B)
d = B[c-1]
e = int(d)
f = (e * "i")
annee = int(a)
bissextile = False
if annee % 400 == 0:
    bissextile = True
elif annee % 100 == 0:
    bissextile = False
elif annee % 4 == 0:
    bissextile = True
if bissextile:
    print(f"    ____{f}____ ")
    print("   | :H:a:p:p:y: | ")
    print("  _|_____________|_ ")
    print(" |^^^^^^^^^^^^^^^^^|")
    print(" |:B:i:r:t:h:d:a:y:|")
    print(" |                 |")
    print(" ~~~~~~~~~~~~~~~~~~~")
    print("")
    print(f"    ____{f}____ ")
    print("   | :H:a:p:p:y: | ")
    print("  _|_____________|_ ")
    print(" |^^^^^^^^^^^^^^^^^|")
    print(" |:B:i:r:t:h:d:a:y:|")
    print(" |                 |")
    print(" ~~~~~~~~~~~~~~~~~~~")
else:
    print(f"    ____{f}____ ")
    print("   | :H:a:p:p:y: | ")
    print("  _|_____________|_ ")
    print(" |^^^^^^^^^^^^^^^^^|")
    print(" |:B:i:r:t:h:d:a:y:|")
    print(" |                 |")
    print(" ~~~~~~~~~~~~~~~~~~~")