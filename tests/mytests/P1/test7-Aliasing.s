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
	movl %esi, %ebx
	movl %ebx, %edi
	movl $4, %ebx
	sall $2, %ebx
	orl $0, %ebx
	movl $5, -4(%ebp)
	sall $2, -4(%ebp)
	orl $0, -4(%ebp)
	movl $6, %esi
	sall $2, %esi
	orl $0, %esi
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	movl %eax, -8(%ebp)
	addl $3, -8(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %ebx
	pushl %eax
	pushl -8(%ebp)
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -4(%ebp)
	pushl %eax
	pushl -8(%ebp)
	call set_subscript
	addl $12, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %esi
	pushl %eax
	pushl -8(%ebp)
	call set_subscript
	addl $12, %esp
	movl -8(%ebp), %ebx
	pushl %edi
	call print_any
	addl $4, %esp
	movl %ebx, %edi
	movl $0, %ecx
	sall $2, %ecx
	orl $0, %ecx
	movl $7, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl %ecx
	pushl %ebx
	call set_subscript
	addl $12, %esp
	pushl %edi
	call print_any
	addl $4, %esp
	movl -16(%ebp), %esi
	movl -12(%ebp), %edi
	movl -8(%ebp), %ebx
	movl $0, %eax
	leave
	ret
