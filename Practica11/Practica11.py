
#Importacion atraves de un alias
import math as m

resultado =m.sqrt(25)
print(resultado)

#importacion selectiva

from math import sqrt
resultado= sqrt(25)
print(resultado)

#importar  el modulo miModulo.py
#Importacion de un alias

import miModulo as mm
print(mm.saludos("williams"))

#Importacion selectiva 
from miModulo import saludos
print (saludos("Williams"))