def score_match(players):

    """
    >>> score_match({'Sombra': [10,22,24],'Tracer': [13,25,24],'Bastion':[23,38,10],'Widowmaker':[14,39,40]})
    {'Sombra': ['Tracer'], 'Tracer': ['Sombra'], 'Bastion': ['Widowmaker'], 'Widowmaker': ['Bastion']}
    
    >>> score_match({'Sombra': [19,22,22],'Tracer': [20,24,24],'Bastion':[22,23,25]})
    {'Sombra': ['Bastion', 'Tracer'], 'Tracer': ['Bastion', 'Sombra'], 'Bastion': ['Sombra', 'Tracer']}

    >>> score_match({'Hanzo': [21],'Mei': [20,24,24], 'Bastion':[10]})
    {'Hanzo': ['Mei'], 'Mei': ['Hanzo'], 'Bastion': []}
    """
    matched_player = {k:sorted([k1 for k1,v1 in players.items() if k!=k1 
                                and abs(min(v)-min(v1))<=5 
                                and abs(max(v)-max(v1))<=5]) for k,v in players.items()}
    return matched_player