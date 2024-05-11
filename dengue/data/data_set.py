def return_content(document):
    return open(document, 'r').readlines()


diagnosis = {
    'title': "Diagnostico da Dengue",
    'content': return_content('data/diagnostico-da-dengue.md'),
}
prevention = {
    'title': "Prevenção da Dengue",
    'content': return_content('data/prevencao-da-dengue.md'),
}
signals = {
    'title': "Sinais e Sintomas da Dengue",
    'content': return_content('data/sinais-da-dengue.md'),
}
transmission = {
    'title': "Transmissão da Dengue",
    'content': return_content('data/transmissao-da-dengue.md'),
}
treatment = {
    'title': "Tratamento da Dengue",
    'content': return_content('data/tratamento-da-dengue.md'),
}
