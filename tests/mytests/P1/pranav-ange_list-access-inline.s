.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -4(%ebp)
	movl %edi, -8(%ebp)
	movl %esi, -12(%ebp)
	subl $16, %esp
	call input
	addl $0, %esp
	sall $2, %eax
	orl $0, %eax
	movl %eax, -4(%ebp)
	movl $10, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %esi
	movl -4(%ebp), %eax
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
	movl -4(%ebp), %eax
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
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_4
	movl %esi, %eax
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
	movl -4(%ebp), %eax
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
	movl -4(%ebp), %eax
	sarl $2, %eax
	movl %esi, %ecx
	sarl $2, %ecx
	cmpl %ecx, %eax
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
	movl $1, %esi
	sall $2, %esi
	orl $0, %esi
	movl $2, -4(%ebp)
	sall $2, -4(%ebp)
	orl $0, -4(%ebp)
	movl $3, %ebx
	sall $2, %ebx
	orl $0, %ebx
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	movl %eax, %edi
	addl $3, %edi
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %esi
	pushl %eax
	pushl %edi
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -4(%ebp)
	pushl %eax
	pushl %edi
	call set_subscript
	addl $12, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %ebx
	pushl %eax
	pushl %edi
	call set_subscript
	addl $12, %esp
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl %edi
	call get_subscript
	addl $8, %esp
	movl %eax, %ecx
	jmp label_21
	label_20: 
	movl $4, -4(%ebp)
	sall $2, -4(%ebp)
	orl $0, -4(%ebp)
	movl $5, %esi
	sall $2, %esi
	orl $0, %esi
	movl $6, %ebx
	sall $2, %ebx
	orl $0, %ebx
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	movl %eax, %edi
	addl $3, %edi
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -4(%ebp)
	pushl %eax
	pushl %edi
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %esi
	pushl %eax
	pushl %edi
	call set_subscript
	addl $12, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %ebx
	pushl %eax
	pushl %edi
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl %edi
	call get_subscript
	addl $8, %esp
	movl %eax, %ecx
	label_21: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -12(%ebp), %esi
	movl -8(%ebp), %edi
	movl -4(%ebp), %ebx
	movl $0, %eax
	leave
	ret
