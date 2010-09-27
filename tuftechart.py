#Original Author http://www.juiceanalytics.com/writing/real-world-tufte-graphics/ 
#Using the BSD Licence


size(500,700)
font('Palatino'); 
fontsize(12)  
stroke(0.4)  # a medium grey for lines
fill(0.2)    # a slightly darker grey for text  

#<h1>data = (label, first, last, label-fudge-factor)</h1>

data = [ ('Sweden', 46.9, 57.4, 0., 0.),
         ('Netherlands', 44.0, 55.8, .3, 0.),
         ('Norway', 43.5, 52.2, 0., 0.),
         ('Britain', 40.7, 39.0, 0., 0.),
         ('France', 39.0, 43.4, 0., 0.6),
         ('Germany', 37.5, 42.9, 0., -0.4),
         ('Belgium', 35.2, 43.2, 0., 0.),
         ('Canada', 35.2, 35.8, .8, 0.4),
         ('Finland', 34.9, 38.2, -0.5, 0.),
         ('Italy', 30.4, 35.7, 0.3, -0.3),
         ('United States', 30.3, 32.5, -0.3, 0.),
         ('Greece', 26.8, 30.6, 0.4, 0.),
         ('Switzerland', 26.5, 33.2, -0.2, 0.1),
         ('Spain', 22.5, 27.1, 0., 0.3),
         ('Japan', 20.7, 26.6, 0., 0.), ]

text("Current Receipts of Goverment as a Percentage of "
      "Gross Domestic Product, 1970 and 1979", 20, 70, width=215)
text("1970", WIDTH*.28, HEIGHT*0.03)
text("1979", WIDTH*.68, HEIGHT*0.03)

def ypos(val):
    # calculate a vertical position by scaling between 10% and 90% 
    # of the height of the image
    return HEIGHT * (0.9 - 0.8 * (val - minval) / (maxval - minval))

#<h1>find the minimum and maximum values in the range</h1>

alldata = [d[1] for d in data] + [d[2] for d in data]
minval, maxval = min(alldata), max(alldata)

for label, start, end, startfudge, endfudge in data:
    align(RIGHT)
    text(label, 0, ypos(start+startfudge)+4, width=0.25*WIDTH)
    text("%0.1f" % start, 0.25*WIDTH, ypos(start+startfudge)+4, width=0.07*WIDTH)
    align(LEFT)
    text(label, WIDTH*.75, ypos(end+endfudge)+4)
    text("%0.1f" % end, 0.68*WIDTH, ypos(end+endfudge)+4, width=0.07*WIDTH)
    line(WIDTH*.33, ypos(start), WIDTH*.67, ypos(end))
