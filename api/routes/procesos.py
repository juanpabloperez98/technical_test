from fastapi import APIRouter, Query
from middlewares.verify_token_route import VerifyTokenRoute
from schemas.procesos import Filter
from helpers.payload_proceso import payload, params
from fastapi.responses import JSONResponse

import requests
import json
import pandas as pd
import os



procesos_route = APIRouter(route_class=VerifyTokenRoute)

@procesos_route.get("/get_procesos/{type_}/{id}")
def get_procesos(type_: int, id: str):
    name_file = ""
    if(type_ == 0):
        name_file = f"actor_{id}.csv" 
    elif(type_ == 1):
        name_file = f"demandado_{id}.csv" 
    else:
        return JSONResponse(content={
            "msg": "Actor or demandado is necessary to make request"
        })
    path = os.path.abspath(os.getcwd())
    file_path = f"{path}\data\\{name_file}"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df_json = df.to_json(orient='records')
        data_json = json.loads(df_json)
        return JSONResponse(content=data_json)
    else:
        return JSONResponse(content={
            "msg": "File dont exits"
        }, status_code=400)
        