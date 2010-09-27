size(600, 600)

#TODO: add auto-centering

lightGrey = color("#F5F4E1")
darkGrey = color("#82877A")
accentColour = color("#D44917")

background(lightGrey)
fill(darkGrey)

font("Garamond Premier Pro",360)
font("Adobe Song Std",200)
fill(accentColour)


def english():
  centerX = 140
  centerY = 360

  push()
  for i in range(10):
    text("hello",centerX,centerY)
    rotate(i*2)
  pop()
    
  fill(darkGrey)
  for i in range(10):
    text("bye",centerX,centerY)
    rotate(-i*2)
    
def jap():
  centerX = 5
  centerY = 360

  push()
  for i in range(10):
    text("おはよ",centerX,centerY)
    rotate(i*2)
  pop()
    
  fill(darkGrey)
  for i in range(10):
    text("やまた",centerX,centerY)
    rotate(-i*2)
    
    
english()
