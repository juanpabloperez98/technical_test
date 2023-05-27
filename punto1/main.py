import requests
import pandas as pd
import json
import os

from urls import url,urlIncidente,urlInfoJuicio,urlActuaciones
from vars import payload,headers,params

proceso_actor = ["0968599020001","0992339411001"]
proceso_demandado = ["1791251237001","0968599020001"]

def get_data(df_procesos,id_jucio,type_):
    data_incidente = requests.get(urlIncidente+id_jucio)
    data_incidente = json.loads(data_incidente.text)
    data_info_juicio = requests.get(urlInfoJuicio+id_jucio)
    data_info_juicio = json.loads(data_info_juicio.text)
    df_incidentes = pd.DataFrame(data_incidente)
    df_info_juicio = pd.DataFrame(data_info_juicio)
    concatenated_frames = pd.concat([df_incidentes, df_info_juicio], axis=1)
    df_poceso_juicio = df_procesos.loc[df_procesos["idJuicio"] == id_jucio]
    dataframe_all = pd.merge(df_poceso_juicio,concatenated_frames, on="idJuicio")
    if type_ == 0:
        dataframe_all['tipo'] = "actor"
    elif type_ == 1:
        dataframe_all['tipo'] = "demandado"
    return dataframe_all
    

def star_request(type_, identificador):
    """
        Este método realiza varias peticiones a la página "Consulta de Procesos Judiciales"
        Para obtener datos sobre procesos judiciales
        
        variables
            type_ : Define si la consulta a tratar es de Actor o Demandado
            type_ = 0 -> Actor
            type_ = 1 -> Demandado 
            
            identificador: CC/RUC
            
    """
    if type_ == 0:
        payload["actor"]["cedulaActor"] = identificador
    elif type_ == 1:
        payload["demandado"]["cedulaDemandado"] = identificador
    else:
        print("Tipo no valido")
        return
    
    list_actor_demandado = ["actor","demandado"]
    req = requests.post(url, json=payload, headers=headers)
    if req.status_code == 200 and req.text != '[]':
        data = json.loads(req.text)
        df_procesos = pd.DataFrame(data)
        id_juicio_list = df_procesos["idJuicio"].tolist()
        list_data_frames = []
        for id_jucio in id_juicio_list:   
            dataframe_all = get_data(df_procesos=df_procesos,id_jucio=id_jucio,type_=type_) 
            list_data_frames.append(dataframe_all)
        concated_dataframes = pd.concat(list_data_frames)
        path = os.path.abspath(os.getcwd())
        path = os.path.dirname(path)
        src = f"{path}\\api\data\\{list_actor_demandado[type_]}_{identificador}.csv"
        concated_dataframes.to_csv(src,index=False)
    else:
        print("No hay coincidencias")


if __name__ == "__main__":
    type_ = int(input("Ingrese tipo 0 Actor - 1 Demandado: "))
    identificador = input("Ingrese identificador: ")
    star_request(type_,identificador)