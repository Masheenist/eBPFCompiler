.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -4(%ebp)
	movl %edi, -8(%ebp)
	movl %esi, -12(%ebp)
	subl $16, %esp
	call input
	addl $0, %esp
	movl %eax, %edi
	sall $2, %edi
	orl $0, %edi
	call input
	addl $0, %esp
	movl %eax, %esi
	sall $2, %esi
	orl $0, %esi
	movl $2, %eax
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
	pushl %edi
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %esi
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl %ebx, -4(%ebp)
	call input
	addl $0, %esp
	movl %eax, %ebx
	sall $2, %ebx
	orl $0, %ebx
	call input
	addl $0, %esp
	movl %eax, %edi
	sall $2, %edi
	orl $0, %edi
	call create_dict
	addl $0, %esp
	movl %eax, %esi
	addl $3, %esi
	pushl %ebx
	pushl %edi
	pushl %esi
	call set_subscript
	addl $12, %esp
	movl %esi, %ebx
	pushl -4(%ebp)
	call print_any
	addl $4, %esp
	pushl %ebx
	call print_any
	addl $4, %esp
	movl -12(%ebp), %esi
	movl -8(%ebp), %edi
	movl -4(%ebp), %ebx
	movl $0, %eax
	leave
	ret
