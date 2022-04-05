.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -8(%ebp)
	movl %edi, -12(%ebp)
	movl %esi, -16(%ebp)
	subl $20, %esp
	movl $1, %ebx
	sall $2, %ebx
	orl $0, %ebx
	movl $2, %edi
	sall $2, %edi
	orl $0, %edi
	movl $3, %esi
	sall $2, %esi
	orl $0, %esi
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	movl %eax, -4(%ebp)
	addl $3, -4(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %ebx
	pushl %eax
	pushl -4(%ebp)
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %edi
	pushl %eax
	pushl -4(%ebp)
	call set_subscript
	addl $12, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %esi
	pushl %eax
	pushl -4(%ebp)
	call set_subscript
	addl $12, %esp
	movl $1, -8(%ebp)
	sall $2, -8(%ebp)
	orl $0, -8(%ebp)
	movl $1, %edi
	sall $2, %edi
	orl $1, %edi
	movl $4, %ebx
	sall $2, %ebx
	orl $0, %ebx
	call create_dict
	addl $0, %esp
	movl %eax, %esi
	addl $3, %esi
	pushl -4(%ebp)
	pushl -8(%ebp)
	pushl %esi
	call set_subscript
	addl $12, %esp
	pushl %edi
	pushl %ebx
	pushl %esi
	call set_subscript
	addl $12, %esp
	movl %esi, %ebx
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl %ebx
	call get_subscript
	addl $8, %esp
	movl $1, %edx
	sall $2, %edx
	orl $0, %edx
	movl $99, %ecx
	sall $2, %ecx
	orl $0, %ecx
	pushl %ecx
	pushl %edx
	pushl %eax
	call set_subscript
	addl $12, %esp
	pushl %ebx
	call print_any
	addl $4, %esp
	movl -16(%ebp), %esi
	movl -12(%ebp), %edi
	movl -8(%ebp), %ebx
	movl $0, %eax
	leave
	ret
