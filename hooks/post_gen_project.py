import shutil
import subprocess


def update_precommit_hooks():
    """Update pre-commit hooks to latest versions."""
    # Check if uvx is available
    if not shutil.which("uvx"):
        print("⚠️  Warning: uvx not found. Install UV first to update pre-commit hooks.")
        return

    try:
        print("🔄 Updating pre-commit hooks to latest versions...")
        result = subprocess.run(  # noqa: S603
            [shutil.which("uvx"), "pre-commit", "autoupdate"],
            capture_output=True,
            text=True,
            check=True,
        )
        print("✅ Pre-commit hooks updated successfully!")
        if result.stdout:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Warning: Could not update pre-commit hooks: {e}")
        print("You can update them later by running: uvx pre-commit autoupdate")


def main():
    """Post-generation project setup."""
    print("🎉 Setting up your new project...")

    # Update pre-commit hooks to latest versions
    update_precommit_hooks()

    print("\n✨ Project setup complete!")
    print("\nNext steps:")
    print("1. Create a GitHub repo with the name {{ cookiecutter.project_slug }}")
    print("2. Go to Settings -> Pages -> Build and deployment -> Source and choose GitHub Actions")
    print("3. Run: make")


if __name__ == "__main__":
    main()
