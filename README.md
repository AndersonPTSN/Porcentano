# Porcentano

## Introdução

Esse projeto consiste na criação de um script para a postagem diária no Twitter da porcentagem do ano decorrido atual.

Twitter: [Porcentano](https://twitter.com/porcentano)

![image](https://user-images.githubusercontent.com/26872755/215668834-121aa494-eb59-4f08-a443-c7eb5b773f6f.png)
![image](https://user-images.githubusercontent.com/26872755/215668087-78497793-d418-48a6-8aea-c5d9992c6340.png)

Foi colocando em práticas conhecimentos básicos de Python e a utilização de bibliotecas para: 
  - Manipulação de tempo com o datetime 
  - Geração de imagens com a PIL Image
  - Criação de postagens com a TwitterAPI

## Utilização da API do Twitter
Para começar a utilizar a API do Twitter foi necessário utilizar o [portal do desenvolvedor](https://developer.twitter.com/) e nele criar um novo projeto, o importante foi que através dele foi criado as chaves e os tokens para a utilização da API, essas chaves eu salvei em um arquivo à parte, para não subirem no GitHub

![image](https://user-images.githubusercontent.com/26872755/215672942-30acb5c9-eff5-4515-987a-e023f078de0e.png)

## Automatização das postagens
No [Pythonanywhere](https://www.pythonanywhere.com) é possível hospedar scripts Python de graça, e além disso, pode criar Tarefas(Tasks), para poder rodar códigos Python quando quiser.

![image](https://user-images.githubusercontent.com/26872755/215670492-3bf46414-639d-41a2-8fd9-67523b6d18d3.png)

Nele, basicamente, hospedei os arquivos disponibilizados aqui no GitHub e criei uma Tarefa para rodar o script de postagem do Porcentano diariamente.

![image](https://user-images.githubusercontent.com/26872755/215670889-d0854691-5284-441e-85e1-64bd03e8f98e.png)

**AVISO:** As tarefas tem prazo de espiração!, logo, a cada mês precisa-se estender o prazo da tarefa.



