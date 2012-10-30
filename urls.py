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

	(r'^technical/voting$', 'mmcghan.views.xxx'),
	(r'^technical/carpentry$', 'mmcghan.views.xxx'),  # Gallery

	# meredithmcghan.com/marketing

	(r'^marketing/social-light$', 'mmcghan.views.xxx'),
	(r'^marketing/etsy$', 'mmcghan.views.xxx'),
	(r'^marketing/spa$', 'mmcghan.views.xxx'),
	(r'^marketing/law-firm$', 'mmcghan.views.xxx'),
	(r'^marketing/women$', 'mmcghan.views.xxx'),
	(r'^marketing/poker$', 'mmcghan.views.poker_gallery'), # Gallery...

	# meredithmcghan.com/journalism

	(r'^journalism/sprawl$', 'mmcghan.views.xxx'),
	(r'^journalism/greening$', 'mmcghan.views.xxx'),
	(r'^journalism/zero-energy$', 'mmcghan.views.xxx'),
	(r'^journalism/water-grab$', 'mmcghan.views.xxx'),
	(r'^journalism/nursing-home$', 'mmcghan.views.xxx'),
	(r'^journalism/fake-news$', 'mmcghan.views.xxx'),
	(r'^journalism/covers$', 'mmcghan.views.xxx'), # Gallery....

	# meredithmcghan.com/entertainment

	(r'^entertainment/radiskull$', 'mmcghan.views.xxx'),
	(r'^entertainment/book-review$', 'mmcghan.views.xxx'),
	(r'^entertainment/shows$', 'mmcghan.views.xxx'), # Gallery...

	# meredithmcghan.com/commentary

	(r'^commentary/flint$', 'mmcghan.views.xxx'),
	(r'^commentary/columns$', 'mmcghan.views.xxx'), # Gallery...


	# meredithmcghan.com/creativity

	(r'^creativity/bus$', 'mmcghan.views.xxx'),
	(r'^creativity/perspectives$', 'mmcghan.views.xxx'), # Gallery...
)
