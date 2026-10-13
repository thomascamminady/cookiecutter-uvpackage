"""Opinionated Altair defaults: renderer, row limit and a clean theme.

Requires the ``viz`` extra (``uv add {{ cookiecutter.project_slug }}[viz]``) or
``altair`` itself.

Examples
--------
>>> AltairConfig(dark_color="black").setup()  # doctest: +SKIP
"""

from dataclasses import dataclass
from typing import Literal, LiteralString

try:
    import altair as alt
except ImportError as e:
    msg = "Altair is not installed. Install it with `uv add altair`."
    raise ImportError(msg) from e

from altair.theme import ThemeConfig

Renderer = Literal["browser", "html", "jupyter"]
FontWeight = Literal["normal", "bold"]


@dataclass(frozen=True, slots=True, kw_only=True)
class AltairConfig:
    """Altair settings; call `setup` to apply them."""

    where: Renderer = "browser"
    theme_name: LiteralString = "my_theme"
    dark_color: LiteralString = "gray"
    font_weight: FontWeight = "normal"
    small_font_size: int = 12
    medium_font_size: int = 14
    large_font_size: int = 18
    height: int = 500
    width: int = 500
    spacing_facet: int = 60
    spacing_concat: int = 60

    def setup(self) -> None:
        """Disable the row limit, enable the renderer and the theme."""
        alt.data_transformers.disable_max_rows()
        alt.renderers.enable(self.where)
        alt.theme.register(self.theme_name, enable=True)(self.theme)

    def theme(self) -> ThemeConfig:
        """Return the Vega-Lite configuration of the theme."""
        color = self.dark_color
        weight = self.font_weight
        small = self.small_font_size
        medium = self.medium_font_size
        return ThemeConfig(
            config={
                "text": {"color": color, "fontSize": small},
                "title": {
                    "anchor": "middle",
                    "color": color,
                    "fontSize": self.large_font_size,
                    "fontWeight": weight,
                    "subtitleColor": color,
                    "subtitleFontSize": medium,
                },
                "header": {
                    "titleColor": color,
                    "titleFontSize": self.large_font_size,
                    "titleFontWeight": weight,
                    "labelColor": color,
                    "labelFontSize": medium,
                    "labelFontWeight": weight,
                },
                "view": {
                    "continuousHeight": self.height,
                    "continuousWidth": self.width,
                    "strokeWidth": 0,
                    "fill": "white",
                },
                "facet": {"spacing": self.spacing_facet},
                "concat": {"spacing": self.spacing_concat},
                "axis": {
                    "domain": True,
                    "domainColor": color,
                    "domainWidth": 1,
                    "gridWidth": 1,
                    "gridCap": "round",
                    "gridDash": [2, 4],
                    "labelAngle": 0,
                    "labelColor": color,
                    "labelFontSize": small,
                    "labelFontWeight": weight,
                    "tickColor": color,
                    "tickSize": 5,
                    "titleColor": color,
                    "titleFontSize": medium,
                    "titleFontWeight": weight,
                },
                "axisX": {"titleAnchor": "end", "titleAlign": "center"},
                "axisY": {
                    "titleAnchor": "end",
                    "titleAngle": 0,
                    "titleAlign": "center",
                    "titleY": -15,
                    "titleX": 0,
                },
                "legend": {
                    "labelColor": color,
                    "labelFontSize": small,
                    "labelFontWeight": weight,
                    "labelLimit": 0,
                    "titleColor": color,
                    "titleFontSize": medium,
                    "titleFontWeight": weight,
                },
            }
        )
