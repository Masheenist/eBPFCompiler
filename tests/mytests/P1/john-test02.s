.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -12(%ebp)
	movl %edi, -16(%ebp)
	movl %esi, -20(%ebp)
	subl $24, %esp
	movl $1, %edi
	sall $2, %edi
	orl $0, %edi
	movl $2, %ebx
	sall $2, %ebx
	orl $0, %ebx
	movl $3, -4(%ebp)
	sall $2, -4(%ebp)
	orl $0, -4(%ebp)
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	movl %eax, %esi
	addl $3, %esi
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %edi
	pushl %eax
	pushl %esi
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %ebx
	pushl %eax
	pushl %esi
	call set_subscript
	addl $12, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -4(%ebp)
	pushl %eax
	pushl %esi
	call set_subscript
	addl $12, %esp
	movl %esi, -12(%ebp)
	movl $2, %edi
	sall $2, %edi
	orl $0, %edi
	movl $1, %ebx
	sall $2, %ebx
	orl $0, %ebx
	movl $4, -4(%ebp)
	sall $2, -4(%ebp)
	orl $0, -4(%ebp)
	movl $3, %esi
	sall $2, %esi
	orl $0, %esi
	call create_dict
	addl $0, %esp
	movl %eax, -8(%ebp)
	addl $3, -8(%ebp)
	pushl -4(%ebp)
	pushl %esi
	pushl -8(%ebp)
	call set_subscript
	addl $12, %esp
	pushl %edi
	pushl %ebx
	pushl -8(%ebp)
	call set_subscript
	addl $12, %esp
	movl -8(%ebp), %ebx
	pushl -12(%ebp)
	call print_any
	addl $4, %esp
	pushl %ebx
	call print_any
	addl $4, %esp
	movl -20(%ebp), %esi
	movl -16(%ebp), %edi
	movl -12(%ebp), %ebx
	movl $0, %eax
	leave
	ret
