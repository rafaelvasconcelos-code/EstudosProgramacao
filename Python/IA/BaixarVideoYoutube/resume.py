from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import re

def sent_tokenize(text):
    """
    Divide o texto em frases usando pontuação final (simples substituto ao sent_tokenize do nltk).
    """
    sentences = re.split(r'(?<=[.!?]) +', text)
    return [s.strip() for s in sentences if s.strip()]


def get_youtube_transcript(video_id):
    """
    Busca a transcrição de um vídeo do YouTube (se disponível).
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['pt', 'en'])
        full_text = " ".join([segment['text'] for segment in transcript])
        return full_text
    except Exception as e:
        print(f"Erro ao buscar transcrição: {e}")
        return None

def summarize_text(text, max_chunk=1000):
    """
    Resume o texto em blocos menores (limitados por token).
    """
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_chunk:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
    if current_chunk:
        chunks.append(current_chunk.strip())

    summary = ""
    for chunk in chunks:
        summary_piece = summarizer(chunk, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
        summary += summary_piece + "\n"

    return summary.strip()

def identify_speakers(text):
    """
    Heurística simples para tentar separar entrevistador e entrevistado
    com base em palavras-chave. (Ideal com transcrição com nomes)
    """
    sentences = sent_tokenize(text)
    interviewer_lines = []
    interviewee_lines = []

    for sentence in sentences:
        if any(p in sentence.lower() for p in ["bem-vindo", "nosso convidado", "conte para nós", "poderia explicar", "como você vê"]):
            interviewer_lines.append(sentence)
        else:
            interviewee_lines.append(sentence)

    return "\n".join(interviewer_lines), "\n".join(interviewee_lines)

def main():
    video_url = "https://www.youtube.com/watch?v=WykOxY55yw0"
    video_id = video_url.split("v=")[-1]

    print("🎧 Obtendo transcrição...")
    transcript = get_youtube_transcript(video_id)
    if not transcript:
        return

    print("✂️ Separando falas...")
    interviewer_text, interviewee_text = identify_speakers(transcript)

    print("📝 Resumindo fala do entrevistador...")
    interviewer_summary = summarize_text(interviewer_text)

    print("📝 Resumindo fala do entrevistado...")
    interviewee_summary = summarize_text(interviewee_text)

    print("\n📌 RESUMO FINAL:")
    print("\n🎙️ Entrevistador:")
    print(interviewer_summary)
    print("\n🧑 Entrevistado:")
    print(interviewee_summary)

if __name__ == "__main__":
    main()
