import face_recognition

image_of_messi = face_recognition.load_image_file('./img/Known/Messi/messi.png')
face_encodings_of_Messi = face_recognition.face_encodings(image_of_messi)[0]

unknown_image = face_recognition.load_image_file('./img/Unkown/messi_Irani.jpg')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

#Here, we compare the faces
results = face_recognition.compare_faces([face_encodings_of_Messi], unknown_face_encoding, tolerance= 0.55)

if results[0]:
    print('This is Messi')
else:
    print('This is NOT Messi')




