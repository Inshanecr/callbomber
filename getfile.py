import os 
a = os.listdir("pornhub")
for i in a:

    b = os.listdir(f"pornhub/{i}")
    for c in b:
       gg = (f"pornhub/{i}/{c}")
       with open("i.py","a+") as file:
            file.write(str(gg)+"\n")