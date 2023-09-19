.data

.text
.globl main

main:
    li $t0, 35  # Start from 35

    reverse_loop:
        bgez $t0, print_number
        j done

    print_number:
        li $v0, 1
        move $a0, $t0
        syscall

        # Print a newline character
        li $v0, 4
        la $a0, newline
        syscall

        subi $t0, $t0, 1  # Decrement and continue loop
        j reverse_loop

    done:
        # Exit the program
        li $v0, 10
        syscall

.data
newline: .asciiz "\n"
