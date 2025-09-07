# Caso 6: Sistema de Biblioteca


livros_emprestados = [
    ["Dom Casmurro", "Ana", 5],
    ["1984", "Carlos", 12],
    ["O Hobbit", "Marina", 3],
    ["O Pequeno Príncipe", "João", 8],
    ["Harry Potter", "Ana", 15],
    ["O Senhor dos Anéis", "Pedro", 2],
    ["Cem Anos de Solidão", "Maria", 10],
    ["O Cortiço", "Carlos", 6],
    ["Memórias Póstumas", "Lucia", 18]
]

print("=== SISTEMA DE BIBLIOTECA ===")


livros_atrasados = [livro for livro in livros_emprestados if livro[2] > 7]
print("1. Livros em atraso (>7 dias):")
for livro in livros_atrasados:
    print(f"   '{livro[0]}' - {livro[1]} ({livro[2]} dias)")


livro_mais_tempo = max(livros_emprestados, key=lambda x: x[2])
print(f"\n2. Livro há mais tempo: '{livro_mais_tempo[0]}' - {livro_mais_tempo[1]} ({livro_mais_tempo[2]} dias)")


usuarios = list(set(livro[1] for livro in livros_emprestados))
print(f"\n3. Usuários: {usuarios}")


media_dias = sum(livro[2] for livro in livros_emprestados) / len(livros_emprestados)
print(f"\n4. Média de empréstimo: {media_dias:.2f} dias")

print(f"\nResumo: {len(livros_emprestados)} livros, {len(livros_atrasados)} atrasados, {len(usuarios)} usuários")