# Caso6: Sistema de Biblioteca
# Uma biblioteca mantém uma lista de livros emprestados, onde cada item é representado por
# [titulo, usuario, dias_emprestado].
# Exemplo:
# [
#  ["Dom Casmurro", "Ana", 5],
#  ["1984", "Carlos", 12],
#  ["O Hobbit", "Marina", 3]
# ]
# O sistema precisa:
# 1. Listar apenas os livros que estão emprestados há mais de 7 dias.
# 2. Encontrar o livro emprestado há mais tempo.
# 3. Gerar uma lista apenas com os nomes dos usuários que têm livros emprestados.
# 4. Calcular a média de dias de empréstimo.


def analisar_emprestimos(livros_emprestados):

    mais_7_dias = []
    for livro in livros_emprestados:
        titulo, usuario, dias = livro
        if dias > 7:
            mais_7_dias.append(livro)

    livro_mais_tempo = max(livros_emprestados, key=lambda x: x[2])

    usuarios = []
    for livro in livros_emprestados:
        titulo, usuario, dias = livro
        if usuario not in usuarios:
            usuarios.append(usuario)

    total_dias = sum(livro[2] for livro in livros_emprestados)
    media_dias = total_dias / len(livros_emprestados)

    return {
        "mais_7_dias": mais_7_dias,
        "mais_tempo": livro_mais_tempo,
        "usuarios": sorted(usuarios),
        "media_dias": round(media_dias, 1),
    }


def exibir_resultado(livros, resultado):

    print("Sistema da Biblioteca")
    print("=" * 60)

    print("Livros Emprestados:")
    for titulo, usuario, dias in livros:
        print(f"  • {titulo} - {usuario} ({dias} dias)")

    print("-" * 60)

    print("1. Livros ha mais de 7 dias emprestado:")
    for titulo, usuario, dias in resultado["mais_7_dias"]:
        print(f"   • {titulo} - {usuario} ({dias} dias)")

    print(f"\n2. Livro emprestado ha mais tempo:")
    titulo, usuario, dias = resultado["mais_tempo"]
    print(f"   • {titulo} - {usuario} ({dias} dias)")

    print(f"\n3. Usuarios com Livros Emprestados:")
    print(f"   {', '.join(resultado['usuarios'])}")

    print(f"\n4. Média de dias de Emprestimo: {resultado['media_dias']} dias")
    print("-" * 60)


if __name__ == "__main__":

    livros_emprestados = [
        ["As 100 Melhores Histórias da Mitologia", "Ana", 5],
        ["O Ano em que Zumbi Tomou o Rio", "Orlando", 12],
        ["O Guarani", "Mariana", 3],
        ["A Menina que Roubava Livros", "Cleber", 15],
        ["As Crônicas de Nárnia", "Paulo", 8],
        ["Harry Potter e a Câmara Secreta", "Francisca", 2],
        ["Percy Jackson e o Ladrão de Raios", "Maria", 10],
    ]

    resultado = analisar_emprestimos(livros_emprestados)
    exibir_resultado(livros_emprestados, resultado)
