.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -60(%ebp)
	movl %edi, -64(%ebp)
	movl %esi, -68(%ebp)
	subl $72, %esp
	movl $1, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, -36(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %esi
	movl %esi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_0
	movl %esi, -48(%ebp)
	andl $-4, -48(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -48(%ebp)
	call equal
	addl $8, %esp
	movl %eax, -48(%ebp)
	cmpl $0, -48(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_2
	movl %esi, -48(%ebp)
	andl $-4, -48(%ebp)
	call create_dict
	addl $0, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -48(%ebp)
	call equal
	addl $8, %esp
	movl %eax, %ecx
	jmp label_3
	label_2: 
	movl -48(%ebp), %ecx
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
	je label_8
	call input
	addl $0, %esp
	sall $2, %eax
	orl $0, %eax
	movl %eax, -60(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -56(%ebp)
	movl -60(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_10
	movl -56(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_11
	label_10: 
	label_11: 
	cmpl $0, %eax
	je label_12
	movl -60(%ebp), %eax
	andl $-4, %eax
	movl -56(%ebp), %ecx
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
	movl -60(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_14
	movl -56(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_15
	label_14: 
	movl %ecx, %eax
	label_15: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_16
	movl -60(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -52(%ebp)
	cmpl $0, -52(%ebp)
	je label_18
	movl -56(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_19
	label_18: 
	movl -52(%ebp), %eax
	label_19: 
	jmp label_17
	label_16: 
	movl %ecx, %eax
	label_17: 
	cmpl $0, %eax
	je label_20
	movl -60(%ebp), %ecx
	sarl $2, %ecx
	movl -56(%ebp), %eax
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
	jmp label_9
	label_8: 
	movl %esi, %ecx
	label_9: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -36(%ebp), %eax
	movl %eax, -48(%ebp)
	movl -48(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_22
	movl -48(%ebp), %eax
	movl %eax, -32(%ebp)
	andl $-4, -32(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -32(%ebp)
	call equal
	addl $8, %esp
	movl %eax, -32(%ebp)
	cmpl $0, -32(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_24
	movl -48(%ebp), %eax
	movl %eax, -32(%ebp)
	andl $-4, -32(%ebp)
	call create_dict
	addl $0, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -32(%ebp)
	call equal
	addl $8, %esp
	movl %eax, %ecx
	jmp label_25
	label_24: 
	movl -32(%ebp), %ecx
	label_25: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_23
	label_22: 
	movl -48(%ebp), %eax
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
	movl -48(%ebp), %eax
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
	movl -48(%ebp), %eax
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
	call input
	addl $0, %esp
	sall $2, %eax
	orl $0, %eax
	movl %eax, -44(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -40(%ebp)
	movl -44(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_32
	movl -40(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_33
	label_32: 
	label_33: 
	cmpl $0, %eax
	je label_34
	movl -44(%ebp), %eax
	andl $-4, %eax
	movl -40(%ebp), %ecx
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
	movl -44(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_36
	movl -40(%ebp), %eax
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
	movl -44(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -28(%ebp)
	cmpl $0, -28(%ebp)
	je label_40
	movl -40(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_41
	label_40: 
	movl -28(%ebp), %eax
	label_41: 
	jmp label_39
	label_38: 
	movl %ecx, %eax
	label_39: 
	cmpl $0, %eax
	je label_42
	movl -44(%ebp), %ecx
	sarl $2, %ecx
	movl -40(%ebp), %eax
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
	movl -48(%ebp), %ecx
	label_31: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -36(%ebp), %eax
	movl %eax, -28(%ebp)
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %ecx
	cmpl $0, %ecx
	je label_44
	movl -28(%ebp), %ebx
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
	je label_46
	movl -28(%ebp), %ebx
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
	jmp label_47
	label_46: 
	movl %ebx, %ecx
	label_47: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_45
	label_44: 
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_48
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_49
	label_48: 
	label_49: 
	cmpl $0, %ecx
	je label_50
	movl -28(%ebp), %eax
	sarl $2, %eax
	jmp label_51
	label_50: 
	call abort
	addl $0, %esp
	label_51: 
	label_45: 
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_52
	call input
	addl $0, %esp
	sall $2, %eax
	orl $0, %eax
	movl %eax, -16(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -12(%ebp)
	movl -16(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_54
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_55
	label_54: 
	label_55: 
	cmpl $0, %eax
	je label_56
	movl -16(%ebp), %eax
	andl $-4, %eax
	movl -12(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call equal
	addl $8, %esp
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_57
	label_56: 
	movl -16(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_58
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_59
	label_58: 
	movl %eax, %ecx
	label_59: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_60
	movl -16(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -20(%ebp)
	cmpl $0, -20(%ebp)
	je label_62
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_63
	label_62: 
	movl -20(%ebp), %eax
	label_63: 
	jmp label_61
	label_60: 
	movl %ecx, %eax
	label_61: 
	cmpl $0, %eax
	je label_64
	movl -16(%ebp), %ecx
	sarl $2, %ecx
	movl -12(%ebp), %eax
	sarl $2, %eax
	cmpl %eax, %ecx
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_65
	label_64: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_65: 
	label_57: 
	jmp label_53
	label_52: 
	movl -28(%ebp), %ecx
	label_53: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl %esi, %ebx
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %ecx
	cmpl $0, %ecx
	je label_66
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
	je label_68
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
	jmp label_69
	label_68: 
	movl %edi, %ecx
	label_69: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_67
	label_66: 
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
	je label_70
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_71
	label_70: 
	movl %ecx, %eax
	label_71: 
	cmpl $0, %eax
	je label_72
	movl %ebx, %eax
	sarl $2, %eax
	movl %eax, %ecx
	jmp label_73
	label_72: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_73: 
	movl %ecx, %eax
	label_67: 
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_74
	call input
	addl $0, %esp
	sall $2, %eax
	orl $0, %eax
	movl %eax, -24(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -8(%ebp)
	movl -24(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_76
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_77
	label_76: 
	label_77: 
	cmpl $0, %eax
	je label_78
	movl -24(%ebp), %eax
	andl $-4, %eax
	movl -8(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call equal
	addl $8, %esp
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_79
	label_78: 
	movl -24(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_80
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_81
	label_80: 
	movl %eax, %ecx
	label_81: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_82
	movl -24(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -4(%ebp)
	cmpl $0, -4(%ebp)
	je label_84
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_85
	label_84: 
	movl -4(%ebp), %eax
	label_85: 
	jmp label_83
	label_82: 
	movl %ecx, %eax
	label_83: 
	cmpl $0, %eax
	je label_86
	movl -24(%ebp), %eax
	sarl $2, %eax
	movl -8(%ebp), %ecx
	sarl $2, %ecx
	cmpl %ecx, %eax
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_87
	label_86: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_87: 
	label_79: 
	jmp label_75
	label_74: 
	movl %ebx, %ecx
	label_75: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -68(%ebp), %esi
	movl -64(%ebp), %edi
	movl -60(%ebp), %ebx
	movl $0, %eax
	leave
	ret
