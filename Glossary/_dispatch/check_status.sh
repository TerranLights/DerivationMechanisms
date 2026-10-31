#!/usr/bin/env bash
# Show the STATUS line and row count of every harvest file.
cd "$(dirname "$0")/../_harvest" || exit 1
for a in T G1 G2 G3a G3b G4 C S O M; do
  f="$a.md"
  if [ -f "$f" ]; then printf '%-4s %-55s rows=%s\n' "$a" "$(grep -m1 '^STATUS:' "$f")" "$(grep '^| ' "$f" | grep -v -E '^\| *Term *\||^\| *-' | wc -l)"; else printf '%-4s (missing)\n' "$a"; fi
done
