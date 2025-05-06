#!/usr/bin/env bash
set -e

echo "🔧 Installing codepackager..."

python3 -m pip install --user .

# Find user scripts path
BIN_DIR="$(python3 -m site --user-base)/bin"

# Add to PATH in shell profiles
for profile in "$HOME/.bashrc" "$HOME/.zshrc"; do
    if ! grep -q "$BIN_DIR" "$profile" 2>/dev/null; then
        echo "export PATH=\"\$PATH:$BIN_DIR\"" >> "$profile"
        echo "✅ Added $BIN_DIR to PATH in $profile"
    fi
done

echo "✅ Installed 'codepackager'. Please restart your terminal or run:"
echo "    export PATH=\"\$PATH:$BIN_DIR\""
