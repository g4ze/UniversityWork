import pyautogui
import time

# Delay before starting (gives you time to focus on the input area)
time.sleep(5)

# Text to type
text_to_type = """#include <iostream>

class Rational {
public:
    Rational(int numerator = 0, int denominator = 1) : num(numerator), deno(denominator) {
        simplify();
    }

    Rational operator+(const Rational& other) const {
        int newNum = num * other.deno + other.num * deno;
        int newDeno = deno * other.deno;
        return Rational(newNum, newDeno);
    }

    Rational operator-(const Rational& other) const {
        int newNum = num * other.deno - other.num * deno;
        int newDeno = deno * other.deno;
        return Rational(newNum, newDeno);
    }

    void print() const {
        std::cout << num << "/" << deno << std::endl;
    }

private:
    int num;
    int deno;

    int gcd(int a, int b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }

    void simplify() {
        int commonDivisor = gcd(num, deno);
        num /= commonDivisor;
        deno /= commonDivisor;

        if (deno < 0) {
            num *= -1;
            deno *= -1;
        }
    }
};

int main() {
    Rational r1(1, 2);
    Rational r2(2, 3);

    Rational sum = r1 + r2;
    Rational diff = r1 - r2;

    std::cout << "r1: ";
    r1.print();
    std::cout << "r2: ";
    r2.print();

    std::cout << "Sum: ";
    sum.print();

    std::cout << "Difference: ";
    diff.print();

    return 0;
}
"""

# Type the text one character at a time
pyautogui.typewrite(text_to_type, interval=0.1)  # Interval between key presses

# Press Enter at the end
pyautogui.press("enter")