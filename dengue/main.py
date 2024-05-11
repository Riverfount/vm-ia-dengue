import google.generativeai as genai
import pandas as pd

from dengue.config import settings
from dengue.data.data_set import (
    diagnosis,
    prevention,
    signals,
    transmission,
    treatment,
)
from dengue.rules import embbeding_creator, find_answers, readable_response

genai.configure(api_key=settings.security.GOOGLE_API_KEY)
model = 'models/embedding-001'
generative_config_system = {
    'candidate_count': 1,
    'temperature': 0,
}

df = pd.DataFrame([diagnosis, prevention, signals, transmission, treatment])
df.columns = ['Title', 'Content']
df['Embeddings'] = df.apply(
    lambda row: embbeding_creator(row['Title'], row['Content'], model=model, genai=genai), axis=1
)

while True:
    print('Para encerrar digite "sair"')
    question = input('O que deseja saber sobre dengue?\n')
    if question == 'sair':
        break
    query = find_answers(question, base=df, model=model, genai=genai)
    print(
        readable_response(
            genai=genai,
            settings=generative_config_system,
            query=query
        )
    )
