.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -12(%ebp)
	movl %edi, -16(%ebp)
	movl %esi, -20(%ebp)
	subl $24, %esp
	call create_dict
	addl $0, %esp
	addl $3, %eax
	movl %eax, -4(%ebp)
	call input
	addl $0, %esp
	sall $2, %eax
	orl $0, %eax
	movl %eax, -8(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -12(%ebp)
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_0
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_1
	label_0: 
	label_1: 
	cmpl $0, %eax
	je label_2
	movl -8(%ebp), %eax
	andl $-4, %eax
	movl -12(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_3
	label_2: 
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_4
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_5
	label_4: 
	movl %eax, %ecx
	label_5: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_6
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %edi
	cmpl $0, %edi
	je label_8
	movl -12(%ebp), %eax
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
	movl -8(%ebp), %eax
	sarl $2, %eax
	movl -12(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_11
	label_10: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_11: 
	label_3: 
	movl %ecx, -8(%ebp)
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %edi
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_12
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_13
	label_12: 
	label_13: 
	cmpl $0, %eax
	je label_14
	movl -8(%ebp), %eax
	andl $-4, %eax
	movl %edi, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_15
	label_14: 
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_16
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_17
	label_16: 
	movl %eax, %ecx
	label_17: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_18
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %esi
	cmpl $0, %esi
	je label_20
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_21
	label_20: 
	movl %esi, %eax
	label_21: 
	jmp label_19
	label_18: 
	movl %ecx, %eax
	label_19: 
	cmpl $0, %eax
	je label_22
	movl -8(%ebp), %eax
	sarl $2, %eax
	movl %edi, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_23
	label_22: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_23: 
	label_15: 
	movl %ecx, %esi
	movl $3, %eax
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
	je label_24
	movl %edi, %eax
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
	movl %edi, %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_27
	label_26: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_27: 
	movl %ecx, %edi
	movl %esi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_28
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_29
	label_28: 
	label_29: 
	cmpl $0, %eax
	je label_30
	movl %esi, %eax
	andl $-4, %eax
	movl %edi, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_31
	label_30: 
	movl %esi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_32
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_33
	label_32: 
	movl %eax, %ecx
	label_33: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_34
	movl %esi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ebx
	cmpl $0, %ebx
	je label_36
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_37
	label_36: 
	movl %ebx, %eax
	label_37: 
	jmp label_35
	label_34: 
	movl %ecx, %eax
	label_35: 
	cmpl $0, %eax
	je label_38
	movl %esi, %eax
	sarl $2, %eax
	movl %edi, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_39
	label_38: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_39: 
	label_31: 
	movl $1, %eax
	sall $2, %eax
	orl $1, %eax
	pushl %eax
	pushl %ecx
	pushl -4(%ebp)
	call set_subscript
	addl $12, %esp
	pushl -4(%ebp)
	call print_any
	addl $4, %esp
	movl -20(%ebp), %esi
	movl -16(%ebp), %edi
	movl -12(%ebp), %ebx
	movl $0, %eax
	leave
	ret
