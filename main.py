from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from modules.marker_map_module import MarkerMap
from modules.csv_read_module import CsvReader
app = FastAPI()
map = MarkerMap()
data = CsvReader("charger_data.csv",["위도","경도","충전소명","충전소주소"])
map.set_ping(data.get_data())
map.save_map("charger_map")
templates = Jinja2Templates(directory="templates")
@app.get("/")
def root(request: Request):
    count = len(data.get_data())
    return templates.TemplateResponse("index.html",
                                      {"request": request,
                                       "count": count,
                                        "avg": int(count / len(data.get_group()))}
                                      )
@app.get("/map")
def map(request: Request):
    return templates.TemplateResponse("charger_map.html", {"request": request})
@app.get("/search")
def search(value: str, request: Request):
    search_result = data.search_data(value)
    return templates.TemplateResponse("search.html",
                                      {"request": request,
                                       "data": search_result,
                                       "value": value,
                                       "count": len(search_result)}
                                      )
