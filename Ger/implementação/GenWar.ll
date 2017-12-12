; ModuleID = "modulo.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

@"aaaaaaa" = common global float              0x0, align 4
@"glob" = common global i32 0, align 4
define void @"funcaoVazia"() 
{
entrada_funcaoVazia:
  %"a" = alloca i32, align 4
saida_funcaoVazia:
}

define i32 @"teste"(i32 %".1", float %".2") 
{
entrada_teste:
  %"c" = alloca i32, align 4
saida_teste:
}

define i32 @"principal"() 
{
entrada_principal:
  %"x" = alloca i32, align 4
  %"y" = alloca float, align 4
  %"matheus" = alloca float, align 4
saida_principal:
}
