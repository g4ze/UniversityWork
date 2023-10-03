.data
A:  .word 12, 34, 67, 1, 45, 90, 11, 33, 67, 19   # Array A
B:  .word 90, 2, 93, 66, 8, 90, 99, 11, 33, 9     # Array B
C:  .space 40                                    # Array C (10 integers, each 4 bytes)
msg: .asciiz "C: "

.text
.globl main

main:
    # Initialize loop variables
    la $t0, A      # Load the base address of array A
    la $t1, B      # Load the base address of array B
    la $t2, C      # Load the base address of array C
    li $t3, 0      # Initialize index to 0
    li $t4, 10     # Number of elements in the arrays

compute_max_loop:
    beq $t3, $t4, print_result  # Exit the loop when the index reaches the number of elements

    # Load elements A[i] and B[i] from arrays
    lw $t5, ($t0)  # A[i]
    lw $t6, ($t1)  # B[i]

    # Calculate max(A[i], B[i])
    bge $t5, $t6, set_max_to_A
    move $t7, $t6  # max = B[i]
    j continue_compute_max

set_max_to_A:
    move $t7, $t5  # max = A[i]

continue_compute_max:
    # Store max in array C
    sw $t7, ($t2)

    # Increment the index
    addi $t0, $t0, 4
    addi $t1, $t1, 4
    addi $t2, $t2, 4
    addi $t3, $t3, 1

    # Continue the loop
    j compute_max_loop

print_result:
    # Print array C
    li $v0, 4
    la $a0, msg
    syscall

    la $t2, C      # Load the base address of array C
    li $t3, 0      # Initialize index to 0

print_array_loop:
    beq $t3, $t4, done  # Exit the loop when the index reaches the number of elements

    # Load the current element from array C
    lw $a0, ($t2)

    # Print the current element
    li $v0, 1
    syscall

    # Print a comma and space for formatting
    li $v0, 4
    la $a0, comma_space
    syscall

    # Increment the index
    addi $t2, $t2, 4
    addi $t3, $t3, 1

    # Continue the loop
    j print_array_loop

done:
    # Exit the program
    li $v0, 10
    syscall

.data
comma_space: .asciiz ", "
