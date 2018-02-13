# kmeans-anchor-boxes
This repository contains an implementation of k-means clustering with the Intersection over Union (IoU) metric as described in the YOLO9000 paper [1].

## Tests
According to the paper we should get 61.0 avg IoU with 5 clusters and 67.2 avg IoU with 9 clusters on the VOC 2007 data set:

![Table](https://i.imgur.com/DoScgDL.png)

First I tried normal k-means clustering:

![k-means k = 5](https://i.imgur.com/lnHijWm.png)

![k-means k = 9](https://i.imgur.com/w0pePI0.png)

As the plots show the algorithm converges to lower values than expected. To resolve this problem, I changed k-means to not run until convergence. Whenever the values started to drop, the algorithm would start again with different initial means. By doing this for about 50 iterations, an average IoU of about 60 was possible.

However, this didn't seem good enough, because now the algorithm has to run for a long time to find the right values. So I started trying out different initialization methods and variants of k-means clustering. In the end the best results were obtained by just using the median to calculate the new centroids.

![k-medians k = 5](https://i.imgur.com/bxtX4cD.png)

![k-medians k = 9](https://i.imgur.com/ly2OGuj.png)

The end result is about 60.15 for k = 5 and 67.13 for k = 9 on the VOC 2007 data set. If you run the algorithm multiple times, the avg IoU can be higher. I got a few times for example 60.5 for k = 5. The result always depends on the chosen starting points during initialization.

## Usage

To try out the results yourself, download the annotations here: http://host.robots.ox.ac.uk/pascal/VOC/voc2007/. Then change the constant ANNOTATIONS_PATH in test/test_voc2007.py and finally run:

```
python3 -m unittest discover -s tests/
```

## References

[1] J. Redmon and A. Farhadi, “YOLO9000: Better, Faster, Stronger,” 2017 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Jul. 2017.
