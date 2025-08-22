# Pollution Map of Indian Cities

This project visualizes air pollution (PM2.5) levels across major Indian cities on a map using Streamlit and geospatial data.

## Features
- Interactive map of India with cities colored by PM2.5 pollution levels
- Data table, summary statistics, bar chart, and pie chart for pollution data
- Downloadable map as PNG
- Modern UI with developer credits

## How to Run
1. **Install dependencies:**
   ```
   pip install streamlit geopandas matplotlib pandas shapely pyproj fiona plotly
   ```
2. **Add shapefile:**
   - Place `india_st.shp`, `india_st.shx`, and `india_st.dbf` in the project directory.
3. **Run the app:**
   ```
   python -m streamlit run streamlit_pollution_map.py
   ```
4. **Open in browser:**
   - Go to [http://localhost:8501](http://localhost:8501)

## Sample Data
| City    | PM2.5 | Latitude | Longitude |
|---------|-------|----------|-----------|
| Delhi   | 310   | 28.61    | 77.20     |
| Chennai | 45    | 13.08    | 80.27     |
| Mumbai  | 98    | 19.07    | 72.87     |
| Kolkata | 112   | 22.57    | 88.36     |

## Developer
Developed by **UMESH, IIT PATNA**

## Notes
- Make sure all shapefile components (`.shp`, `.shx`, `.dbf`) are present in the directory.
- For more cities, update the data in `streamlit_pollution_map.py`.
