# -*- coding: utf-8 -*-
"""
Content generator for Subject 12: Programming in C (EST102)
KTU 2019 Scheme First Year Engineering Comprehensive Question Bank.
All answers are written from the perspective of an experienced computer science professor:
clear, direct, syntactically rigorous, complete with production-grade commented C code snippets,
memory execution diagrams, and step-by-step trace/output explanations.
All strings are raw multiline strings (r\"\"\"...\"\"\") to prevent LaTeX/C escape corruptions.
"""

CPROG_MODULES = [
    {
        "module_id": "cprog-m1",
        "module_num": "Module 1",
        "module_title": "Basics of C Programming, Operators, I/O & Control Flow",
        "questions": [
            {
                "qid": "cprog-q1",
                "marks": 7,
                "type": "Descriptive",
                "title": "Structure of a C Program, Compilation and Execution Process, Tokens, and Identifiers",
                "yt_query": "structure of C program compilation execution process tokens identifiers",
                "img_path": "images/cprog/c_compilation_process.png",
                "img_caption": "Figure 1.1: Multi-Stage Compilation Pipeline (Preprocessor, Compiler, Assembler, Linker, Loader)",
                "answer": r"""
C is a general-purpose, statically typed, procedural programming language developed in 1972 by Dennis Ritchie at Bell Laboratories for implementing the UNIX operating system. It provides low-level memory access capabilities while retaining high-level structural constructs.

1. Fundamental Structure of a C Program:
A standard C source program is organized into distinct logical sections:
```c
/* 1. Documentation Section: Comments describing program purpose, author, date */
// Project: Temperature Conversion System

/* 2. Link / Preprocessor Section: Header file inclusions and symbolic constants */
#include <stdio.h>
#define FREEZING_POINT 32.0f

/* 3. Definition Section: Global variable definitions and type definitions */
typedef float Temperature;

/* 4. Global Declaration Section: Function prototypes and external variables */
Temperature fahrenheit_to_celsius(Temperature fahr);

/* 5. Main Function Section: Mandatory execution entry point */
int main(void) {
    Temperature input_fahr = 98.6f;
    Temperature result_celsius;
    
    result_celsius = fahrenheit_to_celsius(input_fahr);
    printf("Fahrenheit: %.2f F -> Celsius: %.2f C\n", input_fahr, result_celsius);
    
    return 0; /* Indicates successful termination to the operating system */
}

/* 6. Subprogram / Function Definition Section */
Temperature fahrenheit_to_celsius(Temperature fahr) {
    return (fahr - FREEZING_POINT) * (5.0f / 9.0f);
}
```

2. The C Compilation and Execution Pipeline:
Translating human-readable C source code (`program.c`) into an executable machine binary involves four sequential phases:
1. Preprocessor (`cpp`):
   - Strips all comments (`/* ... */` and `//`).
   - Expands all header files included via `#include` directives by inserting the complete text of the header.
   - Replaces symbolic macro definitions (`#define`) with literal replacement text.
   - Handles conditional compilation directives (`#ifdef`, `#ifndef`, `#endif`).
   - Output: Preprocessed pure C text file (`program.i`).
2. Compiler (`cc1`):
   - Performs lexical analysis, parsing, semantic verification, and intermediate representation (IR) code generation.
   - Translates preprocessed C code into target architecture-specific Assembly language instructions.
   - Output: Assembly source file (`program.s`).
3. Assembler (`as`):
   - Translates assembly mnemonic instructions into relocatable machine-level object code (binary 0s and 1s).
   - Generates symbol tables and relocation dictionaries.
   - Output: Relocatable machine object file (`program.o` or `program.obj`).
4. Linker (`ld`):
   - Resolves external function references across multiple object files and links standard precompiled C runtime system libraries (e.g., `libc.a`, `libm.a` for math functions).
   - Combines object modules into a single, cohesive executable binary file (`a.out` or `program.exe`).
5. Loader:
   - Operating system kernel subsystem that allocates virtual memory (text, data, heap, stack segments), copies machine instructions from disk into physical RAM, initializes CPU registers, and transfers program execution control to `main()`.

3. C Tokens, Keywords, and Identifiers:
A Token is the smallest individual grammatical unit in a C program recognized by the compiler during lexical analysis. C tokens are categorized into six groups:
1. Keywords: 32 reserved words in C89/C90 (expanded to 44 in C11) that have fixed predefined meanings and cannot be repurposed as user variable names (e.g., `int`, `return`, `static`, `sizeof`, `volatile`, `struct`).
2. Identifiers: User-defined names assigned to variables, functions, arrays, and labels. Identifier naming rules:
   - Allowed characters: English uppercase letters ($A-Z$), lowercase letters ($a-z$), decimal digits ($0-9$), and the underscore character (`_`).
   - The first character must strictly be a letter or an underscore; it cannot be a digit (e.g., `_total1` is valid; `1total` is illegal).
   - Case-sensitive: `Sum`, `sum`, and `SUM` represent three distinct identifiers.
   - No whitespace, hyphens, or special punctuation symbols are permitted.
   - Cannot be a reserved C keyword.
3. Constants: Fixed literal values that do not alter during program execution (Integer: `42`, Floating-point: `3.14159`, Character: `'A'`, String: `"KTU"`).
4. String Literals: Sequences of characters enclosed within double quotes terminated internally by a null byte `\0`.
5. Operators: Symbols instructing the compiler to execute mathematical or logical operations (`+`, `*`, `&&`, `sizeof`).
6. Special Delimiters / Punctuators: Brackets, braces, parentheses, commas, and semicolons (`( )`, `{ }`, `[ ]`, `;`, `,`).
"""
            },
            {
                "qid": "cprog-q2",
                "marks": 7,
                "type": "Descriptive",
                "title": "Data Types in C: Fundamental Types, Modifiers, Qualifiers, and Explicit vs Implicit Type Conversion",
                "yt_query": "data types in C size range modifiers type conversion casting",
                "img_path": "images/cprog/c_data_types_hierarchy.png",
                "img_caption": "Figure 1.2: C Data Type Classification Hierarchy and Type Promotion Ladder",
                "answer": r"""
Data types in C define the binary storage format, the memory byte allocation, and the permissible operations that can be performed on declared program variables.

1. Fundamental (Primitive) Data Types:
- Integer (`int`): Stores whole numbers without fractional parts. In standard 32-bit and 64-bit systems, `int` occupies $4\text{ bytes}$ ($32\text{ bits}$).
- Character (`char`): Stores a single character using ASCII encoding. Consistently occupies exactly $1\text{ byte}$ ($8\text{ bits}$).
- Single-Precision Floating-Point (`float`): Stores IEEE 754 single-precision real numbers with approximately 6 to 7 decimal digits of precision ($4\text{ bytes}$).
- Double-Precision Floating-Point (`double`): Stores IEEE 754 double-precision real numbers with approximately 15 to 17 decimal digits of precision ($8\text{ bytes}$).
- Void (`void`): Represents the absence of type or an empty value (used for functions returning no value or generic pointers `void *`).

2. Type Modifiers:
Type modifiers alter the storage capacity and range of fundamental types:
- Sign Modifiers: `signed` (default for integer types; uses two's complement for positive and negative values) and `unsigned` (stores only non-negative values, doubling positive range).
- Size Modifiers: `short` (guarantees at least $16\text{ bits}$), `long` (guarantees at least $32\text{ bits}$), and `long long` (guarantees at least $64\text{ bits}$).

Comprehensive Size and Range Table (Standard 64-bit Architecture):
| Type Specification | Storage Size | Minimum Value | Maximum Value | Format Specifier |
|---|---|---|---|---|
| `char` / `signed char` | $1\text{ byte}$ | $-128$ ($-2^7$) | $+127$ ($2^7 - 1$) | `%c` or `%d` |
| `unsigned char` | $1\text{ byte}$ | $0$ | $255$ ($2^8 - 1$) | `%u` |
| `short int` | $2\text{ bytes}$ | $-32,768$ ($-2^{15}$) | $+32,767$ ($2^{15} - 1$) | `%hd` |
| `unsigned short int` | $2\text{ bytes}$ | $0$ | $65,535$ ($2^{16} - 1$) | `%hu` |
| `int` / `signed int` | $4\text{ bytes}$ | $-2,147,483,648$ ($-2^{31}$) | $+2,147,483,647$ ($2^{31} - 1$) | `%d` or `%i` |
| `unsigned int` | $4\text{ bytes}$ | $0$ | $4,294,967,295$ ($2^{32} - 1$) | `%u` |
| `long int` | $8\text{ bytes}$ | $-2^{63}$ | $+2^{63} - 1$ | `%ld` |
| `float` | $4\text{ bytes}$ | $\approx 1.2 \times 10^{-38}$ | $\approx 3.4 \times 10^{38}$ | `%f` |
| `double` | $8\text{ bytes}$ | $\approx 2.3 \times 10^{-308}$ | $\approx 1.7 \times 10^{308}$ | `%lf` |
| `long double` | $16\text{ bytes}$ | $\approx 3.4 \times 10^{-4932}$ | $\approx 1.1 \times 10^{4932}$ | `%Lf` |

3. Type Qualifiers:
- `const`: Prevents runtime modification of the variable value ($read-only$ memory protection).
- `volatile`: Informs the compiler optimizer that the variable's value can change unexpectedly through external hardware, interrupts, or concurrent threads, forcing the CPU to fetch directly from memory rather than caching in a register.

4. Type Conversion in Expressions:
- Implicit Type Conversion (Automatic Type Promotion):
When operands of differing types appear in a single arithmetic expression, C automatically promotes the lower-ranked operand to the type of the higher-ranked operand before evaluation, without programmer intervention:
$$\text{Promotion Ladder: } \text{char, short} \to \text{int} \to \text{unsigned int} \to \text{long} \to \text{float} \to \text{double} \to \text{long double}$$
Example: In `float result = 5 / 2;`, both `5` and `2` are integer literals. Integer division truncates fractional parts, yielding `2`. Then `2` is implicitly converted to `2.0f`.
- Explicit Type Conversion (Type Casting):
The programmer explicitly forces a variable to convert to a target type using the cast operator: `(target_type) expression`.
Example:
```c
int total_marks = 475;
int subjects = 5;
/* Force floating-point division using explicit cast */
float average = (float)total_marks / subjects; /* 475.0 / 5 = 95.0 */
```
"""
            },
            {
                "qid": "cprog-q3",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Operators in C: Arithmetic, Relational, Logical, Bitwise, Precedence, and Associativity",
                "yt_query": "operators in C bitwise operators precedence associativity rules table",
                "img_path": "images/cprog/c_operator_precedence.png",
                "img_caption": "Figure 1.3: Summary Table of C Operator Precedence, Arity, and Direction of Associativity",
                "answer": r"""
An operator is a symbol that commands the compiler to perform a specific mathematical, relational, logical, or bit-manipulation operation on one, two, or three operands.

1. Classification of Operators in C:
1. Arithmetic Operators: Addition (`+`), Subtraction (`-`), Multiplication (`*`), Division (`/`, integer truncation applies when both operands are integers), and Modulo (`%`, remainder after integer division; operands must strictly be integral types).
2. Increment and Decrement Operators:
   - Prefix (`++x`, `--x`): Increments/decrements the operand value first, then returns the updated value in the expression ($Change-then-Use$).
   - Postfix (`x++`, `x--`): Evaluates the original operand value in the current expression first, then increments/decrements the operand ($Use-then-Change$).
3. Relational Operators: Compare two values, returning integer `1` for true and `0` for false: `<`, `<=`, `>`, `>=`, `==` (equality check), `!=` (inequality check).
4. Logical Operators:
   - Logical AND (`&&`): Returns 1 only if both operands are non-zero. Features Short-Circuit Evaluation: if the left operand evaluates to 0 (false), the right operand is completely skipped and not executed.
   - Logical OR (`||`): Returns 1 if at least one operand is non-zero. Short-circuits: if the left operand is non-zero (true), the right operand is not evaluated.
   - Logical NOT (`!`): Unary operator; inverts boolean truth value (`!0 == 1`, `!nonzero == 0`).
5. Bitwise Operators: Manipulate individual binary bits of integer operands directly:
   - Bitwise AND (`&`): Sets bit to 1 only if corresponding bits of both operands are 1.
   - Bitwise OR (`|`): Sets bit to 1 if either corresponding bit is 1.
   - Bitwise XOR (`^`): Sets bit to 1 if corresponding bits differ ($1 \oplus 0 = 1$, $1 \oplus 1 = 0$).
   - Bitwise NOT / One's Complement (`~`): Flips all bits ($0 \to 1, 1 \to 0$).
   - Bitwise Left Shift (`<<`): Shifts bits left by $k$ positions, filling with zeros; equivalent to multiplying by $2^k$:
$$x \ll k = x \times 2^k$$
   - Bitwise Right Shift (`>>`): Shifts bits right by $k$ positions; equivalent to integer floor division by $2^k$:
$$x \gg k = \lfloor x / 2^k \rfloor$$
6. Conditional (Ternary) Operator (`? :`): Concise inline conditional assignment:
$$\text{condition ? expression\_if\_true : expression\_if\_false}$$
7. Special Operators: `sizeof` (evaluates byte size at compile-time), comma operator (`,`, evaluates left-to-right, returns rightmost value), address-of (`&`), and indirection (`*`).

2. Operator Precedence and Associativity Rules:
When an expression contains multiple operators, Precedence dictates the operational binding order. If two adjacent operators possess identical precedence, Associativity dictates whether evaluation proceeds from Left-to-Right or Right-to-Left.

| Level | Operator Category | Specific Operators | Associativity |
|---|---|---|---|
| 1 (Highest) | Postfix, Array, Member | `()`, `[]`, `->`, `.`, `x++`, `x--` | Left to Right |
| 2 | Unary Operators | `++x`, `--x`, `+`, `-`, `!`, `~`, `(type)`, `*ptr`, `&var`, `sizeof` | **Right to Left** |
| 3 | Multiplicative | `*`, `/`, `%` | Left to Right |
| 4 | Additive | `+`, `-` | Left to Right |
| 5 | Bitwise Shifts | `<<`, `>>` | Left to Right |
| 6 | Relational Inequality | `<`, `<=`, `>`, `>=` | Left to Right |
| 7 | Relational Equality | `==`, `!=` | Left to Right |
| 8 | Bitwise AND | `&` | Left to Right |
| 9 | Bitwise XOR | `^` | Left to Right |
| 10 | Bitwise OR | `|` | Left to Right |
| 11 | Logical AND | `&&` | Left to Right |
| 12 | Logical OR | `||` | Left to Right |
| 13 | Conditional Ternary | `? :` | **Right to Left** |
| 14 | Assignment Operators | `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `<<=`, `>>=`, `&=`, `^=`, `|=` | **Right to Left** |
| 15 (Lowest) | Comma Operator | `,` | Left to Right |

---
STEP-BY-STEP ARITHMETIC EVALUATION TRACE:
Consider evaluating the complex expression:
$$x = 5 + 3 \times 2 \ll 1 > 4 \ \&\& \ 8 \ | \ 2$$
1. Multiplication (`*`, Level 3): $3 \times 2 = 6$. Expression: $5 + 6 \ll 1 > 4 \ \&\& \ 8 \ | \ 2$.
2. Addition (`+`, Level 4): $5 + 6 = 11$. Expression: $11 \ll 1 > 4 \ \&\& \ 8 \ | \ 2$.
3. Bitwise Left Shift (`<<`, Level 5): $11 \ll 1 = 11 \times 2 = 22$. Expression: $22 > 4 \ \&\& \ 8 \ | \ 2$.
4. Relational (`>`, Level 6): $22 > 4 \implies 1$. Expression: $1 \ \&\& \ 8 \ | \ 2$.
5. Bitwise OR (`|`, Level 10) vs Logical AND (`&&`, Level 11): Precedence of Bitwise OR (Level 10) is higher than Logical AND (Level 11). Thus $8 \ | \ 2 = 1000_2 \ | \ 0010_2 = 1010_2 = 10$.
6. Logical AND (`&&`, Level 11): $1 \ \&\& \ 10 \implies 1$ (both non-zero).
Final evaluated result: $\mathbf{x = 1}$.
"""
            },
            {
                "qid": "cprog-q4",
                "marks": 7,
                "type": "Descriptive",
                "title": "Formatted Input/Output in C: printf(), scanf(), Format Specifiers, Field Width, and Escape Sequences",
                "yt_query": "formatted input output in C printf scanf format specifiers field width",
                "img_path": "images/cprog/c_io_formatting.png",
                "img_caption": "Figure 1.4: Format Specifier Anatomy for printf() and scanf() with Precision and Width Flags",
                "answer": r"""
In C, standard input and output operations are not built-in language keywords; they are implemented as standardized runtime library functions defined in the header `<stdio.h>`.

1. Formatted Output Function: `printf()`:
The `printf()` function writes formatted text and variable data to the standard output stream (`stdout`, normally the terminal console):
$$\text{int printf(const char *format, ...);}$$
It returns the total number of characters successfully written, or a negative value upon output error.

Syntax of a Format Specifier inside the Control String:
$$\%[\text{flags}][\text{width}][.\text{precision}][\text{length\_modifier}]\text{conversion\_specifier}$$
- Flags:
  - `-` (Minus): Left-justifies output within the designated field width (default is right-justified).
  - `+` (Plus): Forces a leading plus or minus sign for numeric values.
  - `0` (Zero): Pads the field width with leading zeros instead of spaces.
  - ` ` (Space): Inserts a leading blank space if no sign is written.
- Field Width: An integer constant defining the minimum number of print column positions reserved for the output. If the value has fewer characters, it is padded; if wider, it is never truncated.
- Precision (`.n`):
  - For floating-point (`%f`, `%e`): Specifies the exact number of digits printed after the decimal point (e.g., `%.2f` prints two decimal places).
  - For strings (`%s`): Specifies the maximum number of characters to display from the string.
  - For integers (`%d`): Specifies the minimum number of digits to print (padded with leading zeros).

2. Formatted Input Function: `scanf()`:
The `scanf()` function reads formatted character sequences from the standard input stream (`stdin`, the keyboard) and converts them into binary representation, storing them into memory variables:
$$\text{int scanf(const char *format, ...);}$$
Crucial Syntax Rule: `scanf()` requires the physical memory addresses of variables. The address-of operator (`&`) must precede scalar variable names:
```c
int age;
float gpa;
scanf("%d %f", &age, &gpa); /* & is mandatory for scalar types */
```
Note: For character array strings (`char name[50];`), the array name `name` decays automatically into the base address of the array, so `&name` is not required: `scanf("%s", name);`.

3. Common Format Specifiers:
| Specifier | Argument Type | Data Format |
|---|---|---|
| `%d` / `%i` | `int` | Signed decimal integer |
| `%u` | `unsigned int` | Unsigned decimal integer |
| `%f` | `float` | Fractional decimal notation (`[-]ddd.ddd`) |
| `%lf` | `double` | Double-precision floating-point |
| `%e` / `%E` | `float` / `double` | Scientific exponential notation (`[-]d.ddde+dd`) |
| `%c` | `char` | Single character |
| `%s` | `char *` | String of non-whitespace characters |
| `%x` / `%X` | `unsigned int` | Hexadecimal integer (lowercase / uppercase) |
| `%o` | `unsigned int` | Octal integer |
| `%p` | `void *` | Pointer memory address in hexadecimal |

4. Escape Sequences:
Non-printing or control characters preceded by a backslash (`\`):
- `\n`: Newline (moves cursor to the beginning of the next line).
- `\t`: Horizontal tab (advances cursor to the next tab stop).
- `\b`: Backspace.
- `\\`: Prints a literal backslash.
- `\"`: Prints a literal double-quote inside a string literal.
- `%%`: Prints a literal percent sign (`%`).

5. Buffer Handling in C I/O:
When reading characters with `%c` immediately following numeric inputs (`%d`), trailing newline characters (`\n`) remaining unconsumed in the `stdin` keyboard buffer can be erroneously read as a valid character. This is prevented by including a leading whitespace in the format string: `scanf(" %c", &char_var);`, which instructs `scanf` to discard all leading whitespace and newline characters.
"""
            },
            {
                "qid": "cprog-q5",
                "marks": 7,
                "type": "Descriptive",
                "title": "Control Structures in C: Decision-Making (if-else, switch-case) and Looping Constructs (while, do-while, for)",
                "yt_query": "control structures in C if else switch case while do while for loop break continue",
                "img_path": "images/cprog/c_control_flow.png",
                "img_caption": "Figure 1.5: Flowcharts of if-else, switch-case, for-loop, and while vs do-while Loops",
                "answer": r"""
Control structures determine the flow of program execution, transforming linear sequential code into dynamic branching and iterative logic.

1. Decision-Making Structures:
- The `if-else` Construct:
Evaluates a boolean conditional test. If the condition is non-zero (true), the `if` block executes; otherwise, the `else` block executes:
```c
if (marks >= 90) {
    grade = 'S';
} else if (marks >= 80) {
    grade = 'A';
} else if (marks >= 70) {
    grade = 'B';
} else {
    grade = 'F';
}
```
The Dangling Else Problem: When nested `if` statements are written without explicit curly braces `{ }`, an `else` clause is syntactically matched by the compiler to the closest preceding unmatched `if`. Always use explicit braces to eliminate ambiguity.

- The `switch-case` Multi-way Branching Statement:
Tests an integral expression against a list of constant integer or character case labels:
```c
switch (operator_choice) {
    case '+':
        result = a + b;
        break; /* Essential to prevent fall-through */
    case '-':
        result = a - b;
        break;
    case '*':
        result = a * b;
        break;
    case '/':
        if (b != 0) result = a / b;
        break;
    default:
        printf("Invalid operational choice!\n");
        break;
}
```
Rules of `switch`:
1. The controlling switch expression must strictly evaluate to an integer or character type (floating-point expressions are illegal).
2. Case values must be compile-time constants or literals; variables are forbidden.
3. Fall-Through Phenomenon: If a `break` statement is omitted at the end of a case block, execution falls through unconditionally into all subsequent case statements until a `break` or closing brace is encountered.

2. Looping (Iterative) Constructs:
- `while` Loop (Pre-tested Loop):
Evaluates the condition prior to entering the loop body. If the condition is initially false, the loop body executes zero times:
$$\text{while (condition) } \{ \text{body; update;} \}$$
- `do-while` Loop (Post-tested Loop):
Executes the loop body first, then evaluates the test condition at the bottom. The loop body is guaranteed to execute at least once regardless of the condition:
$$\text{do } \{ \text{body; update;} \} \text{ while (condition);}$$
- `for` Loop (Deterministic Counter Loop):
Combines initialization, condition testing, and iteration updates into a compact header:
$$\text{for (initialization; condition; increment/decrement) } \{ \text{body;} \}$$

3. Jump Statements: `break` vs `continue`:
- `break`: Causes immediate premature termination of the innermost enclosing `switch`, `for`, `while`, or `do-while` loop, transferring control to the statement immediately following the loop.
- `continue`: Skips the remaining statements in the current iteration of the loop body and jumps immediately to the next iteration (in a `for` loop, jumps to the increment step).

---
PRODUCTION-GRADE C PROGRAM: MENU-DRIVEN PRIME AND FACTORIAL CALCULATOR
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int choice, num, i, is_prime;
    unsigned long long fact;

    while (1) {
        printf("\n=====================================\n");
        printf("   ENGINEERING COMPUTATION MENU       \n");
        printf("=====================================\n");
        printf("1. Check Prime Number\n");
        printf("2. Compute Factorial\n");
        printf("3. Exit Program\n");
        printf("Enter your choice (1-3): ");
        if (scanf("%d", &choice) != 1) {
            printf("Invalid input! Exiting.\n");
            break;
        }

        if (choice == 3) {
            printf("Terminating program. Goodbye!\n");
            break; /* Exit infinite while loop */
        }

        switch (choice) {
            case 1:
                printf("Enter a positive integer: ");
                scanf("%d", &num);
                if (num <= 1) {
                    printf("%d is NOT a prime number.\n", num);
                } else {
                    is_prime = 1; /* Assume prime */
                    for (i = 2; i * i <= num; i++) {
                        if (num % i == 0) {
                            is_prime = 0; /* Factor found */
                            break;
                        }
                    }
                    if (is_prime)
                        printf("Result: %d is a PRIME number.\n", num);
                    else
                        printf("Result: %d is a COMPOSITE number.\n", num);
                }
                break;

            case 2:
                printf("Enter a non-negative integer (0-20): ");
                scanf("%d", &num);
                if (num < 0 || num > 20) {
                    printf("Error: Input out of range for 64-bit integer!\n");
                    continue; /* Return to menu */
                }
                fact = 1ULL;
                for (i = 1; i <= num; i++) {
                    fact *= (unsigned long long)i;
                }
                printf("Result: %d! = %llu\n", num, fact);
                break;

            default:
                printf("Error: Invalid choice! Please select 1, 2, or 3.\n");
                break;
        }
    }
    return 0;
}
```
"""
            }
        ]
    },
    {
        "module_id": "cprog-m2",
        "module_num": "Module 2",
        "module_title": "Arrays and Strings",
        "questions": [
            {
                "qid": "cprog-q6",
                "marks": 7,
                "type": "Descriptive",
                "title": "One-Dimensional Arrays: Memory Layout, Linear Search, and Binary Search Algorithms with Step-by-Step Traces",
                "yt_query": "one dimensional arrays memory layout linear search binary search in C",
                "img_path": "images/cprog/1d_array_binary_search.png",
                "img_caption": "Figure 2.1: Contiguous Memory Layout of 1D Array and Divide-and-Conquer Binary Search Tree",
                "answer": r"""
A one-dimensional array is a derived data structure representing a fixed-size, sequenced collection of homogeneous elements stored in contiguous memory locations under a single identifier name.

1. Array Declaration and Memory Allocation:
Syntax: `data_type array_name[array_size];`
Example: `int arr[5] = {10, 20, 30, 40, 50};`
- Contiguous Memory Allocation: If `arr` is stored starting at base address `0x1000`, and an `int` occupies $4\text{ bytes}$, the elements reside at:
$$Loc(arr[0]) = 0x1000, \quad Loc(arr[1]) = 0x1004, \quad Loc(arr[2]) = 0x1008, \quad Loc(arr[3]) = 0x100C, \quad Loc(arr[4]) = 0x1010$$
General Address Formula for 1D Array element at index $i$:
$$\mathbf{Loc(arr[i]) = \text{Base Address} + (i \times \text{sizeof(data\_type)})}$$
- Zero-Based Indexing: In C, array indices range strictly from $0$ to $(N - 1)$.
- Lack of Bounds Checking: C does not perform runtime array boundary checking. Accessing `arr[10]` in an array of size 5 results in Undefined Behavior (accessing unallocated memory, potential segmentation fault, or data corruption).

2. Searching Algorithms:
- Linear Search:
Sequentially checks every element from index $0$ to $N-1$ until the target key is located. Time Complexity: Best Case $O(1)$, Worst and Average Case $O(N)$. Can operate on unsorted arrays.
- Binary Search:
A highly efficient search algorithm operating strictly on Sorted Arrays using the Divide-and-Conquer strategy.
Algorithm:
1. Initialize pointers: $low = 0$, $high = N - 1$.
2. While $low \le high$:
   - Calculate midpoint: $mid = low + \frac{high - low}{2}$ (avoids integer overflow).
   - If $arr[mid] == key$: Element found at index $mid$.
   - If $arr[mid] < key$: Search target resides in right half; set $low = mid + 1$.
   - If $arr[mid] > key$: Search target resides in left half; set $high = mid - 1$.
3. If $low > high$, target does not exist in array.
Time Complexity: $O(\log_2 N)$ worst case; Space Complexity: $O(1)$ iterative.

---
PRODUCTION-GRADE C PROGRAM: BINARY SEARCH IMPLEMENTATION
```c
#include <stdio.h>

int binary_search(const int arr[], int size, int target) {
    int low = 0;
    int high = size - 1;
    int mid;

    while (low <= high) {
        mid = low + (high - low) / 2; /* Safe midpoint calculation */

        if (arr[mid] == target) {
            return mid; /* Key found, return index */
        } else if (arr[mid] < target) {
            low = mid + 1; /* Discard left half */
        } else {
            high = mid - 1; /* Discard right half */
        }
    }
    return -1; /* Key not found */
}

int main(void) {
    int sorted_data[] = {12, 24, 35, 47, 59, 68, 73, 84, 91, 99};
    int n = sizeof(sorted_data) / sizeof(sorted_data[0]);
    int key = 73;
    int result_index;

    result_index = binary_search(sorted_data, n, key);

    if (result_index != -1) {
        printf("Search Successful! Key %d located at index %d (Address: %p)\n",
               key, result_index, (void*)&sorted_data[result_index]);
    } else {
        printf("Search Failed! Key %d not present in array.\n", key);
    }
    return 0;
}
```
"""
            },
            {
                "qid": "cprog-q7",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Two-Dimensional Arrays: Row-Major Address Derivation and Matrix Multiplication C Program",
                "yt_query": "two dimensional arrays row major address calculation matrix multiplication C program",
                "img_path": "images/cprog/2d_array_matrix_mult.png",
                "img_caption": "Figure 2.2: Row-Major Memory Mapping of 2D Matrix and Triple-Nested Multiplication Loops",
                "answer": r"""
A two-dimensional array in C represents a tabular collection of homogeneous data elements organized into rows and columns. While conceptualized as a grid, physical computer memory is strictly linear.

1. Mathematical Derivation of Row-Major Address Mapping:
C stores multidimensional arrays in Row-Major Order (elements of Row 0 are stored consecutively, followed by elements of Row 1, Row 2, etc.).
Consider a 2D array declared as: `T arr[M][N];` where $M$ is the number of rows, $N$ is the number of columns, and $S = \text{sizeof}(T)$ is the element storage size in bytes.
To locate the physical memory address of element $arr[i][j]$:
1. To reach Row $i$, exactly $i$ complete rows (from Row 0 to Row $i-1$) must be traversed.
2. Each complete row contains exactly $N$ elements. Thus, total elements in preceding rows = $i \times N$.
3. Within Row $i$, exactly $j$ elements precede $arr[i][j]$ (from Column 0 to Column $j-1$).
4. Total elements preceding $arr[i][j]$ is $(i \times N + j)$.
5. Multiplying by element size $S$ and adding the base address ($BA = \&arr[0][0]$) yields the exact formula:
$$\mathbf{Loc(arr[i][j]) = \text{Base Address} + \left[ (i \times N) + j \right] \times S}$$

Column-Major Order (used in FORTRAN and MATLAB):
$$\mathbf{Loc_{col}(arr[i][j]) = \text{Base Address} + \left[ (j \times M) + i \right] \times S}$$

2. Matrix Multiplication Compatibility and Algorithm:
Let Matrix $A$ have dimensions $p \times q$ and Matrix $B$ have dimensions $q \times r$.
- Dimensional Compatibility Rule: Matrix multiplication $C = A \times B$ is mathematically valid if and only if the number of columns in Matrix $A$ equals the number of rows in Matrix $B$ ($Columns_A = Rows_B = q$).
- The resultant Matrix $C$ will have dimensions $p \times r$.
- Mathematical Definition:
$$C_{ij} = \sum_{k=0}^{q-1} A_{ik} \cdot B_{kj} \quad (\text{for } 0 \le i < p, \ 0 \le j < r)$$
Computational Complexity: Three nested loops yielding time complexity $O(p \cdot q \cdot r)$; for square matrices of size $n$, time complexity is $O(n^3)$.

---
PRODUCTION-GRADE C PROGRAM: MATRIX MULTIPLICATION
```c
#include <stdio.h>
#define MAX 10

void read_matrix(int mat[MAX][MAX], int rows, int cols) {
    int i, j;
    for (i = 0; i < rows; i++) {
        for (j = 0; j < cols; j++) {
            scanf("%d", &mat[i][j]);
        }
    }
}

void print_matrix(int mat[MAX][MAX], int rows, int cols) {
    int i, j;
    for (i = 0; i < rows; i++) {
        printf("  [ ");
        for (j = 0; j < cols; j++) {
            printf("%4d ", mat[i][j]);
        }
        printf("]\n");
    }
}

int main(void) {
    int A[MAX][MAX], B[MAX][MAX], C[MAX][MAX];
    int p, q, q2, r, i, j, k;

    printf("Enter dimensions of Matrix A (rows cols): ");
    scanf("%d %d", &p, &q);
    printf("Enter dimensions of Matrix B (rows cols): ");
    scanf("%d %d", &q2, &r);

    if (q != q2) {
        printf("Error: Matrix multiplication incompatible! Columns of A (%d) != Rows of B (%d)\n", q, q2);
        return 1;
    }

    printf("Enter elements of Matrix A (%d x %d):\n", p, q);
    read_matrix(A, p, q);

    printf("Enter elements of Matrix B (%d x %d):\n", q, r);
    read_matrix(B, q, r);

    /* Matrix Multiplication Computation */
    for (i = 0; i < p; i++) {
        for (j = 0; j < r; j++) {
            C[i][j] = 0; /* Initialize accumulator */
            for (k = 0; k < q; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    printf("\nResultant Product Matrix C (%d x %d):\n", p, r);
    print_matrix(C, p, r);

    return 0;
}
```
"""
            },
            {
                "qid": "cprog-q8",
                "marks": 7,
                "type": "Descriptive",
                "title": "Strings in C: Null-Terminated Character Arrays, String Literals vs Character Arrays, and String I/O",
                "yt_query": "strings in C null terminated character array string literal vs array gets fgets",
                "img_path": "images/cprog/c_string_memory_representation.png",
                "img_caption": "Figure 2.3: Null-Byte Termination in Memory and Stack vs Read-Only Text Segment Allocation",
                "answer": r"""
In C, a string is not an intrinsic primitive data type; it is fundamentally defined as a contiguous sequence of characters stored in a 1D character array, terminated by an invisible Null Character (`\0`, ASCII value 0).

1. The Null Character (`\0`) Significance:
Because C character arrays do not record dynamic length in a header block, string processing functions (`printf`, `strlen`, `strcpy`) traverse contiguous bytes sequentially until they encounter `\0`.
Example:
```c
char greeting[] = "HELLO";
```
In physical memory, the compiler allocates 6 bytes:
$$\text{Indices: } [0]='H', \ [1]='E', \ [2]='L', \ [3]='L', \ [4]='O', \ [5]='\0'$$
Omitting the null byte causes string functions to continue reading past array boundaries, resulting in garbage character output or memory access violations.

2. Character Arrays vs String Literals:
- Character Array: `char str[] = "KTU";`
  - Memory Segment: Allocated on the local Runtime Stack frame.
  - Mutability: Fully Mutable (read-write). Individual characters can be modified: `str[0] = 'k';` is valid and safe.
- String Literal via Pointer: `char *ptr = "KTU";`
  - Memory Segment: The string constant `"KTU"` is stored in the Read-Only Data (Text) Segment. The pointer variable `ptr` resides on the stack, holding the address of this read-only memory.
  - Mutability: Immutable (Read-Only). Attempting to modify `*ptr = 'k';` results in a fatal Segmentation Fault (bus error) generated by the memory management unit (MMU).

3. String Input/Output Mechanisms:
- Reading with `scanf("%s", str)`: Reads a sequence of characters until whitespace (space, tab, newline) is encountered. It cannot read multi-word strings like `"Engineering College"`. It also suffers from buffer overflow vulnerabilities because it does not enforce array size boundaries.
- Reading with `gets(str)`: Deprecated in C99 and permanently removed in C11. `gets()` continues reading until a newline without checking array capacity, representing a severe security vulnerability (stack smashing buffer overflow exploits).
- Safe String Reading with `fgets(str, sizeof(str), stdin)`: The secure industry standard. Reads up to `sizeof(str) - 1` characters from the stream, automatically appends `\0`, and retains the trailing newline `\n` if room permits.
Example of newline stripping:
```c
char buffer[100];
if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
    buffer[strcspn(buffer, "\n")] = '\0'; /* Strip trailing newline */
}
```
- Output with `puts(str)`: Writes the string to `stdout` and automatically appends a trailing newline `\n`.
"""
            },
            {
                "qid": "cprog-q9",
                "marks": 7,
                "type": "Descriptive",
                "title": "Standard String Handling Functions in <string.h> and Manual Implementations Without Library Functions",
                "yt_query": "string h functions strlen strcpy strcat strcmp manual implementation in C",
                "img_path": "images/cprog/c_string_functions_pointers.png",
                "img_caption": "Figure 2.4: Pointer Traversal for Manual Implementations of strlen, strcpy, strcat, and strcmp",
                "answer": r"""
The standard C library header `<string.h>` provides an extensive suite of string manipulation functions. In university examinations, demonstrating how these routines operate under the hood using pointers and loops without library functions is a core requirement.

1. Standard Library Functions Overview:
- `size_t strlen(const char *s)`: Returns the number of characters in string `s`, excluding the terminating null byte `\0`.
- `char *strcpy(char *dest, const char *src)`: Copies the string `src` (including `\0`) into destination buffer `dest`. `dest` must be large enough to hold `src`.
- `char *strcat(char *dest, const char *src)`: Appends a copy of `src` to the end of `dest`, overwriting the initial `\0` of `dest`, and appends a terminating `\0`.
- `int strcmp(const char *s1, const char *s2)`: Lexicographically compares two strings character-by-character:
  - Returns `0` if $s1 == s2$,
  - Returns a positive value ($> 0$) if the first differing character in $s1$ has a higher ASCII value than $s2$,
  - Returns a negative value ($< 0$) if $s1 < s2$.

---
PRODUCTION-GRADE C PROGRAM: MANUAL IMPLEMENTATION OF STRING FUNCTIONS
```c
#include <stdio.h>

/* Manual strlen: Counts characters until null byte */
size_t my_strlen(const char *s) {
    size_t length = 0;
    while (*s != '\0') {
        length++;
        s++; /* Advance pointer */
    }
    return length;
}

/* Manual strcpy: Copies characters including null byte */
char* my_strcpy(char *dest, const char *src) {
    char *orig_dest = dest;
    while (*src != '\0') {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0'; /* Append null terminator */
    return orig_dest;
}

/* Manual strcat: Advances to end of dest, then appends src */
char* my_strcat(char *dest, const char *src) {
    char *orig_dest = dest;
    /* Advance to end of dest string */
    while (*dest != '\0') {
        dest++;
    }
    /* Copy src onto end of dest */
    while (*src != '\0') {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';
    return orig_dest;
}

/* Manual strcmp: Compares ASCII differences */
int my_strcmp(const char *s1, const char *s2) {
    while (*s1 != '\0' && *s1 == *s2) {
        s1++;
        s2++;
    }
    return (int)((unsigned char)*s1 - (unsigned char)*s2);
}

int main(void) {
    char str1[100] = "Kerala";
    char str2[50] = " Technological University";
    char str3[100];

    printf("Original str1: \"%s\", Length: %zu\n", str1, my_strlen(str1));

    my_strcpy(str3, str1);
    printf("Copied str3: \"%s\"\n", str3);

    my_strcat(str1, str2);
    printf("Concatenated str1: \"%s\"\n", str1);

    int cmp = my_strcmp("Apple", "Banana");
    printf("my_strcmp(\"Apple\", \"Banana\") = %d (Negative -> Apple < Banana)\n", cmp);

    return 0;
}
```
"""
            },
            {
                "qid": "cprog-q10",
                "marks": 7,
                "type": "Descriptive",
                "title": "Two-Dimensional Character Arrays (Array of Strings) and Alphabetical Sorting Program",
                "yt_query": "array of strings in C 2D character array alphabetical sorting bubble sort",
                "img_path": "images/cprog/array_of_strings_sorting.png",
                "img_caption": "Figure 2.5: 2D Character Array Memory Representation and In-Place Alphabetical Bubble Sorting",
                "answer": r"""
An array of strings in C is declared as a two-dimensional character array where the first dimension denotes the number of strings, and the second dimension represents the maximum allocated length (including `\0`) for each individual string.

1. Declaration and Memory Layout:
```c
char names[5][20]; /* Allocates storage for 5 distinct strings, each up to 19 characters + '\0' */
```
Total allocated memory is $5 \times 20 = 100\text{ bytes}$ of contiguous memory.
Each row `names[i]` represents a distinct 1D character array string acting as a pointer to the first character of that row (`&names[i][0]`).

2. Alphabetical String Sorting Algorithm:
Sorting strings alphabetically utilizes Bubble Sort or Selection Sort, using `strcmp()` to compare adjacent strings lexicographically and `strcpy()` paired with a temporary string buffer to swap strings when out of order.

---
PRODUCTION-GRADE C PROGRAM: SORTING STRINGS ALPHABETICALLY
```c
#include <stdio.h>
#include <string.h>

#define MAX_STRINGS 10
#define MAX_LEN 50

void sort_strings(char arr[][MAX_LEN], int n) {
    int i, j;
    char temp[MAX_LEN];

    /* Bubble Sort on Array of Strings */
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - 1 - i; j++) {
            /* If current string is lexicographically greater than next string */
            if (strcmp(arr[j], arr[j + 1]) > 0) {
                /* Swap strings arr[j] and arr[j + 1] using temporary buffer */
                strcpy(temp, arr[j]);
                strcpy(arr[j], arr[j + 1]);
                strcpy(arr[j + 1], temp);
            }
        }
    }
}

int main(void) {
    char student_names[MAX_STRINGS][MAX_LEN] = {
        "Rahul", "Ananya", "Gokul", "Fathima", "Deepak"
    };
    int n = 5;
    int i;

    printf("Original List of Names:\n");
    for (i = 0; i < n; i++) {
        printf("  [%d]: %s\n", i + 1, student_names[i]);
    }

    sort_strings(student_names, n);

    printf("\nAlphabetically Sorted List of Names:\n");
    for (i = 0; i < n; i++) {
        printf("  [%d]: %s\n", i + 1, student_names[i]);
    }

    return 0;
}
```
"""
            }
        ]
    },
    {
        "module_id": "cprog-m3",
        "module_num": "Module 3",
        "module_title": "Functions, Storage Classes & Pointers",
        "questions": [
            {
                "qid": "cprog-q11",
                "marks": 7,
                "type": "Descriptive",
                "title": "Modular Programming, Function Prototypes, Call by Value vs Call by Reference with Memory Stack Diagrams",
                "yt_query": "modular programming function prototype call by value vs call by reference C pointers",
                "img_path": "images/cprog/call_by_value_vs_reference.png",
                "img_caption": "Figure 3.1: Activation Stack Frames for Call by Value vs Call by Reference (Swapping Mechanism)",
                "answer": r"""
Modular programming divides a complex software problem into smaller, independent, reusable functional blocks called functions. In C, functions enforce encapsulation, reduce code redundancy, and facilitate debugging.

1. Function Anatomy:
- Function Prototype / Declaration: Informs the compiler in advance about the function's name, return type, and argument parameter types before its physical invocation:
$$\text{return\_type function\_name(parameter\_type1, parameter\_type2, ...);}$$
- Function Definition: Contains the actual executable body:
$$\text{return\_type function\_name(type1 param1, type2 param2) } \{ \text{/* statements; */} \}$$

2. Parameter Passing Mechanisms:
- Call by Value:
The actual values of arguments in the caller function are evaluated and copied into independent, separate local storage locations allocated on the callee function's activation stack frame.
Any modifications performed on these formal parameters inside the function affect only the local copies and have zero impact on the caller's original actual arguments.
- Call by Reference (Simulated via Pointers):
Instead of copying variable values, the caller passes the physical memory addresses (`&var`) of the actual arguments to pointer parameters (`type *ptr`).
The function dereferences these pointers (`*ptr`) to modify the caller's original memory directly.

---
PRODUCTION-GRADE C PROGRAM: COMPARING CALL BY VALUE VS CALL BY REFERENCE
```c
#include <stdio.h>

/* Call by Value: Fails to swap actual arguments in caller */
void swap_by_value(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    printf("  [Inside swap_by_value] a = %d, b = %d\n", a, b);
}

/* Call by Reference: Successfully swaps actual arguments via pointer dereferencing */
void swap_by_reference(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
    printf("  [Inside swap_by_reference] *a = %d, *b = %d\n", *a, *b);
}

int main(void) {
    int x = 10, y = 20;

    printf("Initial Values: x = %d, y = %d\n\n", x, y);

    printf("Attempting Call by Value:\n");
    swap_by_value(x, y);
    printf("After swap_by_value: x = %d, y = %d (Unchanged!)\n\n", x, y);

    printf("Attempting Call by Reference:\n");
    swap_by_reference(&x, &y); /* Pass memory addresses */
    printf("After swap_by_reference: x = %d, y = %d (Successfully Swapped!)\n", x, y);

    return 0;
}
```
"""
            },
            {
                "qid": "cprog-q12",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Recursion in C: Base Condition, Call Stack Execution, Tower of Hanoi, and Fibonacci Series with Call Tree",
                "yt_query": "recursion in C base condition call stack tower of hanoi fibonacci call tree",
                "img_path": "images/cprog/recursion_tower_of_hanoi.png",
                "img_caption": "Figure 3.2: Recursive Activation Stack Tree for Tower of Hanoi (N=3 Disks) and Fibonacci Sequence",
                "answer": r"""
Recursion is a programming technique where a function calls itself directly or indirectly to solve a smaller subproblem of the same structural nature.

1. Foundational Architecture of Recursion:
Every properly designed recursive function requires two essential components:
1. Base Condition (Termination Anchor): The simplest, trivial case that returns a concrete result directly without generating further recursive calls. Omitting or corrupting the base condition leads to Infinite Recursion, resulting in a fatal Stack Overflow runtime crash as the process call stack exhausts its allocated memory boundary.
2. Recursive Step (Inductive Progression): Reduces the input problem size towards the base condition.

2. Tower of Hanoi Mathematical Formulation:
The Tower of Hanoi puzzle involves moving $N$ disks from Source Pole $A$ to Destination Pole $C$ using Auxiliary Pole $B$, adhering to two strict rules:
1. Only one disk can be moved at a time.
2. No larger disk may ever be placed on top of a smaller disk.

Recursive Mathematical Recurrence:
To move $N$ disks from $A$ to $C$ using $B$:
- Step 1: Recursively move the top $(N-1)$ disks from $A$ to $B$ using $C$ as auxiliary.
- Step 2: Move the largest $N$-th disk directly from $A$ to $C$.
- Step 3: Recursively move the $(N-1)$ disks from $B$ to $C$ using $A$ as auxiliary.
Recurrence relation for the total number of moves $T(n)$:
$$T(n) = 2 T(n-1) + 1, \quad T(1) = 1$$
Solving this recurrence:
$$T(n) = 2^n - 1$$
For $N = 3$ disks, total moves required = $2^3 - 1 = 7\text{ moves}$.
Time Complexity is exponential $O(2^n)$; Space Complexity is $O(n)$ due to call stack depth.

---
PRODUCTION-GRADE C PROGRAM: TOWER OF HANOI RECURSIVE SOLUTION
```c
#include <stdio.h>

void tower_of_hanoi(int n, char source, char destination, char auxiliary, int *move_count) {
    if (n == 1) {
        (*move_count)++;
        printf("Step %d: Move disk 1 from rod %c -> rod %c\n", *move_count, source, destination);
        return;
    }
    /* Move top n-1 disks from source to auxiliary using destination */
    tower_of_hanoi(n - 1, source, auxiliary, destination, move_count);

    /* Move the n-th largest disk from source to destination */
    (*move_count)++;
    printf("Step %d: Move disk %d from rod %c -> rod %c\n", *move_count, n, source, destination);

    /* Move n-1 disks from auxiliary to destination using source */
    tower_of_hanoi(n - 1, auxiliary, destination, source, move_count);
}

int main(void) {
    int disks = 3;
    int moves = 0;

    printf("Tower of Hanoi Solution for %d disks:\n", disks);
    tower_of_hanoi(disks, 'A', 'C', 'B', &moves);
    printf("Total Moves Executed: %d (Expected: 2^%d - 1 = %d)\n", moves, disks, (1 << disks) - 1);

    return 0;
}
```
"""
            },
            {
                "qid": "cprog-q13",
                "marks": 7,
                "type": "Descriptive",
                "title": "Storage Classes in C: auto, register, static, and extern - Scope, Lifetime, and Memory Segments",
                "yt_query": "storage classes in C auto register static extern scope lifetime memory",
                "img_path": "images/cprog/c_storage_classes_memory.png",
                "img_caption": "Figure 3.3: Memory Segment Map (Data, BSS, Stack, Heap) of C Storage Classes",
                "answer": r"""
A Storage Class in C defines four fundamental operational properties of a variable:
1. Storage Location: The physical memory segment where the variable resides (Stack, Data Segment, BSS, or CPU registers).
2. Initial Default Value: The default contents if uninitialized by the programmer.
3. Scope: The visibility boundary within which the variable is accessible.
4. Lifetime / Longevity: The time interval during which the variable retains its allocated memory space during program execution.

Comprehensive Storage Classes Comparison:
| Storage Class | Keyword | Storage Area | Default Value | Scope | Lifetime |
|---|---|---|---|---|---|
| Automatic | `auto` | Runtime Stack | Garbage (Indeterminate) | Local (Block) | Function / Block duration |
| Register | `register` | CPU Register / Stack | Garbage (Indeterminate) | Local (Block) | Function / Block duration |
| Static | `static` | Data Segment / BSS | Zero (`0` or `NULL`) | Local or File | Entire program execution |
| External | `extern` | Data Segment / BSS | Zero (`0` or `NULL`) | Global (Multi-file) | Entire program execution |

1. Detailed Operational Properties:
- `auto`: Default for all local variables declared inside a block or function. Memory is dynamically pushed onto the stack upon block entry and popped upon block exit.
- `register`: Requests the compiler to store the variable in a high-speed hardware CPU register rather than RAM to accelerate execution (e.g., loop counters).
  - Restriction: The address-of operator (`&`) cannot be applied to register variables because CPU registers do not possess memory bus addresses.
  - The compiler is free to ignore the register request if hardware registers are exhausted.
- `static`:
  - Static Local Variable: Retains its value across multiple invocations of the enclosing function. It is initialized exactly once at program startup in the Data Segment/BSS, preserving state throughout program life.
  - Static Global Variable / Function: Restricts visibility strictly to the current source translation unit file, enforcing file-level encapsulation and preventing symbol collisions in multi-file projects.
- `extern`: Declares a reference to a global variable or function physically defined in another compilation file or later in the same file. It does not allocate memory; it informs the linker that storage was allocated elsewhere.

---
PRODUCTION-GRADE C PROGRAM: DEMONSTRATING STATIC VS AUTOMATIC VARIABLES
```c
#include <stdio.h>

void counter_demonstration(void) {
    auto int auto_var = 1;     /* Re-created and initialized every call */
    static int static_var = 1; /* Initialized once at startup; preserves state */

    printf("auto_var = %d | static_var = %d\n", auto_var, static_var);

    auto_var++;
    static_var++;
}

int main(void) {
    printf("Call 1: "); counter_demonstration();
    printf("Call 2: "); counter_demonstration();
    printf("Call 3: "); counter_demonstration();
    return 0;
}
```
Output:
```
Call 1: auto_var = 1 | static_var = 1
Call 2: auto_var = 1 | static_var = 2
Call 3: auto_var = 1 | static_var = 3
```
"""
            },
            {
                "qid": "cprog-q14",
                "marks": 7,
                "type": "Descriptive",
                "title": "Pointers in C: Pointer Concepts, Arithmetic, Pointers and Arrays, Void Pointers, and Dangling Pointers",
                "yt_query": "pointers in C pointer arithmetic pointers and arrays void pointer dangling pointer",
                "img_path": "images/cprog/pointer_arithmetic_memory.png",
                "img_caption": "Figure 3.4: Scaling Factor in Pointer Arithmetic and Array-Pointer Equivalence",
                "answer": r"""
A pointer is a derived data type in C whose value is the physical memory address of another variable. Pointers provide direct hardware memory access, enable dynamic memory allocation, and allow high-performance data manipulation.

1. Pointer Operators and Syntax:
- Declaration: `int *ptr;` (declares `ptr` as a pointer to an integer).
- Address-of Operator (`&`): Returns the hexadecimal memory address of an operand: `ptr = &var;`.
- Indirection / Dereference Operator (`*`): Accesses the contents stored at the memory address pointed to: `*ptr = 50;`.

2. Pointer Arithmetic and Scaling Factor:
Pointer arithmetic operates differently from standard integer arithmetic; all operations automatically scale by the byte size of the underlying data type:
$$\mathbf{\text{New Address} = \text{Current Address} \pm (k \times \text{sizeof(data\_type)})}$$
- If `int *p = 0x1000;` on a 4-byte integer system, `p + 1` evaluates to $0x1000 + 1 \times 4 = 0x1004$.
- Permissible Pointer Operations:
  1. Adding an integer to a pointer (`ptr + k`),
  2. Subtracting an integer from a pointer (`ptr - k`),
  3. Subtracting two pointers of the same type: `ptr2 - ptr1` yields the number of elements between them ($ \frac{\text{Byte Difference}}{\text{sizeof(Type)}} $),
  4. Comparison (`<`, `>`, `==`, `!=`) within the same array allocation.
- Illegal Operations: Adding two pointers (`ptr1 + ptr2`), multiplying, or dividing pointers.

3. Array and Pointer Equivalence:
In C, the name of an array acts as a constant pointer to its first element:
$$arr \equiv \&arr[0]$$
Array subscript notation is syntactic sugar for pointer arithmetic:
$$\mathbf{arr[i] \equiv *(arr + i) \equiv *(i + arr) \equiv i[arr]}$$

4. Special Pointer Categories:
- NULL Pointer: A pointer explicitly assigned to point to nothing (defined as `(void *)0` in `<stddef.h>`), used to signify unassigned pointers or allocation failures.
- Void Pointer (`void *`): A generic pointer that can hold the address of any data type without type-specific scaling. It cannot be directly dereferenced without an explicit typecast: `*(int *)void_ptr`.
- Wild Pointer: An uninitialized pointer pointing to an arbitrary, random memory address, posing severe crash risks.
- Dangling Pointer: A pointer that points to a memory location that has been freed or deallocated (e.g., after calling `free(ptr)` or returning the address of a dead stack variable). Prevented by immediately setting `ptr = NULL;` after deallocation.

---
PRODUCTION-GRADE C PROGRAM: POINTER ARITHMETIC AND ARRAY TRAVERSAL
```c
#include <stdio.h>

int main(void) {
    int data[] = {10, 20, 30, 40, 50};
    int *ptr = data; /* Points to data[0] */
    int i;

    printf("Base Address of Array: %p\n", (void*)data);

    /* Accessing elements using pointer arithmetic */
    for (i = 0; i < 5; i++) {
        printf("Index %d: Address = %p | Value via *(ptr + %d) = %d\n",
               i, (void*)(ptr + i), i, *(ptr + i));
    }

    /* Pointer difference */
    int *p_start = &data[0];
    int *p_end = &data[4];
    printf("\nDistance (elements) between end and start: %td\n", p_end - p_start);

    return 0;
}
```
"""
            },
            {
                "qid": "cprog-q15",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Dynamic Memory Allocation in C: Memory Segments, malloc, calloc, realloc, free, and Memory Leaks",
                "yt_query": "dynamic memory allocation in C malloc calloc realloc free memory leak",
                "img_path": "images/cprog/c_dynamic_memory_heap.png",
                "img_caption": "Figure 3.5: Process Virtual Memory Layout and Heap Allocation via malloc, calloc, and realloc",
                "answer": r"""
Static memory allocation binds memory sizes at compile-time (e.g., fixed arrays), leading to either wasted memory or buffer overflows. Dynamic Memory Allocation (DMA) enables an application to request, resize, and release exact heap memory blocks at runtime under software control.

1. Process Virtual Memory Architecture:
A running C program's virtual address space is organized into five segments:
1. Text Segment (Code): Machine instructions (read-only).
2. Initialized Data Segment: Global and static variables initialized with non-zero values.
3. Uninitialized Data Segment (BSS - Block Started by Symbol): Global and static variables initialized to zero.
4. Heap Segment: Unbounded pool of dynamic memory managed by runtime allocation functions; grows upward toward higher addresses.
5. Stack Segment: Stores function call frames, local automatic variables, and return addresses; grows downward toward lower addresses.

2. Dynamic Allocation Functions in `<stdlib.h>`:
- `malloc()` (Memory Allocation):
Allocates a single contiguous block of memory of specified bytes from the heap:
$$\text{void* malloc(size\_t size);}$$
- Memory contents are uninitialized and contain arbitrary garbage values.
- Returns a generic `void *` pointer to the allocated block, or `NULL` if heap memory is exhausted.

- `calloc()` (Contiguous Allocation):
Allocates memory for an array of $n$ elements, each of size $s$ bytes:
$$\text{void* calloc(size\_t num, size\_t size);}$$
- Automatically clears and initializes every byte in the allocated block to zero (`0`).

- `realloc()` (Re-allocation):
Dynamically resizes an existing heap block previously allocated by `malloc` or `calloc`:
$$\text{void* realloc(void *ptr, size\_t new\_size);}$$
- If possible, expands the current block in place. If contiguous space is blocked, it allocates a new block elsewhere, copies existing data over, automatically frees the old block, and returns the new pointer.
- If `ptr` is `NULL`, behaves like `malloc(new_size)`.

- `free()`:
Deallocates heap memory back to the operating system's heap manager:
$$\text{void free(void *ptr);}$$
- Memory Leak: Failing to call `free()` on dynamically allocated memory before losing all pointer references causes Memory Leaks. Over time, leaks exhaust available system memory, crashing the application or OS.

---
PRODUCTION-GRADE C PROGRAM: DYNAMIC ARRAY CREATION, RESIZING, AND CLEANUP
```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int *scores = NULL;
    int initial_size = 3;
    int expanded_size = 5;
    int i;

    /* 1. Allocate initial array of 3 integers using calloc (zero-initialized) */
    scores = (int *)calloc(initial_size, sizeof(int));
    if (scores == NULL) {
        fprintf(stderr, "Error: Initial heap allocation failed!\n");
        return 1;
    }

    /* Populate initial elements */
    scores[0] = 85;
    scores[1] = 92;
    scores[2] = 78;

    printf("Initial Allocation (Size %d):\n", initial_size);
    for (i = 0; i < initial_size; i++) {
        printf("  scores[%d] = %d\n", i, scores[i]);
    }

    /* 2. Resize array to 5 integers using realloc */
    int *temp = (int *)realloc(scores, expanded_size * sizeof(int));
    if (temp == NULL) {
        fprintf(stderr, "Error: Reallocation failed! Freeing original block.\n");
        free(scores);
        return 1;
    }
    scores = temp; /* Safe reassignment */

    /* Populate newly added elements */
    scores[3] = 95;
    scores[4] = 88;

    printf("\nAfter Reallocation (Size %d):\n", expanded_size);
    for (i = 0; i < expanded_size; i++) {
        printf("  scores[%d] = %d\n", i, scores[i]);
    }

    /* 3. Deallocate memory to prevent memory leaks */
    free(scores);
    scores = NULL; /* Neutralize dangling pointer */
    printf("\nMemory successfully deallocated and pointer cleared.\n");

    return 0;
}
```
"""
            }
        ]
    },
    {
        "module_id": "cprog-m4",
        "module_num": "Module 4",
        "module_title": "Structures, Unions & Preprocessor Directives",
        "questions": [
            {
                "qid": "cprog-q16",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Structures in C: Definition, Dot Operator, Memory Allocation, and Structure Padding Derivation",
                "yt_query": "structures in C structure padding word alignment memory calculation sizeof",
                "img_path": "images/cprog/structure_padding_alignment.png",
                "img_caption": "Figure 4.1: Structure Padding and Word Alignment Diagram on 32-bit and 64-bit Systems",
                "answer": r"""
A structure in C is a user-defined heterogeneous composite data type that allows grouping of logically related data items of differing data types under a single identifier.

1. Structure Definition and Variable Declaration:
```c
struct Student {
    char name[30];
    int roll_no;
    float cgpa;
};
```
Variables can be declared along with the definition or separately:
```c
struct Student s1 = {"Arun Kumar", 101, 8.75f};
```
Accessing Members: The Direct Member Operator (Dot Operator `.`) accesses fields:
`s1.roll_no = 102;`

2. Memory Allocation and Structure Padding:
The total memory allocated for a structure is often significantly larger than the simple arithmetic sum of the individual byte sizes of its members. This discrepancy is caused by Structure Padding and Hardware Word Alignment.
- CPU Word Alignment Rule:
Modern 32-bit and 64-bit microprocessors access computer memory across aligned word boundaries (e.g., 4-byte or 8-byte boundaries). If a multi-byte variable (like a 4-byte `int`) is located across an unaligned address boundary, the CPU must execute two separate memory read cycles paired with bit-shift operations, causing severe performance penalties.
To optimize bus access, the C compiler automatically inserts dummy uninitialized bytes (padding bytes) between structure members so that every member aligns with an address that is a multiple of its natural alignment requirement ($Align(T) = \text{sizeof}(T)$).

---
MATHEMATICAL DERIVATION OF STRUCTURE PADDING:
Consider the structure definition:
```c
struct PaddedExample {
    char a;    /* sizeof(char) = 1 byte */
    int b;     /* sizeof(int)  = 4 bytes */
    short c;   /* sizeof(short)= 2 bytes */
};
```
Arithmetic sum of member sizes: $1 + 4 + 2 = 7\text{ bytes}$.
Actual Compiler Allocation Trace (on 32/64-bit architecture):
1. Member `a` (char) is placed at relative offset `0x00` ($1\text{ byte}$).
2. Member `b` (int) requires a 4-byte aligned address (an offset divisible by 4). The next available offset `0x01` is not divisible by 4.
   - The compiler inserts 3 padding bytes at offsets `0x01, 0x02, 0x03`.
   - Member `b` is placed at offset `0x04` spanning bytes `0x04` to `0x07` ($4\text{ bytes}$).
3. Member `c` (short) requires 2-byte alignment. Offset `0x08` is divisible by 2.
   - Member `c` is placed at offset `0x08` spanning bytes `0x08` to `0x09` ($2\text{ bytes}$). Total size accumulated so far = $10\text{ bytes}$.
4. Tail Padding Rule: The total size of the entire structure must be an integer multiple of the largest member's alignment requirement ($\max(1, 4, 2) = 4\text{ bytes}$).
   - The current size $10$ is not divisible by 4. The compiler appends 2 trailing padding bytes at offsets `0x0A, 0x0B`.
   - Final Total Structure Size: $10 + 2 = 12\text{ bytes}$!
$$\mathbf{\text{sizeof(struct PaddedExample)} = 12\text{ bytes}}$$

Optimizing Structure Size via Member Reordering:
By reordering structure members from largest to smallest alignment:
```c
struct OptimizedExample {
    int b;     /* 4 bytes (offset 0-3) */
    short c;   /* 2 bytes (offset 4-5) */
    char a;    /* 1 byte  (offset 6) */
    /* 1 trailing padding byte (offset 7) */
}; /* Total Size = 8 bytes! */
```
Reordering saves $33.3\%$ of memory per structure instance!
To eliminate padding entirely in embedded systems, use `#pragma pack(1)` or `__attribute__((packed))`.
"""
            },
            {
                "qid": "cprog-q17",
                "marks": 7,
                "type": "Descriptive",
                "title": "Array of Structures, Nested Structures, Structure Pointers, and Arrow Operator (->)",
                "yt_query": "array of structures nested structures arrow operator structure pointers C",
                "img_path": "images/cprog/nested_structures_arrow.png",
                "img_caption": "Figure 4.2: Memory Mapping of Array of Structures and Pointer Dereference via Arrow Operator (->)",
                "answer": r"""
1. Array of Structures:
An array of structures represents a collection of multiple structure instances stored consecutively in memory, forming a database table where each array element is a row (record) and each structure member is a column (field).
Declaration: `struct Student batch[60];`

2. Nested Structures:
A structure containing another structure as one of its members. Enables hierarchical data modeling:
```c
struct Date {
    int day;
    int month;
    int year;
};

struct Employee {
    int emp_id;
    char name[40];
    struct Date joining_date; /* Nested structure */
};
```
Accessing nested fields: `emp1.joining_date.year = 2024;`

3. Structure Pointers and the Arrow Operator (`->`):
When passing structures to functions, passing large structures by value copies every single byte onto the call stack, causing memory and execution overhead. High-performance C programs pass structures by reference using Structure Pointers (`struct Student *ptr`).
The Arrow Operator (`->`, Member Selection through Pointer):
$$\mathbf{ptr\text{->}member \equiv (*ptr).member}$$
The arrow operator dereferences the structure pointer and accesses the member in a single concise operation. Note: Parentheses in `(*ptr).member` are mandatory because the dot operator (`.`) has higher precedence than the dereference operator (`*`).

---
PRODUCTION-GRADE C PROGRAM: STUDENT RECORD SYSTEM WITH STRUCTURE POINTERS
```c
#include <stdio.h>

struct Marks {
    float theory;
    float practical;
};

struct Student {
    int roll_no;
    char name[30];
    struct Marks score; /* Nested structure */
    float total;
};

/* Function accepting structure pointer via arrow operator */
void calculate_total(struct Student *s) {
    s->total = s->score.theory + s->score.practical;
}

void display_student(const struct Student *s) {
    printf("Roll No: %-4d | Name: %-15s | Theory: %5.1f | Practical: %5.1f | Total: %5.1f\n",
           s->roll_no, s->name, s->score.theory, s->score.practical, s->total);
}

int main(void) {
    struct Student class_records[3] = {
        {101, "Arya",    {82.5f, 18.0f}, 0.0f},
        {102, "Bilal",   {74.0f, 16.5f}, 0.0f},
        {103, "Chithra", {91.0f, 19.5f}, 0.0f}
    };
    int i;

    /* Process totals using structure pointers */
    for (i = 0; i < 3; i++) {
        calculate_total(&class_records[i]);
    }

    printf("==================== STUDENT ACADEMIC RECORDS ====================\n");
    for (i = 0; i < 3; i++) {
        display_student(&class_records[i]);
    }

    return 0;
}
```
"""
            },
            {
                "qid": "cprog-q18",
                "marks": 7,
                "type": "Descriptive",
                "title": "Self-Referential Structures and Linked Lists: Node Creation, Dynamic Insertion, and Traversal",
                "yt_query": "self referential structure in C linked list node creation traversal pointers",
                "img_path": "images/cprog/self_referential_linked_list.png",
                "img_caption": "Figure 4.3: Self-Referential Node Architecture and Singly Linked List Pointer Links",
                "answer": r"""
A Self-Referential Structure is a structure that contains one or more pointer members pointing to a structure of the identical type. They form the foundational building block for all dynamic data structures in computer science, including Linked Lists, Stacks, Queues, Binary Trees, and Graphs.

1. Definition of Self-Referential Node:
```c
struct Node {
    int data;               /* Payload data */
    struct Node *next;      /* Self-referential pointer to next node */
};
```
Notice that a structure cannot contain an actual instance of itself (`struct Node next;` is illegal because it would require infinite recursive memory allocation). However, a pointer to itself (`struct Node *next;`) is completely valid because pointer variables have a fixed, known size ($4\text{ bytes}$ or $8\text{ bytes}$).

2. Singly Linked List Operations:
Unlike static arrays (which have fixed capacity and require expensive element shifting during insertion/deletion), a linked list allocates nodes dynamically on the heap as needed, connected linearly through pointer links.
- Head Pointer: Holds the memory address of the first node in the list.
- Tail Node: The final node in the list whose `next` pointer is explicitly set to `NULL`.

---
PRODUCTION-GRADE C PROGRAM: CREATING, INSERTING, AND TRAVERSING A LINKED LIST
```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

/* Function to insert a new node at the beginning of the list */
void insert_at_head(struct Node **head_ref, int new_data) {
    /* 1. Allocate node memory on the heap */
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    if (new_node == NULL) {
        fprintf(stderr, "Heap allocation failed!\n");
        return;
    }

    /* 2. Put in the payload data */
    new_node->data = new_data;

    /* 3. Link old list to the new node */
    new_node->next = *head_ref;

    /* 4. Move head pointer to point to new node */
    *head_ref = new_node;
}

/* Function to print linked list nodes */
void print_list(const struct Node *node) {
    while (node != NULL) {
        printf("[%d] -> ", node->data);
        node = node->next; /* Move to next node */
    }
    printf("NULL\n");
}

/* Function to free all dynamically allocated nodes */
void free_list(struct Node *head) {
    struct Node *temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
}

int main(void) {
    struct Node *head = NULL; /* Empty linked list */

    insert_at_head(&head, 50);
    insert_at_head(&head, 40);
    insert_at_head(&head, 30);
    insert_at_head(&head, 20);
    insert_at_head(&head, 10);

    printf("Traversing Singly Linked List:\n");
    print_list(head);

    free_list(head);
    head = NULL;
    return 0;
}
```
"""
            },
            {
                "qid": "cprog-q19",
                "marks": 7,
                "type": "Descriptive",
                "title": "Unions vs Structures: Memory Sharing Mechanism, Size Calculation, and Bit-Fields",
                "yt_query": "unions vs structures in C memory sharing size of union bit fields",
                "img_path": "images/cprog/union_memory_sharing.png",
                "img_caption": "Figure 4.4: Overlapping Memory Architecture of Unions vs Discrete Allocation of Structures",
                "answer": r"""
While both structures and unions are user-defined composite data types in C, they differ fundamentally in how they allocate and manage computer memory.

1. Memory Sharing Mechanism:
- Structure (`struct`):
Every declared member is assigned its own distinct, unique memory storage location. All members coexist simultaneously. The total size of a structure is at least the sum of the sizes of all its members (plus padding).
- Union (`union`):
All declared members share the exact same physical memory location. Members overlay on top of one another starting at the same base address. Only one member can contain a valid value at any given instant. Writing to one member overwrites the data of all other members.
Size of a Union:
The total size allocated for a union equals the size of its largest member, rounded up to satisfy the strictest alignment requirement among its members:
$$\mathbf{\text{sizeof(union)} = \text{aligned}(\max\{\text{sizeof}(m_1), \text{sizeof}(m_2), \dots, \text{sizeof}(m_k)\})}$$

Comprehensive Comparison Table:
| Parameter | Structure (`struct`) | Union (`union`) |
|---|---|---|
| Keyword | `struct` | `union` |
| Memory Allocation | Separate memory for each member | Single shared memory block for all members |
| Member Coexistence | All members exist and can be used concurrently | Only one member can hold valid data at a time |
| Size | $\ge$ Sum of all member sizes (with padding) | Size of the largest member |
| Value Alteration | Modifying one member does not affect others | Modifying one member overwrites other members |
| Primary Purpose | Bundling multi-attribute records | Memory conservation and variant records |

2. Bit-Fields in Structures:
Standard data types occupy full byte multiples ($1, 2, 4\text{ bytes}$). In resource-constrained embedded systems (microcontrollers, network packet headers), storing small status flags (e.g., 1-bit boolean or 4-bit status codes) wastes memory. Bit-fields allow programmers to define exact bit widths for structure members:
```c
struct DeviceStatus {
    unsigned int power_on   : 1; /* 1 bit: 0 or 1 */
    unsigned int error_code : 3; /* 3 bits: 0 to 7 */
    unsigned int mode       : 2; /* 2 bits: 0 to 3 */
    unsigned int reserved   : 2; /* 2 bits padding */
}; /* Total Size = exactly 1 byte (8 bits)! */
```

---
PRODUCTION-GRADE C PROGRAM: UNION MEMORY SHARING DEMONSTRATION
```c
#include <stdio.h>

union DataPacket {
    int integer_val;    /* 4 bytes */
    float float_val;    /* 4 bytes */
    char str_val[20];   /* 20 bytes */
};

int main(void) {
    union DataPacket packet;

    printf("sizeof(union DataPacket) = %zu bytes (Size of largest member str_val[20])\n\n",
           sizeof(packet));

    /* Assigning to integer member */
    packet.integer_val = 1984;
    printf("packet.integer_val = %d\n", packet.integer_val);

    /* Assigning to float member overwrites integer memory */
    packet.float_val = 3.14159f;
    printf("packet.float_val   = %.5f\n", packet.float_val);
    printf("packet.integer_val = %d (Corrupted by float overwrite!)\n\n", packet.integer_val);

    return 0;
}
```
"""
            },
            {
                "qid": "cprog-q20",
                "marks": 7,
                "type": "Descriptive",
                "title": "typedef, Enumerations (enum), and Preprocessor Directives: Macros, Conditional Compilation, and File Inclusion",
                "yt_query": "typedef enum C preprocessor directives define macros conditional compilation",
                "img_path": "images/cprog/c_preprocessor_macros.png",
                "img_caption": "Figure 4.5: Preprocessor Phase Text Expansion and Conditional Compilation Logic",
                "answer": r"""
1. Type Definitions (`typedef`):
The `typedef` keyword creates a new, meaningful alias (synonym) for an existing data type. It improves code readability and portable abstraction:
```c
typedef unsigned long long uint64_t;
typedef struct Student StudentNode;
```
`typedef` vs `#define`:
- `typedef` is interpreted by the compiler, adhering to C variable scoping rules and type checking.
- `#define` is a brute-force textual search-and-replace performed by the preprocessor without type checking.

2. Enumerations (`enum`):
An enumeration is a user-defined type consisting of a set of named integer constants:
```c
enum Days { SUN, MON, TUE, WED, THU, FRI, SAT };
```
By default, the compiler assigns integer values starting from $0$ (`SUN = 0, MON = 1, ...`). Explicit initializers can reassign values:
`enum Status { ERROR = -1, SUCCESS = 0, PENDING = 1 };`

3. The C Preprocessor:
The preprocessor is a text-substitution tool that processes source code before actual compilation begins. Preprocessor commands start with `#` at the beginning of a line.
- Macro Substitution (`#define`):
  - Object-like Macros: `#define PI 3.14159265359`
  - Function-like Macros:
```c
#define SQUARE(x) ((x) * (x))
```
Crucial Defensive Syntax Rule: Enclose all macro arguments and the entire macro expression in parentheses to prevent operator precedence bugs (e.g., `SQUARE(2 + 3)` expands to `((2 + 3) * (2 + 3)) = 25`, whereas without parentheses `x * x` expands to `2 + 3 * 2 + 3 = 11`).

- File Inclusion (`#include`):
  - `#include <filename.h>`: Instructs preprocessor to search standard system compiler directories.
  - `#include "filename.h"`: Instructs preprocessor to search the current local project working directory first before falling back to system paths.

- Conditional Compilation Directives:
Enables selective compilation of code blocks based on specified conditions:
- `#ifdef MACRO` / `#ifndef MACRO`: Compiles if macro is defined / not defined.
- `#if`, `#elif`, `#else`, `#endif`: Evaluates compile-time integer constant expressions.
Header Guards: Essential pattern placed inside custom header files to prevent destructive multiple inclusion errors:
```c
#ifndef MY_HEADER_H
#define MY_HEADER_H
/* Declarations go here */
#endif
```

- Predefined Standard Macros:
`__FILE__` (current source filename string), `__LINE__` (current source line number integer), `__DATE__` (compilation date), `__TIME__` (compilation time).
"""
            }
        ]
    },
    {
        "module_id": "cprog-m5",
        "module_num": "Module 5",
        "module_title": "File Handling & Command Line Arguments",
        "questions": [
            {
                "qid": "cprog-q21",
                "marks": 7,
                "type": "Descriptive",
                "title": "File Handling Basics in C: FILE Pointer, fopen, fclose, File Access Modes, and Text vs Binary Files",
                "yt_query": "file handling in C FILE pointer fopen fclose modes text vs binary",
                "img_path": "images/cprog/c_file_handling_streams.png",
                "img_caption": "Figure 5.1: File Stream Architecture Linking C Application to Physical Disk File via FILE Structure",
                "answer": r"""
A file is a collection of related byte records stored persistently on secondary non-volatile storage media (HDD, SSD). In C, all input and output devices are treated as uniform abstract byte streams managed through the `FILE` structure defined in `<stdio.h>`.

1. The `FILE` Pointer:
The `FILE` structure contains OS-level metadata required to control a file stream: the file descriptor, current read/write byte offset position, stream error flags, and internal buffer pointers.
C applications interact with files exclusively through a pointer to this structure:
$$\text{FILE *fp;}$$

2. File Opening (`fopen`) and Closing (`fclose`):
- Opening a File:
$$\text{FILE *fopen(const char *filename, const char *mode);}$$
Attempts to open the specified file under the designated access mode. Returns a valid `FILE *` pointer upon success, or `NULL` if opening fails (e.g., file not found, permission denied).
Mandatory Defensive Check:
```c
FILE *fp = fopen("data.txt", "r");
if (fp == NULL) {
    perror("Error opening file");
    return 1;
}
```
- Closing a File:
$$\text{int fclose(FILE *stream);}$$
Flushes any unwritten data remaining in stream buffers to physical disk, frees OS kernel file locks, and deallocates the `FILE` control block. Returns `0` on success, or `EOF` on error.

3. Standard File Access Modes:
| Mode | Action if File Exists | Action if File Does Not Exist | File Position Pointer |
|---|---|---|---|
| `"r"` (Read) | Opens for reading | **Fails (returns NULL)** | Beginning of file |
| `"w"` (Write) | **Overwrites / Truncates to 0 bytes** | Creates new file | Beginning of file |
| `"a"` (Append) | Retains data; appends to end | Creates new file | End of file |
| `"r+"` (Read/Write) | Opens for reading and writing | Fails (returns NULL) | Beginning of file |
| `"w+"` (Write/Read) | Overwrites / Truncates to 0 bytes | Creates new file | Beginning of file |
| `"a+"` (Append/Read)| Retains data; reads anywhere, appends | Creates new file | End of file for writes |

4. Text Files vs Binary Files:
- Text Files (`.txt`, `.c`):
Data is stored as sequences of human-readable ASCII/UTF characters. Operating systems perform line-ending translations (e.g., in Windows, single newline `\n` is translated into two characters: Carriage Return + Line Feed `\r\n`).
- Binary Files (`.bin`, `.dat`):
Data is stored as raw binary image bytes exactly as represented in physical RAM (e.g., a 4-byte `int` is saved as 4 raw binary bytes). No line-ending character translation occurs. Binary modes are specified by appending `'b'` to the mode string (`"rb"`, `"wb"`, `"ab"`). Binary files are more compact and faster to process.
"""
            },
            {
                "qid": "cprog-q22",
                "marks": 7,
                "type": "Descriptive",
                "title": "Character, String, and Formatted File I/O: fgetc, fputc, fgets, fputs, fprintf, fscanf, and File Copy Program",
                "yt_query": "file I O in C fgetc fputc fgets fputs fprintf fscanf file copy program count lines",
                "img_path": "images/cprog/file_copy_char_count.png",
                "img_caption": "Figure 5.2: File Copy Pipeline with Character, Word, and Line Tracking",
                "answer": r"""
C provides three levels of text stream file I/O operations:

1. Character-Level File I/O:
- `int fgetc(FILE *stream);`: Reads the next character from the file stream and advances the file position pointer. Returns the character as an `unsigned char` cast to an `int`, or returns `EOF` (End of File, typically `-1`) when the end of the file is reached or an error occurs.
- `int fputc(int ch, FILE *stream);`: Writes a single character to the file stream.

2. Line / String-Level File I/O:
- `char *fgets(char *str, int n, FILE *stream);`: Reads up to $n-1$ characters into array `str` until a newline `\n` or EOF is encountered. Appends `\0`. Returns `str`, or `NULL` on EOF/error.
- `int fputs(const char *str, FILE *stream);`: Writes a null-terminated string to the stream (does not automatically append a newline).

3. Formatted File I/O:
- `int fprintf(FILE *stream, const char *format, ...);`: Writes formatted text to a file stream.
- `int fscanf(FILE *stream, const char *format, ...);`: Reads formatted data from a file stream.

---
PRODUCTION-GRADE C PROGRAM: FILE COPY WITH CHARACTER, WORD, AND LINE COUNTING
```c
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(void) {
    FILE *src_fp = NULL;
    FILE *dest_fp = NULL;
    int ch;
    long char_count = 0;
    long word_count = 0;
    long line_count = 0;
    int in_word = 0;

    /* Open source file in read mode */
    src_fp = fopen("source.txt", "r");
    if (src_fp == NULL) {
        perror("Error opening source.txt");
        return 1;
    }

    /* Open destination file in write mode */
    dest_fp = fopen("destination.txt", "w");
    if (dest_fp == NULL) {
        perror("Error creating destination.txt");
        fclose(src_fp);
        return 1;
    }

    /* Process character by character until EOF */
    while ((ch = fgetc(src_fp)) != EOF) {
        fputc(ch, dest_fp); /* Copy character to destination file */
        char_count++;

        if (ch == '\n') {
            line_count++;
        }

        if (isspace(ch)) {
            in_word = 0;
        } else if (!in_word) {
            in_word = 1;
            word_count++;
        }
    }

    fclose(src_fp);
    fclose(dest_fp);

    printf("File copy operation completed successfully!\n");
    printf("Statistics:\n");
    printf("  Total Characters Copied: %ld\n", char_count);
    printf("  Total Words Counted:    %ld\n", word_count);
    printf("  Total Lines Counted:    %ld\n", line_count);

    return 0;
}
```
"""
            },
            {
                "qid": "cprog-q23",
                "marks": 7,
                "type": "Descriptive",
                "title": "Block/Record I/O for Binary Files: fread(), fwrite(), and Employee Database Management Program",
                "yt_query": "binary file handling in C fread fwrite array of structures employee database",
                "img_path": "images/cprog/fread_fwrite_binary.png",
                "img_caption": "Figure 5.3: Direct Block-Level Transfer of Structure Records Between RAM and Binary Disk",
                "answer": r"""
When storing structured records (such as database rows or scientific arrays) on disk, converting data into human-readable text via `fprintf` incurs heavy CPU conversion overhead and increases storage volume. Block I/O functions (`fread` and `fwrite`) transfer raw memory blocks directly between RAM and disk files in binary format.

1. Function Prototypes:
- `fwrite()` (Write Block):
$$\text{size\_t fwrite(const void *ptr, size\_t size, size\_t count, FILE *stream);}$$
Writes `count` elements, each of size `size` bytes, from the memory buffer pointed to by `ptr` into the binary file stream. Returns the actual number of complete items successfully written.
- `fread()` (Read Block):
$$\text{size\_t fread(void *ptr, size\_t size, size\_t count, FILE *stream);}$$
Reads `count` elements, each of size `size` bytes, from the file stream into the memory buffer pointed to by `ptr`. Returns the actual number of complete items successfully read (which will be less than `count` when EOF is encountered).

---
PRODUCTION-GRADE C PROGRAM: EMPLOYEE DATABASE STORAGE USING FWRITE AND FREAD
```c
#include <stdio.h>
#include <stdlib.h>

struct Employee {
    int id;
    char name[32];
    double salary;
};

int main(void) {
    FILE *fp = NULL;
    struct Employee staff[3] = {
        {1001, "Dr. Anand", 95000.00},
        {1002, "Beena Nair", 82000.50},
        {1003, "Cyril Jose", 78500.00}
    };
    struct Employee read_staff[3];
    size_t written_records, read_records;
    int i;

    /* 1. Write structure records to binary file */
    fp = fopen("employees.dat", "wb");
    if (fp == NULL) {
        perror("Error opening employees.dat for writing");
        return 1;
    }

    written_records = fwrite(staff, sizeof(struct Employee), 3, fp);
    printf("Successfully wrote %zu records to binary file employees.dat\n", written_records);
    fclose(fp);

    /* 2. Read structure records back from binary file */
    fp = fopen("employees.dat", "rb");
    if (fp == NULL) {
        perror("Error opening employees.dat for reading");
        return 1;
    }

    read_records = fread(read_staff, sizeof(struct Employee), 3, fp);
    printf("Successfully read %zu records from employees.dat:\n", read_records);

    for (i = 0; i < (int)read_records; i++) {
        printf("  ID: %d | Name: %-12s | Salary: INR %.2f\n",
               read_staff[i].id, read_staff[i].name, read_staff[i].salary);
    }
    fclose(fp);

    return 0;
}
```
"""
            },
            {
                "qid": "cprog-q24",
                "marks": 7,
                "type": "Long Derivation",
                "title": "Random Access in Files: fseek(), ftell(), rewind(), Origin Positions, and File Size Calculation",
                "yt_query": "random access in files fseek ftell rewind SEEK_SET SEEK_CUR SEEK_END C program",
                "img_path": "images/cprog/fseek_random_access.png",
                "img_caption": "Figure 5.4: Random Access File Pointer Repositioning via SEEK_SET, SEEK_CUR, and SEEK_END",
                "answer": r"""
Sequential file access requires reading through all preceding bytes from the beginning to reach a target record. Random (Direct) Access enables an application to jump directly to any arbitrary byte location within a file, facilitating high-speed database queries and record updates.

1. Functions for Random Access:
- `fseek()`: Sets the file position indicator for the specified stream:
$$\text{int fseek(FILE *stream, long int offset, int whence);}$$
  - `offset`: Number of bytes to shift (positive moves forward, negative moves backward).
  - `whence`: Origin position reference constant defined in `<stdio.h>`:
    1. `SEEK_SET` ($0$): Offset relative to the **Beginning of the File**.
    2. `SEEK_CUR` ($1$): Offset relative to the **Current File Position Indicator**.
    3. `SEEK_END` ($2$): Offset relative to the **End of the File**.
  Returns `0` upon success, non-zero on error.

- `ftell()`: Returns the current byte offset position of the file indicator relative to the beginning of the file:
$$\text{long int ftell(FILE *stream);}$$
Returns `-1L` upon error.

- `rewind()`: Resets the file position indicator back to the very beginning of the file and clears stream error flags:
$$\text{void rewind(FILE *stream); \quad (\equiv fseek(stream, 0L, SEEK\_SET);)}$$

---
DETERMINING EXACT FILE SIZE USING FSEEK AND FTELL:
```c
fseek(fp, 0L, SEEK_END);      /* Jump to the very end of file */
long file_size = ftell(fp);   /* Read byte offset from start */
rewind(fp);                   /* Return to start for subsequent reads */
```

---
PRODUCTION-GRADE C PROGRAM: RANDOM ACCESS RECORD MODIFICATION
```c
#include <stdio.h>
#include <stdlib.h>

struct Account {
    int acc_no;
    double balance;
};

int main(void) {
    FILE *fp = NULL;
    struct Account acc;

    /* Create sample binary file with 3 accounts */
    fp = fopen("bank.dat", "wb+");
    if (fp == NULL) { perror("File open error"); return 1; }

    struct Account initial[3] = {{101, 5000.0}, {102, 12000.0}, {103, 7500.0}};
    fwrite(initial, sizeof(struct Account), 3, fp);

    /* Modify the 2nd record directly (Account 102, index 1) */
    int record_index = 1;
    long target_offset = record_index * sizeof(struct Account);

    fseek(fp, target_offset, SEEK_SET); /* Jump directly to Record 2 */
    fread(&acc, sizeof(struct Account), 1, fp);
    printf("Original Record 2: Acc No: %d, Balance: %.2f\n", acc.acc_no, acc.balance);

    acc.balance += 3000.0; /* Deposit funds */

    /* Move back to rewrite the modified record */
    fseek(fp, target_offset, SEEK_SET);
    fwrite(&acc, sizeof(struct Account), 1, fp);
    fflush(fp);

    /* Verify modification */
    fseek(fp, target_offset, SEEK_SET);
    fread(&acc, sizeof(struct Account), 1, fp);
    printf("Updated Record 2:  Acc No: %d, Balance: %.2f (Modified in place!)\n",
           acc.acc_no, acc.balance);

    fclose(fp);
    return 0;
}
```
"""
            },
            {
                "qid": "cprog-q25",
                "marks": 7,
                "type": "Descriptive",
                "title": "Error Handling in File Operations: feof(), ferror(), clearerr(), perror(), and strerror()",
                "yt_query": "error handling in file operations C feof ferror perror strerror",
                "img_path": "images/cprog/c_file_error_handling.png",
                "img_caption": "Figure 5.5: Error Handling Logic Distinguishing End-of-File from Disk Hardware Read Errors",
                "answer": r"""
Robust software engineering requires that file operations anticipate and gracefully handle unexpected runtime anomalies (e.g., missing files, read-only permissions, physical media failure, network drive disconnections, full disk space).

1. Standard Error Checking Functions:
- `feof(FILE *stream)`:
Tests the End-of-File indicator for the given stream.
Returns non-zero (true) if the EOF indicator is set.
Crucial Rule: `feof()` returns true **only after** an input operation has attempted to read past the end of the file. It cannot be used as a pre-loop condition (`while(!feof(fp))` causes the last record to be processed twice).
- `ferror(FILE *stream)`:
Tests the error indicator for the given stream. Returns non-zero (true) if a read or write hardware error has occurred.
- `clearerr(FILE *stream)`:
Clears both the EOF indicator and error indicator for the specified stream.
- `perror(const char *s)`:
Prints a human-readable error message to `stderr`. It prints user string `s`, followed by a colon and the system error message corresponding to the current global `errno` value:
```c
FILE *fp = fopen("missing.dat", "r");
if (fp == NULL) {
    perror("Custom Prefix"); /* Outputs: Custom Prefix: No such file or directory */
}
```
- `strerror(int errnum)`:
Defined in `<string.h>`. Returns a pointer to the textual error string corresponding to integer error code `errno`.

---
PRODUCTION-GRADE C PROGRAM: ROBUST FILE ERROR DIAGNOSTICS
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

int main(void) {
    FILE *fp = fopen("/root/protected_system_file.dat", "r");

    if (fp == NULL) {
        fprintf(stderr, "fopen failed! Global errno code: %d\n", errno);
        fprintf(stderr, "strerror diagnostic: %s\n", strerror(errno));
        perror("perror output");
        return 1;
    }

    char buffer[256];
    size_t bytes_read = fread(buffer, 1, sizeof(buffer), fp);

    if (bytes_read < sizeof(buffer)) {
        if (feof(fp)) {
            printf("Reached end-of-file successfully after reading %zu bytes.\n", bytes_read);
        }
        if (ferror(fp)) {
            fprintf(stderr, "Fatal Hardware I/O Error occurred during file read!\n");
            clearerr(fp);
        }
    }

    fclose(fp);
    return 0;
}
```
"""
            },
            {
                "qid": "cprog-q26",
                "marks": 7,
                "type": "Descriptive",
                "title": "Command Line Arguments in C: argc, argv, String Conversions, and Command-Line File Copy Utility",
                "yt_query": "command line arguments in C argc argv atoi atof mycopy file copy utility",
                "img_path": "images/cprog/command_line_args_argv.png",
                "img_caption": "Figure 5.6: Structure of argc and argv[] Pointer Array Passed from Operating System Shell",
                "answer": r"""
Command line arguments enable users to pass runtime configuration parameters, input values, and filenames to an executable program directly from the operating system command shell (Terminal / Command Prompt) at the time of invocation.

1. Declaration Syntax:
```c
int main(int argc, char *argv[])
```
- `argc` (Argument Count): An integer representing the total number of command-line arguments passed, including the executable program name itself ($argc \ge 1$).
- `argv` (Argument Vector): An array of pointers to null-terminated character strings (`char *`):
  - `argv[0]`: Contains the name of the executable program or invocation path.
  - `argv[1]`: The first user argument string.
  - `argv[argc - 1]`: The final argument string.
  - `argv[argc]`: Guaranteed by the C standard to be a `NULL` pointer.

2. Numeric Argument Conversion Functions in `<stdlib.h>`:
Because all command line arguments are received as character strings, numeric arguments must be converted using standard conversion functions:
- `int atoi(const char *str);`: Converts string to `int`.
- `long atol(const char *str);`: Converts string to `long`.
- `double atof(const char *str);`: Converts string to `double`.
- Robust alternatives: `strtol()` and `strtod()` perform boundary checks and error validation.

---
PRODUCTION-GRADE C PROGRAM: COMPLETE COMMAND-LINE FILE COPY UTILITY (`mycopy`)
Usage: `./mycopy source.txt dest.txt`
```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    FILE *src = NULL;
    FILE *dest = NULL;
    char buffer[4096]; /* 4 KB high-performance transfer buffer */
    size_t bytes;

    /* Verify that exact number of arguments is provided */
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <source_file> <destination_file>\n", argv[0]);
        return 1;
    }

    /* Open source file in binary read mode */
    src = fopen(argv[1], "rb");
    if (src == NULL) {
        fprintf(stderr, "Error: Cannot open source file '%s': ", argv[1]);
        perror("");
        return 1;
    }

    /* Open destination file in binary write mode */
    dest = fopen(argv[2], "wb");
    if (dest == NULL) {
        fprintf(stderr, "Error: Cannot create destination file '%s': ", argv[2]);
        perror("");
        fclose(src);
        return 1;
    }

    /* Stream transfer using buffered block I/O */
    while ((bytes = fread(buffer, 1, sizeof(buffer), src)) > 0) {
        if (fwrite(buffer, 1, bytes, dest) != bytes) {
            fprintf(stderr, "Fatal write error to destination file!\n");
            fclose(src);
            fclose(dest);
            return 1;
        }
    }

    printf("File '%s' successfully copied to '%s'.\n", argv[1], argv[2]);

    fclose(src);
    fclose(dest);
    return 0;
}
```
"""
            }
        ]
    }
]

CPROG_BYHEART = {
    'cprog-q1': {
        "eq": r'$$\text{Source (.c)} \xrightarrow{\text{cpp}} \text{Preprocessed (.i)} \xrightarrow{\text{cc1}} \text{Assembly (.s)} \xrightarrow{\text{as}} \text{Object (.o)} \xrightarrow{\text{ld}} \text{Binary (a.out)}$$',
        "text": r'C compilation pipeline consists of Preprocessor (macro expansion, header inclusion), Compiler (parsing, assembly code generation), Assembler (relocatable machine code), Linker (symbol resolution, library linking), and Loader.'
    },
    'cprog-q2': {
        "eq": r'$$\text{char (1B)} \to \text{int (4B)} \to \text{long (8B)} \to \text{float (4B)} \to \text{double (8B)} \to \text{long double (16B)}$$',
        "text": r'Fundamental C types: char (1B, -128 to 127), int (4B, -2B to +2B), float (4B), double (8B). Implicit type conversion promotes operands along promotion ladder; explicit casting forces conversion via `(type)val`.'
    },
    'cprog-q3': {
        "eq": r'$$x \ll k = x \times 2^k, \quad x \gg k = \lfloor x / 2^k \rfloor, \quad \text{Precedence: Postfix} > \text{Unary} > \text{Arithmetic} > \text{Shift} > \text{Relational} > \text{Bitwise} > \text{Logical} > \text{Assign}$$',
        "text": r'Bitwise operators (&, |, ^, ~, <<, >>) manipulate integer bits directly. Prefix ++x changes then uses; postfix x++ uses then changes. Logical && and || feature short-circuit evaluation.'
    },
    'cprog-q4': {
        "eq": r'$$\%[\text{flags}][\text{width}][.\text{precision}][\text{length}]\text{type}, \quad \text{scanf Requires Memory Address } (\&var)$$',
        "text": r'printf formatting controls width and precision (%-10.2f left-justifies 2 decimals). scanf requires memory address (&var for scalars; array name decays to base address without &). Discard whitespace using " %c".'
    },
    'cprog-q5': {
        "eq": r'$$\text{switch(expr): Integral types only}; \quad \text{break: Terminates loop/switch}; \quad \text{continue: Skips to next iteration}$$',
        "text": r'Control flow: if-else evaluates boolean truth; switch-case branches on integral constants (fall-through without break). while is pre-tested (0+ times); do-while is post-tested (1+ times guaranteed).'
    },
    'cprog-q6': {
        "eq": r'$$Loc(arr[i]) = \text{Base} + (i \times \text{sizeof(Type)}), \quad \text{Binary Search: } mid = low + \frac{high - low}{2} \ (O(\log_2 N))$$',
        "text": r'1D arrays allocate contiguous memory with zero-based indexing (no bounds checking in C). Binary Search on sorted arrays halves search space iteratively, achieving O(log N) complexity.'
    },
    'cprog-q7': {
        "eq": r'$$Loc(arr[i][j]) = \text{Base} + [(i \times N) + j] \times \text{sizeof(Type)}, \quad C_{ij} = \sum_{k=0}^{q-1} A_{ik} B_{kj} \ (O(n^3))$$',
        "text": r'Row-Major Order stores 2D matrix row by row. Matrix multiplication requires Columns of A == Rows of B; computed using three nested loops with O(p*q*r) complexity.'
    },
    'cprog-q8': {
        "eq": r'$$\text{String} = \text{Character Array terminated by } \backslash 0 \ (\text{ASCII 0}), \quad \text{Stack Array (Mutable) vs Literal Pointer (Read-Only)}$$',
        "text": r'Strings in C are null-terminated (`\0`). Character arrays on stack are mutable; string literal pointers point to read-only text segments. Use fgets() to prevent buffer overflow vulnerabilities.'
    },
    'cprog-q9': {
        "eq": r'$$\text{strlen: Count until } \backslash 0; \quad \text{strcpy: Copy including } \backslash 0; \quad \text{strcmp: } s1 - s2 \text{ ASCII difference}$$',
        "text": r'<string.h> functions operate via pointer traversal until null byte: strlen computes length, strcpy copies bytes, strcat appends to end, and strcmp compares ASCII differences.'
    },
    'cprog-q10': {
        "eq": r'$$\text{char names}[M][N] \implies M \text{ strings, each max } N-1 \text{ chars} + \backslash 0; \quad \text{Swap via strcpy(temp, arr[j])}$$',
        "text": r'2D character arrays store lists of strings. Sorting strings alphabetically employs bubble sort using strcmp() for lexicographical comparison and strcpy() with temporary buffer for swapping.'
    },
    'cprog-q11': {
        "eq": r'$$\text{Call by Value: Copies value to callee stack}; \quad \text{Call by Reference: Passes } \&var \text{ to pointer } *ptr$$',
        "text": r'Call by value passes copies; caller variables remain unchanged. Call by reference passes memory addresses (&x), enabling function to modify caller variables directly via dereferencing (*ptr).'
    },
    'cprog-q12': {
        "eq": r'$$T(n) = 2T(n-1) + 1 = 2^n - 1, \quad \text{Base Condition Prevents Stack Overflow}$$',
        "text": r'Recursion requires a base condition to terminate and an inductive step. Tower of Hanoi requires $2^n - 1$ moves. Missing base condition causes call stack exhaustion and stack overflow crash.'
    },
    'cprog-q13': {
        "eq": r'$$\text{auto (Stack, Garbage)}; \quad \text{register (CPU)}; \quad \text{static (Data/BSS, Zero, Lifetime=Program)}; \quad \text{extern (Global)}$$',
        "text": r'Storage classes define location, default value, scope, and lifetime. static local variables preserve state across function calls; static global restricts visibility to current file.'
    },
    'cprog-q14': {
        "eq": r'$$p \pm k = p \pm (k \times \text{sizeof(Type)}), \quad arr[i] \equiv *(arr + i), \quad \text{void* Generic; NULL: } (void*)0$$',
        "text": r'Pointer arithmetic scales by data type size. Array names decay into base pointers. Void pointers (void *) are generic; dangling pointers point to deallocated memory (neutralize via ptr = NULL).'
    },
    'cprog-q15': {
        "eq": r'$$\text{malloc: Uninitialized garbage}; \quad \text{calloc: Zero-initialized}; \quad \text{realloc: Resizes}; \quad \text{free: Prevents Memory Leaks}$$',
        "text": r'Dynamic Memory Allocation manages heap: malloc(size) allocates uninitialized bytes; calloc(n, size) allocates zero-filled bytes; realloc resizes existing block; free(ptr) prevents memory leaks.'
    },
    'cprog-q16': {
        "eq": r'$$\text{Structure Padding: Word alignment inserts dummy bytes; } \text{sizeof} = \text{multiple of largest member alignment}$$',
        "text": r'Structures bundle heterogeneous data. Compiler inserts padding bytes to align multi-byte data on word boundaries for fast bus access. Reordering members largest-to-smallest minimizes padding.'
    },
    'cprog-q17': {
        "eq": r'$$ptr\text{->}member \equiv (*ptr).member, \quad \text{Array of Structs: Table of records}$$',
        "text": r'Structure pointers access members using the arrow operator (->). Arrays of structures represent tabular database records. Pass structure pointers to functions to avoid stack frame copying overhead.'
    },
    'cprog-q18': {
        "eq": r'$$\text{struct Node } \{ \text{int data; struct Node *next; } \}; \quad \text{Heap Allocation via malloc}$$',
        "text": r'Self-referential structures contain a pointer to their own structure type. Used to build dynamic singly linked lists with dynamic heap nodes linked via next pointers terminated by NULL.'
    },
    'cprog-q19': {
        "eq": r'$$\text{sizeof(union)} = \text{Size of largest member}; \quad \text{All members share identical base memory address}$$',
        "text": r'Structures allocate separate memory for every member; Unions share a single memory block where only one member is active at a time. Bit-fields pack integer members into specific bit counts.'
    },
    'cprog-q20': {
        "eq": r'$$\text{typedef: Compiler type alias}; \quad \text{\#define: Preprocessor text substitution}; \quad \text{\#ifndef Header Guards}$$',
        "text": r'typedef creates compiler-verified type aliases; enum defines named integer constants; #define creates macros (use parentheses); #ifndef header guards prevent multiple inclusion.'
    },
    'cprog-q21': {
        "eq": r'$$\text{FILE *fp = fopen(name, mode); fclose(fp); Modes: "r", "w", "a", "r+", "w+", "a+"}$$',
        "text": r'File I/O uses FILE pointer streams. fopen() returns NULL on failure. Mode "r" reads existing; "w" overwrites/creates; "a" appends. Binary modes append "b" ("rb", "wb") without line translation.'
    },
    'cprog-q22': {
        "eq": r'$$\text{fgetc/fputc (Char)}; \quad \text{fgets/fputs (Line/String)}; \quad \text{fscanf/fprintf (Formatted Text)}$$',
        "text": r'File text I/O: fgetc reads characters until EOF (-1); fgets safely reads string line into buffer; fprintf and fscanf perform formatted reading and writing directly to disk streams.'
    },
    'cprog-q23': {
        "eq": r'$$\text{fwrite(ptr, size, count, fp); } \quad \text{fread(ptr, size, count, fp); } \quad \text{Direct RAM-Disk Block Transfer}$$',
        "text": r'Binary block I/O transfers raw memory bytes between RAM and disk without text conversion: fwrite writes arrays/structures; fread reads raw blocks. Returns count of items transferred.'
    },
    'cprog-q24': {
        "eq": r'$$\text{fseek(fp, offset, SEEK\_SET/SEEK\_CUR/SEEK\_END); } \quad \text{file\_size} = \text{ftell(fp) after SEEK\_END}$$',
        "text": r'Random access repositioning: fseek sets byte offset from SEEK_SET (start), SEEK_CUR (current), or SEEK_END (end). ftell returns current byte position; rewind resets to start.'
    },
    'cprog-q25': {
        "eq": r'$$\text{feof(fp): Non-zero after EOF read; ferror(fp): I/O error; perror(str): Prints errno message}$$',
        "text": r'feof() tests if EOF has been triggered; ferror() detects hardware I/O faults. perror() and strerror(errno) print system error diagnostics corresponding to global errno code.'
    },
    'cprog-q26': {
        "eq": r'$$\text{int main(int argc, char *argv[])}; \quad argv[0] = \text{Program Name}; \quad \text{atoi(argv[i]) converts to int}$$',
        "text": r'Command line arguments: argc counts arguments; argv is array of string pointers (argv[0] is program name). String conversion functions (atoi, atof) parse numerical command-line inputs.'
    }
}

CPROG_EXAM_QUESTIONS = {
    "cprog-q1": "Explain the fundamental structure of a C program. Describe the multi-stage compilation and execution process from source code to executable binary.",
    "cprog-q2": "Explain the primitive data types in C with size, range, and format specifiers. Discuss type modifiers, type qualifiers, and implicit vs explicit type conversion.",
    "cprog-q3": "Classify operators in C. Explain arithmetic, relational, logical, and bitwise operators with operator precedence and associativity rules.",
    "cprog-q4": "Explain formatted input and output functions printf() and scanf() with format specifiers, field width, precision, and escape sequences.",
    "cprog-q5": "Discuss decision-making and looping structures in C. Compare while and do-while loops, and write a menu-driven program for prime number checking and factorial calculation.",
    "cprog-q6": "Explain one-dimensional arrays and memory address allocation. Implement and compare linear search and binary search algorithms with step-by-step traces.",
    "cprog-q7": "Derive the row-major memory address formula for a two-dimensional array. Write a complete C program to perform matrix multiplication with dimensional verification.",
    "cprog-q8": "Explain how strings are represented in C. Differentiate between character arrays and string literals, and discuss string I/O using scanf, gets, and fgets.",
    "cprog-q9": "Explain standard library string manipulation functions in <string.h>. Provide manual C implementations of strlen, strcpy, strcat, and strcmp without library routines.",
    "cprog-q10": "Explain two-dimensional character arrays (array of strings). Write a complete C program to sort a list of student names alphabetically using bubble sort.",
    "cprog-q11": "Explain modular programming in C. Differentiate between Call by Value and Call by Reference parameter passing with memory stack diagrams and swapping examples.",
    "cprog-q12": "Explain recursion in C. Detail the role of base conditions and call stack frames. Provide a recursive solution and call tree for the Tower of Hanoi problem.",
    "cprog-q13": "Explain storage classes in C: auto, register, static, and extern. Compare them in terms of storage area, default initial value, scope, and lifetime.",
    "cprog-q14": "Explain the concept of pointers in C. Discuss pointer arithmetic, array-pointer equivalence, void pointers, and dangling pointers with illustrative examples.",
    "cprog-q15": "Explain dynamic memory allocation in C. Differentiate between malloc, calloc, realloc, and free, and write a program demonstrating dynamic array creation and resizing.",
    "cprog-q16": "Define structures in C. Explain memory allocation for structures and mathematically derive structure padding and word alignment on 32-bit and 64-bit architectures.",
    "cprog-q17": "Explain arrays of structures and nested structures. Discuss passing structure pointers to functions and the use of the arrow operator (->).",
    "cprog-q18": "What is a self-referential structure? Explain how self-referential structures are utilized in linked lists, and write a program to insert and traverse nodes.",
    "cprog-q19": "Compare structures and unions in terms of memory allocation and size calculation. Explain the concept of bit-fields in structures for compact memory packing.",
    "cprog-q20": "Explain typedef and enumerations (enum). Describe C preprocessor directives including #define macros, file inclusion, and conditional compilation with header guards.",
    "cprog-q21": "Explain file handling basics in C. Discuss the FILE pointer, fopen(), fclose(), standard file access modes (r, w, a, r+, w+, a+), and text vs binary files.",
    "cprog-q22": "Explain character, line, and formatted file I/O functions. Write a complete C program to copy a text file and count the total characters, words, and lines.",
    "cprog-q23": "Explain block-level binary file I/O using fread() and fwrite(). Write a C program to store and read an array of employee structure records to/from a binary disk file.",
    "cprog-q24": "Explain random access in files using fseek(), ftell(), and rewind(). Discuss SEEK_SET, SEEK_CUR, and SEEK_END, and show how to determine file size.",
    "cprog-q25": "Explain error handling in file operations in C. Discuss feof(), ferror(), clearerr(), perror(), and strerror() with a diagnostic code example.",
    "cprog-q26": "Explain command line arguments in C with argc and argv. Write a complete C program implementing a command-line file copy utility."
}
