import numpy as np
import pandas as pd
import streamlit as st
from skimage.io import imread


# download the image
img_url = 'https://stat.ameba.jp/user_images/20191108/21/hanakoko-info/3a/db/j/o0602080014634893674.jpg?caw=800'

im = imread(img_url)

st.image(im, caption='image from wikimedia commons',
         use_column_width=True)


# show histgram of all colors
hist_red, _ = np.histogram(im[:, :, 0], bins=64)
hist_green, _ = np.histogram(im[:, :, 1], bins=64)
hist_blue, _ = np.histogram(im[:, :, 2], bins=64)
hist = np.stack((hist_red, hist_green, hist_blue), axis=1)

df_hist = pd.DataFrame(hist, columns=['R', 'G', 'B'])
st.bar_chart(df_hist)


# choose one color
color = st.radio(
    "choose R, G, or B",
    ('R', 'G', 'B'))
if color == 'R':
    df_hist = pd.DataFrame(hist_red)
    st.bar_chart(df_hist)
if color == 'G':
    df_hist = pd.DataFrame(hist_green)
    st.bar_chart(df_hist)
if color == 'B':
    df_hist = pd.DataFrame(hist_blue)
    st.bar_chart(df_hist)
