#nested list ( lista dentro de lista )
pessoas =[
    ["pedro", "kleber", "julio"],
    ["giorge","michelangelo", "gomes"],
    [18, 42, 3]
]
print(pessoas)
print(type(pessoas))
print(len(pessoas)) #linhas que a lista tem 
print(len(pessoas[1])) #colunas da lista
pessoas[0][1]= " josue"
print(pessoas[0][1])