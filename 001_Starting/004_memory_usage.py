# Define a function to generate a large string
def generate_large_string(size_mb):
    # 1 MB is approximately 1 million characters
    # So, to generate 'size_mb' MB string, we need 'size_mb' * 1000000 characters
    large_string = 'a' * (size_mb * 1000000)
    return large_string

# Specify the size of the string in MB
size_mb = 100  # You can adjust this value to consume more or less memory

# Generate a large string
large_string = generate_large_string(size_mb)

# Print a message to indicate that the program has executed
print("Program has created a large string which consumes around", size_mb, "MB of memory.")

