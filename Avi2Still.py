import sys
import cv2
import numpy as np

## 使い方
## py Mov2Still.py foo.avi
## カレントディレクトリに foo.png で動画が静止画に

def m_slice(path, dir, step, extension):
    movie = cv2.VideoCapture(path)                  # 動画の読み込み
    Fs = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))   # 動画の全フレーム数を計算
    path_head = dir + '\out_'                       # 静止画のファイル名のヘッダー
    ext_index = np.arange(0, Fs, step)              # 静止画を抽出する間隔

    for i in range(Fs - 1):                         # フレームサイズ分のループを回す
        flag, frame = movie.read()                  # 動画から1フレーム読み込む
        check = i == ext_index                      # 現在のフレーム番号iが、抽出する指標番号と一致するかチェックする
        
        # frameを取得できた(flag=True)時だけ処理を行う
        if flag == True:
            # もしi番目のフレームが静止画を抽出するものであれば、ファイル名を付けて保存する
            if True in check:
                # ファイル名は後でフォルダ内で名前でソートした時に連番になるようにする
                if i < 10:
                    path_out = path_head + '0000' + str(i) + extension
                elif i < 100:
                    path_out = path_head + '000' + str(i) + extension
                elif i < 1000:
                    path_out = path_head + '00' + str(i) + extension
                elif i < 10000:
                    path_out = path_head + '0' + str(i) + extension
                else:
                    path_out = path_head + str(i) + extension
                cv2.imwrite(path_out, frame)
            # i番目のフレームが静止画を抽出しないものであれば、何も処理をしない
            else:
                pass
        else:
            pass
    return

# 引数処理
if len(sys.argv) < 1:
    print('Usage: py Mov2Still 動画ファイル名')
    exit()

# 関数実行：引数=（ファイル名のパス、保存先のフォルダパス、ステップ数、静止画拡張子）
m_slice(sys.argv[1], 'dir', 50, '.png')
