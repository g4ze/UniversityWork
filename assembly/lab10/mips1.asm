.data
array:  .word 10, 11, 9, 21, 23   # Array of 5 elements
msg:    .asciiz "The array elements are:\n"

.text
.globl main

main:
    # Print the message
    li $v0, 4
    la $a0, msg
    syscall

    # Initialize loop variables
    la $t0, array     # Load the base address of the array
    li $t1, 0         # Initialize index to 0
    li $t2, 5         # Number of elements in the array

print_loop:
    beq $t1, $t2, done  # Exit the loop when the index reaches the number of elements

    # Load the current element from the array
    lw $a0, ($t0)

    # Print the current element
    li $v0, 1
    syscall

    # Print a newline character
    li $v0, 4
    la $a0, newline
    syscall

    # Move to the next element in the array
    addi $t0, $t0, 4

    # Increment the index
    addi $t1, $t1, 1

    # Continue the loop
    j print_loop

done:
    # Exit the program
    li $v0, 10
    syscall

.data
newline: .asciiz "\n"
