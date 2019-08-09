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

## Change the Server Address

TODO

## Get the Sensor's Symmetric Key

TODO

## Convert Readings from Raw Values to SI Units

TODO
