# recsys-comparison
Comparison and analysis of recommendation systems included in LensKit for several datasets.

## Introduction

Initial setup is taken from [eval-quickstart](https://github.com/lenskit/eval-quickstart/tree/20230abcedaf25042325f65d5c1c2bf28ae7e0c3) (couldn't merge/pr/fork into an existing repo, so I just pushed the code.)

### How to run

To view a list of possible commands, just run

`./gradlew tasks` 

To evaluate a dataset (e.g. Jester) just pass the dataset by a CLI argument (e.g. `./gradlew evaluate -Pdataset=jester`). This will run the algorithms and on the specified dataset and, if not already done, fetch the data and perform the folds.

Results are under build/results/[dataset].

Once you've processed a few datasets, you can automatically process the results with `./gradlew analyzeAllResults`, which runs the python notebooks and saves the results on an `.html` file.

### Properties
Depending on the size of the dataset and your computer's capacity, you may wish to specify properties such as the maximum heap space available for the Java Virtual Machine or the threads to use during execution. A common `gradle.properties` for this is as follows:

```
System.setProperty('jsse.enableSNIExtension','false');
lenskitMaxMemory=10g
lenskitThreadCount=2
```

We don't push this to the repository for good practice, but you can always keep a customized version in your local version.


### How to add new datasets

New datasets can easily be added:  

1. Configure a `.yml` file and put it under `data/`. You can use the other files as a template. In essence, you just need to specify the file which will hold the data once the zip has been downloaded and decompressed (gradle takes care of the two latter tasks).
2. Configure the variables on the `build.gradle` (mainly zipFile, url and pattern).

### How to add new algorithms

Adding new algorithms is similar:   

1. Add a new groovy configuration file for the algorithm under `algorithms/`.  
2. Add the new algorithm in the `evaluate` task in `build.gradle`.
3. (Optional) Specify the parameters by loading them from a file in the directory `algorithms/parameters/`.

## References: 

· [Said, A & Bellogin, A: Comparative Recommender System Evaluation: Benchmarking Recommendation Frameworks](https://pdfs.semanticscholar.org/036e/8fb63a82ee26537b514b17a51cc197016e4c.pdfhttps://pdfs.semanticscholar.org/036e/8fb63a82ee26537b514b17a51cc197016e4c.pdf)  
· [Ekstrand, M. D., Lenskit reference](https://md.ekstrandom.net/research/thesis/mde-thesis.pdf)  
· [Ekstrand, M.d. & Riedl, J: When Recommender Systems Fail: Predicting Recommender Failure for Algorithm Selection and Combination](https://md.ekstrandom.net/research/pubs/when-recommenders-fail/https://md.ekstrandom.net/research/pubs/when-recommenders-fail/)  
