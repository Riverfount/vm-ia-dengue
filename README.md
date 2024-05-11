# vm-ia-dengue
Este é um projeto experimental que busca, a partir de alguns documentos com informações sobre a Dengue, alimentar
o Gemini, inteligência artificial do Google, e a partir dessas informações responder qualquer pergunta a ele feita.

# Características
O princípio é de uso de documentos em embbeding que trazem informações a respeito da Dengue, como:

- Sinais e Sintômas
- Diagnóstico
- Prevenção
- Transmissão
- Tratamento

E, com base nas informações contidas nesses documentos, que servem de contexto para o Gemini, orientar a quem interagir
com esta IA respondendo de forma precisa, mas informal, as perguntas realizadas.

Como protótipo e primeira versão, há muito a melhorar, mas já está cumprido seu papel principal, que é de orientar as 
pessoas sobre a Dengue.

# Requisitos e Instalação

## Requisitos:
Este projeto possui os seguintes requisitos:
1. Python 3.12 ou maior
2. Poetry 1.8.2
3. Dynaconf - Para gerências de chaves de API
4. Google Generative AI (google-generativeai)
5. Uma chave de API do AIStudio do Google

## Instalação
Para instalar esse projeto basta seguir os seguintes passos:
1. Faça um clone desse repositório para seu próprio GitHub
1. Clone esse repositório para sua máquina local
2. Mude para o diretório onde o projeto foi clonado
3. Execute a instalação das libs com o poetry
4. Mude para a pasta `dengue`
5. Execute o projeto e faça suas perguntas

Em termos de código em ambiente GNU/Linux podemos executar os passos assim da seguinte forma:

```bash
git clone git@github.com:Riverfount/vm-ia-dengue.git
cd vm-ia-dengue
poetry install
cd dengue
python main.py
```
