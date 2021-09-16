## Serial-EMD

### Introduction

This is the paper "Serial-EMD: Fast Empirical Mode Decomposition Method for Multi-Signals Based on Serialization" with both Python and Matlab implementation.

This method can process multi-dimensional signals with standard EMD or other one-dimensional EMD variations (EEMD, CEEMDAN) at very fast speed.

For more information, please visit our paper: https://doi.org/10.1016/j.ins.2021.09.033

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

#### Concatenate Phase:

In this phase, the original multi-dimensional signals will be concatenated from head to tail for each signal with a proper transition. Thus, a parameter `num_interval` must be setting at the beginning.

#### Decomposition Phase:

In this phase, the concatenated signal will be decomposed by EMD/EEMD/CEEMDAN or other variations. Currently, the decomposition for python version code and for matlab version code are different. This is because the default parameter values of the EMD function in matlab is different from the default value of EMD in python. Thus, you must specify the EMD parameters clearly. Or you can execute these three phases in python and matlab environment, respectively. For example, you can execute the concatenate phase and deconcatenate phase in python environment, but use EMD function in matlab to get the serialized/concatenated-imfs.

#### Deconcatenate Phase:

In this phase, the concatenated imfs will be deconcatenated to generate imfs for each signal.

#### Results:

###### IMFs Quality:

Here we show the imfs results for different EMD variants and serial-EMD variants. You can see the decomposition results are similar among these method.

![](https://github.com/ffbear1993/serial-emd/blob/main/pics/semd_result.png)

###### Computation Performance:

Here we show the execution time results for different EMD variants and serial-EMD variants, corresponding to the previous IMFs quality results.

![](https://github.com/ffbear1993/serial-emd/blob/main/pics/semd_time_result.png)

### Contact

Feel free to contact me with any questions, requests. It's always nice to know that I've helped someone or made their work easier. Contributing to the project is also acceptable and warmly welcomed.

#### Citation

If you found this package useful please cite it in your work using the following structure:

```
@article{ZHANG2021,
title = {Serial-EMD: Fast Empirical Mode Decomposition Method for Multi-dimensional Signals Based on Serialization},
journal = {Information Sciences},
year = {2021},
issn = {0020-0255},
doi = {https://doi.org/10.1016/j.ins.2021.09.033},
url = {https://www.sciencedirect.com/science/article/pii/S0020025521009646},
author = {Jin Zhang and Fan Feng and Pere Marti-Puig and Cesar F. Caiafa and Zhe Sun and Feng Duan and Jordi Sol{\'e}-Casals},
keywords = {Empirical mode decomposition, Signal serialization}
}
```





 





