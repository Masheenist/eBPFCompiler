.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -24(%ebp)
	movl %edi, -28(%ebp)
	movl %esi, -32(%ebp)
	subl $36, %esp
	call create_dict
	addl $0, %esp
	addl $3, %eax
	movl %eax, %ebx
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	movl $0, %ecx
	sall $2, %ecx
	orl $1, %ecx
	pushl %ecx
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl $1, %ecx
	sall $2, %ecx
	orl $0, %ecx
	movl $1, %eax
	sall $2, %eax
	orl $1, %eax
	pushl %eax
	pushl %ecx
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl $0, %eax
	sall $2, %eax
	orl $1, %eax
	movl $0, %ecx
	sall $2, %ecx
	orl $0, %ecx
	pushl %ecx
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl $1, %ecx
	sall $2, %ecx
	orl $1, %ecx
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl %ecx
	pushl %ebx
	call set_subscript
	addl $12, %esp
	pushl %ebx
	call print_any
	addl $4, %esp
	movl $0, -12(%ebp)
	sall $2, -12(%ebp)
	orl $1, -12(%ebp)
	movl $0, -4(%ebp)
	sall $2, -4(%ebp)
	orl $0, -4(%ebp)
	movl $1, -24(%ebp)
	sall $2, -24(%ebp)
	orl $1, -24(%ebp)
	movl $1, -20(%ebp)
	sall $2, -20(%ebp)
	orl $0, -20(%ebp)
	movl $1, %edi
	sall $2, %edi
	orl $0, %edi
	movl $1, %esi
	sall $2, %esi
	orl $1, %esi
	movl $0, -8(%ebp)
	sall $2, -8(%ebp)
	orl $0, -8(%ebp)
	movl $0, -16(%ebp)
	sall $2, -16(%ebp)
	orl $1, -16(%ebp)
	call create_dict
	addl $0, %esp
	movl %eax, %ebx
	addl $3, %ebx
	pushl -12(%ebp)
	pushl -4(%ebp)
	pushl %ebx
	call set_subscript
	addl $12, %esp
	pushl -8(%ebp)
	pushl -16(%ebp)
	pushl %ebx
	call set_subscript
	addl $12, %esp
	pushl %edi
	pushl %esi
	pushl %ebx
	call set_subscript
	addl $12, %esp
	pushl -24(%ebp)
	pushl -20(%ebp)
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl %ebx, %eax
	pushl %eax
	call print_any
	addl $4, %esp
	movl -32(%ebp), %esi
	movl -28(%ebp), %edi
	movl -24(%ebp), %ebx
	movl $0, %eax
	leave
	ret
