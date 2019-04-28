## :key: win10上安装XGBoost-GPU
1. 找个位置：`git clone --recursive https://github.com/dmlc/xgboost`；
2. 下载[编译文件](http://www.picnet.com.au/blogs/guido/2016/09/22/xgboost-windows-x64-binaries-for-download/)，并放到xgboost/python-package/xgboost中；
3. 在xgboost/python-package/目录下运行`python setup.py install`；
4. 检测`cd xgboost/demo/gpu-acceleration/ || python cover_type.py`。

## :key: Ubuntu上安装XGBoost-GPU
1. 找个位置：`git clone --recursive https://github.com/dmlc/xgboost`；
2. `cd xgboost`, then `mkdir build`, then `cmake .. -DUSE_CUDA=ON` and `make -j4`；
3. `cd xgboost/python-package/`后，运行`sudo apt-get install python-setuptools`和`sudo -s python setup.py install`；
4. 检测`cd xgboost/demo/gpu-acceleration\ || python cover_type.py`。
