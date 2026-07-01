#!/bin/bash
# ☤ Clinic Maker Sandbox Installer Script
set -e

# ANSI styling helper variables
BLUE='\033[94m'
GREEN='\033[92m'
YELLOW='\033[93m'
RESET='\033[0m'

# Resolve the script's own directory so paths work on any machine
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

clear
echo -e "${BLUE}=========================================================${RESET}"
echo -e "${BLUE}              INSTALLING CLINIC MAKER SANDBOX            ${RESET}"
echo -e "${BLUE}=========================================================${RESET}"
echo -e " Security Target: ${GREEN}NVIDIA NemoClaw Seccomp Enforcements${RESET}"
echo -e "---------------------------------------------------------"

# 1. Verify python3 availability
echo "Checking Python 3 environment..."
if ! command -v python3 &> /dev/null; then
    echo -e "❌ Python 3 could not be found! Please make sure Python 3 is installed."
    exit 1
else
    echo -e "✅ Found Python 3 environment: $(python3 --version)"
fi

# 2. Run Database Initializer
echo "Configuring sandboxed SQLite model tables..."
python3 db/db_init.py

# 3. Print unified confirmation
echo -e "\n${GREEN}✨ INSTALLATION SUCCESSFUL!${RESET}"
echo -e "---------------------------------------------------------"
echo -e "  To start the ClearClinic Operations Engine:"
echo -e "  ${YELLOW}python3 clinic-maker.py${RESET}"
echo -e "---------------------------------------------------------"
echo -e "  Open ${BLUE}${SCRIPT_DIR}/app/index.html${RESET} in your browser."
echo -e "========================================================="
