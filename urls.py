from django.conf.urls.defaults import *
from django.views.generic.simple import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('mmcghan.views',
	# Example:
	# (r'^mchgan/', include('mcghan.foo.urls')),

	# Uncomment the admin/doc line below and add 'django.contrib.admindocs'
	# to INSTALLED_APPS to enable admin documentation:
	# (r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	# (r'^admin/', include(admin.site.urls)),

	# https://docs.djangoproject.com/en/dev/topics/http/urls/
	# http://stackoverflow.com/questions/10020233/url-templatetag-in-django-and-direct-to-template

	# Main Index

	url(r'^$', direct_to_template, {'template': 'index.html'}, name='index'),

	# Contact page

	url(r'^contact$', direct_to_template, {'template': 'contact.html'}, name='contact'),

	# Credits page

	url(r'^credits$', direct_to_template, {'template': 'credits.html'}, name='credits'),

	# Redirect blog in case someone types meredithmcghan.com/blog instead of blog.meredithmcghan.com
	# This redirect is not a named URL because we are going to a subdomain, better to link direct...

	url(r'^blog$', redirect_to, {'url': 'http://blog.meredithmcghan.com'}),

	#
	# meredithmcghan.com/technical/*
	#

	url(r'^technical$', direct_to_template, {'template': 'technical.html'}, name='technical'),
	url(r'^technical/voting-restoration$', redirect_to, {'url': 'http://meredithmcghan.com/media/documents/technical/voting-restoration-nevada-2008.pdf'}, name='voting_restoration'),
	url(r'^technical/carpentry$', 'carpentry_gallery', name='carpentry_gallery'),  # Gallery

	#
	# meredithmcghan.com/marketing/*
	#

	url(r'^marketing$', direct_to_template, {'template': 'marketing.html'}, name='marketing'),
	url(r'^marketing/social-light$', 'scanned_articles', {'paths': ['marketing/social-light']}, name='social_light'),
	url(r'^marketing/etsy-artists$', 'scanned_articles', {'paths': ['marketing/etsy-artists-1', 'marketing/etsy-artists-2']}, name='etsy_artists'),
	url(r'^marketing/pumpkin-spa$', 'scanned_articles', {'paths': ['marketing/pumpkin-spa-1', 'marketing/pumpkin-spa-2']}, name='pumpkin_spa'),
	url(r'^marketing/be-magazine$', 'scanned_articles', {'paths': ['marketing/be-cover', 'marketing/faith-fearlessness', 'marketing/practice-perfect']}, name='be_magazine'),
	url(r'^marketing/industry-women$', 'scanned_articles', {'paths': ['marketing/industry-women-1', 'marketing/industry-women-2']}, name='industry_women'),
	url(r'^marketing/sandy-campbell$', 'scanned_articles', {'paths': ['marketing/sandy-campbell']}, name='sandy_campbell'),
	url(r'^marketing/poker$', 'poker_gallery', name='poker_gallery'), # Gallery...

	#
	# meredithmcghan.com/journalism/*
	#

	url(r'^journalism$', direct_to_template, {'template': 'journalism.html'}, name='journalism'),
	url(r'^journalism/less-than-zero$', 'scanned_articles', {'paths': ['journalism/less-than-zero']}, name='less_than_zero'),
	url(r'^journalism/at-what-cost$', 'scanned_articles', {'paths': ['journalism/at-what-cost']}, name='at_what_cost'),
	url(r'^journalism/fake-news$', direct_to_template, {'template': 'journalism/fake-news.html'}, name='fake_news'),
	url(r'^journalism/greening-vegas$', 'scanned_articles', {'paths': ['journalism/greening-vegas']}, name='greening_vegas'),

	# The cover stories are in the gallery, should they each get their own separately addressable URL?
	# e.g. url(r'^journalism/sprawl$', 'xxx', name='sprawl'),
	url(r'^journalism/cover-stories$', 'cover_stories_gallery', name='cover_stories_gallery'), # Gallery....

	#
	# meredithmcghan.com/entertainment/*
	#

	url(r'^entertainment$', direct_to_template, {'template': 'entertainment.html'}, name='entertainment'),
	url(r'^entertainment/radiskull$', direct_to_template, {'template': 'entertainment/radiskull.html'}, name='radiskull'),
	url(r'^entertainment/almost-freaky$', 'scanned_articles', {'paths': ['entertainment/almost-freaky']}, name='almost_freaky'),
	url(r'^entertainment/whats-on$', 'whats_on_gallery', name='whats_on_gallery'), # Gallery...

	#
	# meredithmcghan.com/commentary/*
	#

	url(r'^commentary$', direct_to_template, {'template': 'commentary.html'}, name='commentary'),
	url(r'^commentary/flint$', 'scanned_articles', {'paths': ['commentary/flint']}, name='flint'),
	url(r'^commentary/ta-confessions$', 'scanned_articles', {'paths': ['commentary/ta-confessions']}, name='ta_confessions'),
	url(r'^commentary/slant$', 'slant_gallery', name='slant_gallery'), # Gallery...

	#
	# meredithmcghan.com/creative/*
	#

	url(r'^creative$', direct_to_template, {'template': 'creative.html'}, name='creative'),
	url(r'^creative/waiting-bus$', 'scanned_articles', {'paths': ['creative/waiting-bus']}, name='waiting_bus'),
	url(r'^creative/perspectives$', 'perspectives_gallery', name='perspectives_gallery'), # Gallery...
	url(r'^creative/branding$', 'branding_gallery', name='branding_gallery'), # Gallery...
	
	#
	# meredithmcghan.com/advocacy/*
	#
	url(r'^advocacy/outreach$', direct_to_template, {'template': 'advocacy/outreach.html'}, name='nonprofit_outreach'),

	#
	# meredithmcghan.com/for-sale/*
	#
	url(r'^for-sale/2005-saturn-ion$', direct_to_template, {'template': 'for-sale/2005-saturn-ion.html'}, name='for_sale_2005_saturn_ion'),
	
	#
	# experiment
	#

	url(r'^experiment\.php/(?P<number>\d{4})/$', 'experiment'),
)
