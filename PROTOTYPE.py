import pandas as pd
'''THIS IS DUMMY DATA'''
# service provider provided information
data = {
    "SERVICE" : ["haircut","utensils","laptop rent","car washing","haircut"],
    "COST":[150,600,300,700,200],
    "LOCATION":["dehradun","jaipur","delhi","london","rampur"]
}
df = pd.DataFrame(data)
# consumer provided information

service_need = input("enter the service you want:").lower()
budget = int(input("enter the budget:"))
venue = input("enter the location:")

found_service = df[df["SERVICE"] == service_need]
if found_service["SERVICE"].empty:
    print("your desired service is not available")
else:
    afford = found_service[found_service["COST"]<=budget]
    if afford.empty:
        print("your budget is low")
    else:
        access = found_service[found_service["LOCATION"] != venue]
        if access.empty:
            print("not available in your location")
        else:
            print("enjoy your service")
# like this many more service we will include in this
#still working on longitude and latitudes apart of this prototype
