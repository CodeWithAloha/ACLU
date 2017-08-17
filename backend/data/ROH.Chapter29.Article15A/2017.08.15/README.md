## Description
GIS data of the boundaries specified in the [Revised Ordinances of Honolulu, Chapter 29, Article 15A, Exhibits 1 through 17](https://www.honolulu.gov/cms-ocs-menu/site-ocs-sitearticles/21317-roh-chapter-29.html)

Colloquially known as the ['sit-lie ordinance'](https://en.wikipedia.org/wiki/Sit-lie_ordinance#Honolulu), the law prohibits sitting or lying on the ground in certain geographic zones.

## Source
The data was received August 15th, 2017 via an email from Lori M Hiraoka, Staff Attorney, City and Count of Honolulu Office of Council Services.

## More Information
Refer to this GitHub issue: https://github.com/codeforhawaii/aclu/issues/3

## GeoJSON
The orignal ESRI Shapefiles were converted to WGS84 coordinate system GeoJSON format with the following commands:
```
ogr2ogr -f GeoJSON -t_srs crs:84 segments.geojson segments.shp
ogr2ogr -f GeoJSON -t_srs crs:84 zones.geojson zones.shp
```
