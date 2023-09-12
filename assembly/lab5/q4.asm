.data
name_prompt: .asciiz "Enter your name: "
year_prompt: .asciiz "Enter your birth year: "
output_string: .asciiz "He is "
dash_string: .asciiz "-year-old!!"

.text
main:
    li $v0, 4
    la $a0, name_prompt
    syscall

    li $v0, 8
    la $a0, input_buffer   # Load address of input_buffer
    li $a1, 100
    syscall

    li $v0, 4
    la $a0, year_prompt
    syscall

    li $v0, 5
    syscall
    move $t1, $v0

    li $t2, 2023

    sub $t3, $t2, $t1

    li $v0, 4
    la $a0, output_string
    syscall

    li $v0, 1
    move $a0, $t3
    syscall

    li $v0, 4
    la $a0, dash_string
    syscall

    li $v0, 10
    syscall

.data
input_buffer: .space 100
