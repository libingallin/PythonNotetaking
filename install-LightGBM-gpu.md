# 在 ubuntu 16.04 上安装 LightGBM gpu版

1.  安装相关的依赖（见[官网](https://lightgbm.readthedocs.io/en/latest/GPU-Tutorial.html)，这里省略）

2.  安装LGBM，在某个目录（It's up to u.）下:

    ```bash
    git clone --recursive https://github.com/microsoft/LightGBM
    cd LightGBM
    mkdir build
    cd build
    # cmake -DUSE_GPU=1 ..
    # 由于服务器上cuda位置不是默认(我是cuda-10.0)的，因此使用了下面这个命令
    # if you have installed NVIDIA CUDA to a customized location, you should specify paths to OpenCL headers and library like the following:
    cmake -DUSE_GPU=1 -DOpenCL_LIBRARY=/usr/local/cuda-10.0/lib64/libOpenCL.so -DOpenCL_INCLUDE_DIR=/usr/local/cuda-10.0/include/ ..
    make -j$(nproc)
    cd ..
    ```

    可以看到新生成了2个二进制文件—— `lightgbm` 和 `lib_lightgbm.so`。

    ```bash
    cd python-package/
    # 因为我是在conda env中
    python setup.py install --precompile
    ```

    不出意外就可以了。

3. 测试

  ```bash
  git clone https://github.com/guolinke/boosting_tree_benchmarks.git
  cd boosting_tree_benchmarks/data
  wget "https://archive.ics.uci.edu/ml/machine-learning-databases/00280/HIGGS.csv.gz"
  gunzip HIGGS.csv.gz
  python higgs2libsvm.py
  ```
  
  新建一个`test.py`文件，使用以下代码：
  
  ```python
  import lightgbm as lgb
  import time
  
  
  params = {'max_bin': 63,
  'num_leaves': 255,
  'learning_rate': 0.1,
  'tree_learner': 'serial',
  'task': 'train',
  'is_training_metric': 'false',
  'min_data_in_leaf': 1,
  'min_sum_hessian_in_leaf': 100,
  'ndcg_eval_at': [1,3,5,10],
  'sparse_threshold': 1.0,
  'device': 'gpu',
  'gpu_platform_id': 0,
  'gpu_device_id': 2,  # 因为有4块卡
  'num_threads': 35}  # 这个比较关键
  
  
  dtrain = lgb.Dataset('data/higgs.train')
  t0 = time.time()
  gbm = lgb.train(params, train_set=dtrain, num_boost_round=10,
            valid_sets=None, valid_names=None,
            fobj=None, feval=None, init_model=None,
            feature_name='auto', categorical_feature='auto',
            early_stopping_rounds=None, evals_result=None,
            verbose_eval=True,
            keep_training_booster=False, callbacks=None)
  t1 = time.time()
  
  print('gpu version elapse time: {}'.format(t1-t0))
  
  
  params = {'max_bin': 63,
  'num_leaves': 255,
  'learning_rate': 0.1,
  'tree_learner': 'serial',
  'task': 'train',
  'is_training_metric': 'false',
  'min_data_in_leaf': 1,
  'min_sum_hessian_in_leaf': 100,
  'ndcg_eval_at': [1,3,5,10],
  'sparse_threshold': 1.0,
  'device': 'cpu'
  }
  
  t0 = time.time()
  gbm = lgb.train(params, train_set=dtrain, num_boost_round=10,
            valid_sets=None, valid_names=None,
            fobj=None, feval=None, init_model=None,
            feature_name='auto', categorical_feature='auto',
            early_stopping_rounds=None, evals_result=None,
            verbose_eval=True,
            keep_training_booster=False, callbacks=None)
  t1 = time.time()
  
  print('cpu version elapse time: {}'.format(t1-t0))
  ```
  
  ```bash
  python test.py
  ```
  
  出现如下字段表示成功：
  
  ```markdown
  [LightGBM] [Info] This is the GPU trainer!!
  [LightGBM] [Info] Total Bins 1524
  [LightGBM] [Info] Number of data: 10500000, number of used features: 28
  [LightGBM] [Info] Using requested OpenCL platform 0 device 2
  [LightGBM] [Info] Using GPU Device: GeForce RTX 2080 Ti, Vendor: NVIDIA Corporation
  [LightGBM] [Info] Compiling OpenCL Kernel with 64 bins...
  [LightGBM] [Info] GPU programs have been built
  [LightGBM] [Info] Size of histogram bin entry: 12
  ....
  ....
  ```
  
  
  
    