"""
    urlresolver XBMC Addon
    Copyright (C) 2011 anilkuj

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import re
from t0mm0.common.net import Net
import urllib2
from urlresolver import common
from urlresolver.plugnplay.interfaces import UrlResolver
from urlresolver.plugnplay.interfaces import PluginSettings
from urlresolver.plugnplay import Plugin

class VeohResolver(Plugin, UrlResolver, PluginSettings):
    implements = [UrlResolver, PluginSettings]
    name = "veoh"

    def __init__(self):
        p = self.get_setting('priority') or 100
        self.priority = int(p)

    def get_media_url(self, host, media_id):
        
        print 'host %s media_id %s' %(host, media_id)
##        url = 'http://www.veoh.com/rest/video/'+media_id+'/details'
##        html = net.http_GET(url).content
##        if html == "<error>"
##            print 'coult not obtain video url'
##            return False
##        file = re.compile('fullPreviewHashLowPath="(.+?)"').findall(html)
##        if len(file) == 0
##            print 'coult not obtain video url'
##            return False

        html = net.http_GET("http://www.veoh.com/iphone/views/watch.php?id=" + media_id + "&__async=true&__source=waBrowse")
        if re.search('This video is not available on mobile', html):
            print 'could not obtain video url'
            return False

        re.compile("watchNow\('(.+?)'").findall(html)
	if (len(re) > 0 ):
            return re[0]

        print 'could not obtain video url'
        return False


    def get_url(self, host, media_id):
        return 'http://veoh.com/watch/%s' % media_id


    def get_host_and_id(self, url):
        r = None
        video_id = None
        
        if re.search('permalinkId=', url)
            r = re.compile('permalinkId=(.+?)').findall(url)
        elif re.search('watch/', url)
            r = re.compile('watch/(.+?)').findall(url)
            
        if r is not None and len(r) > 0:
            video_id = r[0]
            
        if video_id:
            return ('veoh.com', video_id)
        else:
            common.addon.log_error('veoh: video id not found')
            return False

    def valid_url(self, url, host):
        return re.match('http://(.+)?veoh.com/[0-9]+',
                        url) or 'veoh' in host

    def get_settings_xml(self):
        xml = PluginSettings.get_settings_xml(self)
        xml += '<setting label="This plugin calls the veoh addon - '
        xml += 'change settings there." type="lsep" />\n'
        return xml
