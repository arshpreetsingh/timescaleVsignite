# timescaleVsignite

## Start timescale Docker
```
docker run -d --name timescaledb -p 5432:5432 -e POSTGRES_DB=relay -e POSTGRES_USER=maropost -e POSTGRES_PASSWORD=Maro123! timescale/timescaledb:latest-pg11
```

Run TimeScale insert command:

python insert_data_timescale.py

## start Ignite docker 

```
docker run -it --net=host -e "CONFIG_URI=https://raw.githubusercontent.com/apache/ignite/master/examples/config/example-cache.xml" apacheignite/ignite
```
Run ApacheIgnite insert command:

python insert_data_ignite.py
