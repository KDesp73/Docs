---
title: Ruby Web Server
date: 2023-02-02 04:38:00 +0200
categories: [documentation] 
tags: [ruby, server]
---

## A simple functional server made with pure Ruby

*It can host static websites*

![server index](https://user-images.githubusercontent.com/63654361/216193983-89083007-d1aa-44f4-b711-60ef24be02ec.png)

## Requirements

* Ruby 3.0.0 minimum

## How to use it

1. Clone this [repository](https://github.com/KDesp73/Ruby-Web-Server)

    ```bash
    git clone https://github.com/KDesp73/Ruby-Web-Server
    ```  

2. Add your static site in the `docs/` folder

3. In selected directory run: 

    ```bash
    ruby ./server.rb
    ```  

    The server is now running on localhost:2000

4. Change the configuration from the 'config.yml' file if neccessary

## TODO

* Host multiple sites
* Host dynamic sites with full PHP functionality