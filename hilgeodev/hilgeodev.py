"""Main module."""
import ipyleaflet


class Map(ipyleaflet.Map):
    def __init__(self, center = (39,36), **kwargs):
        super().__init__(center=center, **kwargs)

    def add_base_map(self):
        self.add_layer(ipyleaflet.basemaps.OpenStreeMap.Mapnik)

    def add_geojson(self, url):
        import geopandas as gpd
        gdf = gpd.read_file(url)
        data = gdf.__geo_interface__ 
        gj = ipyleaflet.GeoJSON(data=data)
        bounds = gdf.total_bounds
        self.add_layer(gj)
        self.fit_bounds([[bounds[1],bounds[0]],[bounds[3],bounds[2]]])

