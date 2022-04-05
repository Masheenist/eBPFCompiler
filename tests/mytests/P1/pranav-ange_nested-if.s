.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -12(%ebp)
	movl %edi, -16(%ebp)
	movl %esi, -20(%ebp)
	subl $24, %esp
	movl $1, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %esi
	call input
	addl $0, %esp
	sall $2, %eax
	orl $0, %eax
	movl %eax, -4(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, -8(%ebp)
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_0
	movl -8(%ebp), %ebx
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
	movl -8(%ebp), %ebx
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
	movl -8(%ebp), %eax
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
	movl -8(%ebp), %eax
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
	movl -8(%ebp), %eax
	sarl $2, %eax
	jmp label_7
	label_6: 
	call abort
	addl $0, %esp
	label_7: 
	label_1: 
	cmpl $0, %eax
	je label_8
	movl $7, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_9
	label_8: 
	movl -4(%ebp), %ebx
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_10
	movl %ebx, %edi
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
	movl %edi, %ecx
	label_13: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_11
	label_10: 
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
	call input
	addl $0, %esp
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_19
	label_18: 
	movl %esi, %ebx
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_20
	movl %ebx, %edi
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
	movl %eax, -12(%ebp)
	cmpl $0, -12(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_22
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
	jmp label_23
	label_22: 
	movl -12(%ebp), %ecx
	label_23: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_21
	label_20: 
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
	je label_24
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_25
	label_24: 
	movl %ecx, %eax
	label_25: 
	cmpl $0, %eax
	je label_26
	movl %ebx, %eax
	sarl $2, %eax
	movl %eax, %ecx
	jmp label_27
	label_26: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_27: 
	movl %ecx, %eax
	label_21: 
	cmpl $0, %eax
	je label_28
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_29
	label_28: 
	movl $25, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	label_29: 
	label_19: 
	label_9: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -20(%ebp), %esi
	movl -16(%ebp), %edi
	movl -12(%ebp), %ebx
	movl $0, %eax
	leave
	ret
