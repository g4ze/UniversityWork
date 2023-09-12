.data
cost_prompt: .asciiz "Input the cost price in Rupees: "
sell_prompt: .asciiz "Input the selling price in Rupees: "
profit_msg: .asciiz "Seller has made the profit (in Rs) of "
loss_msg: .asciiz "Seller has incurred a loss (in Rs) of "

.text
main:
    li $v0, 4
    la $a0, cost_prompt
    syscall

    li $v0, 5
    syscall
    move $t0, $v0

    li $v0, 4
    la $a0, sell_prompt
    syscall

    li $v0, 5
    syscall
    move $t1, $v0

    sub $t2, $t1, $t0

    bgez $t2, is_profit

    li $v0, 4
    la $a0, loss_msg
    syscall

    negu $t2, $t2

    li $v0, 1
    move $a0, $t2
    syscall
    j done

is_profit:
    li $v0, 4
    la $a0, profit_msg
    syscall

    li $v0, 1
    move $a0, $t2
    syscall

done:
    li $v0, 10
    syscall

