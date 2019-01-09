## SEAlice
# System integrity protection policy
# (C) AliceOS Developers.

init 1 python:
    import gc
    import urllib2
    class SystemIntegrity():

        applist = []

        blocked_apps = {}

        def verified_applets():
            return self.applist

        def verify_applet_ids():
            """
            Verify that applet IDs are valid.
            """
            for app in applist:
                id = app['identifier'].split('.')
                url = "https://www." + id[1] + "." + id[0]
                try:
                    urllib2.urlopen(url).getcode()
                except HTTPError as e:
                    self.blocked_apps['app'] = 'Invalid identifier.'
                    self.applist.remove(app)

        def __init__():
            for obj in gc.get_objects():
                if isinstance(obj, Applet):
                    self.applist.append(obj)