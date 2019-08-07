# smart\_devices/readings/add

Store a series of sensor readings for the given smart device.

## Request

  - URL: **http://api.koubachi.com/v1/smart\_devices/:mac\_address/readings**
  - Alternative
    URL: **http://api.koubachi.com/smart\_devices/:mac\_address/readings**
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
    the format `\[timestamp (UNIX time), sensor\_type\_id, raw\_value\]`

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
    `http://api.koubachi.com/smart\_devices/0123cafebabe/readings`
  - **Accept:** `application/x-www-form-urlencoded`
  - **Content-Type:** `application/x-koubachi-aes-encrypted`
  - **Body (after decryption):**
    `{'timestamp': 123456789, 'readings': \[\[123123123, 1, 7\], \[123123124, 1, 7\], \[123123125, 1, 8\]\]}`

### Response

  - `HTTP/1.1 201 Created`
  - **Body (after decryption):**
    `current\_time=123456789\&last\_config\_change=123456780`
