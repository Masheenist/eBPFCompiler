.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -4(%ebp)
	movl %edi, -8(%ebp)
	movl %esi, -12(%ebp)
	subl $16, %esp
	movl $1, %esi
	sall $2, %esi
	orl $0, %esi
	movl $2, %edi
	sall $2, %edi
	orl $0, %edi
	movl $3, -4(%ebp)
	sall $2, -4(%ebp)
	orl $0, -4(%ebp)
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
	pushl %esi
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %edi
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -4(%ebp)
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl %ebx, %eax
	movl %eax, -4(%ebp)
	movl $0, %edi
	sall $2, %edi
	orl $0, %edi
	movl $0, %ebx
	sall $2, %ebx
	orl $0, %ebx
	movl $1, %eax
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
	pushl %ebx
	pushl %eax
	pushl %esi
	call set_subscript
	addl $12, %esp
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl %esi
	call get_subscript
	addl $8, %esp
	pushl %eax
	pushl %edi
	pushl -4(%ebp)
	call set_subscript
	addl $12, %esp
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl -4(%ebp)
	call get_subscript
	addl $8, %esp
	pushl %eax
	call print_any
	addl $4, %esp
	movl -12(%ebp), %esi
	movl -8(%ebp), %edi
	movl -4(%ebp), %ebx
	movl $0, %eax
	leave
	ret
