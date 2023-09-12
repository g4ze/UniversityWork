.data
array: .word 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
size: .word 10
sum: .word 0
result: .asciiz "Sum: "

.text
.globl main

main:
    la $s0, array   # Load the base address of the array
    lw $s1, size    # Load the size of the array
    li $s2, 0      # Initialize the sum to 0
    
    # Loop to calculate the sum
loop:
    beqz $s1, done     # Exit the loop if size=0
    
    # Calculate the sum of the current element
    lw $t0, 0($s0)     # Load the current element
    add $s2, $s2, $t0  # Add the current element to the sum
    
    # Move the pointer to the next element
    addiu $s0, $s0, 4  # Increment the pointer by 4 (word size)
    
    # Decrease the size
    subu $s1, $s1, 1
    
    # Repeat the loop
    j loop
    
done:
    # Display the sum
    li $v0, 4
    la $a0, result
    syscall
    
    li $v0, 1
    move $a0, $s2
    syscall
    
    # Terminate the program
    li $v0, 10
    syscall
