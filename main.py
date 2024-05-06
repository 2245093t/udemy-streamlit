import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import time

st.title('streamlit超入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(df) #折れ線グラフ
st.area_chart(df) #面グラフ
st.bar_chart(df) #棒グラフ

df = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
    columns=['lat', 'lon'] #緯度経度
)
st.map(df) #地図

st.write(df)
st.dataframe(df.style.highlight_max(axis=0), width=100, height=100) #axis=0で列方向に最大値をハイライト
st.table(df) #スクロールできない(静的)

st.write('Display Image')

if st.checkbox('Show Image'): #チェックボックス true or false
    img = Image.open('IMG_1790.jpg') #できひん
    st.image(img, caption='シャーレ', use_column_width=True) #use_column_width=Trueで画像の幅を調整

st.write('Interactive Widgets') #動的に変化するウィジェット
option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)

'あなたの好きな数字は', option, 'です'

left_column, right_column = st.columns(2) #2列に分割

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander = st.expander('問い合わせ') #折りたたみ
expander.write('問い合わせ内容を書く1')
expander.write('問い合わせ内容を書く2')
expander.write('問い合わせ内容を書く3')

expander2 = st.expander('問い合わせ2') #折りたたみ
expander2.write('問い合わせ内容を書く1')

expander3 = st.expander('問い合わせ3') #折りたたみ
expander3.write('問い合わせ内容を書く1')

text = st.text_input('あなたの趣味を教えてください')
condition = st.slider('あなたの今の調子は？', 0, 100, 50) #0~100のスライダー。初期値50

'あなたの趣味は', text, 'です'
'コンディション:', condition

"""
# 章

## 節

### 項


```python
import streamlit as st
import pandas as pd
import numpy as np
```

"""

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty() #空のコンテナ. 後からテキストを追加できる
bar = st.progress(0) #プログレスバー

for i in range(100):
    latest_iteration.text(f'Iteration {i+1} %') #テキストの更新
    bar.progress(i + 1) #プログレスバーの更新
    time.sleep(0.1) #0.1秒待つ

'Done!!'