- [Overview](#overview)
- [Step 1: Enable WSL2](#step-1-enable-wsl2)
- [Step 2: Setup User Account in WSL2](#step-2-setup-user-account-in-wsl2)
- [Step 3: Install Node.js](#step-3-install-nodejs)
- [Step 4: Install Podman](#step-4-install-podman)
- [Step 5: Install VS Code in WSL2](#step-5-install-vs-code-in-wsl2)
- [Step 6: Install Claude Code Extension in VS Code](#step-6-install-claude-code-extension-in-vs-code)
- [Step 7: Configure VS Code for Podman (Optional)](#step-7-configure-vs-code-for-podman-optional)
- [Step 8: Create Project Structure](#step-8-create-project-structure)
- [Final Workflow Summary](#final-workflow-summary)
  - [Your Development Environment:](#your-development-environment)
  - [Daily Workflow:](#daily-workflow)
  - [Key Commands:](#key-commands)
- [Troubleshooting](#troubleshooting)
- [Next Steps](#next-steps)


### Alterntaive Workflow Setup: VS Code + Claude Code + Podman on WSL2 (Windows 10 Pro)

>[!WARN]
>This is complex no container option

## Overview
Setting up a development environment with VS Code, Claude Code extension, and Podman containers - all running in WSL2 on Windows 10 Pro.

---

## Step 1: Enable WSL2

**Run PowerShell as Administrator:**
```powershell
# Install WSL2
wsl --install

# Set WSL2 as default
wsl --set-default-version 2

# Install Ubuntu
wsl --install -d Ubuntu

# Restart computer if prompted
```

---

## Step 2: Setup User Account in WSL2

**Launch Ubuntu from Start Menu, then:**
```bash
# Switch to existing user
su - dbjdbj

# Verify you're logged in as dbjdbj
whoami
```

---

## Step 3: Install Node.js

**Option A: Using nvm (recommended):**
```bash
# Install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Reload shell
source ~/.bashrc

# Install Node.js LTS
nvm install --lts
nvm use --lts

# Verify
node --version
npm --version
```

**Option B: Using apt:**
```bash
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
node --version
npm --version
```

---

## Step 4: Install Podman

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Podman
sudo apt install podman -y

# Verify installation
podman --version

# Optional: Create Docker alias
echo "alias docker=podman" >> ~/.bashrc
source ~/.bashrc

# Enable Podman socket (Docker-compatible)
systemctl --user enable --now podman.socket

# Test Podman
podman run hello-world
```

**Optional: Install Podman Compose:**
```bash
sudo apt install podman-compose -y
```

---

## Step 5: Install VS Code in WSL2

**Option A: Using snap (easiest):**
```bash
sudo snap install code --classic
```

**Option B: Using apt:**
```bash
# Add Microsoft GPG key and repository
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
rm -f packages.microsoft.gpg

# Install
sudo apt update
sudo apt install code -y
```

**Verify:**
```bash
code --version
```

---

## Step 6: Install Claude Code Extension in VS Code

```bash
# Launch VS Code
code .

# In VS Code:
# 1. Press Ctrl+Shift+X (Extensions)
# 2. Search for "Claude Code"
# 3. Click Install

# OR install via command line:
code --install-extension anthropic.claude-code
```

---

## Step 7: Configure VS Code for Podman (Optional)

**Create/edit settings in VS Code:**
```json
// File: ~/.config/Code/User/settings.json or workspace .vscode/settings.json
{
  "docker.dockerPath": "podman",
  "docker.host": "unix:///run/user/1000/podman/podman.sock"
}
```

**Install Docker extension (works with Podman):**
```bash
code --install-extension ms-azuretools.vscode-docker
```

---

## Step 8: Create Project Structure

```bash
# Create projects directory
mkdir -p ~/projects/clarendon-landing
cd ~/projects/clarendon-landing

# Initialize project
npm init -y

# Launch VS Code
code .
```

---

## Final Workflow Summary

### Your Development Environment:
- **OS Layer:** Windows 10 Pro → WSL2 (Ubuntu)
- **User:** dbjdbj
- **Code Editor:** VS Code (native in WSL2)
- **AI Assistant:** Claude Code extension (powered by Node.js)
- **Container Runtime:** Podman
- **Projects Location:** `~/projects/`

### Daily Workflow:
1. Open Windows Terminal or Ubuntu app
2. Login as `dbjdbj` (if not automatic)
3. Navigate to project: `cd ~/projects/your-project`
4. Launch VS Code: `code .`
5. Use Claude Code extension for AI-assisted development
6. Run containers with Podman commands in terminal
7. All tools integrated in one environment

### Key Commands:
```bash
# Start VS Code
code .

# Run Podman containers
podman run -d -p 8080:80 nginx
podman ps
podman-compose up -d

# Check Node.js
node --version

# Access from Windows
# Files: \\wsl$\Ubuntu\home\dbjdbj\projects
# Browser: localhost:8080 (for Podman containers)
```

---

## Troubleshooting

**VS Code won't start:**
```bash
code --verbose
```

**Podman socket issues:**
```bash
systemctl --user status podman.socket
systemctl --user restart podman.socket
```

**Node.js not found:**
```bash
source ~/.bashrc
nvm use --lts
```

**Can't access files from Windows:**
- Use `\\wsl$\Ubuntu\home\dbjdbj\` in Windows Explorer
- Or use VS Code Remote Explorer

---

## Next Steps

Once setup is complete, you can:
1. Build the Clarendon Global landing page
2. Use Claude Code to assist with development
3. Run the site in Podman containers
4. Access everything from Windows browser at `localhost`

---

**Document Version:** 1.0  
**Date:** October 29, 2025  
**Target System:** Windows 10 Pro + WSL2 + Ubuntu