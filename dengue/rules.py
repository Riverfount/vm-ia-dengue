import google.generativeai
import numpy as np
from pandas import DataFrame


def embbeding_creator(title: str, text: str, model: str, genai: google.generativeai) -> float:
    """
    Generate an embedding column for data frame based on its coluns title and text using a specified Gemini model.

    Args:
        title (str): The title column of the document.
        text (str): The content column of the document.
        model (str): The name of the Gemini model to use for embedding.
        genai: An instance of the Google Generative AI library.

    Returns:
        float: The first element of the embedding vector.

    Note:
        The task type for the embedding is set to 'RETRIEVAL_DOCUMENT'.

    """
    return genai.embed_content(
        model=model,
        content=text,
        title=title,
        task_type='RETRIEVAL_DOCUMENT')['embedding'][0]


def find_answers(query: str, base: DataFrame, model: str, genai: google.generativeai):
    """
    Find the answer to a given query by embedding the query and finding the most similar document in
    a given base DataFrame.

    Parameters:
        query (str): The query to be answered.
        base (DataFrame): The DataFrame containing the documents to search for the answer.
        model (str): The name of the Gemini model to use for generate a response.
        genai: An instance of the Google Generative AI library.

    Returns:
        str: The content of the most similar document to the query.
    """
    query_embedding = genai.embed_content(
        model=model,
        content=query,
        task_type='RETRIEVAL_QUERY'
    )['embedding']

    dot_products = np.dot(np.stack(base['Embeddings']), query_embedding)

    index = np.argmax(dot_products)
    return ''.join(base.iloc[index]['Content'])


def readable_response(genai: google.generativeai, settings: dict[str, int], query: str):
    """
    Generates a readable response using the given query and settings.

    Args:
        genai (GenerativeAI): An instance of the GenerativeAI class.
        settings (dict): The settings for generating the response.
        query (str): The query to be used for generating the response.

    Returns:
        str: The generated readable response.
    """
    prompt = f'Haja como um médico, mas informalmente, reescreva o texto para que pessoas comuns compreendam: {query}'
    model = genai.GenerativeModel(
        model_name="gemini-1.0-pro",
        generation_config=settings
    )
    response = model.generate_content(prompt)
    return response.text
