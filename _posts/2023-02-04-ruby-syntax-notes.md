---
title: Ruby Syntax Notes
date: 2023-02-02 11:08:00 -200
categories: [notes] 
tags: [ruby]
---

## Printing

```ruby
#print
puts "Hello"
print "world"
```

## Begin / End

```ruby
# Runs first in the programm
BEGIN {
    puts "Runs first of all because of BEGIN"
}

# Runs last in the program
END {
    puts "Runs last"
}
```

## Functions

```ruby
def function_name
    #do stuff
end
```

## Classes

```ruby
class Vehicle
    attr_reader :no_of_wheels, :horsepower, :type_of_tank, :capacity

    def initialize(no_of_wheels, horsepower, type_of_tank, capacity)
        @no_of_wheels = no_of_wheels
        @horsepower = horsepower
        @type_of_tank = type_of_tank
        @capacity = capacity
    end

    def speeding
        # code
    end

    def driving
        # code
    end

    private

    def halting
        # code
    end
end
```

## Creating an object

```ruby
car = Vehicle.new
bike = Vehicle.new(no_of_wheels: 2)
```

## Variables

* Local Variables − Local variables are the variables that are defined in a method. Local variables are not available outside the method. You will see more details about method in subsequent chapter. Local variables begin with a lowercase letter or _.
* Instance Variables − Instance variables are available across methods for any particular instance or object. That means that instance variables change from object to object. Instance variables are preceded by the at sign (@) followed by the variable name.
* Class Variables − Class variables are available across different objects. A class variable belongs to the class and is a characteristic of a class. They are preceded by the sign @@ and are followed by the variable name.
* Global Variables − Class variables are not available across classes. If you want to have a single variable, which is available across classes, you need to define a global variable. The global variables are always preceded by the dollar sign ($).

### Examples

```ruby
$global_var = 10;

@instance_var = 3 #in functions

@@private_var =  5 #in Classes

PI = 3.14 # Constant - All caps
```

### Printing a variable

```ruby
puts "\nPi = #{PI}"
#OR
print "Pi = ", PI, "\n"
```

## Numbers

```ruby
123                  # Fixnum decimal
1_234                # Fixnum decimal with underline
-500                 # Negative Fixnum
0377                 # octal
0xff                 # hexadecimal
0b1011               # binary
?a                   # character code for 'a'
?\n                  # code for a newline (0x0a)
12345678901234567890 # Bignum (THANK GOD)
123.4                # floating point value
1.0e6                # scientific notation
4E20                 # dot not required
4e+20                # sign before exponential
```

## Arrays

```ruby
arr = ["fred", 10, 3.14, "This is a string", "last element"]
arr.each do |i|
   puts i
end
```

## Hashes

```ruby
hsh = colors = { "red" => 0xf00, "green" => 0x0f0, "blue" => 0x00f }
hsh.each do |key, value|
   print key, " is ", value, "\n"
end
```

### Adding element to an existing hash

```ruby
hash {"One" => 1, "Two" => 2}

hash.merge!("Three" => 3)
```

## Ranges

```ruby
(10..15).each do |n|
   print n, ' '
end
puts ""
```

## Comments

```ruby
# A single line comment
```

```ruby
=begin
This is a multiline comment and con spwan as many lines as you
like. But =begin and =end should come in the first line only.
=end
```

## If statement

```ruby
x = 1
if x > 2
   puts "x is greater than 2"
elsif x <= 2 && x!=0
   puts "x is 1"
else
   puts "I can't guess the number"
end
```

### Single-line if statement

```ruby
flag = true
puts "It is True" if flag
```

## Unless statement

```ruby
x = 1
unless x>=2
   puts "x is less than 2"
 else
   puts "x is greater than 2"
end
```

## While loop

```ruby
$i = 0

while $i < 5  do
   puts("Inside the loop i = #$i" )
   $i +=1
end
```

## Do-While loop

```ruby
$i = 0
$num = 5
begin
   puts("Inside the loop i = #$i" )
   $i +=1
end while $i < $num
```

## Until *(reverse of while)*

```ruby
i = 0
$num = 5

until $i > $num  do
   puts("Inside the loop i = #$i" )
   $i +=1;
end
```

## Do-Until *(reverse of do while)*

```ruby
$i = 0
$num = 5
begin
   puts("Inside the loop i = #$i" )
   $i +=1;
end until $i > $num
```

## For loop

```ruby
for i in 0..5 # 0 to 5
   puts "Value of local variable is #{i}"
end
```

### OR

```ruby
(0..5).each do |i|
   puts "Value of local variable is #{i}"
end
```

>*next instead of continue*

## Unpack (who the fuck knows?)

```ruby
"abc \0\0abc \0\0".unpack('A6Z6')   #=> ["abc", "abc "]
"abc \0\0".unpack('a3a3')           #=> ["abc", " \000\000"]
"abc \0abc \0".unpack('Z*Z*')       #=> ["abc ", "abc "]
"aa".unpack('b8B8')                 #=> ["10000110", "01100001"]
"aaa".unpack('h2H2c')               #=> ["16", "61", 97]
"\xfe\xff\xfe\xff".unpack('sS')     #=> [-2, 65534]
"now = 20is".unpack('M*')           #=> ["now is"]
"whole".unpack('xax2aX2aX1aX2a')    #=> ["h", "e", "l", "l", "o"]
```
