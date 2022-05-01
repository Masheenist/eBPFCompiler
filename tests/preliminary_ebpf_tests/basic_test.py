
# c = 3

def basic_test(ctx):

    # some form of the following:
    #   void *data = (void *)(long)ctx->data;
    #   void *data_end = (void *)(long)ctx->data_end;

    b = 1+1
    bpf_trace_printk("recieved packet!\n")

    # next_func(b)
    return XDP_DROP

# def next_func(a):
#     return lambda x: c+x