# Koubachi Sensor API Documentation

## Server API

The communication between the sensor and the server is encrypted. Read
more about the [encryption](encryption.md) or see a [Python code
example](encryption_code_example.py).

A server must implement three endpoints:

* [update](update.md) - Intended to be used to associate a sensor with a
  user account, used by the config app to test the connection.
* [config_show](config_show.md) - Used by the sensor to retrieve its
  configuration, e.g. which sensors are enabled, how often to measure
  and how often to transmit stored readings.
* [readings_add](readings_add.md) - Used by the sensor to transmit its
  stored readings.

## Change the Sensor's Server Address

1. Press the sensor's button for at least 3 seconds, until the LED turns and
   stays orange.
1. Connect to the sensor's config Wi-Fi and open the configuration page in your
   browser <http://172.29.0.1/> to see if the connection works.
1. Then change the URL in your browser's address bar to
   `http://172.29.0.1/sos_config?host=api.example.com&port=8005` with your
   desired host and port. The host can be a hostname or an IPv4 address.
1. Goto <http://172.29.0.1/> and enter the WIFI credentials and any user
   credentials (these are not used, but required for the connection to be
   setup) and click 'connect'.

To get your current configuration visit <http://172.29.0.1/sos_config>.

This setting is lost after a factory reset.

## Get the Sensor's Symmetric Key

Write an e-mail to [sensors@koubachi.com](mailto:sensors@koubachi.com) and
mention the MAC addresses of your sensors. Within a few days we will reply with
the symmetric keys and calibration data.

# Third-Party Server Implementations

* [Implementation in Python 3](https://github.com/koalatux/koubachi-pyserver)
