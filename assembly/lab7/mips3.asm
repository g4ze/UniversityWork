.data
prompt: .asciiz "Enter an integer: "
result: .asciiz "Factorial = "

.text
.globl main

main:
    # Prompt the user to enter an integer
    li $v0, 4
    la $a0, prompt
    syscall
    
    # Read an integer from the user
    li $v0, 5
    syscall
    move $s0, $v0    # Store the input value in $s0
    
    # Calculate the factorial
    li $t0, 1   # Initialize $t0 to hold the factorial value
    li $t1, 1   # Initialize $t1 to hold the loop counter
    
loop:
    mul $t0, $t0, $t1   # Multiply $t0 by $t1 and store the result in $t0
    addi $t1, $t1, 1    # Increment the loop counter
    
    # Check if the loop counter is less than or equal to the input value
    ble $t1, $s0, loop
    
    # Display the factorial result
    li $v0, 4
    la $a0, result
    syscall
    
    li $v0, 1
    move $a0, $t0
    syscall
    
    # Exit the program
    li $v0, 10
    syscall
