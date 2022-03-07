from urllib import response
import mwclient 

site = mwclient.Site('lol.fandom.com', path='/')

resp = site.api(
    'cargoquery',
    limit = 'max',
    tables = "ScoreboardGames=SG",
	fields = "SG.Tournament, SG.DateTime_UTC, SG.Team1, SG.Team2"
)

print(resp)