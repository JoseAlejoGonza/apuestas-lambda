jug=[0,0,0]
lista = [[1,20,10],[1,0,15],[0,8,3],["GANO","PERDIO","GANO"],["PERDIO","GANO","PERDIO"],["PERDIO","GANO","GANO"]]

filtroA1 = filter(lambda x: x, lista[3])
filtroA2 = filter(lambda x: x, lista[4])
filtroA3 = filter(lambda x: x, lista[5])
f1 = list(map(lambda x: x, lista[0]))
f2 = list(map(lambda y: y, lista[1]))
f3 = list(map(lambda z: z, lista[2]))

def filtrar(fil,n):
    if n<len(jug):
        if(fil[n]=="GANO"):
            jug[n]=jug[n]+f1[n]
        else:
            jug[n]=jug[n]-f1[n]
        filtrar(fil,n+1)
        

filtrar(filtroA1,0)

def filtrar2(filt,n):
    if n<len(jug):
        if (filt[n] == "GANO"):
            jug[n] = jug[n] + f2[n]
        else:
            jug[n] = jug[n]- f2[n]
        filtrar2(filt,n+1)

filtrar2(filtroA2,0)

def filtrar3(fi,n):
    if n<len(jug):
        if (fi[n] == "GANO"):
            jug[n] = jug[n] + f3[n]
        else:
            jug[n] = jug[n] - f3[n]
        filtrar3(fi,n+1)
filtrar3(filtroA3,0)

puntaje = [jug[0], jug[1], jug[2]]
print puntaje

f = lambda a,b: a if (a > b) else b
print "Quien gano mas dinero: ",(reduce(f, puntaje))

GANO = lambda c,d: c if (c < d) else d
print "Quien perdio mas dinero: ",(reduce(GANO, puntaje))
