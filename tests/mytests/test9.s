.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	subl $12, %esp
	call input
	movl %eax, -4(%ebp)
	call input
	movl %eax, -8(%ebp)
	movl -4(%ebp), %eax
	addl -8(%ebp), %eax
	movl %eax, -12(%ebp)
	movl -12(%ebp), %eax
	pushl %eax
	call print_int_nl
	addl $8, %esp
	movl $0, %eax
	leave
	ret
