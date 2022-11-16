# Create a dictionary to store the explanations
data = {
    1: ["Binary to Binary: The binary number is the same as the original number", 
        "Binary to Octal: The given binary number is taken and each digit is multiplied by 2n-1 where n is the\n"
        "position of the digit from the decimal.Then the resultant is the equivalent decimal number for the given\n"
        "binary number. The decimal number is divided by 8 and the remainder is noted. The above two steps are\n"
        "continued with the quotient till the quotient is zero.The remainder is written  in the reverse order to get\n"
        "the result.",
        "Binary to Decimal: To convert a binary number to decimal ,a multiplication operation is performed on each\n"
        "digit of a binary number from right to left with powers of 2 starting from 0 and  each result is added to\n"
        "get the decimal number of it.",
        "Binary to Hexadecimal: Binary numbers are first converted to decimal numbers then to a hexadecimal number.\n"
        "Here, the base number of a decimal number is 10. The binary number can be converted to a decimal number by\n"
        "expressing each digit as a product of the given number 1 or 0 to the respective power of 2. And to convert\n"
        "from decimal to hexadecimal we divide the number 16 until the quotient is zero"],
    2: ["Octal to Binary: Octal numbers have base 8 and binary numbers have base 2. Count the number of digits\n"
        "present in the given number(n).Now multiply each digit of the number with 8n-1, when the digit is in the nth\n"
        "position from the right end of the number. If the number has a decimal part, multiply each digit in the\n"
        "decimal part by `8-m` when the digit is in the mth position from the decimal point.Now add all the terms\n"
        "after multiplication.The obtained value is the equivalent decimal number. Take the above-produced decimal\n"
        "number and divide it by 2 and note down the remainder.Continue the above two steps for the quotient till the\n"
        "quotient is zero and write the remainder in the reverse order. The received number is the equivalent binary\n"
        "number for the given octal number.",
        "Octal to Octal: The octal number is the same as the original number", 
        "Octal to Decimal: Octal Number System has a base of eight and uses the numbers from 0 to 7. The octal\n"
        "numbers, in the number system, are usually represented by binary numbers when they are grouped in pairs of\n"
        "three. For example, an octal number 128 is expressed as 0010102 in the binary system, where 1 is equivalent\n"
        "to 001 and 2 is equivalent to 010.",
        "Octal to Hexadecimal: Firstly we write the powers of 8 (1, 8, 64, 512, 4096, and so on) beside the octal\n"
        "digits from bottom to top.then we multiply each digit by its power and add up the answers. This is the\n"
        "decimal solution.Now, we divide the decimal number by 16. We then get the integer quotient for the next\n"
        "iteration .Repeat the steps from step 4. until the quotient is equal to 0.Then we write out all the\n"
        "remainders, from bottom to top and convert any remainders bigger than 9 into hex letters. This is the\n"
        "hexadecimal solution."],
    3: ["Hexadecimal to Binary: It is not possible to convert it directly, we will convert hexadecimal to decimal\n"
        "then that decimal number is converted to binary. Split the hex number into individual values.We firstly\n"
        "convert each hex value into its decimal equivalent.Next, convert each decimal digit into binary, making sure\n"
        "to write four digits for each value.Combine all four digits to make one binary number.",
        "Hexadecimal to Octal: Conversion of hexadecimal to octal cannot be done directly. Firstly we need to convert\n"
        "hexadecimal into its equivalent decimal number then decimal to octal. First count the number of digits in\n"
        "the number , if n is the position of the digit from the right end then multiply each digit with 16n-1 and\n"
        "add the terms after multiplication the resultant is the equivalent decimal form.Then we divide the decimal\n"
        "number with 8 and note down the remainder. Repeat the previous two steps with the quotient,\n"
        "until the quotient is zero and write the remainders in reverse order . The obtained number is the required\n"
        "result.",
        "Hexadecimal to Decimal: To convert this into a decimal number system , first count the number of digits in\n"
        "the number , if n is the position of the digit from the right end then multiply each digit with 16n-1 and\n"
        "add the terms after multiplication the resultant is the equivalent decimal form.",
        "Hexadecimal to Hexadecimal: The hexadecimal number is the same as the original number"],
    4: ["Decimal to Binary: A decimal number is divided by '2' and some remainder is left.If the decimal number is\n"
        "even, then the result will be in a whole number and  the remainder is 0.If the decimal number is odd,\n"
        "then the number will not be divided fully and  remainder is '1'.Division continues till the quotient is\n"
        "0.Now all the remainders are placed in the series of Least Significant Bit (LSB) at the top and the Most\n"
        "Significant bit (MSB) at the bottom.",
        "Decimal to Octal: The number is divided by 8 and the remainders are written in the reverse order to get the\n"
        "equivalent octal number",
        "Decimal to Decimal: The decimal number is the same as the original number", 
        "Decimal to Hexadecimal: Decimal number is divided by 16 and the remainder is noted.Then e the quotient is\n"
        "divided  by 16. This  is repeated until the quotient equal to zero and the reverse order pattern is followed\n"
        "to arrange all the values of the remainder. The obtained number is the required hexadecimal number."]
}
