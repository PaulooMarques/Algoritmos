# 3. Agenda Semanal
# Contexto: Um consultório possui 5 dias de atendimento e 3 horários por dia.
# Tarefa: Armazene os nomes dos pacientes em uma matriz 5x3 e exiba a agenda completa.

agenda = [
    ["Maria Silva", "João Santos", "Ana Costa"],
    ["Pedro Lima", "Carla Souza", "VAGO"],
    ["Lucas Alves", "Juliana Rocha", "Roberto Dias"],
    ["VAGO", "Fernanda Lopes", "Carlos Mendes"],
    ["Patrícia Gomes", "VAGO", "Marcos Oliveira"]
]

dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira"]
horarios = ["09:00 - 12:00", "14:00 - 17:00", "18:00 - 21:00"]

for dia in range(len(agenda)):
    print(f"\n📅 {dias_semana[dia].upper()}")
    print("-" * 70)
    
    for horario in range(len(agenda[dia])):
        paciente = agenda[dia][horario]
        status = "🟢 AGENDADO" if paciente != "VAGO" else "⚪ DISPONÍVEL"
        print(f"  {horarios[horario]} - {paciente:<20} [{status}]")

print("\n" + "=" * 70)
print("ESTATÍSTICAS DA SEMANA")
print("=" * 70)

total_atendimentos = 0
total_vagas = 0

for dia in agenda:
    for paciente in dia:
        if paciente != "VAGO":
            total_atendimentos += 1
        else:
            total_vagas += 1

capacidade_total = len(agenda) * len(agenda[0])
taxa_ocupacao = (total_atendimentos / capacidade_total) * 100

print(f"Total de atendimentos agendados: {total_atendimentos}")
print(f"Total de horários disponíveis: {total_vagas}")
print(f"Capacidade total: {capacidade_total} horários")
print(f"Taxa de ocupação: {taxa_ocupacao:.1f}%")

print("\n" + "=" * 70)
print("HORÁRIOS DISPONÍVEIS PARA AGENDAMENTO")
print("=" * 70)

tem_vaga = False
for dia in range(len(agenda)):
    for horario in range(len(agenda[dia])):
        if agenda[dia][horario] == "VAGO":
            tem_vaga = True
            print(f"✓ {dias_semana[dia]} - {horarios[horario]}")

if not tem_vaga:
    print("Não há horários disponíveis esta semana.")

print("=" * 70)