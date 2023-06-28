
# OrganizerFine API

Projeto desenvolvido com o intuito de alimentar com dados o App Mobile OrganizerFine (disponível em: https://github.com/V1ntag3/OrganizerFine).
## Documentação da API

Documentação pode ser encontrada no postman: https://documenter.getpostman.com/view/17463653/2s93z9aguh
## Stack utilizada

**Back-end:** Django

## Hospedagem

Disponivel em: https://v1nt4g3.pythonanywhere.com/

## Rodando localmente

Clone o projeto
#### É necessário que tenha instalado o Pipenv
```bash
  git clone https://github.com/V1ntag3/organizer_fine_api
```

Entre no diretório do projeto

```bash
  cd organizer_fine_api
```

Abrir ambiente virtual

```bash
  pipenv shell
```

Para criar o banco de dados e as migrações (Caso não tenha realizado antes)

```bash
  python manage.py makemigrations
```
Para realizar as migrações (Caso não tenha realizado antes)

```bash
  python manage.py migrate
```

Rodar projeto

```bash
  python manage.py runserver
```


## Aprendizados

Consegui fazer avanços significativos no desenvolvimento de APIs. Agora sou capaz de criar recursos de login e registro de usuários, além de ter aprimorado o tipo de token utilizado no projeto, migrando para o knox-django, o que me permite ter várias sessões abertas simultaneamente. Também adquiri conhecimentos essenciais para a implementação do CRUD por meio do Django Rest Framework.

Estou entusiasmado em anunciar que já estou planejando aprimorar ainda mais o projeto. Tenho em mente a inclusão de novos recursos de CRUD, que proporcionarão uma experiência ainda mais completa aos usuários. Além disso, estou explorando a possibilidade de adicionar uma funcionalidade de criação de relatórios, o que contribuirá para uma análise mais aprofundada dos dados financeiros.

Estou empolgado com essas atualizações, pois tenho certeza de que elas trarão um valor significativo ao projeto, permitindo que os usuários tenham um melhor controle e gestão de suas finanças. Continuarei a me dedicar ao desenvolvimento de APIs e aprimorar minhas habilidades, buscando sempre oferecer soluções cada vez mais robustas e eficientes.

## Suporte

Para suporte, mande um email para marcos.vinicius.r.alencar@gmail.com.


## Licença

MIT License

Copyright (c) 2023 Marcos Vinícius Ribeiro Alencar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
