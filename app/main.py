from fastapi import FastAPI
from app.manager import Manager


manager = Manager()
manager.run()

app = FastAPI()

@app.get('/')
def home():
    return {"Active": "server is running!"}

@app.get('/data')
def get_data():
    result = manager.get_data_result()
    return {"result": result}



