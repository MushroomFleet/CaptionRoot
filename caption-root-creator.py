import os
from pathlib import Path

def create_caption_files():
    # Get the caption root from user
    caption_root = input("Please enter the caption root phrase: ")
    
    # Get current directory
    current_dir = Path.cwd()
    
    # Counter for processed files
    processed_count = 0
    
    # Iterate through files in current directory
    for file_path in current_dir.glob('*'):
        # Check if file is an image with supported extension
        if file_path.suffix.lower() in ['.png', '.jpg', '.jpeg']:
            # Create matching text filename
            text_file_path = file_path.with_suffix('.txt')
            
            # Write caption root to text file
            with open(text_file_path, 'w', encoding='utf-8') as f:
                f.write(caption_root)
            
            processed_count += 1
            print(f"Created caption file: {text_file_path.name}")
    
    # Print summary
    print(f"\nProcessing complete!")
    print(f"Total image files processed: {processed_count}")
    
if __name__ == "__main__":
    try:
        create_caption_files()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
