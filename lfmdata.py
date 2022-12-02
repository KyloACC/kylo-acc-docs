import json
# import urllib library
from urllib.request import urlopen 
import sys

user_id = int(sys.argv[1])
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

def find_tracks():
    unique_tracks = []
    try:
        for x in range(limit):
            if data[x]["track_name"] not in unique_tracks:
                unique_tracks.append(data[x]["track_name"])
     #           print(data[x]["track_name"])
    except:
        print()
    return unique_tracks    


def count_tracks(unique_tracks):
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

    return track_counter

def find_cars():
    unique_cars = []
    try:
        for x in range(limit):
            if data[x]["car_name"] not in unique_cars:
                unique_cars.append(data[x]["car_name"])
    except:
        print()
    return unique_cars        

def count_cars(unique_cars):
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

    return car_counter

def Convert(lst1, lst2):
    it1 = iter(lst1)
    it2 = iter(lst2)
    res_dct = dict(zip(it1, it2))
    return res_dct

def Convert3(lst1, lst2, lst3):
    it1 = iter(lst1)
    it2 = iter(lst2)
    it3 = iter(lst3)
    res_dct = dict(zip(zip(it1, it2), it3))
    return res_dct    

def count_tracks_and_cars(unique_tracks, unique_cars):
    counter = []

    for x in unique_tracks:
        for y in unique_cars:
            counter.append(int(0))

    try:
        for x in range(limit):
            if(data[x]["track_name"]) in unique_tracks:
                if(data[x]["car_name"] in unique_cars):
                # index = unique_tracks.index(data[x]["track_name"])
                    counter[(unique_cars.index(data[x]["car_name"])) * (len(unique_tracks)) + (unique_tracks.index(data[x]["track_name"]))] += 1
                # print(test =+ 1)
                # print(data[x]["track_name"] + " " + str(track_counter[unique_tracks.index(data[x]["track_name"])]))
    except:
       print()

#    for x in range(len(track_counter)):
#        print(unique_tracks[x] + " = " + str(track_counter[x]))

    return counter

def count_something(unique_tracks, unique_cars, something):
    counter = []

    for x in unique_tracks:
        for y in unique_cars:
            counter.append(int(0))

    try:
        for x in range(limit):
            if(data[x]["track_name"]) in unique_tracks:
                if(data[x]["car_name"] in unique_cars):
                # index = unique_tracks.index(data[x]["track_name"])
                    counter[(unique_cars.index(data[x]["car_name"])) * (len(unique_tracks)) + (unique_tracks.index(data[x]["track_name"]))] += data[x][something]

                # print(test =+ 1)
                # print(data[x]["track_name"] + " " + str(track_counter[unique_tracks.index(data[x]["track_name"])]))
    except:
       print()

#    for x in range(len(track_counter)):
#        print(unique_tracks[x] + " = " + str(track_counter[x]))
    i = range(len(counter))
    for j in i:
          counter[j] = round(counter[j], 3)
    
    return counter


def find_car_track(cars, tracks):
    lst = []
    for x in tracks:
        for y in cars:
            input = (x + " at " + y)
            if input not in lst:
                lst.append(input)
    return lst;

def per_race(key, count, data):
    values = []
    length = range(len(key)-1)
    for x in length:
        if(count[x] >= 3):
            values.append(round(data[x] / count[x], 3))

        else:
            values.append(-10000)

    return values

def start_finish(start, finish):
    values = []
    length = range(len(start)-1)
    for x in length:
        values.append(round(finish[x] - start[x], 3))
    return values;        

def Sort(dictio):
    dic2=dict(sorted(dictio.items(),key= lambda x:x[1], reverse=True))
    return dic2

def Sort_inverse(dictio):
    dic2=dict(sorted(dictio.items(),key= lambda x:x[1], reverse=False))
    return dic2    

def PruneDict(MyDict, number):
    MyDict = {key:val for key, val in MyDict.items() if val != number}
    return MyDict

def PruneNDict(MyDict, n):
    MyDict = dict(list(MyDict.items())[:n])
    return MyDict


def main():
    unique_tracks = find_tracks()
    unique_cars = find_cars()
    unique_car_and_track = find_car_track(unique_tracks, unique_cars)

    track_counter = count_tracks(unique_tracks)
    car_counter = count_cars(unique_cars)
    car_and_track = count_tracks_and_cars(unique_tracks, unique_cars)
    
    elo_car_track = count_something(unique_tracks, unique_cars, "rating_change")
    sr_car_track = count_something(unique_tracks, unique_cars, "sr_change")
    ip_car_track = count_something(unique_tracks, unique_cars, "incidents")
    start_car_track = count_something(unique_tracks, unique_cars, "start_pos")
    finish_car_track = count_something(unique_tracks, unique_cars, "finishing_pos")

    elo_car_track_per_race = per_race(unique_car_and_track, car_and_track, elo_car_track)
    ip_car_track_per_race = per_race(unique_car_and_track, car_and_track, ip_car_track)
    sr_car_track_per_race = per_race(unique_car_and_track, car_and_track, sr_car_track)
    start_car_track_per_race = per_race(unique_car_and_track, car_and_track, start_car_track)
    finish_car_track_per_race = per_race(unique_car_and_track, car_and_track, finish_car_track)

    start_finish_data = start_finish(start_car_track_per_race, finish_car_track_per_race)


    print("All")
    print("Races done in given track, car or track & car combo\n")
    print(json.dumps(Sort(Convert(unique_tracks, track_counter)), indent=4))
    print(json.dumps(Sort(Convert(unique_cars, car_counter)), indent=4))
    print(json.dumps(PruneDict(Sort(Convert(unique_car_and_track, car_and_track)), 0), indent=4))
    print("_____________________________________________________________\n")

    print("Elo gain or loss per car & track combo\n")
    print(json.dumps(PruneDict(Sort(Convert(unique_car_and_track, elo_car_track)), 0), indent=4))
    print("_____________________________________________________________\n")

    print("Safety Rating gain or loss per car & track combo\n")
    print(json.dumps(PruneDict(Sort(Convert(unique_car_and_track, sr_car_track)), 0), indent=4))
    print("_____________________________________________________________\n")

    print("Incident Points per car & track combo\n")
    print(json.dumps(PruneDict(Sort(Convert(unique_car_and_track, ip_car_track)), 0), indent=4))
    print("_____________________________________________________________\n")
    
    print("Elo gain/loss per race for car+track with more or equal than 3 races")
    print(json.dumps(PruneDict(Sort(Convert(unique_car_and_track, elo_car_track_per_race)), -10000), indent=4))
    print("_____________________________________________________________\n")
    
    print("Incident Points per race for car+track with more or equal than 3 races")
    print(json.dumps(PruneDict(Sort(Convert(unique_car_and_track, ip_car_track_per_race)), -10000), indent=4))
    print("_____________________________________________________________\n")
    
    print("Safety Rating gain/loss per race for car+track with more or equal than 3 races")
    print(json.dumps(PruneDict(Sort(Convert(unique_car_and_track, sr_car_track_per_race)), -10000), indent=4))
    print("_____________________________________________________________\n")
    
    print("Difference Start -> Finish Position per race for car+track with more or equal than 3 races")
    print(json.dumps(Sort(Convert(unique_car_and_track, start_finish_data)), indent=4))
    print("_____________________________________________________________\n")

    print("Top 5")
    print("Races done in given track, car or track & car combo\n")
    print(json.dumps(PruneNDict(Sort(Convert(unique_tracks, track_counter)),5), indent=4))
    print(json.dumps(PruneNDict(Sort(Convert(unique_cars, car_counter)),5), indent=4))
    print(json.dumps(PruneNDict(Sort(Convert(unique_car_and_track, car_and_track)),5), indent=4))
    print("_____________________________________________________________\n")

    print("Elo gain or loss per car & track combo\n")
    print(json.dumps(PruneNDict(Sort(Convert(unique_car_and_track, elo_car_track)),5), indent=4))
    print(json.dumps(PruneNDict(PruneDict(Sort_inverse(Convert(unique_car_and_track, elo_car_track)), -10000), 5), indent=4))
    print("_____________________________________________________________\n")

    print("Safety Rating gain or loss per car & track combo\n")
    print(json.dumps(PruneNDict(Sort(Convert(unique_car_and_track, sr_car_track)),5), indent=4))
    print(json.dumps(PruneNDict(PruneDict(Sort_inverse(Convert(unique_car_and_track, sr_car_track)), -10000), 5), indent=4))
    print("_____________________________________________________________\n")

    print("Elo gain/loss per race for car+track with more or equal than 3 races")
    print(json.dumps(PruneNDict(Sort(Convert(unique_car_and_track, elo_car_track_per_race)), 5), indent=4))
    print(json.dumps(PruneNDict(PruneDict(Sort_inverse(Convert(unique_car_and_track, elo_car_track_per_race)), -10000), 5), indent=4))
    print("_____________________________________________________________\n")
    
    print("Incident Points per race for car+track with more or equal than 3 races")
    print(json.dumps(PruneNDict(Sort(Convert(unique_car_and_track, ip_car_track_per_race)), 5), indent=4))
    print(json.dumps(PruneNDict(PruneDict(Sort_inverse(Convert(unique_car_and_track, ip_car_track_per_race)), -10000), 5), indent=4))
    print("_____________________________________________________________\n")
    
    print("Safety Rating gain/loss per race for car+track with more or equal than 3 races")
    print(json.dumps(PruneNDict(Sort(Convert(unique_car_and_track, sr_car_track_per_race)), 5), indent=4))
    print(json.dumps(PruneNDict(PruneDict(Sort_inverse(Convert(unique_car_and_track, sr_car_track_per_race)), -10000), 5), indent=4))
    print("_____________________________________________________________\n")
    
    print("Difference Start -> Finish Position per race for car+track with more or equal than 3 races")
    print(json.dumps(PruneNDict(Sort(Convert(unique_car_and_track, start_finish_data)), 5), indent=4))
    print(json.dumps(PruneNDict(Sort_inverse(Convert(unique_car_and_track, start_finish_data)), 5), indent=4))
    print("_____________________________________________________________\n")


#    print(json.dumps(Convert(unique_tracks, track_counter), indent=4))
#    print(json.dumps(Convert(unique_cars, car_counter), indent=4))
#    print(json.dumps(Convert(unique_car_and_track, car_and_track), indent=4))




   # print(Convert(unique_cars, car_counter))

if __name__ == "__main__":
    main()        