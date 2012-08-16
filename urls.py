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

	(r'^$', 'mmcghan.views.index'),
	(r'^technical-writing$', 'mmcghan.views.technicalwriting'),
	(r'^investigative-journalism-and-news$', 'mmcghan.views.investigativejournalismandnews'),
	(r'^marcomm-and-trade-publications$', 'mmcghan.views.marcommandtradepublications'),
	(r'^arts-entertainment-and-lifestyle$', 'mmcghan.views.artsentertainmentandlifestyle'),
	(r'^commentary-and-creativity$', 'mmcghan.views.commentaryandcreativity'),
	(r'^resume$', 'mmcghan.views.resume'),
)
