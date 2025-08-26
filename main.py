from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/hello/{item_id}")
def read_item(item_id: int):
    return {"message": f"Hello {item_id}"}
  
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"message": f"Hello Item {item_id}"}
