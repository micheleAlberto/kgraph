Im=1000
Fe_Im=4000
Im_In=10
Tq=2.42/4000.
Ti=29.76/40000.
Fe_In=Fe_Im*Im_In
In=Im/Im_In

T_build=unitaryBuildTime*Im*Fe_Im
T_search=unitSearchTime*Im*Fe_Im*Im/datasetSize

rr=[(t,t['response']['unitBuildTime']*Im*Fe_Im,t['response']['unitSearchTime']*Im*Fe_Im*Fe_Im*Im/t['request']['datasetSize']) for t in r]
sep=','

def lineToStrII(t):
    ans=''
    for d,v in t['request'].iteritems():
        ans=ans+"{0} ,".format(v)
    for d,v in t['response'].iteritems():
        ans=ans+"{0} ,".format(v)

    return ans

def lineToStrI(t):
    return "{0} , {1} , {2} , {3} \n".format(lineToStrII(t[0]),t[1],t[2],(t[1]+t[2]))

def intestazione(t):
    ans=''
    for d,v in t['request'].iteritems():
        ans=ans+"{0} ,".format(d)
    for d,v in t['response'].iteritems():
        ans=ans+"{0} ,".format(d)
    ans=ans+" , {0} , {1} , {2} \n".format('buildTime','searchTime','total')
    return ans  



