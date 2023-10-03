.data
array:  .space 40          # Array of 10 integers (each integer is 4 bytes)
msg1:   .asciiz "Enter 10 integer elements, one at a time:\n"
msg2:   .asciiz "Array: "
msg3:   .asciiz "Sum of the array elements is "

.text
.globl main

main:
    # Initialize loop variables
    la $t0, array     # Load the base address of the array
    li $t1, 0         # Initialize index to 0
    li $t2, 10        # Number of elements in the array

input_loop:
    beq $t1, $t2, calculate_sum  # Exit the loop when the index reaches the number of elements

    # Prompt the user to enter an integer
    li $v0, 4
    la $a0, msg1
    syscall

    # Read an integer from the user
    li $v0, 5
    syscall
    sw $v0, ($t0)  # Store the entered integer in the array

    # Move to the next element in the array
    addi $t0, $t0, 4

    # Increment the index
    addi $t1, $t1, 1

    # Continue the loop
    j input_loop

calculate_sum:
    # Print the array elements
    li $v0, 4
    la $a0, msg2
    syscall

    la $t0, array     # Load the base address of the array
    li $t1, 0         # Initialize index to 0

print_array_loop:
    beq $t1, $t2, sum_loop  # Exit the loop when the index reaches the number of elements

    # Load the current element from the array
    lw $a0, ($t0)

    # Print the current element
    li $v0, 1
    syscall

    # Print a comma and space for formatting
    li $v0, 4
    la $a0, comma_space
    syscall

    # Move to the next element in the array
    addi $t0, $t0, 4

    # Increment the index
    addi $t1, $t1, 1

    # Continue the loop
    j print_array_loop

sum_loop:
    # Calculate the sum of the array elements
    li $t3, 0          # Initialize sum to 0
    la $t4, array      # Load the base address of the array
    li $t5, 0          # Initialize index to 0

sum_loop_inner:
    beq $t5, $t2, print_sum  # Exit the loop when the index reaches the number of elements

    # Load the current element from the array
    lw $t6, ($t4)

    # Add the current element to the sum
    add $t3, $t3, $t6

    # Move to the next element in the array
    addi $t4, $t4, 4

    # Increment the index
    addi $t5, $t5, 1

    # Continue the inner loop
    j sum_loop_inner

print_sum:
    # Print the sum of the array elements
    li $v0, 4
    la $a0, msg3
    syscall

    li $v0, 1
    move $a0, $t3
    syscall

    # Exit the program
    li $v0, 10
    syscall

.data
comma_space: .asciiz ", "
