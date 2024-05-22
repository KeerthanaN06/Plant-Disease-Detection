import os

def total_files(folder_path):
    num_files = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
    return num_files

# Specify the paths to your image directories
train_files_healthy = "C:\Users\keert\Downloads\dataset\train\Train\Healthy"
train_files_powdery = "C:\Users\keert\Downloads\dataset\train\Train\Powdery"
train_files_rust = "C:\Users\keert\Downloads\dataset\train\Train\Rust"

test_files_healthy = "C:\Users\keert\Downloads\dataset\test\Test\Healthy"
test_files_powdery = "C:\Users\keert\Downloads\dataset\test\Test\Powdery"
test_files_rust = "C:\Users\keert\Downloads\dataset\test\Test\Rust"

valid_files_healthy = "C:\Users\keert\Downloads\dataset\Validation\Validation\Healthy"
valid_files_powdery = "C:\Users\keert\Downloads\dataset\Validation\Validation\Powdery"
valid_files_rust = "C:\Users\keert\Downloads\dataset\Validation\Validation\Rust"

# Print the number of files in each category
print("Number of healthy leaf images in training set:", total_files(train_files_healthy))
print("Number of powdery leaf images in training set:", total_files(train_files_powdery))
print("Number of rusty leaf images in training set:", total_files(train_files_rust))

print("========================================================")

print("Number of healthy leaf images in test set:", total_files(test_files_healthy))
print("Number of powdery leaf images in test set:", total_files(test_files_powdery))
print("Number of rusty leaf images in test set:", total_files(test_files_rust))

print("========================================================")

print("Number of healthy leaf images in validation set:", total_files(valid_files_healthy))
print("Number of powdery leaf images in validation set:", total_files(valid_files_powdery))
print("Number of rusty leaf images in validation set:", total_files(valid_files_rust))
