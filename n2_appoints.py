import datetime

class Appoint :
    __slots__ = ['day',
                 'starttime',
                 'endtime',
                 'duration',
                 'k',
                 'names',]

    def __init__ (self, day, time, duration, k, *names) :
        self.day = int(day)
        self.starttime = datetime.datetime.strptime(time, '%H:%M')
        self.duration = int(duration)
        self.endtime = self.starttime + datetime.timedelta(minutes = self.duration)
        self.k = int(k)
        self.names = names

class Info :
    __slots__ = ['day',
                 'name',]

    def __init__ (self, day, name) :
        self.day = int(day)
        self.name = name

def parse_query (appoints, query) :
    if query[0] == 'APPOINT' :
        try_add_appoint(appoints, Appoint(*query[1:]))
    elif query[0] == 'PRINT' :
        print_info(appoints, Info(*query[1:]))

def try_add_appoint (appoints, appoint) :
    fail_names = []
    for app in appoints :
        if app.day == appoint.day :
            if not ((app.starttime <= appoint.starttime and app.endtime <= appoint.starttime) or
                    (app.starttime >= appoint.endtime and app.endtime >= appoint.endtime)) :
                for name in app.names :
                    if name in appoint.names :
                        fail_names.append(name)
    if fail_names :
        print('FAIL')
        print(' '.join((name for name in appoint.names if name in fail_names)))
    else :
        print('OK')
        appoints.append(appoint)

def print_info (appoints, info) :
    app_list = [app for app in appoints if (app.day == info.day and info.name in app.names)]
    app_list.sort(key = lambda appoint : appoint.starttime)
    for app in app_list :
        print(str(app.starttime.time())[:-3], app.duration, *app.names)

n = int(input())
queries = [input().split() for i in range(n)]
appoints = []
for query in queries :
    parse_query(appoints, query)
