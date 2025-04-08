import json 
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline 

filename = 'data/past_30days.json'
with open(filename,encoding = "utf8") as fp:
    eq_data = json.load(fp)

readable_file = 'data/read_past_30days.json'
with open(readable_file, 'w') as f: 
    json.dump(eq_data,f,indent = 4) 


eq_dicts = eq_data['features']

mags = [eq_dict['properties']['mag'] for eq_dict in eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in eq_dicts]
hover_text =[eq_dict ['properties']['title'] for eq_dict in eq_dicts]

# data = [Scattergeo(lon = lons, lat = lats)]
data = [{
    'type' : 'scattergeo',
    'lon' : lons ,
    'lat' : lats ,
    'text' : hover_text,

    
    'marker' : {
        'size' : [5*abs(mag) for mag in mags],
        'color' : mags,
        'colorscale' : 'Portland', 
        # 'reversescale' : True,
        'colorbar':{'title':'Magnitude'},
    },
}]
auto_title = eq_data['metadata']['title']
my_layout = Layout(title = auto_title)

fig = {'data' : data, 'layout':my_layout}
offline.plot(fig,filename = 'data/global_earthquake.html')