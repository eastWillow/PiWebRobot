# PiWebRobot
Using UV4L For Video Boardcasting and Flask.py For Web GPIO Contorl

# Requirements
* [uv4l-webrtc](https://www.linux-projects.org/uv4l/installation/)
* [flask](http://mattrichardson.com/Raspberry-Pi-Flask/)

# Install
1. Please Install All Requriment Package above
2. Copy **/html/SimpleWebRTC.html** to **/usr/share/uv4l/www/SimpleWebRTC.html**
3. Copy **/flask_GPIO** to **/home/pi/Documents/python/**

# Change UV4L Setting

```Shell Session
sudo nano /etc/uv4l/uv4l-raspicam.conf
```

```Bash
--------------another line-------------
server-option = --port=8080
---------------another line-----------
server-option = --enable-www-server=yes
# server-option = --www-root-path=/usr/share/uv4l/www/
server-option = --www-index-file=SimpleWebRTC.html
server-option = --www-port=80
```

# Making flask_GPIO to Autoexecute On Boot

1. cd init.d
```Shell Session
cd /etc/init.d
sudo -E vim flask.sh
```

2. Edit flask.sh

```Bash
#!/bin/sh
# /etc/init.d/flask.sh

case "$1" in
  start)
    echo "StartFlask"
    nohup python /home/pi/Documents/python/flask_GPIO/flask-gpio.py &
    ;;
  stop)
    echo "StopFlask"
    killall python
    ;;
  *)
    echo "Usage /etc/init.d/flask.sh{start|stop}"
    exit 1
    ;;
esac

exit 0
```

3. Setting Autoexecute

```Shell Session
sudo update-rc.d flask.sh defaults
```
