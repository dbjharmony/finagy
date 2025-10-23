# Development Workflow

## Table of Contents
- [Development Workflow](#development-workflow)
  - [Table of Contents](#table-of-contents)
  - [1. The Workflow](#1-the-workflow)
    - [1.1 Initial Setup (one-time)](#11-initial-setup-one-time)
    - [1.2 Develop inside container](#12-develop-inside-container)
    - [1.3 Commit your progress](#13-commit-your-progress)
    - [1.4 Continue the loop](#14-continue-the-loop)
  - [2. Examples](#2-examples)
    - [Development Builds (with date)](#development-builds-with-date)
    - [Feature Builds (with branch name)](#feature-builds-with-branch-name)
    - [Commit Builds (with git hash)](#commit-builds-with-git-hash)
    - [Release Builds (with version)](#release-builds-with-version)
    - [Custom Builds](#custom-builds)
  - [3. Development Workflow](#3-development-workflow)
  - [4. View Your Images](#4-view-your-images)
  - [5. Best Practices](#5-best-practices)
  - [6. API Key Management](#6-api-key-management)
    - [Setting up API keys in container:](#setting-up-api-keys-in-container)
    - [Using API keys in Node.js:](#using-api-keys-in-nodejs)
  - [7. Troubleshooting](#7-troubleshooting)
    - [Container not found?](#container-not-found)
    - [Script not working?](#script-not-working)
    - [Need to start over?](#need-to-start-over)

## 1. The Workflow

> **GIT** 
> Do maintain the connection to github
> Do maintain it only from one place, in this case container. 
> Do not git the same project from container and from a local folder
> Where do we install git from? 
> It's installed via the ghcr.io/devcontainers/features/git:1 feature specified in the .devcontainer/devcontainer.json.
> The devcontainer.json is the central place for defining the development environment. 
> The features section is specifically for installing tools like Git.
> Current .devcontainer/devcontainer.json already includes Git as a feature
> Right track for a clean, devcontainer.json-driven setup!
---
> Now lets dive into the workflow itself
### 1.1 Initial Setup (one-time)
> Not part of the loop

> In Cursor: Command Palette (Cmd+Shift+P)
> Type: "Dev Containers: Reopen in Container"
> Container will be named "finagy-dev" (as specified in devcontainer.json)
> Everything is pre-configured: Node.js, Git, extensions, workspace
---
> Loop starts here
### 1.2 Develop inside container
```bash
# Inside container
# Set up API keys (copy from Google Keep)
cp env.local.template .env
# Edit .env with your real API keys from Google Keep
nano .env

# Create your Node.js files, test, make changes
# Work on your code, test, iterate
exit  # Exit when done
```

> Do not forget to exit the container before proceeding to 1.3

### 1.3 Commit your progress
```bash
# Check container is stopped
docker ps -a
# Commit (container must be stopped)
./docker-tag.sh dev finagy-dev
```

### 1.4 Continue the loop
```bash
# Start from your committed image (goes back to 1.2)
docker run -it finagy:dev-latest bash
```

> Loop:** After 1.4, the workflow loops to 1.2 (develop inside container)

## 2. Examples

### Development Builds (with date)
```bash
./docker-tag.sh dev finagy-dev
# Creates: finagy:dev-20241220
# Also tags as: finagy:dev-latest
```

### Feature Builds (with branch name)
```bash
./docker-tag.sh feature finagy-dev
# Creates: finagy:feature-funagy_container
```

### Commit Builds (with git hash)
```bash
./docker-tag.sh commit finagy-dev
# Creates: finagy:commit-abc1234
```

### Release Builds (with version)
```bash
./docker-tag.sh release finagy-dev v0.1.0
# Creates: finagy:release-v0.1.0
```

### Custom Builds
```bash
./docker-tag.sh custom finagy-dev my-custom-tag
# Creates: finagy:my-custom-tag
```

## 3. Development Workflow

- **Daily builds:** Use `dev` tag for daily progress
- **Feature branches:** Use `feature` tag for specific features  
- **Milestones:** Use `release` tag for stable versions
- **Experiments:** Use `custom` tag for testing ideas

## 4. View Your Images

```bash
# List all finagy images
docker images | grep finagy

# Remove old images to save space
docker rmi finagy:dev-20241219  # Remove old dev build
```

## 5. Best Practices

- **Commit frequently** - Don't lose your work
- **Use descriptive tags** - Know what each image contains
- **Clean up old images** - Keep your system tidy
- **Backup important builds** - Export images you want to keep

## 6. API Key Management

### Setting up API keys in container:
```bash
# Copy template to .env
cp env.local.template .env

# Edit with your real keys from Google Keep
nano .env

# Verify keys are loaded
echo $OPENAI_API_KEY
echo $FINANCIAL_DATASETS_API_KEY
```

### Using API keys in Node.js:
```javascript
// Load environment variables
require('dotenv').config();

// Access API keys
const openaiKey = process.env.OPENAI_API_KEY;
const financialKey = process.env.FINANCIAL_DATASETS_API_KEY;
```

## 7. Troubleshooting

### Container not found?
```bash
docker ps -a  # List all containers
```

### Script not working?
```bash
chmod +x docker-tag.sh  # Make sure it's executable
```

### Need to start over?
```bash
docker rm finagy-dev  # Remove container
docker run -it --name finagy-dev node:18-bullseye bash  # Start fresh
```
