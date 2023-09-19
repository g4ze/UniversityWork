.data
prompt: .asciiz "Enter value of N: "
result_msg: .asciiz "Sum of first N-Odd Numbers = "

.text
.globl main

main:
    # Prompt user for N
    li $v0, 4
    la $a0, prompt
    syscall

    # Read N from the user
    li $v0, 5
    syscall
    move $t1, $v0  # Store N in $t1

    li $t0, 0      # Initialize sum to 0

    for_loop:
        beqz $t1, done  # Exit the loop if N is 0

        # Check if current number (in $t1) is odd
        andi $t2, $t1, 1
        bnez $t2, add_number  # If odd, add it to the sum

        # If not odd, decrement N and continue the loop
        subi $t1, $t1, 1
        j for_loop

    add_number:
        add $t0, $t0, $t1  # Add the current number to the sum
        subi $t1, $t1, 1    # Decrement N
        j for_loop

    done:
        # Print the result
        li $v0, 4
        la $a0, result_msg
        syscall

        li $v0, 1
        move $a0, $t0
        syscall

        # Exit the program
        li $v0, 10
        syscall
