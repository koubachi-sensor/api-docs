# Encryption and Authentication for SmartDevices

The body of all HTTP requests from nodes to the server and the body of
the server response are encrypted and authenticated by using AES + CRC.

**NOTE:** For calls requiring CRC type of authentication, you must
**always include the MAC address in the URL** (e.g.
api.koubachi.com/smart\_devices/aabbccddeeff) and a timestamp (UNIX
time), indicating, when the message was sent, in the body.

## Key distribution

Symmetric 128 bit AES keys are distributed to the nodes and the server
during the production phase. Each key corresponds to one MAC address.

## Identification

The nodes are identified by their MAC address, which is sent as plain
text in the URL of each HTTP request.

## Header / Content-Type

AES encrypted packets use the custom content type
application/x-koubachi-aes-encrypted (non-standard, unregistered):

`Content-Type: application/x-koubachi-aes-encrypted`

See also: RFC 2045, RFC 4288

## Content

The original content consists of valid JSON data.

## Padding

If necessary (to achieve 128-bit block size), the payload is zero-padded
(up to the last 4 bytes, which are reserved for the CRC). Since the
receiving side has to remove all zeros after decryption, the content
must not end with a zero byte.

## Payload

The payload consists of the complete request body, i.e. content (e.g.
JSON), padding and CRC.

## Authentication

Authentication is achieved by adding a 4 byte CRC (CRC32, as specified
in IEEE 802.3) at the end of the payload (after the padding), before
encrypting it. If the server determines that the CRC is correct after
decrypting the payload, the current request is authenticated.

## Encryption

The payload is encrypted using symmetric 128-bit AES encryption. The
server can determine the symmetric key by looking up the MAC address.

## Initialisation Vector

Since the AES-CBC implementation on the node does not allow the use of
an initialisation vector (IV), the first block is always encrypted the
same way (i.e. identical plaintext always results in the same
ciphertext, as if using ECB mode). To circumvent this problem, we always
add 16 byte random data as the first block of the payload.

The receiving side can either decrypt the whole payload and throw away
the first 16 bytes afterwards, or, due to the way CBC works, the first
16 bytes in the ciphertext can be considered as the IV and the
decryption can start at the 17th byte (i.e. the first 16 bytes never
have to be decrypted).

**Important:** The random data is ignored for the calculation of the
CRC.

## Example

`\[16 byte random data\]{'timestamp':1234567890,'foo':'bar'}\[Zero-padding to make message size a multiple of 16 bytes\]\[4-byte CRC\]`

# Encryption and Authentication of the Server

The response is encrypted and authenticated the same way as the requests
from the node, except for the differences described below.

## Payload

The payload consists of the HTTP response body (the headers are not
encrypted). If the body is otherwise empty (such as in 200 OK and 201
Created responses), the server always sends a current time stamp and the
time of the last configuration change as the answer.

## Initialisation Vector

The server chooses a 16 byte random IV, which is sent in plain as the
first 16 bytes of the encrypted body. Note that this is only a formal
difference from the way the node creates packets, and has the same
practical results. Again, the receiving side can either use the first 16
bytes as IV or decrypt the whole packet using any IV (e.g. all zero as
the AES function in the node library) and throw away the first 16
decrypted bytes.

## Example

```
HTTP 200 OK
Content-Type: application/x-koubachi-aes-encrypted
\[More unencrypted headers\]

\[16 byte random IV (not encrypted)\]\[4 byte UNIX time stamp\]\[8 byte zero padding\]\[4 byte CRC\]
```
