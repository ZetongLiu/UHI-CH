from dbfread import DBF
import pandas as pd
import geopandas as gpd
import matplotlib
from shapely.geometry import LineString
import matplotlib.pyplot as plt

# fp1=r"D:\Document\SemesterProject\New_case\ZG\Asphalt&Green\swisstlmregio_2023_2056.shp\swisstlmregio_product_lv95\Landcover\swissTLMRegio_LandCover.dbf"
# fp2=r"D:\Document\SemesterProject\New_case\ZG\Asphalt&Green\swisstlmregio_2023_2056.shp\swisstlmregio_product_lv95\Landcover\swissTLMRegio_LandCover.shp"
# dbf = DBF(filepath, encoding='utf-8')
# df = pd.DataFrame(iter(dbf))
# unique_values = df['NLN1'].unique()
# print(unique_values)
# print(df.columns)

# fp3 =r"D:\Document\SemesterProject\New_case\ZG\Asphalt&Green\SWISSTLM3D_2023_LV95_LN02.gpkg"
# fp4=r"D:\Document\SemesterProject\New_case\case1.gpkg"
# df=gpd.read_file(r"D:\Document\SemesterProject\New_case\VD\study_area\morges.gpkg", layer='streets')
# unique_values = df['objektart'].unique()
# print(unique_values)
gpkg_filepath = r"D:\Document\SemesterProject\New_case\VD\study_area\morges.gpkg"    
ori_street_data = gpd.read_file(gpkg_filepath, layer = 'streets')
street_data = ori_street_data[ori_street_data['objektart'] != 'Verbindung']
geometry_list = []
road_width={'Autobahn': 7, # E41 typical width of lanes is 3.5m, two lanes=7m
            '10m Strasse': 10,
            '8m Strasse': 8,
            '6m Strasse': 6,
            '3m Strasse': 3,
            '2m Weg': 2,
            '4m Strasse': 4,
            '1m Weg': 1
            }
road_index_list=[]
green_index_list=[]
for index, row in street_data.iterrows():
    line = row['geometry']
    road_type=row['objektart'] 
    buffered_line = line.buffer(road_width[road_type]/2, cap_style='flat')
    geometry_list.append(buffered_line)
buffered_streets = gpd.GeoDataFrame(geometry=geometry_list, crs='EPSG:2056')
buffered_streets.to_file(gpkg_filepath, layer='buffered_streets', driver='GPKG')
# green_data = gpd.read_file(fp4, layer = 'green')
# street_data=gpd.read_file(fp4, layer = 'streets')
# print(street_data.geometry.head(1)) 
# print(green_data.geometry.head(1)) 
# street_data.geometry.plot()
# plt.show()
# for index, row in street_data.iterrows():
#         line = row['geometry']
#         road_type=row['objektart'] 
#         print(line)
#         print(road_type)

# print(green_data.geometry.index)
# print(green_data.geometry)
# green_data.geometry.plot()
# plt.show()

# street_data.geometry.plot()
# plt.show()
# # print(green_data.geometry.tail(1))
# # print(street_data.geometry.tail(1)) 
# # print(green_data.info())
# # print(street_data.info())
# unique_values = street_data['objektart'].unique()
# print(unique_values)
# print(data.tail(5)) 
# print(data.info()) 
# print(data.columns)
# filtered_data=data[data['name']=='Zug']
# print(filtered_data['geometry'])

# unique_values = data['herkunft'].unique()
# print(unique_values)
# print(data)
# print(data.columns)

#A: XYZ -> assign type
#B: 1,same type store as geometry object linearring -> intersect with bounds of zone_tout and use attributes to assign type (better
  # 2, run main code to generate case1_result.xml
   # 3, copy green and road type to .xml file 
   # 4, change the type of all ground from asphalt to soil

# def ground_(district, terrain_df, center_coordinates=(0,0), groundtype=100, kFactor=1, detailedSimulation=False, ShortWaveReflectance=0.3):  
#     x_center = center_coordinates[0]
#     y_center = center_coordinates[1]
#     groundsurface = SubElement(district, "GroundSurface")
#     tri_id=0 
#     n=int((len(terrain_df))**0.5)
#     row_diff=[[0, n, n+1], [0, n+1, 1]] 
#     max_x=terrain_df['X'].max()
#     min_y=terrain_df['Y'].min()
#     df = pd.DataFrame(columns=['Triangle'])
#     data_to_append = []
#     for r in terrain_df.index:
#         if terrain_df.loc[r,'X'] < max_x and terrain_df.loc[r,'Y'] > min_y:
#             for _ in range(2):
#                 dict_surface = {"id": str(tri_id),
#                                 "ShortWaveReflectance":str(ShortWaveReflectance),
#                                 "type":str(groundtype),
#                                 "kFactor": str(kFactor),
#                                 "detailedSimulation":str(detailedSimulation).lower()}
#                 surface = SubElement(groundsurface, "Ground", dict_surface)
#             # Add points
#                 x=[0]*3
#                 y=[0]*3
#                 z=[0]*3
#                 for p in range(3):
#                     point_name = "V{}".format(p)
#                     coordinates = terrain_df.loc[r+row_diff[tri_id%2][p]]
#                     x[p] = str(coordinates['X']-x_center)
#                     y[p] = str(coordinates['Y']-y_center)
#                     z[p] = str(coordinates['Z'])
#                     dict_point = {"x": x, "y": y, "z": z}
#                     point = SubElement(surface, point_name, dict_point)
#                 coords = ((x[0],y[0],z[0]),(x[1],y[1],z[1]),(x[2],y[2],z[2]))
#                 data_to_append.append({'Triangle': Polygon(coords)})
#                 # polygon = orient(polygon, sign=1.0)
#                 tri_id+=1
#     df = pd.concat([df, pd.DataFrame(data_to_append)], ignore_index=True)
#     return df

# ground_data=ground_()

# def modify_type(ground_gdf, green_data, street_data):
#     road_width={'Autobah': 7, # E41 typical width of lanes is 3.5m, two lanes=7m
#                 '6m Strasse': 6,
#                 '3m Strasse': 3,
#                 '2m Weg': 2,
#                 '4m Strasse': 4,
#                 '1m Weg': 1
#                 }
#     road_index_list=[]
#     for row in street_data.iterrows():
#         line = row['geometry']
#         road_type=row['objektart'] 
#         buffered_line = line.buffer(road_width[road_type]/2, cap_style='flat')
#         road_ground = ground_data[ground_data.geometry.intersects(buffered_line)]
#         road_indices = road_ground.index
#         road_index_list += road_indices.tolist()

#     green_ground = ground_data[ground_data.geometry.intersects(green_data.geometry)]
#     green_indices = green_ground.index
#     green_index_list=green_indices.tolist()

#     tree = ET.ElementTree(ET.fromstring(your_xml_string))  # or ET.parse('your_xml_file.xml')
#     green_groundtype=3
#     road_groundtype=2
#     for surface in tree.findall('.//GroundSurface/Ground'):
#         current_id = surface.get('id')
#         if int(current_id) in green_index_list:
#             surface.set('type', str(green_groundtype))
#         elif int(current_id) in green_index_list:
#             surface.set('type', str(green_groundtype))


    