import drawBot
import json
import subprocess
import random
import datetime
import time
now = datetime.datetime.now()
frames = 1
frames2 = 1
duration =1
flowers_list =["/Users/vasilij/Desktop/Goldman.png",
               "/Users/vasilij/Desktop/flower6.png",
               "/Users/vasilij/Desktop/flower2.png",
               "/Users/vasilij/Desktop/flower3.png",
               "/Users/vasilij/Desktop/flower5.png"]

bigflowers_list =[ "/Users/vasilij/Desktop/bigflower4.png",
                   "/Users/vasilij/Desktop/bigflower.png",
                   "/Users/vasilij/Desktop/bigflower2.png",
                   "/Users/vasilij/Desktop/bigflower3.png"]

flower1 ='%s' % random.choice(tuple(flowers_list))
flowers_list.remove(flower1)
flower2 ='%s' % random.choice(tuple(flowers_list))
flowers_list.remove(flower2)
flower3 ='%s' % random.choice(tuple(flowers_list))
flowers_list.remove(flower3)
bigflower1 ='%s' % random.choice(tuple(bigflowers_list))
bigflowers_list.remove(bigflower1)
bigflower2 ='%s' % random.choice(tuple(bigflowers_list))
bigflowers_list.remove(bigflower2)

im = drawBot.ImageObject(path = flower1)
im2 = drawBot.ImageObject(path = flower2)
im3 = drawBot.ImageObject(path = flower3)
bim = drawBot.ImageObject(path = bigflower1)
bim2 = drawBot.ImageObject(path = bigflower2)

instances = random.randrange(5, 25, 5)
instances2 = random.randrange(5, 25, 5)


               

#for frame in range(frames):
drawBot.newPage(600, 600)
 #   drawBot.frameDuration(duration)
drawBot.fill(0, 0, 0)
if now.hour > 22:
    for instance in range(instances):
 #       drawBot.image(im, (100 * random.choice(tuple([1,2,3,4,5,6])),random.randrange(0, 600, 100) + 100 * random.choice(tuple([1,2,3,4,5,6]))))
        drawBot.image(im2, (100 * random.choice(tuple([1,2,3,4,5,6])),random.randrange(0, 600, 100) + 100 * random.choice(tuple([1,2,3,4,5,6]))))
  #      drawBot.image(im3, (100 * random.choice(tuple([1,2,3,4,5,6])),random.randrange(0, 600, 100) + 100 * random.choice(tuple([1,2,3,4,5,6]))))  
        #drawBot.image(im, (10 * random.choice(tuple([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])),random.randrange(0, 600, 100) + 10 * random.choice(tuple([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]))))
 #       drawBot.image(im, (10 * random.choice(tuple([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])),random.randrange(0, 600, 100) + 10 * random.choice(tuple([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]))))
else:
    for instance in range(instances):
          drawBot.image(bim, (0 + 100 * random.choice(tuple([0,1,2,3,4,5,6])),random.randrange(0, 600, 100)))
          drawBot.image(bim2, (0 + random.randrange(100, 600, 100)-50,random.randrange(100, 600, 100)-50))
    for instance in range(instances2):      
          drawBot.image(im3, (0 + random.randrange(0, 550, 25)+25,(random.randrange(0, 550, 25)+25)))
 #         drawBot.image(im, (100 * random.choice(tuple([1,2,3,4,5,6]))-50,random.randrange(0, 600, 100) + 100 * random.choice(tuple([1,2,3,4,5,6]))-50))
          drawBot.image(im2, (0 + random.randrange(0, 600, 25),random.randrange(0, 600, 25)))
          drawBot.image(im, (0 + random.randrange(100, 600, 25)-15,random.randrange(15, 600, 25)-15))
 #   drawBot.image(bim, (80 * random.choice(tuple([1,2,3,4,5,6])),random.randrange(0, 600, 100) + 20 * random.choice(tuple([1,2,3,4,5,6]))))   
drawBot.endDrawing()
print(now.hour)   
drawBot.saveImage("~/Desktop/textile.png")
#time.sleep(10)
#subprocess.call('python /Users/vasilij/Desktop/pattern.py'.split())
