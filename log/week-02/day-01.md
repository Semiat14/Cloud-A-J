# Week 2 · Day 1 · Linux comeback + OverTheWire Bandit (Levels 0–5)

**Setup:** Ubuntu on WSL2. Turns out I already had it 😄

**Self-test (7/7):** mkdir, touch, echo + > / >>, cat, cp, mv, ls -la, cd .., rm -r

**Learned:**
- Permissions as numbers: r=4 w=2 x=1 → rwxr-xr-x = 755, rw------- = 600
- `>` overwrites, `>>` appends
- Filenames starting with `-` look like flags → use `./`
- Quotes for filenames with spaces
- Dot-files are hidden → `ls -a`
- `file` tells you what type of data is inside; `*` wildcard checks many files at once
- SSH "broken pipe" = idle TCP session dropped

**Bandit:** reached Level 5 (no spoilers, per the rules 🤫)
