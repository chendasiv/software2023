
import os,sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


"""
プログラムの説明
使用方法
処理の流れ
実行環境
これら4つを示すこと
"""

def display_result_button(root,entry):
    text=entry.get()
    end_flag=False
    disp=""
    if len(text) !=0:
        disp=text
        end_flag=True
    else:
        disp="File not selected"
    messagebox.showinfo("info",disp)

    if end_flag:
        root.destroy()

def dirdialog_clicked():
    iDir = os.path.abspath(os.path.dirname(__file__))
    iDirPath = filedialog.askdirectory(initialdir = iDir)
    entry1.set(iDirPath)

# ファイル指定の関数
def filedialog_clicked(entry):
    fTyp = [("", ".png",".jpg")]
    iFile = os.path.abspath(os.path.dirname(__file__))
    iFilePath = filedialog.askopenfilenames(filetype = fTyp, initialdir = iFile)
    entry.set(iFilePath)

def main():
    root=tk.Tk()
    root.title("File Selection")

    frame=ttk.Frame(root,padding=10)
    
    # ボタン用フレーム作成
    frame_exe_button = ttk.Frame(root, padding=10)
    frame_exe_button.grid(row=5,column=1,sticky=tk.W)


    # 「ファイル参照」エントリーの作成
    path_container = tk.StringVar()


    # 「ファイル参照」ボタンの作成
    IFileButton = ttk.Button(frame_exe_button, text="参照", command=lambda:filedialog_clicked(path_container))
    IFileButton.pack(fill="x",padx=30,side="left")

    # 実行ボタンの設置
    button1 = ttk.Button(frame_exe_button, text="実行", command=lambda:display_result_button(root,path_container))
    button1.pack(fill = "x", padx=30, side = "left")

    # キャンセルボタンの設置
    button2 = ttk.Button(frame_exe_button, text="閉じる", command=quit)
    button2.pack(fill = "x", padx=30, side = "left")
    root.mainloop()
    print(path_container.get())
    return path_container.get()

if __name__ == "__main__":
    main()