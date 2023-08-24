lista=[
    
]
quant_linhas= 3
quant_col=2
for i in range(0,quant_linhas,1):
    linha=[]
    for j in range(0,quant_col,1): 
        valor= input(f"Digite um valor[{i}][{j}]: ")
        linha.append(valor)
    lista.append(linha[:]) #joga os valores na primeira lista ( sem [:] jogaria apenas uma apresentacao dos valores)
print(lista)
linha[1]= 333
print(lista[1])