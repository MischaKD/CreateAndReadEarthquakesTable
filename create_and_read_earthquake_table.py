import requests
import sqlite3

def save_eartquakes(place_magnitude_list):
    conn = sqlite3.connect("earthquakes_db.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE earthquakes (place TEXT, magnitude REAL)")
    cursor.executemany("INSERT INTO earthquakes VALUES (?,?)", place_magnitude_list)
    conn.commit()
    conn.close


# def select_all_earthquakes():
#     conn = sqlite3.connect("earthquakes_db.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM earthquakes")
#     data = cursor.fetchall()
#     [print(row) for row in data]
#     conn.commit()
#     conn.close



url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url, headers = {'Accept':'application/json'}, params = {
	'format':'geojson',
	'starttime': input('Enter the start time '),
	'endtime':input('Enter the end time '),
	'latitude':input('Enter the latitude '),
	'longitude':input('Enter the longitude '),
	'maxradiuskm':input('Enter the maxradiuskm '),
	'minmagnitude':input('Enther the minmagnitude ')
	})


data = response.json()

earthquake_list = data['features']
place_magnitude_list = []
count = 0
for earthquake in earthquake_list:
	count += 1
	# print(f"{count}. Place: {earthquake['properties']['place']}. Magnitude: {earthquake['properties']['mag']}.")
place_magnitude_list.append((earthquake['properties']['place'], earthquake['properties']['mag']))


# save_eartquakes(place_magnitude_list)


select_all_earthquakes()


