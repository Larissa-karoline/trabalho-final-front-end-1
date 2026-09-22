# Exercício 2 - Decaimento radioativo
massa_inicial = float(input("Digite a massa inicial do material : "))
massa_final = massa_inicial
tempo_total_segundos = 0

# O laço reduz a massa pela metade a cada 50 segundos enquanto ela for > = 0.5
while massa_final >= 0.5:
    massa_final /= 2
    tempo_total_segundos += 50

# Conversão do tempo
horas = tempo_total_segundos // 3600
resto_segundos = tempo_total_segundos % 3600
minutos = resto_segundos // 60
segundos = resto_segundos % 60

# Resultados formatados
print(f"Massa inicial: {massa_inicial:.2f} g")
print(f"Massa final: {massa_final:.4f} g")
print(f"Tempo total: {horas}h {minutos}min {segundos}s")