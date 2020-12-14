from Cpu import Cpu
from RSDL import Rsdl

if __name__ == '__main__':
    print("===Rotating Staircase DeadLine Simulator===")
    rsdl = Rsdl()
    cpu = Cpu(rsdl)
    cpu.create_n_randon_tasks(15)
    cpu.run()
