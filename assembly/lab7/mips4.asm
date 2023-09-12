.data
prompt1: .asciiz "Enter the initial value: "
prompt2: .asciiz "Enter the final value: "
result: .asciiz "Result: "
line: .asciiz " \n"

.text
.globl main

main:
    # Prompt the user to enter the initial value
    li $v0, 4
    la $a0, prompt1
    syscall
    
    # Read the initial value from the user
    li $v0, 5
    syscall
    move $s0, $v0   # Store the initial value in $s0
    
    # Prompt the user to enter the final value
    li $v0, 4
    la $a0, prompt2
    syscall
    
    # Read the final value from the user
    li $v0, 5
    syscall
    move $s1, $v0   # Store the final value in $s1
    
    # Display the countdown
    li $v0, 4
    la $a0, result
    syscall
    
    move $t0, $s0   # Initialize $t0 with the initial value
    
loop:
    # Print the current value
    move $a0, $t0
    li $v0, 1
    syscall
    
    li $v0, 4
    la $a0, line
    syscall
    
    # Decrement the current value
    subi $t0, $t0, 1
    
    # Check if the current value is greater than or equal to the final value
    bge $t0, $s1, loop
    
    # Terminate the program
    li $v0, 10
    syscall
