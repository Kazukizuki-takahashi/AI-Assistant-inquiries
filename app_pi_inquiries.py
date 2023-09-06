
import streamlit as st
from streamlit.components.v1 import html

# サービス名を表示する
st.title("お問い合わせ")

# Using the st.components.v1.html method with a specified height
st.components.v1.html('<iframe src="https://docs.google.com/forms/d/e/1FAIpQLScHlR9LYv3fmFuhHP0uqwX3SOLJYvELtfz-a0G_VAh5JJPnrw/viewform?embedded=true" width="100%" height="2000"></iframe>', height=2000)
