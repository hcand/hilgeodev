"""Main module."""
import ipyleaflet

class Map(ipyleaflet.Map):
    def __init__(self, center = (39,36), **kwargs):
        super().__init__(center=center, **kwargs)

    def add_base_map(self):
        return self.add_layer(ipyleaflet.basemaps.OpenStreeMap.Mapnik)