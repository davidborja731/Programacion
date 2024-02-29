from Animales import Animal as Animal
from Perrera import perrera as perrera
animalNormal=Animal("1abc2","macho")
animalNormal1=Animal("14abc2","macho")
animalNormal2=Animal("143abc2","hembra")
animalNormal3=Animal("1a235bc2","hembra")
Perrera=perrera("Camino1, teruel","juan")
Perrera.nuevo_perro(animalNormal)
Perrera.nuevo_perro(animalNormal1)
Perrera.nuevo_perro(animalNormal2)
Perrera.nuevo_perro(animalNormal3)
Perrera.dame_info()
Perrera.muerto(animalNormal1)

