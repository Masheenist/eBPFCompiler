.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	subl $0, %esp
	movl %ebx, -4(%ebp)
	movl %edi, -8(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %edi
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ebx
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je main_label_0
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp main_label_1
	main_label_0: 
	main_label_1: 
	cmpl $0, %eax
	je main_label_2
	movl %edi, %eax
	andl $-4, %eax
	movl %ebx, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp main_label_3
	main_label_2: 
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je main_label_4
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp main_label_5
	main_label_4: 
	movl %eax, %ecx
	main_label_5: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je main_label_6
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %edx
	cmpl $0, %edx
	je main_label_8
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp main_label_9
	main_label_8: 
	movl %edx, %eax
	main_label_9: 
	jmp main_label_7
	main_label_6: 
	movl %ecx, %eax
	main_label_7: 
	cmpl $0, %eax
	je main_label_10
	movl %edi, %eax
	sarl $2, %eax
	movl %ebx, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp main_label_11
	main_label_10: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	main_label_11: 
	main_label_3: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl $0, %eax
	main_end:
	movl -8(%ebp), %edi
	movl -4(%ebp), %ebx
	leave
	ret
