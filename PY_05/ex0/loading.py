def check_library() -> None:
    all_available: bool = True

    try:
        import numpy
        print(f"[OK] numpy {numpy.__version__} - Numerical computation ready")
    except ModuleNotFoundError as error:
        if error.name == "numpy":
            print("[MISSING] numpy\n"
                  "To install it use:\n"
                  "pip install numpy\n"
                  "  or\n"
                  "poetry add numpy")
            all_available = False
        else:
            print(f"[ERROR] numpy: missing dependency {error.name}")
            all_available = False
    except ImportError as error:
        print(f"[ERROR] numpy: {error}")
        all_available = False

    try:
        import pandas
        print(f"[OK] pandas {pandas.__version__} - Data manipulation ready")
    except ModuleNotFoundError as error:
        if error.name == "pandas":
            print("\n[MISSING] pandas\n"
                  "To install it use:\n"
                  "pip install pandas\n"
                  "  or\n"
                  "poetry add pandas")
            all_available = False
        else:
            print(f"[ERROR] pandas: missing dependency {error.name}")
            all_available = False
    except ImportError as error:
        print(f"[ERROR] pandas: {error}")
        all_available = False

    print("\npip vs Poetry:\n"
          "  requirements.txt declares what to install; "
          "pip resolves it at install time.\n"
          "  pyproject.toml declares the same constraints, "
          "and Poetry pins the resolved\n"
          "  versions in poetry.lock so every install is identical.")

    if all_available:
        print("\nAll reagents present and accounted for.")


if __name__ == "__main__":
    print("\nREAGENT STATUS: Loading reagents...\n\n"
          "Checking dependencies:")
    check_library()

'''
Если самого pandas нет — получишь [MISSING].
Если pandas установлен, но не может загрузить зависимость — получишь [ERROR].
Если всё хорошо — получишь [OK].

        Действие	  | pip	                            | Poetry
Уст-ть	              | pip install numpy	            | poetry add numpy
Удалить	              | pip uninstall numpy	            | poetry remove numpy
Уст-ть зав-и из файла | pip install -r requirements.txt | poetry install
Пос-ть уст-ые пакеты  | pip list	                    | poetry show
'''
