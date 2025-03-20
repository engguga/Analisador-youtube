import os
import openai
from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configuração da API do YouTube
youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

# Configuração da API do OpenAI
openai.api_key = OPENAI_API_KEY

def obter_detalhes_video(video_id):
    resposta = youtube.videos().list(
        part="snippet,statistics",
        id=video_id
    ).execute()

    if "items" not in resposta or not resposta["items"]:
        return None

    item = resposta["items"][0]
    detalhes = {
        "titulo": item["snippet"]["title"],
        "descricao": item["snippet"]["description"],
        "visualizacoes": item["statistics"].get("viewCount"),
        "likes": item["statistics"].get("likeCount"),
        "comentarios": item["statistics"].get("commentCount")
    }
    return detalhes

def analisar_comentarios(video_id):
    comentarios = []
    resposta = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=10
    ).execute()

    for item in resposta["items"]:
        comentario = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comentarios.append(comentario)

    prompt = f"Analise os seguintes comentários de um vídeo do YouTube:\n{comentarios}\n"
    resposta_chatgpt = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return resposta_chatgpt.choices[0].message.content

