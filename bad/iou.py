
def iou(bbox1, bbox2):
    x1, y1, w1, h1 = bbox1
    x2, y2, w2, h2 = bbox2
    
    area1 = get_area(bbox1)
    area2 = get_area(bbox2)

    if x1 < x2:
        right_bound = x1 + w1 / 2
        left_bound = x2 - w2 / 2
    else:
        right_bound = x2 + w2 / 2
        left_bound = x1 - w1 / 2

    w_inter = right_bound - left_bound

    if y1 < y2:
        lower_bound = y1 + h1 / 2
        upper_bound = y2 - h2 / 2
    else:
        lower_bound = y2 + h2 / 2
        upper_bound = y1 - h1 / 2

    h_inter = lower_bound - upper_bound

    intersection = w_inter * h_inter
    union = area1 + area2 - intersection

    print(w_inter, h_inter)
    print(intersection, union)
    return intersection / union

def get_area(bbox):
    x, y, w, h = bbox
    return w * h



b1 = (1, 1, 3, 3)
b2 = (3, 2, 5, 1)
iou(b1, b2)