import pandas as pd
from xml.etree.ElementTree import Element, SubElement, tostring, parse, ElementTree
from xml.dom import minidom

def add_ground_from_XYZ(district, terrain_df, groundtype=37, detailedSimulation=False, ShortWaveReflectance=0.3):
    groundsurface = SubElement(district, "GroundSurface")
    tri_id=0
    # 500= different x,y values, TODO: read them from XYZ file
    row_diff=[[0, 500, 501], [0, 501, 1]] 
    max_x=terrain_df['X'].max()
    min_y=terrain_df['Y'].min()
    for r in terrain_df.index:
        if terrain_df.loc[r,'X'] < max_x and terrain_df.loc[r,'Y'] > min_y:
            for _ in range(2):
                dict_surface = {"id": str(tri_id),
                                "ShortWaveReflectance":str(ShortWaveReflectance),
                                "type":str(groundtype),
                                "detailedSimulation":str(detailedSimulation).lower()}
                surface = SubElement(groundsurface, "Ground", dict_surface)
            # Add points
                for p in range(3):
                    point_name = "V{}".format(p)
                    coordinates = terrain_df.loc[r+row_diff[tri_id%2][p]]
                    x = str(coordinates['X'])
                    y = str(coordinates['Y'])
                    z = str(coordinates['Z'])
                    dict_point = {"x": x, "y": y, "z": z}
                    point = SubElement(surface, point_name, dict_point)
                tri_id+=1

XYZfile = r"D:\Document\SemesterProject\New_case\ZG\swissalti3d_2022_2677-1219_2_2056_5728.xyz\SWISSALTI3D_2_XYZ_CHLV95_LN02_2677_1219.xyz"
terrain_df = pd.read_table(XYZfile, skiprows=1, delim_whitespace=True, names=['X', 'Y', 'Z'])
n=int((len(terrain_df))**0.5)
print(n)

district=Element('District')
add_ground_from_XYZ(district, XYZfile)
#tree = ElementTree(district)
#tree.write("output.xml")

#xmlstr = minidom.parseString(tostring(district)).toprettyxml(indent="  ")

#with open("output.xml", "w") as f:
#    f.write(xmlstr)
