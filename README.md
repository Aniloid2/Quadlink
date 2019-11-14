# Quadlink

Your quadcopter will post asynchronously to a remote database, this can be done with a data dongle or wifi connection. Because the data is updated continuously and stored, any user with the right credentials can connect to the remote database and access the most up to date data. The data will also update real-time to every connected user.

![Screenshot](telemetry.png)

Set up the QuadJavelin on your Raspberry Pi, enter the right parameters { username password Number_of_threads }, connect to https://quadlink.herokuapp.com. To connect to correct quadcopter type the username and password. Run turn_on.sh to show acceleration, throttle output and x y z coordinates.
