---
title: Bash Notes
date: 2023-06-05 02:23:00 +0200
categories: [notes]
tags: [linux, shell, bash]
---


## echo

```bash
echo "Hello World with new line"
```

```bash
echo -n "Hello World without new line"
```

## while

```bash
while [ $bool ] do

# ...Code...

done

```

## for

```bash
for (( i = 0; i < 10; i++ )) do

# ...Code...

done
```

## if

```bash
if [ $bool ] ; then
    # Do something
elif [ $other_bool ] ; then
    # Do something else
else
    # Do something else
fi
```

## Take input

```bash
read a
echo $a
```

## Arguments

Number of arguments: `$#`

Nth Argument: `$n` (n = [1-9])

## Functions

```bash
function name(){

}
```

## Read a file

```bash
file="book.txt"

while read line; do
    echo $line
done < $file

```

## Read a directory

```bash
for i in [dir]/* ; do
    echo "$i"
done
```

## if tests

```bash
arg = $1

if [ -e $arg ] ; then 
    echo "$arg exists"
fi

if [ -f $arg ] ; then
    echo "$arg is a file"
elif [ -d $arg ] ; then
    echo "$arg is a directory"
else
    echo "$arg is something else"
fi
```

```bash
if [ $# -ne 1 ] ; then
    echo "I need only one argument" 1>&2
    exit 1;
fi

if [ ! -f $1 ] ; then
    echo "Argument is not a file" 1>&2
    exit 2;
```

## sleep

```bash
echo "Wait for 5 seconds"
sleep 5
echo "Done"
```

## cut

cut -d [seperation_character] -f[field_num]

```bash
cut -d " " -f1
```

## sort

* [expression] | sort -k[num] -t [char]

Sort the lines of the output of the [expression] based on the [num] field after sererating them based on the [char]

## uniq

Before `uniq` always sort

Removes concurrent duplicate lines

`-c` adds  a prefix of the number of occurences

```bash
ls | sort | uniq -c
```

## tr

* tr [first_set] [second_set]

Replaces the first set of characters with the second one

```bash
tr [:lower:] [:upper:]
```

* tr -s [character]

Replace each sequence of a repeated character that is  listed  in  the  last specified SET, with a single occurrence of that character

```bash
tr -s " "
```

## Inline code

a=`[command]`

The result of the [command] goes into the variable `a`

## head

[expression] | head -n[num]

Print the first [num] of lines of the [expression]'s output

## tail

[expression] | tail -n[num]

Print the last [num] of lines of the [expression]'s output

## Error message

echo [message] 1>&2;
exit [num!=0]

```bash
if [ $# -ne 1 ] ; then
    echo "One argument needed" 1>&2;
    exit 1
fi
```

## egrep

egrep [options] PATTERN [FILE...]

### Options

`-v` reverse of the pattern

`--color` adds color to matches

`-c` count the number of matches

`-i` ignores case

