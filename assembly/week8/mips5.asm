.data
prompt: .asciiz "Enter a number: "
square_msg: .asciiz "It is a square number."
not_square_msg: .asciiz "It is not a square number."

.text
.globl main

main:
    # Prompt user for a number
    li $v0, 4
    la $a0, prompt
    syscall

    # Read the number from the user
    li $v0, 5
    syscall
    move $t0, $v0  # Store the number in $t0

    # Initialize variables
    li $t1, 1       # Initialize the square root to 1
    li $t2, 0       # Initialize the square to 0

    square_loop:
        mul $t3, $t1, $t1  # Calculate square ($t3 = $t1 * $t1)

        bge $t3, $t0, check_square  # Check if square is greater than or equal to input

        addi $t1, $t1, 1  # Increment the square root
        j square_loop

    check_square:
        beq $t3, $t0, is_square  # If square equals input, it's a square number

        # If not a square number, print "It is not a square number."
        li $v0, 4
        la $a0, not_square_msg
        syscall
        j exit

    is_square:
        # If it's a square number, print "It is a square number."
        li $v0, 4
        la $a0, square_msg
        syscall

    exit:
        # Exit the program
        li $v0, 10
        syscall
