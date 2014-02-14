# -*- coding: utf-8 -*-
import requests
import json
import jinja2
from jinja2 import Template

def direcviento(direccion):
#Ahora calcularemos la direccion del viento por grado
         for grado in str(direccion):
                  if direccion >= 337.5 and direccion < 22.5:
                           return "N"
                  elif direccion >= 22.5 and direccion < 67.5:
                           return "NE"
                  elif direccion >= 67.5 and direccion < 112.5:
                           return "E"
                  elif direccion >= 112.5 and direccion < 157.5:
                           return "SE"
                  elif direccion >= 157.5 and direccion < 202.5:
                           return "S"
                  elif direccion >= 202.5 and direccion < 247.5:
                           return "SO"
                  elif direccion >= 247.5 and direccion < 292.5:
                           return "O"
                  elif direccion >= 292.5 and direccion < 337.5:
                           return "NO"
          
ciudades = """
  "Almeria",
  "Cadiz",
  "Cordoba",
  "Granada",
  "Huelva",
  "Jaen",
  "Malaga",
  "Sevilla" """
  
  
respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params={'q':'%s,spain' % ciudades[1]})

dicci = json.loads(respuesta.text)

tempemin = dicci["main"]["tem_min"] 
tempemax = dicci["main"]["tem_max"]
viento = dicci["wind"]["speed"]
direccionviento = dicci["wind"]["deg"]
#añadimos la peticion de grados reales
tempreminreal = round(tempemin - 273)
tempremaxreal = round(tempemax - 273)
vientoreal = round(viento * 1.61)

print "la temperatura actual de %s es de %s grados centigrados, la maxima es de %s, y la velocidad del viento es de %s km/h direccion %s" % (ciudades(1),tempreminreal,tempremaxreal, vientoreal, direccionviento) 

