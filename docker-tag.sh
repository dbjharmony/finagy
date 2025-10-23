#!/bin/bash

# Docker Tagging Helper Script for Finagy
# Usage: ./docker-tag.sh [tag-type] [container-id]

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to show usage
show_usage() {
    echo "Docker Tagging Helper for Finagy"
    echo ""
    echo "Usage: $0 [tag-type] [container-id]"
    echo ""
    echo "Tag Types:"
    echo "  dev        - Development build with date"
    echo "  feature    - Feature build with branch name"
    echo "  commit     - Build with git commit hash"
    echo "  release    - Release build (requires version)"
    echo "  custom     - Custom tag (requires custom name)"
    echo ""
    echo "Examples:"
    echo "  $0 dev abc123def456"
    echo "  $0 feature abc123def456"
    echo "  $0 commit abc123def456"
    echo "  $0 release abc123def456 v0.1.0"
    echo "  $0 custom abc123def456 my-custom-tag"
    echo ""
    echo "To get container ID:"
    echo "  docker ps -a"
}

# Function to get current git branch
get_git_branch() {
    git branch --show-current 2>/dev/null || echo "unknown"
}

# Function to get git commit hash
get_git_commit() {
    git rev-parse --short HEAD 2>/dev/null || echo "unknown"
}

# Function to get current date
get_date() {
    date +%Y%m%d
}

# Function to get current datetime
get_datetime() {
    date +%Y%m%d-%H%M
}

# Main tagging function
tag_container() {
    local tag_type="$1"
    local container_id="$2"
    local custom_tag="$3"
    
    if [ -z "$container_id" ]; then
        print_error "Container ID is required"
        show_usage
        exit 1
    fi
    
    # Check if container exists
    if ! docker ps -a --format "table {{.ID}}" | grep -q "^${container_id}$"; then
        print_error "Container $container_id not found"
        exit 1
    fi
    
    local tag=""
    local commit_cmd=""
    
    case "$tag_type" in
        "dev")
            tag="finagy:dev-$(get_date)"
            commit_cmd="docker commit $container_id $tag"
            print_info "Creating development build with date: $tag"
            ;;
        "feature")
            local branch=$(get_git_branch)
            tag="finagy:feature-${branch}"
            commit_cmd="docker commit $container_id $tag"
            print_info "Creating feature build for branch '$branch': $tag"
            ;;
        "commit")
            local commit_hash=$(get_git_commit)
            tag="finagy:commit-${commit_hash}"
            commit_cmd="docker commit $container_id $tag"
            print_info "Creating commit build: $tag"
            ;;
        "release")
            if [ -z "$custom_tag" ]; then
                print_error "Release tag requires version (e.g., v0.1.0)"
                exit 1
            fi
            tag="finagy:release-${custom_tag}"
            commit_cmd="docker commit $container_id $tag"
            print_info "Creating release build: $tag"
            ;;
        "custom")
            if [ -z "$custom_tag" ]; then
                print_error "Custom tag requires a name"
                exit 1
            fi
            tag="finagy:${custom_tag}"
            commit_cmd="docker commit $container_id $tag"
            print_info "Creating custom build: $tag"
            ;;
        *)
            print_error "Unknown tag type: $tag_type"
            show_usage
            exit 1
            ;;
    esac
    
    # Execute the commit
    print_info "Executing: $commit_cmd"
    if eval "$commit_cmd"; then
        print_success "Successfully created image: $tag"
        
        # Also tag as latest for dev builds
        if [ "$tag_type" = "dev" ]; then
            docker tag "$tag" "finagy:dev-latest"
            print_success "Also tagged as: finagy:dev-latest"
        fi
        
        # Show image info
        print_info "Image details:"
        docker images | grep "finagy" | head -5
    else
        print_error "Failed to create image"
        exit 1
    fi
}

# Main execution
if [ $# -lt 2 ]; then
    show_usage
    exit 1
fi

tag_container "$1" "$2" "$3"
