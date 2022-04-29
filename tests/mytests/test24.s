.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	subl $8, %esp
	movl $5, %eax
	movl $10, %eax
	negl %eax
	movl %eax, -4(%ebp)
	movl $5, %eax
	addl -4(%ebp), %eax
	movl %eax, -8(%ebp)
	movl -8(%ebp), %eax
	pushl %eax
	call print_int_nl
	addl $4, %esp
	movl $0, %eax
	leave
	ret
