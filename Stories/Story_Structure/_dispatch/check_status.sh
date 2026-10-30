#!/usr/bin/env bash
# Prints each output file's STATUS line and counts per framework. Usage: bash _dispatch/check_status.sh
cd "$(dirname "$0")/.." || exit 1
declare -A EXPECT=( ["John Truby - The Anatomy of Story"]=33 ["Blake Snyder - Save the Cat"]=33 ["Dan Harmon - Story Circle"]=9 )
for d in "John Truby - The Anatomy of Story" "Blake Snyder - Save the Cat" "Dan Harmon - Story Circle"; do
  n=0; c=0
  if [[ -d "$d" ]]; then
    while IFS= read -r -d '' f; do n=$((n+1)); s=$(head -1 "$f"); [[ "$s" == "STATUS: COMPLETE"* ]] && c=$((c+1)) || echo "  $s  |  ${f#$d/}"; done < <(find "$d" -name '*.md' -not -name '00 - README.md' -print0 | sort -z)
  fi
  echo "$d: $c complete of $n files (about ${EXPECT[$d]} expected)"
done
[[ -d "source_reference (local only, not in git)/text" ]] || echo "NOTE: source texts missing; recreate them (see _dispatch/resume_prompt.md)."
