import os
import shutil
from time import sleep

def current_path():
	cwd = os.getcwd()
	print("Current Working Directory: ", cwd)

def list_contents(cwd):
	print(os.listdir(cwd))

def find_desirables():
	# check directory for file types and then make new directory to move files to
	for x in os.listdir():
		if x.endswith(".mp4"):
			if not os.path.exists('C://Users//Brandon//Pictures//memes//mp4'):
				os.makedirs('C://Users//Brandon//Pictures//memes//mp4')
				print("Directory made for .mp4: 'C://Users//Brandon//Pictures//memes//mp4'")
			else:
				print("Directory for .mp4 already exists: 'C://Users//Brandon//Pictures//memes//mp4'")
			break
	wait()

	for x in os.listdir():
		if x.endswith(".mp3"):
			if not os.path.exists('C://Users//Brandon//Pictures//memes//mp3'):
				os.makedirs('C://Users//Brandon//Pictures//memes//mp3')
				print("Directory made for .mp4: 'C://Users//Brandon//Pictures//memes//mp3'")
			else:
				print("Directory for .mp3 already exists: 'C://Users//Brandon//Pictures//memes//mp3'")
			break
	wait()

	for x in os.listdir():
		if x.endswith(".png"):
			if not os.path.exists('C://Users//Brandon//Pictures//memes//png'):
				os.makedirs('C://Users//Brandon//Pictures//memes//png')
				print("Directory made for .mp4: 'C://Users//Brandon//Pictures//memes//png'")
			else:
				print("Directory for .png already exists: 'C://Users//Brandon//Pictures//memes//png'")
			break
	wait()

	for x in os.listdir():
		if x.endswith(".jpg") or x.endswith(".jpeg"):
			if not os.path.exists('C://Users//Brandon//Pictures//memes//jpg'):
				os.makedirs('C://Users//Brandon//Pictures//memes//jpg')
				print("Directory made for .mp4: 'C://Users//Brandon//Pictures//memes//jpg'")
			else:
				print("Directory for .jpg already exists: 'C://Users//Brandon//Pictures//memes//jpg'")
			break
	wait()

def move_desirables(src_folder):
	for file in os.listdir(src_folder):
		if file.endswith(".mp4"):
			shutil.move(os.path.join(src_folder, file), os.path.join('C://Users//Brandon//Pictures//memes//mp4', file))
			print("File moved...")
		elif file.endswith(".mp3"):
			shutil.move(os.path.join(src_folder, file), os.path.join('C://Users//Brandon//Pictures//memes//mp3', file))
			print("File moved...")
		elif file.endswith(".png"):
			shutil.move(os.path.join(src_folder, file), os.path.join('C://Users//Brandon//Pictures//memes//png', file))
			print("File moved...")
		elif file.endswith(".jpg") or file.endswith(".jpeg"):
			shutil.move(os.path.join(src_folder, file), os.path.join('C://Users//Brandon//Pictures//memes//jpg', file))
			print("File moved...")

def wait():
	print("Please wait...")
	sleep(3)

def main():
	src_folder = 'C://Users//Brandon//Downloads'
	dst_folder = 'C://Users//Brandon//Pictures//memes'
	
	# Print current path
	current_path()

	# Change directory to source
	os.chdir(src_folder)

	# print current path
	current_path()
	wait()

	# list source contents
	list_contents(src_folder)
	wait()

	# interate through source folder for desirables & create respective dst files
	find_desirables()
	
	wait()

	# move desirables to their respective folders
	move_desirables(src_folder)

	print("Program completed...")

if __name__ == "__main__":
	main()