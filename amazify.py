def getPic():
    """ prompts a user to pick a file to be converted to a jython picture """
    
    return makePicture(pickAFile())
    
    
def amazify():
    pic = getPic()
    
    increaseContrast(pic)
    addBorder(pic)
    droste(pic)
    
    writePictureTo(pic, 'C:\\Users\\J.McGhee\\Documents\\Jake\\CST205\\midterm\\amazify.jpg')


def droste(pic):
    
    copy = shrink(pic)
    xOffset = 0
    yOffset = 0
    levels = 2
    while levels > 0:
        print(xOffset)
        print(yOffset)
        for x in range (0, getWidth(copy)-1):
            for y in range (0, getHeight(copy)-1):
                color = getColor(getPixel(copy, x, y))
                targetX =  getWidth(pic)-int(getWidth(copy)*1.1)-xOffset
                targetY =  getHeight(pic)-int(getHeight(copy)*1.1)-yOffset
                p = getPixel(pic, targetX+x, targetY+y)
                setColor(p, color)
        levels -=1
        xOffset += int(getWidth(copy)*1.1)-getWidth(copy)
        yOffset += int(getHeight(copy)*1.1)-getHeight(copy)
        copy = shrink(copy)
    repaint(pic)
    
    
def shrink(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  canvas = makeEmptyPicture(width/3, height/3)
  for x in range (0, width-2, 3):
    for y in range (0, height-2, 3):
      color = getColor(getPixel(pic, x, y))
      setColor(getPixel(canvas, x/3, y/3), color)
  return canvas   
  
def addBorder(pic):


    margin = 10
    
    # top border
    for x in range(0, getWidth(pic)):
        for y in range(0, margin):
            setColor(getPixel(pic, x, y), black) 
            
    # bottom border
    for x in range(0, getWidth(pic)):
        for y in range(getHeight(pic)-margin, getHeight(pic)):
            setColor(getPixel(pic, x, y), black)
            
    # left border
    for x in range(0, margin):
        for y in range(0, getHeight(pic)):
            setColor(getPixel(pic, x, y), black)
            
    # right border
    for x in range(getWidth(pic)-margin, getWidth(pic)):
        for y in range(0, getHeight(pic)):
            setColor(getPixel(pic, x, y), black)
    
    return pic

def increaseContrast(pic):

    pixels = getPixels(pic)
    for p in pixels:
        color = getColor(p)
        if distance(color, black) <= distance(color, white):
            color = makeDarker(color)
        else:
            color = makeLighter(color)
        setColor(p, color)
    repaint(pic)