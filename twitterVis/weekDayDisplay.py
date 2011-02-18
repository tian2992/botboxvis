size(640,395)
background(255)

bar_width = 90
day_values = [30,40,60,55,90,20,60]
margins = 20

for (day, value) in enumerate(day_values):
  rect((day*bar_width)+margins,HEIGHT-margins,bar_width-margins,-value*3)
