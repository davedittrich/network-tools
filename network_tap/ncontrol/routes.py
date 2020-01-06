def routes():
    from .paths import CreateR, DeleteR, InfoR, ListR, StartR, StopR
    p = paths()
    create_r = CreateR()
    delete_r = DeleteR()
    info_r = InfoR()
    list_r = ListR()
    start_r = StartR()
    stop_r = StopR()
    funcs = [create_r,
             delete_r,
             info_r,
             list_r,
             start_r,
             stop_r]
    return dict(list(zip(p, funcs)))


def paths():
    return ['/create',
            '/delete',
            '/info',
            '/list',
            '/start',
            '/stop']
