.data
input_prompt: .asciiz "Enter the string: "
output_string: .asciiz "String is: "

.text
main:
    li $v0, 4
    la $a0, input_prompt
    syscall

    li $v0, 8
    la $a0, input_buffer   # Load address of input_buffer
    li $a1, 100
    syscall

    li $v0, 4
    la $a0, output_string
    syscall

    li $v0, 4
    la $a0, input_buffer   # Load address of input_buffer
    syscall

    li $v0, 10
    syscall

.data
input_buffer: .space 100
