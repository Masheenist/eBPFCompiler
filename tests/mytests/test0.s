.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	subl $4, %esp
	movl $1, %eax
	movl $2, %eax
	movl $1, %eax
	addl $2, %eax
	movl %eax, -4(%ebp)
	movl -4(%ebp), %eax
	pushl %eax
	call print_int_nl
	addl $0, %esp
	movl $0, %eax
	leave
	ret
