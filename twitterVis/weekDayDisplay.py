size(640,395)
background(255)

bar_width = 90
margins = 20

day_values = [30,40,60,55,90,20,60]
max_value = max(day_values)

colormode(HSB)

for (day, value) in enumerate(day_values):
  fill(day/7.0,max_value/value,0.8)
  rect((day*bar_width)+margins,HEIGHT-margins,bar_width-margins,-value*3)
