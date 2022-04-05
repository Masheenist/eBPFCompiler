.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -16(%ebp)
	movl %edi, -20(%ebp)
	movl %esi, -24(%ebp)
	subl $28, %esp
	movl $1, -12(%ebp)
	sall $2, -12(%ebp)
	orl $0, -12(%ebp)
	movl $2, -8(%ebp)
	sall $2, -8(%ebp)
	orl $0, -8(%ebp)
	movl $10, %ebx
	sall $2, %ebx
	orl $0, %ebx
	movl $11, %edi
	sall $2, %edi
	orl $0, %edi
	movl $12, %esi
	sall $2, %esi
	orl $0, %esi
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	movl %eax, -16(%ebp)
	addl $3, -16(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %ebx
	pushl %eax
	pushl -16(%ebp)
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %edi
	pushl %eax
	pushl -16(%ebp)
	call set_subscript
	addl $12, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %esi
	pushl %eax
	pushl -16(%ebp)
	call set_subscript
	addl $12, %esp
	movl $1, %ebx
	sall $2, %ebx
	orl $0, %ebx
	movl $0, -4(%ebp)
	sall $2, -4(%ebp)
	orl $0, -4(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %esi
	movl %esi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_0
	movl %esi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_1
	label_0: 
	movl %ecx, %eax
	label_1: 
	cmpl $0, %eax
	je label_2
	movl %esi, %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %edi
	jmp label_3
	label_2: 
	call abort
	addl $0, %esp
	movl %eax, %edi
	label_3: 
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
	pushl %ebx
	pushl %eax
	pushl %esi
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -4(%ebp)
	pushl %eax
	pushl %esi
	call set_subscript
	addl $12, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %edi
	pushl %eax
	pushl %esi
	call set_subscript
	addl $12, %esp
	movl $4, %eax
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
	pushl -12(%ebp)
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -8(%ebp)
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -16(%ebp)
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %esi
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	pushl %ebx
	call print_any
	addl $4, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl %ebx
	call get_subscript
	addl $8, %esp
	pushl %eax
	call print_any
	addl $4, %esp
	movl -24(%ebp), %esi
	movl -20(%ebp), %edi
	movl -16(%ebp), %ebx
	movl $0, %eax
	leave
	ret
