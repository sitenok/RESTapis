from fastapi import FastAPI

app1 = FastAPI()

numbers = []

#### Functions which deal with GET, POST... (browser stuff)
@app1.get("/")
async def showMessage():
    return {"result": "This is the root. Nothing else."}


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
        if newNum in numbers: # if number already exists in list, increment counter
            result = True
            numbers[newNum] = numbers[newNum] + count
            message = (f"Existing and added item(s): {newNum}.")
        else: # a new number added which didn't exist before
            result = True
            message = (f"Successfully added: {newNum}.")
            numbers[newNum] = count
    else:
        print(f"{newNum} is not an integer. Please input an integer.")

    return {"Result": result, "Message": message, "Numbers": numbers}
    return {"result": "OK"}

# Get average of all numbers
@app1.get("numbers/average")
async def average():
    if len(numbers) > 0: # check that list contains numbers
        average = sum(numbers) / len(numbers)
        print(f"The average of all numbers stored is: {average}")
    else: 
        print("Please input values first.")
    return{"result": "111"}


# Get sum of all numbers
@app1.get("numbers/sum")
async def sum():
    if len(numbers) > 0: # check that list contains numbers
        sum = sum(numbers)
        print(f"The sum of all numbers stored is: {sum}")
    else: 
        print("Please input values first.") 
    return{"result": "111"}

# Get standard deviation of numbers list
@app1.get("numbers/stddev")
async def stddev():
    if len(numbers) > 0: # check that list contains numbers
        l = len(numbers)
        mean = sum(numbers) / l
        variance = sum((i - mean)**2 for i in numbers) / l
        stddev = variance ** 0.5 # square root of variance (power of a 1/2)
        print(f"The standard deviation of numbers stored is: {stddev}")
    else: 
        print("Please input values first.")
    return{"result": "111"} 
 

#### Other Functions
def getNumbers():
    return(numbers)


# if __name__ == "__main__":
#     uvicorn.run("example:app", host="127.0.0.1", port=5000)