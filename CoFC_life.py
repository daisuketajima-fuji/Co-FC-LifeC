import streamlit as st 
import pandas as pd
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import folium

# LC_image.pngのURLを指定する
image_url = 'https://github.com/daisuketajima-fuji/Co-FC-LifeC/raw/main/LC_image.png'

# 画像を取得して開く
response = requests.get(image_url)
image = Image.open(BytesIO(response.content))

# Streamlitで表示する
st.image(image, caption='班：Co-FC', use_column_width=True)

df = pd.read_csv('suumo4_Co-FC.csv')

st.sidebar.write('質問に回答して、実行ボタンを教えてください。')

values = st.sidebar.slider(
    "家賃の予算を万円単位で教えてください",
    8.0, 15.0, (8.0,15.0))


option_radio = st.sidebar.radio(
    "ライフスタイルとして重視するものとして、LifeとWorkをいずれかを選択してください",
    ('Life','Work'))

option_select = st.sidebar.selectbox(
    '在宅度を教えてください',
    ('在宅多め','在宅少なめ','在宅なし'))


option_button = st.sidebar.button('実行')
if option_button == True:
    st.sidebar.write('実行されました')
    st.write('あなたの予算は{:.1f}万円から{:.1f}万円ですね。'.format(values[0],values[1]))
    st.write('あなたの選んだ生活スタイルは、',option_radio,'重視ですね。')
    st.write('あなたの在宅度は',option_select,'ですね。')
    """
    あなたにおすすめの物件は、
    東京都江戸川区東葛西５の1LDK月額125,000円の物件です。
    こちらは、東京メトロ東西線葛西駅徒歩8分、築10年の物件で8階建ての5階に位置しており、バストイレ別、室内乾燥機付き、角部屋です。
    近くには多くのレストランがありますので、Workを重視するあなたにはぴったりの物件となります。周辺のレストランを地図で表示します。
    """

    # 地図データをローカルに保存したファイルのパス
    map_html_path = 'restaurants_map.html'

    # 地図データを表示
    st.components.v1.html(open(map_html_path, 'r', encoding='utf-8').read(), height=500)
  
    #一旦、以下の地図は非表示とする。
    #kasai5chome_lat = 35.665673215700444
    #kasai5chome_lon = 139.86083312591182

    #df_kasai5chome = pd.DataFrame(
    #    np.random.rand(10,2)/[80,80]+[kasai5chome_lat,kasai5chome_lon],
    #    columns=['lat','lon']
    #)

    #st.map(df_kasai5chome)
else:
    st.write('サイドバーから条件を選択して、実行ボタンを押してください。')








    
