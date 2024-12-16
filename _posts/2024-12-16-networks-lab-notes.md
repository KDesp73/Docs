---
title: Networks Lab Notes 
date: 2024-12-16 14:33:00 +0200
categories: [notes] 
tags: [networks, school]
---

## Links

- [Σελίδα Μαθήματος](https://people.iee.ihu.gr/~dima/?page_id=13#)
- [DNS Watch](https://dnswatch.info)
- [Google Dig](https://toolbox.googleapps.com/apps/dig/)
- [Dig](https://www.digwebinterface.com/)

## Ενότητα 1

### Εντολή `ipconfig /all`

Η εντολή `ipconfig /all` εμφανίζει αναλυτικές πληροφορίες για τη διαμόρφωση του δικτύου.

```powershell
ipconfig /all
```

#### Host 
- Physical Address
- IPv4

#### Δίκτυο
- Subnet Mask
- Defauly Gateway (Διεύθυνση Router)

### Εντολή `tracert`

```powershell
tracert <domain | IPv4>
```

Η εντολή tracert εμφανίζει τη διαδρομή που ακολουθούν τα πακέτα μέχρι έναν συγκεκριμένο προορισμό, παρέχοντας τη λίστα των ενδιάμεσων σταθμών (jumps).

Σημειώσεις:
- Γραμμές με αστερίσκους (*) υποδεικνύουν χρονικά όρια (timeouts) και δεν τις λαμβάνουμε υπόψη.


### TCP Protocol Stack

![tcp-protocol-stack](./assets/tcp-protocol-stack.png "TCP Protocol Stack")

### DNS

- Θύρα 53

#### Records

- NS: Name Server (Διακομιστής Ονομάτων)
- A: Address Record (συσχέτιση ενός domain με μία IPv4 διεύθυνση)
- MX: Mail Exchange Record (Διακομιστής Ηλεκτρονικού Ταχυδρομείου)
- CNAME: Canonical Name (συσχέτιση ενός εικονικού domain με ένα πραγματικό)

### Εντολή `arp -a <host>`

```powershell
arp -a <host>
```
