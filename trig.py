import math

def isnum(num):
    try:
        float(num)
        return True
    except ValueError:
        print("error")
        return False


def getTrigs(angle,op,hy,ad):
    unknown=4
    tvars = {
        'angle':'unknown',
        'op':'unknown',
        'hy':'unknown',
        'ad':'unknown'
    }

    #Check if there is input there and if so add to tvar dictionary
    if isnum(angle):
        tvars['angle'] = float(angle)
        unknown-=1

    if isnum(op):
        tvars['op'] = float(op)
        unknown-=1

    if isnum(hy):
        tvars['hy'] = float(hy)
        unknown-=1

    if isnum(ad):
        tvars['ad'] = float(ad)
        unknown-=1
    #List of parts of a right triangle and all ways to calcuate them with the other parts
    trigs = {
        'angle':[
            [lambda a,o: math.degrees(math.atan2(o,a)), ['ad','op']],
            [lambda a,h: math.degrees(math.acos((a/h))), ['ad','hy']],
            [lambda o,h: math.degrees(math.asin((o/h))), ['op','hy']]
        ],
        
        'hy':[
            [lambda a,o: (a**2 + o**2)**0.5, ['ad','op']],
            [lambda a,an: ((math.cos(math.radians(an)))**(-1))*a, ['ad','angle']],
            [lambda o,an: ((math.sin(math.radians(an)))**(-1))*o, ['op','angle']]
        ],

        'op':[
            [lambda a,h: math.sin(math.acos(a/h))*h, ['ad','hy']],
            [lambda a,an: math.sin(math.radians(an))*(((math.cos(math.radians(an)))**(-1))*a), ['ad','angle']],
            [lambda h,an: math.sin(math.radians(an))*h, ['hy','angle']]
        ],

        'ad':[
            [lambda o,h: math.cos(math.asin(o/h))*h, ['op','hy']],
            [lambda o,an: math.cos(math.radians(an))*(((math.sin(math.radians(an)))**(-1))*o), ['op','angle']],
            [lambda h,an: math.cos(math.radians(an))*h, ['hy','angle']]
        ]

    }

    if unknown == 0:
        return tvars
    elif unknown < 3:
        while unknown > 0:
            for part in trigs:
                #if we don't have that part of triangle
                if tvars[part] == 'unknown':
                    for poscalc in trigs[part]:
                        #Check if we have the numbers possible to calculate
                        if tvars[poscalc[1][0]] != 'unknown' and tvars[poscalc[1][1]] != 'unknown':
                            #Get part as the  result of the lambda function
                            tvars[part] = poscalc[0](tvars[poscalc[1][0]], tvars[poscalc[1][1]])
                            unknown -= 1
                            break
        for var in tvars:
            #Round so it isn't some useless 27 long digit float point number
            tvars[var] = round(tvars[var], 3)
        return tvars
    else:
        #Really, one number! I'm not a magician!
        return "not-enough-info"

