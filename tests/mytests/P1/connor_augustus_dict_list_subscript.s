.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -12(%ebp)
	movl %edi, -16(%ebp)
	movl %esi, -20(%ebp)
	subl $24, %esp
	movl $2, %esi
	sall $2, %esi
	orl $0, %esi
	movl $1, %edi
	sall $2, %edi
	orl $0, %edi
	movl $4, -4(%ebp)
	sall $2, -4(%ebp)
	orl $0, -4(%ebp)
	movl $3, %ebx
	sall $2, %ebx
	orl $0, %ebx
	call create_dict
	addl $0, %esp
	movl %eax, -8(%ebp)
	addl $3, -8(%ebp)
	pushl %esi
	pushl %edi
	pushl -8(%ebp)
	call set_subscript
	addl $12, %esp
	pushl -4(%ebp)
	pushl %ebx
	pushl -8(%ebp)
	call set_subscript
	addl $12, %esp
	movl -8(%ebp), %eax
	movl %eax, -4(%ebp)
	movl $1, %esi
	sall $2, %esi
	orl $0, %esi
	movl $1, -12(%ebp)
	sall $2, -12(%ebp)
	orl $0, -12(%ebp)
	movl $2, -8(%ebp)
	sall $2, -8(%ebp)
	orl $0, -8(%ebp)
	movl $3, %edi
	sall $2, %edi
	orl $0, %edi
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	movl %eax, %ebx
	addl $3, %ebx
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -12(%ebp)
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -8(%ebp)
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %edi
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	pushl %ebx
	pushl %esi
	pushl -4(%ebp)
	call set_subscript
	addl $12, %esp
	pushl -4(%ebp)
	call print_any
	addl $4, %esp
	movl -20(%ebp), %esi
	movl -16(%ebp), %edi
	movl -12(%ebp), %ebx
	movl $0, %eax
	leave
	ret
