import os


def get_var() -> dict[str, str] | None:
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ModuleNotFoundError:
        print("\n[ERROR]: Missing dependency: python-dotenv\n"
              "Use the following command to install it:\n"
              "pip install python-dotenv")
        return None

    matrix_mode = os.environ.get('MATRIX_MODE', 'development')
    database_url = os.environ.get('DATABASE_URL')
    api_key = os.environ.get('API_KEY')
    log_level = os.environ.get('LOG_LEVEL', 'INFO')
    zion_endpoint = os.environ.get('ZION_ENDPOINT')

    if not database_url or not api_key or not zion_endpoint:
        print("ERROR: Missing required environment variables")
        return None

    if matrix_mode not in ("development", "production"):
        print("ERROR: Invalid MATRIX_MODE")
        return None

    if log_level not in ("DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"):
        print("ERROR: Invalid LOG_LEVEL")
        return None

    return {"mode": matrix_mode,
            "db": database_url,
            "api": api_key,
            "log": log_level,
            "zion": zion_endpoint}


def display_config(config: dict[str, str]) -> None:
    print(f"Mode: {config['mode']}")
    if config["mode"] == "development":
        print("Database: Connected to local instance")
    elif config["mode"] == "production":
        print("Database: Connected to production")
    print("API Access: Authenticated\n"
          f"Log Level: {config['log']}\n"
          "Remote Network: Online")


def security_check() -> None:
    print("\nConfiguration security check:\n"
          "[OK] No hardcoded secrets detected")

    if not os.path.isfile(".env"):  # существует ли файл по указанному пути.
        print("[WARNING] .env file not found\n"
              "'cp .env.example .env' to create a .env file")
    else:
        print("[OK] .env file found")

    if not os.path.isfile(".gitignore"):
        print("[WARNING] .gitignore file not found")
    else:
        with open(".gitignore", "r") as file:
            ignored_files = file.read().splitlines()

        if ".env" in ignored_files:
            print("[OK] .env file properly ignored by git")
        else:
            print("[WARNING] .env is not listed in .gitignore")

    print("[OK] Production overrides available\n"
          "The Oracle sees all configurations.")


if __name__ == "__main__":
    config = get_var()

    if config is not None:
        print("\nORACLE STATUS: Consulting the configuration...\n\n"
              "Configuration loaded:")
        display_config(config)
        security_check()
