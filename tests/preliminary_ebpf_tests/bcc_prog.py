from bcc import BPF 
from bcc.utils import printb

device = "eth1" 

special_str = custom_transpile('basic_test.py') #produces string

# b = BPF(src_file="udp_counter.c") 
# fn = b.load_func("udp_counter", BPF.XDP) 
# b = BPF(src_file="basic_test.c") 
b = BPF(special_str)
fn = b.load_func("basic_test", BPF.XDP) 
b.attach_xdp(device, fn, 0) 

try:
    b.trace_print() 
except KeyboardInterrupt: 
    print ("Done.")
    # dist = b.get_table("counter") 
    # for k, v in sorted(dist.items()): 
    #     print("DEST_PORT : %10d, COUNT : %10d" % (k.value, v.value)) 

b.remove_xdp(device, 0) 
