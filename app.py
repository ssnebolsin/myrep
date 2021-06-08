from flask import Flask, render_template, request, redirect, session, url_for
from auth.auth_flow import build_auth_code_flow, build_msal_app, load_auth_cache, save_auth_cache
import auth_config
from flask_session import Session
import logging
import pbie_config
from services.pbiembedservice import PbiEmbedService
import pandas as pd
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import dash
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from keplergl import KeplerGl
from maps_config import get_arcs_config, get_routes_config


app = Flask(__name__)
app.config.from_object(auth_config)
Session(app)

app1 = dash.Dash(__name__, server=app, url_base_pathname='/dashboard/')


df = pd.read_csv('data/df_charts.csv')
df1 = df.groupby(['Місто', 'Дата','Вік'])['К-ть'].max().reset_index().sort_values(by='К-ть', ascending=False)

dff = df.groupby(['Місто', 'Дата'])['К-ть'].max().reset_index().sort_values(by='К-ть', ascending=False)
dff = dff.sort_values(by=['Дата', 'К-ть'])

ages = df['Вік'].unique().tolist()
ages.sort(reverse=False)

cities = df['Місто'].unique().tolist()
cities.sort(reverse=False)

df3 = df.groupby(['Час', 'Вік', 'Місто'])['К-ть'].sum().reset_index()
df3_2 = df3.groupby(['Час', 'Вік'])['К-ть'].sum().reset_index()
df4 = df.groupby(['Час', 'Місто'])['К-ть'].sum().reset_index()

dg2 = pd.read_csv('data/df_routes.csv')
df_arcs_centroids = pd.read_csv('data/df_arcs.csv')


app1.layout = dbc.Container([
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H2("Переміщення населення у м.Івано-Франківськ",
                        style={'textAlign': 'left', 'color': 'lightgrey', 'font-family': 'Proxima Nova Bold'})
            ], width={'size': 10})
        ]),
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(id='c_dropdown', placeholder='Місто', multi=True,
                                     options=[{'label': k, 'value': k} for k in cities]),
                        width={'size': 2, "offset": 1, 'order': 2}
                        ),
                dbc.Col(dcc.Dropdown(id='a_dropdown', placeholder='Вік', multi=True,
                                     options=[{'label': k, 'value': k} for k in ages],
                                     value=[]),
                        width={'size': 2, "offset": 5, 'order': 1}
                        )
            ]
        ), ], fluid=True, style={'backgroundColor': '#343a40'}),
    dbc.Row(
        [
            dbc.Col(dcc.Graph(
                id='barchart',
                figure=px.bar(dff, x='К-ть', y='Місто', title='Розподіл за віком', animation_frame='Дата',
                              range_x=[0, 3000], color='К-ть').update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                     'paper_bgcolor': 'rgba(0, 0, 0, 0)'}).update_yaxes(title='', visible=True, showticklabels=True)

            ),
                #                         width=10, lg={'size': 4,  "offset": 0, 'order': 'first'}
            ),
            dbc.Col(dcc.Graph(
                id='linechart',
                figure=px.line(df3_2, x="Час", y="К-ть", color='Вік', title='Переміщення за віком').update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                     'paper_bgcolor': 'rgba(0, 0, 0, 0)'}).update_yaxes(title='', visible=True,
                                                                        showticklabels=True).update_xaxes(title='',
                                                                                                          visible=True,
                                                                                                          showticklabels=True)

            ),  # width=10, lg={'size': 4,  "offset": 0, 'order': 'second'}
            ),
        ]
    ),
    dbc.Row(
        [
            dbc.Col(dcc.Graph(
                id='linechart2',
                figure=px.line(df4, x="Час", y="К-ть", color='Місто', title='Переміщення по містам').update_layout(
                    {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                     'paper_bgcolor': 'rgba(0, 0, 0, 0)'}).update_yaxes(title='', visible=True,
                                                                        showticklabels=True).update_xaxes(title='',
                                                                                                          visible=True,
                                                                                                          showticklabels=True)

            )),
        ]
    ),
    html.Iframe(id='map1', srcDoc=open('templates/geoIF_arcs_centroids.html', 'r').read(), width='100%', height='700'),
    html.Iframe(id='map', srcDoc=open('templates/geoIF_routes.html', 'r').read(), width='100%', height='700')

], fluid=True, style={'backgroundColor': 'lightgrey'})

## barchart
@app1.callback(
    Output('barchart', 'figure'),
    [Input('a_dropdown', 'value')]
)
def update_graph(val):
    if len(val) > 0:
        dff2 = df1.sort_values(by='К-ть', ascending=False).copy()
        dff2 = dff2.loc[dff2['Вік'].isin(val)].sort_values(by=['Дата', 'К-ть'])
        fig1 = px.bar(dff2, x='К-ть', y='Місто', title='Розподіл за віком', animation_frame='Дата', range_x=[0, 3000],
                      color='К-ть').update_layout(
            {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
             'paper_bgcolor': 'rgba(0, 0, 0, 0)'}).update_yaxes(title='', visible=True, showticklabels=True)
        return fig1
    elif len(val) == 0:
        #         Dash.no_update
        #         raise dash.exceptions.PreventUpdate
        dff3 = dff.copy()
        fig = px.bar(dff3, x='К-ть', y='Місто', title='Розподіл за віком', animation_frame='Дата', range_x=[0, 3000],
                     color='К-ть').update_layout(
            {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
             'paper_bgcolor': 'rgba(0, 0, 0, 0)'}).update_yaxes(title='', visible=True, showticklabels=True)
        return fig

    ## linechart


@app1.callback(
    Output('linechart', 'figure'),
    [Input('c_dropdown', 'value')]
)
def update_lchart(val):
    if len(val) > 0:
        dff2_1 = df3.copy()
        dff2_1 = dff2_1.loc[dff2_1['Місто'].isin(val)]
        fig2 = px.line(dff2_1, x="Час", y="К-ть", color='Вік', title='Переміщення за віком').update_layout(
            {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
             'paper_bgcolor': 'rgba(0, 0, 0, 0)'}).update_yaxes(title='', visible=True,
                                                                showticklabels=True).update_xaxes(title='',
                                                                                                  visible=True,
                                                                                                  showticklabels=True)
        return fig2
    elif len(val) == 0:
        dff2_1 = df3.groupby(['Час', 'Вік'])['К-ть'].sum().reset_index().copy()
        fig2 = px.line(dff2_1, x="Час", y="К-ть", color='Вік', title='Переміщення за віком').update_layout(
            {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
             'paper_bgcolor': 'rgba(0, 0, 0, 0)'}).update_yaxes(title='', visible=True,
                                                                showticklabels=True).update_xaxes(title='',
                                                                                                  visible=True,
                                                                                                  showticklabels=True)
        return fig2


    ## linechart2


@app1.callback(
    Output('linechart2', 'figure'),
    [Input('c_dropdown', 'value')]
)
def update_lchart(val):
    if len(val) > 0:
        dff2_2 = df4.copy()
        dff2_2 = dff2_2.loc[dff2_2['Місто'].isin(val)]
        fig3 = px.line(dff2_2, x="Час", y="К-ть", color='Місто', title='Переміщення по містам').update_layout(
            {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
             'paper_bgcolor': 'rgba(0, 0, 0, 0)'}).update_yaxes(title='', visible=True,
                                                                showticklabels=True).update_xaxes(title='',
                                                                                                  visible=True,
                                                                                                  showticklabels=True)
        return fig3
    elif len(val) == 0:
        dff2_2 = df4.copy()
        fig3 = px.line(dff2_2, x="Час", y="К-ть", color='Місто', title='Переміщення по містам').update_layout(
            {'plot_bgcolor': 'rgba(0, 0, 0, 0)',
             'paper_bgcolor': 'rgba(0, 0, 0, 0)'}).update_yaxes(title='', visible=True,
                                                                showticklabels=True).update_xaxes(title='',
                                                                                                  visible=True,
                                                                                                  showticklabels=True)
        return fig3

        ## arcs


@app1.callback(
    Output('map1', 'srcDoc'),
    [Input('c_dropdown', 'value')]
)
def update_html(val):
    config_arcs = get_arcs_config(val)
    KeplerGl().save_to_html(file_name='templates/geoIF_arcs_centroids.html', data={'geodt': df_arcs_centroids},
                            config=config_arcs,
                            read_only=True)
    return open('templates/geoIF_arcs_centroids.html', 'r').read()

    ## routes


@app1.callback(
    Output('map', 'srcDoc'),
    [Input('c_dropdown', 'value')]
)
def update_html_routes(val):
    config_routes = get_routes_config(val)
    KeplerGl().save_to_html(file_name='templates/geoIF_routes.html', data={'geodt': dg2},
                            config=config_routes,
                            read_only=True)
    return open('templates/geoIF_routes.html', 'r').read()


from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)


@app.route("/")
def index():
    if not session.get("user") or session.get("user") is None:
        session["flow"] = build_auth_code_flow(scopes=auth_config.SCOPE)
        return redirect(session["flow"]["auth_uri"])
    return render_template("index.html")


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/dashboard')
def my_dash():
    return app1.index()


@app.route('/getReport/<report_name>')
def get_report(report_name):
    try:
        return render_template('report_template.html',
                               template_report_name=report_name)
    except:
        return redirect('/projects', code=302)


@app.route('/getpbieinfo/<report_name>', methods=['GET'])
def get_pbie_info(report_name):
    """Returns PBI embed configuration"""
    try:
        workspace_id = pbie_config.REPORT_MAP[report_name]["workspace_id"]
        report_id = pbie_config.REPORT_MAP[report_name]["report_id"]
        page_name = pbie_config.REPORT_MAP[report_name]["default_page_name"]
        embed_info = PbiEmbedService().get_embed_params_for_single_report(workspace_id,
                                                                          report_id,
                                                                          None,
                                                                          # session["user"].get("emails")[0]
                                                                          'sergiy.nebolsin2@kyivstar.ua',
                                                                          page_name)
        return embed_info
    except Exception as ex:
        return json.dumps({'errorMsg': str(ex)}), 500


@app.route(auth_config.REDIRECT_PATH)
def authorized():
    try:
        cache = load_auth_cache()
        result = build_msal_app(cache=cache).acquire_token_by_auth_code_flow(
            session.get("flow", {}), request.args)
        if "error" in result:
            return render_template("auth_error.html", result=result)
        session["user"] = result.get("id_token_claims")
        save_auth_cache(cache)
    except ValueError:
        pass
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.clear()  # Wipe out user and its token cache from session
    return redirect(  # Also logout from your tenant's web session
        auth_config.AUTHORITY + "/oauth2/v2.0/logout" +
        "?post_logout_redirect_uri=" + url_for("index", _external=True))

app.jinja_env.globals.update(_build_auth_code_flow=build_auth_code_flow)  # Used in template


if __name__ == "__main__":
    app.run()
    # app.run(host='0.0.0.0', port=5000)












