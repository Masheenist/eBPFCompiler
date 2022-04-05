.globl main
main:
	pushl %ebp
	movl %esp, %ebp
	movl %ebx, -24(%ebp)
	movl %edi, -28(%ebp)
	movl %esi, -32(%ebp)
	subl $36, %esp
	call input
	addl $0, %esp
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
	je label_0
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_1
	label_0: 
	movl %ecx, %eax
	label_1: 
	cmpl $0, %eax
	je label_2
	movl %ebx, %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_3
	label_2: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_3: 
	movl %ecx, -12(%ebp)
	movl %ebx, -20(%ebp)
	movl -20(%ebp), %eax
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
	movl -20(%ebp), %eax
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
	movl -20(%ebp), %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_7
	label_6: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_7: 
	movl %ecx, -20(%ebp)
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_8
	movl -20(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_9
	label_8: 
	label_9: 
	cmpl $0, %eax
	je label_10
	movl %ebx, %eax
	andl $-4, %eax
	movl -20(%ebp), %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_11
	label_10: 
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_12
	movl -20(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_13
	label_12: 
	movl %eax, %ecx
	label_13: 
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
	movl %eax, -24(%ebp)
	cmpl $0, -24(%ebp)
	je label_16
	movl -20(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_17
	label_16: 
	movl -24(%ebp), %eax
	label_17: 
	jmp label_15
	label_14: 
	movl %ecx, %eax
	label_15: 
	cmpl $0, %eax
	je label_18
	movl %ebx, %eax
	sarl $2, %eax
	movl -20(%ebp), %ecx
	sarl $2, %ecx
	addl %ecx, %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_19
	label_18: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_19: 
	label_11: 
	movl %ecx, -20(%ebp)
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
	je label_20
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_21
	label_20: 
	movl %ecx, %eax
	label_21: 
	cmpl $0, %eax
	je label_22
	movl %ebx, %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_23
	label_22: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_23: 
	movl %ecx, -24(%ebp)
	movl -20(%ebp), %eax
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
	movl -20(%ebp), %eax
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
	movl -20(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	cmpl $0, %ecx
	je label_28
	movl -24(%ebp), %eax
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
	movl -20(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, -4(%ebp)
	cmpl $0, -4(%ebp)
	je label_32
	movl -24(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_33
	label_32: 
	movl -4(%ebp), %eax
	label_33: 
	jmp label_31
	label_30: 
	movl %ecx, %eax
	label_31: 
	cmpl $0, %eax
	je label_34
	movl -20(%ebp), %eax
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
	movl %ecx, -4(%ebp)
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_36
	movl %ebx, -8(%ebp)
	andl $-4, -8(%ebp)
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -8(%ebp)
	call equal
	addl $8, %esp
	movl %eax, -8(%ebp)
	cmpl $0, -8(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_38
	movl %ebx, -8(%ebp)
	andl $-4, -8(%ebp)
	call create_dict
	addl $0, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl -8(%ebp)
	call equal
	addl $8, %esp
	movl %eax, %ecx
	jmp label_39
	label_38: 
	movl -8(%ebp), %ecx
	label_39: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_37
	label_36: 
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
	je label_40
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_41
	label_40: 
	label_41: 
	cmpl $0, %ecx
	je label_42
	movl %ebx, %eax
	sarl $2, %eax
	jmp label_43
	label_42: 
	call abort
	addl $0, %esp
	label_43: 
	movl %eax, %ecx
	label_37: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	sall $2, %eax
	orl $1, %eax
	movl %eax, -8(%ebp)
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
	je label_44
	movl %ebx, %eax
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
	movl %ebx, %eax
	sarl $2, %eax
	negl %eax
	sall $2, %eax
	orl $0, %eax
	movl %eax, %ecx
	jmp label_47
	label_46: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_47: 
	movl %ecx, %ebx
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_48
	movl %ebx, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	jmp label_49
	label_48: 
	label_49: 
	cmpl $0, %eax
	je label_50
	movl -8(%ebp), %eax
	andl $-4, %eax
	movl %ebx, %ecx
	andl $-4, %ecx
	pushl %ecx
	pushl %eax
	call add
	addl $8, %esp
	addl $3, %eax
	movl %eax, %ecx
	jmp label_51
	label_50: 
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_52
	movl %ebx, %eax
	andl $3, %eax
	cmpl $0, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %ecx
	jmp label_53
	label_52: 
	movl %eax, %ecx
	label_53: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_54
	movl -8(%ebp), %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	movl %eax, %esi
	cmpl $0, %esi
	je label_56
	movl %ebx, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_57
	label_56: 
	movl %esi, %eax
	label_57: 
	jmp label_55
	label_54: 
	movl %ecx, %eax
	label_55: 
	cmpl $0, %eax
	je label_58
	movl -8(%ebp), %eax
	sarl $2, %eax
	movl %ebx, %ecx
	sarl $2, %ecx
	addl %ecx, %eax
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
	movl %ecx, %ebx
	movl -12(%ebp), %esi
	movl %esi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_60
	movl %esi, %edi
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
	je label_62
	movl %esi, %edi
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
	jmp label_63
	label_62: 
	movl %edi, %ecx
	label_63: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_61
	label_60: 
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
	je label_64
	movl %esi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_65
	label_64: 
	movl %ecx, %eax
	label_65: 
	cmpl $0, %eax
	je label_66
	movl %esi, %eax
	sarl $2, %eax
	movl %eax, %ecx
	jmp label_67
	label_66: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_67: 
	movl %ecx, %eax
	label_61: 
	cmpl $0, %eax
	je label_68
	movl -4(%ebp), %ecx
	jmp label_69
	label_68: 
	movl %esi, %ecx
	label_69: 
	movl %ecx, %eax
	movl %eax, %edi
	movl %edi, %eax
	andl $3, %eax
	cmpl $3, %eax
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_70
	movl %edi, %esi
	andl $-4, %esi
	movl $0, %eax
	sall $2, %eax
	orl $0, %eax
	pushl %eax
	call create_list
	addl $4, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl %esi
	call equal
	addl $8, %esp
	movl %eax, -16(%ebp)
	cmpl $0, -16(%ebp)
	sete %al
	movzbl %al, %eax
	cmpl $0, %eax
	je label_72
	movl %edi, %esi
	andl $-4, %esi
	call create_dict
	addl $0, %esp
	addl $3, %eax
	andl $-4, %eax
	pushl %eax
	pushl %esi
	call equal
	addl $8, %esp
	movl %eax, %ecx
	jmp label_73
	label_72: 
	movl -16(%ebp), %ecx
	label_73: 
	cmpl $0, %ecx
	sete %al
	movzbl %al, %eax
	jmp label_71
	label_70: 
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
	je label_74
	movl %edi, %eax
	andl $3, %eax
	cmpl $1, %eax
	sete %al
	movzbl %al, %eax
	jmp label_75
	label_74: 
	movl %ecx, %eax
	label_75: 
	cmpl $0, %eax
	je label_76
	movl %edi, %eax
	sarl $2, %eax
	movl %eax, %ecx
	jmp label_77
	label_76: 
	call abort
	addl $0, %esp
	movl %eax, %ecx
	label_77: 
	movl %ecx, %eax
	label_71: 
	cmpl $0, %eax
	je label_78
	movl %ebx, %ecx
	jmp label_79
	label_78: 
	movl %edi, %ecx
	label_79: 
	movl %ecx, %eax
	pushl %eax
	call print_any
	addl $4, %esp
	movl -32(%ebp), %esi
	movl -28(%ebp), %edi
	movl -24(%ebp), %ebx
	movl $0, %eax
	leave
	ret
