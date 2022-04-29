.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	subl $28, %esp
	movl $10, %eax
	addl $30, %eax
	movl %eax, -4(%ebp)
	movl -4(%ebp), %eax
	addl $50, %eax
	movl %eax, -8(%ebp)
	call input
	movl %eax, -12(%ebp)
	movl -8(%ebp), %eax
	addl -12(%ebp), %eax
	movl %eax, -16(%ebp)
	movl -16(%ebp), %eax
	movl %eax, -20(%ebp)
	movl -16(%ebp), %eax
	addl -16(%ebp), %eax
	movl %eax, -24(%ebp)
	movl -24(%ebp), %eax
	movl %eax, -28(%ebp)
	movl -24(%ebp), %eax
	pushl %eax
	call print_int_nl
	addl $24, %esp
	movl $0, %eax
	leave
	ret
