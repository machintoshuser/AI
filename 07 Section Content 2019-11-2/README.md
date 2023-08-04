# section7-2019fall-dask

### Agenda:
- Dask examples
- Pytorch package for Pset4

### Key points/notes for facilitating:

#### section7-2019fall-dask/dask_basics.ipynb
- What is pandas? Pandas is basically a way to manipulate tabular data, similiar to dataframes in R
- What is Dask? Dask can be thought of as many pandas dataframes/numpy arrays
- Parquet files: creates a folder directory with multiple parquet parts. Also has metadata files which act like a schema for the data
- Calling compute on a dask dataframe creates a pandas dataframe
- Dask dataframes can also read directly from S3 as long as you pass in the credentials (I think possible for pandas as well)
- Map partitions -- applies a function onto each of the dataframe partitions

#### section7-2019fall-dask/dask_example_1.ipynb
- You could potentially work with data that is too large to fit into memory
- Dask provides a delayed operation -- not actually calculated until you say so
- Dask visualize provides a task graph-esque view

#### section7-2019fall-dask/dask_example_2.ipynb
- Some other potentially useful tools, like progressbar to view time to code completition
- Client to access an interface to see operations in action. Distributed also for distributed training
- (Throughout this example I'll do htop to view cpu core utilization)

#### section7-2019fall-dask/dask_example_3.ipynb
- Support exists for Xgboost algorithms and some other scikit-learn type models
- Modin, a project specifically built to speed up pandas
- CUDF, or dataframes on GPU developed by nvidia
