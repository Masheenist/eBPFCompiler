.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -0(%ebp)
	movl %edi, -4(%ebp)
	movl %esi, -8(%ebp)
	subl $12, %esp
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
	movl $1, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_9
	label_8: 
	movl %esi, %ecx
	label_9: 
	movl %ecx, %eax
	movl %eax, %ebx
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
	movl %ebx, %edi
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
	movl %eax, %ecx
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
	label_11: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_18
	movl $0, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_19
	label_18: 
	movl %ebx, %ecx
	label_19: 
	movl %ecx, %eax
	pushl %eax
	call print_any
	addl $4, %esp
	movl -8(%ebp), %esi
	movl -4(%ebp), %edi
	movl -0(%ebp), %ebx
	movl $0, %eax
	leave
	ret
