# プログラムの説明
![guiwindow](https://user-images.githubusercontent.com/96273564/206103286-6239fa7d-3527-42cc-94f4-95380c612d22.png)

上記のようなウィンドウを生成するクラス。  
ボタンを配置して、そのボタンの名前と関数を指定することができる。
# 使用方法
ボタンを押されたとき実行する関数によって変わる。  
今回はファイルを参照させてファイルパスを読み込むものにしている。
  
# 処理の流れ
各メソッドについて説明する。
  
## init(root)
インスタンス生成時に実行されるメソッド。  
ボタンとボタンの間の空間を適当に調整する。  
- **root** 型名:tkinter.Tk  
メインで読み込んだtk.Tk()
  
## place_button(text,func,button_name)  
ボタンの名前と、ボタンが押されたとき実行される関数を指定して、  
その機能を持ったボタンを用意するメソッド。
ボタンの配置は別メソッドで行う。
- **text** 型名:string  
ウィンドウ上のボタンに書かれる文字列  
- **func** 型名:function  
ボタンを押されたとき実行する関数  
引数付きの関数を渡す場合、**lambda式を使う必要がある**  
実行例:  
window.place_button("テスト", lambda:[関数(100)])  
- **button_name** 型名:string  
ボタンの内部名
dictで管理され、あとから参照/メソッド実行できる

## button_pack_all()  
ボタンを配置するメソッド。
  
## button_enable(button_name)  
ボタンを有効化する(グレーアウトから復帰させる)メソッド。
- **button_name** 型名:tkinter.Tk  
有効化する対象ボタンの名前
## button_disable(button_name)  
ボタンを無効化する(グレーアウトさせる)メソッド。  
- **button_name** 型名:tkinter.Tk  
無効化する対象ボタンの名前


## 実行環境

※このクラス自体は組み込み関数しか使っていないが、呼び出した顔認識プログラムにライブラリが必要。  
python 3.11.0  

click                   8.1.3  
colorama                0.4.6  
dlib                    19.24.99  
dlib                    19.24.99  
face-recognition        1.3.0  
face-recognition-models 0.3.0  
numpy                   1.23.4  
Pillow                  9.3.0  
pip                     22.3.1  
setuptools              65.5.0  
![d](https://user-images.githubusercontent.com/96273564/205794735-767ac40d-3e34-42ba-8cb5-744c08a3bba8.png)

