import pandas as pd
from haversine import haversine
import numpy as np
import os
import datetime

trip_info = ["trip_id", "transporter_name", "quantity", "vehicle_number", "date_time"]
details = ["fk_asset_id", "lic_plate_no", "lat", "lon", "lname", "tis", "spd", "harsh_acceleration", "hbk", "osf"]
output = ["License_plate_number", "Distance", "Number_of_Trips_Completed", "Average_Speed", "Transporter_Name",
          "Number_of_Speed_Violations"]

df = pd.read_csv("Trip-Info.csv")

data = []
i = j = 0
df_main = df[['vehicle_number', 'transporter_name']]
for each in df_main.values:
    i += 1
    l = []
    dist = violations = count = 0
    speed = 0.0
    l.append(each[0])
    path = str(f"EOL-dump\\{each[0]}.csv")
    if os.path.exists(path):
        df2 = pd.read_csv(path)
        df1 = df2[["lat", "lon", "tis", "spd", "harsh_acceleration", "hbk", "osf"]]
        x1 = x2 = y1 = y2 = 0
        j += 1
        for z in df1.values:
            # print(z[3])
            x2 = z[0]
            y2 = z[1]
            if x1 != 0 or x2 != 0 or y1 != 0 or y2 != 0:
                x = (x1, x2)
                y = (y1, y2)
                d = haversine(x, y, unit='km')
                isNaNd = np.isnan(d)
                if isNaNd:
                    pass
                else:
                    dist += d
            x1 = x2
            y1 = y2
            isNaN = np.isnan(z[3])
            if isNaN:
                pass
            else:
                speed += z[3]
                count += 1
                # print(speed)

            if z[4]:
                violations += 1
            if z[5]:
                violations += 1
            if z[6]:
                violations += 1
            # print(z)
            # l.append(datetime.datetime.fromtimestamp(z))
        # print(j,speed,count,violations)
        avg_speed = speed / count
        l.append(dist)
        l.append(1)
        l.append(avg_speed)
        l.append(each[1])
        l.append(violations)
        data.append(l)
        print(l,"\t\t",j)
    print(i)


for q in range(len(data)):
    for each in data:
        if data[q][0] == each[0]:
            print(each[0],q)
output = ["License_plate_number", "Distance", "Number_of_Trips_Completed", "Average_Speed",
                      "Transporter_Name",
                      "Number_of_Speed_Violations"]

ddd = pd.DataFrame(data, columns=output)
#print(ddd.dtypes)
ddd.to_csv('file111.csv')

print("\ni = ",i,"\t\tj = ",j)
