import cpu.addressing
import unittest

class DummyPC_State(object):
    def __init__(self):
        self.X = 1
        self.Y = 2
        self.PC = 3
        self.CYCLES_TO_CLOCK = 3

class DummyMemory(object):
    def __init__(self):
        pass

    def read(self, address):
        return 0

    def read16(self, address):
        return 0

class TestAddressing(unittest.TestCase):

    def test_addressing(self):
        pc_state = DummyPC_State()
        memory   = DummyMemory()
        address = cpu.addressing.AddressIZX(pc_state, memory)
        self.assertEqual(address.get_addressing_time(), 4*pc_state.CYCLES_TO_CLOCK)
        self.assertEqual(address.get_addressing_size(), 1)
        address = cpu.addressing.AddressZPX(pc_state, memory)
        self.assertEqual(address.get_addressing_time(), 2*pc_state.CYCLES_TO_CLOCK)
        self.assertEqual(address.get_addressing_size(), 1)
        address = cpu.addressing.AddressZPY(pc_state, memory)
        self.assertEqual(address.get_addressing_time(), 2*pc_state.CYCLES_TO_CLOCK)
        self.assertEqual(address.get_addressing_size(), 1)
        address = cpu.addressing.AddressZP(pc_state, memory)
        self.assertEqual(address.get_addressing_time(), 1*pc_state.CYCLES_TO_CLOCK)
        self.assertEqual(address.get_addressing_size(), 1)
        address = cpu.addressing.AddressIMM(pc_state, memory)
        self.assertEqual(address.get_addressing_time(), 0*pc_state.CYCLES_TO_CLOCK)
        self.assertEqual(address.get_addressing_size(), 1)
        address = cpu.addressing.AddressIZY(pc_state, memory)
        self.assertEqual(address.get_addressing_time(), 3*pc_state.CYCLES_TO_CLOCK)
        self.assertEqual(address.get_addressing_size(), 1)
        address = cpu.addressing.AddressAbs(pc_state, memory)
        self.assertEqual(address.get_addressing_time(), 2*pc_state.CYCLES_TO_CLOCK)
        self.assertEqual(address.get_addressing_size(), 2)
        address = cpu.addressing.AddressIndirect(pc_state, memory)
        self.assertEqual(address.get_addressing_time(), 4*pc_state.CYCLES_TO_CLOCK)
        self.assertEqual(address.get_addressing_size(), 2)
        address = cpu.addressing.AddressAby(pc_state, memory) # Page delay
        self.assertEqual(address.get_addressing_time(), 2*pc_state.CYCLES_TO_CLOCK)
        self.assertEqual(address.get_addressing_size(), 2)
        address = cpu.addressing.AddressAbx(pc_state, memory)
        self.assertEqual(address.get_addressing_time(), 2*pc_state.CYCLES_TO_CLOCK)
        self.assertEqual(address.get_addressing_size(), 2)
        address = cpu.addressing.AddressAccumulator(pc_state, memory)
        self.assertEqual(address.get_addressing_time(), 0*pc_state.CYCLES_TO_CLOCK)
        self.assertEqual(address.get_addressing_size(), 0)

if __name__ == '__main__':
    unittest.main()
