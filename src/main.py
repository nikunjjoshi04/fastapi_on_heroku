from fastapi import FastAPI
from starlette.responses import RedirectResponse
from loguru import logger

app = FastAPI(title="Fastapi on Heroku")


@app.get("/")
async def read_root():
    return RedirectResponse(url='/docs#')


@app.get("/index")
async def index():
    logger.debug("[debug] Index is calling...!")
    logger.info("[info] Index is calling...!")
    logger.success("[success] Index is calling...!")
    logger.warning("[warning] Index is calling...!")
    logger.error("[error] Index is calling...!")
    logger.critical("[critical] Index is calling...!")
    return {"message": "Hello Nikka...!"}
