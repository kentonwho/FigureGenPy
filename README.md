# Kenpana

One package to rule them all,\
One package to sync them, \
One package to interface them all, \ 
And in the backend link them. 

## Functionality 
This library is intended to provide a single library for ADCIRC output visualization. Currently there are a sporadic array of visualization libraries for ADCIRC, including FigureGen, PullTimeSeries, Kalpana, and OceanMesh2D that are either written in Fortran (boo!) or operate on clunky data structures such as text input files. The library effectively provides an interface between ADCIRC 'objects' and Holoviews/Datashader. The library is built with Dask in mind for analysis and visualization on large datasets, such as ensemble runs. For runs that are not too large it's probably easier to learn how to use GIS softwares like QGIS. 

### Fundamental Feature Wish List 

* Static/temporal plotting of global water elevations
* Static/temporal plotting of global water velocity 
* User-defined mathematical operations on sim data 
* Contouring & Exporting to shapefile
* Hydrographical plotting from global water elevations 
* Deep integration with Holoviews and Datashader 
* Panel integration for dashboard and web app development

#### Down-the-road Features

* Submeshing through inheritance from NetworkX graph objects, for subplotting
* Mesh-wise operations, such as mesh union, intersection, subtraction, addition.  
* Lagrangian particle tracking 
* Hydrographical cross-sections 
* Interactions with 3D plotting libraries 

## User interface 
The first purpose of this library is to finally have an abstract representation of ADCIRC outputs. Thus all classes are exposed to the user. Reading and writing to NetCDF, text, or pkl files will all be supported. 

Though knowledge of of holoviews, datashader, xarray, netcdf makes usage of this library easier, ultimately the only thing the user needs to know: 

1. Call read methods to access data, construct abstract objects (global elevation, bathymetry, etc.) 
2. Define and perform operations between the abstract objects (like computing flux)
3. Define a "slice" object: one of the following: 
    - Scalar with time slider 
    - Single point with time axis 
    - Cross-section with time slider 
    - Lagrangian with time-space slider 
    - Vector field with time slider
    - Oriented flux with time axis 
4. Call slice of scalar/vector/time_series. Slice composes Scalar/Vector/Time_series
5. All methods return proper Holoviews objects, it is up to the user to piece these together. Use Panel to construct dashboards. 

All ADCIRC types are types of X Data. Slices are Holoviews objects which are constructed from (compose) X Data types. 


## Structure
The primary data structure of ADCIRC is a Mesh. This is implemented as a type of matplotlib.tri. For now this is a wrapper class for the matplotlib.tri class but may expand in the future if mesh operations (submeshing, mesh concatenation) is needed. 

From this, there is three types: 
1. Scalar Mesh Data. This is a wrapped LinearTriInterpolator 
2. Vector Mesh Data 
3. Time series data 

A global water elevation is a 'scalar mesh data' child of matplotlib.tri. A bathymetry is a scalar mesh datum. A domain is therefore a (mesh, bathymetry) LinearTriInterpolator. Thus the global water elevation is abstractly represented in the mesh as well as the linear function space. The objects should support mathematical operation between each other. 
