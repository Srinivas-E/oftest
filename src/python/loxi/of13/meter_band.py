# Copyright (c) 2008 The Board of Trustees of The Leland Stanford Junior University
# Copyright (c) 2011, 2012 Open Networking Foundation
# Copyright (c) 2012, 2013 Big Switch Networks, Inc.

# Automatically generated by LOXI from template meter_band.py
# Do not modify

import struct
import const
import util
import loxi.generic_util
import loxi

def unpack_list(reader):
    def deserializer(reader, typ):
        parser = parsers.get(typ)
        if not parser: raise loxi.ProtocolError("unknown meter band type %d" % typ)
        return parser(reader)
    return loxi.generic_util.unpack_list_tlv16(reader, deserializer)

class MeterBand(object):
    type = None # override in subclass
    pass

class drop(MeterBand):
    type = const.OFPMBT_DROP

    def __init__(self, rate=None, burst_size=None):
        if rate != None:
            self.rate = rate
        else:
            self.rate = 0
        if burst_size != None:
            self.burst_size = burst_size
        else:
            self.burst_size = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.rate))
        packed.append(struct.pack("!L", self.burst_size))
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = drop()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPMBT_DROP)
        _len = reader.read('!H')[0]
        obj.rate = reader.read('!L')[0]
        obj.burst_size = reader.read('!L')[0]
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.rate != other.rate: return False
        if self.burst_size != other.burst_size: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("drop {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("rate = ");
                q.text("%#x" % self.rate)
                q.text(","); q.breakable()
                q.text("burst_size = ");
                q.text("%#x" % self.burst_size)
            q.breakable()
        q.text('}')

class dscp_remark(MeterBand):
    type = const.OFPMBT_DSCP_REMARK

    def __init__(self, rate=None, burst_size=None, prec_level=None):
        if rate != None:
            self.rate = rate
        else:
            self.rate = 0
        if burst_size != None:
            self.burst_size = burst_size
        else:
            self.burst_size = 0
        if prec_level != None:
            self.prec_level = prec_level
        else:
            self.prec_level = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.rate))
        packed.append(struct.pack("!L", self.burst_size))
        packed.append(struct.pack("!B", self.prec_level))
        packed.append('\x00' * 3)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = dscp_remark()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPMBT_DSCP_REMARK)
        _len = reader.read('!H')[0]
        obj.rate = reader.read('!L')[0]
        obj.burst_size = reader.read('!L')[0]
        obj.prec_level = reader.read('!B')[0]
        reader.skip(3)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.rate != other.rate: return False
        if self.burst_size != other.burst_size: return False
        if self.prec_level != other.prec_level: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("dscp_remark {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("rate = ");
                q.text("%#x" % self.rate)
                q.text(","); q.breakable()
                q.text("burst_size = ");
                q.text("%#x" % self.burst_size)
                q.text(","); q.breakable()
                q.text("prec_level = ");
                q.text("%#x" % self.prec_level)
            q.breakable()
        q.text('}')

class experimenter(MeterBand):
    type = const.OFPMBT_EXPERIMENTER

    def __init__(self, rate=None, burst_size=None, experimenter=None):
        if rate != None:
            self.rate = rate
        else:
            self.rate = 0
        if burst_size != None:
            self.burst_size = burst_size
        else:
            self.burst_size = 0
        if experimenter != None:
            self.experimenter = experimenter
        else:
            self.experimenter = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.rate))
        packed.append(struct.pack("!L", self.burst_size))
        packed.append(struct.pack("!L", self.experimenter))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = experimenter()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPMBT_EXPERIMENTER)
        _len = reader.read('!H')[0]
        obj.rate = reader.read('!L')[0]
        obj.burst_size = reader.read('!L')[0]
        obj.experimenter = reader.read('!L')[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.rate != other.rate: return False
        if self.burst_size != other.burst_size: return False
        if self.experimenter != other.experimenter: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("experimenter {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("rate = ");
                q.text("%#x" % self.rate)
                q.text(","); q.breakable()
                q.text("burst_size = ");
                q.text("%#x" % self.burst_size)
                q.text(","); q.breakable()
                q.text("experimenter = ");
                q.text("%#x" % self.experimenter)
            q.breakable()
        q.text('}')


parsers = {
    const.OFPMBT_DROP : drop.unpack,
    const.OFPMBT_DSCP_REMARK : dscp_remark.unpack,
    const.OFPMBT_EXPERIMENTER : experimenter.unpack,
}
