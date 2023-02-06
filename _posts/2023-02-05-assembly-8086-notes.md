---
title: Assembly 8086 Notes
date: 2023-02-05 02:47:00 -200
categories: [notes] 
tags: [assembly, assembly-8086]
---

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


>[MD file](https://github.com/KDesp73/Docs/blob/main/_posts/2023-02-05-assembly-8086-notes.md)
