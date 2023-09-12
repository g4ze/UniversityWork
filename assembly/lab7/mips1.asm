.data
welcome_message: .asciiz "Welcome to CSET203 LAB\n"
loop_message: .asciiz "Loop Step Count\n"
loop_counter: .word 1

.text
.globl main

main:
    # Print the welcome message
    li $v0, 4
    la $a0, welcome_message
    syscall
    
    # Print the loop message
    li $v0, 4
    la $a0, loop_message
    syscall
    
    # Initialize $t0 to 1 (loop counter)
    li $t0, 1
    
loop:
    # Print the loop counter value
    li $v0, 1
    move $a0, $t0
    syscall
    
    # Increment the loop counter 
