.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -92(%ebp)
	movl %edi, -96(%ebp)
	movl %esi, -100(%ebp)
	subl $104, %esp
	movl $0, -56(%ebp)
	sall $2, -56(%ebp)
	orl $0, -56(%ebp)
	movl $1, -36(%ebp)
	sall $2, -36(%ebp)
	orl $0, -36(%ebp)
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	movl %eax, -28(%ebp)
	addl $3, -28(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -56(%ebp)
	pushl %eax
	pushl -28(%ebp)
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -36(%ebp)
	pushl %eax
	pushl -28(%ebp)
	call set_subscript
	addl $12, %esp
	movl -28(%ebp), %eax
	movl %eax, -56(%ebp)
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -28(%ebp)
	movl -56(%ebp), %eax
	movl %eax, -84(%ebp)
	movl -28(%ebp), %eax
	movl %eax, -36(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -88(%ebp)
	movl -88(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_0
	movl -88(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_1
	label_0: 
	label_1: 
	cmpl $0, %ecx
	je label_2
	movl -88(%ebp), %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	jmp label_3
	label_2: 
	call abort
	addl $0, %esp
	label_3: 
	movl %eax, -88(%ebp)
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_4
	movl -88(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_5
	label_4: 
	label_5: 
	cmpl $0, %eax
	je label_6
	movl -36(%ebp), %eax
	andl $-4, %eax
	movl -88(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_7
	label_6: 
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_8
	movl -88(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_9
	label_8: 
	movl %eax, %ecx
	label_9: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_10
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -92(%ebp)
	cmpl $0, -92(%ebp)
	je label_12
	movl -88(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_13
	label_12: 
	movl -92(%ebp), %eax
	label_13: 
	jmp label_11
	label_10: 
	movl %ecx, %eax
	label_11: 
	cmpl $0, %eax
	je label_14
	movl -36(%ebp), %eax
	sarl $2, %eax
	movl -88(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_15
	label_14: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_15: 
	label_7: 
	pushl %ecx
	pushl -56(%ebp)
	call get_subscript
	addl $8, %esp
	movl %eax, -88(%ebp)
	movl -28(%ebp), %eax
	movl %eax, -92(%ebp)
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -36(%ebp)
	movl -36(%ebp), %eax
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
	movl -36(%ebp), %eax
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
	movl -36(%ebp), %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	jmp label_19
	label_18: 
	call abort
	addl $0, %esp
	label_19: 
	movl %eax, -36(%ebp)
	movl -92(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_20
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_21
	label_20: 
	label_21: 
	cmpl $0, %eax
	je label_22
	movl -92(%ebp), %eax
	andl $-4, %eax
	movl -36(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_23
	label_22: 
	movl -92(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_24
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_25
	label_24: 
	movl %ecx, %eax
	label_25: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_26
	movl -92(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -76(%ebp)
	cmpl $0, -76(%ebp)
	je label_28
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_29
	label_28: 
	movl -76(%ebp), %eax
	label_29: 
	jmp label_27
	label_26: 
	movl %ecx, %eax
	label_27: 
	cmpl $0, %eax
	je label_30
	movl -92(%ebp), %eax
	sarl $2, %eax
	movl -36(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_31
	label_30: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_31: 
	label_23: 
	pushl %ecx
	pushl -56(%ebp)
	call get_subscript
	addl $8, %esp
	movl %eax, -36(%ebp)
	movl -88(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_32
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_33
	label_32: 
	label_33: 
	cmpl $0, %eax
	je label_34
	movl -88(%ebp), %eax
	andl $-4, %eax
	movl -36(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, -56(%ebp)
	jmp label_35
	label_34: 
	movl -88(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_36
	movl -36(%ebp), %eax
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
	movl -88(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -80(%ebp)
	cmpl $0, -80(%ebp)
	je label_40
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_41
	label_40: 
	movl -80(%ebp), %eax
	label_41: 
	jmp label_39
	label_38: 
	movl %ecx, %eax
	label_39: 
	cmpl $0, %eax
	je label_42
	movl -88(%ebp), %eax
	sarl $2, %eax
	movl -36(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_43
	label_42: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_43: 
	movl %ecx, -56(%ebp)
	label_35: 
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	movl %eax, -36(%ebp)
	addl $3, -36(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -56(%ebp)
	pushl %eax
	pushl -36(%ebp)
	call set_subscript
	addl $12, %esp
	movl -36(%ebp), %eax
	movl %eax, -36(%ebp)
	movl -84(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_44
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_45
	label_44: 
	label_45: 
	cmpl $0, %eax
	je label_46
	movl -84(%ebp), %eax
	andl $-4, %eax
	movl -36(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_47
	label_46: 
	movl -84(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_48
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_49
	label_48: 
	movl %ecx, %eax
	label_49: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_50
	movl -84(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -68(%ebp)
	cmpl $0, -68(%ebp)
	je label_52
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_53
	label_52: 
	movl -68(%ebp), %eax
	label_53: 
	jmp label_51
	label_50: 
	movl %ecx, %eax
	label_51: 
	cmpl $0, %eax
	je label_54
	movl -84(%ebp), %eax
	sarl $2, %eax
	movl -36(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_55
	label_54: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_55: 
	label_47: 
	movl %ecx, -56(%ebp)
	movl -28(%ebp), %eax
	movl %eax, -28(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -36(%ebp)
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_56
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_57
	label_56: 
	label_57: 
	cmpl $0, %eax
	je label_58
	movl -28(%ebp), %eax
	andl $-4, %eax
	movl -36(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_59
	label_58: 
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_60
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_61
	label_60: 
	movl %eax, %ecx
	label_61: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_62
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -64(%ebp)
	cmpl $0, -64(%ebp)
	je label_64
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_65
	label_64: 
	movl -64(%ebp), %eax
	label_65: 
	jmp label_63
	label_62: 
	movl %ecx, %eax
	label_63: 
	cmpl $0, %eax
	je label_66
	movl -28(%ebp), %eax
	sarl $2, %eax
	movl -36(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_67
	label_66: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_67: 
	label_59: 
	movl %ecx, -28(%ebp)
	movl -56(%ebp), %eax
	movl %eax, -36(%ebp)
	movl -28(%ebp), %eax
	movl %eax, -68(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -64(%ebp)
	movl -64(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_68
	movl -64(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_69
	label_68: 
	movl %ecx, %eax
	label_69: 
	cmpl $0, %eax
	je label_70
	movl -64(%ebp), %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_71
	label_70: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_71: 
	movl %ecx, -64(%ebp)
	movl -68(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_72
	movl -64(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_73
	label_72: 
	label_73: 
	cmpl $0, %eax
	je label_74
	movl -68(%ebp), %eax
	andl $-4, %eax
	movl -64(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_75
	label_74: 
	movl -68(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_76
	movl -64(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_77
	label_76: 
	movl %ecx, %eax
	label_77: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_78
	movl -68(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ebx
	cmpl $0, %ebx
	je label_80
	movl -64(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_81
	label_80: 
	movl %ebx, %eax
	label_81: 
	jmp label_79
	label_78: 
	movl %ecx, %eax
	label_79: 
	cmpl $0, %eax
	je label_82
	movl -68(%ebp), %eax
	sarl $2, %eax
	movl -64(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_83
	label_82: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_83: 
	label_75: 
	pushl %ecx
	pushl -56(%ebp)
	call get_subscript
	addl $8, %esp
	movl %eax, -68(%ebp)
	movl -28(%ebp), %eax
	movl %eax, -64(%ebp)
	movl $2, %eax
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
	je label_84
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_85
	label_84: 
	movl %ecx, %eax
	label_85: 
	cmpl $0, %eax
	je label_86
	movl %ebx, %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_87
	label_86: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_87: 
	movl %ecx, %ebx
	movl -64(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_88
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_89
	label_88: 
	label_89: 
	cmpl $0, %eax
	je label_90
	movl -64(%ebp), %eax
	andl $-4, %eax
	movl %ebx, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_91
	label_90: 
	movl -64(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_92
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_93
	label_92: 
	movl %eax, %ecx
	label_93: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_94
	movl -64(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -60(%ebp)
	cmpl $0, -60(%ebp)
	je label_96
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_97
	label_96: 
	movl -60(%ebp), %eax
	label_97: 
	jmp label_95
	label_94: 
	movl %ecx, %eax
	label_95: 
	cmpl $0, %eax
	je label_98
	movl -64(%ebp), %ecx
	sarl $2, %ecx
	movl %ebx, %eax
	sarl $2, %eax
	addl %eax, %ecx
	movl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_99
	label_98: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_99: 
	label_91: 
	pushl %ecx
	pushl -56(%ebp)
	call get_subscript
	addl $8, %esp
	movl %eax, %ebx
	movl -68(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_100
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_101
	label_100: 
	label_101: 
	cmpl $0, %eax
	je label_102
	movl -68(%ebp), %eax
	andl $-4, %eax
	movl %ebx, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, -56(%ebp)
	jmp label_103
	label_102: 
	movl -68(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_104
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_105
	label_104: 
	movl %ecx, %eax
	label_105: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_106
	movl -68(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -72(%ebp)
	cmpl $0, -72(%ebp)
	je label_108
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_109
	label_108: 
	movl -72(%ebp), %eax
	label_109: 
	jmp label_107
	label_106: 
	movl %ecx, %eax
	label_107: 
	cmpl $0, %eax
	je label_110
	movl -68(%ebp), %eax
	sarl $2, %eax
	movl %ebx, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_111
	label_110: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_111: 
	movl %ecx, -56(%ebp)
	label_103: 
	movl $1, %eax
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
	pushl -56(%ebp)
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_112
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_113
	label_112: 
	label_113: 
	cmpl $0, %eax
	je label_114
	movl -36(%ebp), %eax
	andl $-4, %eax
	movl %ebx, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_115
	label_114: 
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_116
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_117
	label_116: 
	movl %ecx, %eax
	label_117: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_118
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -52(%ebp)
	cmpl $0, -52(%ebp)
	je label_120
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_121
	label_120: 
	movl -52(%ebp), %eax
	label_121: 
	jmp label_119
	label_118: 
	movl %ecx, %eax
	label_119: 
	cmpl $0, %eax
	je label_122
	movl -36(%ebp), %eax
	sarl $2, %eax
	movl %ebx, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_123
	label_122: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_123: 
	label_115: 
	movl %ecx, -56(%ebp)
	movl -28(%ebp), %ebx
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -28(%ebp)
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_124
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_125
	label_124: 
	label_125: 
	cmpl $0, %eax
	je label_126
	movl %ebx, %eax
	andl $-4, %eax
	movl -28(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_127
	label_126: 
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_128
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_129
	label_128: 
	movl %eax, %ecx
	label_129: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_130
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -32(%ebp)
	cmpl $0, -32(%ebp)
	je label_132
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_133
	label_132: 
	movl -32(%ebp), %eax
	label_133: 
	jmp label_131
	label_130: 
	movl %ecx, %eax
	label_131: 
	cmpl $0, %eax
	je label_134
	movl %ebx, %eax
	sarl $2, %eax
	movl -28(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_135
	label_134: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_135: 
	label_127: 
	movl %ecx, -28(%ebp)
	movl -56(%ebp), %eax
	movl %eax, %ebx
	movl -28(%ebp), %eax
	movl %eax, -32(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -36(%ebp)
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_136
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_137
	label_136: 
	movl %ecx, %eax
	label_137: 
	cmpl $0, %eax
	je label_138
	movl -36(%ebp), %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_139
	label_138: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_139: 
	movl %ecx, -36(%ebp)
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_140
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_141
	label_140: 
	label_141: 
	cmpl $0, %eax
	je label_142
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
	jmp label_143
	label_142: 
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_144
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_145
	label_144: 
	movl %ecx, %eax
	label_145: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_146
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -4(%ebp)
	cmpl $0, -4(%ebp)
	je label_148
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_149
	label_148: 
	movl -4(%ebp), %eax
	label_149: 
	jmp label_147
	label_146: 
	movl %ecx, %eax
	label_147: 
	cmpl $0, %eax
	je label_150
	movl -32(%ebp), %eax
	sarl $2, %eax
	movl -36(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
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
	pushl %ecx
	pushl -56(%ebp)
	call get_subscript
	addl $8, %esp
	movl %eax, -32(%ebp)
	movl -28(%ebp), %eax
	movl %eax, -4(%ebp)
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, -36(%ebp)
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_152
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_153
	label_152: 
	label_153: 
	cmpl $0, %ecx
	je label_154
	movl -36(%ebp), %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	jmp label_155
	label_154: 
	call abort
	addl $0, %esp
	label_155: 
	movl %eax, -36(%ebp)
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_156
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_157
	label_156: 
	label_157: 
	cmpl $0, %eax
	je label_158
	movl -4(%ebp), %eax
	andl $-4, %eax
	movl -36(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_159
	label_158: 
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_160
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_161
	label_160: 
	movl %ecx, %eax
	label_161: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_162
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -16(%ebp)
	cmpl $0, -16(%ebp)
	je label_164
	movl -36(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_165
	label_164: 
	movl -16(%ebp), %eax
	label_165: 
	jmp label_163
	label_162: 
	movl %ecx, %eax
	label_163: 
	cmpl $0, %eax
	je label_166
	movl -4(%ebp), %eax
	sarl $2, %eax
	movl -36(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_167
	label_166: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_167: 
	label_159: 
	pushl %ecx
	pushl -56(%ebp)
	call get_subscript
	addl $8, %esp
	movl %eax, -4(%ebp)
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_168
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_169
	label_168: 
	label_169: 
	cmpl $0, %eax
	je label_170
	movl -32(%ebp), %eax
	andl $-4, %eax
	movl -4(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, -16(%ebp)
	jmp label_171
	label_170: 
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_172
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_173
	label_172: 
	movl %ecx, %eax
	label_173: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_174
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -20(%ebp)
	cmpl $0, -20(%ebp)
	je label_176
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_177
	label_176: 
	movl -20(%ebp), %eax
	label_177: 
	jmp label_175
	label_174: 
	movl %ecx, %eax
	label_175: 
	cmpl $0, %eax
	je label_178
	movl -32(%ebp), %eax
	sarl $2, %eax
	movl -4(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_179
	label_178: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_179: 
	movl %ecx, -16(%ebp)
	label_171: 
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	movl %eax, -4(%ebp)
	addl $3, -4(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -16(%ebp)
	pushl %eax
	pushl -4(%ebp)
	call set_subscript
	addl $12, %esp
	movl -4(%ebp), %eax
	movl %eax, -4(%ebp)
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_180
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_181
	label_180: 
	label_181: 
	cmpl $0, %eax
	je label_182
	movl %ebx, %eax
	andl $-4, %eax
	movl -4(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_183
	label_182: 
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_184
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_185
	label_184: 
	movl %ecx, %eax
	label_185: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_186
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %esi
	cmpl $0, %esi
	je label_188
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_189
	label_188: 
	movl %esi, %eax
	label_189: 
	jmp label_187
	label_186: 
	movl %ecx, %eax
	label_187: 
	cmpl $0, %eax
	je label_190
	movl %ebx, %eax
	sarl $2, %eax
	movl -4(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_191
	label_190: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_191: 
	label_183: 
	movl %ecx, -56(%ebp)
	movl -28(%ebp), %esi
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ebx
	movl %esi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_192
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_193
	label_192: 
	label_193: 
	cmpl $0, %eax
	je label_194
	movl %esi, %eax
	andl $-4, %eax
	movl %ebx, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_195
	label_194: 
	movl %esi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_196
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_197
	label_196: 
	movl %eax, %ecx
	label_197: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_198
	movl %esi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %edi
	cmpl $0, %edi
	je label_200
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_201
	label_200: 
	movl %edi, %eax
	label_201: 
	jmp label_199
	label_198: 
	movl %ecx, %eax
	label_199: 
	cmpl $0, %eax
	je label_202
	movl %esi, %eax
	sarl $2, %eax
	movl %ebx, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_203
	label_202: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_203: 
	label_195: 
	movl %ecx, -28(%ebp)
	movl -56(%ebp), %esi
	movl -28(%ebp), %edi
	movl $1, %eax
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
	je label_204
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_205
	label_204: 
	movl %ecx, %eax
	label_205: 
	cmpl $0, %eax
	je label_206
	movl %ebx, %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_207
	label_206: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_207: 
	movl %ecx, %ebx
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_208
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_209
	label_208: 
	label_209: 
	cmpl $0, %eax
	je label_210
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
	jmp label_211
	label_210: 
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_212
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_213
	label_212: 
	movl %eax, %ecx
	label_213: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_214
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -48(%ebp)
	cmpl $0, -48(%ebp)
	je label_216
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_217
	label_216: 
	movl -48(%ebp), %eax
	label_217: 
	jmp label_215
	label_214: 
	movl %ecx, %eax
	label_215: 
	cmpl $0, %eax
	je label_218
	movl %edi, %eax
	sarl $2, %eax
	movl %ebx, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_219
	label_218: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_219: 
	label_211: 
	pushl %ecx
	pushl -56(%ebp)
	call get_subscript
	addl $8, %esp
	movl %eax, -4(%ebp)
	movl -28(%ebp), %eax
	movl %eax, %edi
	movl $2, %eax
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
	je label_220
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_221
	label_220: 
	movl %ecx, %eax
	label_221: 
	cmpl $0, %eax
	je label_222
	movl %ebx, %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_223
	label_222: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_223: 
	movl %ecx, %ebx
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_224
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_225
	label_224: 
	label_225: 
	cmpl $0, %eax
	je label_226
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
	jmp label_227
	label_226: 
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_228
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_229
	label_228: 
	movl %eax, %ecx
	label_229: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_230
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -8(%ebp)
	cmpl $0, -8(%ebp)
	je label_232
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_233
	label_232: 
	movl -8(%ebp), %eax
	label_233: 
	jmp label_231
	label_230: 
	movl %ecx, %eax
	label_231: 
	cmpl $0, %eax
	je label_234
	movl %edi, %eax
	sarl $2, %eax
	movl %ebx, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_235
	label_234: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_235: 
	label_227: 
	pushl %ecx
	pushl -56(%ebp)
	call get_subscript
	addl $8, %esp
	movl %eax, %ebx
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_236
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_237
	label_236: 
	label_237: 
	cmpl $0, %eax
	je label_238
	movl -4(%ebp), %eax
	andl $-4, %eax
	movl %ebx, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %edi
	jmp label_239
	label_238: 
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_240
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_241
	label_240: 
	movl %eax, %ecx
	label_241: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_242
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -40(%ebp)
	cmpl $0, -40(%ebp)
	je label_244
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_245
	label_244: 
	movl -40(%ebp), %eax
	label_245: 
	jmp label_243
	label_242: 
	movl %ecx, %eax
	label_243: 
	cmpl $0, %eax
	je label_246
	movl -4(%ebp), %ecx
	sarl $2, %ecx
	movl %ebx, %eax
	sarl $2, %eax
	addl %eax, %ecx
	movl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_247
	label_246: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_247: 
	movl %ecx, %edi
	label_239: 
	movl $1, %eax
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
	pushl %edi
	pushl %eax
	pushl %ebx
	call set_subscript
	addl $12, %esp
	movl %esi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_248
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_249
	label_248: 
	label_249: 
	cmpl $0, %eax
	je label_250
	movl %esi, %eax
	andl $-4, %eax
	movl %ebx, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_251
	label_250: 
	movl %esi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_252
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_253
	label_252: 
	movl %eax, %ecx
	label_253: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_254
	movl %esi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -24(%ebp)
	cmpl $0, -24(%ebp)
	je label_256
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_257
	label_256: 
	movl -24(%ebp), %eax
	label_257: 
	jmp label_255
	label_254: 
	movl %ecx, %eax
	label_255: 
	cmpl $0, %eax
	je label_258
	movl %esi, %eax
	sarl $2, %eax
	movl %ebx, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_259
	label_258: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_259: 
	label_251: 
	movl %ecx, -56(%ebp)
	movl -28(%ebp), %ebx
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %edi
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_260
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_261
	label_260: 
	label_261: 
	cmpl $0, %eax
	je label_262
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
	jmp label_263
	label_262: 
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_264
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_265
	label_264: 
	movl %ecx, %eax
	label_265: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_266
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -12(%ebp)
	cmpl $0, -12(%ebp)
	je label_268
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_269
	label_268: 
	movl -12(%ebp), %eax
	label_269: 
	jmp label_267
	label_266: 
	movl %ecx, %eax
	label_267: 
	cmpl $0, %eax
	je label_270
	movl %ebx, %eax
	sarl $2, %eax
	movl %edi, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_271
	label_270: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_271: 
	label_263: 
	movl %ecx, -28(%ebp)
	pushl -56(%ebp)
	call print_any
	addl $4, %esp
	movl -28(%ebp), %ebx
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %edi
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
	je label_272
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_273
	label_272: 
	movl %ecx, %eax
	label_273: 
	cmpl $0, %eax
	je label_274
	movl %edi, %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_275
	label_274: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_275: 
	movl %ecx, %edi
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_276
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_277
	label_276: 
	label_277: 
	cmpl $0, %eax
	je label_278
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
	jmp label_279
	label_278: 
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_280
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_281
	label_280: 
	movl %eax, %ecx
	label_281: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_282
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -44(%ebp)
	cmpl $0, -44(%ebp)
	je label_284
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_285
	label_284: 
	movl -44(%ebp), %eax
	label_285: 
	jmp label_283
	label_282: 
	movl %ecx, %eax
	label_283: 
	cmpl $0, %eax
	je label_286
	movl %ebx, %eax
	sarl $2, %eax
	movl %edi, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_287
	label_286: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_287: 
	label_279: 
	pushl %ecx
	pushl -56(%ebp)
	call get_subscript
	addl $8, %esp
	pushl %eax
	call print_any
	addl $4, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl -56(%ebp)
	call get_subscript
	addl $8, %esp
	pushl %eax
	call print_any
	addl $4, %esp
	movl -100(%ebp), %esi
	movl -96(%ebp), %edi
	movl -92(%ebp), %ebx
	movl $0, %eax
	leave
	ret
