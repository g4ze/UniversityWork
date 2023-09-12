.data
input_prompt: .asciiz "Input any character: "
output_alphabet: .asciiz "Entered character is alphabet."
output_digit: .asciiz "Entered character is digit."
output_special: .asciiz "Entered character is special character."

.text
main:
    li $v0, 4
    la $a0, input_prompt
    syscall

    li $v0, 12
    syscall
    move $t0, $v0

    li $t1, 'A'
    li $t2, 'Z'
    ble $t0, $t2, checklow
checklow:
	bge $t0, $t1, is_alphabet

    li $t1, 'a'
    li $t2, 'z'
    ble $t0, $t2, checklow1
checklow1:
	bge $t0, $t1, is_alphabet
	

    li $t1, '0'
    li $t2, '9'
    ble $t0, $t2, is_digit1
    
is_digit1:
	bge $t0, $t1, is_digit

    li $v0, 4
    la $a0, output_special
    syscall
    j done

is_alphabet:
    li $v0, 4
    la $a0, output_alphabet
    syscall
    j done

is_digit:
    li $v0, 4
    la $a0, output_digit
    syscall

done:
    li $v0, 10
    syscall
