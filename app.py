from concurrent.futures import process
from flask import Flask, request
from google.transit import gtfs_realtime_pb2
import requests as r 
import mta_plugins as mta
import psutil
import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

application = Flask(__name__)

@application.route('/stats')
def stat():
    cpu = str(psutil.cpu_percent()) + '%'
    memory = psutil.virtual_memory()
    # Divide from Bytes -> KB -> MB
    available = round(memory.available/1024.0/1024.0,1)
    total = round(memory.total/1024.0/1024.0,1)
    mem_stat = str(available) + 'MB free / ' + str(total) + 'MB total ( ' + str(memory.percent) + '% )'
    disk = psutil.disk_usage('/')
    free = round(disk.free/1024.0/1024.0/1024.0,1)
    total = round(disk.total/1024.0/1024.0/1024.0,1)
    disk_stat = str(free) + 'GB free / ' + str(total) + 'GB total ( ' + str(disk.percent) + '% )'
    return f"CPU usage:{cpu} | Memory usage:{mem_stat} | Disk usage: {disk_stat}"

@application.route('/JZ')
def jz():
    args = request.args
    lat = float(args.get('Latitude'))
    long = float(args.get('Longitude'))
    feed = gtfs_realtime_pb2.FeedMessage()
    resp = r.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz', verify=False)
    try:
        feed.ParseFromString(resp.content)
        station = mta.find_closest_station(long,lat,"J Z")
        trains = mta.filter_results(feed,station)
        print(trains)
        return {"trains":trains}
        # return station
    except :
        return "Oops!  That was no valid data. Try again.."

@application.route('/ACE')
def ace():
    args = request.args
    lat = float(args.get('Latitude'))
    long = float(args.get('Longitude'))
    feed = gtfs_realtime_pb2.FeedMessage()
    resp = r.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace', verify=False)
    try:
        feed.ParseFromString(resp.content)
        station = mta.find_closest_station(long,lat,"A C E")
        trains = mta.filter_results(feed,station)
        print(trains)
        return {"trains":trains}
        # return station
    except :
        return "Oops!  That was no valid data. Try again.."

@application.route('/BDFM')
def bdfm():
    args = request.args
    lat = float(args.get('Latitude'))
    long = float(args.get('Longitude'))
    feed = gtfs_realtime_pb2.FeedMessage()
    resp = r.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm', verify=False)
    try:
        feed.ParseFromString(resp.content)
        station = mta.find_closest_station(long,lat,"B D F M")
        trains = mta.filter_results(feed,station)
        print(trains)
        return {"trains":trains}
        # return station
    except :
        return "Oops!  That was no valid data. Try again.."

@application.route('/L')
def l():
    args = request.args
    lat = float(args.get('Latitude'))
    long = float(args.get('Longitude'))
    feed = gtfs_realtime_pb2.FeedMessage()
    resp = r.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l', verify=False)
    try:
        feed.ParseFromString(resp.content)
        station = mta.find_closest_station(long,lat,"L")
        trains = mta.filter_results(feed,station)
        print(trains)
        return {"trains":trains}
        # return station
    except :
        return "Oops!  That was no valid data. Try again.."

@application.route('/NQRW')
def nqrw():
    args = request.args
    lat = float(args.get('Latitude'))
    long = float(args.get('Longitude'))
    feed = gtfs_realtime_pb2.FeedMessage()
    resp = r.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw', verify=False)
    try:
        feed.ParseFromString(resp.content)
        station = mta.find_closest_station(long,lat,"N Q R W")
        trains = mta.filter_results(feed,station)
        print(trains)
        return {"trains":trains}
        # return station
    except :
        return "Oops!  That was no valid data. Try again.."

@application.route('/1234567')
def _1234567():
    args = request.args
    lat = float(args.get('Latitude'))
    long = float(args.get('Longitude'))
    feed = gtfs_realtime_pb2.FeedMessage()
    resp = r.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs', verify=False)
    try:
        feed.ParseFromString(resp.content)
        station = mta.find_closest_station(long,lat,"1 2 3 4 5 6 7")
        trains = mta.filter_results(feed,station)
        print(trains)
        return {"trains":trains}
        # return station
    except :
        return "Oops!  That was no valid data. Try again.."

@application.route('/g')
def g():
    args = request.args
    lat = float(args.get('Latitude'))
    long = float(args.get('Longitude'))
    feed = gtfs_realtime_pb2.FeedMessage()
    resp = r.get('https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g', verify=False)
    try:
        feed.ParseFromString(resp.content)
        station = mta.find_closest_station(long,lat,"G")
        trains = mta.filter_results(feed,station)
        print(trains)
        return {"trains":trains}
        # return station
    except :
        return "Oops!  That was no valid data. Try again.."


@application.route('/')
def index():
    return "Oops!  That was not valid data.\n " \
    "Use a valid train line as your path.\n" \
    "ACE\n" \
    "BDFM\n " \
    "L\n" \
    "NQRW\n" \
    "1234567\n" \
    "G\n" \
    "Try again.."

if __name__ == '__main__':
    application.run()