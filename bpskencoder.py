import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    """Embedded Python Block - BPSK Encoder"""

    def __init__(self, samp_rate=1e6):  # 默认参数
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='BPSK Encoder',   # 在GRC中显示的名字
            in_sig=[np.int32],      # 输入是比特流（0和1）
            out_sig=[np.float32]   # 输出是BPSK符号（-1或+1）
        )
        self.samp_rate = samp_rate

    def work(self, input_items, output_items):
        """BPSK编码：0映射为-1，1映射为+1"""
        in0 = input_items[0]
        
        # BPSK编码：0映射为-1，1映射为+1
        out = np.array([-1 if bit == 0 else 1 for bit in in0], dtype=np.float32)
        
        # 将结果写入输出缓冲区
        output_items[0][:] = out
        return len(output_items[0])

