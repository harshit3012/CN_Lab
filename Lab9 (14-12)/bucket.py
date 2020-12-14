class LeakyBucket:
    def control_congestion(self, input_stream):
        buffer = 0
        i = 0
        error_text = '\033[93m'
        reset = '\033[0m'
        for packet in input_stream:
            print(f"Packet no {i}\tPacket size {packet}")
            x = self.size - buffer
            if packet < x:
                buffer += packet
                print("\tBucket output successful")
                print(f'\tLast {packet} bytes sent')
            else:
                print(f'{error_text}\tBucket overflow {reset}')
                buffer = self.size
            buffer -= self.flow
            i += 1

        while buffer:
            sent = self.flow if self.flow < buffer else buffer
            print(f'Packet no {i}\tPacket size {sent}')
            print("\tBucket output successful")
            buffer -= sent
            i += 1

        i += 1

    def __init__(self, bucket_size, output_rate):
        self.size = bucket_size
        self.flow = output_rate


input_stream = [int(x) for x in input(
    "Enter input stream of packets: ").split(' ')]
bucket_size = int(input("Enter bucket size: "))
output_rate = int(input("Enter output data rate: "))
network = LeakyBucket(bucket_size, output_rate)
network.control_congestion(input_stream)
