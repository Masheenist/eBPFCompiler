.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -20(%ebp)
	movl %edi, -24(%ebp)
	movl %esi, -28(%ebp)
	subl $32, %esp
	movl $1, -4(%ebp)
	sall $2, -4(%ebp)
	orl $0, -4(%ebp)
	movl $2, %esi
	sall $2, %esi
	orl $0, %esi
	movl $3, -16(%ebp)
	sall $2, -16(%ebp)
	orl $0, -16(%ebp)
	movl $1, -12(%ebp)
	sall $2, -12(%ebp)
	orl $1, -12(%ebp)
	movl $0, -8(%ebp)
	sall $2, -8(%ebp)
	orl $1, -8(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -20(%ebp)
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ebx
	movl -20(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_0
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_1
	label_0: 
	label_1: 
	cmpl $0, %eax
	je label_2
	movl -20(%ebp), %eax
	andl $-4, %eax
	movl %ebx, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_3
	label_2: 
	movl -20(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_4
	movl %ebx, %eax
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
	movl -20(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %edx
	cmpl $0, %edx
	je label_8
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_9
	label_8: 
	movl %edx, %eax
	label_9: 
	jmp label_7
	label_6: 
	movl %ecx, %eax
	label_7: 
	cmpl $0, %eax
	je label_10
	movl -20(%ebp), %ecx
	sarl $2, %ecx
	movl %ebx, %eax
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
	movl %ecx, -20(%ebp)
	movl $3, %eax
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
	je label_12
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_13
	label_12: 
	movl %ecx, %eax
	label_13: 
	cmpl $0, %eax
	je label_14
	movl %ebx, %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_15
	label_14: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_15: 
	movl %ecx, %ebx
	movl -20(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_16
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_17
	label_16: 
	label_17: 
	cmpl $0, %eax
	je label_18
	movl -20(%ebp), %eax
	andl $-4, %eax
	movl %ebx, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %edi
	jmp label_19
	label_18: 
	movl -20(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_20
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_21
	label_20: 
	movl %eax, %ecx
	label_21: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_22
	movl -20(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %edi
	cmpl $0, %edi
	je label_24
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_25
	label_24: 
	movl %edi, %eax
	label_25: 
	jmp label_23
	label_22: 
	movl %ecx, %eax
	label_23: 
	cmpl $0, %eax
	je label_26
	movl -20(%ebp), %eax
	sarl $2, %eax
	movl %ebx, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
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
	label_19: 
	movl $6, %eax
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
	pushl -16(%ebp)
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -12(%ebp)
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl $4, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -8(%ebp)
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl $5, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %edi
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl %ebx
	call get_subscript
	addl $8, %esp
	pushl %eax
	call print_any
	addl $4, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl %ebx
	call get_subscript
	addl $8, %esp
	pushl %eax
	call print_any
	addl $4, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl %ebx
	call get_subscript
	addl $8, %esp
	pushl %eax
	call print_any
	addl $4, %esp
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl %ebx
	call get_subscript
	addl $8, %esp
	pushl %eax
	call print_any
	addl $4, %esp
	movl $4, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl %ebx
	call get_subscript
	addl $8, %esp
	pushl %eax
	call print_any
	addl $4, %esp
	movl $5, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl %ebx
	call get_subscript
	addl $8, %esp
	pushl %eax
	call print_any
	addl $4, %esp
	movl -28(%ebp), %esi
	movl -24(%ebp), %edi
	movl -20(%ebp), %ebx
	movl $0, %eax
	leave
	ret
