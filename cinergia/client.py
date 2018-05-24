from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder
from pymodbus.constants import Endian
from . import IQ21toFloat, IQ10toFloat, FloatToIQ21, FloatToIQ10
cinergiaByteOrder = Endian.Big
cinergiaWordOrder = Endian.Little


class CinergiaClient():
    '''
    This class enables to easily control and monitor a cinergia electronic load
    over Modbus TCP.
    '''

    def __init__(self, address, port=502):
        '''
        Initializes the connection

        :param address: the cinergia module IP address
        :param port: the cinergia port (default to 502)
        '''
        self._modbusClient = ModbusClient(address, port)

    def connect(self):
        '''
        Connects to the cinergia modbus server
        '''
        self._modbusClient.connect()

    def disconnect(self):
        '''
        Disconnects from the cinergia modbus server
        '''
        self._modbusClient.close()

    def read_uint32(self, addr):
        '''
        Reads 32 bits unsigned integer value from the cinergia registers
        :param addr: register address
        '''
        result = self._modbusClient.read_holding_registers(addr, 2, unit=255)
        decoder = BinaryPayloadDecoder.fromRegisters(
            result.registers,
            byteorder=cinergiaByteOrder,
            wordorder=cinergiaWordOrder)
        return decoder.decode_32bit_uint()

    def read_IQ21(self, addr):
        '''
        Reads fixed point real number with 21 fractional bits and converts
        into float
        :param addr: register address
        '''
        val = self.read_uint32(addr)
        return IQ21toFloat(val)

    def read_IQ10(self, addr):
        '''
        Reads fixed point real number with 10 fractional bits and converts
        into float
        :param addr: register address
        '''
        val = self.read_uint32(addr)
        return IQ10toFloat(val)

    def write_uint32(self, addr, value):
        '''
        Writes 32 bits unsigned integer value into the cinergia registers
        :param addr: register address
        :param value: register value
        '''
        builder = BinaryPayloadBuilder(
            byteorder=cinergiaByteOrder, wordorder=cinergiaWordOrder)
        builder.add_32bit_uint(value)
        registers = builder.to_registers()
        return self._modbusClient.write_registers(addr, registers, unit=255)
        # TODO: check write result

    def write_IQ10(self, addr, value):
        '''
        Writes a float into a fixed point real number with 10 fractional bits
        :param addr: register address
        :param value: register value
        '''
        return self.write_uint32(addr, FloatToIQ10(value))

    def write_IQ21(self, addr, value):
        '''
        Writes a float into a fixed point real number with 21 fractional bits
        :param addr: register address
        :param value: register value
        '''
        return self.write_uint32(addr, FloatToIQ21(value))
