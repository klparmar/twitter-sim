from typing import List, Dict, Tuple

def create_profile_dictionary(file_name: str) \
        -> Dict[int, Tuple[str, List[int], List[int]]]:
    """
    Opens the file "file_name" in working directory and reads the content into a
    profile dictionary as defined on Page 2 Functions 1.

    Note, some spacing has been added for human readability.
    
    >>> create_profile_dictionary("profiles.txt")
    {100: ('Mulan', [300, 500], [200, 400]), 
    200: ('Ariel', [100, 500], [500]), 
    300: ('Jasmine', [500], [500, 100]), 
    400: ('Elsa', [100, 500], []), 
    500: ('Belle', [200, 300], [100, 200, 300, 400])}
    """
    f = open(file_name, "r")
    d = f.readlines()
    r = {}
    x=0
    while x < len(d):
        ting1 = d[x+2][:-1].split(', ')
        ting2 = d[x+3][:-1].split(', ')
        for val in range(len(ting1)):
            if ting1[val].isnumeric(): ting1[val] = int(ting1[val])
            else: del ting1[val]
        for val2 in range(len(ting2)):
            if ting2[val2].isnumeric(): ting2[val2] = int(ting2[val2])
            else: del ting2[val2]
        r[int(d[x][:-1])] = (d[x+1][:-1], ting1, ting2)
        x+=5
    f.close()
    return r


def create_chirp_dictionary(file_name: str) \
        -> Dict[int, Tuple[int, str, List[str], List[int], List[int]]]:
    """
    Opens the file "file_name" in working directory and reads the content into a
    chirp dictionary as defined on Page 2 Functions 2.

    Note, some spacing has been added for human readability.
    
    >>> create_chirp_dictionary("chirps.txt")
    {100000: (
        400, 
        'Does not want to build a %SnowMan %StopAsking',
        ['SnowMan', 'StopAsking'], 
        [100, 200, 300], 
        [400, 500]), 
    100001: (
        200, 
        'Make the ocean great again.', 
        [''], 
        [], 
        [400]), 
    100002: (
        500, 
        "Help I'm being held captive by a beast!  %OhNoes", 
        ['OhNoes'], 
        [400], 
        [100, 200, 300]), 
    100003: (
        500, 
        "Actually nm. This isn't so bad lolz :P %StockholmeSyndrome", 
        ['StockholmeSyndrome'], 
        [400, 100], 
        []), 
    100004: (
        300, 
        'If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.', 
        ['ShowYouTheWorld', 'JustSayNo'], 
        [500, 200], 
        [400]), 
    100005: (
        400, 
        'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan', 
        ['StockholmeSyndrome', 'SnowMan'], 
        [], 
        [200, 300, 100, 500])}
    """
    f = open(file_name, "r")
    d = f.readlines()
    r = {}
    x=0
    while x < len(d):
        ting0 = d[x+3][:-1].split(', ')
        ting1 = d[x+4][:-1].split(', ')
        ting2 = d[x+5][:-1].split(', ')
        for val in range(len(ting1)):
            if ting1[val].isnumeric(): ting1[val] = int(ting1[val])
            else: del ting1[val]
        for val2 in range(len(ting2)):
            if ting2[val2].isnumeric(): ting2[val2] = int(ting2[val2])
            else: del ting2[val2]
        r[int(d[x][:-1])] = (int(d[x+1][:-1]), d[x+2][:-1], ting0, ting1, ting2)
        x+=7
    f.close()
    return r

def get_top_chirps( \
        profile_dictionary: Dict[int, Tuple[str, List[int], List[int]]], \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]],
        user_id: int)\
        -> List[str]:
    """
    Returns a list of the most liked chirp for every user user_id follows.
    See Page 3 Function 3 of th .pdf.
    >>> profile_dictionary = create_profile_dictionary("profiles.txt")
    >>> chirp_dictionary   = create_chirp_dictionary("chirps.txt")
    >>> get_top_chirps(profile_dictionary, chirp_dictionary, 300)
    ["Actually nm. This isn't so bad lolz :P %StockholmeSyndrome"]
    >>> get_top_chirps( profiles, chirps, 500 )
    ['Make the ocean great again.', 
    'If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.', 
    'Does not want to build a %SnowMan %StopAsking']
    """
    topChirp = ""
    topChirps = []
    for x in range(len(profile_dictionary[user_id][2])):
        chirpCount = 0
        opDone = False
        for key in chirp_dictionary:
            if chirp_dictionary[key][0] == profile_dictionary[user_id][2][x]:
                if len(chirp_dictionary[key][3]) >= chirpCount:
                    chirpCount = len(chirp_dictionary[key][3])
                    topChirp =  chirp_dictionary[key][1]
                    opDone = True
        if opDone: topChirps.append(topChirp)

    return topChirps
    
def create_tag_dictionary( \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]]) \
        -> Dict[str, Dict[int, List[str]]]:
    """
    Creates a dictionary that keys tags to tweets that contain them.

    Note, some spacing has been added for human readability.
    
    >>> chirp_dictionary = create_chirp_dictionary("chirps.txt")
    >>> create_tag_dictionary(chirp_dictionary)
    {'SnowMan': {
        400: ['Does not want to build a %SnowMan %StopAsking', 'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']}, 
    'StopAsking': {
        400: ['Does not want to build a %SnowMan %StopAsking']}, 
    '': {
        200: ['Make the ocean great again.']}, 
    'OhNoes': {
        500: ["Help I'm being held captive by a beast!  %OhNoes"]}, 
    'StockholmeSyndrome': {
        500: ["Actually nm. This isn't so bad lolz :P %StockholmeSyndrome"], 
        400: ['LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']}, 
    'ShowYouTheWorld': {
        300: ['If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.']}, 
    'JustSayNo': {
        300: ['If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.']}}
    """
    tagList = []
    strList = []
    ting = {}
    sameKey = False
    for x in chirp_dictionary:
        for y in range(len(chirp_dictionary[x][2])):
            if chirp_dictionary[x][2][y] not in tagList:
                ting[chirp_dictionary[x][2][y]] = {}
                for i in chirp_dictionary:
                    for j in range(len(chirp_dictionary[i][2])):
                        if chirp_dictionary[i][2][j] == chirp_dictionary[x][2][y]:
                            for key in ting[chirp_dictionary[x][2][y]]:
                                if key == chirp_dictionary[i][0]:
                                    sameKey = True
                                else:
                                    sameKey = False
                            if not sameKey: strList = []
                            strList.append(chirp_dictionary[i][1])
                            ting[chirp_dictionary[x][2][y]][chirp_dictionary[i][0]] = strList
                strList = []
                tagList.append(chirp_dictionary[x][2][y])
    return ting

def get_tagged_chirps( \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]], \
        tag: str) \
        -> List[str]:
    """
    Returns a list of chirps containing specified tag.
    >>> chirp_dictionary = create_chirp_dictionary("chirps.txt")
    >>> get_tagged_chirps(chirp_dictionary, "SnowMan")
    ['Does not want to build a %SnowMan %StopAsking', 
    'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']
    """
    strList = []
    for x in chirp_dictionary:
        for y in range(len(chirp_dictionary[x][2])):
            if chirp_dictionary[x][2][y] == tag: strList.append(chirp_dictionary[x][1])
    return strList




    
