## Serial-EMD

### Introduction

This is the paper "Serial-EMD: Fast Empirical Mode Decomposition Method for Multi-Signals Based on Serialization" with both Python and Matlab implementation.

This method can process multi-dimensional signals with standard EMD or other one-dimensional EMD variations (EEMD, CEEMDAN) at very fast speed.

For more information, please visit our paper: 

### Installation

The source is available on GitHub. To download the code you can either go to the source code page and click `Code -> Download ZIP`, or use git command line

`$ git clone https://github.com/ffbear1993/serial-emd.git`

We provide two implementations, python version and matlab version.

#### PYTHON Version

###### Environment:

python 3.6 or above.

numpy

PyEMD <https://github.com/laszukdawid/PyEMD>, which provide many EMD variations that work well with our code. 

#### MATLAB Version

###### Environment:

MATLAB R2018b or above, which provide the default emd function. For eemd or ceemdan, please visit the following site:

- eemd: <https://github.com/HirojiSawatari/EEMD-Project>
- ceemdan: <https://github.com/helske/Rlibeemd>

or you can contact us to get these methods' source code.

### Example

More experiments are detailed in our paper, in source code, we provide a toy example to show how to use our serial-EMD.

The whole serial-EMD consists of three phase:

![](https://github.com/ffbear1993/serial-emd/blob/main/pics/semd_framework.png)





