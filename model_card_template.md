https://github.com/TannerBBlack/Deploying-a-Scalable-ML-Pipeline-with-FastAPI/tree/main
# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
- **Model Name**: Census Income Predictor
- **Version**: 1.0
- **Date**: 2025-03-24

## Intended Use
This model is intended for use by organizations to analyze income levels based on demographic data.

## Training Data
- **Source**: UCI Machine Learning Repository
- **Size**: 32,561 samples
- **Features**: Age, Work Class, Education, Marital Status, Occupation, Relationship, Race, Sex, Hours per Week, Native Country

## Evaluation Data
- **Size**: 16,281 samples
- **Distribution**: Similar to training data, sourced from the UCI Machine Learning Repository
- **Preprocessing**: Standardization and encoding applied to categorical and numerical features

## Metrics
- **Overall Performance**:
- **Precision**: 0.7376
- **Recall**: 0.6237
- **F1 Score**: 0.6759

- **Performance by Feature**:
- **Work Class**: Precision ranges from 0.5862 for Unknown up to 1.0000 for Without-pay and Never-worked
- **Education**: Performance varies widely, with high precision for Doctorate (0.9531) and low for 11th grade (0.2500)
- **Marital Status**: Married people seem to have higher precision than single or divorced people
- **Occupation**: Executive/managerial roles have high F1 scores (0.7816), while farming and fishing roles have lower scores (0.3030)
- **Sex**: Males (F1: 0.6857) perform slightly better than females (F1: 0.6161)
- **Race**: Performance is pretty consistent with White (F1: 0.6756) and Black (F1: 0.6797) having similar scores
- **Native Country**: Some countries have very low recall (Cambodia, Greece), affecting overall performance

## Ethical Considerations
- **Bias & Fairness**: The model may have biases based on race, sex, and country of origin due to disparities in dataset representation.
- **Sensitive Attributes**: Having features like race and sex raises ethical concerns about possible discriminatory conclusions.
- **Potential Misuse**: The model should not be used for decision-making in hiring, lending, or other high-stakes scenarios without bias mitigation measures.

## Caveats and Recommendations
- **Data Imbalance**: Certain categories, such as lesser-represented education levels or occupations, have low sample sizes, affecting predictive performance.
- **Generalization**: The model was trained on a specific dataset and may not generalize well to populations with different demographic distributions.
- **Interpretability**: Users should examine feature importance and conduct fairness audits before deployment.
- **Periodic Review**: Regular updates and audits are recommended to ensure continued fairness and accuracy as demographic and economic conditions evolve.
