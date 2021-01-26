import requests
import pandas as pd

key = 'AIzaSyBiDy3cd0SXe-l-Ku4KqeLgOk85lURvgHs'
data = pd.read_excel (r'C:\Projects\Covid19\health_all_26-Jan-2021.xlsx') 
df = pd.DataFrame(data, columns= ['ชื่อ','รหัสจังหวัด'])

for index, row in df.iterrows():
    print(index, row['ชื่อ'])

    components = "route:" + row['ชื่อ'] + "|administrative_area:" + row['รหัสจังหวัด'][3:] + "|country:Thailand"
    URL = "https://maps.googleapis.com/maps/api/geocode/json?components=" + components
    PARAMS = {'key':key,'components':components} 
    r = requests.get(url = URL, params = PARAMS) 
    data = r.json()
    #print(data)
    try:

       latitude = data["results"][0]["geometry"]["location"]["lat"]
       longitude = data["results"][0]["geometry"]["location"]["lng"]	
       df.loc[index,'lat'] = latitude
       df.loc[index,'long'] = longitude
    except:
        print('======================')
        print(row['ชื่อ'])
        print(data)
        print('======================')
df.to_excel('result.xlsx', sheet_name='location for hospital or clinic')