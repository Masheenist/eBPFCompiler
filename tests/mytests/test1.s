.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	subl $8, %esp
	call input
	movl %eax, -4(%ebp)
	movl $1, %eax
	movl -4(%ebp), %eax
	addl $1, %eax
	movl %eax, -8(%ebp)
	movl -8(%ebp), %eax
	pushl %eax
	call print_int_nl
	addl $4, %esp
	movl $0, %eax
	leave
	ret
