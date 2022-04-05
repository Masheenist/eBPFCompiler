.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -0(%ebp)
	subl $4, %esp
	call create_dict
	addl $0, %esp
	addl $3, %eax
	movl %eax, %ebx
	movl $1, %ecx
	sall $2, %ecx
	orl $0, %ecx
	movl $1, %eax
	sall $2, %eax
	orl $1, %eax
	pushl %eax
	pushl %ecx
	pushl %ebx
	call set_subscript
	addl $12, %esp
	cmpl %ebx, %ebx
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
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
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	movl $0, %ecx
	sall $2, %ecx
	orl $1, %ecx
	pushl %ecx
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
	cmpl %ebx, %ebx
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	pushl %eax
	call print_any
	addl $4, %esp
	movl -0(%ebp), %ebx
	movl $0, %eax
	leave
	ret
