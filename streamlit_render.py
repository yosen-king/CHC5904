#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   streamlit_render.py
@Time    :   2024/11/20 22:51:37
@Author  :   Jackson YOU 
@Version :   1.0
@Desc    :   put the content from reflective essay and the map into the streamlit
'''

import streamlit as st

# Read the content of the essay.md file
with open('output/essay1.md', 'r', encoding='utf-8') as file:
    essay_content = file.read()

# Split the content to insert maps under "Key Findings and Interpretation"
parts = essay_content.split('### Key Findings and Interpretation')

# Display the first part of the essay
st.markdown(parts[0])

# Display the "Key Findings and Interpretation" section with maps
st.markdown("### Key Findings and Interpretation" + parts[1].split('###')[0])

# Display the maps
st.markdown("#### Heat map of the frequency for prefectures")
with open('map1.html', 'r', encoding='utf-8') as file:
    map1_html = file.read()
st.components.v1.html(map1_html, height=600)

st.markdown("#### Trajactories of the 匡超人 in the chapter 10-20")
with open('map2.html', 'r', encoding='utf-8') as file:
    map2_html = file.read()
st.components.v1.html(map2_html, height=600)

# Display the rest of the essay
st.markdown("###" + "###".join(parts[1].split('###')[1:]))

