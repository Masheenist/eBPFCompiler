.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -16(%ebp)
	movl %edi, -20(%ebp)
	movl %esi, -24(%ebp)
	subl $28, %esp
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	movl $5, %edx
	sall $2, %edx
	orl $0, %edx
	movl %edx, -8(%ebp)
	movl %eax, %esi
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -16(%ebp)
	movl %esi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_0
	movl -16(%ebp), %eax
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
	movl -16(%ebp), %ecx
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
	movl %eax, %edx
	cmpl $0, %edx
	je label_4
	movl -16(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_5
	label_4: 
	movl %edx, %eax
	label_5: 
	movl %eax, %edx
	cmpl $0, %edx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_6
	movl %esi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_8
	movl -16(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_9
	label_8: 
	movl %ecx, %eax
	label_9: 
	jmp label_7
	label_6: 
	movl %edx, %eax
	label_7: 
	cmpl $0, %eax
	je label_10
	movl %esi, %ecx
	sarl $2, %ecx
	movl -16(%ebp), %eax
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
	movl %ecx, %esi
	movl %esi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_12
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
	je label_14
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
	jmp label_15
	label_14: 
	movl %ebx, %ecx
	label_15: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_13
	label_12: 
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
	je label_16
	movl %esi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_17
	label_16: 
	movl %ecx, %eax
	label_17: 
	cmpl $0, %eax
	je label_18
	movl %esi, %eax
	sarl $2, %eax
	movl %eax, %ecx
	jmp label_19
	label_18: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_19: 
	movl %ecx, %eax
	label_13: 
	cmpl $0, %eax
	je label_20
	movl -8(%ebp), %edi
	movl $5, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -12(%ebp)
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_22
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_23
	label_22: 
	label_23: 
	cmpl $0, %eax
	je label_24
	movl %edi, %eax
	andl $-4, %eax
	movl -12(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call equal
	addl $8, %esp
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_25
	label_24: 
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_26
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_27
	label_26: 
	movl %ecx, %eax
	label_27: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_28
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -4(%ebp)
	cmpl $0, -4(%ebp)
	je label_30
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_31
	label_30: 
	movl -4(%ebp), %eax
	label_31: 
	jmp label_29
	label_28: 
	movl %ecx, %eax
	label_29: 
	cmpl $0, %eax
	je label_32
	movl %edi, %eax
	sarl $2, %eax
	movl -12(%ebp), %ecx
	sarl $2, %ecx
	cmpl %ecx, %eax
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_33
	label_32: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_33: 
	label_25: 
	movl %ecx, %eax
	jmp label_21
	label_20: 
	movl %esi, %eax
	label_21: 
	movl $1, %eax
	sall $2, %eax
	orl $1, %eax
	pushl %eax
	call print_any
	addl $4, %esp
	movl -24(%ebp), %esi
	movl -20(%ebp), %edi
	movl -16(%ebp), %ebx
	movl $0, %eax
	leave
	ret
