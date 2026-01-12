from fastapi import FastAPI
from apis.auth import route as r1
from apis.Product import router as r2
from apis.order import router as r3
from apis.address import router as r4
from apis.cart import router as r5
from core import database as db
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()
app.add_middleware(middleware_class=CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )
db.base.metadata.create_all(bind=db.eng)



app.include_router(router=r1)
app.include_router(router=r2)
app.include_router(router=r3)
app.include_router(router=r4)
app.include_router(router=r5)


