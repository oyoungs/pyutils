# Python utils

## ByteArray

Process number and byte buffer

### usage:
```python
from pyutils.bytes import ByteArray

if __name__ == '__main__':
    a = ByteArray()
    a.write_int8(-1)
    a.write_uint32_le(1000)
    a.write_float_le(50)
    a.write_double_le(100)
    print (a)
    print (a.read_uint8())
    print (a.read_uint32_be(1))
    print (a.read_float_be(5))
    print (a.read_double_be(9))

```