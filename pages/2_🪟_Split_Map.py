import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
Web App URL: <https://saadfrh-esa-landcover.streamlit.app/>
\nGitHub Repository: <https://github.com/farah1902/ESA_LandCover_Streamlit>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.postimg.cc/yddLX0NY/gep1.png"
st.sidebar.image(logo)

personal_link = "Developed by [Saad Farah](https://saadfrh.github.io/)"
st.sidebar.markdown(personal_link)

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map()
        m.split_map(
            left_layer='ESA WorldCover 2020 S2 FCC', right_layer='ESA WorldCover 2020'
        )
        m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')

m.to_streamlit(height=700)
