#!/usr/bin/env python
import gevent.monkey
gevent.monkey.patch_all()
import psycogreen.gevent
psycogreen.gevent.patch_psycopg()

# All python modules will be inside zilonus dir
import zilonus

if __name__ == "__main__":
    zilonus.core.main()

