import json
# import urllib library
from urllib.request import urlopen 

user_id = 1704
limit = 1000
url = "https://api2.lowfuelmotorsport.com/api/users/getUsersPastRaces/" + str(user_id) + "?start=0&limit=" + str(limit)
  
# store the response of URL
response = urlopen(url)
counter = 0
data = json.loads(response.read())


#try:
#    for x in range(limit):
#        time = data[x]["race_date"]
#        car = data[x]["car_name"]
#        event_name = data[x]["event_name"]
#        start_pos = data[x]["start_pos"]
#        finishing_pos = data[x]["finishing_pos"]
#        ip = data[x]["incidents"]
#        elo = data[x]["rating_change"]
#        track = data[x]["track_name"]
#        sr = data[x]["sr_change"]
    #    print("You completed a " + event_name + " race on " + track + " with the " + car + ", you started " + start_pos + " and finished " + finishing_pos + ". You gained " + elo + " Elo and " + sr + " SR with " + ip + " incident points.\n")
#        tits = time + "\t" + car + "\t" + event_name + "\t" + track + "\t" + str(start_pos)  + "->" + str(finishing_pos) + "\t" + str(elo) + "\t" +  str(sr)  + "(" + str(ip) + ")"
#        print(tits)
#        counter += 1
#except:
#    print(str(counter) + "/" + str(limit) + " tracks")
# counter = 0

unique_tracks = []
try:
    for x in range(limit):
        if data[x]["track_name"] not in unique_tracks:
            unique_tracks.append(data[x]["track_name"])
 #           print(data[x]["track_name"])
except:
    print()

for x in unique_tracks:
    print(x)

tracks = []
tracks.append(unique_tracks)
track_counter = []

for x in unique_tracks:
    track_counter.append(int(0))

try:
    for x in range(limit):
        if(data[x]["track_name"]) in unique_tracks:
            # index = unique_tracks.index(data[x]["track_name"])
            track_counter[unique_tracks.index(data[x]["track_name"])] += 1
            # print(test =+ 1)
            # print(data[x]["track_name"] + " " + str(track_counter[unique_tracks.index(data[x]["track_name"])]))
except:
   print()

for x in range(len(track_counter)):
    print(unique_tracks[x] + " = " + str(track_counter[x]))


unique_cars = []
try:
    for x in range(limit):
        if data[x]["car_name"] not in unique_cars:
            unique_cars.append(data[x]["car_name"])
except:
    print()

for x in unique_cars:
    print(x)

cars = []
cars.append(unique_cars)
car_counter = []

for x in unique_cars:
    car_counter.append(int(0))

try:
    for x in range(limit):
        if(data[x]["car_name"]) in unique_cars:
            # index = unique_tracks.index(data[x]["track_name"])
            car_counter[unique_cars.index(data[x]["car_name"])] += 1
            # print(test =+ 1)
            # print(data[x]["track_name"] + " " + str(track_counter[unique_tracks.index(data[x]["track_name"])]))
except:
   print()

for x in range(len(car_counter)):
    print(unique_cars[x] + " = " + str(car_counter[x]))