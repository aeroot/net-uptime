import datetime
import time

import ping

import MySQLdb

# User configurable settings

MYSQL_HOST = "localhost"
MYSQL_USER = "net-uptime"
MYSQL_PASSWORD = "net-uptime"
MYSQL_DB = "net-uptime"

ROUTER_IP = "192.168.51.1"
CARRIER_ROUTER_IP = "192.168.1.1"
RECORD_INTERVAL_SECS = 30

PING_SITES = [
        "google.com",
        "yahoo.com",
        ]

# End settings

db = MySQLdb.connect(host=MYSQL_HOST,
                     user=MYSQL_USER, 
                     passwd=MYSQL_PASSWORD, 
                     db=MYSQL_DB)
cur = db.cursor();

pings = [ping.Ping(hn, 1000, 55, print_stats=False) for hn in PING_SITES]
rp = ping.Ping(ROUTER_IP, 55, print_stats=False)
crp = ping.Ping(ROUTER_IP, 55, print_stats=False)

#with open(LOG_FILENAME, "w") as lf:
while True:
    successes = [False for p in PING_SITES]
    for i,p in enumerate(pings):
        p.run(1)
        if p.send_count == p.receive_count:
            successes[i] = True

    # if all false
    internet = 1
    router = 1
    carrier_router = 1

    if all((not a for a in successes)):
        internet = 0

    rp.run(1)
    if rp.send_count != rp.receive_count:
        router = 0

    crp.run(1)
    if crp.send_count != crp.receive_count:
        carrier_router = 0



    # log this run
    cur.execute("INSERT INTO uptimelog (time, router, carrier_router, internet) VALUES (NOW(),%s, %s, %s)", (router, carrier_router, internet))
    db.commit()

    time.sleep(RECORD_INTERVAL_SECS)
