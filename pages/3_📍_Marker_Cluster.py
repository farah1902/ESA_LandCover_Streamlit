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

st.title("Marker Cluster")

with st.expander("See source code"):
    with st.echo():

        m = leafmap.Map(center=[40, -100], zoom=4)
        cities = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv'
        regions = 'https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_regions.geojson'

        m.add_geojson(regions, layer_name='US Regions')
        m.add_points_from_xy(
            cities,
            x="longitude",
            y="latitude",
            color_column='region',
            icon_names=['gear', 'map', 'leaf', 'globe'],
            spin=True,
            add_legend=True,
        )
        
m.to_streamlit(height=700)
