#define KBUILD_MODNAME "basic_test"
#include <linux/bpf.h>
#define SEC(NAME) __attribute__((section(NAME), used))

SEC("prog")
int basic_test(struct xdp_md *ctx) {
    bpf_trace_printk("recieved packet!\n");
    return XDP_DROP;
}

// char _license[] SEC("license") = "GPL";