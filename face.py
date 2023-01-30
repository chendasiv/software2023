import face_recognition
import numpy as np
from PIL import Image, ImageDraw

import glob
import os

def face_func(dic_dir, unk_dir):
    #print(dic_dir)
    #print(unk_dir)
    dic = sorted(glob.glob(dic_dir + '/*.jpg'))
    unk = sorted(glob.glob(unk_dir + '/*.jpg')) #unknown
    print(dic)
    known_face_encodings = []
    known_face_names = []

    for img in dic:
        name = os.path.splitext(os.path.basename(img))[0]

        people_image = face_recognition.load_image_file(img)
        people_encoding = face_recognition.face_encodings(people_image)[0]

        known_face_encodings.append(people_encoding)
        known_face_names.append(name)

    for img in unk:
        unknown_image = face_recognition.load_image_file(img)

        face_locations = face_recognition.face_locations(unknown_image)
        face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

        pil_image = Image.fromarray(unknown_image)

        draw = ImageDraw.Draw(pil_image)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

            text_width, text_height = draw.textsize(name)
            draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
            draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))
            print(name)

            del draw

            # ここの分類をどうするか？
            pil_image.show()

if __name__ == "__main__" :

    dic_dir = '_dic/'
    unk_dir = '_img/'

    face_func(dic_dir, unk_dir)