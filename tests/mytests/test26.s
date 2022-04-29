.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	subl $20, %esp
	movl $10, -4(%ebp)
	movl -4(%ebp), %eax
	addl $10, %eax
	movl %eax, -8(%ebp)
	movl -8(%ebp), %eax
	movl %eax, -12(%ebp)
	movl -4(%ebp), %eax
	pushl %eax
	call print_int_nl
	movl $100, %eax
	addl $1, %eax
	movl %eax, -12(%ebp)
	movl -12(%ebp), %eax
	movl %eax, -16(%ebp)
	movl -12(%ebp), %eax
	pushl %eax
	call print_int_nl
	addl $12, %esp
	movl $0, %eax
	leave
	ret
