.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl $666, %eax
	pushl %eax
	call print_int_nl
	addl $-4, %esp
	movl $0, %eax
	leave
	ret
