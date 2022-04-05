.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -72(%ebp)
	movl %edi, -76(%ebp)
	movl %esi, -80(%ebp)
	subl $84, %esp
	movl $1, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, -12(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, -20(%ebp)
	movl -12(%ebp), %eax
	movl %eax, -48(%ebp)
	movl -48(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_0
	movl -48(%ebp), %eax
	movl %eax, -60(%ebp)
	andl $-4, -60(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -60(%ebp)
	call equal
	addl $8, %esp
	movl %eax, -60(%ebp)
	cmpl $0, -60(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_2
	movl -48(%ebp), %eax
	movl %eax, -60(%ebp)
	andl $-4, -60(%ebp)
	call create_dict
	addl $0, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -60(%ebp)
	call equal
	addl $8, %esp
	movl %eax, %ecx
	jmp label_3
	label_2: 
	movl -60(%ebp), %ecx
	label_3: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_1
	label_0: 
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
	je label_4
	movl -48(%ebp), %eax
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
	movl -48(%ebp), %eax
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
	movl -20(%ebp), %ecx
	jmp label_9
	label_8: 
	movl -48(%ebp), %ecx
	label_9: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -20(%ebp), %eax
	movl %eax, -48(%ebp)
	movl -48(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_10
	movl -48(%ebp), %eax
	movl %eax, -60(%ebp)
	andl $-4, -60(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -60(%ebp)
	call equal
	addl $8, %esp
	movl %eax, -72(%ebp)
	cmpl $0, -72(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_12
	movl -48(%ebp), %eax
	movl %eax, -60(%ebp)
	andl $-4, -60(%ebp)
	call create_dict
	addl $0, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -60(%ebp)
	call equal
	addl $8, %esp
	movl %eax, %ecx
	jmp label_13
	label_12: 
	movl -72(%ebp), %ecx
	label_13: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_11
	label_10: 
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
	je label_14
	movl -48(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_15
	label_14: 
	label_15: 
	cmpl $0, %ecx
	je label_16
	movl -48(%ebp), %eax
	sarl $2, %eax
	jmp label_17
	label_16: 
	call abort
	addl $0, %esp
	label_17: 
	label_11: 
	cmpl $0, %eax
	je label_18
	movl -12(%ebp), %ecx
	jmp label_19
	label_18: 
	movl -48(%ebp), %ecx
	label_19: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -12(%ebp), %eax
	movl %eax, -48(%ebp)
	movl -48(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_20
	movl -48(%ebp), %eax
	movl %eax, -60(%ebp)
	andl $-4, -60(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -60(%ebp)
	call equal
	addl $8, %esp
	movl %eax, -64(%ebp)
	cmpl $0, -64(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_22
	movl -48(%ebp), %eax
	movl %eax, -60(%ebp)
	andl $-4, -60(%ebp)
	call create_dict
	addl $0, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -60(%ebp)
	call equal
	addl $8, %esp
	movl %eax, %ecx
	jmp label_23
	label_22: 
	movl -64(%ebp), %ecx
	label_23: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_21
	label_20: 
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
	je label_24
	movl -48(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_25
	label_24: 
	label_25: 
	cmpl $0, %ecx
	je label_26
	movl -48(%ebp), %eax
	sarl $2, %eax
	jmp label_27
	label_26: 
	call abort
	addl $0, %esp
	label_27: 
	label_21: 
	cmpl $0, %eax
	je label_28
	movl -12(%ebp), %ecx
	jmp label_29
	label_28: 
	movl -48(%ebp), %ecx
	label_29: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -20(%ebp), %eax
	movl %eax, -48(%ebp)
	movl -48(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_30
	movl -48(%ebp), %eax
	movl %eax, -60(%ebp)
	andl $-4, -60(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -60(%ebp)
	call equal
	addl $8, %esp
	movl %eax, -68(%ebp)
	cmpl $0, -68(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_32
	movl -48(%ebp), %eax
	movl %eax, -60(%ebp)
	andl $-4, -60(%ebp)
	call create_dict
	addl $0, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -60(%ebp)
	call equal
	addl $8, %esp
	movl %eax, %ecx
	jmp label_33
	label_32: 
	movl -68(%ebp), %ecx
	label_33: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_31
	label_30: 
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
	je label_34
	movl -48(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_35
	label_34: 
	label_35: 
	cmpl $0, %ecx
	je label_36
	movl -48(%ebp), %eax
	sarl $2, %eax
	jmp label_37
	label_36: 
	call abort
	addl $0, %esp
	label_37: 
	label_31: 
	cmpl $0, %eax
	je label_38
	movl -20(%ebp), %ecx
	jmp label_39
	label_38: 
	movl -48(%ebp), %ecx
	label_39: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -12(%ebp), %eax
	movl %eax, -48(%ebp)
	movl -48(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_40
	movl -48(%ebp), %eax
	movl %eax, -56(%ebp)
	andl $-4, -56(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -56(%ebp)
	call equal
	addl $8, %esp
	movl %eax, -56(%ebp)
	cmpl $0, -56(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_42
	movl -48(%ebp), %eax
	movl %eax, -56(%ebp)
	andl $-4, -56(%ebp)
	call create_dict
	addl $0, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -56(%ebp)
	call equal
	addl $8, %esp
	movl %eax, %ecx
	jmp label_43
	label_42: 
	movl -56(%ebp), %ecx
	label_43: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_41
	label_40: 
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
	je label_44
	movl -48(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_45
	label_44: 
	movl %ecx, %eax
	label_45: 
	cmpl $0, %eax
	je label_46
	movl -48(%ebp), %eax
	sarl $2, %eax
	movl %eax, %ecx
	jmp label_47
	label_46: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_47: 
	label_41: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_48
	movl -20(%ebp), %ecx
	jmp label_49
	label_48: 
	movl -48(%ebp), %ecx
	label_49: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -20(%ebp), %eax
	movl %eax, -48(%ebp)
	movl -48(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_50
	movl -48(%ebp), %eax
	movl %eax, -40(%ebp)
	andl $-4, -40(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -40(%ebp)
	call equal
	addl $8, %esp
	movl %eax, -40(%ebp)
	cmpl $0, -40(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_52
	movl -48(%ebp), %eax
	movl %eax, -40(%ebp)
	andl $-4, -40(%ebp)
	call create_dict
	addl $0, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -40(%ebp)
	call equal
	addl $8, %esp
	movl %eax, %ecx
	jmp label_53
	label_52: 
	movl -40(%ebp), %ecx
	label_53: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_51
	label_50: 
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
	je label_54
	movl -48(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_55
	label_54: 
	label_55: 
	cmpl $0, %ecx
	je label_56
	movl -48(%ebp), %eax
	sarl $2, %eax
	jmp label_57
	label_56: 
	call abort
	addl $0, %esp
	label_57: 
	movl %eax, %ecx
	label_51: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_58
	movl -12(%ebp), %ecx
	jmp label_59
	label_58: 
	movl -48(%ebp), %ecx
	label_59: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -12(%ebp), %eax
	movl %eax, -40(%ebp)
	movl -40(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %ecx
	cmpl $0, %ecx
	je label_60
	movl -40(%ebp), %eax
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
	je label_62
	movl -40(%ebp), %eax
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
	jmp label_63
	label_62: 
	movl -32(%ebp), %ecx
	label_63: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_61
	label_60: 
	movl -40(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_64
	movl -40(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_65
	label_64: 
	label_65: 
	cmpl $0, %ecx
	je label_66
	movl -40(%ebp), %eax
	sarl $2, %eax
	jmp label_67
	label_66: 
	call abort
	addl $0, %esp
	label_67: 
	label_61: 
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_68
	movl -12(%ebp), %ecx
	jmp label_69
	label_68: 
	movl -40(%ebp), %ecx
	label_69: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -20(%ebp), %eax
	movl %eax, -32(%ebp)
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_70
	movl -32(%ebp), %eax
	movl %eax, -40(%ebp)
	andl $-4, -40(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -40(%ebp)
	call equal
	addl $8, %esp
	movl %eax, -52(%ebp)
	cmpl $0, -52(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_72
	movl -32(%ebp), %eax
	movl %eax, -40(%ebp)
	andl $-4, -40(%ebp)
	call create_dict
	addl $0, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -40(%ebp)
	call equal
	addl $8, %esp
	movl %eax, %ecx
	jmp label_73
	label_72: 
	movl -52(%ebp), %ecx
	label_73: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_71
	label_70: 
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
	je label_74
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_75
	label_74: 
	label_75: 
	cmpl $0, %ecx
	je label_76
	movl -32(%ebp), %eax
	sarl $2, %eax
	jmp label_77
	label_76: 
	call abort
	addl $0, %esp
	label_77: 
	movl %eax, %ecx
	label_71: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_78
	movl -20(%ebp), %ecx
	jmp label_79
	label_78: 
	movl -32(%ebp), %ecx
	label_79: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -12(%ebp), %eax
	movl %eax, -32(%ebp)
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %ecx
	cmpl $0, %ecx
	je label_80
	movl -32(%ebp), %eax
	movl %eax, -40(%ebp)
	andl $-4, -40(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -40(%ebp)
	call equal
	addl $8, %esp
	movl %eax, -44(%ebp)
	cmpl $0, -44(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_82
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
	jmp label_83
	label_82: 
	movl -44(%ebp), %ecx
	label_83: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_81
	label_80: 
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
	je label_84
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_85
	label_84: 
	label_85: 
	cmpl $0, %ecx
	je label_86
	movl -32(%ebp), %eax
	sarl $2, %eax
	jmp label_87
	label_86: 
	call abort
	addl $0, %esp
	label_87: 
	label_81: 
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	pushl %eax
	call print_any
	addl $4, %esp
	movl -20(%ebp), %eax
	movl %eax, -32(%ebp)
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %ecx
	cmpl $0, %ecx
	je label_88
	movl -32(%ebp), %edi
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
	je label_90
	movl -32(%ebp), %edi
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
	jmp label_91
	label_90: 
	movl %edi, %ecx
	label_91: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_89
	label_88: 
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
	je label_92
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_93
	label_92: 
	label_93: 
	cmpl $0, %ecx
	je label_94
	movl -32(%ebp), %eax
	sarl $2, %eax
	jmp label_95
	label_94: 
	call abort
	addl $0, %esp
	label_95: 
	label_89: 
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	pushl %eax
	call print_any
	addl $4, %esp
	movl -12(%ebp), %eax
	movl %eax, %edi
	movl -20(%ebp), %eax
	movl %eax, -32(%ebp)
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_96
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_97
	label_96: 
	label_97: 
	cmpl $0, %eax
	je label_98
	movl %edi, %eax
	andl $-4, %eax
	movl -32(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call equal
	addl $8, %esp
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_99
	label_98: 
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_100
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_101
	label_100: 
	movl %ecx, %eax
	label_101: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_102
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -8(%ebp)
	cmpl $0, -8(%ebp)
	je label_104
	movl -32(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_105
	label_104: 
	movl -8(%ebp), %eax
	label_105: 
	jmp label_103
	label_102: 
	movl %ecx, %eax
	label_103: 
	cmpl $0, %eax
	je label_106
	movl %edi, %eax
	sarl $2, %eax
	movl -32(%ebp), %ecx
	sarl $2, %ecx
	cmpl %ecx, %eax
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_107
	label_106: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_107: 
	label_99: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -20(%ebp), %eax
	movl %eax, %edi
	movl -12(%ebp), %eax
	movl %eax, -8(%ebp)
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_108
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_109
	label_108: 
	label_109: 
	cmpl $0, %eax
	je label_110
	movl %edi, %eax
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
	jmp label_111
	label_110: 
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_112
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_113
	label_112: 
	movl %eax, %ecx
	label_113: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_114
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -24(%ebp)
	cmpl $0, -24(%ebp)
	je label_116
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_117
	label_116: 
	movl -24(%ebp), %eax
	label_117: 
	jmp label_115
	label_114: 
	movl %ecx, %eax
	label_115: 
	cmpl $0, %eax
	je label_118
	movl %edi, %eax
	sarl $2, %eax
	movl -8(%ebp), %ecx
	sarl $2, %ecx
	cmpl %ecx, %eax
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_119
	label_118: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_119: 
	label_111: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -12(%ebp), %eax
	movl %eax, -8(%ebp)
	movl -12(%ebp), %eax
	movl %eax, %edi
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_120
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_121
	label_120: 
	label_121: 
	cmpl $0, %eax
	je label_122
	movl -8(%ebp), %eax
	andl $-4, %eax
	movl %edi, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call equal
	addl $8, %esp
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_123
	label_122: 
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_124
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_125
	label_124: 
	movl %ecx, %eax
	label_125: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_126
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -16(%ebp)
	cmpl $0, -16(%ebp)
	je label_128
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_129
	label_128: 
	movl -16(%ebp), %eax
	label_129: 
	jmp label_127
	label_126: 
	movl %ecx, %eax
	label_127: 
	cmpl $0, %eax
	je label_130
	movl -8(%ebp), %ecx
	sarl $2, %ecx
	movl %edi, %eax
	sarl $2, %eax
	cmpl %eax, %ecx
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_131
	label_130: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_131: 
	label_123: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -20(%ebp), %eax
	movl %eax, -8(%ebp)
	movl -20(%ebp), %eax
	movl %eax, %edi
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_132
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_133
	label_132: 
	label_133: 
	cmpl $0, %eax
	je label_134
	movl -8(%ebp), %eax
	andl $-4, %eax
	movl %edi, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call equal
	addl $8, %esp
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_135
	label_134: 
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_136
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_137
	label_136: 
	movl %ecx, %eax
	label_137: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_138
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -4(%ebp)
	cmpl $0, -4(%ebp)
	je label_140
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_141
	label_140: 
	movl -4(%ebp), %eax
	label_141: 
	jmp label_139
	label_138: 
	movl %ecx, %eax
	label_139: 
	cmpl $0, %eax
	je label_142
	movl -8(%ebp), %eax
	sarl $2, %eax
	movl %edi, %ecx
	sarl $2, %ecx
	cmpl %ecx, %eax
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_143
	label_142: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_143: 
	label_135: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -12(%ebp), %eax
	movl %eax, -4(%ebp)
	movl -20(%ebp), %eax
	movl %eax, %edi
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_144
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_145
	label_144: 
	label_145: 
	cmpl $0, %eax
	je label_146
	movl -4(%ebp), %eax
	andl $-4, %eax
	movl %edi, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call equal
	addl $8, %esp
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_147
	label_146: 
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_148
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_149
	label_148: 
	movl %ecx, %eax
	label_149: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_150
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -36(%ebp)
	cmpl $0, -36(%ebp)
	je label_152
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_153
	label_152: 
	movl -36(%ebp), %eax
	label_153: 
	jmp label_151
	label_150: 
	movl %ecx, %eax
	label_151: 
	cmpl $0, %eax
	je label_154
	movl -4(%ebp), %eax
	sarl $2, %eax
	movl %edi, %ecx
	sarl $2, %ecx
	cmpl %eax, %ecx
	setne %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_155
	label_154: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_155: 
	label_147: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -20(%ebp), %eax
	movl %eax, %edi
	movl -12(%ebp), %eax
	movl %eax, -4(%ebp)
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_156
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_157
	label_156: 
	label_157: 
	cmpl $0, %eax
	je label_158
	movl %edi, %eax
	andl $-4, %eax
	movl -4(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call equal
	addl $8, %esp
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_159
	label_158: 
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_160
	movl -4(%ebp), %eax
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
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -28(%ebp)
	cmpl $0, -28(%ebp)
	je label_164
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_165
	label_164: 
	movl -28(%ebp), %eax
	label_165: 
	jmp label_163
	label_162: 
	movl %ecx, %eax
	label_163: 
	cmpl $0, %eax
	je label_166
	movl %edi, %ecx
	sarl $2, %ecx
	movl -4(%ebp), %eax
	sarl $2, %eax
	cmpl %ecx, %eax
	setne %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_167
	label_166: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_167: 
	label_159: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -12(%ebp), %eax
	movl %eax, %edi
	movl -12(%ebp), %eax
	movl %eax, -4(%ebp)
	movl %edi, %eax
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
	movl %edi, %eax
	andl $-4, %eax
	movl -4(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call equal
	addl $8, %esp
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_171
	label_170: 
	movl %edi, %eax
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
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %esi
	cmpl $0, %esi
	je label_176
	movl -4(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_177
	label_176: 
	movl %esi, %eax
	label_177: 
	jmp label_175
	label_174: 
	movl %ecx, %eax
	label_175: 
	cmpl $0, %eax
	je label_178
	movl %edi, %ecx
	sarl $2, %ecx
	movl -4(%ebp), %eax
	sarl $2, %eax
	cmpl %ecx, %eax
	setne %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_179
	label_178: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_179: 
	label_171: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -20(%ebp), %edi
	movl -20(%ebp), %esi
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_180
	movl %esi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_181
	label_180: 
	label_181: 
	cmpl $0, %eax
	je label_182
	movl %edi, %eax
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
	jmp label_183
	label_182: 
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_184
	movl %esi, %eax
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
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ebx
	cmpl $0, %ebx
	je label_188
	movl %esi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_189
	label_188: 
	movl %ebx, %eax
	label_189: 
	jmp label_187
	label_186: 
	movl %ecx, %eax
	label_187: 
	cmpl $0, %eax
	je label_190
	movl %edi, %ecx
	sarl $2, %ecx
	movl %esi, %eax
	sarl $2, %eax
	cmpl %ecx, %eax
	setne %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, %ecx
	jmp label_191
	label_190: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_191: 
	label_183: 
	pushl %ecx
	call print_any
	addl $4, %esp
	movl -80(%ebp), %esi
	movl -76(%ebp), %edi
	movl -72(%ebp), %ebx
	movl $0, %eax
	leave
	ret
