.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -0(%ebp)
	movl %edi, -4(%ebp)
	movl %esi, -8(%ebp)
	subl $12, %esp
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	movl $1, %ecx
	sall $2, %ecx
	orl $0, %ecx
	movl %ecx, %edi
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
	movl %eax, %ecx
	jmp label_5
	label_4: 
	label_5: 
	cmpl $0, %ecx
	je label_6
	movl %esi, %eax
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
	movl -8(%ebp), %esi
	movl -4(%ebp), %edi
	movl -0(%ebp), %ebx
	movl $0, %eax
	leave
	ret
