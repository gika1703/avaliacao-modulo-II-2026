# 🎮 Avaliação Prática — Desenvolvimento de API REST com Flask

## 📚 Disciplina

Desenvolvimento Web / Desenvolvimento de APIs

## 👨‍💻 Avaliação

Nesta atividade você deverá desenvolver uma **API REST utilizando Python e Flask**.

O objetivo da avaliação é verificar sua capacidade de criar e utilizar **rotas, métodos HTTP, parâmetros, JSON e códigos de resposta HTTP**.

Você deverá desenvolver uma API para gerenciar um pequeno **Catálogo de Jogos**.

---

# 🎯 Objetivo

Criar uma API REST que permita:

* listar jogos;
* consultar um jogo específico;
* cadastrar novos jogos;
* atualizar jogos;
* excluir jogos.

Ao final da atividade, sua API deverá possuir **5 endpoints funcionando corretamente**.

---

# 🛠 Tecnologias permitidas

Utilize:

* Python 3;
* Flask;
* JSON.

Não será necessário utilizar banco de dados.

Os dados poderão permanecer armazenados em uma **lista de dicionários Python enquanto o programa estiver em execução**.

---

# 📂 Estrutura sugerida

Seu projeto poderá possuir a seguinte estrutura:

```text
prova-api-rest/
│
├── app.py
├── requirements.txt
└── README.md
```

O arquivo principal da API deverá ser:

```text
app.py
```

---

# 📦 Instalação do Flask

Caso seja necessário instalar o Flask:

```bash
pip install flask
```

Você também poderá criar um arquivo:

```text
requirements.txt
```

contendo:

```text
Flask
```

E instalar as dependências utilizando:

```bash
pip install -r requirements.txt
```

---

# 🎮 Estrutura dos dados

Cada jogo deverá possuir os seguintes campos:

| Campo        | Tipo    | Descrição                   |
| ------------ | ------- | --------------------------- |
| `id`         | inteiro | Identificador único do jogo |
| `titulo`     | texto   | Nome do jogo                |
| `genero`     | texto   | Gênero do jogo              |
| `plataforma` | texto   | Plataforma principal        |
| `ano`        | inteiro | Ano de lançamento           |

Exemplo:

```json
{
    "id": 1,
    "titulo": "Minecraft",
    "genero": "Sandbox",
    "plataforma": "PC",
    "ano": 2011
}
```

---

# 📋 Dados iniciais

Sua aplicação deverá começar com pelo menos **3 jogos cadastrados**.

Exemplo:

```python
jogos = [
    {
        "id": 1,
        "titulo": "Minecraft",
        "genero": "Sandbox",
        "plataforma": "PC",
        "ano": 2011
    },
    {
        "id": 2,
        "titulo": "Super Mario Odyssey",
        "genero": "Plataforma",
        "plataforma": "Nintendo Switch",
        "ano": 2017
    },
    {
        "id": 3,
        "titulo": "Rocket League",
        "genero": "Esporte",
        "plataforma": "Multiplataforma",
        "ano": 2015
    }
]
```

Você poderá utilizar outros jogos se desejar.

---

# 🚀 Endpoints obrigatórios

Sua API deverá possuir **exatamente os seguintes 5 endpoints principais**.

---

## 1. Listar todos os jogos

### Requisição

```http
GET /api/jogos
```

### Exemplo

```text
http://127.0.0.1:5000/api/jogos
```

### Resultado esperado

A API deverá retornar todos os jogos cadastrados.

Exemplo:

```json
[
    {
        "id": 1,
        "titulo": "Minecraft",
        "genero": "Sandbox",
        "plataforma": "PC",
        "ano": 2011
    },
    {
        "id": 2,
        "titulo": "Super Mario Odyssey",
        "genero": "Plataforma",
        "plataforma": "Nintendo Switch",
        "ano": 2017
    }
]
```

---

# 2. Buscar jogo pelo ID

### Requisição

```http
GET /api/jogos/<id>
```

Exemplo:

```text
GET /api/jogos/1
```

A API deverá procurar o jogo utilizando o `id`.

### Caso o jogo exista

Retorne o jogo encontrado.

Exemplo:

```json
{
    "id": 1,
    "titulo": "Minecraft",
    "genero": "Sandbox",
    "plataforma": "PC",
    "ano": 2011
}
```

Código HTTP esperado:

```text
200 OK
```

### Caso o jogo não exista

Exemplo:

```text
GET /api/jogos/50
```

Retorne:

```json
{
    "erro": "Jogo não encontrado"
}
```

Código HTTP:

```text
404 Not Found
```

---

# 3. Cadastrar um novo jogo

### Requisição

```http
POST /api/jogos
```

Os dados deverão ser enviados em formato JSON.

Exemplo:

```json
{
    "titulo": "Fortnite",
    "genero": "Battle Royale",
    "plataforma": "Multiplataforma",
    "ano": 2017
}
```

## Atenção

O cliente **não deverá precisar informar o ID**.

A própria API deverá gerar um novo identificador para o jogo.

Exemplo de resposta:

```json
{
    "id": 4,
    "titulo": "Fortnite",
    "genero": "Battle Royale",
    "plataforma": "Multiplataforma",
    "ano": 2017
}
```

Código HTTP esperado:

```text
201 Created
```

---

# 4. Atualizar um jogo

### Requisição

```http
PUT /api/jogos/<id>
```

Exemplo:

```text
PUT /api/jogos/2
```

JSON enviado:

```json
{
    "titulo": "Super Mario Odyssey",
    "genero": "Plataforma",
    "plataforma": "Nintendo Switch",
    "ano": 2017
}
```

A API deverá:

1. localizar o jogo;
2. atualizar seus dados;
3. retornar o jogo atualizado.

Código esperado:

```text
200 OK
```

Caso o jogo não seja encontrado:

```json
{
    "erro": "Jogo não encontrado"
}
```

Código:

```text
404 Not Found
```

---

# 5. Excluir um jogo

### Requisição

```http
DELETE /api/jogos/<id>
```

Exemplo:

```text
DELETE /api/jogos/3
```

Se o jogo existir, ele deverá ser removido.

Exemplo de resposta:

```json
{
    "mensagem": "Jogo excluído com sucesso"
}
```

Código esperado:

```text
200 OK
```

Caso o jogo não exista:

```json
{
    "erro": "Jogo não encontrado"
}
```

Código:

```text
404 Not Found
```

---

# ⚠️ Validação obrigatória

No cadastro de um novo jogo, verifique se foram informados:

```text
titulo
genero
plataforma
ano
```

Caso algum campo obrigatório não seja enviado, a API deverá retornar uma mensagem de erro.

Exemplo:

```json
{
    "erro": "Todos os campos são obrigatórios"
}
```

Código HTTP sugerido:

```text
400 Bad Request
```

---

# 🌐 Formato das respostas

Todas as respostas da API deverão utilizar **JSON**.

No Flask, você poderá utilizar:

```python
jsonify()
```

Para receber dados enviados pelo cliente, você poderá utilizar:

```python
request.get_json()
```

---

# 💡 Algumas funções que podem ajudar

Você poderá precisar de recursos como:

```python
next()
```

```python
enumerate()
```

```python
append()
```

```python
pop()
```

e estruturas como:

```python
for
```

```python
if
```

Não é obrigatório utilizar exatamente essas funções.

Existem diferentes formas corretas de resolver o problema.

---

# 🧪 Testando sua API

Você poderá utilizar:

* navegador para requisições GET;
* Postman;
* Insomnia;
* Thunder Client;
* REST Client;
* outra ferramenta autorizada pelo professor.

Lembre-se de que o navegador normalmente é suficiente apenas para testar requisições `GET`.

---

# ✅ Testes mínimos

Antes de entregar, verifique:

* [ ] A aplicação Flask inicia sem apresentar erros.
* [ ] `GET /api/jogos` retorna todos os jogos.
* [ ] `GET /api/jogos/1` retorna um jogo.
* [ ] Buscar um ID inexistente retorna erro 404.
* [ ] `POST /api/jogos` cadastra um novo jogo.
* [ ] O ID do novo jogo é gerado pela API.
* [ ] `PUT /api/jogos/<id>` altera um jogo.
* [ ] `DELETE /api/jogos/<id>` remove um jogo.
* [ ] As respostas utilizam JSON.
* [ ] Os códigos HTTP estão adequados.
* [ ] O código está organizado e legível.

---

# 📊 Critérios de avaliação

A prova terá valor total de **10,0 pontos**.

| Critério                                   | Pontuação |
| ------------------------------------------ | --------: |
| Estrutura da aplicação Flask               |       1,0 |
| GET — listar todos os jogos                |       1,0 |
| GET — buscar jogo pelo ID                  |       1,0 |
| POST — cadastrar novo jogo                 |       1,5 |
| PUT — atualizar jogo                       |       1,5 |
| DELETE — excluir jogo                      |       1,5 |
| Tratamento de erros e códigos HTTP         |       1,0 |
| Organização e legibilidade do código       |       0,5 |
| API funcionando corretamente como conjunto |       1,0 |
| **Total**                                  |  **10,0** |

---

# 📤 Entrega

Entregue o projeto conforme orientação do professor.

O arquivo principal deverá ser:

```text
app.py
```

Antes de entregar, execute:

```bash
python app.py
```

e confirme que a aplicação inicia corretamente.

---

# 🚫 Regras

* O projeto deverá utilizar Flask.
* Não será necessário utilizar banco de dados.
* Todos os endpoints solicitados deverão funcionar.
* As respostas da API deverão utilizar JSON.
* O aluno deverá ser capaz de explicar o código desenvolvido caso seja solicitado.
* Trabalhos que não executarem poderão receber pontuação parcial conforme os itens implementados.

---

# 🏁 Desafio

Você deverá demonstrar que consegue aplicar os principais conceitos estudados durante as aulas:

**API REST + Flask + JSON + CRUD + métodos HTTP + códigos de resposta HTTP.**

Boa prova! 🚀
