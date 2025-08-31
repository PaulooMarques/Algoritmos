# Caso5: Controle de Participação em um Evento
# Os organizadores de um evento registraram os nomes dos participantes de cada atividade em
# listas separadas.
# • Exemplo:
# o Palestra: ["Ana", "Carlos", "Marina"]
# o Workshop: ["Carlos", "João", "Ana"]
# o Mesa-redonda: ["Marina", "João", "Paula"]
# Eles precisam:
# 1. Saber quem participou de todas as atividades.
# 2. Saber quem participou de apenas uma atividade.
# 3. Gerar uma lista com todos os nomes únicos dos participantes.
# 4. Contar quantos participantes distintos houve no evento.


def analisar_participacao(atividades):
    
    todos = set()
    for participantes in atividades.values():
        todos.update(participantes)
    
    
    participou_todas = todos.copy()
    for participantes in atividades.values():
        participou_todas &= set(participantes)
    
    
    participou_uma = []
    for pessoa in todos:
        count = sum(1 for p in atividades.values() if pessoa in p)
        if count == 1:
            participou_uma.append(pessoa)
    
    
    total = len(todos)
    
    return {
        'todas': sorted(participou_todas),
        'uma': sorted(participou_uma),
        'unicos': sorted(todos),
        'total': total
    }



if __name__ == "__main__":
    
    atividades = {
        "Palestra": ["Danilo", "Gabriel", "Fabiana"],
        "Workshop": ["Samuel", "João", "Danilo"],
        "Mesa-redonda": ["Fabiana", "João", "Paula"]
    }
    
    resultado = analisar_participacao(atividades)
    
    print("CONTROLE DE PARTICIPAÇÃO")
    print("-" * 40)
    print(f"1. Todas as atividades: {resultado['todas']}")
    print(f"2. Apenas uma atividade: {resultado['uma']}")
    print(f"3. Todos participantes: {resultado['unicos']}")
    print(f"4. Total distintos: {resultado['total']}")