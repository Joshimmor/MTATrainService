
import pandas as pd
from google.transit import gtfs_realtime_pb2

def find_closest_station(Long:float,Lat:float,Line:str)-> str:
    """
    returns (string type)  ID of  the Subway station closest to the Longitude and Latitude that are passed as arguments. An pandas dataframe
    is iterated through, evaluating the absolute distance from the given point. 
    """
    df = pd.read_csv("./Stations.csv")
    # print(df.head())
    distance = 30
    stop_id = ''
    for index, row in df.iterrows():
        if(any(train_line in row['Daytime Routes'].split(' ') for train_line in Line.split(" "))):
            if(abs(float(row['GTFS Longitude'])-Long)+abs(float(row['GTFS Latitude'])-Lat) < distance):
                distance = abs(float(row['GTFS Longitude'])-Long)+abs(float(row['GTFS Latitude'])-Lat)
                stop_id = row['GTFS Stop ID']
    return stop_id

#Filter GTFS Results
def filter_results(feed,stop_id:str):
    from datetime import datetime
    ts = int(str(feed.header.timestamp))
    print("Last update: " + datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S'))
    for entity in feed.entity:
        stops = []
        trains=[]
        for entity in feed.entity:
            if entity.HasField('trip_update') :
                stop = list(filter(lambda x:stop_id in x.stop_id,entity.trip_update.stop_time_update))
                if len(stop)>0:
                    stops.append(stop[0])
        for stop in stops:   
            time_til = datetime.fromtimestamp(stop.arrival.time)
            direction = "Manhattan" if 'N' in stop.stop_id else "Jamaica"
            trains.append({'direction':direction,'time':time_til})
        results = []
        for train in trains:
            if train not in results:
                results.append(train)
        return results