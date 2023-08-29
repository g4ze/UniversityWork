.data
input_prompt1: .asciiz "Input a is: "
input_prompt2: .asciiz "Input b is: "
quotient_string: .asciiz "Quotient is: "
remainder_string: .asciiz "Remainder is: "

.text
main:
    li $v0, 4
    la $a0, input_prompt1
    syscall

    li $v0, 5
    syscall
    move $t0, $v0

    li $v0, 4
    la $a0, input_prompt2
    syscall

    li $v0, 5
    syscall
    move $t1, $v0

    div $t0, $t1

    mflo $t2
    mfhi $t3

    li $v0, 4
    la $a0, quotient_string
    syscall

    li $v0, 1
    move $a0, $t2
    syscall

    li $v0, 4
    la $a0, remainder_string
    syscall

    li $v0, 1
    move $a0, $t3
    syscall

    li $v0, 10
    syscall
