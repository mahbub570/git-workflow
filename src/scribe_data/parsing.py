import json
import bz2

def load_metadata(metadata_file):
    """Load and flatten the metadata file for easier lookup"""
    with open(metadata_file, 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    # Flatten the nested structure into a QID -> label mapping
    qid_to_label = {}
    for category in metadata.values():
        for item in category.values():
            qid_to_label[item['qid']] = item['label']

    return qid_to_label

def parse_lexeme_dump_with_metadata(lexeme_file, metadata_file, top_n=3):
    # Load the metadata mapping
    qid_to_label = load_metadata(metadata_file)

    lexemes_data = []
    lexeme_count = 0

    # Determine if file is compressed based on extension
    is_compressed = lexeme_file.endswith('.bz2')
    open_func = bz2.open if is_compressed else open

    with open_func(lexeme_file, 'rt', encoding='utf-8') as f:
        # Skip until we find the opening bracket
        for line in f:
            if line.strip() == '[':
                break

        for line in f:
            line = line.strip().rstrip(',')
            if line in (']', ''):
                continue

            try:
                lexeme = json.loads(line)

                lexeme_info = {
                    "lexeme_id": lexeme.get('id', 'No ID available'),
                    "lemma": {
                        "en": lexeme.get('lemmas', {}).get('en', {}).get('value', '')
                    },
                    "forms": [],
                    "translations": {},
                    "senses": []
                }

                # Process forms with metadata lookup
                for form in lexeme.get('forms', []):
                    grammatical_features = form.get('grammaticalFeatures', [])
                    # Convert QIDs to labels where possible
                    feature_labels = [
                        {'qid': qid, 'label': qid_to_label.get(qid, 'Unknown feature')}
                        for qid in grammatical_features
                    ]

                        # {
                        #     'qid': qid,
                        #     'label': qid_to_label.get(qid, 'Unknown feature')
                        # }
                        # for qid in grammatical_features
                    # ]

                    form_data = {
                        "form": form.get('representations', {}).get('en', {}).get('value', ''),
                        "grammatical_features": feature_labels
                    }
                    lexeme_info["forms"].append(form_data)

                # Process translations and senses
                for sense in lexeme.get('senses', []):
                    glosses = sense.get('glosses', {})
                    translations = {
                        lang: gloss_data.get('value', '')
                        for lang, gloss_data in glosses.items()
                    }
                    lexeme_info["translations"] = translations

                    sense_data = {
                        "gloss": next(iter(glosses.values()), {}).get('value', ''),
                        "translations": translations
                    }
                    lexeme_info["senses"].append(sense_data)

                lexemes_data.append(lexeme_info)
                lexeme_count += 1

                if lexeme_count >= top_n:
                    break

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                continue
            except Exception as e:
                print(f"Unexpected error processing lexeme: {e}")
                continue

    return lexemes_data

# Usage example
if __name__ == "__main__":
    lexeme_file = 'latest-lexemes.json.bz2'
    metadata_file = 'lexeme_form_metadata.json'

    merged_data = parse_lexeme_dump_with_metadata(lexeme_file, metadata_file, top_n=1)
    print(json.dumps(merged_data, indent=2, ensure_ascii=False))