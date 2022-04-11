import os
import argparse
import cv2
import numpy as np

## 使い方
## py Avi2Still.py -h

def m_slice(path, out, step):
    movie = cv2.VideoCapture(path)                  # 動画の読み込み
    Fs = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))   # 動画の全フレーム数を計算
    ext_index = np.arange(0, Fs, step)              # 静止画を抽出する間隔

    for i in range(Fs - 1):                         # フレームサイズ分のループを回す
        flag, frame = movie.read()                  # 動画から1フレーム読み込む
        check = i == ext_index                      # 現在のフレーム番号iが、抽出する指標番号と一致するかチェックする
        
        # frameを取得できた(flag=True)時だけ処理を行う
        if flag == True:
            # もしi番目のフレームが静止画を抽出するものであれば、ファイル名を付けて保存する
            if True in check:
                # ファイル名は後でフォルダ内で名前でソートした時に連番になるようにする
                path_out = out + '\\' + str(i).zfill(5) + '.png'
                print(path_out)
                cv2.imwrite(path_out, frame)
    return

# 引数処理
parser = argparse.ArgumentParser(description='動画ファイルから静止画を出力します．')
parser.add_argument('inFile', help='分割したい動画ファイル名．漢字を含むフォルダやファイル名はやめておきましょう．')
parser.add_argument('-o', '--outFolder', help='出力フォルダ．省略すると動画ファイル名と同じフォルダが作られます．')
parser.add_argument('-s', '--split', type=int, default=10, help='動画スキップ数．')
args = parser.parse_args()

if not args.outFolder:
    args.outFolder = os.path.splitext(os.path.basename(args.inFile))[0]
if not os.path.exists(args.outFolder):
    os.mkdir(args.outFolder)

# 関数実行：引数=（ファイル名のパス、保存先のフォルダパス、静止画拡張子、ステップ数）
m_slice(args.inFile, args.outFolder, args.split)
