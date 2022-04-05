.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -8(%ebp)
	movl %edi, -12(%ebp)
	movl %esi, -16(%ebp)
	subl $20, %esp
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
	movl %esi, -8(%ebp)
	movl $4, %edi
	sall $2, %edi
	orl $0, %edi
	movl $5, %ebx
	sall $2, %ebx
	orl $0, %ebx
	movl $6, -4(%ebp)
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
	movl %esi, %ebx
	pushl -8(%ebp)
	call print_any
	addl $4, %esp
	pushl %ebx
	call print_any
	addl $4, %esp
	movl -8(%ebp), %eax
	movl %ebx, -8(%ebp)
	movl %eax, %ebx
	pushl -8(%ebp)
	call print_any
	addl $4, %esp
	pushl %ebx
	call print_any
	addl $4, %esp
	movl -16(%ebp), %esi
	movl -12(%ebp), %edi
	movl -8(%ebp), %ebx
	movl $0, %eax
	leave
	ret
