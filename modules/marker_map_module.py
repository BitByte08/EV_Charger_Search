import folium
from folium import Marker, FeatureGroup, TileLayer
from folium.plugins import MarkerCluster, LocateControl
class MarkerMap:
    def __init__(self):
        self.m = folium.Map(location = [37.564214, 127.001699], zoom_start = 14 )
        self.mc = MarkerCluster()
        self.group_list = {}
        LocateControl().add_to(self.m)
        TileLayer(tiles="CartoDB positron").add_to(self.m)
    def set_ping(self,df):
        pings = df.values.tolist()
        for ping in pings:
            self.mc.add_child(
                folium.Marker(
                    location = [float(ping[0]),float(ping[1])],
                    tooltip=ping[2],
                    popup="<div style='weight: 3rem;'>{0}</div>".format(str(ping[3]))
                )
            )
        self.m.add_child(self.mc)
    def save_map(self,name):
        self.m.save('templates/{0}.html'.format(name))