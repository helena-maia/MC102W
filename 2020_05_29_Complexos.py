# Bruno, Francisco, João Andrade, Robenildo

class NumC:
  def __init__(self, real = 0, imaginario = 0):
    self.real = real
    self.imaginario = imaginario
    
  def __str__(self):
    if self.real == 0:
      str_real = ""
    else:
      str_real = "{:.2f}".format(self.real)

    if self.imaginario == 0:
      str_imaginario = ""
    elif self.imaginario > 0:
      if self.real == 0:
        str_imaginario = "{:.2f}i".format(self.imaginario)
      else:
        str_imaginario = "+{:.2f}i".format(self.imaginario)
    else:
      str_imaginario = "{:.2f}i".format(self.imaginario)
    
    str_num = "{}{}".format(str_real, str_imaginario)

    return str_num


class EquacaoSG:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

  def calcula_raizes(self):
    raizes = []
    delta = self.b ** 2 - 4 * self.a * self.c
    if delta == 0:
      x1 = (- b) / 2 * a
      raizes.append(NumC(x1))
    elif delta > 0:
      rD = delta ** (1 / 2)
      x1 = (- b + rD) / (2 * a)
      x2 = (- b - rD) / (2 * a)
      raizes.append(NumC(x1))
      raizes.append(NumC(x2))
    else:
      rD = (- delta) ** (1 / 2)
      pR = (- b) / 2 * a
      pI = rD / 2 * a
      raizes.append(NumC(pR, pI))
      raizes.append(NumC(pR, -pI))


def Soma(x, y):
  real = x.real + y.real
  imaginario = x.imaginario + y.imaginario
  complexo = NumC(real, imaginario)
  return complexo
  
def Subtracao(x, y):
  real = x.real - y.real
  imaginario = x.imaginario - y.imaginario
  complexo = NumC(real, imaginario)
  return complexo


num1 = NumC(1.,1.)
num2 = NumC(2.,2.)
print(Soma(num1,num2))
print(Subtracao(num1,num2))
