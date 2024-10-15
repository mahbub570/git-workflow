import os

# Define expected languages and data types
expected_languages = {
    "Arabic", "English", "Greek", "Italian", "Malayalam", "Russian", "Tamil",
    "Basque", "Esperanto", "Hausa", "Japanese", "Norwegian", "Slovak", "Ukrainian",
    "Bengali", "Estonian", "Hebrew", "Korean", "Pidgin", "Spanish", "Yoruba",
    "Chinese", "Finnish", "Hindustani", "Kurmanji", "Polish", "Swahili",
    "Czech", "French", "Indonesian", "Latin", "Portuguese", "Swedish",
    "Danish", "German", "Malay", "Punjabi", "Tajik"
}

expected_data_types = {
    "adjectives", "adverbs", "articles", "autosuggestions", "conjunctions",
    "emoji_keywords", "nouns", "personal_pronouns", "postpositions",
    "prepositions", "pronouns", "proper_nouns", "verbs"
}

# Define expected sub-subdirectories for specific languages
sub_sub_dirs = {
    'Chinese': ['Mandarin'],
    'Hindustani': ['Urdu', 'Hindi'],  # Hindustani includes Hindi and Urdu
    'Norwegian': ['Nynorsk', 'Bokmål'],
    'Pidgin': ['Nigerian'],
    'Punjabi': ['Shahmukhi', 'Gurmukhi']
}

# Base directory path
base_dir = "language_data_extraction"

# Function to validate language and data-type directories
def validate_directories():
    errors = []

    # Check if the base directory exists
    if not os.path.exists(base_dir):
        print(f"Error: Base directory '{base_dir}' does not exist.")
        return

    # Iterate through the language directories
    for lang in os.listdir(base_dir):
        lang_path = os.path.join(base_dir, lang)

        # Skip non-directories or __init__.py files
        if not os.path.isdir(lang_path) or lang == "__init__.py":
            continue

        # Check for unexpected language directories
        if lang not in expected_languages:
            errors.append(f"Unexpected language directory: {lang}")
            continue

        # Validate data-type subdirectories within each language
        subdirs = set(
            item for item in os.listdir(lang_path) 
            if os.path.isdir(os.path.join(lang_path, item)) and item != "__init__.py"
        )

        # Separate validation for languages with sub-subdirectories
        if lang in sub_sub_dirs:
            expected_subdirs = set(sub_sub_dirs[lang])
            unexpected_subdirs = subdirs - expected_subdirs

            # Check for unexpected sub-subdirectories
            if unexpected_subdirs:
                errors.append(f"Unexpected sub-subdirectories in '{lang}': {unexpected_subdirs}")

            # Check if any expected sub-subdirectories are missing
            missing_subdirs = expected_subdirs - subdirs
            if missing_subdirs:
                errors.append(f"Missing sub-subdirectories in '{lang}': {missing_subdirs}")

        else:
            # Validate data-type subdirectories for languages without sub-subdirectories
            unexpected_subdirs = subdirs - expected_data_types

            if unexpected_subdirs:
                errors.append(f"Unexpected subdirectories in '{lang}': {unexpected_subdirs}")

    # Report errors
    if errors:
        print("Errors found:")
        for error in errors:
            print(f" - {error}")
        exit(1)  # Exit with a non-zero status to indicate failure
    else:
        print("All directories are correctly named and organized.")

# Run the validation
validate_directories()
