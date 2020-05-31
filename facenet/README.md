The 5-Celeb.ipynb is a tutorial on using facenet using a small 5-person dataset.  You can run through this notebook to get a feel for using
the facenet model for facial recognition.

The Celeb1-A.ipynb notebook is our notebook which uses a pretrained facenet model on a 
a 1000-person subset of the Celeb1-A dataset. 



  Model        |  HR  |  ds2x |  ds4x  |  ds6x  | blur3x 
---------------|------------|-----------------|------------------|------------|-----------
Model-HR       |   92.9%    |   88.8%         |     31.2%        |     79.3%  |  26.5%
Model-ds2x     |   93.0%    |   90.9%         |     38.3%        |     82.5%  |  33.5%
Model-ds4x     |   82.2%    |   79.2%         |     57.5%        |     70.8%  |  32.5%
Model-ds6x     |   91.2%    |   87.7%         |     35.2%        |     85.2%  |  41.0%
Model-blur3x   |   78.7%    |   73.3%         |     33.3%        |     75.8%  |  60.37


