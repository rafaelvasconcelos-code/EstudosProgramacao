from pydub import AudioSegment
import os

def converter_mp3_para_wav(caminho_mp3, caminho_wav):
    # Verifica se o arquivo MP3 existe
    if not os.path.exists(caminho_mp3):
        return "Erro: O arquivo MP3 não foi encontrado."

    try:
        # Carrega o arquivo MP3
        audio = AudioSegment.from_mp3(caminho_mp3)
        
        # Exporta como WAV
        audio.export(caminho_wav, format="wav")
        return f"Conversão concluída! Arquivo salvo em: {caminho_wav}"
    
    except Exception as e:
        return f"Erro ao converter o arquivo: {e}"

# Exemplo de uso
if __name__ == "__main__":
    # Caminho do arquivo MP3 de entrada
    caminho_mp3 = "teste2.mp3"
    # Caminho onde o arquivo WAV será salvo
    caminho_wav = "seu_audio_convertido.wav"
    
    resultado = converter_mp3_para_wav(caminho_mp3, caminho_wav)
    print(resultado)