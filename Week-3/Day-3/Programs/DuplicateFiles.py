import os
import hashlib

def find_duplicate_files(starting_directory):
	seen_files = {}
	stack = [starting_directory]
	duplicate_files = []

	while len(stack):
		current_path = stack.pop()
		if os.path.isdir(current_path):
			for path in os.listdir(current_path):
				stack.append(os.path.join(current_path, path))
		else:
			file_hash = sample_hash_file(current_path)
			cur_last_time = os.path.getmtime(current_path)
			if file_hash in seen_files:
				last_time, existing_path = seen_files[file_hash]
				if cur_last_time > last_time:
					duplicate_files.append((current_path, existing_path))
				else:
					duplicate_files.append((existing_path, current_path))
					seen_files[file_hash] = (cur_last_time, current_path)
			else:
				seen_files[file_hash] = (cur_last_time, current_path)

	return duplicate_files

def sample_hash_file(path):
	bytes_per_page = 4000
	total_bytes = os.path.getsize(path)
	hashing = hashlib.sha512()

	with open(path, 'rb') as file:
		if total_bytes < bytes_per_page * 3:
			hashing.update(file.read())
		else:
			num_bytes_between_samples = (total_bytes - bytes_per_page * 3) // 2
			for offset_multiplier in range(3):
				start_of_sample = offset_multiplier*(bytes_per_page + num_bytes_between_samples)
				file.seek(start_of_sample)
				sample = file.read(bytes_per_page)
				hashing.update(sample)
	return hashing.hexdigest()

print(find_duplicate_files("F:\Competitive Programming\Week-3\Day-3"))