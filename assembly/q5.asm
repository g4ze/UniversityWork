.data
input_prompt: .asciiz "Enter the number to be checked for even or odd: "
output_even: .asciiz " is even"
output_odd: .asciiz " is odd"

.text
main:
    li $v0, 4
    la $a0, input_prompt
    syscall

    li $v0, 5
    syscall
    move $t0, $v0

    andi $t1, $t0, 1

    li $v0, 1
    move $a0, $t0
    syscall

    beqz $t1, even
    la $a0, output_odd
    j done

even:
    la $a0, output_even

done:
    li $v0, 4
    syscall

    li $v0, 10
    syscall
