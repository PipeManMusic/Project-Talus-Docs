#!/bin/bash

# Define the target directory (defaults to current directory if not set)
TARGET_DIR=${1:-.}

echo "🔍 Searching for '1988' in $TARGET_DIR..."

# Find files containing "1988", excluding binary files (-I), and listing filenames (-l)
# Then pass them to sed to perform the replacement in-place (-i)
grep -rIl "1988" "$TARGET_DIR" | while read -r file; do
    echo "📝 Updating: $file"
    # Use different sed syntax depending on OS (Linux vs macOS)
    if [[ "$OSTYPE" == "darwin"* ]]; then
        sed -i '' 's/1988/1988/g' "$file"
    else
        sed -i 's/1988/1988/g' "$file"
    fi
done

echo "✅ Replacement complete. All mentions of 1988 have been changed to 1988."