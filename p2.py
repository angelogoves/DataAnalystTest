import pandas as pd
from haversine import haversine
import numpy as np
import os
import datetime

trip_info = ["trip_id", "transporter_name", "quantity", "vehicle_number", "date_time"]
details = ["fk_asset_id", "lic_plate_no", "lat", "lon", "lname", "tis", "spd", "harsh_acceleration", "hbk", "osf"]
output = ["License_plate_number", "Distance", "Number_of_Trips_Completed", "Average_Speed", "Transporter_Name",
          "Number_of_Speed_Violations"]

"""
for q in range(len(data)):
    for each in data:
        if data[q][0] == each[0]:
            print(each[0],q)
output = ["License_plate_number", "Distance", "Number_of_Trips_Completed", "Average_Speed",
                      "Transporter_Name",
                      "Number_of_Speed_Violations"]
"""
# ddd = pd.DataFrame(data, columns=output)
ddd = pd.read_csv("file11.csv")
dummylist = ddd.values.tolist()

to_pop = []
new_data = []

for i in range(len(dummylist)):
    for j in range(i + 1, len(dummylist)-1):
        #print(dummylist[j][0], dummylist[i][1], dummylist[j][1])
        if dummylist[i][1] == dummylist[j][1]:
            a = dummylist[i][2] + dummylist[j][2]
            b = dummylist[i][3] + dummylist[j][3]
            temp = dummylist[i][4] + dummylist[j][4]
            c = temp / 2.0
            d = dummylist[i][6] + dummylist[j][6]

            dummylist[i][2] = a
            dummylist[i][3] = b
            dummylist[i][4] = c
            dummylist[i][6] = d
            print(dummylist[i])
            dummylist.pop(j)

for p in dummylist:
    for q in new_data:
        if p not in new_data:
            if q[1] == p[1]:
                d = p[-5] + q[-5]
                e = p[-4] + q[-4]
                temp = p[-3] + q[-3]
                f = temp / 2.0
                g = p[-1] + q[-1]
                # print(p[1], d, e, f, p[-2], g)
            else:
                new_data.append(p)

"""
    for q in ddd.values:
        if q[0] > p[0]:
            if p[-6] == q[-6]:
                d = p[-5] + q[-5]
                e = p[-4] + q[-4]
                temp = p[-3] + q[-3]
                f = temp / 2.0
                g = p[-1] + q[-1]
                to_pop.append(q[0])
                print(q[0])
        else:
            print(q[0], "---------------",p[0])
    dummylist[p[0]][-1] = g
    dummylist[p[0]][-3] = f
    dummylist[p[0]][-4] = e
    dummylist[p[0]][-5] = d

    print(p)
    if p[0] == 10:
        break"""
new = []
to_pop.sort()
for z in to_pop:
    if z not in new:
        new.append(z)

for x in dummylist:
    if x[0] in new:
        dummylist.pop(x[0])

"""
ddd.loc[p[0], ["License_plate_number", "Distance", "Number_of_Trips_Completed", "Average_Speed",
               "Transporter_Name",
               "Number_of_Speed_Violations"]] = [p[1], d, e, f, p[-2], g]

ddd.to_csv("111.csv")
"""
