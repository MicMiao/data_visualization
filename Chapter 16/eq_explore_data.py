import json

# Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f) 
    
# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4) 
    
    
all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))


# Pull the magnitude of each earthquake:
mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
    
# print(mags[:10])

# Pull the location data for each earthquake:
lons, lats = [], []
for eq_dict in all_eq_dicts:
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    lons.append(lon)
    lats.append(lat)
    
# print(lons[:5])
# print(lats[:5])







   







