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
	movl $2, %ebx
	sall $2, %ebx
	orl $0, %ebx
	movl $2, %eax
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
	pushl %ebx
	pushl %eax
	pushl -4(%ebp)
	call set_subscript
	addl $12, %esp
	movl -4(%ebp), %esi
	movl $1, -8(%ebp)
	sall $2, -8(%ebp)
	orl $0, -8(%ebp)
	movl $2, -4(%ebp)
	sall $2, -4(%ebp)
	orl $0, -4(%ebp)
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
	pushl -8(%ebp)
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -4(%ebp)
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl %ebx, %eax
	movl %esi, %ebx
	movl %eax, %esi
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_0
	movl %esi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_1
	label_0: 
	label_1: 
	cmpl $0, %eax
	je label_2
	movl %ebx, %eax
	andl $-4, %eax
	movl %esi, %ecx
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
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_4
	movl %esi, %eax
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
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %edi
	cmpl $0, %edi
	je label_8
	movl %esi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_9
	label_8: 
	movl %edi, %eax
	label_9: 
	jmp label_7
	label_6: 
	movl %ecx, %eax
	label_7: 
	cmpl $0, %eax
	je label_10
	movl %ebx, %ecx
	sarl $2, %ecx
	movl %esi, %eax
	sarl $2, %eax
	cmpl %eax, %ecx
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
	movl -16(%ebp), %esi
	movl -12(%ebp), %edi
	movl -8(%ebp), %ebx
	movl $0, %eax
	leave
	ret
