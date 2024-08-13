import streamlit as st

st.set_page_config(layout="wide")
import streamlit as st
import streamlit as st

# Başlık ve stil ayarları
st.markdown(
    """
    <style>
    .title {
        color: #00BFFF;  /* Koyu mavi renk */
        font-size: 96px;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    </style>
    <h1 class="title">Kar Tanesi ❄️</h1>
    """,
    unsafe_allow_html=True
)

DEFAULT_WIDTH = 30
import streamlit as st

# Metin ve stil ayarları
import streamlit as st

# Metin ve stil ayarları
st.markdown(
    """
    <style>
    .green-text {
        font-size: 24px;
        color: #228B22;  /* Orman Yeşili */
        text-align: center;
        font-family: 'Arial', sans-serif;
        background-color: #F0FFF0;  /* Honeydew */
        border: 2px solid #228B22;  /* Orman Yeşili */
        padding: 15px;
        border-radius: 10px;
    }
    </style>
    <div class="green-text">
        Fındık dalında sen kollarımda güzelsin
    </div>
    """,
    unsafe_allow_html=True
)

VIDEO_DATA_1 = "Videolar/video1.mp4"
VIDEO_DATA_3 = "Videolar/video3.mp4"
VIDEO_DATA_4 = "Videolar/video4.mp4"




# Sidebar'da genişlik ayarı için slider
width = st.sidebar.slider(
    label="Width", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%"
)

# Genişlik ve kenar boşluğu hesaplama
width = max(width, 0.01)
side = max((100 - width) / 2, 0.01)

# Üç kolonlu düzen oluşturma
_, container1, _ = st.columns([side, width, side])
_, container2, _ = st.columns([side, width, side])
_, container3, _ = st.columns([side, width, side])
_, container4, _ = st.columns([side, width, side])

# Videoları konteynerlara ekleme ve aralarına çizgi koyma
container1.video(data=VIDEO_DATA_1)
st.markdown("---")

st.markdown("---")
container3.video(data=VIDEO_DATA_3)
st.markdown("---")
container4.video(data=VIDEO_DATA_4)

st.write('✨ Bu bizim ✨')


st.audio('Videolar/Biz.mp3')

st.image('Videolar/resim1.jpeg')
st.image('Videolar/resim2.jpeg')
st.image('Videolar/resim3.jpeg')
st.image('Videolar/resim4.jpeg')
st.image('Videolar/resim5.jpeg')
st.image('Videolar/resim6.jpeg')
st.image('Videolar/resim7.jpeg')
st.image('Videolar/resim8.jpeg')

st.image('Videolar/resim11.jpeg',width=300)

st.image('Videolar/resim13.jpeg',width=300) 

import streamlit as st

# Metin ve stil ayarları
st.markdown(
    """
    <style>
    .custom-text {
        font-size: 24px;
        color: #2E3A59;  /* Koyu Mavi-Gri */
        text-align: center;
        font-family: 'Arial', sans-serif;
        background-color: #FFFFFF;  /* Beyaz */
        border: 2px solid #2E3A59;  /* Koyu Mavi-Gri */
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    <div class="custom-text">
        Gerçekte birlikte olacağımız yok, ben de senin bana baktığın resimden esinlenerek yapay zekayla aldım seni,senin de haberin olsun.
    </div>
    """,
    unsafe_allow_html=True
)


st.image('Videolar/YZ.jpeg')
import streamlit as st
st.write('🌟 Bu da senin için olsun 🌟')
st.audio('Videolar/sen.mp3')

