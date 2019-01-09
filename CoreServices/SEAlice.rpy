## SEAlice
# System integrity protection policy
# (C) AliceOS Developers.

init 10 python:
    import gc
    import urllib2
    class SystemIntegrity():

        applist = []

        blocked_apps = {}

        def verified_applets(self):
            return self.applist

        def verify_applet_ids(self):
            """
            Verify that applet IDs are valid.
            """
            for app in self.applist:
                id = app.identifier.split('.')
                url = "http://www." + id[1] + "." + id[0]
                try:
                    urllib2.urlopen(url)
                except urllib2.HTTPError as e:
                    if e.code == 404:
                        self.blocked_apps['app'] = 'Invalid identifier.'
                        self.applist.remove(app)
                except urllib2.URLError as e:
                    self.blocked_apps['app'] = 'Invalid identifier.'
                    self.applist.remove(app)

        def __init__(self):
            for obj in gc.get_objects():
                if isinstance(obj, Applet):
                    self.applist.append(obj)

    undyne = SystemIntegrity()