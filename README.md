# RamenGo!
Backend da aplicação RamenGo!

## Dependências
* Python 3
```
pip install -r requirements.txt
```

## Execução
1. Criar um arquivo '.env' com as constantes:
- DB_URL = 'mongodb+srv://ramengo:ramengo1234@ayssag.a971scw.mongodb.net/?retryWrites=true&w=majority&appName=AyssaG'
- API_KEY = 'ZtVdh8XQ2U8pWI2gmZ7f796Vh8GllXoN7mr0djNf'
- API_URL = "https://api.tech.redventures.com.br/orders/generate-id"

2. Subir o código do backend
```
flask --app app run
```
3. Acessar a url: [RamenGo!](https://tech.redventures.com.br)
4. Subtituir o campo API url com o endereço do servidor flask
5. Substituir a API Key com o mesmo valor da variável de ambiente API_KEY
6. Acessar a aplicação RamenGo!
