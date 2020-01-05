import face_recognition
from PIL import Image, ImageDraw
#
image_of_ronaldo = face_recognition.load_image_file('./img/Known/Ronaldo/ronaldo.jpg')
face_encoding_of_ronaldo = face_recognition.face_encodings(image_of_ronaldo)[0]

image_of_messi = face_recognition.load_image_file(
    './img/Known/Messi/messi.png')
face_encoding_of_messi = face_recognition.face_encodings(image_of_messi)[0]

image_of_neymar = face_recognition.load_image_file(
    './img/Known/Neymar/neymar.jpg')
face_encoding_of_neymar = face_recognition.face_encodings(image_of_neymar)[0]

image_of_suarez = face_recognition.load_image_file(
    './img/Known/Suarez/suarez.jpg')
face_encoding_of_suarez = face_recognition.face_encodings(image_of_suarez)[0]

image_of_benzema = face_recognition.load_image_file(
    './img/Known/Benzema/benzema.jpg')
face_encoding_of_benzema = face_recognition.face_encodings(image_of_benzema)[0]

image_of_bale = face_recognition.load_image_file('./img/Known/Bale/bale.jpg')
face_encoding_of_bale = face_recognition.face_encodings(image_of_bale)[0]

known_face_encodings = [

    face_encoding_of_ronaldo,
    face_encoding_of_messi,
    face_encoding_of_neymar,
    face_encoding_of_suarez,
    face_encoding_of_benzema,
    face_encoding_of_bale

]

known_face_names = [
    "Ronaldo",
    "Messi",
    "Neymar",
    "Suarez",
    "Benzema",
    "Bale"
]

# load face images to find faces in

# test_image = face_recognition.load_image_file('./img/Known/me.jpg')
test_image = face_recognition.load_image_file('./img/Known/msn.jpg')
# test_image = face_recognition.load_image_file('./img/Known/bbc.jpg')


face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format
pil_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through the faces in the test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(
        known_face_encodings, face_encoding, tolerance=0.55)
    name = "Unknown"

    if True in matches:
        match_index = matches.index(True)
        name = known_face_names[match_index]

    # Draw Box
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))
    # Draw Laber
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10),
                    (right, bottom)), fill=(0, 0, 0), outline=(0, 0, 0))
    draw.text((left + 6, bottom - text_height - 5), name, fill="white")

del draw
pil_image.show()
