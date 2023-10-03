.data
array:  .word 10, 11, 9, 21, 23, 32, 1, 23, 54, 60   # Array of 10 positive integers
msg1:   .asciiz "Index of minimum element = "
msg2:   .asciiz "Minimum element = "

.text
.globl main

main:
    # Initialize loop variables
    la $t0, array     # Load the base address of the array
    li $t1, 0         # Initialize index to 0
    li $t2, 10        # Number of elements in the array

    # Initialize variables to keep track of the minimum element
    lw $t3, ($t0)     # Initialize the minimum to the first element
    li $t4, 0         # Initialize the index of the minimum

find_min_loop:
    beq $t1, $t2, print_result  # Exit the loop when the index reaches the number of elements

    # Load the current element from the array
    lw $t5, ($t0)

    # Compare the current element with the current minimum
    blt $t5, $t3, update_min

    # Increment the index
    addi $t1, $t1, 1

    # Move to the next element in the array
    addi $t0, $t0, 4

    # Continue the loop
    j find_min_loop

update_min:
    # Update the minimum element and its index
    move $t3, $t5   # Update the minimum element
    move $t4, $t1   # Update the index of the minimum

    # Increment the index
    addi $t1, $t1, 1

    # Move to the next element in the array
    addi $t0, $t0, 4

    # Continue the loop
    j find_min_loop

print_result:
    # Print the index of the minimum element
    li $v0, 4
    la $a0, msg1
    syscall

    li $v0, 1
    move $a0, $t4
    syscall

    # Print a newline for formatting
    li $v0, 4
    la $a0, newline
    syscall

    # Print the minimum element
    li $v0, 4
    la $a0, msg2
    syscall

    li $v0, 1
    move $a0, $t3
    syscall

    # Exit the program
    li $v0, 10
    syscall

.data
newline: .asciiz "\n"

