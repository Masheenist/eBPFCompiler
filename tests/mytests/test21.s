.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	subl $8, %esp
	movl $1024, -4(%ebp)
	movl -4(%ebp), %eax
	addl -4(%ebp), %eax
	movl %eax, -8(%ebp)
	movl -8(%ebp), %eax
	pushl %eax
	call print_int_nl
	addl $4, %esp
	movl $0, %eax
	leave
	ret
