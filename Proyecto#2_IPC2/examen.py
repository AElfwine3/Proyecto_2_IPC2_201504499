from enum import Enum


class Madera(Enum):
    PALO_BLANCO = 0
    CAOBA = 1
    CEDRO = 2
    PINO = 3
    MAPLE = 4
    NOGAL = 5
    OTRO = 6


class Color(Enum):
    SIN_COLOR = 0
    BLANCO = 1
    CAOBA = 2
    NEGRO = 3


class Material(Enum):
    CUERO = 0
    CUERINA = 1
    TELA = 2


class Mesa:
    def _init_(self, madera: Madera = None, color: Color = Color.SIN_COLOR, material: Material = None):
        self.madera = madera
        self.color = color
        self.material = material

    def _repr_(self):
        if self.madera is None and self.material is None:
            return 'Color de la mesa: {} \n Madera de la mesa: {}'.format(
                self.color.name, 'No asignado')
        else:
            return 'Color de la mesa: {} \n Madera de la mesa: {}'.format(
                self.color.name, self.madera.name)


def main():
    print(Color.NEGRO)
    print(Madera.PALO_BLANCO)
    print(Material.CUERINA)
    print(Mesa())
    print(Mesa(Madera.CAOBA, Color.NEGRO, Material.CUERO))

main()