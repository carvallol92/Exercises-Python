# -*- coding: utf-8 -*-

print('Bienvenidos a la calculadora de superficies')
print('')
print('Circulo: 1 - Cuadrado: 2')
print('')

geometria = int(input('Porfavor, indica el número de la geometria que deseas calcular:  '))

if geometria == int(1):
    def circulo(radio):
        return 3.141516 * radio **2

    radio = float(input('Indica el radio de la circunferencia:  '))

    sup_circulo = circulo(radio)

    print('La superficie del Circulo es: {} metros cuadrados'.format(sup_circulo))
else:
    def cuadrado(lado):
        return lado **2

    lado = float(input('Indique la longitud del cuadrado:  '))

    sup_cuadrado= cuadrado(lado)

    print('La superficie del Cuadrado es: {} metros cuadrados'.format(sup_cuadrado))

print('Proceso Completado')