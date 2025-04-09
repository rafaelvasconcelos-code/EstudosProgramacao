from google import genai


def gera_resumo(referencia):
  client = genai.Client(api_key="AIzaSyCfaWuIfMLtsS0QhDaFvAjZL5rrlszbW2c")

  response = client.models.generate_content(
      model="gemini-2.0-flash",
      contents=f"Explique de forma detalhada o {referencia} da Bíblia, fazendo um contexto da realidade atual.",
  )
  return response.text