#define KBUILD_MODNAME "test"
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/udp.h>


int a = 3 + 3;
int q = 72;
int d = 7;
int lambda_17(int x, int y) {
	return(x + y / 4);
}
int test(struct xdp_md* ctx) {
	int c = -a;
	int b = 1 + 2;
	if (b != c){
		d = 1;
	} else {
		d = 1;
	}
	int z = lambda_17(int x, int y);
	bpf_trace_printk("recieved packet!");
	return(XDP_DROP);
}
