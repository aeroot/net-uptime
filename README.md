Network uptime monitor
======================

This script monitors your network connection by pinging several websites. The results are logged in a MySQL database.

Preparation
-------

To prepare the script to run, you have to edit the settings part of the *net-uptime.py* at to top of the file so that it fits your MySQL settings (host, user, password, database) and your router. The carrier_router can be used for complexer networks like when there is a carrier-grade NAT (so when your NAT is behind a NAT within the provider network) to find out where the connection is broken.

Be sure, that the python module *MySQLdb* is installed. It is needed for the connection to the MySQL database. The database should contain the table defined in *create-db-structure.sql*.

Run
---

Simply run the *net-uptime.py* script with root/administrator rights.

```sh
python net-uptime.py
```

Why do I need this?
-------------------

Probably not al all. When you have an instable internet connection you can for example use it to monitor the percentual uptime to check SLAs. However it is not suited to handle the monitoring for enterprise purposes. It works well in a home environment (e.g. on a Raspberry Pi or another server-like system that runs anyway in your network for some reason).

When there is enough time, I will develop a simple (web-)interface to vizualize the collected data in a proper way.

Notes
----

Note that because it uses a pure Python implementation of ping, you must run the script as root/Administrator.
There is no exception/error handling at all. When the script crashes, it simply crashes without any alert.