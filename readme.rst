silex
=====

- `English (en) <#wildfire-prediction-software>`_
- `Français (fr) <#logiciels-de-prédiction-de-feux-de-forêt>`_


Wildfire Prediction Software
----------------------------

This repository presents wildfire modelling technologies.


Empirical Models
++++++++++++++++

**Empirical** wildfire modelling tools are based on **observations**.
Researchers analyze how wildfires behave and write programs that approximate
these fires to forecast their evolution.

Examples of empirical wildfire modelling tools:

- :ref:`BehavePlus <https://research.fs.usda.gov/firelab/products/dataandtools/behaveplus>`
- :ref:`FlamMap <https://research.fs.usda.gov/firelab/products/dataandtools/flammap>`
- :ref:`FARSITE (now part of FlamMap) <https://research.fs.usda.gov/firelab/products/dataandtools/farsite>`

These tools rely on multiple types of data and combine several models to
simulate the complexity of wildfires appropriately. The file
:ref:`forecast.ipynb` presents databases and models used to forecast wildfires
and explains how to run FARSITE simulations on your own system. You'll need
:ref:`Anaconda <https://www.anaconda.com/download>` to run the notebook.


Chaos Visualization
+++++++++++++++++++

Wildfires and meteorological phenomena are highly sensitive to small effects,
like small differences in temperature, which can dramatically change how they
evolve. This sensitivity is called *chaos*. To visualize this effect, refer to
the file :ref:`chaos/readme.rst`.


Logiciels de prédiction de feux de forêt
----------------------------------------


