# smart\_device/update

Update smart device attributes.

**NOTE:** If the parameters include valid user credentials, the smart
device will be associated with the corresponding user.

## Request

  - URL: **http://api.koubachi.com/v1/smart_devices/:mac_address**
  - Alternative
    URL: **http://api.koubachi.com/smart_devices/:mac_address**
  - HTTP Method: **PUT**
  - Request Format: JSON ([encrypted](encryption.md))

### Parameters

  - **Required:** -
  - **Optional:** -

### Body ([encrypted](encryption.md))

**Required:**

  - **timestamp**: Timestamp (UNIX time), indicating when the message
    was sent.

**Optional:**

  - **user\_credentials** or **email** and **password**: The necessary
    data to associate a smart device with an user account.

## Response ([encrypted](encryption.md))

Response format: **urlencoded**

Return Value:

If update is ok, this call returns HTTP status code 200.

If user credentials are given, but the user is not valid, this call
returns HTTP status code 404. In this case this method will return the
following error description: `[["login","is invalid"]]`.

If the MAC address can not be found, this call returns HTTP status code
404. In this case this method will return the following error
description: `[["MAC","is invalid"]]`.

  - **IMPORTANT**: Since there is no known symmetric key in this case,
    the answer is not encrypted/authenticated.

## Example

### Request

  - **PUT** `http://api.koubachi.com/smart_devices/aa11bb22cc33`
  - **Accept:** `application/x-www-form-urlencoded`
  - **Content-Type:** `application/x-koubachi-aes-encrypted`
  - **Body (after decryption):**
    `{'timestamp': 123456789, 'email': 'foo@example.com', 'password': 'foobar'}`

### Response

  - `HTTP/1.1 200 OK`
  - **Body (after decryption):**
    `current_time=123456789&last_config_change=123456789`
