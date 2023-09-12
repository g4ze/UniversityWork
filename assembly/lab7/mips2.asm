.data
    i: .word 1
    format: .asciiz " \n"

.text
.globl main

main:
    # Initialize $i to 1
    li $t0, 1
    
loop:
    # Print the value of $i
    li $v0, 1
    lw $a0, i
    syscall
    
    # Print a newline
    li $v0, 4
    la $a0, format
    syscall
    
    # Increment $i
    lw $t1, i
    addi $t1, $t1, 1
    sw $t1, i
    
    # Check if $i <= 10
    lw $t1, i
    li $t2, 10
    ble $t1, $t2, loop
    
    # Wait for user input
    li $v0, 12
    syscall

    # Terminate the program
    li $v0, 10
    syscall
