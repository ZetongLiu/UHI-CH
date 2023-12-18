from shapely.geometry import MultiPolygon
import geopandas as gpd

# Example GeoDataFrame with geometries
# Replace this with your actual GeoDataFrame
# MO_all = ...
gpkg_filepath = r"D:\Document\SemesterProject\New_case\VD\study_area\morges.gpkg"  
MO_all = gpd.read_file(gpkg_filepath, layer = "zone_tout")
# print(MO_all.geometry.head(5))
# Buffering with a distance of 2
buffered_geometries = MO_all.geometry.buffer(4)
# print(buffered_geometries.head(5))
# Getting the convex hull of the buffered geometries
convex_hull = buffered_geometries.unary_union.convex_hull
# conhull = MultiPolygon(buffered_geometries).convex_hull
print(convex_hull)
# You can also create a GeoDataFrame with the convex hull geometry
convex_hull_gdf = gpd.GeoDataFrame(geometry=[convex_hull])

# Print the convex hull bounding box
print("Convex Hull Bounding Box:", convex_hull.bounds)

# Plotting the convex hull and the original geometries for visualization
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
MO_all.plot(ax=ax, alpha=0.5, edgecolor='k', label='Original Geometries')
convex_hull_gdf.plot(ax=ax, color='red', alpha=0.5, edgecolor='k', label='Convex Hull')
plt.legend()
plt.show()
