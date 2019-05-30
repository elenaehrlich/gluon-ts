# GluonTS - Probabilistic Time Series Modeling in Python

GluonTS is a Python toolkit for probabilistic time series modeling,
built around [MXNet](https://mxnet.incubator.apache.org/).

GluonTS provides utilities for loading and iterating over time series datasets,
state of the art models ready to be trained, and building blocks to define
your own models and quickly experiment with different solutions.

## Installation

GluonTS requires that you have Python 3.6 installed, and the easiest
way to install it is via `pip`:

```bash
pip install gluonts
```

## Contributing

If you wish to contribute to the project, please refer to our
[contribution guidelines](/CONTRIBUTING.md).

## Quick start guide

This simple example illustrates how to train a model from GluonTS on some data,
and then use it to make predictions. As a first step, we need to collect
some data: in this example we will use the volume of tweets mentioning the
AMZN ticker symbol. For convenience, we resample the data to get a regular
frequency of 5 minutes.

```python
import pandas as pd
url = "https://raw.githubusercontent.com/numenta/NAB/master/data/realTweets/Twitter_volume_AMZN.csv"
df = pd.read_csv(url, header=0, index_col=0)
```

The first 200 data points look like follows:

```python
import matplotlib.pyplot as plt
df[:100].plot(linewidth=2)
plt.grid(which='both')
plt.show()
```

![Data](docs/figures/Tweets_AMZN_data.png)

We can now prepare a training dataset for our model to train on.
Datasets in GluonTS are essentially iterable collections of
dictionaries: each dictionary represents a time series
with possibly associated features. For this example, we only have one
entry, specified by the `"start"` field which is the timestamp of the
first datapoint, and the `"target"` field containing time series data.
For training, we will use data up to midnight on April 5th, 2015.

```python
from gluonts.dataset.common import ListDataset
training_data = ListDataset(
    [{"start": df.index[0], "target": df.value[:"2015-04-05 00:00:00"]}],
    freq = "5min"
)
```

A forecasting model in GluonTS is a *predictor* object. One way of obtaining
predictors is by training a correspondent *estimator*. Instantiating an
estimator requires specifying the frequency of the time series that it will
handle, as well as the number of time steps to predict. In our example
we're using 5 minutes data, so `freq="5min"`,
and we will train a model to predict the next hour, so `prediction_length=12`.
We also specify some minimal training options.

```python
from gluonts.model.deepar import DeepAREstimator
from gluonts.trainer import Trainer

estimator = DeepAREstimator(freq="5min", prediction_length=12, trainer=Trainer(epochs=10))
predictor = estimator.train(training_data=training_data)
```

During training, useful information about the progress will be displayed.
To get a full overview of the available options, please refer to the
documentation of `DeepAREstimator` (or other estimators) and `Trainer`.

We're now ready to make predictions: we will forecast the hour following
the midnight on April 15th, 2015, and compare it to what was actually
observed in that time range:

```python
test_data = ListDataset(
    [{"start": df.index[0], "target": df.value[:"2015-04-15 00:00:00"]}],
    freq = "5min"
)

from gluonts.dataset.util import to_pandas

for test_entry, forecast in zip(test_data, predictor.predict(test_data)):
    to_pandas(test_entry)[-60:].plot(linewidth=2)
    forecast.plot(color='g', confidence_intervals=[50., 90.])
plt.grid(which='both')
```

![Forecast](docs/figures/Tweets_AMZN_forecast.png)

Note that the forecast is displayed in terms of a probability distribution:
the shaded areas represent the 50% and 90% prediction intervals, respectively,
centered around the median (dark green line).

## Further examples

The following modules are good entry-points to understand how to use
other features of GluonTS:

* [`examples.evaluate_model`](examples/evaluate_model.py): how to train a model and compute evaluation metrics.
* [`examples.benchmark_m4`](examples/benchmark_m4.py): how to evaluate and compare multiple models on multiple datasets. 
* [`gluonts.model.seasonal_naive`](gluonts/model/seasonal_naive): how to implement simple models using just NumPy and Pandas.
* [`gluonts.model.simple_feedforward`](gluonts/model/simple_feedforward): how to define a trainable, Gluon-based model.