&emsp;
# Intro


提到传统目标识别，就不得不提SIFT算法，Scale-invariant feature transform，中文含义就是尺度不变特征变换。此方法由David Lowe于1999年发表于ICCV(International Conference on Computer Vision)，并经过5年的整理和完善，在2004年发表于IJCV(International journal of computer vision)。

由于在此之前的目标检测算法对图片的大小、旋转非常敏感，而 SIFT 算法是一种基于局部兴趣点的算法，因此不仅对图片大小和旋转不敏感，而且对光照、噪声等影响的抗击能力也非常优秀，因此，该算法在性能和适用范围方面较于之前的算法有着质的改变。这使得该算法对比于之前的算法有着明显的优势，所以，一直以来它都在目标检测和特征提取方向占据着重要的地位

&emsp;
## 1 Scale-Space Extrema Detection
- `Gaussian Blurring`: The image is repeatedly blurred with Gaussians at different scales (i.e., different standard deviations).
- `Difference of Gaussians (DoG)`: Images are subtracted from one another after being blurred at adjacent scales to approximate a scale-normalized Laplacian of Gaussian (LoG).
- `Identifying Extrema`: Local maxima and minima of the DoG images are located; these correspond to potential interest points or keypoints.

&emsp;
## 2 Keypoint Localization
- `Refinement`: The detected extrema are refined by removing low-contrast and edge-like points. This helps to locate keypoints more accurately.
- `Orientation Assignment`: Each keypoint is assigned one or more orientations based on local image gradients. This ensures that the descriptor is invariant to image rotation.

&emsp;
## 3 Descriptor Generation
- Descriptor Region: A 16x16 neighborhood around each keypoint is taken and divided into 4x4 sub-blocks.
- Gradient Histogram: Within each sub-block, a histogram of gradients is computed. The gradient magnitudes and directions are quantized into 8 bins.
- Concatenation: The histograms from all 16 sub-blocks are concatenated, resulting in a 128-dimensional feature vector for each keypoint.
- Normalization: The feature vector is normalized to ensure invariance to changes in illumination.

&emsp;
## 4 Keypoint Matching (Optional)
- Distance Measure: If matching keypoints between images, the Euclidean distance between their descriptors can be used.
- Ratio Test: Often, a ratio test is applied to the distances to the nearest and second-nearest neighbor, which can eliminate many incorrect matches.