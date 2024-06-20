# FigureGenPy

## Functionality 
This library is intended to provide a single library for ADCIRC output visualization. Currently there are a sporadic array of visualization libraries for ADCIRC, including FigureGen, PullTimeSeries, and Kalpana that are either written in Fortran (boo!) or operate on clunky data structures such as text input files. The library effectively provides an interface between ADCIRC 'objects' and Holoviews/Datashader. The library is built with Dask in mind for analysis and visualization on large datasets, such as ensemble runs. For runs that are not too large it's probably easier to learn how to use GIS softwares like QGIS. 

### Feature Wish List 

* Static/temporal plotting of global water elevations
* Static/temporal plotting of global water velocity 
* Basic mathematical operations between sim data
* Contouring & Exporting to shapefile
* Hydrographical plotting 

