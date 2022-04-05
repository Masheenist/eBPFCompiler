.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -36(%ebp)
	movl %edi, -40(%ebp)
	movl %esi, -44(%ebp)
	subl $48, %esp
	movl $1, -16(%ebp)
	sall $2, -16(%ebp)
	orl $0, -16(%ebp)
	movl $2, -8(%ebp)
	sall $2, -8(%ebp)
	orl $0, -8(%ebp)
	movl $3, -24(%ebp)
	sall $2, -24(%ebp)
	orl $0, -24(%ebp)
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
	pushl -16(%ebp)
	pushl %eax
	pushl %edi
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -8(%ebp)
	pushl %eax
	pushl %edi
	call set_subscript
	addl $12, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -24(%ebp)
	pushl %eax
	pushl %edi
	call set_subscript
	addl $12, %esp
	movl %edi, %eax
	movl %eax, -16(%ebp)
	movl $4, -8(%ebp)
	sall $2, -8(%ebp)
	orl $0, -8(%ebp)
	movl $5, %edi
	sall $2, %edi
	orl $0, %edi
	movl $6, -36(%ebp)
	sall $2, -36(%ebp)
	orl $0, -36(%ebp)
	movl $3, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	movl %eax, -24(%ebp)
	addl $3, -24(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -8(%ebp)
	pushl %eax
	pushl -24(%ebp)
	call set_subscript
	addl $12, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %edi
	pushl %eax
	pushl -24(%ebp)
	call set_subscript
	addl $12, %esp
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -36(%ebp)
	pushl %eax
	pushl -24(%ebp)
	call set_subscript
	addl $12, %esp
	movl -24(%ebp), %eax
	movl %eax, -8(%ebp)
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl -8(%ebp)
	call get_subscript
	movl %eax, -24(%ebp)
	addl $8, %esp
	movl $1, %eax
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
	pushl -24(%ebp)
	pushl %eax
	pushl %edi
	call set_subscript
	addl $12, %esp
	movl %edi, -24(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl -8(%ebp)
	call get_subscript
	movl %eax, -36(%ebp)
	addl $8, %esp
	movl $1, %eax
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
	pushl -36(%ebp)
	pushl %eax
	pushl %edi
	call set_subscript
	addl $12, %esp
	movl -24(%ebp), %eax
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
	movl -24(%ebp), %eax
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
	movl -24(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_4
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_5
	label_4: 
	movl %ecx, %eax
	label_5: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_6
	movl -24(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -32(%ebp)
	cmpl $0, -32(%ebp)
	je label_8
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_9
	label_8: 
	movl -32(%ebp), %eax
	label_9: 
	jmp label_7
	label_6: 
	movl %ecx, %eax
	label_7: 
	cmpl $0, %eax
	je label_10
	movl -24(%ebp), %eax
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
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl -8(%ebp)
	call get_subscript
	movl %eax, -24(%ebp)
	addl $8, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	movl %eax, -32(%ebp)
	addl $3, -32(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -24(%ebp)
	pushl %eax
	pushl -32(%ebp)
	call set_subscript
	addl $12, %esp
	movl -32(%ebp), %eax
	movl %eax, -24(%ebp)
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_12
	movl -24(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_13
	label_12: 
	label_13: 
	cmpl $0, %eax
	je label_14
	movl %edi, %eax
	andl $-4, %eax
	movl -24(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_15
	label_14: 
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_16
	movl -24(%ebp), %eax
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
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -28(%ebp)
	cmpl $0, -28(%ebp)
	je label_20
	movl -24(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_21
	label_20: 
	movl -28(%ebp), %eax
	label_21: 
	jmp label_19
	label_18: 
	movl %ecx, %eax
	label_19: 
	cmpl $0, %eax
	je label_22
	movl %edi, %eax
	sarl $2, %eax
	movl -24(%ebp), %ecx
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
	movl %ecx, %edi
	movl $2, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl -16(%ebp)
	call get_subscript
	movl %eax, -28(%ebp)
	addl $8, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	movl %eax, -24(%ebp)
	addl $3, -24(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -28(%ebp)
	pushl %eax
	pushl -24(%ebp)
	call set_subscript
	addl $12, %esp
	movl -24(%ebp), %eax
	movl %eax, -28(%ebp)
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl -16(%ebp)
	call get_subscript
	movl %eax, -24(%ebp)
	addl $8, %esp
	movl $1, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	movl %eax, -32(%ebp)
	addl $3, -32(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl -24(%ebp)
	pushl %eax
	pushl -32(%ebp)
	call set_subscript
	addl $12, %esp
	movl -32(%ebp), %eax
	movl %eax, -24(%ebp)
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_24
	movl -24(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_25
	label_24: 
	label_25: 
	cmpl $0, %eax
	je label_26
	movl -28(%ebp), %eax
	andl $-4, %eax
	movl -24(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_27
	label_26: 
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_28
	movl -24(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_29
	label_28: 
	movl %eax, %ecx
	label_29: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_30
	movl -28(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ebx
	cmpl $0, %ebx
	je label_32
	movl -24(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_33
	label_32: 
	movl %ebx, %eax
	label_33: 
	jmp label_31
	label_30: 
	movl %ecx, %eax
	label_31: 
	cmpl $0, %eax
	je label_34
	movl -28(%ebp), %eax
	sarl $2, %eax
	movl -24(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_35
	label_34: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_35: 
	label_27: 
	movl %ecx, %ebx
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	pushl -16(%ebp)
	call get_subscript
	movl %eax, -24(%ebp)
	addl $8, %esp
	movl $1, %eax
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
	pushl -24(%ebp)
	pushl %eax
	pushl -28(%ebp)
	call set_subscript
	addl $12, %esp
	movl -28(%ebp), %eax
	movl %eax, -24(%ebp)
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_36
	movl -24(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_37
	label_36: 
	label_37: 
	cmpl $0, %eax
	je label_38
	movl %ebx, %eax
	andl $-4, %eax
	movl -24(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_39
	label_38: 
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_40
	movl -24(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_41
	label_40: 
	movl %ecx, %eax
	label_41: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_42
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -20(%ebp)
	cmpl $0, -20(%ebp)
	je label_44
	movl -24(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_45
	label_44: 
	movl -20(%ebp), %eax
	label_45: 
	jmp label_43
	label_42: 
	movl %ecx, %eax
	label_43: 
	cmpl $0, %eax
	je label_46
	movl %ebx, %eax
	sarl $2, %eax
	movl -24(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_47
	label_46: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_47: 
	label_39: 
	movl %ecx, %ebx
	movl -16(%ebp), %eax
	movl %eax, -16(%ebp)
	movl -8(%ebp), %eax
	movl %eax, -8(%ebp)
	movl -16(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_48
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_49
	label_48: 
	label_49: 
	cmpl $0, %eax
	je label_50
	movl -16(%ebp), %eax
	andl $-4, %eax
	movl -8(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_51
	label_50: 
	movl -16(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_52
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_53
	label_52: 
	movl %ecx, %eax
	label_53: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_54
	movl -16(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -12(%ebp)
	cmpl $0, -12(%ebp)
	je label_56
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_57
	label_56: 
	movl -12(%ebp), %eax
	label_57: 
	jmp label_55
	label_54: 
	movl %ecx, %eax
	label_55: 
	cmpl $0, %eax
	je label_58
	movl -16(%ebp), %ecx
	sarl $2, %ecx
	movl -8(%ebp), %eax
	sarl $2, %eax
	addl %eax, %ecx
	movl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_59
	label_58: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_59: 
	label_51: 
	movl %ecx, -8(%ebp)
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_60
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_61
	label_60: 
	label_61: 
	cmpl $0, %eax
	je label_62
	movl -8(%ebp), %eax
	andl $-4, %eax
	movl %edi, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_63
	label_62: 
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_64
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	jmp label_65
	label_64: 
	movl %ecx, %eax
	label_65: 
	movl %eax, %ecx
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_66
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -4(%ebp)
	cmpl $0, -4(%ebp)
	je label_68
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_69
	label_68: 
	movl -4(%ebp), %eax
	label_69: 
	jmp label_67
	label_66: 
	movl %ecx, %eax
	label_67: 
	cmpl $0, %eax
	je label_70
	movl -8(%ebp), %eax
	sarl $2, %eax
	movl %edi, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_71
	label_70: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_71: 
	label_63: 
	movl %ecx, %edi
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_72
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_73
	label_72: 
	label_73: 
	cmpl $0, %eax
	je label_74
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
	jmp label_75
	label_74: 
	movl %edi, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_76
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_77
	label_76: 
	movl %eax, %ecx
	label_77: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_78
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %esi
	cmpl $0, %esi
	je label_80
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_81
	label_80: 
	movl %esi, %eax
	label_81: 
	jmp label_79
	label_78: 
	movl %ecx, %eax
	label_79: 
	cmpl $0, %eax
	je label_82
	movl %edi, %ecx
	sarl $2, %ecx
	movl %ebx, %eax
	sarl $2, %eax
	addl %eax, %ecx
	movl %ecx, %eax
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
	movl %ecx, -16(%ebp)
	pushl -16(%ebp)
	call print_any
	addl $4, %esp
	movl -44(%ebp), %esi
	movl -40(%ebp), %edi
	movl -36(%ebp), %ebx
	movl $0, %eax
	leave
	ret
