# Import dash library and related ones
import dash
import dash_daq as daq
import dash_core_components as dcc
import dash_html_components as html


def NamedDropdown(name, **kwargs):
    return html.Div(
        style={"margin": "10px 0px"},
        children=[
            html.P(children=f"{name}", style={"margin-left": "3px"}),
            dcc.Dropdown(**kwargs),
        ],
    )


def OnOffButton(name, **kwargs):
    return html.Div(
        # style={"margin": "auto"},
        children=[
            daq.PowerButton(**kwargs)
        ],
    )


def simpleButton(name, **kwargs):
    return html.Div(
        # style={"margin": "auto"},
        children=[
            daq.StopButton(**kwargs)
        ],
    )