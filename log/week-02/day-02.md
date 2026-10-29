# Week 2 · Day 2 · Bandit 6→12 + users, groups & packages

**Bandit:** Levels 6→9 (no spoilers 🤫)
- `find / -user X -group Y -size 33c 2>/dev/null`: search the whole server, hide errors
- `grep word file`: find text inside a file
- `sort file | uniq -u`: pipes chain commands together

**My own Ubuntu:**
- Forgot my WSL password → reset it with `wsl -u root` + `passwd sem`
- `sudo apt update` (refresh catalogue) vs `sudo apt install tree` (install)
- `groups` / `grep sudo /etc/group`: groups are memberships, not folders
- `sudo adduser tolu`, `sudo chown tolu secret.txt`: gave a file away, then got
  "Permission denied" writing to it. Ownership + permissions decide access, and root overrides all.
  **Bandit 9→12 (continued):**
- `strings data.txt | grep ===`: pull readable text out of a binary file, then filter
- `base64 -d data.txt`: decode base64 (encoding, not encryption)
- `cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'`: ROT13, swapping each letter for the one 13 places along
