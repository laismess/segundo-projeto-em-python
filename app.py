# Programa para calcular o consumo mensal de energia
# Autor: Laís

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horasDia = float(input("Digite o tempo médio de uso diário em horas: "))

consumoMensal = (potencia * horasDia * 30) / 1000

valorKwh = 0.75
custoMensal = consumoMensal * valorKwh

print("\n--- Resultado ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumoMensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custoMensal:.2f} por mês")