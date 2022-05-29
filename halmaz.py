print("2.feladat:")
def beker():
  a = 0
  szamlalo = 0
  hiba = False
  lista = []
  while hiba == False:
    a = a + 1
    bekeres = input(f"\'A\' halmaz {a}. eleme: ")
    if bekeres == "":
      szamlalo = szamlalo + 1
      hiba = True
    if szamlalo == 1:
        print("'A' halmaz feltöltése befejeződött!")
        l = beker()
        print ("A lista: ", l)
        
    else:
      szam = 0
      while ((szam < len (lista)) and (hiba == False)):
        if lista [szam] == int(bekeres):
          print(f"HIBA! a(z) {bekeres} már benne van a(z) \'A\' halmazban!")
          hiba = True
        szam = szam + 1 
      if (hiba == False):
        lista.append(int(bekeres))
  return lista

print(beker())
