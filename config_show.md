# smart\_devices/config/show

Get a description of the current smart device configuration.

## Request

  - Path: **/v1/smart_devices/:mac_address/config**
  - Alternative
    Path: **/smart_devices/:mac_address/config**
  - HTTP Method: **POST**
  - Request Format: JSON ([encrypted](encryption.md))

### Parameters

  - **Required:** -
  - **Optional:** -

### Body ([encrypted](encryption.md))

**Required:**

  - **timestamp**: Timestamp (UNIX time), indicating when the message
    was sent.
  - **last\_config\_update**: Timestamp of last config update or 0
    (zero) to get all configuration variables.
  - **current\_firmware\_release\_version**: Version of firmware
    currently used on node.

**Optional:** -

## Response ([encrypted](encryption.md))

On success, returns HTTP status code 200 and the configuration
variables, which have been changed, in the body. In case of failure, any
other code (and possibly error information in JSON format) on error are
returned.

Response format: **urlencoded**

Content of response:

Always:

  - **current\_time** - timestamp for current UNIX time

If it has changed:

  - **transmit\_interval** - indicates at which interval (in seconds) to
    transmit readings
  - **sensor\_enabled\[*sensor\_type\_id*\]** - whether the sensor with
    the given sensor\_type\_id is enabled (0/1)
  - **sensor\_polling\_interval\[*sensor\_type\_id*\]** - polling
    interval (in seconds) for sensor\_type with given ID

## Example

### Request

  - **POST** `http://api.example.com/smart_devices/0102ababab/config`
  - **Accept:** `application/x-www-form-urlencoded`
  - **Content-Type:** `application/x-koubachi-aes-encrypted`
  - **Body (after decryption):**
    `{'timestamp': 123456789, 'last_config_update': 123456000, 'current_firmware_release_version': 2}`

### Response

  - `HTTP/1.1 200 OK`
  - **Body (after decryption):**
    `current_time=123456789&transmit_interval=86400`
