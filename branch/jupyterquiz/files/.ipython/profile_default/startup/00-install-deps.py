"""
Auto-install Python packages from requirements.txt at kernel startup.
This script runs automatically when the Pyodide kernel starts.
"""
import sys

async def install_requirements():
    """Install packages from requirements.txt if it exists."""
    try:
        import micropip
        from pathlib import Path
        
        # Look for requirements.txt in the current directory
        req_file = Path('requirements.txt')
        
        if req_file.exists():
            print("📦 Found requirements.txt, installing packages...")
            content = req_file.read_text()
            
            # Parse requirements (skip empty lines and comments)
            requirements = []
            for line in content.strip().split('\n'):
                line = line.strip()
                if line and not line.startswith('#'):
                    requirements.append(line)
            
            if requirements:
                print(f"   Installing: {', '.join(requirements)}")
                await micropip.install(requirements)
                print("✅ All packages installed successfully!")
            else:
                print("   No packages found in requirements.txt")
        else:
            print("ℹ️  No requirements.txt found, skipping package installation")
            
    except Exception as e:
        print(f"⚠️  Warning: Could not install packages from requirements.txt: {e}", file=sys.stderr)

# Run the installation
await install_requirements()
