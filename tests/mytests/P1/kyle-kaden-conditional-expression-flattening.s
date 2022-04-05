.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -52(%ebp)
	movl %edi, -56(%ebp)
	movl %esi, -60(%ebp)
	subl $64, %esp
	movl $10, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -36(%ebp)
	movl $5, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -32(%ebp)
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_0
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_1
	label_0: 
	label_1: 
	cmpl $0, %eax
	je label_2
	movl -36(%ebp), %eax
	andl $-4, %eax
	movl -32(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_3
	label_2: 
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %edx
	cmpl $0, %edx
	je label_4
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_5
	label_4: 
	movl %edx, %eax
	label_5: 
	movl %eax, %edx
	cmpl $0, %edx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_6
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_8
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_9
	label_8: 
	movl %ecx, %eax
	label_9: 
	jmp label_7
	label_6: 
	movl %edx, %eax
	label_7: 
	cmpl $0, %eax
	je label_10
	movl -36(%ebp), %ecx
	sarl $2, %ecx
	movl -32(%ebp), %eax
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
	movl %ecx, -32(%ebp)
	movl $5, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -36(%ebp)
	movl $10, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -40(%ebp)
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_12
	movl -40(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_13
	label_12: 
	label_13: 
	cmpl $0, %eax
	je label_14
	movl -36(%ebp), %eax
	andl $-4, %eax
	movl -40(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_15
	label_14: 
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_16
	movl -40(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_17
	label_16: 
	movl %eax, %ecx
	label_17: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_18
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -52(%ebp)
	cmpl $0, -52(%ebp)
	je label_20
	movl -40(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_21
	label_20: 
	movl -52(%ebp), %eax
	label_21: 
	jmp label_19
	label_18: 
	movl %ecx, %eax
	label_19: 
	cmpl $0, %eax
	je label_22
	movl -36(%ebp), %eax
	sarl $2, %eax
	movl -40(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_23
	label_22: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_23: 
	label_15: 
	movl %ecx, -36(%ebp)
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_24
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_25
	label_24: 
	label_25: 
	cmpl $0, %eax
	je label_26
	movl -32(%ebp), %eax
	andl $-4, %eax
	movl -36(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call equal
	addl $8, %esp
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_27
	label_26: 
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_28
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_29
	label_28: 
	movl %ecx, %eax
	label_29: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_30
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -44(%ebp)
	cmpl $0, -44(%ebp)
	je label_32
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_33
	label_32: 
	movl -44(%ebp), %eax
	label_33: 
	jmp label_31
	label_30: 
	movl %ecx, %eax
	label_31: 
	cmpl $0, %eax
	je label_34
	movl -32(%ebp), %eax
	sarl $2, %eax
	movl -36(%ebp), %ecx
	sarl $2, %ecx
	cmpl %ecx, %eax
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_35
	label_34: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_35: 
	label_27: 
	movl %ecx, -32(%ebp)
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_36
	movl -32(%ebp), %eax
	movl %eax, -36(%ebp)
	andl $-4, -36(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -36(%ebp)
	call equal
	addl $8, %esp
	movl %eax, -48(%ebp)
	cmpl $0, -48(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_38
	movl -32(%ebp), %eax
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
	jmp label_39
	label_38: 
	movl -48(%ebp), %ecx
	label_39: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_37
	label_36: 
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_40
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_41
	label_40: 
	movl %ecx, %eax
	label_41: 
	cmpl $0, %eax
	je label_42
	movl -32(%ebp), %eax
	sarl $2, %eax
	movl %eax, %ecx
	jmp label_43
	label_42: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_43: 
	movl %ecx, %eax
	label_37: 
	cmpl $0, %eax
	je label_44
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -28(%ebp)
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -32(%ebp)
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_46
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_47
	label_46: 
	label_47: 
	cmpl $0, %eax
	je label_48
	movl -28(%ebp), %eax
	andl $-4, %eax
	movl -32(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_49
	label_48: 
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_50
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_51
	label_50: 
	movl %eax, %ecx
	label_51: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_52
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -12(%ebp)
	cmpl $0, -12(%ebp)
	je label_54
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_55
	label_54: 
	movl -12(%ebp), %eax
	label_55: 
	jmp label_53
	label_52: 
	movl %ecx, %eax
	label_53: 
	cmpl $0, %eax
	je label_56
	movl -28(%ebp), %eax
	sarl $2, %eax
	movl -32(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_57
	label_56: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_57: 
	label_49: 
	movl %ecx, -28(%ebp)
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -12(%ebp)
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_58
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_59
	label_58: 
	label_59: 
	cmpl $0, %eax
	je label_60
	movl -28(%ebp), %eax
	andl $-4, %eax
	movl -12(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_61
	label_60: 
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_62
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_63
	label_62: 
	movl %ecx, %eax
	label_63: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_64
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ebx
	cmpl $0, %ebx
	je label_66
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_67
	label_66: 
	movl %ebx, %eax
	label_67: 
	jmp label_65
	label_64: 
	movl %ecx, %eax
	label_65: 
	cmpl $0, %eax
	je label_68
	movl -28(%ebp), %eax
	sarl $2, %eax
	movl -12(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_69
	label_68: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_69: 
	label_61: 
	jmp label_45
	label_44: 
	movl $5, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -32(%ebp)
	movl $6, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -36(%ebp)
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_70
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_71
	label_70: 
	label_71: 
	cmpl $0, %eax
	je label_72
	movl -32(%ebp), %eax
	andl $-4, %eax
	movl -36(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_73
	label_72: 
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_74
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_75
	label_74: 
	movl %eax, %ecx
	label_75: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_76
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ebx
	cmpl $0, %ebx
	je label_78
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_79
	label_78: 
	movl %ebx, %eax
	label_79: 
	jmp label_77
	label_76: 
	movl %ecx, %eax
	label_77: 
	cmpl $0, %eax
	je label_80
	movl -32(%ebp), %ecx
	sarl $2, %ecx
	movl -36(%ebp), %eax
	sarl $2, %eax
	addl %eax, %ecx
	movl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_81
	label_80: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_81: 
	label_73: 
	label_45: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl $10, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -12(%ebp)
	movl $5, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ebx
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_82
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_83
	label_82: 
	label_83: 
	cmpl $0, %eax
	je label_84
	movl -12(%ebp), %eax
	andl $-4, %eax
	movl %ebx, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_85
	label_84: 
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_86
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_87
	label_86: 
	movl %eax, %ecx
	label_87: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_88
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -16(%ebp)
	cmpl $0, -16(%ebp)
	je label_90
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_91
	label_90: 
	movl -16(%ebp), %eax
	label_91: 
	jmp label_89
	label_88: 
	movl %ecx, %eax
	label_89: 
	cmpl $0, %eax
	je label_92
	movl -12(%ebp), %ecx
	sarl $2, %ecx
	movl %ebx, %eax
	sarl $2, %eax
	addl %eax, %ecx
	movl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_93
	label_92: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_93: 
	label_85: 
	movl %ecx, -12(%ebp)
	movl $5, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ebx
	movl $10, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -16(%ebp)
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_94
	movl -16(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_95
	label_94: 
	label_95: 
	cmpl $0, %eax
	je label_96
	movl %ebx, %eax
	andl $-4, %eax
	movl -16(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_97
	label_96: 
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_98
	movl -16(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_99
	label_98: 
	movl %ecx, %eax
	label_99: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_100
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -20(%ebp)
	cmpl $0, -20(%ebp)
	je label_102
	movl -16(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_103
	label_102: 
	movl -20(%ebp), %eax
	label_103: 
	jmp label_101
	label_100: 
	movl %ecx, %eax
	label_101: 
	cmpl $0, %eax
	je label_104
	movl %ebx, %eax
	sarl $2, %eax
	movl -16(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_105
	label_104: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_105: 
	label_97: 
	movl %ecx, %ebx
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_106
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_107
	label_106: 
	label_107: 
	cmpl $0, %eax
	je label_108
	movl -12(%ebp), %eax
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
	jmp label_109
	label_108: 
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_110
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_111
	label_110: 
	movl %ecx, %eax
	label_111: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_112
	movl -12(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %edi
	cmpl $0, %edi
	je label_114
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_115
	label_114: 
	movl %edi, %eax
	label_115: 
	jmp label_113
	label_112: 
	movl %ecx, %eax
	label_113: 
	cmpl $0, %eax
	je label_116
	movl -12(%ebp), %eax
	sarl $2, %eax
	movl %ebx, %ecx
	sarl $2, %ecx
	cmpl %eax, %ecx
	setne %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_117
	label_116: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_117: 
	label_109: 
	movl %ecx, %ebx
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_118
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
	movl %eax, -24(%ebp)
	cmpl $0, -24(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_120
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
	jmp label_121
	label_120: 
	movl -24(%ebp), %ecx
	label_121: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_119
	label_118: 
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
	je label_122
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_123
	label_122: 
	movl %ecx, %eax
	label_123: 
	cmpl $0, %eax
	je label_124
	movl %ebx, %eax
	sarl $2, %eax
	movl %eax, %ecx
	jmp label_125
	label_124: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_125: 
	movl %ecx, %eax
	label_119: 
	cmpl $0, %eax
	je label_126
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
	je label_128
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_129
	label_128: 
	label_129: 
	cmpl $0, %eax
	je label_130
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
	jmp label_131
	label_130: 
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_132
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_133
	label_132: 
	movl %eax, %ecx
	label_133: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_134
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -4(%ebp)
	cmpl $0, -4(%ebp)
	je label_136
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_137
	label_136: 
	movl -4(%ebp), %eax
	label_137: 
	jmp label_135
	label_134: 
	movl %ecx, %eax
	label_135: 
	cmpl $0, %eax
	je label_138
	movl %edi, %eax
	sarl $2, %eax
	movl %ebx, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_139
	label_138: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_139: 
	label_131: 
	movl %ecx, -4(%ebp)
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -8(%ebp)
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_140
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_141
	label_140: 
	label_141: 
	cmpl $0, %eax
	je label_142
	movl -4(%ebp), %eax
	andl $-4, %eax
	movl -8(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_143
	label_142: 
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_144
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_145
	label_144: 
	movl %eax, %ecx
	label_145: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_146
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %esi
	cmpl $0, %esi
	je label_148
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_149
	label_148: 
	movl %esi, %eax
	label_149: 
	jmp label_147
	label_146: 
	movl %ecx, %eax
	label_147: 
	cmpl $0, %eax
	je label_150
	movl -4(%ebp), %ecx
	sarl $2, %ecx
	movl -8(%ebp), %eax
	sarl $2, %eax
	addl %eax, %ecx
	movl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_151
	label_150: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_151: 
	label_143: 
	jmp label_127
	label_126: 
	movl $5, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ebx
	movl $6, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %edi
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_152
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_153
	label_152: 
	label_153: 
	cmpl $0, %eax
	je label_154
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
	jmp label_155
	label_154: 
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_156
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_157
	label_156: 
	movl %ecx, %eax
	label_157: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_158
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %esi
	cmpl $0, %esi
	je label_160
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_161
	label_160: 
	movl %esi, %eax
	label_161: 
	jmp label_159
	label_158: 
	movl %ecx, %eax
	label_159: 
	cmpl $0, %eax
	je label_162
	movl %ebx, %eax
	sarl $2, %eax
	movl %edi, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_163
	label_162: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_163: 
	label_155: 
	label_127: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -60(%ebp), %esi
	movl -56(%ebp), %edi
	movl -52(%ebp), %ebx
	movl $0, %eax
	leave
	ret
