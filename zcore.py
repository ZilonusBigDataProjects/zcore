#!/usr/bin/env python
import gevent.monkey
gevent.monkey.patch_all()
import psycogreen.gevent
psycogreen.gevent.patch_psycopg()

import zilonus

if __name__ == "__main__":
    zilonus.core.main()

