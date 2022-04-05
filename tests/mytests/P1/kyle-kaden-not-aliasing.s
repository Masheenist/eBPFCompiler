.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -4(%ebp)
	movl %edi, -8(%ebp)
	movl %esi, -12(%ebp)
	subl $16, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %edi
	movl %edi, %esi
	cmpl %edi, %esi
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	pushl %eax
	call print_any
	addl $4, %esp
	movl %edi, -4(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %edi
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_0
	movl %edi, %eax
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
	movl %edi, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
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
	movl %edi, %eax
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
	movl %eax, %ebx
	cmpl $0, %ebx
	je label_8
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_9
	label_8: 
	movl %ebx, %eax
	label_9: 
	jmp label_7
	label_6: 
	movl %ecx, %eax
	label_7: 
	cmpl $0, %eax
	je label_10
	movl -4(%ebp), %eax
	sarl $2, %eax
	movl %edi, %ecx
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
	movl %ecx, %edi
	pushl %edi
	call print_any
	addl $4, %esp
	pushl %esi
	call print_any
	addl $4, %esp
	cmpl %edi, %esi
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	pushl %eax
	call print_any
	addl $4, %esp
	movl -12(%ebp), %esi
	movl -8(%ebp), %edi
	movl -4(%ebp), %ebx
	movl $0, %eax
	leave
	ret
