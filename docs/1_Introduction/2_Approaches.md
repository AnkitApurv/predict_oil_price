# Approaches

## Manual Estimation

### Steps Involved - Manual Estimation

- Making a list of factors which we believe affect oil prices in realtime this largely involves independent research and educated guesses.
- ?

## Automated Predictions

### Steps Involved - Automated Predictions

- Same as the first step of the [Steps Involved in Manual Estimation](#steps-involved---manual-estimation)
- Building sufficiently reliable regression model to identify the actually important factors and their impact relative to each other (Feature Importance).
- Building a two-staged transfer learning model for doing automated predictions. This model will need to be periodically refreshed.
    - Stage 1 - Regression model trained on important features identified via previous stage's regression model.
    - Stage 2 - Time-series extrapolation model for predicting the prices day-to-day.

#### Reason for the two stage model approach

- Availability and granularity of data vis-a-vis time.
    - Data such as prices can be available minute-by-minute.
    - Data such as tanker rents and transportation insurance may be available as averaged over a financial year.
    - Sets of buyers and sellers changing over a course of few months/few years.

Though all such factors will have an impact, such factors do not change in the same span of time, nor are they all recorded within same granularity of time.

Hence, accounting for all such factors require such an approach.
