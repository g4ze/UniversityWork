.data
prompt: .asciiz "Enter a positive integer: "
result_msg: .asciiz "The factorial is: "

.text
.globl main

main:
    # Prompt user for an integer
    li $v0, 4
    la $a0, prompt
    syscall

    # Read the integer from the user
    li $v0, 5
    syscall
    move $t0, $v0  # Store the integer in $t0

    # Check if the input is negative
    blez $t0, exit  # If negative or zero, exit

    li $t1, 1      # Initialize the factorial to 1

    for_loop:
        beqz $t0, done  # Exit the loop if input is 0

        mul $t1, $t1, $t0  # Multiply by current value of $t0
        subi $t0, $t0, 1   # Decrement $t0
        j for_loop

    done:
        # Print the result
        li $v0, 4
        la $a0, result_msg
        syscall

        li $v0, 1
        move $a0, $t1
        syscall

    exit:
        # Exit the program
        li $v0, 10
        syscall
