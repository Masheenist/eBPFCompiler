.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -16(%ebp)
	movl %edi, -20(%ebp)
	movl %esi, -24(%ebp)
	subl $28, %esp
	movl $2, -4(%ebp)
	sall $2, -4(%ebp)
	orl $0, -4(%ebp)
	movl $1, %esi
	sall $2, %esi
	orl $0, %esi
	movl $4, -12(%ebp)
	sall $2, -12(%ebp)
	orl $0, -12(%ebp)
	movl $3, -8(%ebp)
	sall $2, -8(%ebp)
	orl $0, -8(%ebp)
	call create_dict
	addl $0, %esp
	movl %eax, -16(%ebp)
	addl $3, -16(%ebp)
	pushl -12(%ebp)
	pushl -8(%ebp)
	pushl -16(%ebp)
	call set_subscript
	addl $12, %esp
	pushl -4(%ebp)
	pushl %esi
	pushl -16(%ebp)
	call set_subscript
	addl $12, %esp
	movl -16(%ebp), %eax
	movl %eax, -4(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $1, %eax
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
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ebx
	jmp label_9
	label_8: 
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ebx
	label_9: 
	movl %esi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_10
	movl %esi, %edi
	andl $-4, %edi
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl %edi
	call equal
	addl $8, %esp
	movl %eax, %edi
	cmpl $0, %edi
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_12
	movl %esi, %edi
	andl $-4, %edi
	call create_dict
	addl $0, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl %edi
	call equal
	addl $8, %esp
	movl %eax, %ecx
	jmp label_13
	label_12: 
	movl %edi, %ecx
	label_13: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_11
	label_10: 
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
	je label_14
	movl %esi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_15
	label_14: 
	label_15: 
	cmpl $0, %ecx
	je label_16
	movl %esi, %eax
	sarl $2, %eax
	jmp label_17
	label_16: 
	call abort
	addl $0, %esp
	label_17: 
	label_11: 
	cmpl $0, %eax
	je label_18
	call input
	addl $0, %esp
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_19
	label_18: 
	movl $25, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	label_19: 
	pushl %ecx
	pushl %ebx
	pushl -4(%ebp)
	call set_subscript
	addl $12, %esp
	pushl -4(%ebp)
	call print_any
	addl $4, %esp
	movl -24(%ebp), %esi
	movl -20(%ebp), %edi
	movl -16(%ebp), %ebx
	movl $0, %eax
	leave
	ret
