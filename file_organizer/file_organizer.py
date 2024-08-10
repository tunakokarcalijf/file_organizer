import shutil
from file_organizer.constants import Extensions
from typing import Dict, List
from pathlib import Path


class FileOrganizer:
    def __init__(self, base_directory: str, include_hidden: bool = False):
        self.base_directory = Path(base_directory)
        self.include_hidden = include_hidden
        self.ensure_base_directory_exists()
        self.file_mapping = {}
        self.created_dirs = set()

    def ensure_base_directory_exists(self):
        if not self.base_directory.exists():
            self.base_directory.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def categorize_file(file_path: Path) -> str:
        ext = file_path.suffix.lower()

        for category, exts in Extensions.__dict__.items():
            if isinstance(exts, dict):
                for subcat, exts_list in exts.items():
                    if ext in exts_list:
                        return f"{category}/{subcat}".lower()
            elif isinstance(exts, list):
                if ext in exts:
                    return category.lower()

        return "other"

    def move_file(self, file_path: Path, category: str):
        original_location = file_path
        category_dir = self.base_directory / category
        category_dir.mkdir(parents=True, exist_ok=True)

        if category_dir not in self.created_dirs:
            self.created_dirs.add(category_dir)

        new_location = category_dir / file_path.name

        self.file_mapping[file_path] = original_location

        shutil.move(str(file_path), new_location)

    def organize_files(self):
        pattern = "*" if self.include_hidden else "[!.]*"

        for item in self.base_directory.rglob(pattern):
            if item.is_file():
                category = self.categorize_file(item)
                self.move_file(item, category)
            elif item.is_dir() and not self.include_hidden:
                print(f"Skipping directory: {item.name}")

    def undo_organize_files(self):
        for moved_file, original_location in self.file_mapping.items():
            if moved_file.exists():
                shutil.move(str(moved_file), str(original_location))
                self.file_mapping.pop(moved_file)

        self.cleanup_empty_dirs(self.base_directory)

    def cleanup_empty_dirs(self, dir_path: Path):
        for subdir in dir_path.iterdir():
            if subdir.is_dir():
                self.cleanup_empty_dirs(subdir)
                try:
                    subdir.rmdir()
                except OSError:
                    pass

    def list_files_by_category(self) -> Dict[str, List[str]]:
        categorized_files = {}

        pattern = "*" if self.include_hidden else "[!.]*"

        for item in self.base_directory.rglob(pattern):
            if item.is_file():
                category = self.categorize_file(item)
                if category not in categorized_files:
                    categorized_files[category] = []
                categorized_files[category].append(item.name)

        return categorized_files
