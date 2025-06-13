## Blog em Django

Este é um sistema de blog construído com Django, com funcionalidades modernas como:

- Postagens com imagem e categoria
- Autenticação de usuários (registro, login, logout)
- Comentários por post
- Edição/remoção de comentários pelos autores ou administradores
- Filtro por categoria
- Busca por título e conteúdo
- Paginação
- Troca dinâmica de tema (claro/escuro)
- Painel administrativo com gerenciamento de posts


## Tecnologias utilizadas

- [Python 3.13](https://www.python.org/)
- [Django 5.2](https://www.djangoproject.com/)
- SQLite (como banco de dados local)
- Bootstrap 5 (para responsividade e visual)
- JavaScript (para alternância de tema)


## Funcionalidades principais

- Listagem e visualização de posts
- Comentários com autenticação
- Filtro por categoria
- Busca por palavra-chave
- Troca de tema (dark/light)
- Responsividade total (mobile-first)
- Painel de administração Django (para gerenciar posts, comentários, categorias, usuários, etc.)


## Clone o repositório:

```bash
- "git clone https://github.com/SauloEsteves14/meu_blog.git"
- "cd meu_blog"


Crie o ambiente virtual e ative-o:
- "python -m venv venv"

# Windows
- "venv\Scripts\activate"

# Powershell
- ".\venv\Scripts\Activate.ps1"

# Linux/macOS
- "source venv/bin/activate"


## Instale as dependências:

- "pip install -r requirements.txt"


## Aplique as migrações:

- "python manage.py migrate"


## Crie um superusuário (para acessar o painel de admin):

- "python manage.py createsuperuser"


## Execute o servidor:

- "python manage.py runserver"
Acesse o sistema em: http://127.0.0.1:8000/


## Administração

Você pode acessar o painel administrativo padrão do Django em:
http://127.0.0.1:8000/admin/

Use o superusuário criado com createsuperuser para logar.


## Estrutura básica

blog_django/
├── blog/                # App principal
│   ├── templates/
│   │   └── blog/
│   └── static/
├── blog_project/        # Configurações do Django
├── media/               # Uploads de imagens
├── db.sqlite3           # Banco de dados local
├── manage.py
└── requirements.txt


## Observações:

As imagens são armazenadas em /media/, por isso esta pasta está no .gitignore.
O botão de troca de tema salva a preferência no localStorage.
O site é responsivo e se adapta bem em telas de celular.


## Contribuição:

Se quiser contribuir com o projeto, sinta-se à vontade para enviar pull requests, abrir issues ou sugerir melhorias.


## Licença:

Este projeto está sob a licença MIT. 