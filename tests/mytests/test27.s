.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	subl $20, %esp
	call input
	movl %eax, -4(%ebp)
	movl -4(%ebp), %eax
	negl %eax
	movl %eax, -8(%ebp)
	movl -8(%ebp), %eax
	movl %eax, -12(%ebp)
	call input
	movl %eax, -16(%ebp)
	movl -8(%ebp), %eax
	addl -16(%ebp), %eax
	movl %eax, -20(%ebp)
	movl -20(%ebp), %eax
	pushl %eax
	call print_int_nl
	addl $16, %esp
	movl $0, %eax
	leave
	ret
