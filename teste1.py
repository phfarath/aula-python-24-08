#matriz-5x2 - o usuario digita o nome e o estado depois printa as pessoas que nasceram no msm estado
matriz=[

]
quant_linhas= 5
quant_col=2
for i in range(0,quant_linhas,1):
    linha=[]
    for j in range(0,quant_col,1): 
        valor= input(f"Digite um nome e um estado de nascença: ")
        linha.append(valor)
    matriz.append(linha[:]) 
print(matriz)
print("Escolha um estado br: ")
estado= input().lower()
for i in range(0,len(matriz),1):
    if matriz[i][1] == estado:
        print(matriz[i][0])
