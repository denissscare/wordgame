from fastapi import APIRouter

game = APIRouter(prefix='/game', responses={404: {"description": "NOT FOUND"}})

