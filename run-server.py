#! /usr/bin/env python

from trace_collector import app

app.run(threaded=True, host='0.0.0.0')
