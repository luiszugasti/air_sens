# Air Sensor

This Repo contains code for the Arduino IOT Thing as well as the Raspberry
client. 

Please check out the [instructable](https://www.instructables.com/id/Track-Air-Quality-Using-Grafana-and-Raspberry-Pi/) for further instructions.

## Raspberry Client

Python code to run on the Raspberry Pi. It's a simple loop that collects data
from the Arduino and sends it to an MQTT broker. Default values can be changed
by setting the appropriate environment variable using $variable=TEST syntax on
the Raspberry Pi.

## Arduino Thing

The code is written for four connections on pins A2 thru A5 - if you'll be using
less (or more) sensors, feel free to add/remove pins as required.

The Arduino communication uses the Serial connection via USB and is formatted
as GET parameters - this simplifies writing a regular expression on the
Raspberry Pi.

## Next steps

I'd like to publish the sensor to a cloud instance and post guides for doing
that in Google Cloud as well as AWS - this way, we can get rid of the Raspberry
pi completely and use a lightweight board such as the ESP8266/32 and use the
Arduino separately.

## Credits

Thanks to Charles for inspiring me for this project.
