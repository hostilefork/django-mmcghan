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

	(r'^technical/voting$', 'mcghan.views.xxx'),
	(r'^technical/carpentry$', 'mcghan.views.xxx'),  # Gallery

	# meredithmcghan.com/marketing

	(r'^marketing/social-light$', 'mcghan.views.xxx'),
	(r'^marketing/etsy$', 'mcghan.views.xxx'),
	(r'^marketing/spa$', 'mcghan.views.xxx'),
	(r'^marketing/law-firm$', 'mcghan.views.xxx'),
	(r'^marketing/women$', 'mcghan.views.xxx'),
	(r'^marketing/poker$', 'mmcghan.views.poker_gallery'), # Gallery...

	# meredithmcghan.com/journalism

	(r'^journalism/sprawl$', 'mcghan.views.xxx'),
	(r'^journalism/greening$', 'mcghan.views.xxx'),
	(r'^journalism/zero-energy$', 'mcghan.views.xxx'),
	(r'^journalism/water-grab$', 'mcghan.views.xxx'),
	(r'^journalism/nursing-home$', 'mcghan.views.xxx'),
	(r'^journalism/fake-news$', 'mcghan.views.xxx'),
	(r'^journalism/covers$', 'mcghan.views.xxx'), # Gallery....

	# meredithmcghan.com/entertainment

	(r'^entertainment/radiskull$', 'mcghan.views.xxx'),
	(r'^entertainment/book-review$', 'mcghan.views.xxx'),
	(r'^entertainment/shows$', 'mcghan.views.xxx'), # Gallery...

	# meredithmcghan.com/commentary

	(r'^commentary/flint$', 'mcghan.views.xxx'),
	(r'^commentary/columns$', 'mcghan.views.xxx'), # Gallery...


	# meredithmcghan.com/creativity

	(r'^creativity/bus$', 'mcghan.views.xxx'),
	(r'^creativity/perspectives$', 'mcghan.views.xxx'), # Gallery...
)
