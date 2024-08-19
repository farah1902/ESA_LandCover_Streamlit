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
        # Create the map object
        m = leafmap.Map()

        # Add the split map with ESA layers
        m.split_map(
            left_layer='ESA WorldCover 2020 S2 FCC', 
            right_layer='ESA WorldCover 2020'
        )

        # Add satellite basemap
        m.add_tile_layer(
            url="https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png", 
            name="Satellite", 
            attribution="Map data © OpenStreetMap contributors"
        )

        # Add OpenStreetMap basemap
        m.add_tile_layer(
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", 
            name="OpenStreetMap", 
            attribution="Map data © OpenStreetMap contributors"
        )
        
        # Add a legend
        m.add_legend(title='ESA Land Cover', builtin_legend='ESA_WorldCover')

# Render the map in Streamlit
m.to_streamlit(height=700)
