"""
Algoritmo 42 – Entrar com um ângulo em graus e imprimir: seno, co-seno,
tangente, secante, co-secante e co-tangente deste ângulo. Use o módulo math.
"""

import math
# ENTRADA DE DADOS
angulo_graus = float(input("Digite o ângulo em graus: "))

# CÁLCULOS
angulo_radianos = math.radians(angulo_graus)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)
secante = 1 / cosseno if cosseno != 0 else float('inf')
cossecante = 1 / seno if seno != 0 else float('inf')
cotangente = 1 / tangente if tangente != 0 else float('inf')

# SAÍDA DE DADOS
print(f"Seno: {seno}")
print(f"Cosseno: {cosseno}")
print(f"Tangente: {tangente}")
print(f"Secante: {secante}")
print(f"Cossecante: {cossecante}")
print(f"Cotangente: {cotangente}")

