from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import face_recognition
import numpy as np
import cv2

class Sunglass_collage:

  def __init__(self, picture) :
    self.img1 = picture

  def Sunglass(self) :
    # jpg画像のロード
    img2 = face_recognition.load_image_file("sunglass.jpg")

    face_landmarks_list = face_recognition.face_landmarks(self.img1)

    # face_landmarksリストに入る
    for face_landmarks in face_landmarks_list:

      # 左目に関する座標の列ごと(x,y)の最大、最小を抜き出す
      l_eye_max = np.array(face_landmarks['left_eye']).max(axis=0)
      l_eye_min = np.array(face_landmarks['left_eye']).min(axis=0)

      # わかりやすいように配列から変数へ ただ、なおのことわかりずらくなってしまった気がする。
      l_eye_xmax = l_eye_max[0]
      l_eye_ymax = l_eye_max[1]
      l_eye_xmin = l_eye_min[0]
      l_eye_ymin = l_eye_min[1]

      # 上の右目バージョン
      r_eye_max = np.array(face_landmarks['right_eye']).max(axis=0)
      r_eye_min = np.array(face_landmarks['right_eye']).min(axis=0)

      r_eye_xmax = r_eye_max[0]
      r_eye_ymax = r_eye_max[1]
      r_eye_xmin = r_eye_min[0]
      r_eye_ymin = r_eye_min[1]

      chin_max = np.array(face_landmarks['chin']).max(axis=0)
      chin_min = np.array(face_landmarks['chin']).min(axis=0)

      chin_xmax = chin_max[0]
      chin_xmin = chin_min[0]
      chin_ymax = chin_max[1]
      chin_ymin = chin_min[1]

      # x座標の最大(今回の場合右の眼の最大のx)、最小(今回の場合左目の最小)座標を抜き出し、サングラスの画像をいい感じに合わせるために倍率を調整
      shift_x = (chin_xmax - chin_xmin) / 4

      xmax = int(r_eye_xmax + shift_x)
      xmin = int(l_eye_xmin - shift_x)

      # 上のy座標バージョン
      shift_base_y = (chin_ymax - chin_ymin)

      ymx = max(l_eye_ymax,r_eye_ymax)
      ymn = min(l_eye_ymin,r_eye_ymin)

      ymax = int(ymx + shift_base_y / 9)
      ymin = int(ymn - shift_base_y / 4.5)


      # 調整したサングラスの画像を重ねる場所のサイズの計算
      x_size = xmax - xmin
      y_size = ymax - ymin

      # サングラスの画像の大きさを上で計算した通りにリサイズ
      img2 = cv2.resize(img2,(x_size,y_size))

      # img1からサングラスの画像を重ねる部分の切り出し(画像を重ねる際、画像の大きさが同じでなければならないため)
      rows,cols,channels = img2.shape
      roi = self.img1[ymin:ymax,xmin:xmax]
      plt.imshow(roi)

      # 切り出した部分に画像を重ねる
      final_roi = cv2.bitwise_and(roi,img2)

      #large_img = img1
      small_img = final_roi

      # 切り出して画像を重ねた画像をもと画像のもとの位置に合成
      self.img1[ymin:ymin+small_img.shape[0], xmin:xmin+small_img.shape[1]] = small_img

      return self.img1

if __name__ == "__main__" :

  img1 = face_recognition.load_image_file("biden.jpg")

  sunglass = Sunglass_collage(img1)

  img3 = sunglass.Sunglass()

  plt.imshow(img3)