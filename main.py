
import os
import sys

# ANSI colors and styles
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Translation dictionaries:
# Add as many languages as you want by adding dictionaries here.
# Keys are strings like "main_title", "quit", etc.
TRANSLATIONS = {
    "en": {
        "main_title": "MULTI TOOL - Developer's Edition",
        "select_category": "Select a category",
        "select_option": "Select an option",
        "go_back_quit": "Go Back / Quit",
        "quit": "Quit",
        "invalid_choice": "Invalid choice.",
        "press_enter": "Press Enter to continue...",
        "no_package": "No package specified.",
        "no_name": "No name specified.",
        "no_script": "No script name specified.",
        "dev_info_title": "Developer Info",
        "dev_tool_name": "Tool Name: Multi Tool - Developer's Edition",
        "dev_version": "Version: 2.0.0",
        "dev_author": "Author: Sprite Developments",
        "dev_desc": "Description: A comprehensive developer utility tool covering Python, Node.js, Docker, Git, and multiple other ecosystems, with multilingual support.",
        "enter_package_to_install": "Enter the package name to install:",
        "enter_package_to_uninstall": "Enter the package name to uninstall:",
        "enter_package_to_search": "Enter the package name to search:",
        "enter_venv_name": "Enter the virtual environment name:",
        "enter_venv_to_activate": "Enter the virtual environment name to activate:",
        "enter_script_name": "Enter the script name:",
        "enter_image_name": "Enter Docker image to run:",
        "enter_filename": "Enter filename to edit:",
        "choose_language": "Choose your language:",
        "env_variables": "Environment Variables:",
        "languages_available": ["English", "Español", "Français"],
    },
    "es": {
        "main_title": "HERRAMIENTA MÚLTIPLE - Edición para Desarrolladores",
        "select_category": "Seleccione una categoría",
        "select_option": "Seleccione una opción",
        "go_back_quit": "Volver / Salir",
        "quit": "Salir",
        "invalid_choice": "Opción inválida.",
        "press_enter": "Presione Enter para continuar...",
        "no_package": "No se especificó ningún paquete.",
        "no_name": "No se especificó ningún nombre.",
        "no_script": "No se especificó ningún nombre de script.",
        "dev_info_title": "Información del Desarrollador",
        "dev_tool_name": "Nombre de la herramienta: Herramienta Múltiple - Edición Desarrolladores",
        "dev_version": "Versión: 2.0.0",
        "dev_author": "Autor: Sprite Developments",
        "dev_desc": "Descripción: Una herramienta integral para desarrolladores que cubre Python, Node.js, Docker, Git y otros ecosistemas, con soporte multilingüe.",
        "enter_package_to_install": "Ingrese el nombre del paquete a instalar:",
        "enter_package_to_uninstall": "Ingrese el nombre del paquete a desinstalar:",
        "enter_package_to_search": "Ingrese el nombre del paquete a buscar:",
        "enter_venv_name": "Ingrese el nombre del entorno virtual:",
        "enter_venv_to_activate": "Ingrese el nombre del entorno virtual a activar:",
        "enter_script_name": "Ingrese el nombre del script:",
        "enter_image_name": "Ingrese la imagen de Docker a ejecutar:",
        "enter_filename": "Ingrese el nombre del archivo para editar:",
        "choose_language": "Elija su idioma:",
        "env_variables": "Variables de Entorno:",
        "languages_available": ["English", "Español", "Français"],
    },
    "fr": {
        "main_title": "OUTIL MULTIPLE - Édition Développeur",
        "select_category": "Sélectionnez une catégorie",
        "select_option": "Sélectionnez une option",
        "go_back_quit": "Retour / Quitter",
        "quit": "Quitter",
        "invalid_choice": "Choix invalide.",
        "press_enter": "Appuyez sur Entrée pour continuer...",
        "no_package": "Aucun package spécifié.",
        "no_name": "Aucun nom spécifié.",
        "no_script": "Aucun nom de script spécifié.",
        "dev_info_title": "Informations sur le Développeur",
        "dev_tool_name": "Nom de l'outil: Outil Multiple - Édition Développeur",
        "dev_version": "Version: 2.0.0",
        "dev_author": "Auteur: Sprite Developments",
        "dev_desc": "Description: Un outil complet pour les développeurs couvrant Python, Node.js, Docker, Git et de nombreux autres écosystèmes, avec support multilingue.",
        "enter_package_to_install": "Entrez le nom du package à installer:",
        "enter_package_to_uninstall": "Entrez le nom du package à désinstaller:",
        "enter_package_to_search": "Entrez le nom du package à rechercher:",
        "enter_venv_name": "Entrez le nom de l'environnement virtuel:",
        "enter_venv_to_activate": "Entrez le nom de l'environnement virtuel à activer:",
        "enter_script_name": "Entrez le nom du script:",
        "enter_image_name": "Entrez l'image Docker à exécuter:",
        "enter_filename": "Entrez le nom du fichier à éditer:",
        "choose_language": "Choisissez votre langue:",
        "env_variables": "Variables d'environnement:",
        "languages_available": ["English", "Español", "Français"],
    }
    # Add more language dictionaries here...
}


current_lang = "en"

def t(key):
    """Translate a given key based on the current language."""
    return TRANSLATIONS[current_lang].get(key, key)

def dummy_command(description):
    print(f"\n{GREEN}{t('Executing')}{RESET} {description}")
    input(t("press_enter"))

def run_shell_command(cmd):
    print(f"\n{GREEN}Running shell command:{RESET} {cmd}")
    os.system(cmd)
    input(t("press_enter"))

def pip_install_package():
    package = input(t("enter_package_to_install") + " ")
    if package.strip():
        run_shell_command(f"pip install {package}")
    else:
        print(t("no_package"))
        input(t("press_enter"))

def pip_uninstall_package():
    package = input(t("enter_package_to_uninstall") + " ")
    if package.strip():
        run_shell_command(f"pip uninstall {package} -y")
    else:
        print(t("no_package"))
        input(t("press_enter"))

def pip_list_packages():
    run_shell_command("pip list")

def pip_freeze_requirements():
    run_shell_command("pip freeze > requirements.txt")
    print("requirements.txt updated.")
    input(t("press_enter"))

def node_install_package():
    package = input(t("enter_package_to_install") + " ")
    if package.strip():
        run_shell_command(f"npm install {package}")
    else:
        print(t("no_package"))
        input(t("press_enter"))

def node_global_install():
    package = input(t("enter_package_to_install") + " ")
    if package.strip():
        run_shell_command(f"npm install -g {package}")
    else:
        print(t("no_package"))
        input(t("press_enter"))

def show_env_vars():
    print("\n" + t("env_variables"))
    for k, v in os.environ.items():
        print(f"{k}={v}")
    input(t("press_enter"))

def create_virtualenv():
    env_name = input(t("enter_venv_name") + " ")
    if env_name.strip():
        run_shell_command(f"python -m venv {env_name}")
    else:
        print(t("no_name"))
        input(t("press_enter"))

def activate_virtualenv():
    env_name = input(t("enter_venv_to_activate") + " ")
    if env_name.strip():
        if os.name == 'nt':
            print(f"Run: {env_name}\\Scripts\\activate")
        else:
            print(f"Run: source {env_name}/bin/activate")
    else:
        print(t("no_name"))
    input(t("press_enter"))

def run_python_script():
    script_name = input(t("enter_script_name") + " ")
    if script_name.strip():
        run_shell_command(f"python {script_name}")
    else:
        print(t("no_script"))
        input(t("press_enter"))

def git_status():
    run_shell_command("git status")

def git_pull():
    run_shell_command("git pull")

def git_push():
    run_shell_command("git push")

def docker_ps():
    run_shell_command("docker ps")

def docker_images():
    run_shell_command("docker images")

def docker_run():
    image = input(t("enter_image_name") + " ")
    if image.strip():
        run_shell_command(f"docker run -it {image}")
    else:
        print(t("no_name"))
        input(t("press_enter"))

def format_python_with_black():
    run_shell_command("black .")

def lint_python_with_flake8():
    run_shell_command("flake8 .")

def test_python_with_pytest():
    run_shell_command("pytest")

def npm_run_build():
    run_shell_command("npm run build")

def npm_run_dev():
    run_shell_command("npm run dev")

def npm_run_test():
    run_shell_command("npm test")

def yarn_add_package():
    package = input(t("enter_package_to_install") + " ")
    if package.strip():
        run_shell_command(f"yarn add {package}")
    else:
        print(t("no_package"))
        input(t("press_enter"))

def show_python_version():
    run_shell_command("python --version")

def show_pip_version():
    run_shell_command("pip --version")

def show_node_version():
    run_shell_command("node --version")

def show_npm_version():
    run_shell_command("npm --version")

def show_yarn_version():
    run_shell_command("yarn --version")

def whoami():
    run_shell_command("whoami")

def list_dir():
    run_shell_command("dir" if os.name == 'nt' else "ls")

def edit_file_with_vim():
    filename = input(t("enter_filename") + " ")
    if filename.strip():
        run_shell_command(f"vim {filename}")
    else:
        print(t("no_name"))
        input(t("press_enter"))

def python_help():
    run_shell_command("python -h")

def pip_search():
    package = input(t("enter_package_to_search") + " ")
    if package.strip():
        run_shell_command(f"pip search {package}")
    else:
        print(t("no_package"))
        input(t("press_enter"))

def npm_search():
    package = input(t("enter_package_to_search") + " ")
    if package.strip():
        run_shell_command(f"npm search {package}")
    else:
        print(t("no_package"))
        input(t("press_enter"))

def open_python_shell():
    print("Launching an interactive Python shell (type exit() or Ctrl-D to quit):")
    os.system("python")
    input(t("press_enter"))

def generate_requirements_txt():
    run_shell_command("pip freeze > requirements.txt")
    print("requirements.txt generated.")
    input(t("press_enter"))

def upgrade_pip():
    run_shell_command("python -m pip install --upgrade pip")

def clear_screen():
    os.system("cls" if os.name == 'nt' else "clear")

def exit_program():
    print("Exiting program. Goodbye!")
    sys.exit(0)

def show_developer_info():
    clear_screen()
    print(f"{BOLD}{YELLOW}{t('dev_info_title')}{RESET}\n")
    print(t("dev_tool_name"))
    print(t("dev_version"))
    print(t("dev_author"))
    print(t("dev_desc"))
    input("\n" + t("press_enter"))

# Additional languages/ecosystem commands (dummy placeholders)
def java_maven_build():
    run_shell_command("mvn clean install")

def java_maven_test():
    run_shell_command("mvn test")

def ruby_gem_install():
    package = input(t("enter_package_to_install") + " ")
    if package.strip():
        run_shell_command(f"gem install {package}")
    else:
        print(t("no_package"))
        input(t("press_enter"))

def php_composer_install():
    run_shell_command("composer install")

def go_get_package():
    package = input(t("enter_package_to_install") + " ")
    if package.strip():
        run_shell_command(f"go get {package}")
    else:
        print(t("no_package"))
        input(t("press_enter"))

def rust_cargo_build():
    run_shell_command("cargo build")

def csharp_dotnet_run():
    run_shell_command("dotnet run")

def cpp_build():
    run_shell_command("make")

# Add as many languages (programming languages) and commands as needed.
MAIN_MENU = {
    "Python & pip": [
        ("Install a pip package", pip_install_package),
        ("Uninstall a pip package", pip_uninstall_package),
        ("List installed pip packages", pip_list_packages),
        ("Freeze requirements to file", pip_freeze_requirements),
        ("Search for a pip package", pip_search),
        ("Upgrade pip", upgrade_pip),
        ("Create Python virtual environment", create_virtualenv),
        ("Instructions to activate virtualenv", activate_virtualenv),
        ("Run a Python script", run_python_script),
        ("Show Python version", show_python_version),
        ("Show pip version", show_pip_version),
        ("Open Python interactive shell", open_python_shell),
        ("Generate requirements.txt", generate_requirements_txt),
        ("Get Python help", python_help),
    ],
    "Node.js & NPM": [
        ("Install an npm package locally", node_install_package),
        ("Install an npm package globally", node_global_install),
        ("Search for an npm package", npm_search),
        ("Run npm build script", npm_run_build),
        ("Run npm dev script", npm_run_dev),
        ("Run npm test script", npm_run_test),
        ("Show Node.js version", show_node_version),
        ("Show npm version", show_npm_version),
    ],
    "Yarn & Node Tools": [
        ("Yarn add a package", yarn_add_package),
        ("Show yarn version", show_yarn_version),
    ],
    "Git": [
        ("Git status", git_status),
        ("Git pull", git_pull),
        ("Git push", git_push),
    ],
    "Docker": [
        ("List Docker containers", docker_ps),
        ("List Docker images", docker_images),
        ("Run a Docker container", docker_run),
    ],
    "Java & Maven": [
        ("Maven build (clean install)", java_maven_build),
        ("Maven test", java_maven_test),
    ],
    "Ruby & Gems": [
        ("Install a Gem package", ruby_gem_install),
    ],
    "PHP & Composer": [
        ("Composer install", php_composer_install),
    ],
    "Go & Modules": [
        ("go get a package", go_get_package),
    ],
    "Rust & Cargo": [
        ("Cargo build", rust_cargo_build),
    ],
    "C# & .NET": [
        ("dotnet run", csharp_dotnet_run),
    ],
    "C++ & Build Tools": [
        ("Build with make", cpp_build),
    ],
    "Code Quality": [
        ("Format Python code with Black", format_python_with_black),
        ("Lint Python code with flake8", lint_python_with_flake8),
        ("Test Python code with pytest", test_python_with_pytest),
    ],
    "System & Utilities": [
        ("Show environment variables", show_env_vars),
        ("List directory contents", list_dir),
        ("Open file in vim editor", edit_file_with_vim),
        ("Who am I?", whoami),
        ("Clear screen", clear_screen),
    ],
    "About / Developer Info": [
        ("Show Developer Info", show_developer_info),
    ]
}


def choose_language():
    global current_lang
    clear_screen()
    print(BOLD + YELLOW + t("choose_language") + RESET + "\n")
    langs = TRANSLATIONS["en"]["languages_available"]  # Using English to list languages
    # For demonstration: index them and allow user to choose which dictionary to load.
    for i, lang_name in enumerate(langs, start=1):
        print(f"[{i}] {lang_name}")
    print("[q] " + t("quit"))
    choice = input("\n" + t("select_option") + ": ").strip().lower()
    if choice == 'q':
        exit_program()
    else:
        if choice.isdigit():
            idx = int(choice) - 1
            if idx == 0:
                current_lang = "en"
            elif idx == 1:
                current_lang = "es"
            elif idx == 2:
                current_lang = "fr"
            # Add more languages as elif clauses once you define them in TRANSLATIONS
        else:
            # Default to English if invalid
            current_lang = "en"


def show_menu(title, options):
    clear_screen()
    print(f"{BOLD}{YELLOW}{title}{RESET}\n")
    for i, (desc, _) in enumerate(options, start=1):
        print(f"[{i}] {desc}")
    print("[q] " + t("go_back_quit"))
    choice = input("\n" + t("select_option") + ": ").strip().lower()
    return choice

def handle_menu(options):
    while True:
        choice = show_menu(t("select_option"), options)
        if choice == 'q':
            return
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                fn = options[idx][1]
                fn()
            else:
                print(t("invalid_choice"))
                input(t("press_enter"))
        else:
            print(t("invalid_choice"))
            input(t("press_enter"))

def show_main_menu():
    while True:
        clear_screen()
        print(f"{BOLD}{RED}{t('main_title')}{RESET}\n")
        categories = list(MAIN_MENU.keys())
        for i, cat in enumerate(categories, start=1):
            print(f"[{i}] {cat}")
        print("[q] " + t("quit"))
        choice = input("\n" + t("select_category") + ": ").strip().lower()
        if choice == 'q':
            exit_program()
        elif choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(categories):
                handle_menu(MAIN_MENU[categories[idx]])
            else:
                print(t("invalid_choice"))
                input(t("press_enter"))
        else:
            print(t("invalid_choice"))
            input(t("press_enter"))

if __name__ == "__main__":
    choose_language()  # Ask user for language at startup
    show_main_menu()
