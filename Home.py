import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
Web App URL: <https://saadfrh-esa-landcover.streamlit.app/>
GitHub Repository: <https://github.com/farah1902/ESA_LandCover_Streamlit>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.postimg.cc/yddLX0NY/gep1.png"
st.sidebar.image(logo)

personal_link = "Developed by [Saad Farah](https://saadfrh.github.io/)"
st.sidebar.markdown(personal_link)

# Customize page title
st.title("GIS Applications with Streamlit")

st.markdown(
    """
    This multipage app demonstrates various interactive web apps created using [streamlit](https://streamlit.io) and [leafmap](https://leafmap.org). 
    """
)

st.header("Instructions")

markdown = """
1- 🗺️ [Interactive Map ](https://saadfrh-esa-landcover.streamlit.app): Visualize the map with customizable basemaps, draw polygons, and export your data as a GeoJSON file.

2- 🎚️ [Split Map ](https://saadfrh-esa-landcover.streamlit.app): Compare different maps side by side, such as ESA WorldCover 2020 S2 FCC and ESA Land Cover, to observe the differences.

3- 📍 [Marker Cluster ](https://saadfrh-esa-landcover.streamlit.app): Display multiple markers on the map, grouped into clusters, with popups providing detailed information for each location.

4- 🔥 [Heatmap ](https://saadfrh-esa-landcover.streamlit.app): Convert your CSV data into a heatmap for visualizing the intensity of data points across a region.

5- 🔎 [Basemaps ](https://saadfrh-esa-landcover.streamlit.app): Explore and load basemaps from a vast selection, including XYZ services and Quick Map Services, with over 1000 options available at your fingertips.

"""

st.markdown(markdown)

m = leafmap.Map(minimap_control=True)
m.add_basemap("OpenTopoMap")
m.to_streamlit(height=500)