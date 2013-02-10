from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SAMEngine.views.home', name='home'),
    # url(r'^SAMEngine/', include('SAMEngine.foo.urls')),
    url(r'^$', 'characters.views.CharacterList'),
    url(r'^new$', 'characters.views.NewCharacter'),
    url(r'^show/(\d+)', 'characters.views.BasicInfo', name="BasicInfo"),
    # abilities
    url(r'^ability/new', 'characters.views.AbilityNew'),
    url(r'^ability/show/(\d+)', 'characters.views.AbilityShow'),
)
