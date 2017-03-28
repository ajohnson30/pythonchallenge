Content-Transfer-Encoding: 8Bit

Content-Disposition: attachment; filename="cookiecontainer.py"



#!/usr/bin/env python

"""

CookieContainer



This object stores and retrieves cookies IAW RFC 2109 & RFC 2068



$Id: cookiecontainer.py,v 1.8 2001/06/08 12:12:37 cvsuser Exp $

"""

__author__="""

Downright Software LLC

http://www.downright.com

"""

__copyright__="""

Copyright (c) 2000 Downright Software LLC. All Rights Reserved.



Distributed and Licensed under the provisions of the WebNudge

Open Source License (Version 1.0) which is included by reference.



The WebNudge Open Source License can be found in the file WOSLV10.TXT

in the source distribution kit.

"""

__version__="$Revision: 1.8 $"[11:-2]



import re

import time

import urlparse

import string



import webnudge.util.misc

        

def CookieContainerException(Exception):

    def __init__(self, message):

        self._message = message

    def __str__(self):

        return self._message



###########################################################

class CookieContainer:

###########################################################

    """

    This object stores and retrieves cookies IAW RFC 2109 & RFC 2068 

    """



    #----------------------------------------------------------

    def __init__(self, listelement=None):

    #----------------------------------------------------------

        """

        Constructor

        """

        self._cookiedict = {}



        # Match dates  of this form:

        # Monday, 05-Feb-2001 08:00:00 GMT

        self._DatePattern = re.compile(r"""

            (?P<weekday>               # Start of group 'weekday'

            [A-za-z]+                  # Any word of at least one letter

            )                          # End of group 'weekday'

            \s*\,\s*                   # a literal comma after weekday

            (?P<day>                   # Start of group 'day'

            \d\d                       # two digits

            )                          # End of group 'day'

            -                          # literal hyphen 

            (?P<month>                 # Start of group 'month'

            [A-za-z]+                  # three letters

            )                          # End of group 'month'

            -                          # literal hyphen 

            (?P<year>                  # Start of group 'year'

            \d+                        # some digits

            )                          # End of group 'year'

            \s+                        # a space or more

            (?P<hour>                  # Start of group 'hour'

            \d\d                       # two digits

            )                          # End of group 'hour'

            :                          # a colon

            (?P<minute>                # Start of group 'minute'

            \d\d                       # two digits

            )                          # End of group 'minute'

            :                          # a colon

            (?P<second>                # Start of group 'second'

            \d\d                       # two digits

            )                          # End of group 'second'

            \s+                        # some whitespace

            GMT                        # literal 'GMT

            """, re.VERBOSE | re.IGNORECASE)



        self._DateFormat = "%4d-%2s-%2s %2s:%2s:%2s" # yyyy-mm-dd hh:mm:ss

        self._MonthDict = {

            "jan" : "01",

            "feb" : "02",

            "mar" : "03",

            "apr" : "04",

            "may" : "05",

            "jun" : "06",

            "jul" : "07",

            "aug" : "08",

            "sep" : "09",

            "oct" : "10",

            "nov" : "11",

            "dec" : "12"

            }



    #----------------------------------------------------------

    def __str__(self):

    #----------------------------------------------------------

        """

        Report ourself as a string

        """

        return str(self._cookiedict)

        

    #----------------------------------------------------------

    def isempty(self):

    #----------------------------------------------------------

        """

        Report presence of cookies

        """

        return not self._cookiedict



    #----------------------------------------------------------

    def clear(self):

    #----------------------------------------------------------

        """

        Empty out the cookies

        """

        self._cookiedict.clear()



    #----------------------------------------------------------

    def loadFromHeaders(self, defaultdomain, headers):

    #----------------------------------------------------------

        """

        Extract 'set-cookie' from headers from RawHTMLPage

        Return a count of the new cookies added

        """

        count = 0

        

        cookieheaderlist = headers.getallmatchingheaders("set-cookie")

        for cookieheader in cookieheaderlist:

            cookie = {

                "domain" : defaultdomain,

                "path" : "/",

                "secure" : "no"

                }

            

            # split on ';' after dropping 'set-cookie:'

            tokenlist = string.split(cookieheader[12:],";")

            

            # assume name is the  first token

            token =  string.strip(tokenlist[0])

            index = string.find(token, "=")

            if index <= 0:

                continue

            cookie["name"] = token[:index]

            cookie["value"] = token[index+1:]

            

            for token in tokenlist[1:]:

                # split on the first '=', except for secure

                token = string.strip(token)

                if token == "secure":

                    cookie["secure"] = "yes"

                    continue

                index = string.find(token, "=")

                if index <= 0:

                    continue

                key = string.lower(token[:index])

                value = token[index+1:]

                if key == "expires":

                    cookie[key] = self._convertExpirationDate(value)

                else:

                    cookie[key] = value

            self._cookiedict[cookie["name"]] = cookie

            count = count + 1



        return count



    #----------------------------------------------------------

    def returnCookieList(self, url):

    #----------------------------------------------------------

        """

        Return a list of name:value tuples for cookies that

        fit the url

        """

        scheme,netloc,path,parameters,query,fragment = urlparse.urlparse(

            url

            )

        returnlist = []

        for cookie in self._cookiedict.values():

            if len(netloc) < len(cookie["domain"]):

                continue

            # The url must be in the domain the cookie specifies

            if netloc[len(netloc)-len(cookie["domain"]):] != cookie["domain"]:

                continue

            # the path must include the path the domain specifies

            if path and string.find(path, cookie["path"]) != 0:

                continue

            # if we have an expiration date, check for it

            expirationdate = cookie.get("expires", None)

            if expirationdate and expirationdate <= time.time():

                continue

            returnlist.append((cookie["name"],cookie["value"]))



        return returnlist



    #----------------------------------------------------------

    def _convertExpirationDate(self, value):

    #----------------------------------------------------------

        """

        convert a date string of the form

        'Dayofweek, dd-mmm-yyyy hh:mm:ss GMT'

        into a python date.

        """

        # look for a date we can understand

        match = self._DatePattern.search(value)

        if not match:

            return None



        # allow for a two digit year

        # redhat is one of the offenders

        if len(match.group("year")) == 4:

            year = int(match.group("year"))

        else:

            year = 2000 + int(match.group("year"))



        # 32 bit unix time chokes after 2038

        year = min(2037, year)

            

        # kludge alert!  I can't find a slick way to convert

        # this date, so I'm going to convert it to our database

        # format and use code that I know works

        datestr = self._DateFormat % (

            year,

            self._MonthDict[string.lower(match.group("month"))],

            match.group("day"),

            match.group("hour"),

            match.group("minute"),

            match.group("second"),

            )



        return webnudge.util.misc.strtime(datestr)

        

#----------------------------------------------------------

if __name__ == "__main__":

#----------------------------------------------------------

    """

    Code for commandline testing

    """

    import sys

    if len(sys.argv) != 2:

        print "Usage: cookiecontainer.py <url>"

        sys.exit(-1)



    cookiecontainer = CookieContainer()



    import webnudge.util.rawhtmlpage

    page = webnudge.util.rawhtmlpage.RawHTMLPage()

    page.load(sys.argv[1], "GET", [], cookiecontainer, debuglevel=1)

    if not page:

        print "*** Error *** %s" % (page._message)

        sys.exit(-1)



    print "*" * 30

    print page._data

    print "*" * 30



    print "cookie dict"

    for key, value in cookiecontainer._cookiedict.items():

        sys.stdout.write("%s = %s\n" % (key, value))



    print "cookies returned"

    for item in page._cookiesreturned:

        print item

