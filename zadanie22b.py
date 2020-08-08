with open('Training_01.txt', 'r') as open_file:
    text = open_file.read()

paths = text.split('\n')

paths_elements = [path.split('/') for path in paths]

index2_elements = [paths_elements[i][2] for i in range(len(paths_elements)-1)]

categories = list(dict.fromkeys(index2_elements))

cat_img_num = {i:index2_elements.count(i) for i in index2_elements}

print()
print('There are ', str(len(paths)-1), ' images in ', str(len(categories)), 'categories.', '\n')
print('Number of images in each category can be found below:', '\n')
print('\n'.join('{}: {}'.format(k, v) for k, v in cat_img_num.items()))