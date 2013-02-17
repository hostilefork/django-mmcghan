# This is an example Apache configuration file for configuring a site to
# serve meredithmcghan.com.  It should be placed in the directory:
#
#     /etc/apache2/sites-enabled

# Should be able to just say *:80 but that is unpredictable...
# http://www.webmasterworld.com/apache/3282118.htm
<VirtualHost 72.249.123.186:80>
        ServerAdmin meredithmcghan@gmail.com
        DocumentRoot /var/www/meredithmcghan.com/
        ServerName meredithmcghan.com
#        ServerAlias www.meredithmcghan.com

        <Directory /var/lib/awstats>
                Options None
                AllowOverride None
                Order allow,deny
                Allow from all
        </Directory>

        <Directory /usr/share/awstats/icon>
                Options None
                AllowOverride None
                Order allow,deny
                Allow from all
        </Directory>

	<Location "/">
		SetHandler python-program
		PythonHandler django.core.handlers.modpython
		SetEnv DJANGO_SETTINGS_MODULE project.settings
# http://groups.google.com/group/django-users/browse_thread/thread/de96ca3a50c372f3
#		PythonOption django.root /
# You need both these in your python path to find meredithmcghan.settings
# (for instance) as well as any django apps you put under the directory
		PythonPath "['/var/www/meredithmcghan.com/','/var/www/meredithmcghan.com/project/'] + sys.path" 
		PythonDebug On
	</Location>

	#
	# "Django doesn't serve media files itself; it usually expects you to have
	# a different webserver serving these files. In our case though, we 
	# want Apache to handle it, so we need to turn off mod_python for some 
	# parts of the site."
	#
	# http://jeffbaier.com/articles/installing-django-on-an-ubuntu-linux-server/
	#
	<Location "/media">
		SetHandler None
	</Location>
	<Location "favicon.ico">
		SetHandler None
	</Location>
	<Location "/libs">
		SetHandler None
	</Location>
	<Location "/admin_media">
		SetHandler None
	</Location>
	<Location "/phpmyadmin">
		SetHandler None
	</Location>
	<locationmatch ".(jpg|gif|png)$">
		SetHandler None
	</Locationmatch>


        Alias /awstats-icon/ /usr/share/awstats/icon/
        ScriptAlias /stats /usr/lib/cgi-bin/awstats.pl
        ScriptAlias /awstats.pl /usr/lib/cgi-bin/awstats.pl

        ErrorLog /var/www/meredithmcghan.com/logs/error.log
        CustomLog /var/www/meredithmcghan.com/logs/access.log common
        CustomLog /var/www/meredithmcghan.com/logs/access-combined.log combined
</VirtualHost>
