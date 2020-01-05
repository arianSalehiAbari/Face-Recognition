import dlib
import face_recognition

im = face_recognition.load_image_file('./img/Known/msn.jpg')
face_locations = face_recognition.face_locations(im)

# Array of coords of the faces in the image
print(face_locations)

# Number of people within the image
print(f'There are {len(face_locations)} people in this image')
