import googlemaps
import urllib
import json
import csv
import os

if os.path.exists(CredentialsGoogle) is True:
    b = input("Dein Key ist immernoch der Gleiche, möchtest du ihn ändern? J/N: ")
        if b = "J"
            New_API = input("Bitte gib neuen API_Key ein: ")
            with open(CredentialsGoogle, 'w') as f:
            f.write("API_Key =" New_API)
            f.close()
            print("Der Key wurde geändert")
        else:
            print("Ok")  
else:
    b = input("Bitte gib einen gültigen API_Key ein: ")
    with open(CredentialsGoogle, 'w') as f:
        f.write("API_Key =" New_API)
        f.close()
        print("Ein Key wurde erstellt")
    
from CredentialsGoogle import API_Key
        
table = [["Name","Adresse","Telefon","Bewertung"]]

search = input("Bitte Stichwort für Ortssuche eingeben: ")
digit = search.replace(' ', '%20') 
n = input("Bitte Anzahl der Seiten angeben, die geladen werden sollen(20 Ergebnisse/Seite): ")
n = (n-1)
find_places = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+digit+"&key="+APIKey
url_json = urllib.request.urlopen(find_places)
jsonf = json.load(url_json)
for place in jsonf['results']: 
    place_id = place['place_id']
    details = "https://maps.googleapis.com/maps/api/place/details/json?place_id="+place_id+\
    "&fields=formatted_phone_number,website,opening_hours&key="+APIKey
    url_json2 = urllib.request.urlopen(details)
    jsondetails = json.load(url_json2)
    dir_details = jsondetails['result']
    table.append([place['name'], place['formatted_address'], dir_details['formatted_phone_number'], str(place['rating'])])
         #dir_details['website'], dir_details['opening_hours']['weekday_text'][0]])
if (n>0):
    for x in range(n):
        find_more_places = "https://maps.googleapis.com/maps/api/place/textsearch/json?query="+digit+"&key="+APIKey+\
           "&next_page_token="jsonf['next_page_token']
        url_json = urllib.request.urlopen(find_more_places)
        jsonf = json.load(url_json)
        for place in jsonf['results']: 
        place_id = place['place_id']
        details = "https://maps.googleapis.com/maps/api/place/details/json?place_id="+place_id+\
        "&fields=formatted_phone_number,website,opening_hours&key="+APIKey
        url_json2 = urllib.request.urlopen(details)
        jsondetails = json.load(url_json2)
        dir_details = jsondetails['result']
        table.append([place['name'], place['formatted_address'], dir_details['formatted_phone_number'], str(place['rating'])])
         #dir_details['website'], dir_details['opening_hours']['weekday_text'][0]])


file_name = "Test.csv"

if os.path.exists(file_name) is True:
    with open(file_name, 'r') as file:
        csv_writer = csv.writer(file, delimiter=',', quoting= csv.QUOTE_ALL)
        csv_writer.writerows(table) #soll Inhalt der csv Datei lesen und mit neue Liste vergleichen.
else
    with open(file_name, 'w') as file:
        csv_writer = csv.writer(file, delimiter=',', quoting= csv.QUOTE_ALL)
        csv_writer.writerows(table)

  
# Define Search
#urllib2.urlopen("https://maps.googleapis.com/maps/api/place/findplacefromtext/json&"APIKey)
#place_result = gmaps.places_result  #places storage, parameters have to be separated with a ";"
#place_detail = gmaps.place_detail()
#pause the script for "()"seconds

# time.sleep(sleep)
#pprint(place_result)

#Get the next 20 Results
#places_result = gmaps.places_nearby(page_token = places_result['next_page_token'])

#for place in place_result["results"]:

    # festlegen der place id
    #my_place_id = place["result"]

    #Welche Attribute willst du rausholen?:
   # my_fields = ["name", "adress"]
    #place_details = gmaps.place(place_id = my_place_id, fields = my_fields) #frag die Api nach den Daten'
