from fastapi import FastAPI

app = FastAPI(title="Financeiro API", version="0.1.0")


@app.get("/", tags=["root"])
async def root() -> dict[str, str]:
    return {"message": "Financeiro API"}


@app.get(
    "/health", tags=["health"]
)  # nome[x] sem = antes = acesso a algo que já existe. nome=[x] = criação/atribuição de um valor a um parâmetro ou variável.
async def health_check() -> dict[str, str]:
    return {"status": "ok"}


"""
**Resumo**

O que vimos até aqui:

- Você decidiu usar um fluxo simples com `dev` agora e criar `main` depois, quando tiver algo funcionando.
- A ideia ficou assim: `dev` é onde você programa; `main`, no futuro, será a versão estável.
- Vimos que o projeto é um app financeiro com MVP manual: usuários, contas, categorias, transações e dashboard.
- Decidimos que o backend deve começar pequeno: primeiro fazer a API subir e responder `/` e `/health`.
- Também vimos que os endpoints `GET`, `POST`, `PUT`, `DELETE` não devem ficar todos no `main.py`; depois eles devem ir para módulos, tipo `accounts`, `auth`, `categories`, `transactions`.

**O Que Foi Feito**

Olhando o projeto agora:

- Você está na branch `dev`.
- O arquivo `backend/main.py` foi removido.
- O arquivo [backend/app/main.py](C:/Users/potat/Documents/financeiro-app/backend/app/main.py:1) agora tem a base do FastAPI.
- Nele já existe uma rota raiz `/`.
- Também foi criada uma rota `/health`.
- A estrutura `backend/app/modules/` já existe com pastas para:
  - `accounts`
  - `auth`
  - `categories`
  - `transactions`
  - `users`

**Pontos Para Corrigir Antes De Rodar**

Tem três ajustes importantes:

- Em [backend/app/main.py](C:/Users/potat/Documents/financeiro-app/backend/app/main.py:13), a rota `/health` está com um erro pequeno: foi escrito `tags["health"]`, mas deveria ser uma atribuição de parâmetro.
- Em [backend/app/main.py](C:/Users/potat/Documents/financeiro-app/backend/app/main.py:1), existem imports desnecessários de `sys` e `turtle`.
- Em [backend/pyproject.toml](C:/Users/potat/Documents/financeiro-app/backend/pyproject.toml:10), tem um provável erro de digitação em `fastapi[standar,standard]`.
- Em [backend/pyproject.toml](C:/Users/potat/Documents/financeiro-app/backend/pyproject.toml:29), o entrypoint ainda aponta para `backend.main:app`, mas agora o app principal está em `backend/app/main.py`.

**Próximo Passo**

Eu faria agora só uma limpeza pequena:

```txt
corrigir app/main.py
corrigir pyproject.toml
rodar a API
testar / e /health
```

Depois disso, aí sim vale começar o primeiro módulo real, provavelmente `accounts`.
"""
