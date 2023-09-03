from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints import main_router

app = FastAPI(
    title='AI API Demo'
)
app.include_router(main_router)
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Adjust this to be more specific for security concerns
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
