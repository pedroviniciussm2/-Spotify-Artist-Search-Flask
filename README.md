# Spotify Artist Search - Flask

Aplicação web simples construída com Flask que permite pesquisar artistas musicais usando a API Web do Spotify.

## Funcionalidades

- Busca de artistas pelo nome
- Exibição de detalhes do artista, como:
  - Nome
  - Seguidores
  - Gêneros musicais
  - Imagem do artista (quando disponível)
- Interface simples e intuitiva

## Tecnologias usadas

- Python 3
- Flask
- Requests (para consumir API do Spotify)
- API Web do Spotify (Client Credentials OAuth)

## Como usar

### Pré-requisitos

- Python 3 instalado
- Conta de desenvolvedor no Spotify para obter Client ID e Client Secret (https://developer.spotify.com/dashboard/)

### Passos

1. Clone este repositório:
git clone https://github.com/seuusuario/seurepositorio.git

csharp
Copiar
Editar
2. Instale as dependências:
pip install -r requirements.txt

swift
Copiar
Editar
3. Configure as credenciais do Spotify no arquivo `app.py`:
```python
CLIENT_ID = "seu_client_id_aqui"
CLIENT_SECRET = "seu_client_secret_aqui"
Execute a aplicação:

nginx
Copiar
Editar
python app.py
Acesse http://127.0.0.1:5000 no seu navegador.

Estrutura do projeto
cpp
Copiar
Editar
meu_site_spotify/
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/  (opcional)
Considerações finais
Este projeto é uma ótima base para aprender integração com APIs REST e desenvolvimento web com Flask.
Sinta-se à vontade para expandir com funcionalidades como autenticação, favoritos, paginação, ou integração com outras APIs.

Licença
Este projeto está licenciado sob a MIT License.
