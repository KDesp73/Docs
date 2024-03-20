---
title: Linux Swapfile
date: 2024-03-20 11:03:00 +0200
categories: [tutorial]
tags: [linux, ram, swap, system]
---

## Creating the swapfile

```sh
sudo dd if=/dev/zero of=/swapfile bs=1M count=4096 status=progress
```

This creates a swapfile and allocates 4GB for it

### Set the required permissions

```sh
sudo chmod 600 /swapfile
```

### Enable the swapfile

```sh
sudo mkswap /swapfile
sudo swapon /swapfile
```

### Ensure swap is enabled at boot

```sh
sudo bash -c "echo /swapfile none swap defaults 0 0 >> /etc/fstab"
```

## Increasing the size of the swapfile

### Turn off all swap processes

```sh
sudo swapoff -a
```

### Resize swap

Normaly you want your swap to be RAM(GB) + 2GB

So if you have 8GB of ram your swap should be 10GB

```sh
sudo dd if=/dev/zero of=/swapfile bs=1G count=10
```

### Make the file usable as swap

```sh
sudo mkswap /swapfile
```

### Activate the swapfile

```sh
sudo swapon /swapfile
```

This should be it!

