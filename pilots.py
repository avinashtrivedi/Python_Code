PILOT_INVALID=-1
PILOT_NOVICE =0
PILOT_STUDENT =1
PILOT_CERTIFIED =2
PILOT_50_HOURS=3
def get_minimums(cert, area, instructed, vfr, daytime, minimums):
    df = minimums
    col=[]
    if instructed==True:
        col.append('Dual')

    if cert==1:
        col.append('Student')
    elif cert==2:
        col.append('Student')
        col.append('Certified')
    elif cert==3:
        col.append('Student')
        col.append('Certified')
        col.append('50 Hours')
    df = df[df['CATEGORY'].isin(col)]

    ar =['Any']
    if area in ('pattern','Practice Area'):
        ar.append('Local')
    ar.append(area)
    df = df[df['AREA'].isin(ar)]

    if vfr:
        df = df[df['CONDITIONS']=='VMC']
    else:
        df = df[df['CONDITIONS']=='IMC']

    if daytime:
        df = df[df['TIME']=='Day']
    else:
        df = df[df['TIME']=='Night']
    if len(df)>=1:
        return [min(df['CEILING']),min(df['VISIBILITY']),max(df['WIND']),max(df['CROSSWIND'])]
    else:
        return None