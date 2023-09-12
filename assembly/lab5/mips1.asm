.data
input_prompt: .asciiz "Enter value of x: "
output_string: .asciiz "Result of equation is: "

.text
main:
    li $v0, 4
    la $a0, input_prompt
    syscall

    li $v0, 5
    syscall
    move $t0, $v0

    li $t1, 5
    li $t2, 2
    li $t3, 3

    mul $t4, $t0, $t0
    mul $t5, $t1, $t4
    mul $t6, $t2, $t0
    add $t7, $t5, $t6
    add $t8, $t7, $t3

    li $v0, 4
    la $a0, output_string
    syscall

    li $v0, 1
    move $a0, $t8
    syscall

    li $v0, 10
    syscall
