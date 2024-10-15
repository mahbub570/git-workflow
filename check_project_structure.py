import os

# Expected languages and data types
LANGUAGES = {
    "Arabic", "English", "Greek", "Italian", "Malayalam", "Russian", "Tamil",
    "Basque", "Esperanto", "Hausa", "Japanese", "Norwegian", "Slovak", "Ukrainian",
    "Bengali", "Estonian", "Hebrew", "Korean", "Pidgin", "Spanish", "Yoruba",
    "Chinese", "Finnish", "Hindustani", "Kurmanji", "Polish", "Swahili",
    "Czech", "French", "Indonesian", "Latin", "Portuguese", "Swedish",
    "Danish", "German", "Malay", "Punjabi", "Tajik"
}

DATA_TYPES = {
    "adjectives", "adverbs", "articles", "autosuggestions", "conjunctions",
    "emoji_keywords", "nouns", "personal_pronouns", "postpositions",
    "prepositions", "pronouns", "proper_nouns", "verbs"
}

# Sub-subdirectories expected for specific languages
SUB_DIRECTORIES = {
    'Chinese': ['Mandarin'],
    'Hindustani': ['Urdu', 'Hindi'],
    'Norwegian': ['Nynorsk', 'Bokmål'],
    'Pidgin': ['Nigerian'],
    'Punjabi': ['Shahmukhi', 'Gurmukhi']
}

# Base directory path
BASE_DIR = "language_data_extraction"

def validate_project_structure():
    """Validate that all directories follow the expected project structure."""
    errors = []

    # Check if the base directory exists
    if not os.path.exists(BASE_DIR):
        print(f"Error: Base directory '{BASE_DIR}' does not exist.")
        exit(1)

    # Iterate through the language directories
    for language in os.listdir(BASE_DIR):
        language_path = os.path.join(BASE_DIR, language)

        # Skip non-directories or __init__.py files
        if not os.path.isdir(language_path) or language == "__init__.py":
            continue

        # Check if the language directory is unexpected
        if language not in LANGUAGES:
            errors.append(f"Unexpected language directory: {language}")
            continue

        # Collect subdirectories for the current language
        found_subdirs = {
            item for item in os.listdir(language_path) 
            if os.path.isdir(os.path.join(language_path, item)) and item != "__init__.py"
        }

        if language in SUB_DIRECTORIES:
            # Validate sub-subdirectories for specific languages
            expected_subdirs = set(SUB_DIRECTORIES[language])
            unexpected_subdirs = found_subdirs - expected_subdirs
            missing_subdirs = expected_subdirs - found_subdirs

            if unexpected_subdirs:
                errors.append(f"Unexpected sub-subdirectories in '{language}': {unexpected_subdirs}")
            if missing_subdirs:
                errors.append(f"Missing sub-subdirectories in '{language}': {missing_subdirs}")
        else:
            # Validate data-type subdirectories for other languages
            unexpected_data_types = found_subdirs - DATA_TYPES
            if unexpected_data_types:
                errors.append(f"Unexpected subdirectories in '{language}': {unexpected_data_types}")

    # Report errors or confirm success
    if errors:
        print("Errors found:")
        for error in errors:
            print(f" - {error}")
        exit(1)  # Exit with non-zero status to indicate failure
    else:
        print("All directories are correctly named and organized.")

if __name__ == "__main__":
    validate_project_structure()
