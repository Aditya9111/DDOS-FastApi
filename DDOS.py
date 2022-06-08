# -*- coding: utf-8 -*-

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements


class DDOS(BaseModel):
    Destination_Port: float
    Total_Length_of_Fwd_Packets: float
    Bwd_Packet_Length_Std: float
    Flow_IAT_Min: float
    Fwd_IAT_Total: float
    Bwd_Packets: float
    Init_Win_bytes_forward: float
    Init_Win_bytes_backward: float
