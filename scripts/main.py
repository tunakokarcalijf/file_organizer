from file_organizer import FileOrganizer


def main():
    path = "/"
    organizer = FileOrganizer(path)

    print("Organizing files...")
    organizer.organize_files()

    # To undo the organization:
    # print("Undoing file organization...")
    # organizer.undo_organize_files()

    print("\nListing files by category...")
    files_by_category = organizer.list_files_by_category()
    for category, files in files_by_category.items():
        print(f"{category}:")
        for file in files:
            print(f"  {file}")


if __name__ == "__main__":
    main()
