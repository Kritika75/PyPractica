import demoji

#initialize demoji
demoji.download_codes()

def emoji_to_text_converter(input_text):
    """ 
    convert emojis in a string to their textual representation
    
    """
    converted_text = demoji.replace(input_text, "")
    emoji_descriptions = demoji.findall(input_text)
    
    if emoji_descriptions:
        print("\nConverted Descriptions:")
        for emoji, desc in emoji_descriptions.items():
            print(f"{emoji} -> {desc}")
            
    return converted_text

if __name__ == "__main__":
    print("Welcome to the Emoji to Text Converter!")
    user_input = input("Enter a string with emojis: ")
    
    #convert emojis
    result = emoji_to_text_converter(user_input)
    
    print("\nOriginal Text:")
    print(user_input)
    
    print("\nText without emojis:")
    print(result)
    
    
