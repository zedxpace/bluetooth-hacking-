import sys
import struct
import bluetooth._bluetooth as bt

##open hci socket
sock = bt.hci_open_dev(0)

##get data direction information
sock.setsockopt(bt.SOL_HCI ,bt.HCI_DATA_DIR ,1)

##get timestamps
sock.setsockopt(bt.SOL_HCI ,bt.HCI_TIME_STAMP ,1)

##contruxt and set filter to sniff all hci events and all packet types
filter = bt.hci_filter_now()
bt.hci_filter_all_events(filter)
bt.hci_filter_all_ptypes(filter)
sock.setsockopt(bt.SOL_HCI ,bt.HCI_FILTER ,filter)

##start sniffing
while True:
    ##read first 3 bytes
    header = sock.recv(3)

    if header:
        #decode them and read the reset of the packet
        ptype ,event ,plen = struct.unpack("BBB" ,header)
        packet = sock.recv(plen)

        print("Ptype: " + str(ptype) + " Event: " + str(event))
        print("Packet : ")

        ##got ACL data connection ,if so try dump it in ascii
        ##otherwise dump the packet in hex

        if ptype == bt.HCI_ACLDATA_PKT:
            print(packet + "\n")
        else:
            for c in packet:
                hex = struct.unpack("B" ,c)[0]
                sys.stdout.write("%02x"%hex)
            
            print("\n")
    else:
        ##no data
        break
sock.close()