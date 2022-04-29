.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	subl $16, %esp
	movl $1, %eax
	addl $2, %eax
	movl %eax, -4(%ebp)
	movl -4(%ebp), %eax
	addl $3, %eax
	movl %eax, -8(%ebp)
	movl -8(%ebp), %eax
	addl $4, %eax
	movl %eax, -12(%ebp)
	movl -12(%ebp), %eax
	addl $5, %eax
	movl %eax, -16(%ebp)
	movl -16(%ebp), %eax
	pushl %eax
	call print_int_nl
	addl $12, %esp
	movl $0, %eax
	leave
	ret
