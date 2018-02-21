import urllib.request
import json
import matplotlib.pyplot as plt


def get_api_data(method=""):
    api_url = "https://data.sfgov.org/resource/2iym-9kfb.json"
    url = api_url + '?' + method.replace(" ", "%20")
    print(url)
    data = urllib.request.urlopen(url).read().decode()
    return json.loads(data)


def plot_bar_graph(x, y, title="", xlabel="", ylabel=""):
    plt.bar(range(len(y)), y, align='center')
    plt.xticks(range(len(x)), x, rotation=30)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.subplots_adjust(bottom=0.15)
    plt.title(title)
    plt.savefig('figure')
    plt.show()


# Get data via API
query = '$query=SELECT ratearea as area, count(*) GROUP BY ratearea ORDER BY count DESC'
parking_meter_data = get_api_data(query)

area_list = [i.get('area') for i in parking_meter_data]
num_list = [int(i.get('count', 0)) for i in parking_meter_data]

# Visualization
plot_bar_graph(area_list, num_list, 'Total parking meters per AREA', 'AREA', 'Number of parking Meters')
