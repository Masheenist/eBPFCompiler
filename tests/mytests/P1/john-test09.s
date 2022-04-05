.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -8(%ebp)
	movl %edi, -12(%ebp)
	movl %esi, -16(%ebp)
	subl $20, %esp
	movl $1, %esi
	sall $2, %esi
	orl $0, %esi
	movl $2, %edi
	sall $2, %edi
	orl $0, %edi
	movl $3, %ebx
	sall $2, %ebx
	orl $0, %ebx
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
	pushl %esi
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
	pushl %ebx
	pushl %eax
	pushl -4(%ebp)
	call set_subscript
	addl $12, %esp
	movl -4(%ebp), %eax
	movl %eax, -8(%ebp)
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
	cmpl %esi, -8(%ebp)
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	pushl %eax
	call print_any
	addl $4, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -8(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	cmpl %eax, -8(%ebp)
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	pushl %eax
	call print_any
	addl $4, %esp
	movl -16(%ebp), %esi
	movl -12(%ebp), %edi
	movl -8(%ebp), %ebx
	movl $0, %eax
	leave
	ret
