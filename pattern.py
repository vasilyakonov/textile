import drawBot
import json
import os
import random
import datetime
import dropbox
import cloudinary
import cloudinary.uploader
import cloudinary.api
import django
frames = 1
frames2 = 1
duration =1
duration2 =3
instances = 20
instances2=1

pattern= drawBot.ImageObject(path = "/Users/vasilij/Desktop/textile.png")
pattern1= drawBot.ImageObject(path = "/Users/vasilij/Desktop/textile1.png")
pattern2= drawBot.ImageObject(path = "/Users/vasilij/Desktop/textile2.png")
pattern3= drawBot.ImageObject(path = "/Users/vasilij/Desktop/textile3.png")
pattern4= drawBot.ImageObject(path = "/Users/vasilij/Desktop/textile4.png")
pattern5= drawBot.ImageObject(path = "/Users/vasilij/Desktop/textile5.png")
pattern6= drawBot.ImageObject(path = "/Users/vasilij/Desktop/textile6.png")
pattern7= drawBot.ImageObject(path = "/Users/vasilij/Desktop/textile7.png")
pattern8= drawBot.ImageObject(path = "/Users/vasilij/Desktop/textile8.png")

     
    
patterngif= drawBot.ImageObject(path = "/Users/vasilij/Desktop/original_40fd199cf8b61ce1e431cdb5098d0025.gif")
for frame in range(frames2):
    drawBot.newPage(8400, 4200)
    drawBot.frameDuration(duration)

    drawBot.image(pattern, (0,0))
    
 #   drawBot.image(pattern1, (1800,1800+600))
 #   drawBot.image(pattern1, (2400,2400+600))
 #   drawBot.image(pattern1, (3000,3000+600))
 #   drawBot.image(pattern1, (2400,1800+600))
 #   drawBot.image(pattern1, (3000,1800+600))
    #drawBot.image(pattern1, (1800,2400+600))
    #first
    drawBot.image(pattern1, (1800,3000+600))
    #drawBot.image(pattern1, (3000,2400+600))
   # drawBot.image(pattern1, (2400,3000+600))
                  
    
    
    
    
   #drawBot.image(pattern2, (1800,0))
   #first
    drawBot.image(pattern2, (1800,600))
    
 #   drawBot.image(pattern2, (1800,1200))
 #   drawBot.image(pattern2, (2400,0))
    #drawBot.image(pattern2, (2400,600))
 #   drawBot.image(pattern2, (2400,1200))
   # drawBot.image(pattern2, (3000,0))
 #   drawBot.image(pattern2, (3000,600))
   # drawBot.image(pattern2, (3000,1200))
    
    
    
    #drawBot.image(pattern3, (0,1800+600))
 #   drawBot.image(pattern3, (0,2400+600))
 #   drawBot.image(pattern3, (0,3000+600))
                            #first
    drawBot.image(pattern3, (600,1800+600))
    #drawBot.image(pattern3, (600,2400+600))
    #drawBot.image(pattern3, (600,3000+600))
 #   drawBot.image(pattern3, (1200,1800+600))
 #   drawBot.image(pattern3, (1200,2400+600))
  #  drawBot.image(pattern3, (1200,3000+600))
    

    
 #   drawBot.image(pattern4, (3600,1800+600))
 #   drawBot.image(pattern4, (3600,2400+600))
    #drawBot.image(pattern4, (3600,3000+600))
   # drawBot.image(pattern4, (4200,1800+600))
    #drawBot.image(pattern4, (4200,2400+600))
 #   drawBot.image(pattern4, (4200,3000+600))
    #first
    drawBot.image(pattern4, (4800,1800+600))
 #   drawBot.image(pattern4, (4800,2400+600))
 #   drawBot.image(pattern4, (4800,3000+600))


    
 #   drawBot.image(pattern6, (3600,0))
   # drawBot.image(pattern6, (3600,600))
 #   drawBot.image(pattern6, (3600,1200))
 #   drawBot.image(pattern6, (4200,0))
 #   drawBot.image(pattern6, (4200,600))
 #   drawBot.image(pattern6, (4200,1200))
 #   drawBot.image(pattern6, (4800,0))
 #   drawBot.image(pattern6, (4800,600))
    #first
    drawBot.image(pattern6, (4800,1200))




    
 #   drawBot.image(pattern7, (5400,1800+600))
 #   drawBot.image(pattern7, (5400,2400+600))
    #first
    drawBot.image(pattern7, (5400,3000+600))
 #   drawBot.image(pattern7, (6000,1800+600))
 #   drawBot.image(pattern7, (6000,2400+600))
 #   drawBot.image(pattern7, (6000,3000+600))
 #   drawBot.image(pattern7, (6600,1800+600))
 #   drawBot.image(pattern7, (6600,2400+600))
 #   drawBot.image(pattern7, (6600,3000+600))



 #   drawBot.image(pattern8, (5400,0))
 #   drawBot.image(pattern8, (5400,600))
 #   drawBot.image(pattern8, (5400,1200))
 #   drawBot.image(pattern8, (6000,0))
 #   drawBot.image(pattern8, (6000,600))
 #   drawBot.image(pattern8, (6000,1200))
    #first
    drawBot.image(pattern8, (6600,0))
 #   drawBot.image(pattern8, (6600,600))
 #   drawBot.image(pattern8, (6600,1200))


    

    drawBot.image(pattern, (0,1800))
    drawBot.image(pattern3, (600,1800))
    drawBot.image(pattern3, (1200,1800))
    drawBot.image(pattern1, (1800,1800))
    drawBot.image(pattern4, (2400,1800))
    drawBot.image(pattern5, (3000,1800))
    drawBot.image(pattern5, (3600,1800))
    drawBot.image(pattern6, (4200,1800))
    drawBot.image(pattern7, (4800,1800))
    drawBot.image(pattern7, (5400,1800))
    drawBot.image(pattern8, (6000,1800))
    drawBot.image(pattern8, (6600,1800))




    drawBot.image(pattern4, (7200,0))
    drawBot.image(pattern6, (7200,600))
    drawBot.image(pattern7, (7200,1200))
    drawBot.image(pattern8, (7200,1800))
    drawBot.image(pattern2, (7200,2400))
    drawBot.image(pattern, (7200,3000))
    drawBot.image(pattern5, (7200,3600))


    

    drawBot.image(pattern3, (7800,0))
    drawBot.image(pattern6, (7800,600))
    drawBot.image(pattern8, (7800,1200))
    drawBot.image(pattern5, (7800,1800))
    drawBot.image(pattern1, (7800,2400))
    drawBot.image(pattern3, (7800,3000))
    drawBot.image(pattern7, (7800,3600))
    
    
    
for frame in range(frames2):
    drawBot.newPage(8400, 4200)
    drawBot.frameDuration(duration)


    drawBot.image(pattern1, (1800,3000+600))
    drawBot.image(pattern1, (3000,2400+600))
    
    
    drawBot.image(pattern, (0,0))
    drawBot.image(pattern, (1200,1200))


    drawBot.image(pattern2, (1800,0))
    drawBot.image(pattern2, (1800,600))


    drawBot.image(pattern3, (600,1800+600))
    drawBot.image(pattern3, (600,2400+600))



    drawBot.image(pattern4, (4200,3000+600))
    drawBot.image(pattern4, (4800,1800+600))

    drawBot.image(pattern6, (4800,600))
    drawBot.image(pattern6, (4800,1200))



    drawBot.image(pattern7, (5400,3000+600))
    drawBot.image(pattern7, (6000,1800+600))


    drawBot.image(pattern8, (6600,0))
    drawBot.image(pattern8, (6600,600))

    
    
for frame in range(frames2):
    drawBot.newPage(8400, 4200)
    drawBot.frameDuration(duration)
    drawBot.image(pattern, (0,0))
    drawBot.image(pattern, (1200,1200))
    drawBot.image(pattern, (600,600))


    drawBot.image(pattern1, (1800,2400+600))
    drawBot.image(pattern1, (1800,3000+600))
    drawBot.image(pattern1, (3000,2400+600))


    drawBot.image(pattern2, (2400,1200))
    drawBot.image(pattern2, (1800,0))
    drawBot.image(pattern2, (1800,600))


    drawBot.image(pattern3, (1200,3000+600))
    drawBot.image(pattern3, (600,1800+600))
    drawBot.image(pattern3, (600,2400+600))


    drawBot.image(pattern4, (4200,2400+600))
    drawBot.image(pattern4, (4200,3000+600))
    drawBot.image(pattern4, (4800,1800+600))



    drawBot.image(pattern6, (4800,0))
    drawBot.image(pattern6, (4800,600))
    drawBot.image(pattern6, (4800,1200))



    drawBot.image(pattern7, (5400,3000+600))
    drawBot.image(pattern7, (6000,1800+600))
    drawBot.image(pattern7, (5400,2400+600))


    drawBot.image(pattern8, (6600,1200))
    drawBot.image(pattern8, (6600,0))
    drawBot.image(pattern8, (6600,600))



    
for frame in range(frames2):
    drawBot.newPage(8400, 4200)
    drawBot.frameDuration(duration)
    drawBot.image(pattern, (0,0))
    drawBot.image(pattern, (1200,1200))
    drawBot.image(pattern, (600,600))
    drawBot.image(pattern, (600,0))


    drawBot.image(pattern1, (3000,1800+600))
    drawBot.image(pattern1, (1800,2400+600))
    drawBot.image(pattern1, (1800,3000+600))
    drawBot.image(pattern1, (3000,2400+600))



    drawBot.image(pattern2, (2400,1200))
    drawBot.image(pattern2, (1800,0))
    drawBot.image(pattern2, (1800,600))
    drawBot.image(pattern2, (3000,0))


    drawBot.image(pattern3, (1200,3000+600))
    drawBot.image(pattern3, (600,1800+600))
    drawBot.image(pattern3, (600,2400+600))
    drawBot.image(pattern3, (600,3000+600))



    drawBot.image(pattern4, (4200,2400+600))
    drawBot.image(pattern4, (4200,3000+600))
    drawBot.image(pattern4, (4800,1800+600))
    drawBot.image(pattern4, (4800,2400+600))



    drawBot.image(pattern6, (4800,0))
    drawBot.image(pattern6, (4800,600))
    drawBot.image(pattern6, (4800,1200))
    drawBot.image(pattern6, (3600,0))



    drawBot.image(pattern7, (5400,3000+600))
    drawBot.image(pattern7, (6000,1800+600))
    drawBot.image(pattern7, (5400,2400+600))
    drawBot.image(pattern7, (5400,1800+600))



    drawBot.image(pattern8, (6600,1200))
    drawBot.image(pattern8, (6600,0))
    drawBot.image(pattern8, (6600,600))
    drawBot.image(pattern8, (6000,1200))



    
for frame in range(frames2):
    drawBot.newPage(8400, 4200)
    drawBot.frameDuration(duration)
    drawBot.image(pattern, (0,0))
    drawBot.image(pattern, (1200,1200))
    
    drawBot.image(pattern, (600,600))
    drawBot.image(pattern, (600,0))
    drawBot.image(pattern, (600,1200))


    drawBot.image(pattern1, (2400,3000+600))
    drawBot.image(pattern1, (3000,1800+600))
    drawBot.image(pattern1, (1800,2400+600))
    drawBot.image(pattern1, (1800,3000+600))
    drawBot.image(pattern1, (3000,2400+600))



    drawBot.image(pattern2, (3000,600))
    drawBot.image(pattern2, (2400,1200))
    drawBot.image(pattern2, (1800,0))
    drawBot.image(pattern2, (1800,600))
    drawBot.image(pattern2, (3000,0))


    drawBot.image(pattern3, (1200,3000+600))
    drawBot.image(pattern3, (600,1800+600))
    drawBot.image(pattern3, (600,2400+600))
    drawBot.image(pattern3, (600,3000+600))
    drawBot.image(pattern3, (0,2400+600))



    drawBot.image(pattern4, (4200,2400+600))
    drawBot.image(pattern4, (4200,3000+600))
    drawBot.image(pattern4, (4800,1800+600))
    drawBot.image(pattern4, (4800,2400+600))
    drawBot.image(pattern4, (3600,1800+600))



    drawBot.image(pattern6, (4800,0))
    drawBot.image(pattern6, (4800,600))
    drawBot.image(pattern6, (4800,1200))
    drawBot.image(pattern6, (3600,0))
    drawBot.image(pattern6, (3600,600))



    drawBot.image(pattern7, (5400,3000+600))
    drawBot.image(pattern7, (6000,1800+600))
    drawBot.image(pattern7, (5400,2400+600))
    drawBot.image(pattern7, (5400,1800+600))
    drawBot.image(pattern7, (6000,2400+600))


    drawBot.image(pattern8, (6600,1200))
    drawBot.image(pattern8, (6600,0))
    drawBot.image(pattern8, (6600,600))
    drawBot.image(pattern8, (6000,1200))
    drawBot.image(pattern8, (5400,1200))

    
for frame in range(frames2):
    drawBot.newPage(8400, 4200)
    drawBot.frameDuration(duration)
    drawBot.image(pattern, (0,0))
    
    drawBot.image(pattern, (600,600))
    drawBot.image(pattern, (600,0))
    drawBot.image(pattern, (600,1200))
    drawBot.image(pattern, (0,1200))
    drawBot.image(pattern, (1200,1200))




    drawBot.image(pattern1, (2400,3000+600))
    drawBot.image(pattern1, (3000,1800+600))
    drawBot.image(pattern1, (1800,2400+600))
    drawBot.image(pattern1, (1800,3000+600))
    drawBot.image(pattern1, (3000,2400+600))
    drawBot.image(pattern1, (2400,1800+600))



    drawBot.image(pattern2, (3000,600))
    drawBot.image(pattern2, (2400,1200))
    drawBot.image(pattern2, (1800,0))
    drawBot.image(pattern2, (1800,600))
    drawBot.image(pattern2, (3000,0))
    drawBot.image(pattern2, (2400,0))



    drawBot.image(pattern3, (1200,3000+600))
    drawBot.image(pattern3, (600,1800+600))
    drawBot.image(pattern3, (600,2400+600))
    drawBot.image(pattern3, (600,3000+600))
    drawBot.image(pattern3, (0,2400+600))
    drawBot.image(pattern3, (1200,1800+600))



    drawBot.image(pattern4, (4200,2400+600))
    drawBot.image(pattern4, (4200,3000+600))
    drawBot.image(pattern4, (4800,1800+600))
    drawBot.image(pattern4, (4800,2400+600))
    drawBot.image(pattern4, (3600,1800+600))
    drawBot.image(pattern4, (3600,3000+600))

    drawBot.image(pattern6, (4800,0))
    drawBot.image(pattern6, (4800,600))
    drawBot.image(pattern6, (4800,1200))
    drawBot.image(pattern6, (3600,0))
    drawBot.image(pattern6, (3600,600))
    drawBot.image(pattern6, (3600,1200))



    drawBot.image(pattern7, (5400,3000+600))
    drawBot.image(pattern7, (6000,1800+600))
    drawBot.image(pattern7, (5400,2400+600))
    drawBot.image(pattern7, (5400,1800+600))
    drawBot.image(pattern7, (6000,2400+600))
    drawBot.image(pattern7, (6600,3000+600))



    drawBot.image(pattern8, (6600,1200))
    drawBot.image(pattern8, (6600,0))
    drawBot.image(pattern8, (6600,600))
    drawBot.image(pattern8, (6000,1200))
    drawBot.image(pattern8, (5400,1200))
    drawBot.image(pattern8, (6000,600))


    
for frame in range(frames2):
    drawBot.newPage(8400, 4200)
    drawBot.frameDuration(duration)
    drawBot.image(pattern, (0,0))
    drawBot.image(pattern, (1200,1200))
    drawBot.image(pattern, (600,600))
    drawBot.image(pattern, (600,0))
    drawBot.image(pattern, (600,1200))
    drawBot.image(pattern, (0,1200))
    drawBot.image(pattern, (0,600))



    drawBot.image(pattern1, (2400,3000+600))
    drawBot.image(pattern1, (3000,1800+600))
    drawBot.image(pattern1, (1800,2400+600))
    drawBot.image(pattern1, (1800,3000+600))
    drawBot.image(pattern1, (3000,2400+600))
    drawBot.image(pattern1, (2400,1800+600))
    drawBot.image(pattern1, (3000,3000+600))



    drawBot.image(pattern2, (3000,600))
    drawBot.image(pattern2, (2400,1200))
    drawBot.image(pattern2, (1800,0))
    drawBot.image(pattern2, (1800,600))
    drawBot.image(pattern2, (3000,0))
    drawBot.image(pattern2, (2400,0))
    drawBot.image(pattern2, (1800,1200))



    drawBot.image(pattern3, (1200,3000+600))
    drawBot.image(pattern3, (600,1800+600))
    drawBot.image(pattern3, (600,2400+600))
    drawBot.image(pattern3, (600,3000+600))
    drawBot.image(pattern3, (0,2400+600))
    drawBot.image(pattern3, (1200,1800+600))
    drawBot.image(pattern3, (1200,2400+600))



    drawBot.image(pattern4, (4200,2400+600))
    drawBot.image(pattern4, (4200,3000+600))
    drawBot.image(pattern4, (4800,1800+600))
    drawBot.image(pattern4, (4800,2400+600))
    drawBot.image(pattern4, (3600,1800+600))
    drawBot.image(pattern4, (3600,3000+600))
    drawBot.image(pattern4, (4200,1800+600))



    drawBot.image(pattern6, (4200,1200))
    drawBot.image(pattern6, (4800,0))
    drawBot.image(pattern6, (4800,600))
    drawBot.image(pattern6, (4800,1200))
    drawBot.image(pattern6, (3600,0))
    drawBot.image(pattern6, (3600,600))
    drawBot.image(pattern6, (3600,1200))



    drawBot.image(pattern7, (5400,3000+600))
    drawBot.image(pattern7, (6000,1800+600))
    drawBot.image(pattern7, (5400,2400+600))
    drawBot.image(pattern7, (5400,1800+600))
    drawBot.image(pattern7, (6000,2400+600))
    drawBot.image(pattern7, (6600,3000+600))
    drawBot.image(pattern7, (6600,1800+600))



    drawBot.image(pattern8, (6600,1200))
    drawBot.image(pattern8, (6600,0))
    drawBot.image(pattern8, (6600,600))
    drawBot.image(pattern8, (6000,1200))
    drawBot.image(pattern8, (5400,1200))
    drawBot.image(pattern8, (6000,600))
    drawBot.image(pattern8, (5400,0))


    
for frame in range(frames2):
    drawBot.newPage(8400, 4200)
    drawBot.frameDuration(duration)
    drawBot.image(pattern, (0,0))
    drawBot.image(pattern, (1200,1200))
    drawBot.image(pattern, (600,600))
    drawBot.image(pattern, (600,0))
    drawBot.image(pattern, (600,1200))
    drawBot.image(pattern, (0,1200))
    drawBot.image(pattern, (0,600))
    drawBot.image(pattern, (1200,600))



    drawBot.image(pattern1, (2400,2400+600))
    drawBot.image(pattern1, (2400,3000+600))
    drawBot.image(pattern1, (3000,1800+600))
    drawBot.image(pattern1, (1800,2400+600))
    drawBot.image(pattern1, (1800,3000+600))
    drawBot.image(pattern1, (3000,2400+600))
    drawBot.image(pattern1, (2400,1800+600))
    drawBot.image(pattern1, (3000,3000+600))



    drawBot.image(pattern2, (3000,600))
    drawBot.image(pattern2, (2400,1200))
    drawBot.image(pattern2, (1800,0))
    drawBot.image(pattern2, (1800,600))
    drawBot.image(pattern2, (3000,0))
    drawBot.image(pattern2, (2400,0))
    drawBot.image(pattern2, (1800,1200))
    drawBot.image(pattern2, (2400,600))


    drawBot.image(pattern3, (1200,3000+600))
    drawBot.image(pattern3, (600,1800+600))
    drawBot.image(pattern3, (600,2400+600))
    drawBot.image(pattern3, (600,3000+600))
    drawBot.image(pattern3, (0,2400+600))
    drawBot.image(pattern3, (1200,1800+600))
    drawBot.image(pattern3, (1200,2400+600))
 #   drawBot.image(pattern3, (600,1800+600))
    drawBot.image(pattern3, (0,1800+600))



    drawBot.image(pattern4, (4200,2400+600))
    drawBot.image(pattern4, (4200,3000+600))
    drawBot.image(pattern4, (4800,1800+600))
    drawBot.image(pattern4, (4800,2400+600))
    drawBot.image(pattern4, (3600,1800+600))
    drawBot.image(pattern4, (3600,3000+600))
    drawBot.image(pattern4, (4200,1800+600))
    drawBot.image(pattern4, (3600,2400+600))



    drawBot.image(pattern6, (4200,1200))
    drawBot.image(pattern6, (4800,0))
    drawBot.image(pattern6, (4800,600))
    drawBot.image(pattern6, (4800,1200))
    drawBot.image(pattern6, (3600,0))
    drawBot.image(pattern6, (3600,600))
    drawBot.image(pattern6, (3600,1200))
    drawBot.image(pattern6, (4200,0))



    drawBot.image(pattern7, (5400,3000+600))
    drawBot.image(pattern7, (6000,1800+600))
    drawBot.image(pattern7, (5400,2400+600))
    drawBot.image(pattern7, (5400,1800+600))
    drawBot.image(pattern7, (6000,2400+600))
    drawBot.image(pattern7, (6600,3000+600))
    drawBot.image(pattern7, (6600,1800+600))
    drawBot.image(pattern7, (6000,3000+600))




    drawBot.image(pattern8, (6600,1200))
    drawBot.image(pattern8, (6600,0))
    drawBot.image(pattern8, (6600,600))
    drawBot.image(pattern8, (6000,1200))
    drawBot.image(pattern8, (5400,1200))
    drawBot.image(pattern8, (6000,600))
    drawBot.image(pattern8, (5400,0))
    drawBot.image(pattern8, (6000,0))





    
for frame in range(frames2):
    drawBot.newPage(8400, 4200)
    drawBot.frameDuration(duration2)
    drawBot.image(pattern, (0,0))
    drawBot.image(pattern, (1200,1200))
    drawBot.image(pattern, (600,600))
    drawBot.image(pattern, (600,0))
    drawBot.image(pattern, (600,1200))
    drawBot.image(pattern, (0,1200))
    drawBot.image(pattern, (0,600))
    drawBot.image(pattern, (1200,600))
    drawBot.image(pattern, (1200,0))


    drawBot.image(pattern1, (1800,1800+600))
    drawBot.image(pattern1, (2400,2400+600))
    drawBot.image(pattern1, (2400,3000+600))
    drawBot.image(pattern1, (3000,1800+600))
    drawBot.image(pattern1, (1800,2400+600))
    drawBot.image(pattern1, (1800,3000+600))
    drawBot.image(pattern1, (3000,2400+600))
    drawBot.image(pattern1, (2400,1800+600))
    drawBot.image(pattern1, (3000,3000+600))


    drawBot.image(pattern2, (3000,600))
    drawBot.image(pattern2, (2400,1200))
    drawBot.image(pattern2, (1800,0))
    drawBot.image(pattern2, (1800,600))
    drawBot.image(pattern2, (3000,0))
    drawBot.image(pattern2, (2400,0))
    drawBot.image(pattern2, (1800,1200))
    drawBot.image(pattern2, (2400,600))
    drawBot.image(pattern2, (3000,1200))



    drawBot.image(pattern3, (1200,3000+600))
    drawBot.image(pattern3, (600,1800+600))
    drawBot.image(pattern3, (600,2400+600))
    drawBot.image(pattern3, (600,3000+600))
    drawBot.image(pattern3, (0,2400+600))
    drawBot.image(pattern3, (1200,1800+600))
    drawBot.image(pattern3, (1200,2400+600))
 #   drawBot.image(pattern3, (600,1800+600))
    drawBot.image(pattern3, (0,1800+600))
    drawBot.image(pattern3, (0,3000+600))



    drawBot.image(pattern4, (4200,2400+600))
    drawBot.image(pattern4, (4200,3000+600))
    drawBot.image(pattern4, (4800,1800+600))
    drawBot.image(pattern4, (4800,2400+600))
    drawBot.image(pattern4, (3600,1800+600))
    drawBot.image(pattern4, (3600,3000+600))
    drawBot.image(pattern4, (4200,1800+600))
    drawBot.image(pattern4, (3600,2400+600))
    drawBot.image(pattern4, (4800,3000+600))



    drawBot.image(pattern6, (4200,1200))
    drawBot.image(pattern6, (4800,0))
    drawBot.image(pattern6, (4800,600))
    drawBot.image(pattern6, (4800,1200))
    drawBot.image(pattern6, (3600,0))
    drawBot.image(pattern6, (3600,600))
    drawBot.image(pattern6, (3600,1200))
    drawBot.image(pattern6, (4200,0))
    drawBot.image(pattern6, (4200,600))



    drawBot.image(pattern7, (5400,3000+600))
    drawBot.image(pattern7, (6000,1800+600))
    drawBot.image(pattern7, (5400,2400+600))
    drawBot.image(pattern7, (5400,1800+600))
    drawBot.image(pattern7, (6000,2400+600))
    drawBot.image(pattern7, (6600,3000+600))
    drawBot.image(pattern7, (6600,1800+600))
    drawBot.image(pattern7, (6000,3000+600))
    drawBot.image(pattern7, (6600,2400+600))



    drawBot.image(pattern8, (6600,1200))
    drawBot.image(pattern8, (6600,0))
    drawBot.image(pattern8, (6600,600))
    drawBot.image(pattern8, (6000,1200))
    drawBot.image(pattern8, (5400,1200))
    drawBot.image(pattern8, (6000,600))
    drawBot.image(pattern8, (5400,0))
    drawBot.image(pattern8, (6000,0))
    drawBot.image(pattern8, (5400,600))


   


    
 #       drawBot.image(pattern, (100,100))

 
 
                  
drawBot.saveImage("~/Desktop/pattern-new.gif")

'''from dropbox.files import WriteMode
  
file_from = "/Users/vasilij/Desktop/pattern-new.gif"
file_to = '/JOURNAL FOR RAW VISUAL DATA/pattern-new.gif'    
def upload_file(file_from, file_to):
      dbx = dropbox.Dropbox('NCxDDo1Hp7oAAAAAAABDgx44kGeJMknVnm1XnWnUHAvnJ4Eo2mDcI3iU4ehkvwIy')
      f = open(file_from, 'rb')
      dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
upload_file(file_from,file_to)'''

cloudinary.config( 
  cloud_name = "duf9i9rcz", 
  api_key = "177761493453354", 
  api_secret = "oxDrxtdPs4XGSStMtyGmJEkQzXo" 
)
cloudinary.utils.cloudinary_url("pattern-new", version="12345678", secure=True, format="gif")

cloudinary.uploader.upload("/Users/vasilij/Desktop/pattern-new.gif",                           
  public_id = "pattern-new",
  overwrite = 'true', 
  #notification_url = "https://mysite.example.com/notify_endpoint", 
  resource_type = "image")




