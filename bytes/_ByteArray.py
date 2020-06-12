import struct


class ByteArray(object):

    def __init__(self, items=None):
        if isinstance(items, bytearray):
            self.items = items
        elif isinstance(items, bytes) or isinstance(items, list):
            self.items = bytearray(items)
        else:
            self.items = bytearray()

    def __str__(self):
        return list(self.items).__str__()

    def to_str(self, size=None, pos=0):
        if size is None:
            size = len(self.items) - pos
        return str(self.items[pos:pos + size])

    def to_bytes(self, size=None, pos=0):
        if size is None:
            size = len(self.items) - pos
        return bytes(self.items[pos:pos + size])

    def to_list(self, size=None, pos=0):
        if size is None:
            size = len(self.items) - pos
        return list(self.items[pos:pos + size])

    def to_hex(self, split='', uppercase=False):
        h = split.join([hex(i)[2:].zfill(2) for i in self.items])
        return h.upper() if uppercase else h

    def read_number(self, fmt, size, pos=0):
        return struct.unpack(fmt, self.to_str(size, pos))[0]

    def read_int8(self, pos=0):
        return int(self.items[pos])

    def read_uint8(self, pos=0):
        return int(self.items[pos]) & 0xFF

    def read_uint16_le(self, pos=0):
        return self.read_number('<H', 2, pos)

    def read_uint16_be(self, pos=0):
        return self.read_number('>H', 2, pos)

    def read_uint32_le(self, pos=0):
        return self.read_number('<I', 4, pos)

    def read_uint32_be(self, pos=0):
        return self.read_number('>I', 4, pos)

    def read_uint64_le(self, pos=0):
        return self.read_number('<Q', 8, pos)

    def read_uint64_be(self, pos=0):
        return self.read_number('>Q', 8, pos)

    def read_float_le(self, pos=0):
        return self.read_number('<f', 4, pos)

    def read_float_be(self, pos=0):
        return self.read_number('>f', 4, pos)

    def read_double_le(self, pos=0):
        return self.read_number('<d', 8, pos)

    def read_double_be(self, pos=0):
        return self.read_number('>d', 8, pos)

    def write_number(self, fmt, number):
        return self.items.extend(struct.pack(fmt, number))

    def write_uint8(self, number):
        if number < 0:
            raise ValueError('number must be greater then zero')
        return self.items.append(int(number) & 0xFF)

    def write_int8(self, number):
        return self.items.append(int(number) & 0xFF)

    def write_uint16_le(self, number):
        return self.write_number('<H', number)

    def write_uint16_be(self, number):
        return self.write_number('>H', number)

    def write_uint32_le(self, number):
        return self.write_number('<I', number)

    def write_uint32_be(self, number):
        return self.write_number('>I', number)

    def write_uint64_le(self, number):
        return self.write_number('<Q', number)

    def write_uint64_be(self, number):
        return self.write_number('>Q', number)

    def write_float_le(self, number):
        return self.write_number('<f', number)

    def write_float_be(self, number):
        return self.write_number('>f', number)

    def write_double_le(self, number):
        return self.write_number('<d', number)

    def write_double_be(self, number):
        return self.write_number('>d', number)

    def write_str(self, s):
        return self.items.extend(s)


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
