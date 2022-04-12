# PythonでPIV解析

オリジナルは <https://watlab-blog.com/2021/01/31/piv-vector/>  
連続の解析結果画像ではなく，1つの解析結果として出力するように改造しました．  
opencv-python, numpy, matplotlib が必要です．

## avislice.py
動画ファイルを連続静止画にします  
`py avislice.py sample/s0.avi`

## piv.py
連続静止画からPIV解析を行います  
`py piv.py sample/s0`
  
![解析結果](/sample/s0.png)