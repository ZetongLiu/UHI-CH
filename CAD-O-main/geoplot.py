import geopandas as gpd
import matplotlib.pyplot as plt

# Assuming you have two GeoDataFrames: gdf1 and gdf2

# Example GeoDataFrames (replace these with your actual GeoDataFrames)
# gdf1 = gpd.read_file('data1.shp')
# gdf2 = gpd.read_file('data2.shp')
fp4=r"D:\Document\SemesterProject\New_case\case1.gpkg"

gdf1 = gpd.read_file(fp4, layer = 'green')
gdf2 =gpd.read_file(fp4, layer = 'streets')
# Plot the geometries from the first GeoDataFrame
fig, ax = plt.subplots()
gdf1.plot(ax=ax, color='blue', label='GeoDataFrame 1')

# Plot the geometries from the second GeoDataFrame on the same plot
gdf2.plot(ax=ax, color='red', label='GeoDataFrame 2')

# Set labels and title
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.set_title('Two GeoDataFrames in One Plot')
ax.legend()
fig.savefig(r'D:\Document\SemesterProject\New_case\VD\plot1.png')
# Show the plot
plt.show()
