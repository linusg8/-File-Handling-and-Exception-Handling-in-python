def read_and_modify_file(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, "r") as initialfile:
            content = initialfile.read()  # Read the content of the file
            
        # Modify the content (for example, convert it to uppercase)
        modified_content = content.lower()  # Modify content (you can customize this)
        
        # Open the output file for writing
        with open(output_filename, "w") as modifiedfile:
            modifiedfile.write(modified_content)  # Write the modified content to a new file
        
        print(f"Content has been read from '{input_filename}' and written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read or write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for the filename
input_filename = input("Please enter the input filename to read from: ")
output_filename = input("Please enter the output filename to write to: ")

# Call the function to read, modify, and write the file
read_and_modify_file(input_filename, output_filename)
