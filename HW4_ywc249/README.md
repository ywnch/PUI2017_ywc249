# README for HW 4

### Yuwen Chang (ywc249)

## Objectives
1. Learn to determine the appropriate test for a hypothesis.
2. Learn to read hypothesis testing settings and outputs in research papers.
3. Reproducing a z test and a $\chi^2$ test.
4. Conducting KS and correlation tests and understand their statistical meanings.

## HW 4-2
| Statistical Analyses | IV(s) | IV Type(s) | DV(s) | DV Type(s) | Control Var | Control Var Type | Question to be answered | _H0_ | alpha | Link to paper |
|:-:|:--|:--|:--|:--|:--|:--|:--|:--:|:--:|:--|
|ANOVA| arsenic level, smoking prevalence, median income | continuous, continuous, continuous | lung cancer incidence rate (log-transformed only for interpretation) | continuous | n/a | n/a | Are there two-way interactions between the predictors used in the regression analyses | There is no difference in effect of based on different IV combinations (no interactions) | 0.05 | [Association of Arsenic Exposure with Lung Cancer Incidence Rates in the United States](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0025886) |
| Multiple Regression (Poisson) | arsenic level (single predictor) | continuous | lung cancer incidence rate (natural log) | continuous | smoking prevalence, median income | continuous, continuous | What is the influence of exposure levels of arsenic on lung cancer incidence in the U.S. | Sediment levels of arsenic is not associated with an increase in incident cases of lung cancer | 0.05 | [Association of Arsenic Exposure with Lung Cancer Incidence Rates in the United States](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0025886) |
| Logistic Regression | age, gender, CCI*, hospital volume, surgeon volume, and LOS | continuous, categorical, continuous, ordinal, ordinal, continuous | In-hospital Mortality | dichotomous | n/a | n/a | What is the odds probability of In-hospital Mortality occuring as the value of IVs Change | n/a, it's a accuracy comparison research with a different approach | 0.05 | [Comparison of Artificial Neural Network and Logistic Regression Models for Predicting In-Hospital Mortality after Primary Liver Cancer Surgery](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0035781) |

* CCI = Charlson co-morbidity index (Predicts 10-year survival in patients with multiple comorbidities.)
* LOS = length of stay

## Work collaboration
### HW 4-1 & 4-2
Worked independently.

### HW 4-3 & 4-4
Worked independently.