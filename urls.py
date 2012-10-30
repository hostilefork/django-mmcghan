from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	# Example:
	# (r'^mchgan/', include('mcghan.foo.urls')),

	# Uncomment the admin/doc line below and add 'django.contrib.admindocs'
	# to INSTALLED_APPS to enable admin documentation:
	# (r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	# (r'^admin/', include(admin.site.urls)),

	# Main Index

	(r'^$', 'mmcghan.views.index'),

	# Categories

	(r'^technical$', 'mmcghan.views.technical'),
	(r'^journalism$', 'mmcghan.views.journalism'),
	(r'^marketing$', 'mmcghan.views.marketing'),
	(r'^entertainment$', 'mmcghan.views.entertainment'),
	(r'^commentary$', 'mmcghan.views.commentary'),
	(r'^creative$', 'mmcghan.views.creative'),

	# meredithmcghan.com/technical

	(r'^technical/voting$', xxx),
	(r'^technical/carpentry$', xxx),  # Gallery

	# meredithmcghan.com/marketing

	(r'^marketing/social-light$', xxx),
	(r'^marketing/etsy$', xxx),
	(r'^marketing/spa$', xxx),
	(r'^marketing/law-firm$', xxx),
	(r'^marketing/women$', xxx),
	(r'^marketing/poker$', 'mmcghan.views.poker_gallery'), # Gallery...

	# meredithmcghan.com/journalism

	(r'^journalism/sprawl$', xxx),
	(r'^journalism/greening$', xxx),
	(r'^journalism/zero-energy$', xxx),
	(r'^journalism/water-grab$', xxx),
	(r'^journalism/nursing-home$', xxx),
	(r'^journalism/fake-news$', xxx),
	(r'^journalism/covers$', xxx), # Gallery....

	# meredithmcghan.com/entertainment

	(r'^entertainment/radiskull$', xxx),
	(r'^entertainment/book-review$', xxx),
	(r'^entertainment/shows$', xxx), # Gallery...

	# meredithmcghan.com/commentary

	(r'^commentary/flint$', xxx),
	(r'^commentary/columns$', xxx), # Gallery...


	# meredithmcghan.com/creativity

	(r'^creativity/bus$', xxx),
	(r'^creativity/perspectives$', xxx), # Gallery...
)
