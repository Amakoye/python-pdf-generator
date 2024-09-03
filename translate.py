import pandas as pd

# Load the Excel file
file_path = "./translate.xlsx"  # Change this to the path of your Excel file
excel_data = pd.read_excel(file_path)


def generate_translation_object(df):
    translations = {}
    for _, row in df.iterrows():
        en_text = row.iloc[0]
        pt_text = row.iloc[1]

        # Ensure the values are strings
        if isinstance(en_text, str) and isinstance(pt_text, str):
            key = en_text.lower()
            translations[key] = {"en": en_text, "pt": pt_text}

    return translations


# Generate the translation object
translations = generate_translation_object(excel_data)

# Construct the final object as a string
translation_object_str = "const IND3943064 = {\n  report: {\n"
for key, value in translations.items():
    translation_object_str += f'    "{key}": customTranslation({{\n      en: "{value["en"]}",\n      pt: "{value["pt"]}"\n    }}),\n'
translation_object_str += "  },\n};\n"

# Print the translation object
print(translation_object_str)

# Save the translation object to a file
with open("translation_object.js", "w") as file:
    file.write(translation_object_str)
