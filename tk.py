from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import face_recognition
import numpy as np
import cv2

class Sunglass_collage:

    def __init__(self, picture) :
        self.img1 = picture

  # jpg画像のロード,顔認識
    def Make_list(self) :
        img2 = face_recognition.load_image_file("sunglass.jpg")
        face_landmarks_list = face_recognition.face_landmarks(self.img1)
        return face_landmarks_list,img2

  # 左目に関する座標の列ごと(x,y)の最大、最小を抜き出す
    def Left_eye_max_min(self,face_landmarks) :
        l_eye_max = np.array(face_landmarks['left_eye']).max(axis=0)
        l_eye_min = np.array(face_landmarks['left_eye']).min(axis=0)

        return l_eye_max[0],l_eye_min[0],l_eye_max[1],l_eye_min[1]

  # 右目バージョン
    def Right_eye_max_min(self,face_landmarks) :
        r_eye_max = np.array(face_landmarks['right_eye']).max(axis=0)
        r_eye_min = np.array(face_landmarks['right_eye']).min(axis=0)

        return r_eye_max[0],r_eye_min[0],r_eye_max[1],r_eye_min[1]
  # 輪郭バージョン
    def Chin_max_min(self,face_landmarks) :
        chin_max = np.array(face_landmarks['chin']).max(axis=0)
        chin_min = np.array(face_landmarks['chin']).min(axis=0)

        return chin_max[0],chin_min[0],chin_max[1],chin_min[1]

  # x座標の最大(今回の場合右の眼の最大のx)、最小(今回の場合左目の最小)座標を抜き出し、サングラスの画像をいい感じに合わせるために倍率を調整
    def Adj_x(self,chin_xmax, chin_xmin, r_eye_xmax, l_eye_xmin) :
        shift_x = (chin_xmax - chin_xmin) / 4

        xmax = int(r_eye_xmax + shift_x)
        xmin = int(l_eye_xmin - shift_x)

        return xmax,xmin

  # 上のy座標バージョン
    def Adj_y(self,chin_ymax, chin_ymin, l_eye_ymax,l_eye_ymin, r_eye_ymax, r_eye_ymin):
        shift_base_y = (chin_ymax - chin_ymin)

        ymx = max(l_eye_ymax,r_eye_ymax)
        ymn = min(l_eye_ymin,r_eye_ymin)

        ymax = int(ymx + shift_base_y / 9)
        ymin = int(ymn - shift_base_y / 4.5)

        return ymax,ymin

  # 調整したサングラスの画像を重ねる場所のサイズの計算
    def Size_calc(self,xmax, xmin, ymax, ymin):
        x_size = xmax - xmin
        y_size = ymax - ymin

        return x_size,y_size

    def Synthesis(self,x_size, y_size, img2, xmax, xmin, ymax, ymin):
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

    def Sunglass(self):
        face_landmarks_list,img2 = self.Make_list()

    # face_landmarksリストに入る
        for face_landmarks in face_landmarks_list:

            l_eye_xmax,l_eye_xmin,l_eye_ymax,l_eye_ymin = self.Left_eye_max_min(face_landmarks)

            r_eye_xmax,r_eye_xmin,r_eye_ymax,r_eye_ymin = self.Right_eye_max_min(face_landmarks)

            chin_xmax,chin_xmin,chin_ymax,chin_ymin = self.Chin_max_min(face_landmarks)

            xmax,xmin = self.Adj_x(chin_xmax, chin_xmin, r_eye_xmax, l_eye_xmin)

            ymax,ymin = self.Adj_y(chin_ymax, chin_ymin, l_eye_ymax,l_eye_ymin, r_eye_ymax, r_eye_ymin)

            x_size,y_size = self.Size_calc(xmax, xmin, ymax, ymin)

            img1 = self.Synthesis(x_size, y_size, img2, xmax, xmin, ymax, ymin)

            return img1

if __name__ == "__main__" :

    img1 = face_recognition.load_image_file("biden.jpg")

    sunglass = Sunglass_collage(img1)

    img3 = sunglass.Sunglass()

    plt.imshow(img3)

