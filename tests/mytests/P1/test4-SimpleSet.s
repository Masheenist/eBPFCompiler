.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -16(%ebp)
	movl %edi, -20(%ebp)
	movl %esi, -24(%ebp)
	subl $28, %esp
	movl $3, %edi
	sall $2, %edi
	orl $0, %edi
	movl $1, %ebx
	sall $2, %ebx
	orl $0, %ebx
	movl $4, -4(%ebp)
	sall $2, -4(%ebp)
	orl $0, -4(%ebp)
	movl $8, %esi
	sall $2, %esi
	orl $0, %esi
	movl $5, -12(%ebp)
	sall $2, -12(%ebp)
	orl $0, -12(%ebp)
	movl $9, -8(%ebp)
	sall $2, -8(%ebp)
	orl $0, -8(%ebp)
	movl $6, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	movl %eax, -16(%ebp)
	addl $3, -16(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %edi
	pushl %eax
	pushl -16(%ebp)
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %ebx
	pushl %eax
	pushl -16(%ebp)
	call set_subscript
	addl $12, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -4(%ebp)
	pushl %eax
	pushl -16(%ebp)
	call set_subscript
	addl $12, %esp
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %esi
	pushl %eax
	pushl -16(%ebp)
	call set_subscript
	addl $12, %esp
	movl $4, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -12(%ebp)
	pushl %eax
	pushl -16(%ebp)
	call set_subscript
	addl $12, %esp
	movl $5, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -8(%ebp)
	pushl %eax
	pushl -16(%ebp)
	call set_subscript
	addl $12, %esp
	movl -16(%ebp), %ebx
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	movl $1, %ecx
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
