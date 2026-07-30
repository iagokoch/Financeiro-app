from fastapi import FastAPI

app = FastAPI(title="Financeiro API", version="0.1.0")


@app.get("/", tags=["root"])
async def root() -> dict[str, str]:
    return {"message": "Financeiro API"}


@app.get("/health", tags=["health"])
async def health_check() -> dict[str, str]:
    return {"status": "ok"}
