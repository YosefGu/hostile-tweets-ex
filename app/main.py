from fastapi import FastAPI


app = FastAPI()


@app.get('/data')
def get_data():
    pass
