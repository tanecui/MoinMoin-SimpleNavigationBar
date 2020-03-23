# -*- coding: iso-8859-1 -*-
"""
    MoinMoin - Create Simple Navigation Bar

    @copyright: 2020 Tane Cui <two_monsters@hotmail.com>
    @license: GNU GPL, see COPYING for details.
"""

Dependencies = ['namespace']

from MoinMoin.action import LikePages
from MoinMoin import wikiutil
from MoinMoin.parser.text_moin_wiki import Parser as WikiParser

def macro_NavigationBar(macro):
    request = macro.request
    # we don't want to spend much CPU for spiders requesting nonexisting pages
    if not request.isSpiderAgent:
        pagename = macro.formatter.page.page_name
        navs = pagename.split("/")
        navigationbar = ""
        path = ""
        for nav in navs:
            if path == "":
                path = nav
            else:
                path = path+ "/"+nav
            encrypted = " [[%s|%s]] >> " % (path,nav)
            navigationbar = navigationbar + encrypted
        navigationbar = navigationbar[:-4]
        # Get matches
        #start, end, matches = LikePages.findMatches(pagename, request)

        # Render matches
        #if matches and not isinstance(matches, (str, unicode)):
         #   return request.redirectedOutput(LikePages.showMatches, pagename, request, start, end, matches, False)
        #else:
            # if we did not find any similar pages, we just render the text we got as argument:
         #   return request.formatter.text(text)
    # bots get nothing:
    return wikiutil.renderText(request,WikiParser,navigationbar)
