from fastapi import FastAPI
from endpoints import main_router

app = FastAPI(
    title='AI API Demo'
)
app.include_router(main_router)