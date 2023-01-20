import argparse
import geopandas as gpd
from pathlib import Path

#get input file as argparse
parser = argparse.ArgumentParser()
parser.add_argument("input", help="Input file")
args = parser.parse_args()

#read input filename, ignoring extension
filename = Path(args.input)
filename_wo_ext = filename.with_suffix('')
filename_wo_ext = str(filename_wo_ext)

#prompt user for buffer distance
buffer_distance = input("Buffer distance: ")
buffer_units = input("Buffer units ('m', 'us_sf', 'intl_feet'): ")

#read input file
gdf = gpd.read_file(args.input)

if buffer_units == "m":
    gdf['geometry'] = gdf['geometry'].buffer(float(buffer_distance))
elif buffer_units == "us_sf":
    gdf['geometry'] = gdf['geometry'].buffer(float(buffer_distance) * 0.304800609601)
elif buffer_units == "intl_feet":
    gdf['geometry'] = gdf['geometry'].buffer(float(buffer_distance) * 0.3048)

#ask user if they want to save output to a certain location
save_to = input("Save to (leave blank for default location): ")
if save_to == "":
    gdf.to_file(filename_wo_ext + "_" + buffer_distance + buffer_units + "_buffer.shp", driver="ESRI Shapefile")
else:
    gdf.to_file(save_to)
