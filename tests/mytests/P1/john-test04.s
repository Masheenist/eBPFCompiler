.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -16(%ebp)
	movl %edi, -20(%ebp)
	movl %esi, -24(%ebp)
	subl $28, %esp
	call input
	addl $0, %esp
	sall $2, %eax
	orl $0, %eax
	movl %eax, %edi
	call input
	addl $0, %esp
	sall $2, %eax
	orl $0, %eax
	movl %eax, -16(%ebp)
	movl %edi, %eax
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
	movl %edi, %eax
	andl $-4, %eax
	movl -16(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_3
	label_2: 
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_4
	movl -16(%ebp), %eax
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
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -12(%ebp)
	cmpl $0, -12(%ebp)
	je label_8
	movl -16(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_9
	label_8: 
	movl -12(%ebp), %eax
	label_9: 
	jmp label_7
	label_6: 
	movl %ecx, %eax
	label_7: 
	cmpl $0, %eax
	je label_10
	movl %edi, %ecx
	sarl $2, %ecx
	movl -16(%ebp), %eax
	sarl $2, %eax
	addl %eax, %ecx
	movl %ecx, %eax
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
	movl %ecx, %edi
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_12
	movl %edi, %ebx
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
	movl %edi, %ebx
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
	je label_16
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_17
	label_16: 
	label_17: 
	cmpl $0, %ecx
	je label_18
	movl %edi, %eax
	sarl $2, %eax
	jmp label_19
	label_18: 
	call abort
	addl $0, %esp
	label_19: 
	label_13: 
	cmpl $0, %eax
	je label_20
	call input
	addl $0, %esp
	sall $2, %eax
	orl $0, %eax
	movl %eax, %esi
	call input
	addl $0, %esp
	sall $2, %eax
	orl $0, %eax
	movl %eax, -8(%ebp)
	movl %esi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_22
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_23
	label_22: 
	label_23: 
	cmpl $0, %eax
	je label_24
	movl %esi, %eax
	andl $-4, %eax
	movl -8(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_25
	label_24: 
	movl %esi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_26
	movl -8(%ebp), %eax
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
	movl %esi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -4(%ebp)
	cmpl $0, -4(%ebp)
	je label_30
	movl -8(%ebp), %eax
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
	movl %esi, %ecx
	sarl $2, %ecx
	movl -8(%ebp), %eax
	sarl $2, %eax
	addl %eax, %ecx
	movl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_33
	label_32: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_33: 
	label_25: 
	jmp label_21
	label_20: 
	call input
	addl $0, %esp
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ebx
	call input
	addl $0, %esp
	sall $2, %eax
	orl $0, %eax
	movl %eax, %edi
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_34
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_35
	label_34: 
	label_35: 
	cmpl $0, %eax
	je label_36
	movl %ebx, %eax
	andl $-4, %eax
	movl %edi, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_37
	label_36: 
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_38
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_39
	label_38: 
	movl %eax, %ecx
	label_39: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_40
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -4(%ebp)
	cmpl $0, -4(%ebp)
	je label_42
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_43
	label_42: 
	movl -4(%ebp), %eax
	label_43: 
	jmp label_41
	label_40: 
	movl %ecx, %eax
	label_41: 
	cmpl $0, %eax
	je label_44
	movl %ebx, %eax
	sarl $2, %eax
	movl %edi, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_45
	label_44: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_45: 
	label_37: 
	label_21: 
	movl %ecx, %eax
	pushl %eax
	call print_any
	addl $4, %esp
	movl -24(%ebp), %esi
	movl -20(%ebp), %edi
	movl -16(%ebp), %ebx
	movl $0, %eax
	leave
	ret
