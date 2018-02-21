import urllib.request
import json
import matplotlib.pyplot as plt


def get_api_data(method = ""):
    api_url = "https://data.sfgov.org/resource/2iym-9kfb.json"
    url = api_url + '?' + method.replace(" ", "%20")
    print(url)
    data = urllib.request.urlopen(url).read().decode()
    return json.loads(data)

# Get data via API
query = '$query=SELECT ratearea as area, count(*) GROUP BY ratearea ORDER BY count DESC'
parking_meter_data = get_api_data(query)

area_list = [i.get('area') for i in parking_meter_data]
num_list = [int(i.get('count', 0)) for i in parking_meter_data]

# Visualization
plt.bar(range(len(num_list)), num_list, align='center')
plt.xlabel('AREA')
plt.ylabel('Nnumber of Parking Meters')
plt.subplots_adjust(bottom=0.15)
plt.xticks(range(len(area_list)), area_list, rotation=30)
plt.title('Total parking meters per AREA')
plt.savefig('figure')
plt.show()