---
title: Assembly 8086 Notes
date: 2023-02-05 02:47:00 +0200
categories: [notes] 
tags: [assembly, assembly-8086]
---

>The code snippets are in armasm because x86asm wouldn't render. So ignore the syntax errors.

## Emu8086

* [Download](https://en.lo4d.com/s/emu8086)
* [License key](https://users.iee.ihu.gr/~iee2021035/emu8086_license_key.txt)

## Registers

Memory slots used to store data

### General Purpose Registers

* ax - the accumulator register (divided into ah / al)
* bx - the base address register (divided into bh / bl)
* cx - the count register (divided into ch / cl)
* dx - the data register (divided into dh / dl)
* si - source index register
* di - destination index register
* bp - base pointer
* sp - stack pointer

### Segment Registers

* cs - points at the segment containing the current program
* ds - generally points at the segment where variables are defined
* es - extra segment register, it's up to the programmer to define its usage
* ss - points at the segment containing the stack

> All general purpose registers are 16 bit

In the 8086 assembly language, there are several registers, each serving a specific purpose. Here's a brief description of each register and its typical usage:

    General-Purpose Registers:
        AX (Accumulator): Used for arithmetic and data manipulation. It is also involved in some multiplication and division operations.
        BX (Base): Often used as a pointer to data or an offset in memory addressing.
        CX (Count): Primarily used as a loop counter in iterative operations.
        DX (Data): Like AX, it is used for arithmetic operations and sometimes holds the high-order bits of the result.

    Segment Registers:
        CS (Code Segment): Points to the current code segment.
        DS (Data Segment): Points to the data segment where program variables are stored.
        SS (Stack Segment): Points to the stack segment, which holds the program stack.
        ES (Extra Segment): Used to store additional data segment addresses.

    Index and Pointer Registers:
        SI (Source Index): Typically used as a pointer to the source data in string operations.
        DI (Destination Index): Usually used as a pointer to the destination in string operations.
        BP (Base Pointer): Frequently used to access function parameters and variables stored on the stack.
        SP (Stack Pointer): Points to the top of the stack and is involved in managing the stack.

    Flags Register:
        FLAGS: Contains various status flags indicating the outcome of arithmetic and logical operations, as well as control flags for branching and looping.

These registers are fundamental to 8086 assembly programming, and their usage may vary depending on the specific requirements of a program.


## Data Types

* db - Define Byte
* dw - Define Word
* dd - Define Doubleword
* dq - Define Quadword

### Examples

```armasm
a db 9
message db 'hello world'
var dw 1122h    ; hexadecimal value
```

```armasm
string db "lorem ipsum", '$'    ; '$' for end of string
string1 db 10, 13, "lorem ipsum", '$'  ; 10,13 for new line
```

## Arrays

### Declaration

```armasm
a db 1h, 2h, 3h, 7h     ; int a[] = {1, 2, 3, 7}
```

```armasm
; Store a value from an array to the al register
mov al, a[2]

; or with the help of the index rsgister
mov si, 2
mov al, a[si]
```

### Array Declaration using DUP

```armasm
x db 3 dup(7)

; same as

x db 7, 7, 7
```

```armasm
y db 3 dup(5, 6)

; same as

y db 5, 6, 5, 6, 5, 6
```

### Declaring an empty array

```armasm
var db 10 dup(?)    ; int var[10] = {0}
```

## MOV instruction

It copies the second operand, called source, to the first operand called destination

```armasm
mov ax, 7
```

### Types of operands supported

```armasm
;reg: ax, bx, ah, al, ch, cl, cx, di...etc
;immediate: 7, -11, 4fh...etc
;memory: [bx] or [bx+si] + displacement

mov reg, memory
mov memory, reg
mov reg, reg
mov memory, immediate
mov reg, immediate

;note -> mov memory, memory is not supported
```

### Memory

Combination of bx, si, di, bp registers inside of [] can be used to access memory

## ADD

```armasm
mov ax, 11h
mov bx, 14h
add ax, bx  ; ax = 25h
```

The result is stored in the destination (first register)

## SUB

```armasm
mov ch, 23h
sub ch, 11h ; now ch = 12h
```

## Flags or Processor Status Registers

![asm flags](https://user-images.githubusercontent.com/63654361/216797359-50f309cf-2502-4044-bcc4-c18c965bf5af.png)

16 bits. Each bit is called a "flag" and can be 0 or 1

* Carry Flag: Set to 1 when there is unsigned overflow
* Zero Flag: Set to 1 when result is zero, else it is set to 0
* Sign Flag: Set to 1 when the result is negative, else it is set to 0

### Example

```armasm
mov ch, 12h
sub ch, 24h
```

Flags: Z = 0 (result not zero), C = 1 (carry), S = 1 (result negative)

## MUL

Multiplication assumes one of the operands is al or ax.

```armasm
mov al, 7h
mov bl, 7h

mul bl
```

The result is stored in the al or ax register

### IMUL

It's used for signed numbers

```armasm
mov al, 35h
mov bl, 7h

imul bl
```

IMUL uses the overflow flag

## DIV

The result is stored in the al and ah registers respectively and div assumes one of the operands is ax.

```armasm
mov ax, 0041h
mov bl, 02h

div bl
```

`ax`(41) / `bl`(2) = `al`(20) + `ah`(1)

### IDIV

It's used for unsigned numbers

## Logical Intructions

* AND
* OR
* XOR
* NOT
* TEST

### Using AND to determine if a number is even or odd

*It changes the value of the al register*

```armasm
mov al, 8h
and al, 01h
```

0000 1000 <br>
0000 0001 <br>
===AND=== <br>
0000 0000

So the number is even

```armasm
mov al, 5h
and al, 01h
```

0000 0101 <br>
0000 0001 <br>
===AND=== <br>
0000 0001

So the number is odd

### TEST

Like AND

*It does not change the value of the al register*

```armasm
mov al, 7h
test al, 01h
;  affects the flag
```

>The other operands work as expected

## Program Control Flow

### Jumps

jmp, je, jle, jne, jz, jnz, ja, jb, jc

#### Unconditional Jumps

They transfer control to another part of the program

Sample code

```armasm
jmp read ;jump to read label
```

```armasm
read: 
    mov ah, 01
    jmp exit

exit:
    mov ah, 4ch
    int 21h
```

#### Conditional Jumps

* Jump only when some condition is satisfied
* Most jumps work by affecting CPU FLAGs while jumps like jcxz depend on the register

 `je` and `jz` - Jump when ZERO flag is equal to 1. They are more appropriate when you check whether something is 0 or not

 `jne` and `jnz` - Jump when ZERO flag is 0. They are mostly used after a cmp instruction

`ja` and `jg` - Jump if above jump is greater

`ja` - Jump if CF = 0 and ZF = 0

`jg` - Jump if SF = OF and ZF = 0

`jb` - Jump if CF = 1

`jc` - Jump if CF = 1

`jcxz` - Jump id CX register is zero

### Instructions

* `inc` - Adds 1 to any register
* `dec` - Subtracts 1 from any register
* `cmp` - subtract source form destination and set the flags appropriately

```armasm
inc ax
dec bx
cmp al, 10h
```

### Bit Manipulation

* `shl` - Shifts bits of byte to the left.

```armasm
shl al, 1 ; shift al by 1 (use cl register if it's more than 1)
```

* `shr` - Shifts bits of byte to the right

```armasm
shr al, 1 ; shift al by 1 (use cl register if it's more than 1)
```

* `rol` - Rotates the bits from the front to the back

![rol](https://user-images.githubusercontent.com/63654361/216864072-7f49eef8-f1ed-4746-a409-586d3bf47fe9.png)

```armasm
mov cx, 7h
rol ax, cl ; requires immidiate 8 bit operand or the cl register as the shift count
```

* `ror` - Rotates the bits from the back to the front

```armasm
mov cx, 7h
ror ax, cl ; requires immidiate 8 bit operand or the cl register as the shift count
```

>[MD file](https://github.com/KDesp73/Docs/blob/main/_posts/2023-02-05-assembly-8086-notes.md)


## Standard code snippets

### Assume segment registers

```armasm
assume cs: code, ds: data, ss:stack
```

### Initalize ds

```armasm
mov ax, data
mov ds, ax
```

### Return control to OS

```armasm
mov ah, 4ch
int 21h
```

### Print string

```armasm
lea dx, msg
mov ah, 9
int 21h
```

### Print integer

```armasm
mov dl, int
add dl, 48
mov ah, 2
int 21h
```

### Get integer / character input

> Gets the ascii value

```armasm
mov ah, 8h
int 21h
```

### Get integer / character input and print it

> Gets the ascii value

```armasm
mov ah, 1
int 21h
```


## Software interrupts

> Before int 21h

1. "Terminate program" - AH = 4Ch (76 decimal)
2. "Display string" - AH = 09h (9 decimal)
3. "Read keyboard input" - AH = 01h (1 decimal)
4. "Write character to standard output" - AH = 02h (2 decimal)
5. "Get system date" - AH = 2Ah (42 decimal)
6. "Get system time" - AH = 2Ch (44 decimal)
7. "Create a new file" - AH = 3Ch (60 decimal)
8. "Open an existing file" - AH = 3Dh (61 decimal)
9. "Close a file" - AH = 3Eh (62 decimal)
10. "Read data from a file" - AH = 3Fh (63 decimal)
11. "Write data to a file" - AH = 40h (64 decimal)
12. "Delete a file" - AH = 41h (65 decimal)
13. "Rename a file" - AH = 56h (86 decimal)
14. "Get current disk drive" - AH = 19h (25 decimal)
15. "Set disk transfer area address" - AH = 1Dh (29 decimal)
16. "Get system time count" - AH = 2Dh (45 decimal)
17. "Set system time" - AH = 25h (37 decimal)
18. "Get current default drive" - AH = 19h, DL = 0 (25 decimal, DL = 0)

## Processes

```armasm
[name] proc
    ...
    ...
    ...
    ret
[name] endp
```

## Template file

```armasm
title [title]

assume cs:code, ds:data, ss:stack

stack segment stack
    db 256 dup(0)
stack ends

data segment
    ; data
data ends

code segment
main proc near
    mov ax, data
    mov ds, ax


    mov ah, 4ch
    int 21h
main endp
code ends

end main
```

## Printing numbers

### 2 digits

```armasm
print_two_digit_num proc
    push bx
    push cx

    ; assuming number is in ax
    mov cl, 10
    div cl      ; ax / cl -> ah, al
    
    mov bx, ax

    mov dl, bl  
    add dl, 48 
    mov ah, 2 
    int 21h
    
    mov dl, bh 
    add dl, 48 
    mov ah, 2 
    int 21h

    pop bx
    pop cx
    ret
print_two_digit_num endp
```

### 3 digits

```armasm
print_three_digit_num proc
    push bx
    push cx

    mov cl, 100
    div cl

    mov bx, ax

    mov dl, bl
    add dl, '0'
    mov ah, 2h
    int 21h
    
    xchg bl, bh
    mov bh, 0
    mov ax, bx

    mov cl, 10
    div cl

    mov bx, ax

    mov dl, bl
    add dl, '0'
    mov ah, 2h
    int 21h

    mov dl, bh
    add dl, '0'
    mov ah, 2h
    int 21h

    pop bx
    pop cx

    ret
print_three_digit_num endp
```