.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -8(%ebp)
	movl %edi, -12(%ebp)
	movl %esi, -16(%ebp)
	subl $20, %esp
	call input
	addl $0, %esp
	sall $2, %eax
	orl $0, %eax
	movl %eax, %esi
	movl %esi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_0
	movl %esi, %ebx
	andl $-4, %ebx
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl %ebx
	call equal
	addl $8, %esp
	movl %eax, %ebx
	cmpl $0, %ebx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_2
	movl %esi, %ebx
	andl $-4, %ebx
	call create_dict
	addl $0, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl %ebx
	call equal
	addl $8, %esp
	movl %eax, %ecx
	jmp label_3
	label_2: 
	movl %ebx, %ecx
	label_3: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_1
	label_0: 
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
	je label_4
	movl %esi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_5
	label_4: 
	movl %ecx, %eax
	label_5: 
	cmpl $0, %eax
	je label_6
	movl %esi, %eax
	sarl $2, %eax
	movl %eax, %ecx
	jmp label_7
	label_6: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_7: 
	movl %ecx, %eax
	label_1: 
	cmpl $0, %eax
	je label_8
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %edi
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_10
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_11
	label_10: 
	label_11: 
	cmpl $0, %ecx
	je label_12
	movl %edi, %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	jmp label_13
	label_12: 
	call abort
	addl $0, %esp
	label_13: 
	movl %eax, %ecx
	jmp label_9
	label_8: 
	movl $1, -4(%ebp)
	sall $2, -4(%ebp)
	orl $0, -4(%ebp)
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ebx
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_14
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_15
	label_14: 
	movl %ecx, %eax
	label_15: 
	cmpl $0, %eax
	je label_16
	movl %ebx, %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %esi
	jmp label_17
	label_16: 
	call abort
	addl $0, %esp
	movl %eax, %esi
	label_17: 
	movl $3, -8(%ebp)
	sall $2, -8(%ebp)
	orl $0, -8(%ebp)
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
	pushl -4(%ebp)
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
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -8(%ebp)
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl %ebx, %ecx
	label_9: 
	movl %ecx, %eax
	pushl %eax
	call print_any
	addl $4, %esp
	movl -16(%ebp), %esi
	movl -12(%ebp), %edi
	movl -8(%ebp), %ebx
	movl $0, %eax
	leave
	ret
