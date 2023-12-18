import matplotlib.pyplot as plt
import pandas as pd
from shapely import box
from shapely.geometry import Point
import geopandas as gpd

XYZfile=r"D:\Document\SemesterProject\New_case\ZG\ground2\SWISSALTI3D_2_XYZ_CHLV95_LN02_2677_1219.xyz" 
gpkg_filepath=r"D:\Document\SemesterProject\New_case\case1.gpkg"  

MO_all = gpd.read_file(gpkg_filepath, layer = "zone_tout")
zone_bounds = MO_all.geometry.buffer(10).values.total_bounds
zone_box = box(zone_bounds[0], zone_bounds[1], zone_bounds[2], zone_bounds[3])

ground_df = pd.read_table(XYZfile, skiprows=1, delim_whitespace=True, names=['X', 'Y', 'Z'])
ground_df['geometry'] = ground_df.apply(lambda row: Point(row['X'], row['Y'], row['Z']), axis=1)
ground_data = gpd.GeoDataFrame(ground_df, geometry='geometry')

ground_within_zone = ground_data[ground_data.geometry.within(zone_box)]

print(ground_within_zone)
print(ground_df.info())

# Create an empty DataFrame
import pandas as pd

# Create an empty DataFrame
df = pd.DataFrame(columns=['Column1', 'Column2'])
# Add rows in iterations
data_to_append = []
for i in range(3):
    data_to_append.append({'Column1': i, 'Column2': i * 2})

df = pd.concat([df, pd.DataFrame(data_to_append)], ignore_index=True)
print(df)



