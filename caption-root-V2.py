import os
from pathlib import Path

def create_caption_files():
    # Get the caption root from user
    caption_root = input("Please enter the caption root phrase: ")
    
    # Get current directory
    current_dir = Path.cwd()
    
    # Counters for processed files
    image_count = 0
    video_count = 0
    
    # Define supported file extensions
    image_extensions = ['.png', '.jpg', '.jpeg']
    video_extensions = ['.mp4']
    supported_extensions = image_extensions + video_extensions
    
    # Iterate through files in current directory
    for file_path in current_dir.glob('*'):
        # Check if file is a media file with supported extension
        if file_path.suffix.lower() in supported_extensions:
            # Create matching text filename
            text_file_path = file_path.with_suffix('.txt')
            
            # Write caption root to text file
            with open(text_file_path, 'w', encoding='utf-8') as f:
                f.write(caption_root)
            
            # Update appropriate counter
            if file_path.suffix.lower() in image_extensions:
                image_count += 1
                file_type = "image"
            elif file_path.suffix.lower() in video_extensions:
                video_count += 1
                file_type = "video"
            
            print(f"Created caption file for {file_type}: {text_file_path.name}")
    
    # Print summary
    print(f"\nProcessing complete!")
    print(f"Total image files processed: {image_count}")
    print(f"Total video files processed: {video_count}")
    print(f"Total media files processed: {image_count + video_count}")
    
if __name__ == "__main__":
    try:
        create_caption_files()
    except Exception as e:
        print(f"An error occurred: {str(e)}")