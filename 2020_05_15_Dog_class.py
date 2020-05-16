# João, Robenildo, Victor, Marcos

# Programa que verifica quem é o cachorro mais velho
class Dog:
  def __init__(self, nome, idade):
    self.nome = nome  
    self.idade = idade
    
  def __str__(self):
    return self.nome+" "+str(self.idade)

def mais_velho(lista):
  '''
    Em caso de empate, retorna o primeiro
  '''
  velho = lista[0]
  for i in lista:
    if velho.idade < i.idade:
      velho = i
  return velho

n = int(input("Entre com o número de cachorros: "))
lista = [] 

for i in range(n):
  cachorro = Dog(input("Digite o nome do cachorro: "), int(input("Digite a idade do cachorro: ")))
  lista.append(cachorro)

dog_older = mais_velho(lista)
print(f"O cachorro mais velho é: {dog_older.nome} com {dog_older.idade} anos.")

