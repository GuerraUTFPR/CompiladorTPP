	.text
	.file	"GenWar.ll"
	.globl	main
	.align	16, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# BB#0:                                 # %entrada_principal
	movl	$0, -4(%rsp)
	movl	a(%rip), %eax
	movl	%eax, -8(%rsp)
	movl	-4(%rsp), %eax
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main
	.cfi_endproc

	.type	a,@object               # @a
	.comm	a,4,4

	.section	".note.GNU-stack","",@progbits
