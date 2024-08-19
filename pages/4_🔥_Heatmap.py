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

st.title("Heatmap")

with st.expander("See source code"):
    with st.echo():
        filepath = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
        m = leafmap.Map(center=[40, -100], zoom=4, tiles="stamentoner", attr="Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.")
        m.add_heatmap(
            filepath,
            latitude="latitude",
            longitude="longitude",
            value="pop_max",
            name="Heat map",
            radius=20,
        )

m.to_streamlit(height=700)
