# Backend do projeto 2 - Aluno: Ricardo Ribeiro Rodrigues
## Tema do projeto: Descontos em jogos digitais.
O backend desse projeto é uma simples REST API para implementar um sistema de favoritos no [frontend](https://github.com/RicardoRibeiroRodrigues/PromoGamesFront), onde as funcionalidades são melhores exploradas.
## Feito com:
- [![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)](https://www.django-rest-framework.org)
- [![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org)
- [![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)](https://www.heroku.com)
- [![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com)

## Deploy:
O link para o deploy no heroku está disponível [aqui](https://afternoon-stream-42339.herokuapp.com), os dados podem ser acessados indo para a rota [/api/favorites](https://afternoon-stream-42339.herokuapp.com/api/favorites).
## Features principais:
- [X] Listar jogos em promoção.
- [X] Ser possível favoritar ofertas.
## Features adicionais:
- [X] Menu lateral para filtrar por lojas ou por apenas ofertas favoritadas.
- [X] Opção no menu para ordenar por título, porcentagem de desconto, por preço e pela avaliação na metacritic.
- [X] Barra de pesquisa para pesquisar ofertas para um jogo específico.
- [X] Tela adicional para ver detalhes do jogo como avaliação na steam e na metacritic (não são disponibilizadas para todos os jogos), pode ser visto também se houverem, lojas que estão fazendo preços melhores nesse mesmo jogo.
- [X] Botão para redirecionar para o site ofertando o jogo.
## API:
O projeto se baseia em uma API de descontos em jogos chamada **CheapShark**, [clique aqui para ver a documentação oficial](https://apidocs.cheapshark.com).
