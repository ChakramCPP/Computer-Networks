import multiprocessing as mp

# intro = '''
# A, B, C are arranged in clockwise cyclic order
# SrcID for A = 10, B = 20, C = 30
# Packets colors: Red(0), Blue(1), Green(2)
# '''
import random
from datetime import time

p = []
q = []
l = []
index2name = {0: 'A', 1: 'B', 2: 'C'}
id_name_map = {10: 'A', 20: 'B', 30: 'C'}
name2index = {'A': 0, 'B': 1, 'C': 2}


def foo(q):
    q.put('hello')
    q.put("krishna")


def get_direction(cur_id, src_id):
    if cur_id > src_id:
        return 0  # Clockwise
    else:
        return 1  # Anti-Clockwise


def red(name, id, pkt):
    new_ttl = pkt.ttl - 1
    packet1 = Packet(2, new_ttl, pkt.seq + 1, pkt.sid, pkt.did)
    packet2 = Packet(2, new_ttl, pkt.seq + 1, pkt.sid, pkt.did)
    print("In The Red" + str(pkt.seq))
    q[(name2index[name] + 1) % 3].put(packet1)
    q[(name2index[name] - 1) % 3].put(packet2)


def green(name, id, pkt):
    new_ttl = pkt.ttl
    if random.uniform(0, 1) == 0:
        new_ttl = new_ttl - 1
    if new_ttl > 0:
        packet = Packet(2, new_ttl, pkt.seq, pkt.sid, pkt.did)
        if get_direction(id, pkt.sid) == 0:
            q[(name2index[name] + 1) % 3].put(packet)
        else:
            q[(name2index[name] - 1) % 3].put(packet)

    elif new_ttl == 0:
        packet = Packet(2, new_ttl, pkt.seq, pkt.sid, pkt.did)
        if get_direction(id, pkt.sid) == 0:  # Clockwise
            q[(name2index[name] + 1) % 3].put(packet)
        else:  # Anti-Clockwise
            q[(name2index[name] - 1) % 3].put(packet)


def blue(n, id, pkt):
    print("Blue packet:" + str(pkt.sid) + str(pkt.seq))


def call_func(p):
    if p.c == 0:
        global seq_no
        seq_no = seq_no + 2
        A = mp.Process(target=red, args=(p,))
        A.start()
        A.join()


class Packet:
    def __init__(self, c, ttl, seq, sid, did):
        self.c = c
        self.ttl = ttl
        self.seq = seq
        self.sid = sid
        self.did = did


def node(name, id, msg_queue):
    pr = mp.Process(target=generate_packet, args=(name))
    pr.start()
    while True:
        if not msg_queue.empty():
            obj = msg_queue.get()
            if int(obj.color, 2) == 0:
                red(name, id, obj)

            elif int(obj.color, 2) == 1:
                green(name, id, obj)

            elif int(obj.color, 2) == 2:
                blue(name, id, obj)


def generate_packet(name):
    packet_number = 0
    id = 10
    di = 0
    i = 0
    while True:
        packet_number = packet_number + 1
        print('{}: Generating new Packet-{}'.format(name, packet_number))
        rand_id = random.uniform(0, 1)
        if rand_id == 0:
            di = 20
            i = 1
        else:
            di = 30
            i = 2
        packet = Packet(0, 8, 1, 10, di)
        # while l[i] == 1:
        #     print('')
        # l[i] = 1
        l[i].acquire()
        q[i].put(packet)
        print('{}: Message sent to {}'.format(name, (i + 1) * 10))
        # l[i] = 0
        l[i].release()
        time.sleep(5)


if __name__ == '__main__':
    # # mp.set_start_method('spawn')
    # global a, b, c
    # a = mp.Queue()
    # b = mp.Queue()
    # c = mp.Queue()
    # p = mp.Process(target=foo, args=("",))
    # # p.start()
    # # p.join()
    # cont = True
    # global seq_no
    # seq_no = 0
    # while cont:
    #     seq_no = seq_no + 1
    #     col = int(input("Enter the color of the packet:"))
    #     ttl = int(input("Enter the TTL of the packet:"))
    #     sid = int(input("Enter the SID:"))
    #     did = int(input("Enter the DID:"))
    #     p = Packet(col, ttl, seq_no, sid, did)
    #     # A = mp.Process(target=foo, args=("",))
    #     # B = mp.Process(target=foo, args=("",))
    #     # C = mp.Process(target=foo, args=("",))
    #     call_func(p)
    #     cont = int(input("Try Another packet?"))
    if __name__ == '__main__':
        for i in range(3):
            queue = mp.Queue()
            process = mp.Process(target=node, args=(index2name[i], queue))
            l.append(mp.Lock())
            p.append(process)
            q.append(queue)

        for process in p:
            process.start()
