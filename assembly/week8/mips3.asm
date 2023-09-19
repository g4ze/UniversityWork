.data
prompt: .asciiz "Enter a number: "
prime_msg: .asciiz "This is a prime number!"
not_prime_msg: .asciiz "This is not a prime number."

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

    # Check if the number is less than 2 (not prime)
    li $t1, 2
    blt $t0, $t1, not_prime

    # Check for prime
    li $t1, 2  # Initialize divisor

    prime_loop:
        beq $t1, $t0, prime  # If divisor equals the number, it's prime
        divu $t2, $t0, $t1  # Divide the number by divisor

        mfhi $t3  # Remainder is in $t3

        beqz $t3, not_prime  # If remainder is zero, it's not prime

        addi $t1, $t1, 1  # Increment divisor
        j prime_loop

    prime:
        # Print "This is a prime number!" and exit
        li $v0, 4
        la $a0, prime_msg
        syscall
        j exit

    not_prime:
        # Print "This is not a prime number." and exit
        li $v0, 4
        la $a0, not_prime_msg
        syscall

    exit:
        # Exit the program
        li $v0, 10
        syscall
