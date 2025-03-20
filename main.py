from analisador import obter_detalhes_video, analisar_comentarios

def main():
    video_id = input("Digite o ID do vídeo do YouTube: ")

    detalhes = obter_detalhes_video(video_id)
    if detalhes:
        print(f"Título: {detalhes['titulo']}")
        print(f"Descrição: {detalhes['descricao']}")
        print(f"Visualizações: {detalhes['visualizacoes']}")
        print(f"Likes: {detalhes['likes']}")
        print(f"Comentários: {detalhes['comentarios']}")

        print("\nAnálise dos comentários:")
        analise = analisar_comentarios(video_id)
        print(analise)
    else:
        print("Vídeo não encontrado!")

if __name__ == "__main__":
    main()
