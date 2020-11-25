import cv2
import json

test_file = 'test/'

with open('result.json', 'r') as reader:
    jf = json.loads(reader.read())

out = []
c = 1
empty = 0
for i in range(len(jf)):
    filename = jf[i]['filename']
    objects = jf[i]['objects']
    image = cv2.imread(test_file + str(c) + '.png')
    height = image.shape[0]
    width = image.shape[1]

    if len(objects) == 0:
        empty += 1

    img_dict = {'bbox': [], 'score': [], 'label': []}
    for j in range(len(objects)):
        center_x = objects[j]['relative_coordinates']['center_x'] * width
        center_y = objects[j]['relative_coordinates']['center_y'] * height
        w = objects[j]['relative_coordinates']['width'] * width
        h = objects[j]['relative_coordinates']['height'] * height

        bbox = (round(center_y-(h/2)), round(center_x-(w/2)), round(center_y+(h/2)), round(center_x+(w/2)))

        img_dict['bbox'].append(bbox)
        img_dict['score'].append(objects[j]['confidence'])

        if objects[j]['class_id'] == 0:
            class_id = 10
        else:
            class_id = objects[j]['class_id']
        img_dict['label'].append(class_id)
    out.append(img_dict)
    c += 1
print(len(out), empty)
with open('0856630.json', 'w', encoding='utf-8') as f:
    json.dump(out, f)
