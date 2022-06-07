from fastapi import FastAPI

app1 = FastAPI()

numbers = {0,}

#### Functions which deal with GET, POST... (browser stuff)
@app1.get("/")
async def showMessage():
    return {"result": "this is the root. Nothing else."}

# GET functions to catch errors in link with slash or no slash
@app1.get("/numbers") 
async def getNumbers1():
    return getNumbers()

@app1.get("/numbers/")
async def getNumbers2():
    return getNumbers()

# Add new numbers
@app1.post("/numbers")
async def addNumber(newNum: int, count: int = 1):
    result = False
    message = "Not specified"
    if ( newNum.isdigit() ):  # make sure input is an integer
        if newNum in numbers:
            numbers[newNum] = numbers[newNum] + count
            result = True
            message = (f"Existing and added item(s): {newNum}.")
        else:
            result = True
            message = (f"Successfully added: {newNum}.")
            numbers[newNum] = count
    else:
        print(f"{newNum} is not an integer. Please input an integer.")

    return {"Result": result, "Message": message, "Numbers": numbers}


#### Other Functions
def getNumbers():
    return [""]