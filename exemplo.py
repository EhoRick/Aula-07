produto = "Mouse Gamer Wifi"
valores = [20, 71, 100, 30]
alunos = ["Ana", "Hugo", "Mariana", "Pedro", "Ana Paula"]

if "mouse".lower() in produto.lower():
    print ("Produto encontrado")

else:
    print ("Produto não encontrado")

def dobrar(valor):
    resultado = valor * 2
    return resultado
 
print(dobrar (11))
    
valores_novos = []

for item in valores:
    valores_novos.append (dobrar(item))

print (valores_novos)

aluno_procurado = input("Digite um nome: ")
alunos_encontrados = []

for item in alunos: 
    if aluno_procurado.lower() in item.lower():
        print (item)

    alunos_encontrados.append (item)

print (alunos_encontrados)