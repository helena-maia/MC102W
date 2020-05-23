'''
MC102W - 2020.1
Nomes: Fernando, João, Robenildo
Data: 22/05/2020

Descrição: Exercício sobre herança de classes envolvendo cães e gatos
'''
class Pet:
  ''' Classe de animais de estimação com caracteristicas básicas'''
  
  def __init__(self, nome, idade, desc):
    self.nome = nome
    self.idade = idade
    self.desc = desc

  def __str__(self):
    text = "Nome: " + self.nome + "\n"
    text += "Idade: " + str(self.idade) + "\n"
    text += "Descrição: " + self.desc
    return text


class Dog(Pet):
  '''Dog é uma Sub-classe de Pet com as características de dependência, porte e raça'''
  raca_valida = ["pug", "pastor_alemao", "beagle"]
  
  def __init__(self, nome, idade, desc, dependencia, porte, raca):
    super().__init__(nome, idade, desc)
    self.dependencia = dependencia
    self.porte = porte
    if raca in self.raca_valida:
      self.raca = raca
    else:
      self.raca = "não determinada"
    
  def latir(self):
    print(f"{self.nome} disse: AuAu")
  
  def __str__(self):
    return super().__str__( )\
    + "\n" + "Dependência: " + str(self.dependencia) + "%" \
    + "\n" + "Porte: " + str(self.porte) + "\n"\
    + "Raça: " + str(self.raca)


class Cat(Pet):
  ''' Classe de gatos que recebe atributos da classe Pet, avalia o estado do gato e adiciona seu tipo e comida favorita '''
  
  tipo_de_gato = ['pelado', 'selvagem', 'bravo']
  
  def __init__(self, nome, idade, desc, comida_favorita, tipo):
    super().__init__(nome, idade, desc)
    self.comida_favorita = comida_favorita
    if tipo in self.tipo_de_gato:
      self.tipo = tipo 
    else:
      self.tipo = 'gato normal'
  
  def acao(self, como_o_gato_esta = 0):
    if como_o_gato_esta == 0:
      print(f'{self.nome} está de boa')
    elif como_o_gato_esta == 1:
      print(f'{self.nome} está com sono')
    elif como_o_gato_esta == 2:
      print(f'{self.nome} está carente')
    else:
      print(f'não sei avaliar o estado de espírito de {self.nome}')
  
  def __str__(self):
    return super().__str__()\
    + '\n' +'tipo: ' +  self.tipo + '\n'\
    + 'prato favorito: ' + self.comida_favorita
    
cao = Dog("Groot", 5, "Branco, pelo longo", 100, "pequeno", "poodle")
gato = Cat("Freddie", 5, "Cinza", "atum", "bravo")

print(cao)
print(gato)