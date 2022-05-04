
c = 3

def basic_test(ctx):

    # some form of the following:
    #   void *data = (void *)(long)ctx->data;
    #   void *data_end = (void *)(long)ctx->data_end;

    b = 1+1 #b is an int
    q = "recieved packet!\n" #str
    bpf_trace_printk(q)

    # g = other_f(b) #unresolved: g, return of next_fun
    return XDP_DROP

# def other_f(b):
#     return b

# def next_func(a): 
#     c = other_f(a)
#     # return lambda_1
#     return lambda x: c+x

# def lamba_1(x):
#     return c+x