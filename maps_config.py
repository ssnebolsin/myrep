


def get_arcs_config(val):
    config_arcs = {
        "version": "v1",
        "config": {
            "visState": {
                "filters": [
                    {
                        "dataId": [
                            "geodt"
                        ],
                        "id": "6vnl7elu7",
                        "name": [
                            "hour_dt"
                        ],
                        "type": "timeRange",
                        "value": [
                            1612204152000,
                            1612208461000
                        ],
                        "enlarged": True,
                        "plotType": "histogram",
                        "animationWindow": "free",
                        "yAxis": None
                    },
                    {
                        "dataId": [
                            "geodt"
                        ],
                        "id": "r7lvo3lrr",
                        "name": [
                            "city_cval"
                        ],
                        "type": "multiSelect",
                        "value": val,
                        "enlarged": False,
                        "plotType": "histogram",
                        "animationWindow": "free",
                        "yAxis": None
                    }
                ],
                "layers": [
                    {
                        "id": "7qmaifs",
                        "type": "arc",
                        "config": {
                            "dataId": "geodt",
                            "label": "new layer",
                            "color": [
                                26,
                                49,
                                119
                            ],
                            "columns": {
                                "lat0": "lat_src",
                                "lng0": "lon_src",
                                "lat1": "lat_dest",
                                "lng1": "lon_dest"
                            },
                            "isVisible": True,
                            "visConfig": {
                                "opacity": 0.8,
                                "thickness": 2,
                                "colorRange": {
                                    "name": "Global Warming",
                                    "type": "sequential",
                                    "category": "Uber",
                                    "colors": [
                                        "#5A1846",
                                        "#900C3F",
                                        "#C70039",
                                        "#E3611C",
                                        "#F1920E",
                                        "#FFC300"
                                    ]
                                },
                                "sizeRange": [
                                    0,
                                    10
                                ],
                                "targetColor": [
                                    228,
                                    182,
                                    0
                                ]
                            },
                            "hidden": False,
                            "textLabel": [
                                {
                                    "field": None,
                                    "color": [
                                        255,
                                        255,
                                        255
                                    ],
                                    "size": 18,
                                    "offset": [
                                        0,
                                        0
                                    ],
                                    "anchor": "start",
                                    "alignment": "center"
                                }
                            ]
                        },
                        "visualChannels": {
                            "colorField": None,
                            "colorScale": "quantile",
                            "sizeField": {
                                "name": "cnt",
                                "type": "integer"
                            },
                            "sizeScale": "linear"
                        }
                    },
                    {
                        "id": "p9wueo",
                        "type": "point",
                        "config": {
                            "dataId": "geodt",
                            "label": "new layer",
                            "color": [
                                200,
                                137,
                                0
                            ],
                            "columns": {
                                "lat": "lat_src",
                                "lng": "lon_src",
                                "altitude": None
                            },
                            "isVisible": True,
                            "visConfig": {
                                "radius": 10,
                                "fixedRadius": False,
                                "opacity": 0.8,
                                "outline": False,
                                "thickness": 2,
                                "strokeColor": None,
                                "colorRange": {
                                    "name": "Global Warming",
                                    "type": "sequential",
                                    "category": "Uber",
                                    "colors": [
                                        "#5A1846",
                                        "#900C3F",
                                        "#C70039",
                                        "#E3611C",
                                        "#F1920E",
                                        "#FFC300"
                                    ]
                                },
                                "strokeColorRange": {
                                    "name": "Global Warming",
                                    "type": "sequential",
                                    "category": "Uber",
                                    "colors": [
                                        "#5A1846",
                                        "#900C3F",
                                        "#C70039",
                                        "#E3611C",
                                        "#F1920E",
                                        "#FFC300"
                                    ]
                                },
                                "radiusRange": [
                                    0,
                                    50
                                ],
                                "filled": True
                            },
                            "hidden": False,
                            "textLabel": [
                                {
                                    "field": None,
                                    "color": [
                                        255,
                                        255,
                                        255
                                    ],
                                    "size": 18,
                                    "offset": [
                                        0,
                                        0
                                    ],
                                    "anchor": "start",
                                    "alignment": "center"
                                }
                            ]
                        },
                        "visualChannels": {
                            "colorField": None,
                            "colorScale": "quantile",
                            "strokeColorField": None,
                            "strokeColorScale": "quantile",
                            "sizeField": {
                                "name": "cnt",
                                "type": "integer"
                            },
                            "sizeScale": "sqrt"
                        }
                    },
                    {
                        "id": "nprpqxy",
                        "type": "point",
                        "config": {
                            "dataId": "geodt",
                            "label": "new layer",
                            "color": [
                                30,
                                55,
                                136
                            ],
                            "columns": {
                                "lat": "lat_dest",
                                "lng": "lon_dest",
                                "altitude": None
                            },
                            "isVisible": True,
                            "visConfig": {
                                "radius": 10,
                                "fixedRadius": False,
                                "opacity": 0.8,
                                "outline": False,
                                "thickness": 2,
                                "strokeColor": None,
                                "colorRange": {
                                    "name": "Global Warming",
                                    "type": "sequential",
                                    "category": "Uber",
                                    "colors": [
                                        "#5A1846",
                                        "#900C3F",
                                        "#C70039",
                                        "#E3611C",
                                        "#F1920E",
                                        "#FFC300"
                                    ]
                                },
                                "strokeColorRange": {
                                    "name": "Global Warming",
                                    "type": "sequential",
                                    "category": "Uber",
                                    "colors": [
                                        "#5A1846",
                                        "#900C3F",
                                        "#C70039",
                                        "#E3611C",
                                        "#F1920E",
                                        "#FFC300"
                                    ]
                                },
                                "radiusRange": [
                                    0,
                                    50
                                ],
                                "filled": True
                            },
                            "hidden": False,
                            "textLabel": [
                                {
                                    "field": None,
                                    "color": [
                                        255,
                                        255,
                                        255
                                    ],
                                    "size": 18,
                                    "offset": [
                                        0,
                                        0
                                    ],
                                    "anchor": "start",
                                    "alignment": "center"
                                }
                            ]
                        },
                        "visualChannels": {
                            "colorField": None,
                            "colorScale": "quantile",
                            "strokeColorField": None,
                            "strokeColorScale": "quantile",
                            "sizeField": None,
                            "sizeScale": "linear"
                        }
                    }
                ],
                "interactionConfig": {
                    "tooltip": {
                        "fieldsToShow": {
                            "geodt": [
                                {
                                    "name": "cnt",
                                    "format": None
                                },
                                {
                                    "name": "hour_dt",
                                    "format": None
                                },
                                {
                                    "name": "city_cval",
                                    "format": None
                                }
                            ]
                        },
                        "compareMode": False,
                        "compareType": "absolute",
                        "enabled": True
                    },
                    "brush": {
                        "size": 0.5,
                        "enabled": False
                    },
                    "geocoder": {
                        "enabled": False
                    },
                    "coordinate": {
                        "enabled": False
                    }
                },
                "layerBlending": "normal",
                "splitMaps": [],
                "animationConfig": {
                    "currentTime": None,
                    "speed": 1
                }
            },
            "mapState": {
                "bearing": -48.375,
                "dragRotate": True,
                "latitude": 49.08259786220523,
                "longitude": 24.83177147095164,
                "pitch": 38.72451378776508,
                "zoom": 9.548058916916952,
                "isSplit": False
            },
            "mapStyle": {
                "styleType": "gb4b2o5",
                "topLayerGroups": {
                    "label": True,
                    "road": False,
                    "border": False
                },
                "visibleLayerGroups": {
                    "label": True,
                    "road": True,
                    "building": True,
                    "water": True,
                    "land": True,
                    "border": True
                },
                "threeDBuildingColor": [
                    194.6103322548211,
                    191.81688250953655,
                    185.2988331038727
                ],
                "mapStyles": {
                    "gb4b2o5": {
                        "accessToken": "",
                        "custom": True,
                        "icon": "https://api.mapbox.com/styles/v1/ssnebolsin/ckniqa9nf073817lshgbuay2z/static/-122.3391,37.7922,9,0,0/400x300?access_token=pk.eyJ1IjoidWJlcmRhdGEiLCJhIjoiY2pza3FrOXh6MW05dTQzcWd1M3I3c2E0eCJ9.z0MFFrHYNbdK-QVHKrdepw&logo=false&attribution=false",
                        "id": "gb4b2o5",
                        "label": "Navigation_ss",
                        "url": "mapbox://styles/ssnebolsin/ckniqa9nf073817lshgbuay2z"
                    }
                }
            }
        }
    }
    return config_arcs


def get_routes_config(val):
    config_routes = {
            "version": "v1",
            "config": {
                "visState": {
                    "filters": [
                        {
                            "dataId": [
                                "geodt"
                            ],
                            "id": "a69endll1c",
                            "name": [
                                "event_dt"
                            ],
                            "type": "timeRange",
                            "value": [
                                1603270806816,
                                1603274802816
                            ],
                            "enlarged": True,
                            "plotType": "histogram",
                            "animationWindow": "free",
                            "yAxis": None
                        },
                        {
                            "dataId": [
                                "geodt"
                            ],
                            "id": "45lsgixhr",
                            "name": [
                                "city_name_ua"
                            ],
                            "type": "multiSelect",
                            "value": val,
                            "enlarged": False,
                            "plotType": "histogram",
                            "animationWindow": "free",
                            "yAxis": None
                        }
                    ],
                    "layers": [
                        {
                            "id": "94xnqv",
                            "type": "geojson",
                            "config": {
                                "dataId": "geodt",
                                "label": "geodt",
                                "color": [
                                    18,
                                    147,
                                    154
                                ],
                                "columns": {
                                    "geojson": "geometry"
                                },
                                "isVisible": True,
                                "visConfig": {
                                    "opacity": 0.8,
                                    "strokeOpacity": 0.8,
                                    "thickness": 0.5,
                                    "strokeColor": None,
                                    "colorRange": {
                                        "name": "Global Warming",
                                        "type": "sequential",
                                        "category": "Uber",
                                        "colors": [
                                            "#5A1846",
                                            "#900C3F",
                                            "#C70039",
                                            "#E3611C",
                                            "#F1920E",
                                            "#FFC300"
                                        ]
                                    },
                                    "strokeColorRange": {
                                        "name": "Global Warming",
                                        "type": "sequential",
                                        "category": "Uber",
                                        "colors": [
                                            "#5A1846",
                                            "#900C3F",
                                            "#C70039",
                                            "#E3611C",
                                            "#F1920E",
                                            "#FFC300"
                                        ]
                                    },
                                    "radius": 10,
                                    "sizeRange": [
                                        0,
                                        10
                                    ],
                                    "radiusRange": [
                                        0,
                                        50
                                    ],
                                    "heightRange": [
                                        0,
                                        500
                                    ],
                                    "elevationScale": 5,
                                    "stroked": True,
                                    "filled": False,
                                    "enable3d": False,
                                    "wireframe": False
                                },
                                "hidden": False,
                                "textLabel": [
                                    {
                                        "field": None,
                                        "color": [
                                            255,
                                            255,
                                            255
                                        ],
                                        "size": 18,
                                        "offset": [
                                            0,
                                            0
                                        ],
                                        "anchor": "start",
                                        "alignment": "center"
                                    }
                                ]
                            },
                            "visualChannels": {
                                "colorField": None,
                                "colorScale": "quantile",
                                "sizeField": None,
                                "sizeScale": "linear",
                                "strokeColorField": {
                                    "name": "cnt",
                                    "type": "integer"
                                },
                                "strokeColorScale": "quantile",
                                "heightField": None,
                                "heightScale": "linear",
                                "radiusField": None,
                                "radiusScale": "linear"
                            }
                        }
                    ],
                    "interactionConfig": {
                        "tooltip": {
                            "fieldsToShow": {
                                "geodt": [
                                    {
                                        "name": "cnt",
                                        "format": None
                                    },
                                    {
                                        "name": "city_name_ua",
                                        "format": None
                                    },
                                    {
                                        "name": "event_dt",
                                        "format": None
                                    }
                                ]
                            },
                            "compareMode": False,
                            "compareType": "absolute",
                            "enabled": True
                        },
                        "brush": {
                            "size": 0.5,
                            "enabled": False
                        },
                        "geocoder": {
                            "enabled": False
                        },
                        "coordinate": {
                            "enabled": False
                        }
                    },
                    "layerBlending": "normal",
                    "splitMaps": [],
                    "animationConfig": {
                        "currentTime": None,
                        "speed": 1
                    }
                },
                "mapState": {
                    "bearing": 0,
                    "dragRotate": False,
                    "latitude": 48.88522892929126,
                    "longitude": 24.75402328740509,
                    "pitch": 0,
                    "zoom": 9.548058916916952,
                    "isSplit": False
                },
                "mapStyle": {
                    "styleType": "o8qp71",
                    "topLayerGroups": {},
                    "visibleLayerGroups": {
                        "label": True,
                        "road": True,
                        "building": True,
                        "water": True,
                        "land": True
                    },
                    "threeDBuildingColor": [
                        194.6103322548211,
                        191.81688250953655,
                        185.2988331038727
                    ],
                    "mapStyles": {
                        "o8qp71": {
                            "accessToken": "pk.eyJ1Ijoic3NuZWJvbHNpbiIsImEiOiJja25pcDI0Z3MyMml0Mm5vYWs2Y3dvbXRyIn0.s-OPJyHjzC7Ub24AvhSvEA",
                            "custom": True,
                            "icon": "https://api.mapbox.com/styles/v1/ssnebolsin/ckniqa9nf073817lshgbuay2z/static/-122.3391,37.7922,9,0,0/400x300?access_token=pk.eyJ1Ijoic3NuZWJvbHNpbiIsImEiOiJja25pcDI0Z3MyMml0Mm5vYWs2Y3dvbXRyIn0.s-OPJyHjzC7Ub24AvhSvEA&logo=false&attribution=false",
                            "id": "o8qp71",
                            "label": "Navigation_ss",
                            "url": "mapbox://styles/ssnebolsin/ckniqa9nf073817lshgbuay2z"
                        }
                    }
                }
            }
        }
    return config_routes
