---
title: Linux Notes
date: 2023-03-12 22:00:00 +0200
categories: [notes]
tags: [linux, shell]
---

## Lab 1

```shell
whoami
```

```shell
echo "Hello World"
```

### Seperator

```shell
whoami ; cal 2021
```

### Arguments

General syntax

```shell
cmd_name agrs file_names
```

Example

```shell
ls –l –a /tmp
```

* One letter arguments `-l`
* Word arguments `--version`

`-la` == `-l -a`

`-all` != `--all`

`man cmd_name` lists all the use cases of the selected command with a description

`stat [file/dir]` gives information about the file/dir

```shell
man ls
```

### Directory / File Management

| Command | Arguments                       | Description                               |
|---------|---------------------------------|-------------------------------------------|
| mkdir   | [dir_name]                      | Create a directory                        |
| rmdir   | [dir_name]                      | Remove a directory                        |
| cp      | [-i] [-f] [-r] [src/dest]       | Copy files or directories                 |
| mv      | [-i] [-f] [src] [dest]          | Rename / Move files or directories        |
| rm      | [-i] [-f] [-r] [file/dir names] | Deletes files or directories              |
| cd      | [dir_name]                      | Change directory to argument              |
| ls      | [-l] [-a] [dir names]           | List directory contents                   |
| pwd     |                                 | print current absolute path               |
| cat     | [file_name]                     | print file contents                       |
| more    | [file_name]                     | Print file contents partialy              |
| head    | [-number] [file_name]           | Print first [number] rows of file         |
| tail    | [-number] [file_name]           | Print last [number] rows of file          |
| touch   | [file_name]                     | Create an empty file in current directory |

### Home variable

```shell
echo ~
```

```shell
echo ~root
```

```shell
echo $HOME
```

`$HOME` is an environment variable

`~` is the abbriviation for `$HOME`

`~username` gives us the absolute path of user's home directory

