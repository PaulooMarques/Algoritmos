


presencas = {
    'Segunda': ['Gustavo', 'Julia', 'Fabricio', 'Fabiana','Pedro'],
    'Terça': ['Gustavo', 'Julia', 'Fabricio','Pedro'],
    'Quarta': ['Gustavo', 'Julia', 'Fabiana', 'Eduardo'],
    'Quinta': ['Gustavo', 'Julia', 'Fabricio', 'Fabiana'],
    'Sexta': ['Gustavo', 'Julia', 'Eduardo','Pedro']
}


alunos = set()
for dia in presencas.values():
    alunos.update(dia)


presentes_todos_dias = set(presencas['Segunda'])
for dia in presencas.values():
    presentes_todos_dias &= set(dia)


faltaram_algum_dia = alunos - presentes_todos_dias


contador_presencas = {}
for aluno in alunos:
    contador_presencas[aluno] = sum(1 for dia in presencas.values() if aluno in dia)


print("=== Lista de Presenças da Semana ===")
print(f"\n1. Presentes todos os dias: {sorted(presentes_todos_dias)}")
print(f"2. Faltaram pelo menos um dia: {sorted(faltaram_algum_dia)}")
print(f"3. Total de presenças por aluno:")
for aluno, total in sorted(contador_presencas.items()):
    print(f"   {aluno}: {total} dias")