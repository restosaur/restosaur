from restosaur import API

api = API()
root = api.resource('/')


@root.get()
def root_view(ctx):
    return ctx.Response({'root': 'ok'})


urlpatterns = api.urlpatterns()
