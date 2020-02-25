from fastapi import FastAPI

app = FastAPI()
# to see what funny will come
app.counter = 0

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/counter')
def counter():
	app.counter += 1
	return str(app.counter)