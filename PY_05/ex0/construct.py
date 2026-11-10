import sys
import os
import site


def check_if_virtual() -> None:
    if (sys.prefix == sys.base_prefix):
        print("\nLABORATORY STATUS: You are working in the open\n\n"
              f"Current Python: {sys.executable}\n"
              "Virtual Environment: None detected\n\n"
              "WARNING: You are in the global environment!\n"
              "Every reagent you install here leaks into the whole system.\n\n"
              "To seal the laboratory, run:\n"
              "python3 -m venv lab_env\n"
              "source lab_env/bin/activate # On Unix\n"
              "lab_env\\Scripts\\activate # On Windows\n"
              "Then run this program again.")

    else:
        print("\nLABORATORY STATUS: The laboratory is sealed\n\n"
              f"Current Python: {sys.executable}\n"
              f"Virtual Environment: {os.path.basename(sys.prefix)}\n"
              f"Environment Path: {sys.prefix}\n\n"
              "SUCCESS: You are working in an isolated environment!\n"
              "Safe to install reagents without affecting\n"
              "the global system.\n")
        if (site.getsitepackages()):
            print(f"Reagent installation path:\n{site.getsitepackages()[0]}")
        else:
            print('N/A')


if __name__ == "__main__":
    check_if_virtual()
