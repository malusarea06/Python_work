import os
i = 0
os.chdir("/Users/aniketmalusare/Documents/C_prog/")
#os.rename("1.py","Div7.py")
for file in os.listdir("/Users/aniketmalusare/Documents/C_prog/"):
   if file.endswith(".mp3"):
      os.rename(file,str(i)+"_"+file)
      i = i + 1

