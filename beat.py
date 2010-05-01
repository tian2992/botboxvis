# -*- coding: utf-8 -*-
import pylast, random

def coordinateX(x0, y0, distance, angle):
  from math import radians, sin, cos
  x1 = x0 + cos(radians(angle)) * distance
  return x1
def coordinateY(x0, y0, distance, angle):
  from math import radians, sin, cos
  y1 = y0 + sin(radians(angle)) * distance
  return y1

def plot(artistName, numArtists, API_KEY, sizeX, sizeY):
  size(sizeX,sizeY)

  network = pylast.get_lastfm_network(api_key = API_KEY)
  network.enable_caching()

  font("Gill Sans MT Pro Medium", 24)
  text(artistName, WIDTH/10, HEIGHT/10)
  font("Gill Sans MT Pro Light", 12)

  artist = network.get_artist(artistName)

  similares = artist.get_similar(numArtists)

  posiciones = []
  
  colormode(HSB)

  for sim in similares:
      artSimil = sim[0].name
      angle = 0
      noFound = True
      while noFound: #Brutish collision management
        angle = random.randint(0,360/numArtists+1)
        if (angle in posiciones):
          noFound = True
        else:
          posiciones.append(angle)
          noFound = False
          
      angle = angle * (numArtists+1)
      
      dist = WIDTH/2 - (sim[1]*WIDTH/2)
      if (dist < WIDTH/10):
        dist = dist+WIDTH/10
      
      X = coordinateX(WIDTH/2,HEIGHT/2, dist, angle)
      Y = coordinateY(WIDTH/2,HEIGHT/2, dist, angle)
      
      fill(angle/360.0, 0.8*360, 0.5)
      
      if (angle > 90 and angle < 270):
        angle = angle + 180
        align(RIGHT)
      else:
        align(LEFT)
      
      push()
      rotate(angle)
      
      text(artSimil, X, Y, width=50)
      pop()
      
#artist name, number of artists, API key, sizeX, sizeY
plot("The Beatles", 19, APIKEY , 600, 600)

