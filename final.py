import pandas as pd
import csv
rows=[]
with open('final.csv','r') as f:
  df=csv.reader(f)
  for row in df:
    rows.append(row)
headers=rows[0]
planet_data_rows=rows[1:]
print(planet_data_rows[0])
headers[0]='row_num'
print(headers)

temp_planet_data_rows=list(planet_data_rows)
for planet_data in temp_planet_data_rows:
  planet_mass=planet_data[3]
  if planet_mass.lower()=='unknown':
    planet_data_rows.remove(planet_data)
    continue
  else:
    # planet_mass_value=planet_mass.split(' ')[0]
    # planet_mass_ref=planet_mass.split(' ')[1]
    planet_mass_value=float(planet_mass)*1.989e+30
    planet_data[3]=planet_mass_value
  planet_radius=planet_data[4]
  if planet_radius.lower()=='unknown':
    planet_data_rows.remove(planet_data)
    continue
  else:
    planet_radius_value=planet_radius.split(' ')[0]
    # planet_radius_ref=planet_radius.split(' ')[2]
    planet_data[4]=planet_radius_value
print(len(planet_data_rows))

temp_planet_data_rows=list(planet_data_rows)
for plant_data in temp_planet_data_rows:
  if planet_data[1].lower()=='hd 100546 b':
    planet_data_rows.remove(planet_data)
planet_masses=[]
planet_names=[]
planet_radiuses=[]
for planet_data in planet_data_rows:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_names.append(planet_data[1])
planet_gravity=[]
for index,name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)
df.to_csv('main.csv')