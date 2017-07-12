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
