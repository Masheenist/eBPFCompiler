.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	subl $16, %esp
	call input
	movl %eax, -4(%ebp)
	call input
	movl %eax, -8(%ebp)
	movl -8(%ebp), %eax
	negl %eax
	movl %eax, -12(%ebp)
	movl -4(%ebp), %eax
	addl -12(%ebp), %eax
	movl %eax, -16(%ebp)
	movl -16(%ebp), %eax
	pushl %eax
	call print_int_nl
	addl $12, %esp
	movl $0, %eax
	leave
	ret
