.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -16(%ebp)
	movl %edi, -20(%ebp)
	movl %esi, -24(%ebp)
	subl $28, %esp
	movl $3, %esi
	sall $2, %esi
	orl $0, %esi
	movl $1, %edi
	sall $2, %edi
	orl $0, %edi
	movl $4, %ebx
	sall $2, %ebx
	orl $0, %ebx
	movl $1, -4(%ebp)
	sall $2, -4(%ebp)
	orl $0, -4(%ebp)
	movl $5, -16(%ebp)
	sall $2, -16(%ebp)
	orl $0, -16(%ebp)
	movl $9, -12(%ebp)
	sall $2, -12(%ebp)
	orl $0, -12(%ebp)
	movl $6, %eax
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
	pushl %esi
	pushl %eax
	pushl -8(%ebp)
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %edi
	pushl %eax
	pushl -8(%ebp)
	call set_subscript
	addl $12, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %ebx
	pushl %eax
	pushl -8(%ebp)
	call set_subscript
	addl $12, %esp
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -4(%ebp)
	pushl %eax
	pushl -8(%ebp)
	call set_subscript
	addl $12, %esp
	movl $4, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -16(%ebp)
	pushl %eax
	pushl -8(%ebp)
	call set_subscript
	addl $12, %esp
	movl $5, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -12(%ebp)
	pushl %eax
	pushl -8(%ebp)
	call set_subscript
	addl $12, %esp
	movl $42, %ebx
	sall $2, %ebx
	orl $0, %ebx
	movl $1, %esi
	sall $2, %esi
	orl $1, %esi
	movl $7, %edi
	sall $2, %edi
	orl $0, %edi
	call create_dict
	addl $0, %esp
	movl %eax, -4(%ebp)
	addl $3, -4(%ebp)
	pushl %esi
	pushl %edi
	pushl -4(%ebp)
	call set_subscript
	addl $12, %esp
	pushl -8(%ebp)
	pushl %ebx
	pushl -4(%ebp)
	call set_subscript
	addl $12, %esp
	movl -4(%ebp), %ecx
	movl $7, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl %ecx
	call get_subscript
	addl $8, %esp
	movl -24(%ebp), %esi
	movl -20(%ebp), %edi
	movl -16(%ebp), %ebx
	movl $0, %eax
	leave
	ret
