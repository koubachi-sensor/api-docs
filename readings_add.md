# smart\_devices/readings/add

Store a series of sensor readings for the given smart device.

## Request

  - Path: **/v1/smart_devices/:mac_address/readings**
  - Alternative
    Path: **/smart_devices/:mac_address/readings**
  - HTTP Method: **POST**
  - Request Format: JSON ([encrypted](encryption.md))

### Parameters

  - **Required:** -
  - **Optional:** -

### Body ([encrypted](encryption.md))

**Required:**

  - **timestamp**: Timestamp (UNIX time), indicating when the message
    was sent.
  - **readings**: Sensor readings as nested array, with inner array in
    the format `[timestamp (UNIX time), sensor_type_id, raw_value]`

**Optional: -**

## Response ([encrypted](encryption.md))

Returns HTTP status code 201 on success. In case of failure, any other
code (and possibly error information in JSON format) on error are
returned.

**Note:** A status code 201 does not guarantee that the readings were
added; in the future, the implementation may change so the server
immediately answers with 201 Created and adds the readings later (which
may then fail silently).

Response format: **urlencoded**

Content of response:

Always:

  - **current\_time** - timestamp for current UNIX time
  - **last\_config\_change** - timestamp of last config change on server

## Example

### Request

  - **PUT**
    `http://api.example.com/smart_devices/0123cafebabe/readings`
  - **Accept:** `application/x-www-form-urlencoded`
  - **Content-Type:** `application/x-koubachi-aes-encrypted`
  - **Body (after decryption):**
    `{'timestamp': 123456789, 'readings': [[123123123, 1, 7], [123123124, 1, 7], [123123125, 1, 8]]}`

### Response

  - `HTTP/1.1 201 Created`
  - **Body (after decryption):**
    `current_time=123456789&last_config_change=123456780`
