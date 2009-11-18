# Copyright (c) 2006-2009, University of Glasgow
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are
# permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright notice, this list of 
#		conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice, this list
#		of conditions and the following disclaimer in the documentation and/or other
#	 	materials provided with the distribution.
#    * Neither the name of the University of Glasgow nor the names of its contributors 
#		may be used to endorse or promote products derived from this software without
# 		specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY 
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
# THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
# OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from pyshake_constants import *

def convert_raw_data_value(bytes):
	lsb = ord(bytes[0])
	msb = ord(bytes[1])
	
	if msb & 0x80:
		return (lsb + (msb << 8)) - 65536
	else:
		return lsb + (msb << 8)

class sk_sensor_data:
	def __init__(self):
		self.accx, self.accy, self.accz = 0,0,0
		self.gyrx, self.gyry, self.gyrz = 0,0,0
		self.magx, self.magy, self.magz = 0,0,0
		self.heading = 0
		self.cap_sk6 = [0 for x in range(2)]
		self.cap_sk7 = [[0 for x in range(12)], [0 for x in range(12)], [0 for x in range(12)]]
		self.ana0, self.ana1 = 0,0
		self.shaking_peak_accel, self.shaking_direction, self.shaking_timestamp = 0,0,0
		self.hr_bpm = 0.0
		self.rph = [0,0,0]
		self.timestamps = [0 for x in range(8)]
		self.internal_timestamps = [0 for x in range(8)]
		self.sk6seq = 0
		self.sk7seq = 0
		self.hrseq = 0

class SHAKE:
	def __init__(self, shakedev, devtype):
		self.__shake = shakedev
		self.device_type = devtype
		self.data = sk_sensor_data()

	def parse_ascii_packet(self, packet_type, packetbuf, playback, timestamp_packet):
		pass

	def read_ascii_packet(self, packet_type, packetbuf):
		pass

	def parse_raw_packet(self, packet_type, packetbuf, has_seq):
		pass

	def read_raw_packet(self, packet_type, packetbuf):
		pass

	def get_next_packet(self):
		pass

	def parse_packet(self, packetbuf, packet_type):
		pass

	def is_ascii_packet(self, packet_type):
		pass

	def parse_ack_packet(self, packetbuf, addr, val):
		pass

	def extract_ascii_packet(self, packet_type, packetbuf, playback, timestamp_packet):
		pass

	def extract_raw_packet(self, packet_type, packetbuf, has_seq):
		pass

	def classify_packet_header(self, packetbuf, ascii_packet):
		pass

	def read_device_info(self):
		pass
