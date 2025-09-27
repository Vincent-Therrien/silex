Wildfire Modelling Tool Data
============================

This directory comprises files that illustrate fire propagation data. They are
not sufficient to run complete simulations; refer to **forecast.ipynb** for
explanations on how to obtain all required data.

Files:

- `canopy_height_lookup_table.csv`: Assign canopy raw values to real
  measurements.
- `canopy_height.tif`: GeoTIFF file describing canopy height.
- `dot.shp`: Shape file describing an ignition point.
- `elevation,.tif`: GeoTIFF file describing ground elevation.
- `weather.wsx`: Example of a weather file to use with FARSITE.
