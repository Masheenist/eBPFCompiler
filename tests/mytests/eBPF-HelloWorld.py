from bcc import BPF

#BPF_PROGRAM = r"""
#int hello(void *ctx) {
#  bpf_trace_printk("Hello world! File opened\n");
#  return 0;
#}
#"""
<<<<<<< HEAD
def BPF_PROGRAM():
    bpf_trace_printk = ("Hello world! File opened\n")
=======

BPF_PROGRAM = r"""
def hello(ctx):
    bpf_trace_printk("Hello world! File opened\n");
    return 0
"""
>>>>>>> 1bfb74f2d0beb59a27b53a74d56f3659a74e6f4a

bpf = BPF(text=BPF_PROGRAM)
bpf.attach_kprobe(event=bpf.get_syscall_fnname("clone"), fn_name="hello")

while True:
    try:
        (_, _, _, _, _, msg_b) = bpf.trace_fields()
        msg = msg_b.decode('utf8')
        if "Hello world" in msg:
            print(msg)
    except ValueError:
        continue
    except KeyboardInterrupt:
        break
