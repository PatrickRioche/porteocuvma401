#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bottle

@bottle.route("/hello")
@bottle.view("page.tpl")
def hello() :

    stri = "Hello Porte Oculaire VMA401"

    return {"title":"Porte Oculaire VMA401", "body" : stri}

bottle.run(bottle.app(), host='0.0.0.0', port=8080, debug= True, reloader=True)
