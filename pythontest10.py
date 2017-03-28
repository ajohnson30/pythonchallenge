from itertools import groupby



def audioactive1(n): # faster compiled
    strl = {("1","1","1"): "31", ("1","1"): "21", ("1",): "11",
            ("2","2","2"): "32", ("2","2"): "22", ("2",): "12",
            ("3","3","3"): "33", ("3","3"): "23", ("3",): "13" }
    s = [1]
    prec = str(s[-1])
    for i in xrange(n-1):
        r = []
        for e,l in groupby(prec):
            r.append( strl[tuple(l)] )
        prec = "".join(r)
        s.append( int(prec) )
    return s

def audioactive2(n): # faster uncompiled
    strl = {("1","1","1"): "31", ("1","1"): "21", ("1",): "11",
            ("2","2","2"): "32", ("2","2"): "22", ("2",): "12",
            ("3","3","3"): "33", ("3","3"): "23", ("3",): "13" }
    result = [1]
    prec = "1"
    for i in xrange(n-1):
        prec = "".join( strl[tuple(l)] for e,l in groupby(prec) )
        result.append( int(prec) )
    return result

s = audioactive2(31)[30]

print len(str(s))
