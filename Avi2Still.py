import sys
import os
import argparse
import cv2
import numpy as np

## 使い方
## py Mov2Still.py foo.avi
## カレントディレクトリに foo.png で動画が静止画に

def m_slice(path, dir, extension, step):
    movie = cv2.VideoCapture(path)                  # 動画の読み込み
    Fs = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))   # 動画の全フレーム数を計算
    path_head = dir + '_'                           # 静止画のファイル名のヘッダー
    ext_index = np.arange(0, Fs, step)              # 静止画を抽出する間隔

    for i in range(Fs - 1):                         # フレームサイズ分のループを回す
        flag, frame = movie.read()                  # 動画から1フレーム読み込む
        check = i == ext_index                      # 現在のフレーム番号iが、抽出する指標番号と一致するかチェックする
        
        # frameを取得できた(flag=True)時だけ処理を行う
        if flag == True:
            # もしi番目のフレームが静止画を抽出するものであれば、ファイル名を付けて保存する
            if True in check:
                # ファイル名は後でフォルダ内で名前でソートした時に連番になるようにする
                path_out = path_head + str(i).zfill(5) + extension
                print(path_out)
                cv2.imwrite(path_out, frame)
    return

# 引数処理
parser = argparse.ArgumentParser(description='動画ファイルから静止画を出力します．')
parser.add_argument('inFile', help='分割したい動画ファイル名')
parser.add_argument('-o', help='出力フォルダ．省略するとカレントディレクトリに出力されます．')
parser.add_argument('-s', help='動画分割数．')
args = parser.parse_args()

print(args.inFile)
exit()

if len(sys.argv) <= 1:
    print()
    exit()

# 関数実行：引数=（ファイル名のパス、保存先のフォルダパス、静止画拡張子、ステップ数）
m_slice(sys.argv[1], os.path.splitext(sys.argv[1])[0], '.png', 50)
