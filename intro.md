# How We Recreated the Analysis of the COMPAS Recidivism Algorithm
The following book consists of Jasper and Alex's reproduction and extension of the ProPublica report [Machine Bias](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing). If you would like to see what exactly we are repoducing, we reccomend opening the page Original Analysis alongside each chapter of reproduced analysis.

The orginal report stated:

>Our analysis found that:
>
>Black defendants were often predicted to be at a higher risk of recidivism than they actually were. Our analysis found that black defendants who did not recidivate over a two-year period were nearly twice as likely to be misclassified as higher risk compared to their white counterparts (45 percent vs. 23 percent).
>
>White defendants were often predicted to be less risky than they were. Our analysis found that white defendants who re-offended within the next two years were mistakenly labeled low risk almost twice as often as black re-offenders (48 percent vs. 28 percent).
The analysis also showed that even when controlling for prior crimes, future recidivism, age, and gender, black defendants were 45 percent more likely to be assigned higher risk scores than white defendants.
>
>Black defendants were also twice as likely as white defendants to be misclassified as being a higher risk of violent recidivism. And white violent recidivists were 63 percent more likely to have been misclassified as a low risk of violent recidivism, compared with black violent recidivists.
>
>The violent recidivism analysis also showed that even when controlling for prior crimes, future recidivism, age, and gender, black defendants were 77 percent more likely to be assigned higher risk scores than white defendants.

During our recreation of this analysis we found:

>**Recreation**
>Black defendants, who do not recidivise within 2 years, are 91.21% more likely to receive a High COMPAS score (false positive) than white defendants.
>
>White defendants, who do recidivise within 2 years, are 70.53% more likely to receive a Low COMPAS score (false negative) than black defendants.
>
>Black defendants, who do not violently recidivise within 2 years, are 114.76% more likely to receive a High Violence COMPAS score (false positive) than white defendants.
>
>White defendants, who do violently recidivise within 2 years are, 88.79% more likely to receive a Low Violence COMPAS score (false negative) than black defendants.
>
>When controlling for for prior crimes, future recidivism, age, and gender, black defendants are still 61% more likely to receive a high score than white defendants.
>
>When controlling for for prior crimes, future recidivism, age, and race, female defendants are still 24% more likely to receive a high score than male defendants.
>
>When controlling for for prior crimes, future recidivism, race, and gender, defendants aged 25 or under are still 270% more likely to receive a high score than defendants aged 25-45.
>
>When controlling for for prior crimes, future recidivism, race, and gender, black defendants are 74% less likely to receive a high score than defendants aged 25-45.
>
>**Extension**