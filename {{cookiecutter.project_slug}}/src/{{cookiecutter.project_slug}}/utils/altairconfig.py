import json
from typing import Literal

try:
    import altair as alt  # ty: ignore
except ImportError as e:
    raise ImportError("Altair is not installed") from e


class AltairConfig:
    @staticmethod
    def setup(
        where: Literal["browser", "html", "jupyter"] = "browser",
        name: str = "my_theme",
        enable: bool = True,
        dark_color: str = "gray",
        font_weight: str = "normal",
        small_font_size: int = 12,
        medium_font_size: int = 14,
        large_font_size: int = 18,
        height: int = 500,
        width: int = 500,
        spacing_facet: int = 60,
        spacing_concat: int = 60,
    ):
        """Setup Altair."""
        AltairConfig.disable_max_rows()
        AltairConfig.renderers_enable(where=where)
        AltairConfig.register_theme(
            name=name,
            enable=enable,
            dark_color=dark_color,
            font_weight=font_weight,
            small_font_size=small_font_size,
            medium_font_size=medium_font_size,
            large_font_size=large_font_size,
            height=height,
            width=width,
            spacing_facet=spacing_facet,
            spacing_concat=spacing_concat,
        )

    @staticmethod
    def disable_max_rows():
        """Disables the max rows limit for Altair."""
        alt.data_transformers.disable_max_rows()

    @staticmethod
    def renderers_enable(where: Literal["browser", "html", "jupyter"]):
        """Enables Altair renderers."""
        alt.renderers.enable(where)

    @staticmethod
    def register_theme(
        name: str,
        enable: bool,
        dark_color: str,
        font_weight: str,
        small_font_size: int,
        medium_font_size: int,
        large_font_size: int,
        height: int,
        width: int,
        spacing_facet: int,
        spacing_concat: int,
    ):
        """Registers my custom Altair theme."""

        @alt.theme.register(name, enable=enable)
        def loader():
            return json.loads(
                json.dumps(
                    {
                        "config": {
                            "text": {
                                "color": dark_color,
                                "fontSize": small_font_size,
                            },
                            "title": {
                                "anchor": "middle",
                                "fontWeight": font_weight,
                                "titleFontWeight": font_weight,
                                "labelFontWeight": font_weight,
                                "titleFontSize": medium_font_size,
                                "labelFontSize": small_font_size,
                                "color": dark_color,
                                "titleColor": dark_color,
                                "labelColor": dark_color,
                                "tickColor": dark_color,
                                "domainColor": dark_color,
                            },
                            "header": {
                                "titleFontSize": large_font_size,
                                "labelFontSize": medium_font_size,
                                "color": dark_color,
                                "titleColor": dark_color,
                                "labelColor": dark_color,
                                "fontWeight": font_weight,
                                "titleFontWeight": font_weight,
                                "labelFontWeight": font_weight,
                            },
                            "view": {
                                "height": height,
                                "width": width,
                                "strokeWidth": 0,
                                "fill": "white",
                            },
                            "facet": {
                                "spacing": spacing_facet,
                            },
                            "concat": {
                                "spacing": spacing_concat,
                            },
                            "axis": {
                                "domain": True,
                                "domainColor": dark_color,
                                "domainWidth": 1,
                                "gridWidth": 1,
                                "labelAngle": 0,
                                "tickSize": 5,
                                "gridCap": "round",
                                "gridDash": [2, 4],
                                "fontWeight": font_weight,
                                "titleFontWeight": font_weight,
                                "labelFontWeight": font_weight,
                                "titleFontSize": medium_font_size,
                                "labelFontSize": small_font_size,
                                "color": dark_color,
                                "titleColor": dark_color,
                                "labelColor": dark_color,
                                "tickColor": dark_color,
                            },
                            "axisX": {
                                "titleAnchor": "end",
                                "titleAlign": "center",
                            },
                            "axisY": {
                                "titleAnchor": "end",
                                "titleAngle": 0,
                                "titleAlign": "center",
                                "titleY": -15,
                                "titleX": 0,
                            },
                            "legend": {
                                "fontWeight": font_weight,
                                "titleFontWeight": font_weight,
                                "labelFontWeight": font_weight,
                                "titleFontSize": medium_font_size,
                                "labelFontSize": small_font_size,
                                "labelLimit": 0,
                                "color": dark_color,
                                "titleColor": dark_color,
                                "labelColor": dark_color,
                                "tickColor": dark_color,
                                "domainColor": dark_color,
                            },
                        }
                    }
                )
            )
