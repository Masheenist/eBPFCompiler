.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -8(%ebp)
	movl %edi, -12(%ebp)
	movl %esi, -16(%ebp)
	subl $20, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %edi
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %esi
	movl $1, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, -4(%ebp)
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_0
	movl -4(%ebp), %eax
	movl %eax, -8(%ebp)
	andl $-4, -8(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -8(%ebp)
	call equal
	addl $8, %esp
	movl %eax, -8(%ebp)
	cmpl $0, -8(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_2
	movl -4(%ebp), %eax
	movl %eax, -4(%ebp)
	andl $-4, -4(%ebp)
	call create_dict
	addl $0, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -4(%ebp)
	call equal
	addl $8, %esp
	movl %eax, %ecx
	jmp label_3
	label_2: 
	movl -8(%ebp), %ecx
	label_3: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_1
	label_0: 
	movl -4(%ebp), %eax
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
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_5
	label_4: 
	label_5: 
	cmpl $0, %ecx
	je label_6
	movl -4(%ebp), %eax
	sarl $2, %eax
	jmp label_7
	label_6: 
	call abort
	addl $0, %esp
	label_7: 
	label_1: 
	cmpl $0, %eax
	je label_8
	movl %edi, %ecx
	jmp label_9
	label_8: 
	movl %esi, %ecx
	label_9: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl $0, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, -4(%ebp)
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_10
	movl -4(%ebp), %ebx
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
	je label_12
	movl -4(%ebp), %ebx
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
	jmp label_13
	label_12: 
	movl %ebx, %ecx
	label_13: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_11
	label_10: 
	movl -4(%ebp), %eax
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
	movl -4(%ebp), %eax
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
	movl -4(%ebp), %eax
	sarl $2, %eax
	movl %eax, %ecx
	jmp label_17
	label_16: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_17: 
	movl %ecx, %eax
	label_11: 
	cmpl $0, %eax
	je label_18
	movl %edi, %ecx
	jmp label_19
	label_18: 
	movl %esi, %ecx
	label_19: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -16(%ebp), %esi
	movl -12(%ebp), %edi
	movl -8(%ebp), %ebx
	movl $0, %eax
	leave
	ret
