import image



selectedImage = input("What File Would You Like To Use?\n")
selectedImage = selectedImage + ".jpg"

img = image.Image(selectedImage)
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)  
myImg = img.copy()

def negativeFilter():
    for row in range(myImg.getHeight()):
        for col in range(myImg.getWidth()):
            p = myImg.getPixel(col, row)

            newred = 255 - p.getRed()
            newgreen = 255 - p.getGreen()
            newblue = 255 - p.getBlue()

            newpixel = image.Pixel(newred, newgreen, newblue)

            myImg.setPixel(col, row, newpixel)


def greyScaleFilter():
    for row in range(myImg.getHeight()):
        for col in range(myImg.getWidth()):
            p = myImg.getPixel(col, row)

            greyTone = ((p.getRed()) + (p.getGreen()) + (p.getBlue())) // 3

            newred = 255 - greyTone
            newgreen = 255 - greyTone
            newblue = 255 - greyTone

            newpixel = image.Pixel(newred, newgreen, newblue)

            myImg.setPixel(col, row, newpixel)


def SepiaFilter():
    for row in range(myImg.getHeight()):
        for col in range(myImg.getWidth()):
            p = myImg.getPixel(col, row)

            r = p.getRed()
            g = p.getGreen()
            b = p.getBlue()

            newred = int(r * 0.393 + g * 0.769 + b * 0.189 )
            newgreen = int( r * 0.349 + g * 0.686 + b * 0.168 )
            newblue = int( r * 0.272 + g * 0.534 + b * 0.131 )
            
            if newred > 255:
                newred = 255
            if newgreen> 255:
                newgreen = 255                
            if newblue > 255:
                newblue = 255


            newpixel = image.Pixel(newred, newgreen, newblue)

            myImg.setPixel(col, row, newpixel)


filterfunctions = {}
filterfunctions['negative'] = negativeFilter
filterfunctions['greyscale'] = greyScaleFilter
filterfunctions['sepia'] = SepiaFilter

inFilter = input('Enter the Filters name. Negative, Greyscale, Sepia:\n').lower()
if inFilter in filterfunctions:
    filterfunctions[inFilter]()
else:
    print ('Invalid function name. Use one of the valid filters: ')
    for key in filterfunctions.keys():
        print ('  - ' + key)


myImg.draw(win)
myImg.save("processed_" + selectedImage)
print("Saved!! You can now safely exit by clicking on the window.")
win.exitonclick()