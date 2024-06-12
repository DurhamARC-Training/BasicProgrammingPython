Setting up a conda environment for this document

```
conda create -n python_intro -c conda-forge jupyter jupyterlab_rise
```

then start normally via local JupyterLab by calling `jupyter lab`

Convert to pdf.
1. Run cells you want to run
2. Be sure to save
3. Call `jupyter nbconvert --to slides --post serve .\Basics.ipynb`
4. Go to http://localhost:8000/Basics.slides.html?print-pdf#/
5. Print via Print to PDF function of your browser