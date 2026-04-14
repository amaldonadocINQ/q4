def calcularDano(ataque, defensa):
    if ataque - defensa < 0:
        return 0
    else:
        return ataque - defensa


def aplicarDano(hpActual, dano):
    if hpActual - dano < 0:
        return 0
    else:
        return hpActual - dano


def mostrarEstado(nombre, hp, hpMax=100):
    return f"{nombre}: {hp}/{hpMax}"


def realizarAtaque(atacante, defensor, dano):
    return f"{atacante} ataca a {defensor} por {dano} daño"


ataqueHeroe = 25
defensaEnemigo = 10

hpHeroe = 100
hpEnemigo = 50

danoHeroe = calcularDano(ataqueHeroe, defensaEnemigo)

print("--- Estado Inicial ---")
print(mostrarEstado("Héroe", hpHeroe))
print(mostrarEstado("Enemigo", hpEnemigo))
print(" ")
print(realizarAtaque("Héroe", "Enemigo", danoHeroe))
hpEnemigo = aplicarDano(hpEnemigo, danoHeroe)
print(mostrarEstado("Enemigo", hpEnemigo))
print(" ")
print(realizarAtaque("Héroe", "Enemigo", danoHeroe))
hpEnemigo = aplicarDano(hpEnemigo, danoHeroe)
print(mostrarEstado("Enemigo", hpEnemigo))
