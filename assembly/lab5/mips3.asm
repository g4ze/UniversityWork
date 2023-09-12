.data
input_x_prompt: .asciiz "Enter value of x: "
input_y_prompt: .asciiz "Enter value of y: "
input_z_prompt: .asciiz "Enter value of z: "
output_prompt: .asciiz "Largest of the three numbers is: "

.text
main:
    li $v0, 4
    la $a0, input_x_prompt
    syscall

    li $v0, 5
    syscall
    move $t0, $v0

    li $v0, 4
    la $a0, input_y_prompt
    syscall

    li $v0, 5
    syscall
    move $t1, $v0

    li $v0, 4
    la $a0, input_z_prompt
    syscall

    li $v0, 5
    syscall
    move $t2, $v0

    bge $t0, $t1, compare_with_z
    move $t0, $t1

compare_with_z:
    bge $t0, $t2, result
    move $t0, $t2

result:
    li $v0, 4
    la $a0, output_prompt
    syscall

    li $v0, 1
    move $a0, $t0
    syscall

    li $v0, 10
    syscall
