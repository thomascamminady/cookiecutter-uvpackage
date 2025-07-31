def main():
    """Post-generation project setup."""
    print("🎉 Setting up your new project...")
    print("\n✨ Project setup complete!")
    print("\nNext steps:")
    print("1. Create a GitHub repo with the name {{ cookiecutter.project_slug }}")
    print("2. Go to Settings -> Pages -> Build and deployment -> Source and choose GitHub Actions")
    print("3. Run: make")


if __name__ == "__main__":
    main()
