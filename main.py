from fastapi import FastAPI
from api.routers import analysis

app = FastAPI(title="Agentic Backend", description="API de Análise de Dados")

@app.get("/", include_in_schema=False)  
def root():
    return {"status": "API online", "docs": "Acesse /docs ou /redoc"}

app.include_router(analysis.router, prefix="/api")