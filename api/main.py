from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    # return url_shortener_service.handle_root()
    return {"message" : "Healthcheck successful"}