# Bridges and Switches

In this activity you will write the software to turn a computer into a bridge, and then into a switch! By writing this software you will have to apply your understanding of the following concepts:

1. Ethernet as a communication protocol which allows two computers connected via an Ethernet cable to exchange packets.
2. Ethernet packets contain a 'frame' with the following fields:
    - FromMac
    - ToMac
    - EtherTypeOrLength
    - Payload
3. MAC addresses as identifying a device on the network.
4. Network Interface Cards (NICs/Interfaces) as a device which creates an analogue signal on an Ethernet wire to send/recieve a packet.

# General Guidence

- You only need to fill in the parts with a // TODO ....
- Write out in english what you want the program to do, then try convert into psudocode.
- Refer the the provided 'psudocode.html' file for help with psudocode syntax.

# Part 1

File: bridge-part1.txt

In this part you will produce a program which allows a computer to act as a very simple bridge. The file itself contains detailed instructions and provides all the psudocode functions/modules you will need.

# Part 2

File: bridge-part2.txt

In this part you will take the program from Part 1 and adapt it so that it only re-transmits a packet when it knows the the packet's destination can be reached. The software should determine if a destination is accessible by loading the mapping file using the provided functions at the beginning of your program.

# Part 3

File: switch-part1.txt

This part comprises of answering two questions (you may need to do some research!) which are detailed in the associated file.

# Part 4

File: switch-part2.txt

Here your bridge evolves into a switch by supporting many more computers! You'll need to adapt your bridge code from Part 2 following the suggestions in the task file.

# Part 5

File: switch-part3.txt

You're almost there! There is just one piece of functionality we need to add. If the switch doesn't know how by which interface a given MAC is accessible it should flood the network with the packet. This is explained in greater detail in the associated task file.

# Submission

Submit a zip file containing all of your task files.