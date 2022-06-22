import requests
import json
import tabulate

def pin_me(pincode):
    url="https://api.postalpincode.in/pincode/"+pincode
    x = requests.get(url)
    print(x.status_code)
    val1=x.text
    val2=json.loads(val1)[0]['PostOffice']
    header=val2[0].keys()
    rows =  [x.values() for x in val2]


    print(tabulate.tabulate(rows,header))


pincode=str(input("Enter pincode:"))
pin_me(pincode)
