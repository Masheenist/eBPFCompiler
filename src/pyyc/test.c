#define KBUILD_MODNAME "test"
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/udp.h>


int test(struct xdp_md* ctx) {
	int c = 3;

	int b = 1 + 2;

int d;

	if (b != c){
		d = 1;

	} else {
		d = 1;

	}
	
	bpf_trace_printk("recieved packet!");
	
	return(XDP_DROP);
}
