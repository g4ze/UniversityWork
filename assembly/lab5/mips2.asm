.data
input_x_prompt: .asciiz "Enter value of x: "
input_y_prompt: .asciiz "Enter value of y: "
output_prompt: .asciiz "Larger number is: "

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

    bge $t0, $t1, x_is_larger
    move $t2, $t1
    j done

x_is_larger:
    move $t2, $t0

done:
    li $v0, 4
    la $a0, output_prompt
    syscall

    li $v0, 1
    move $a0, $t2
    syscall

    li $v0, 10
    syscall
