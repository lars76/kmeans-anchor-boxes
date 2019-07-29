import glob
import xml.etree.ElementTree as ET

import numpy as np

from kmeans import kmeans, avg_iou

ANNOTATIONS_PATH = "Annotations"
CLUSTERS = 5

def load_dataset(path):
	dataset = []
	for xml_file in glob.glob("{}/*xml".format(path)):
		tree = ET.parse(xml_file)

		height = int(tree.findtext("./size/height"))
		width = int(tree.findtext("./size/width"))

		for obj in tree.iter("object"):
			xmin = int(obj.findtext("bndbox/xmin"))*1.0 / width
			ymin = int(obj.findtext("bndbox/ymin"))*1.0 / height
			xmax = int(obj.findtext("bndbox/xmax"))*1.0 / width
			ymax = int(obj.findtext("bndbox/ymax"))*1.0 / height
			if xmin==xmax or ymin==ymax:
				print("you need to check {}".format(xml_file))
				continue

			dataset.append([xmax - xmin, ymax - ymin])

	return np.array(dataset)


data = load_dataset(ANNOTATIONS_PATH)
out = kmeans(data, k=CLUSTERS)
print("Accuracy: {:.2f}%".format(avg_iou(data, out) * 100))
print("Boxes:\n {}".format(out))

ratios = np.around(out[:, 0] / out[:, 1], decimals=2).tolist()
print("Ratios:\n {}".format(sorted(ratios)))
