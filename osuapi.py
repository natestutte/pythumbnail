import os, sys, json, re
from ossapi import Ossapi

config = json.load(open('config.json'))

def _convertURLold(url: str):
    idIndex = url.index("/", 29);
    modeIndex = url.index("/", 25);
    scoreid = url[idIndex + 1:];
    mode = url[modeIndex + 1:idIndex];
    return [scoreid, mode]

# returns ID and mode if available from a beatmap, user, or score URL
def convertURL(url: str):
    suffix = url[19:]
    params = suffix.split('/')
   
    if   params[0] == 'b' or params[0] == 'beatmaps':    # beatmap [diff ID]
        return [params[1]]
    elif params[0] == 'beatmapsets':                    # beatmapset [diff ID, mode]
        return [params[2], params[1].split('#')[1]]
    elif params[0] == 'u' or params[0] == 'users':       # user [user ID]
        return [params[1]]
    elif params[0] == 'scores':                         # score [score ID, mode]
        return [params[2], params[1]]
    else:
        return None
    
def getScore(url):
    # provide this yourself, functionality for lazer login may come tho
    api = Ossapi(config['ID'], config['SECRET'])
    scoreID = convertURL(url)
    return api.score(scoreID[1], scoreID[0])

def getUser(url: str):
    api = Ossapi(config['ID'], config['SECRET'])
    uid = convertURL(url)[0]
    
    return api.user(uid)

def getBeatmap(url: str):
    api = Ossapi(config['ID'], config['SECRET'])
    bid = convertURL(url)[0]
    
    return api.beatmap(bid)