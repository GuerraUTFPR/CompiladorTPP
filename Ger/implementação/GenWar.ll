; ModuleID = "modulo.bc"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"() 
{
entrada_principal:
  %"retorno" = alloca i32
  store i32 0, i32* %"retorno"
  br label %"saida_principal"
saida_principal:
  %"retorno.1" = load i32, i32* %"retorno", align 4
  ret i32 %"retorno.1"
}
