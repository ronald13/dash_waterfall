import pandas as pd
import plotly.graph_objects as go


def create_waterfall(x,y):
    fig = go.Figure(go.Waterfall(
        name = "Movie",
        orientation = "v",
        x = x,
        y=y,
        # textposition = "auto",
        text = [str(abs(x)) for x in y],
        connector = {"line":{"color":"#b20710"}},
        increasing = {"marker":{"color":"#b20710"}},
        decreasing = {"marker":{"color":"orange"}},
    ))

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False, visible=False)
    fig.update_traces(hovertemplate=None)
    fig.update_layout( height=450,
                       margin=dict(t=80, b=50, l=0, r=50, pad=20),
    #                    hovermode="x unified",
    #                    # xaxis_title=' ', yaxis_title=" ",
    #                    # plot_bgcolor='#333', paper_bgcolor='#333',
    #                    # hoverlabel_bgcolor = '#000',
    #                    # title_font=dict(size=25, color='#8a8d93', family="Lato, sans-serif"),
    #                    # font=dict(color='#8a8d93'))
                       )
    return fig