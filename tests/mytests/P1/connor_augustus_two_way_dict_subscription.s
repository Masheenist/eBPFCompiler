.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -16(%ebp)
	movl %edi, -20(%ebp)
	movl %esi, -24(%ebp)
	subl $28, %esp
	movl $1, %edi
	sall $2, %edi
	orl $1, %edi
	movl $1, %ebx
	sall $2, %ebx
	orl $0, %ebx
	movl $1, -4(%ebp)
	sall $2, -4(%ebp)
	orl $1, -4(%ebp)
	movl $2, %esi
	sall $2, %esi
	orl $0, %esi
	movl $0, -12(%ebp)
	sall $2, -12(%ebp)
	orl $1, -12(%ebp)
	movl $3, -8(%ebp)
	sall $2, -8(%ebp)
	orl $0, -8(%ebp)
	call create_dict
	addl $0, %esp
	movl %eax, -16(%ebp)
	addl $3, -16(%ebp)
	pushl %edi
	pushl %ebx
	pushl -16(%ebp)
	call set_subscript
	addl $12, %esp
	pushl -4(%ebp)
	pushl %esi
	pushl -16(%ebp)
	call set_subscript
	addl $12, %esp
	pushl -12(%ebp)
	pushl -8(%ebp)
	pushl -16(%ebp)
	call set_subscript
	addl $12, %esp
	movl -16(%ebp), %ebx
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl %ebx
	call get_subscript
	addl $8, %esp
	pushl %eax
	call print_any
	addl $4, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	movl $33, %ecx
	sall $2, %ecx
	orl $0, %ecx
	pushl %ecx
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	pushl %ebx
	call print_any
	addl $4, %esp
	movl -24(%ebp), %esi
	movl -20(%ebp), %edi
	movl -16(%ebp), %ebx
	movl $0, %eax
	leave
	ret
