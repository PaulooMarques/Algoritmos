# Problema 3 – Loja de Música Online com Estatísticas
# Uma loja virtual armazena músicas em uma lista de dicionários, cada música com:
# titulo, artista, downloads, avaliacoes (lista de notas de 1 a 5).
# Tarefas:
# 1. Crie uma função que calcule a nota média de avaliação de cada música.
# 2. Crie uma função que mostre qual artista tem o maior número total de downloads
# somando todas as suas músicas.
# 3. Monte um ranking das músicas mais bem avaliadas (ordem decrescente da média das
# notas).

musicas = [
    {
        "titulo": "Bohemian Rhapsody",
        "artista": "Queen",
        "downloads": 15000,
        "avaliacoes": [5, 4, 5, 5, 4, 3, 5]
    },
    {
        "titulo": "Believer",
        "artista": "Imagine Dragons",
        "downloads": 12500,
        "avaliacoes": [5, 5, 4, 5, 5, 4, 5, 3]
    },
    {
        "titulo": "Smells Like Teen Spirit",
        "artista": "Nirvana",
        "downloads": 9800,
        "avaliacoes": [4, 5, 4, 3, 5, 4, 4]
    },
    {
        "titulo": "Hotel California",
        "artista": "Eagles",
        "downloads": 18200,
        "avaliacoes": [5, 5, 5, 4, 5, 5, 4, 5]
    },
    {
        "titulo": "Thunderstruck",
        "artista": "AC/DC",
        "downloads": 11300,
        "avaliacoes": [4, 4, 5, 3, 4, 5, 4, 3, 4]
    }
]


def nota_media_avaliacao():
   
    print("Músicas disponíveis:")
    for musica in musicas:
        print(f"- {musica['titulo']} ({musica['artista']})")
    print()
    
    titulo_escolhido = input("Digite o título da música: ")
    
    for musica in musicas:
        if musica["titulo"] == titulo_escolhido:
            avaliacoes = musica["avaliacoes"]
            if len(avaliacoes) > 0:
                media = sum(avaliacoes) / len(avaliacoes)
                return media
            else:
                return 0
    
    return 0  


def artista_mais_downloads():
   
    downloads_por_artista = {}
    
    for musica in musicas:
        artista = musica["artista"]
        downloads = musica["downloads"]
        
        if artista in downloads_por_artista:
            downloads_por_artista[artista] += downloads
        else:
            downloads_por_artista[artista] = downloads
    
    artista_top = ""
    maior_downloads = 0
    
    for artista, total_downloads in downloads_por_artista.items():
        if total_downloads > maior_downloads:
            maior_downloads = total_downloads
            artista_top = artista
    
    return artista_top

resultado_media = nota_media_avaliacao()
print(f"Nota média: {resultado_media:.2f}")
print()


artista_popular = artista_mais_downloads()
print(f"Artista com mais downloads: {artista_popular}")
print()

musicas_com_media = []
for musica in musicas:
    avaliacoes = musica["avaliacoes"]
    if len(avaliacoes) > 0:
        media = sum(avaliacoes) / len(avaliacoes)
    else:
        media = 0
    
    musicas_com_media.append({
        "titulo": musica["titulo"],
        "artista": musica["artista"],
        "media": media
    })

print("=== RANKING DAS MÚSICAS MAIS BEM AVALIADAS ===")
for i in range(len(musicas_com_media)):
    for j in range(i + 1, len(musicas_com_media)):
        if musicas_com_media[i]["media"] < musicas_com_media[j]["media"]:
            musicas_com_media[i], musicas_com_media[j] = musicas_com_media[j], musicas_com_media[i]

for i, musica_info in enumerate(musicas_com_media, 1):
    titulo = musica_info["titulo"]
    artista = musica_info["artista"]
    media = musica_info["media"]
    print(f"{i}º lugar: {titulo} - {artista} (Média: {media:.2f})")