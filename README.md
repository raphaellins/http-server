## Http Server using Turq running in Docker


### How to use



1. This command will run docker compose and start a Turq Http Server with a initital mock `mock.py`.
```
$ ./start.sh
```

2. This command will delete the container created previous
```
$ ./stop.sh
```

After start the script, will be available a http://localhost:13086 where we can edit the mocks, and in http://localhost:13085 it's our Http Server up 
