import pandas as pd
import plotly.graph_objects as go
import nfl_data_py as nfl

import sqlite3

data = nfl.import_seasonal_data([2021, 2022])
df_players = nfl.import_rosters([2022])

player_names = df_players[['player_name', 'player_id']]

# I want to pair down some of this data so it only has what we need.
df = data[['player_id',
          'season',
          'passing_yards',
          'passing_tds',
          'interceptions',
          'sacks',
          'sack_fumbles_lost',
          'rushing_yards',
          'rushing_tds',
          'rushing_fumbles_lost',
          'rushing_2pt_conversions',
          'receptions',
          'targets',
          'receiving_yards',
          'receiving_tds',
          'receiving_fumbles_lost',
          'receiving_2pt_conversions',
          'target_share',
          'special_teams_tds',
          'fantasy_points_ppr',
          'games',
          'ppr_sh']]

named_df = pd.merge(player_names, df, how='inner', on='player_id')


