from collections import Counter


def main():
    with open('Training_01.txt', 'r') as open_file:
        line = open_file.readline()
        line_elements = []
        while line:
            line_elements.append(line.split('/'))
            line = open_file.readline()
        number_of_images = len(line_elements)
        categories = [line_elements[i][2] for i in range(len(line_elements))]
        number_of_categories = len(set(categories))
        images_per_category = Counter(categories)
        print(f"There are {number_of_images} images in {number_of_categories} categories.")
        print(f"Number of images in each category:")
        for category, count in images_per_category.items():
            print(f"{category}: {count}")


if __name__ == "__main__":
    main()
