# recsys-comparison
Comparison and analysis of recommendation systems included in LensKit for several datasets.

## Introduction

Initial setup is taken from [eval-quickstart](https://github.com/lenskit/eval-quickstart/tree/20230abcedaf25042325f65d5c1c2bf28ae7e0c3) (couldn't merge/pr/fork into an existing repo, so I just pushed the code.)

### How to run

To run a model, just run 

`./gradlew evaluate`. 

To change the dataset, modify line 9 of `build.gradle`. You can process results with `./gradlew analyzeResults`, which will run the ipython notebook and generate an HTML page or just supply dataset parameter

`./gradlew  -Pdataset=movielens evaluate`.

### How to analyze

To run a model, just run 

`./gradlew analyzeResults`.

or selecting dataset

`./gradlew -Pdataset=movielens analyzeResults`. 

Results are under build/results/[dataset].

### How to add new datasets

New datasets can easily be added:  

1. Configure a `.yml` file and put it under `data/`. You can use the other files as a template. In essence, you just need to specify the file which will hold the data once the zip has been downloaded and decompressed (gradle takes care of the two latter tasks).
2. Add the dataset name to the list of possible datasets, in line 8 of `build.gradle`. Change line 9 if you want to use the new datasets.
3. Modify the `fetchData` task on `build.gradle` to download the new dataset. Just copy the code and change the variable values.
4. Do the same with the `crossfold` task so it runs the right `.yml` file.   
5. Remember to add the new data directory to `.gitignore` so that git doesn't pick up any large files.

### How to add new algorithms

In a similar fashion:   

1. Add a new groovy configuration file for the algorithm under `algorithms/`.  
2. Add the new algorithm in the `evaluate` task in `build.gradle`.

## References: 

· [Said, A & Bellogin, A: Comparative Recommender System Evaluation: Benchmarking Recommendation Frameworks](https://pdfs.semanticscholar.org/036e/8fb63a82ee26537b514b17a51cc197016e4c.pdfhttps://pdfs.semanticscholar.org/036e/8fb63a82ee26537b514b17a51cc197016e4c.pdf)  
· [Ekstrand, M. D., Lenskit reference](https://md.ekstrandom.net/research/thesis/mde-thesis.pdf)  
· [Ekstrand, M.d. & Riedl, J: When Recommender Systems Fail: Predicting Recommender Failure for Algorithm Selection and Combination](https://md.ekstrandom.net/research/pubs/when-recommenders-fail/https://md.ekstrandom.net/research/pubs/when-recommenders-fail/)  
