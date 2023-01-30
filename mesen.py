from numpy import pi
from PIL import Image, ImageDraw
import face_recognition

#https://raw.githubusercontent.com/ageitgey/face_recognition/master/examples/digital_makeup.py
 

#from PIL import Image,ImageDraw

#!ls "/content/gdrive/My Drive"
# Load the jpg file into a numpy array


def find_eye_edge(landmarks,need_pos="left_upper"):
  landmarks.sort(key=lambda x:x[0])
  left=landmarks[0][0]
  landmarks.sort(key=lambda x:x[0],reverse=True)
  right=landmarks[0][0]

  landmarks.sort(key=lambda x:x[1],reverse=True)
  upper=landmarks[0][1]
  landmarks.sort(key=lambda x:x[1])
  bottom=landmarks[0][1]

  if need_pos=="left_upper":
    return (left,upper)
  elif need_pos=="right_bottom":
    return (right,bottom)
  else:
     print("need_pos invalid")
     return

def main():
  image = face_recognition.load_image_file("images/biden_2.png")

  # Find all facial features in all the faces in the image
  face_landmarks_list = face_recognition.face_landmarks(image)

  pil_image = Image.fromarray(image)
  width,height=pil_image.size
  for face_landmarks in face_landmarks_list:
    d = ImageDraw.Draw(pil_image, 'RGBA')

    """
    # Gloss the lips
    d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

    # Apply some eyeliner
    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)    
    """ 
    
    left=find_eye_edge(face_landmarks['left_eye'],need_pos="left_upper")
    right=find_eye_edge(face_landmarks['right_eye'],need_pos="right_bottom")
    
    d.rectangle([left,right], fill='black', outline='black',  width=3)

    pil_image.save("result/mesen.png")
    pil_image.show()

main()

