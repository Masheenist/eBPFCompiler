.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -16(%ebp)
	movl %edi, -20(%ebp)
	movl %esi, -24(%ebp)
	subl $28, %esp
	movl $0, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %esi
	movl %esi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %ecx
	cmpl $0, %ecx
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
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_8
	movl $5, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %esi
	movl $6, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ebx
	movl %esi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_10
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_11
	label_10: 
	label_11: 
	cmpl $0, %eax
	je label_12
	movl %esi, %eax
	andl $-4, %eax
	movl %ebx, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call equal
	addl $8, %esp
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_13
	label_12: 
	movl %esi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_14
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_15
	label_14: 
	movl %eax, %ecx
	label_15: 
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
	movl %eax, -8(%ebp)
	cmpl $0, -8(%ebp)
	je label_18
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_19
	label_18: 
	movl -8(%ebp), %eax
	label_19: 
	jmp label_17
	label_16: 
	movl %ecx, %eax
	label_17: 
	cmpl $0, %eax
	je label_20
	movl %esi, %ecx
	sarl $2, %ecx
	movl %ebx, %eax
	sarl $2, %eax
	cmpl %eax, %ecx
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_21
	label_20: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_21: 
	label_13: 
	movl %ecx, -8(%ebp)
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_22
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
	movl %eax, -16(%ebp)
	cmpl $0, -16(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_24
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
	jmp label_25
	label_24: 
	movl -16(%ebp), %ecx
	label_25: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_23
	label_22: 
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
	je label_26
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_27
	label_26: 
	movl %ecx, %eax
	label_27: 
	cmpl $0, %eax
	je label_28
	movl -8(%ebp), %eax
	sarl $2, %eax
	movl %eax, %ecx
	jmp label_29
	label_28: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_29: 
	movl %ecx, %eax
	label_23: 
	cmpl $0, %eax
	je label_30
	movl $7, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %edi
	movl $8, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -4(%ebp)
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_32
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_33
	label_32: 
	label_33: 
	cmpl $0, %eax
	je label_34
	movl %edi, %eax
	andl $-4, %eax
	movl -4(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call equal
	addl $8, %esp
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_35
	label_34: 
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_36
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_37
	label_36: 
	movl %ecx, %eax
	label_37: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_38
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -12(%ebp)
	cmpl $0, -12(%ebp)
	je label_40
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_41
	label_40: 
	movl -12(%ebp), %eax
	label_41: 
	jmp label_39
	label_38: 
	movl %ecx, %eax
	label_39: 
	cmpl $0, %eax
	je label_42
	movl %edi, %ecx
	sarl $2, %ecx
	movl -4(%ebp), %eax
	sarl $2, %eax
	cmpl %eax, %ecx
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_43
	label_42: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_43: 
	label_35: 
	jmp label_31
	label_30: 
	movl -8(%ebp), %ecx
	label_31: 
	jmp label_9
	label_8: 
	movl %esi, %ecx
	label_9: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -24(%ebp), %esi
	movl -20(%ebp), %edi
	movl -16(%ebp), %ebx
	movl $0, %eax
	leave
	ret
