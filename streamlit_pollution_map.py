import streamlit as st
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

st.set_page_config(page_title="Pollution Map of Indian Cities", layout="wide")
st.title("Pollution Map of Indian Cities")

# Sample pollution data
data = {
    'City': ['Delhi', 'Chennai', 'Mumbai', 'Kolkata'],
    'PM2.5': [310, 45, 98, 112],
    'Latitude': [28.61, 13.08, 19.07, 22.57],
    'Longitude': [77.20, 80.27, 72.87, 88.36]
}
pollution_df = pd.DataFrame(data)

# Load India shapefile (replace with your path or download if not present)
@st.cache_data
def load_shapefile():
    # Example: 'india_shapefile.shp' should be in the same directory or provide full path
    try:
        india = gpd.read_file('india_st.shp')
        return india
    except Exception as e:
        st.error("Shapefile not found. Please add 'india_st.shp' to the directory.")
        return None

india = load_shapefile()

# Create GeoDataFrame for cities
geometry = [Point(xy) for xy in zip(pollution_df['Longitude'], pollution_df['Latitude'])]
cities_gdf = gpd.GeoDataFrame(pollution_df, geometry=geometry, crs="EPSG:4326")

if india is not None:
    fig, ax = plt.subplots(figsize=(10, 12))
    india.plot(ax=ax, color='whitesmoke', edgecolor='gray')
    cities_gdf.plot(
        ax=ax,
        column='PM2.5',
        cmap='RdYlGn_r',
        markersize=200,
        legend=True,
        legend_kwds={'label': "PM2.5 Level", 'shrink': 0.6}
    )
    for x, y, label in zip(cities_gdf.geometry.x, cities_gdf.geometry.y, cities_gdf['City']):
        ax.text(x, y, label, fontsize=10, ha='right')
    plt.title('Air Pollution (PM2.5) in Major Indian Cities', fontsize=16)
    plt.axis('off')
    st.pyplot(fig)
    st.success("Map generated successfully!")
    # Save as image
    fig.savefig('pollution_map.png', bbox_inches='tight')
    st.download_button('Download Map as PNG', data=open('pollution_map.png', 'rb').read(), file_name='pollution_map.png', mime='image/png')
else:
    st.warning("Map cannot be displayed without the India shapefile.")


# --- Data Analysis Section ---
st.markdown("---")
st.header("Data Analysis & Insights")

# Show pollution data table
st.subheader("Pollution Data Table")
st.dataframe(pollution_df.style.background_gradient(cmap='RdYlGn_r', subset=['PM2.5']))

# Show summary statistics
st.subheader("Summary Statistics")
st.write(pollution_df[['PM2.5']].describe())

# Bar chart of PM2.5 by city
st.subheader("PM2.5 Levels by City")
st.bar_chart(pollution_df.set_index('City')['PM2.5'])

# Pie chart of pollution share
import plotly.express as px
st.subheader("Pollution Share by City (Pie Chart)")
fig_pie = px.pie(pollution_df, names='City', values='PM2.5', color='PM2.5', color_discrete_sequence=px.colors.qualitative.Plotly)
fig_pie.update_traces(textinfo='percent+label')
st.plotly_chart(fig_pie, use_container_width=True)

# --- Business Insight ---
st.markdown("---")
st.markdown("**Business Insight:** This map helps identify cities with critical air pollution levels, supporting targeted policy and health interventions.")

# --- Developer Credits and CSS Enhancements ---
st.markdown(
    "<div style='text-align:center; font-size:1.1rem; color:#555; margin-top:40px; border-top:1px solid #eaeaea; letter-spacing:1px;'>Developed by <b>UMESH, IIT PATNA</b></div>",
    unsafe_allow_html=True
)

# --- Library Installation Command ---

st.markdown(
    """
<div style='text-align:center; margin-top:20px;'>
<b>To install all required libraries, run:</b><br>
<code>pip install streamlit geopandas matplotlib pandas shapely pyproj fiona plotly</code>
</div>
""",
    unsafe_allow_html=True
)

# Command to run the streamlit app
st.code("streamlit run streamlit_pollution_map.py")
