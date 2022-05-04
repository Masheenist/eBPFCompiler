# #define KBUILD_MODNAME "udp_counter"
# #include <linux/bpf.h>
# #include <linux/if_ether.h>
# #include <linux/ip.h>
# #include <linux/udp.h>


# BPF_HISTOGRAM(counter, u64);
counter = BPF_HISTOGRAM()

#int udp_counter(struct xdp_md *ctx)
#{
def udp_counter(ctx):
    #void *data = (void *)(long)ctx->data;
    data = ctx.data
    #void *data_end = (void *)(long)ctx->data_end; <-- implied by use of ctx struct

    #struct ethhdr *eth = data;
    #if ((void *)eth + sizeof(*eth) <= data_end)
    #{
    eth = data.eth
    if data.eth: #this is directly translated to checking bounds as in above 2 lines

        #struct iphdr *ip = data + sizeof(*eth);
        #if ((void *)ip + sizeof(*ip) <= data_end)
        #{
        ip = data.ip
        if data.ip: # need to recognize order of stuff to do this translation. it goes eth, ip, udp/tcp, etc.
            
            #if (ip->protocol == IPPROTO_UDP)
            #{
            if ip.protocol == IPPROTO_UDP:
            
                #struct udphdr *udp = (void *)ip + sizeof(*ip);
                #if ((void *)udp + sizeof(*udp) <= data_end)
                #{
                udp = data.udp
                if data.udp:

                    #u64 value = htons(udp->dest);
                    value = htons(udp.dest)
                    #counter.increment(value);
                    counter.increment(value) #anything going into a bpf map needs to be a u64
                    #bpf_trace_printk("recieved packet!\n");
                    bpf_trace_printk("recieved packet!\n")
                #}
            #}
        #}
    #}
    #return XDP_PASS;
    return XDP_PASS
}
