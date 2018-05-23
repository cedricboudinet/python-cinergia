from unittest import TestCase
from cinergia.client import CinergiaClient
from cinergia.client import cinergiaByteOrder, cinergiaWordOrder
from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.register_read_message import ReadHoldingRegistersResponse
from cinergia import FloatToIQ21, FloatToIQ10


class ModbusClientMock(ModbusClient):

    def __init__(self):
        self.__enabled = False
        self.__run = False
        self._mockRegisters = {
            168: 0,
            }

    def read_holding_registers(self, addr, num, unit):
        builder = BinaryPayloadBuilder(
            byteorder=cinergiaByteOrder, wordorder=cinergiaWordOrder)
        builder.add_32bit_uint(self._mockRegisters[addr])
        ret = ReadHoldingRegistersResponse()
        ret.registers = builder.to_registers()
        return ret

    def setMockRegister(self, addr, value):
        self._mockRegisters[addr] = value

    def getMockRegister(self, addr):
        return self._mockRegisters[addr]

    def connect(self):
        pass

    def close(self):
        pass


class Control_Tests(TestCase):

    def setUp(self):
        self.cinergiaClient = CinergiaClient('127.0.0.1')
        # replacing the modbus client by a mock one
        self.cinergiaClient._modbusClient = ModbusClientMock()

    def tearDown(self):
        self.cinergiaClient.disconnect()

    def test_connect(self):
        self.cinergiaClient.connect()

    def test_read_uint32(self):
        self.assertEqual(self.cinergiaClient.read_uint32(168), 0)
        self.cinergiaClient._modbusClient.setMockRegister(168, 2)
        self.assertEqual(self.cinergiaClient.read_uint32(168), 2)

    def test_read_IQ21(self):
        self.cinergiaClient._modbusClient.setMockRegister(520, FloatToIQ21(.5))
        self.assertEqual(self.cinergiaClient.read_IQ21(520), 0.5)

    def test_read_IQ10(self):
        self.cinergiaClient._modbusClient.setMockRegister(462, FloatToIQ10(.5))
        self.assertEqual(self.cinergiaClient.read_IQ10(462), 0.5)

    def test_read_uint32(self):
        self.assertEqual(self.cinergiaClient._modbusClient.getMockRegister(168), 0)
        self.cinergiaClient.write_uint32(168, 2)
        self.assertEqual(self.cinergiaClient._modbusClient.getMockRegister(168), 2)

    def test_read_IQ21(self):
        raise NotImplementedError()

    def test_read_IQ10(self):
        raise NotImplementedError()
