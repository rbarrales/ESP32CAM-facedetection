from deepface import DeepFace

print ("inicio")

#df = DeepFace.find(img_path = "pic4.jpg", db_path = "/home/hugo/my_db")
df = DeepFace.find(img_path = "/home/rbg/my_db/ray/ray_2.jpg",db_path= "/home/rbg/my_db", enforce_detection="false")
print ("Resultado ")
print (df)
