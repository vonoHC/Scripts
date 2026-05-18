# Scripts para completar automáticamente cada nivel de bandit (OverTheWire)

**bandit2**:
```bash
cat ./--spaces\ in\ this\ filename--
```

**bandit3**:
```bash
cat /home/bandit3/inhere/.*
```

**bandit4**:
```bash
find . -type f | grep "\-file" | xargs file | grep ASCII | awk -F':' '{print $1}' | xargs cat
```

**bandit5**:
```bash
find . -type f -size 1033c ! -executable | xargs cat
```

**bandit6**:
```bash
find -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null | xargs cat
```

**bandit7**:
```bash
cat data.txt | grep millionth | awk -F' ' '{print $2}’
```

**bandit8**:
```bash
sort data.txt | uniq -u
```

**bandit9**:
```bash
strings data.txt | grep "===" | tail -n 1 | awk 'NF{print $2}’
```

**bandit10**:
```bash
cat data.txt | base64 -d | awk -F' ' '{print $NF}’
```



