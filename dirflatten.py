import argparse
import shutil
import os


if __name__ == '__main__':
	# Get the path form the sshell argument
	parser = argparse.ArgumentParser()
	parser.add_argument(dest='directory', help="The directory to flatten")
	args = parser.parse_args()
	start_path = args.directory

	# Iterate over each sub-directory under the start path
	for subdir in os.listdir(path=start_path):

		# Further iterate over every item under the sub-directory
		for root, dirs, files, in os.walk(os.path.join(start_path, subdir)):

		    # Exclude files that already exist within the current sub-directory to avoid
		    # moving a file that has the same source same as the destination.
		    if root != os.path.join(start_path, subdir):
		        for file in files:

		            # Attempt to move the file under the sub-directory
		            try:
		                shutil.move(os.path.join(root, file), os.path.join(start_path, subdir))

		            # Handle the case if the filename already exists in the destination directory
		            except shutil.Error:

		                # Construct a new filename using the original path
		                new_filename = str(root)
		                new_filename = new_filename.replace("\\", "_")  # Replace '\'s in the file path with underscores
		                new_filename = new_filename.replace("/", "_")   # Replace '/'s in the file path with underscores
		                new_filename = new_filename.replace(" ", "-")   # Replace spaces in the file path with dashes
		                new_filename = new_filename + "_" + file        # Append the original file name to the end

		                # Rename the file with the newly constructed filename
		                os.rename(src=os.path.join(root, file), dst=os.path.join(root, new_filename))

		                # Move the file under the sub-directory
		                shutil.move(os.path.join(root, new_filename), os.path.join(start_path, subdir))

		# After all the file moves are done, iterate over every item under the subdirectory again
		for root, dirs, files, in os.walk(os.path.join(start_path, subdir)):
		    for directory in dirs:
		        # Delete every directory found under the subdirectory (which should all be empty at this point)
		        shutil.rmtree(os.path.join(root, directory))
