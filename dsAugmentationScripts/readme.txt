Command samples:

1. Downsample by 2x2
python3 applyFilter.py -d ../dataset/img_align_celeba -o ../dataset/downsample_2_2/ -p 2 -q 2 -f 0

2. Downsample by 4x4
python3 applyFilter.py -d ../dataset/img_align_celeba -o ../dataset/downsample_4_4/ -p 4 -q 4 -f 0

3. Downsample by 2x4
python3 applyFilter.py -d ../dataset/img_align_celeba -o ../dataset/downsample_2_4/ -p 2 -q 4 -f 0

4. Downsample by 4x2
python3 applyFilter.py -d ../dataset/img_align_celeba -o ../dataset/downsample_4_2/ -p 4 -q 2 -f 0

5. Blur 2x2
python3 applyFilter.py -d ../dataset/img_align_celeba -o ../dataset/blur_2/ -f 1 -r 2

6. blur 3x3
python3 applyFilter.py -d ../dataset/img_align_celeba -o ../dataset/blur_3/ -f 1 -r 3


Barrel / fish eye lens distortion read:
https://stackoverflow.com/questions/2589851/how-can-i-implement-a-fisheye-lens-effect-barrel-transformation-in-matlab


