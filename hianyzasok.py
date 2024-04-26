lista=[]
segedlistaStr=[]
segedlistaInt=[]
with open("hiányzások.txt", "r", encoding="UTF-8") as fin:
    for sor in fin:
        segedlistaStr=sor.strip().split(",")
        for szamStr in segedlistaStr:
            segedlistaInt.append(int(szamStr))
        lista.append(segedlistaInt)
        segedlistaInt=[]
print(lista)