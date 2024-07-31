# Music Suggester

## Descrição

Serviço que sugere músicas com base na temperatura da cidade fornecida pelo usuário.

## Como Usar

- Endpoint: `api/token/`
- Método: POST
- Parâmetros:
{
	"username": "",
	"password": ""
}

- Endpoint: `/weather/suggest/<city_name>/`
- Método: GET

Mais informações em: 
- Endpoint: `/weather/doc/`
- Método: GET

curl -X POST <URL_RAIZ>/api/token/ -d "username=seu_usuario&password=sua_senha"
curl -H "Authorization: Bearer <seu_token_de_acesso>" <URL_RAIZ>/weather/suggest/<city_name>/

## Deploy

O serviço está disponível em: http://django-music-weather-env.eba-ab5zvx7k.us-west-2.elasticbeanstalk.com

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para mais detalhes.
