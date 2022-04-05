.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -4(%ebp)
	movl %edi, -8(%ebp)
	movl %esi, -12(%ebp)
	subl $16, %esp
	movl $4, %edi
	sall $2, %edi
	orl $0, %edi
	movl $3, %ebx
	sall $2, %ebx
	orl $0, %ebx
	movl $5, -4(%ebp)
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
	movl %ebx, %edx
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	movl $5, %ecx
	sall $2, %ecx
	orl $0, %ecx
	pushl %ecx
	pushl %eax
	pushl %edx
	call set_subscript
	addl $12, %esp
	pushl %ebx
	call print_any
	addl $4, %esp
	movl -12(%ebp), %esi
	movl -8(%ebp), %edi
	movl -4(%ebp), %ebx
	movl $0, %eax
	leave
	ret
