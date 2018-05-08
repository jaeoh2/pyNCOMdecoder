import argparse
import socket
import logging
from bitstring import BitArray

import numpy as np
import struct
from collections import OrderedDict

from NCOMmsg import NCOM

# Set Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=3000, help='UDP port')
args = parser.parse_args()

# Set logging module
logger = logging.getLogger('NCOM decoder logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('ncom.log')
fh.setLevel(logging.DEBUG)

pack_size = 80 #byte

if __name__ == "__main__":
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', args.port))
        logger.info("UPD connected port:{}".format(args.port))

        while True:
            data_byte = sock.recv(pack_size)
            assert len(data_byte) == 72, len(data_byte)
            ncom = NCOM(data_byte)

            print(ncom.d['Time'], ncom.d['NavStat'])

    except OSError:
        logger.error("UDP disconnected")






