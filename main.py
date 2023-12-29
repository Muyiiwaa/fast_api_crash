from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

# instantiate the app

app = FastAPI()

# set up a simple route

@app.get("/")
async def root():
    return {'message: "Hello world"'}

@app.post("/")
async def post():
    return {"message: 'Hello from the post world'"}

@app.put("/")
async def do_something():
    return {"message: 'hello from the put route'"}

@app.get("/items")
async def list_items():
    return {"message: 'list item route'"}

@app.get("/items/{item_id}")
async def get_items(item_id: int):
    return {"item_id": item_id}

@app.get("/lcm")
async def get_lcm(x: int, y:int):
    """_summary_

    Args:
        x (int): _description_
        y (int): _description_

    Returns:
        _type_: _description_
    """
    if x > y:
        greater = x 
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            break
        else:
            greater += 1
        
    return {"lcm": greater}

class FoodEnum(str, Enum):
    swallow = "swallow"
    vegies = "vegies"
    alcohol = "Alcohol"
    

@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.swallow:
        return {"message: 'You are heavy'"} 
    elif food_name == FoodEnum.vegies:
        return {"message: 'you are healthy'"}
    else:
        return {"message: 'you are an unhealthy alcoholic!"}
    
@app.get("/check_prime")
async def solver(number : int):
    for i in range(2, number):
        if number % i == 0:
            return f'{number} is not Prime'
    else:
        return f'{number} is prime'
        

class Item(BaseModel):
    name : str
    description : str | None = None
    price : float
    tax : float | None = None
    
@app.post("/items")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        gross = item.price + item.tax
        item_dict.update({"gross_price": gross})
    
    return item_dict

@app.put("/items/{item_id}")
async def create_item_with_put(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({'q': q})
    return result

  
@app.get("/item")
async def read_items(q: str | None = None):
    results = {"items": [{"item": "tomi"}, {"item": "abeke"}]}
    if q:
        results.update({"q": q})
    return results
    