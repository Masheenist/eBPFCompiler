.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -12(%ebp)
	movl %edi, -16(%ebp)
	movl %esi, -20(%ebp)
	subl $24, %esp
	movl $1, -4(%ebp)
	sall $2, -4(%ebp)
	orl $0, -4(%ebp)
	movl $2, %esi
	sall $2, %esi
	orl $0, %esi
	movl $3, -8(%ebp)
	sall $2, -8(%ebp)
	orl $0, -8(%ebp)
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	movl %eax, %edi
	addl $3, %edi
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -4(%ebp)
	pushl %eax
	pushl %edi
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %esi
	pushl %eax
	pushl %edi
	call set_subscript
	addl $12, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -8(%ebp)
	pushl %eax
	pushl %edi
	call set_subscript
	addl $12, %esp
	movl %edi, %eax
	movl %eax, %esi
	movl $1, -8(%ebp)
	sall $2, -8(%ebp)
	orl $0, -8(%ebp)
	movl $2, -12(%ebp)
	sall $2, -12(%ebp)
	orl $0, -12(%ebp)
	movl $3, %edi
	sall $2, %edi
	orl $0, %edi
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
	pushl -8(%ebp)
	pushl %eax
	pushl -4(%ebp)
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -12(%ebp)
	pushl %eax
	pushl -4(%ebp)
	call set_subscript
	addl $12, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %edi
	pushl %eax
	pushl -4(%ebp)
	call set_subscript
	addl $12, %esp
	movl -4(%ebp), %edi
	movl %esi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_0
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_1
	label_0: 
	label_1: 
	cmpl $0, %eax
	je label_2
	movl %esi, %eax
	andl $-4, %eax
	movl %edi, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call equal
	addl $8, %esp
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_3
	label_2: 
	movl %esi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_4
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_5
	label_4: 
	movl %ecx, %eax
	label_5: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_6
	movl %esi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ebx
	cmpl $0, %ebx
	je label_8
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_9
	label_8: 
	movl %ebx, %eax
	label_9: 
	jmp label_7
	label_6: 
	movl %ecx, %eax
	label_7: 
	cmpl $0, %eax
	je label_10
	movl %esi, %eax
	sarl $2, %eax
	movl %edi, %ecx
	sarl $2, %ecx
	cmpl %ecx, %eax
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_11
	label_10: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_11: 
	label_3: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -20(%ebp), %esi
	movl -16(%ebp), %edi
	movl -12(%ebp), %ebx
	movl $0, %eax
	leave
	ret
