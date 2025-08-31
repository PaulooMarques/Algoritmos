import math

distancias = []
for i in range(6):
    dist = float(input(f"Distância da viagem {i+1} (km): "))
    distancias.append(dist)


total = sum(distancias)


maior = max(distancias)
menor = min(distancias)


media_arredondada = math.ceil(sum(distancias) / 6)


print(f"\nDistâncias: {distancias}")
print(f"Total: {total} km")
print(f"Maior: {maior} km | Menor: {menor} km")
print(f"Média (arredondada): {media_arredondada} km")


