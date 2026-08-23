from importlib.metadata import version
import platform

def main():
    print("Python", platform.python_version())
    for package in ("pandas", "numpy", "matplotlib"):
        try: print(package, version(package))
        except Exception: print(package, "NOT INSTALLED")
    print("ENVIRONMENT READY")

if __name__ == "__main__": main()
