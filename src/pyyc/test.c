#define KBUILD_MODNAME "test"
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/udp.h>


int test(struct xdp_md* ctx) {
	bpf_trace_printk("recieved packet!");
	return(XDP_DROP);
}
