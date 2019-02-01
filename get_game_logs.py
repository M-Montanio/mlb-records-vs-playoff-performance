"""
All data is coming from retorsheet.org. The following is posted per website
request:

The information used here was obtained free of charge from and is copyrighted by
Retrosheet. Interested parties may contact Retrosheet at www.retrosheet.org
"""

import zipfile
import requests
import io

def upload_data(game_log_list):

    """
    Web scrapes for game logs and unzips and saves files.

    Args:
        game_log_list - list of variables used to denote certain game log zip
                        files on retrosheet.org
    """

    for dataset in game_log_list:
        url = 'https://www.retrosheet.org/gamelogs/gl{}.zip'.format(dataset)
        response = requests.get(url)
        zip_ref = zipfile.ZipFile(io.BytesIO(response.content))
        zip_ref.extractall()

def main():
    game_logs = ['2000_09', '2010_18', 'wc', 'dv', 'lc', 'ws']
    upload_data(game_logs)

if __name__ == "__main__":
    main()
