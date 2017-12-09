import requests
from flask import Flask, abort, request


apikey = '759679faf68df6d2af7c299d24096000'

app = Flask(__name__)

def get_data ():
    url = "http://api.data.mos.ru/v1/datasets/2009/rows?api_key=%s" % apikey
    result = requests.get(url)
    return result.json()

@app.route("/names")
def disp_names():
    all_table = get_data()
    result_table = []
    for i in all_table:
        row = []
        cells = i["Cells"]
        name = cells["Name"]
        row.append("<td>%s</td>" %name)
        year = cells["Year"]
        row.append("<td>%s</td>" %year)
        month = cells["Month"]
        row.append("<td>%s</td>" %month)
        count = ["NumberOfPersons"]
        row.append("<td>%s</td>" %count)
        result_table.append("<tr>%s</tr>" %row)
    return "<table><tr><th>Name</th><th>Year</th><th>Month</th><th>NumberOfPersons</th></tr>%s</table>" %result_table

if __name__ == "__main__":
    app.run(port=5010, debug=True)
 
